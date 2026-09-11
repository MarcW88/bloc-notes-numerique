#!/usr/bin/env python3
"""Generate approved editorial images through a local Draw Things HTTP API.

The script has no third-party Python dependency. It is designed to run on a
GitHub self-hosted macOS runner while Draw Things is open on the same Mac.
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_REQUESTS_DIR = ".content/image-requests"
DEFAULT_DRAW_THINGS_URL = "http://127.0.0.1:7860/sdapi/v1/txt2img"
ACTIVE_STATUSES = {"PENDING", "REGENERATE"}
VALID_STATUSES = {"NOT_NEEDED", "BLOCKED", "PENDING", "GENERATED", "REGENERATE"}


class RequestError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument(
        "--requests-dir",
        default=DEFAULT_REQUESTS_DIR,
        help="Directory containing image request JSON files",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Validate requests and report whether the local runner is needed",
    )
    parser.add_argument(
        "--github-output",
        default=None,
        help="Optional GITHUB_OUTPUT file used by GitHub Actions",
    )
    parser.add_argument(
        "--api-url",
        default=os.environ.get("DRAW_THINGS_URL", DEFAULT_DRAW_THINGS_URL),
        help="Draw Things txt2img endpoint",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=int(os.environ.get("DRAW_THINGS_TIMEOUT", "600")),
        help="HTTP timeout in seconds",
    )
    return parser.parse_args()


def request_files(root: Path, requests_dir: str) -> list[Path]:
    directory = root / requests_dir
    if not directory.exists():
        return []
    return sorted(
        path
        for path in directory.glob("*.json")
        if path.name != "_template.json"
    )


def load_request(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RequestError(f"{path}: JSON illisible: {exc}") from exc
    if not isinstance(data, dict):
        raise RequestError(f"{path}: la racine JSON doit être un objet")
    return data


def safe_repo_path(root: Path, value: str, field: str, source: Path) -> Path:
    if not value or not isinstance(value, str):
        raise RequestError(f"{source}: champ {field!r} manquant")
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise RequestError(f"{source}: chemin {field!r} non sûr: {value}")
    resolved = (root / candidate).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise RequestError(f"{source}: {field!r} sort du dépôt") from exc
    return resolved


def validate_request(root: Path, source: Path, req: dict[str, Any]) -> None:
    request_id = req.get("id")
    if not isinstance(request_id, str) or not request_id.strip():
        raise RequestError(f"{source}: id manquant")

    status = req.get("status")
    if status not in VALID_STATUSES:
        raise RequestError(
            f"{source}: status {status!r} invalide; attendu {sorted(VALID_STATUSES)}"
        )

    required = req.get("required")
    allowed = req.get("allow_ai_generation")
    if not isinstance(required, bool) or not isinstance(allowed, bool):
        raise RequestError(
            f"{source}: required et allow_ai_generation doivent être des booléens"
        )

    if not required and status in ACTIVE_STATUSES:
        raise RequestError(f"{source}: une requête non requise ne peut pas être {status}")

    if status in ACTIVE_STATUSES:
        if not allowed:
            raise RequestError(
                f"{source}: {status} exige allow_ai_generation=true; utiliser BLOCKED sinon"
            )
        if req.get("truth_risk") != "LOW":
            raise RequestError(
                f"{source}: la génération automatique est limitée à truth_risk=LOW"
            )

        for field in ("page", "marker", "output_path", "prompt", "alt"):
            value = req.get(field)
            if not isinstance(value, str) or not value.strip():
                raise RequestError(f"{source}: champ {field!r} requis pour {status}")

        output_path = str(req["output_path"])
        if not output_path.startswith("assets/generated/"):
            raise RequestError(
                f"{source}: output_path doit rester sous assets/generated/"
            )

        safe_repo_path(root, str(req["page"]), "page", source)
        safe_repo_path(root, output_path, "output_path", source)

        for field in ("width", "height", "steps", "batch_count"):
            value = req.get(field)
            if not isinstance(value, int) or value <= 0:
                raise RequestError(f"{source}: {field} doit être un entier positif")

        if req.get("batch_count") != 1:
            raise RequestError(
                f"{source}: batch_count doit rester à 1 pour protéger le Mac 16 Go"
            )

        guidance = req.get("guidance_scale")
        if not isinstance(guidance, (int, float)) or guidance < 0:
            raise RequestError(f"{source}: guidance_scale invalide")


def figure_markup(req: dict[str, Any]) -> str:
    request_id = html.escape(str(req["id"]), quote=True)
    src = "/" + str(req["output_path"]).lstrip("/")
    alt = html.escape(str(req["alt"]), quote=True)
    caption = str(req.get("caption") or "").strip()
    width = int(req["width"])
    height = int(req["height"])

    lines = [
        f'<figure class="editorial-media" data-generated-image="{request_id}" '
        'style="margin:28px 0 32px;">',
        f'  <img src="{html.escape(src, quote=True)}" alt="{alt}" '
        f'width="{width}" height="{height}" loading="lazy" decoding="async" '
        'style="width:100%;height:auto;border-radius:var(--radius-md);display:block;">',
    ]
    if caption:
        lines.append(
            "  <figcaption "
            'style="margin-top:8px;font-size:.78rem;line-height:1.5;color:var(--color-text-muted);">'
            f"{html.escape(caption)}</figcaption>"
        )
    lines.append("</figure>")
    return "\n".join(lines)


def page_needs_insertion(root: Path, source: Path, req: dict[str, Any]) -> bool:
    if not req.get("required") or not req.get("allow_ai_generation"):
        return False
    if req.get("truth_risk") != "LOW":
        return False
    if req.get("status") != "GENERATED":
        return False

    page_path = safe_repo_path(root, str(req.get("page", "")), "page", source)
    output_path = safe_repo_path(
        root, str(req.get("output_path", "")), "output_path", source
    )
    if not page_path.exists() or not output_path.exists():
        return False

    text = page_path.read_text(encoding="utf-8")
    marker = str(req.get("marker", ""))
    figure_token = f'data-generated-image="{req.get("id", "")}"'
    return marker in text and figure_token not in text


def request_needs_generation(req: dict[str, Any]) -> bool:
    return bool(
        req.get("required")
        and req.get("allow_ai_generation")
        and req.get("truth_risk") == "LOW"
        and req.get("status") in ACTIVE_STATUSES
    )


def check_work(root: Path, sources: list[Path]) -> tuple[bool, int, int]:
    seen_outputs: dict[str, Path] = {}
    pending = 0
    reinsert = 0

    for source in sources:
        req = load_request(source)
        validate_request(root, source, req)

        output = str(req.get("output_path") or "")
        if output:
            previous = seen_outputs.get(output)
            if previous and previous != source:
                raise RequestError(
                    f"{source}: output_path dupliqué avec {previous}: {output}"
                )
            seen_outputs[output] = source

        if request_needs_generation(req):
            page_path = safe_repo_path(root, str(req["page"]), "page", source)
            if not page_path.exists():
                raise RequestError(f"{source}: page cible absente: {req['page']}")
            page_text = page_path.read_text(encoding="utf-8")
            figure_token = f'data-generated-image="{req["id"]}"'
            if str(req["marker"]) not in page_text and figure_token not in page_text:
                raise RequestError(
                    f"{source}: marker absent de la page générée: {req['marker']}"
                )
            pending += 1
        elif page_needs_insertion(root, source, req):
            reinsert += 1

    return (pending + reinsert > 0, pending, reinsert)


def call_draw_things(api_url: str, timeout: int, req: dict[str, Any]) -> bytes:
    payload = {
        "prompt": req["prompt"],
        "negative_prompt": req.get("negative_prompt", ""),
        "seed": int(req.get("seed", -1)),
        "steps": int(req.get("steps", 4)),
        "guidance_scale": float(req.get("guidance_scale", 1.0)),
        "batch_count": 1,
        "width": int(req.get("width", 768)),
        "height": int(req.get("height", 512)),
    }

    request = urllib.request.Request(
        api_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read()
    except urllib.error.URLError as exc:
        raise RequestError(
            "Impossible de joindre Draw Things. Ouvrir l'app, sélectionner le modèle "
            f"local, activer l'API HTTP puis vérifier {api_url}. Détail: {exc}"
        ) from exc

    try:
        data = json.loads(body)
    except json.JSONDecodeError as exc:
        raise RequestError("Réponse Draw Things non JSON") from exc

    images = data.get("images") if isinstance(data, dict) else None
    if not isinstance(images, list) or not images:
        raise RequestError(f"Draw Things n'a renvoyé aucune image: {data!r}")

    encoded = images[0]
    if not isinstance(encoded, str):
        raise RequestError("Image Draw Things invalide")
    if encoded.startswith("data:") and "," in encoded:
        encoded = encoded.split(",", 1)[1]

    try:
        return base64.b64decode(encoded)
    except Exception as exc:  # base64 raises several subclasses depending on input
        raise RequestError("Impossible de décoder l'image Draw Things") from exc


def insert_or_restore_figure(root: Path, source: Path, req: dict[str, Any]) -> bool:
    page_path = safe_repo_path(root, str(req["page"]), "page", source)
    output_path = safe_repo_path(root, str(req["output_path"]), "output_path", source)
    if not output_path.exists():
        raise RequestError(f"{source}: image absente: {req['output_path']}")
    if not page_path.exists():
        raise RequestError(f"{source}: page cible absente: {req['page']}")

    text = page_path.read_text(encoding="utf-8")
    marker = str(req["marker"])
    figure_token = f'data-generated-image="{req["id"]}"'

    if figure_token in text:
        return False
    if marker not in text:
        raise RequestError(
            f"{source}: impossible d'insérer l'image, marker absent: {marker}"
        )

    text = text.replace(marker, figure_markup(req), 1)
    page_path.write_text(text, encoding="utf-8")
    return True


def process(root: Path, sources: list[Path], api_url: str, timeout: int) -> None:
    for source in sources:
        req = load_request(source)
        validate_request(root, source, req)

        if not req.get("required") or not req.get("allow_ai_generation"):
            continue
        if req.get("truth_risk") != "LOW":
            continue

        status = req.get("status")
        output_path = safe_repo_path(
            root, str(req.get("output_path", "")), "output_path", source
        )

        generated_now = False
        if status in ACTIVE_STATUSES:
            page_path = safe_repo_path(root, str(req["page"]), "page", source)
            page_text = page_path.read_text(encoding="utf-8") if page_path.exists() else ""
            figure_token = f'data-generated-image="{req["id"]}"'
            if str(req["marker"]) not in page_text and figure_token not in page_text:
                raise RequestError(
                    f"{source}: marker absent de la page générée: {req['marker']}"
                )

            must_generate = status == "REGENERATE" or not output_path.exists()
            if must_generate:
                print(f"Generating {req['id']} with Draw Things…")
                image = call_draw_things(api_url, timeout, req)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_bytes(image)
                generated_now = True
                print(f"Saved {output_path.relative_to(root)}")
            else:
                print(f"Reusing existing image {output_path.relative_to(root)}")

            req["status"] = "GENERATED"
            if generated_now or not req.get("generated_at"):
                req["generated_at"] = datetime.now(timezone.utc).isoformat()
            source.write_text(
                json.dumps(req, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

        if req.get("status") == "GENERATED" and output_path.exists():
            if insert_or_restore_figure(root, source, req):
                print(f"Inserted {req['id']} into {req['page']}")


def write_github_output(path: str | None, work: bool, pending: int, reinsert: int) -> None:
    if not path:
        return
    with Path(path).open("a", encoding="utf-8") as handle:
        handle.write(f"work_needed={'true' if work else 'false'}\n")
        handle.write(f"pending_count={pending}\n")
        handle.write(f"reinsert_count={reinsert}\n")


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    sources = request_files(root, args.requests_dir)

    try:
        work, pending, reinsert = check_work(root, sources)
        print(
            f"Image requests: {len(sources)} | pending generation: {pending} | "
            f"reinsertion: {reinsert}"
        )
        write_github_output(args.github_output, work, pending, reinsert)
        if args.check_only:
            return 0

        if not work:
            print("No image work required.")
            return 0

        process(root, sources, args.api_url, args.timeout)
        return 0
    except RequestError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
