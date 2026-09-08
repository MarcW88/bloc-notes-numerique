#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / ".content/visuals/choisir-bloc-notes-numerique.json"

spec = json.loads(MANIFEST.read_text(encoding="utf-8"))
page = ROOT / spec["page_url"].strip("/") / "index.html"
asset = ROOT / spec["output"]
failures = []

if not page.exists():
    failures.append("pilot guide page missing")
else:
    html = page.read_text(encoding="utf-8")
    if 'name="robots" content="noindex,follow"' not in html:
        failures.append("noindex,follow missing")
    marker = f'visual:start:{spec["id"]}'
    if html.count(marker) != 1:
        failures.append(f"visual marker count is {html.count(marker)}, expected 1")
    expected_src = '/' + spec['output'].lstrip('/')
    if f'src="{expected_src}"' not in html:
        failures.append("visual img src missing")
    if f'alt="{spec["alt"]}"' not in html:
        failures.append("visual alt text missing or changed")
    if spec["caption"] not in html:
        failures.append("visual caption missing")
    if '<figure class="guide-visual' not in html:
        failures.append("semantic figure wrapper missing")

if not asset.exists():
    failures.append("SVG asset missing")
else:
    svg = asset.read_text(encoding="utf-8")
    if "viewBox=" not in svg:
        failures.append("SVG viewBox missing")
    if re.search(r'<image\b[^>]+(?:href|xlink:href)="https?://', svg, re.I):
        failures.append("external image embedded in SVG")

if failures:
    for failure in failures:
        print("FAIL:", failure)
    raise SystemExit(1)

print("PASS: pilot guide visual is generated, accessible, unique and noindex-safe")
