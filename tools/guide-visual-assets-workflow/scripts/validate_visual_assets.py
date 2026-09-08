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

    failures = []
    visual_type = spec.get("type")
    if visual_type in FORBIDDEN_TYPES:
        failures.append(f"table-like visual type forbidden: {visual_type}")
    elif visual_type not in REQUIRED_DATA:
        failures.append(f"unsupported visual type: {visual_type}")

    output = root / spec["output"]
    if not output.exists():
        failures.append(f"asset missing: {spec['output']}")
    else:
        svg = output.read_text(encoding="utf-8")
        if "<svg" not in svg or "viewBox=" not in svg:
            failures.append("SVG or viewBox missing")
        if re.search(r'<image\b', svg, re.I):
            failures.append("embedded image element forbidden")
        if "<title" not in svg or "<desc" not in svg:
            failures.append("accessible SVG title/description missing")

    if not str(spec.get("alt", "")).strip():
        failures.append("alt text missing")
    if not str(spec.get("caption", "")).strip():
        failures.append("caption missing")
    if not str(spec.get("page_url", "")).startswith("/guides/"):
        failures.append("guide page_url missing")

    data_key = REQUIRED_DATA.get(visual_type)
    if data_key and len(spec.get(data_key, [])) < 2:
        failures.append(f"visual has too little {data_key} data")

    if visual_type == "decision_tree" and len(spec.get("edges", [])) < 1:
        failures.append("decision tree has no edges")

    if failures:
        for failure in failures:
            print("FAIL:", failure)
        raise SystemExit(1)

    print(f"PASS: {visual_type} asset manifest and SVG meet structural requirements")


if __name__ == "__main__":
    main()
