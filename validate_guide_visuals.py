#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
manifests = {p.stem: p for p in (ROOT / ".content" / "visuals").glob("*.json")}
guides = {p.parent.name: p for p in (ROOT / "guides").glob("*/index.html")}
issues = []
FORBIDDEN_TYPES = {"decision_matrix", "table", "comparison_table"}
EDITORIAL_EXTENSIONS = {".webp", ".png", ".jpg", ".jpeg", ".avif"}
counts = {"functional_diagram": 0, "editorial_image": 0, "no_visual": 0}

if set(manifests) != set(guides):
    missing = sorted(set(guides) - set(manifests))
    extra = sorted(set(manifests) - set(guides))
    issues.append(f"manifest/page mismatch; missing={missing}, extra={extra}")

for slug, page in guides.items():
    manifest_path = manifests.get(slug)
    if not manifest_path:
        continue

    spec = json.loads(manifest_path.read_text(encoding="utf-8"))
    asset_mode = spec.get("asset_mode", "functional_diagram")
    counts[asset_mode] = counts.get(asset_mode, 0) + 1

    html = page.read_text(encoding="utf-8")
    if 'name="robots" content="noindex,follow"' not in html:
        issues.append(f"{slug}: noindex,follow lost")

    all_visuals = len(re.findall(r'data-visual-id="[^"]+"', html))

    if asset_mode == "no_visual":
        if spec.get("output"):
            issues.append(f"{slug}: no_visual must not define output")
        if not str(spec.get("reason", "")).strip():
            issues.append(f"{slug}: no_visual reason missing")
        if all_visuals != 0:
            issues.append(f"{slug}: no_visual page still contains {all_visuals} injected visual block(s)")
        continue

    if not spec.get("alt", "").strip():
        issues.append(f"{slug}: alt missing")
    output_value = str(spec.get("output", ""))
    if not output_value:
        issues.append(f"{slug}: output missing")
        continue
    asset = ROOT / output_value
    if not asset.exists():
        issues.append(f"{slug}: asset missing")
        continue

    if asset_mode == "functional_diagram":
        if spec.get("type") in FORBIDDEN_TYPES:
            issues.append(f"{slug}: table-like visual forbidden ({spec.get('type')})")
        svg = asset.read_text(encoding="utf-8")
        if "<svg" not in svg or "viewBox=" not in svg:
            issues.append(f"{slug}: responsive SVG invalid")
        if re.search(r"<image\b", svg, re.I):
            issues.append(f"{slug}: embedded image forbidden")
        if not spec.get("caption", "").strip():
            issues.append(f"{slug}: caption missing")
    elif asset_mode == "editorial_image":
        if asset.suffix.lower() not in EDITORIAL_EXTENSIONS:
            issues.append(f"{slug}: unsupported editorial image extension")
    else:
        issues.append(f"{slug}: unsupported asset_mode {asset_mode}")
        continue

    marker = f'data-visual-id="{spec["id"]}"'
    if html.count(marker) != 1:
        issues.append(f"{slug}: expected selected visual once, found {html.count(marker)}")
    if all_visuals != 1:
        issues.append(f"{slug}: expected exactly one visual block, found {all_visuals}")
    if f'/{output_value}' not in html:
        issues.append(f"{slug}: asset URL absent from page")

if issues:
    for issue in issues:
        print("FAIL", issue)
    raise SystemExit(1)

print(
    "PASS: guide visual routing valid — "
    f"{counts.get('functional_diagram', 0)} functional diagrams, "
    f"{counts.get('editorial_image', 0)} editorial images, "
    f"{counts.get('no_visual', 0)} no-visual pages"
)
