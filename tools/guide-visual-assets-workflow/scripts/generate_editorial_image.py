#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Iterable

SUPPORTED_OUTPUT_FORMATS = {"png", "jpeg", "webp"}
DEFAULT_MODEL = "gpt-image-2"
DEFAULT_QUALITY = "medium"
DEFAULT_BASE_URL = "https://api.openai.com/v1"


def load_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_output_format(path: Path) -> str:
    suffix = path.suffix.lower().lstrip(".")
    if suffix == "jpg":
        suffix = "jpeg"
    if suffix not in SUPPORTED_OUTPUT_FORMATS:
        raise ValueError(
            f"Unsupported editorial image extension '.{suffix}'. "
            f"Use one of: {', '.join(sorted(SUPPORTED_OUTPUT_FORMATS))}."
        )
    return suffix


def size_for_spec(spec: dict) -> str:
    explicit = str(spec.get("size", "")).strip()
    if explicit:
        return explicit

    ratio = str(spec.get("aspect_ratio", "3:2")).strip().lower().replace(" ", "")
    landscape = {"3:2", "16:9", "4:3", "landscape", "horizontal"}
    portrait = {"2:3", "9:16", "3:4", "portrait", "vertical"}
    square = {"1:1", "square"}
    if ratio in landscape:
        return "1536x1024"
    if ratio in portrait:
        return "1024x1536"
    if ratio in square:
        return "1024x1024"
    raise ValueError(
        f"Unsupported aspect_ratio '{ratio}'. Set an explicit size or use 3:2, 16:9, 2:3, 9:16, or 1:1."
    )


def composed_prompt(spec: dict) -> str:
    prompt = str(spec.get("prompt", "")).strip()
    if not prompt:
        raise ValueError("editorial_image manifest is missing prompt")

    constraints = spec.get("negative_constraints", [])
    if constraints and not isinstance(constraints, list):
        raise ValueError("negative_constraints must be a list")
    constraints = [str(item).strip() for item in constraints if str(item).strip()]

    site_direction = (
        "Editorial visual for a specialist French technology guide. "
        "Credible, understated, premium editorial aesthetic; natural light; simple composition; "
        "generic unbranded hardware only; no embedded typography."
    )
    pieces = [site_direction, prompt]
    if constraints:
        pieces.append("Strict constraints: " + "; ".join(constraints) + ".")
    return "\n\n".join(pieces)


def api_request(*, api_key: str, model: str, prompt: str, size: str, quality: str, output_format: str, base_url: str, timeout: int) -> dict:
    payload = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "quality": quality,
        "n": 1,
        "output_format": output_format,
    }
    request = urllib.request.Request(
        base_url.rstrip("/") + "/images/generations",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "bloc-notes-numerique-guide-visual-workflow/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI Images API returned HTTP {exc.code}: {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"OpenAI Images API request failed: {exc.reason}") from exc


def extract_image_bytes(response: dict, *, timeout: int) -> bytes:
    data = response.get("data")
    if not isinstance(data, list) or not data:
        raise RuntimeError("Images API response does not contain data[0]")
    first = data[0]
    if not isinstance(first, dict):
        raise RuntimeError("Images API response data[0] is not an object")

    encoded = first.get("b64_json")
    if encoded:
        try:
            return base64.b64decode(encoded, validate=True)
        except (ValueError, TypeError) as exc:
            raise RuntimeError("Could not decode b64_json from Images API response") from exc

    url = first.get("url")
    if url:
        try:
            with urllib.request.urlopen(str(url), timeout=timeout) as response_obj:
                return response_obj.read()
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Could not download generated image URL: {exc.reason}") from exc

    raise RuntimeError("Images API response contains neither b64_json nor url")


def atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_bytes(content)
    temp.replace(path)


def eligible_manifests(root: Path, manifest_args: Iterable[str], all_manifests: bool) -> list[Path]:
    if all_manifests:
        candidates = sorted((root / ".content" / "visuals").glob("*.json"))
    else:
        candidates = []
        for raw in manifest_args:
            path = Path(raw)
            if not path.is_absolute():
                path = root / path
            candidates.append(path)

    selected: list[Path] = []
    for path in candidates:
        spec = load_manifest(path)
        if spec.get("asset_mode") == "editorial_image":
            selected.append(path)
    return selected


def generate_one(path: Path, *, root: Path, model: str, quality: str, overwrite: bool, dry_run: bool, timeout: int, retries: int, base_url: str, api_key: str | None) -> bool:
    spec = load_manifest(path)
    if spec.get("asset_mode") != "editorial_image":
        print(f"SKIP {path.relative_to(root)}: asset_mode={spec.get('asset_mode')}")
        return False

    output_value = str(spec.get("output", "")).strip()
    if not output_value:
        raise ValueError(f"{path}: editorial_image manifest is missing output")
    output = root / output_value
    output_format = normalize_output_format(output)
    size = size_for_spec(spec)
    prompt = composed_prompt(spec)
    selected_model = str(spec.get("model") or model)
    selected_quality = str(spec.get("quality") or quality)

    print(f"PLAN {path.relative_to(root)} -> {output.relative_to(root)}")
    print(f"     model={selected_model} size={size} quality={selected_quality} format={output_format}")

    if output.exists() and not overwrite:
        print("SKIP output already exists (use --overwrite to regenerate)")
        return False

    if dry_run:
        print("DRY-RUN no API request sent")
        return False

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required for image generation")

    last_error: Exception | None = None
    for attempt in range(1, retries + 2):
        try:
            response = api_request(
                api_key=api_key,
                model=selected_model,
                prompt=prompt,
                size=size,
                quality=selected_quality,
                output_format=output_format,
                base_url=base_url,
                timeout=timeout,
            )
            content = extract_image_bytes(response, timeout=timeout)
            atomic_write(output, content)
            print(f"WROTE {output.relative_to(root)} ({len(content):,} bytes)")
            return True
        except Exception as exc:
            last_error = exc
            if attempt > retries:
                break
            delay = min(2 ** attempt, 8)
            print(f"WARN attempt {attempt} failed: {exc}; retrying in {delay}s", file=sys.stderr)
            time.sleep(delay)

    raise RuntimeError(f"Generation failed for {path}: {last_error}") from last_error


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate editorial guide images from versioned manifests using the OpenAI Images API.")
    parser.add_argument("manifests", nargs="*", help="Manifest paths. Non-editorial manifests are skipped.")
    parser.add_argument("--all", action="store_true", help="Scan .content/visuals/*.json and generate editorial_image manifests.")
    parser.add_argument("--root", default=".")
    parser.add_argument("--model", default=os.getenv("OPENAI_IMAGE_MODEL", DEFAULT_MODEL))
    parser.add_argument("--quality", default=os.getenv("OPENAI_IMAGE_QUALITY", DEFAULT_QUALITY))
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--retries", type=int, default=2)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not args.all and not args.manifests:
        parser.error("provide at least one manifest or use --all")

    selected = eligible_manifests(root, args.manifests, args.all)
    if not selected:
        print("No editorial_image manifests selected.")
        return

    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL", DEFAULT_BASE_URL)

    generated = 0
    for manifest in selected:
        if generate_one(
            manifest,
            root=root,
            model=args.model,
            quality=args.quality,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
            timeout=args.timeout,
            retries=args.retries,
            base_url=base_url,
            api_key=api_key,
        ):
            generated += 1

    print(f"DONE generated={generated} selected={len(selected)} dry_run={args.dry_run}")


if __name__ == "__main__":
    main()
