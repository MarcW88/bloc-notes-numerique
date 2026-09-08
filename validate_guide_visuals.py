#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
manifests = {p.stem: p for p in (ROOT / ".content" / "visuals").glob("*.json")}
guides = {p.parent.name: p for p in (ROOT / "guides").glob("*/index.html")}
issues = []

if set(manifests) != set(guides):
    missing = sorted(set(guides) - set(manifests))
    extra = sorted(set(manifests) - set(guides))
    issues.append(f"manifest/page mismatch; missing={missing}, extra={extra}")

for slug, page in guides.items():
    manifest_path = manifests.get(slug)
    if not manifest_path:
        continue
    spec = json.loads(manifest_path.read_text(encoding="utf-8"))
    asset = ROOT / spec["output"]
    if not asset.exists():
        issues.append(f"{slug}: asset missing")
        continue
    svg = asset.read_text(encoding="utf-8")
    if "<svg" not in svg or "viewBox=" not in svg:
        issues.append(f"{slug}: responsive SVG invalid")
    if re.search(r"<image\b", svg, re.I):
        issues.append(f"{slug}: embedded image forbidden")
    if not spec.get("alt", "").strip():
        issues.append(f"{slug}: alt missing")
    if not spec.get("caption", "").strip():
        issues.append(f"{slug}: caption missing")

    html = page.read_text(encoding="utf-8")
    if 'name="robots" content="noindex,follow"' not in html:
        issues.append(f"{slug}: noindex,follow lost")
    marker = f'data-visual-id="{spec["id"]}"'
    if html.count(marker) != 1:
        issues.append(f"{slug}: expected one visual, found {html.count(marker)}")
    if f'/{spec["output"]}' not in html:
        issues.append(f"{slug}: asset URL absent from page")

if issues:
    for issue in issues:
        print("FAIL", issue)
    raise SystemExit(1)

print(f"PASS: {len(guides)} guide pages each contain exactly one validated visual")
