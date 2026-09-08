#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REQUIRED_DATA = {
    "decision_tree": "nodes",
    "process_flow": "steps",
    "ecosystem_map": "layers",
    "checklist": "items",
    "cost_breakdown": "items",
    "size_comparison": "sizes",
}

FORBIDDEN_TYPES = {"decision_matrix", "table", "comparison_table"}
EDITORIAL_EXTENSIONS = {".webp", ".png", ".jpg", ".jpeg", ".avif"}


def fail_if_empty(spec: dict, field: str, failures: list[str]) -> None:
    if not str(spec.get(field, "")).strip():
        failures.append(f"{field} missing")


def validate_common(spec: dict, failures: list[str]) -> None:
    if not str(spec.get("page_url", "")).startswith("/guides/"):
        failures.append("guide page_url missing")
    if "asset_mode" in spec:
        fail_if_empty(spec, "visual_goal", failures)


def validate_no_visual(spec: dict, failures: list[str]) -> None:
    fail_if_empty(spec, "reason", failures)
    if spec.get("output"):
        failures.append("no_visual must not define an output asset")


def validate_editorial_image(spec: dict, root: Path, failures: list[str]) -> None:
    fail_if_empty(spec, "alt", failures)
    fail_if_empty(spec, "prompt", failures)
    fail_if_empty(spec, "output", failures)
    fail_if_empty(spec, "aspect_ratio", failures)

    constraints = spec.get("negative_constraints", [])
    if not isinstance(constraints, list) or len(constraints) < 2:
        failures.append("editorial_image needs at least two negative_constraints")

    output_value = str(spec.get("output", ""))
    if output_value:
        output = root / output_value
        if output.suffix.lower() not in EDITORIAL_EXTENSIONS:
            failures.append("editorial_image output must be a raster/web image format")
        if not output.exists():
            failures.append(f"asset missing: {output_value}")

    prompt = str(spec.get("prompt", "")).lower()
    forbidden_prompt_patterns = [
        "logo of ",
        "screenshot of ",
        "exact remarkable",
        "exact kindle",
        "exact boox",
        "exact supernote",
        "exact kobo",
    ]
    if any(pattern in prompt for pattern in forbidden_prompt_patterns):
        failures.append("editorial image prompt requests risky branded/fake representation")


def validate_functional_diagram(spec: dict, root: Path, failures: list[str]) -> None:
    visual_type = spec.get("type")
    if visual_type in FORBIDDEN_TYPES:
        failures.append(f"table-like visual type forbidden: {visual_type}")
    elif visual_type not in REQUIRED_DATA:
        failures.append(f"unsupported visual type: {visual_type}")

    fail_if_empty(spec, "alt", failures)
    fail_if_empty(spec, "caption", failures)
    fail_if_empty(spec, "output", failures)

    output_value = str(spec.get("output", ""))
    if output_value:
        output = root / output_value
        if not output.exists():
            failures.append(f"asset missing: {output_value}")
        else:
            svg = output.read_text(encoding="utf-8")
            if "<svg" not in svg or "viewBox=" not in svg:
                failures.append("SVG or viewBox missing")
            if re.search(r'<image\b', svg, re.I):
                failures.append("embedded image element forbidden")
            if "<title" not in svg or "<desc" not in svg:
                failures.append("accessible SVG title/description missing")

    data_key = REQUIRED_DATA.get(visual_type)
    if data_key and len(spec.get(data_key, [])) < 2:
        failures.append(f"visual has too little {data_key} data")

    if visual_type == "decision_tree" and len(spec.get("edges", [])) < 1:
        failures.append("decision tree has no edges")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    manifest = Path(args.manifest)
    if not manifest.is_absolute():
        manifest = root / manifest
    spec = json.loads(manifest.read_text(encoding="utf-8"))

    failures: list[str] = []
    asset_mode = spec.get("asset_mode", "functional_diagram")

    validate_common(spec, failures)

    if asset_mode == "no_visual":
        validate_no_visual(spec, failures)
    elif asset_mode == "editorial_image":
        validate_editorial_image(spec, root, failures)
    elif asset_mode == "functional_diagram":
        validate_functional_diagram(spec, root, failures)
    else:
        failures.append(f"unsupported asset_mode: {asset_mode}")

    if failures:
        for failure in failures:
            print("FAIL:", failure)
        raise SystemExit(1)

    print(f"PASS: {asset_mode} manifest meets structural requirements")


if __name__ == "__main__":
    main()
