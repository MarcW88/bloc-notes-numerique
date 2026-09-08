#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


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
    output = root / spec["output"]
    if not output.exists():
        failures.append(f"asset missing: {spec['output']}")
    else:
        svg = output.read_text(encoding="utf-8")
        if "<svg" not in svg or "viewBox=" not in svg:
            failures.append("SVG or viewBox missing")
        if re.search(r'<image\b[^>]+(?:href|xlink:href)="https?://', svg, re.I):
            failures.append("external raster image embedded in SVG")

    if not str(spec.get("alt", "")).strip():
        failures.append("alt text missing")
    if not str(spec.get("caption", "")).strip():
        failures.append("caption missing")
    if not spec.get("after_section_id"):
        failures.append("after_section_id missing")
    if len(spec.get("nodes", [])) < 2:
        failures.append("visual has too few nodes")

    if failures:
        for failure in failures:
            print("FAIL:", failure)
        raise SystemExit(1)

    print("PASS: visual asset manifest and SVG meet structural requirements")


if __name__ == "__main__":
    main()
