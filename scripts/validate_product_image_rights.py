#!/usr/bin/env python3
"""Check product images against the central registry and the rights review."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
registry = json.loads((ROOT / ".content/products/registry.json").read_text(encoding="utf-8"))["products"]
audit = json.loads((ROOT / ".content/products/image-rights-audit-20261029.json").read_text(encoding="utf-8"))["products"]
errors = []
pending = []
for product_id, product in registry.items():
    image = product.get("image", {})
    record = audit.get(product_id)
    if not record:
        errors.append(f"{product_id}: missing rights review")
        continue
    url = image.get("url", "")
    if not url:
        pending.append(product_id)
        continue
    if not image.get("rights_checked") or not record.get("license") or not record.get("source_page"):
        errors.append(f"{product_id}: image configured without rights evidence")
    elif url.startswith("/"):
        target = ROOT / url.lstrip("/")
        if not target.is_file():
            errors.append(f"{product_id}: local image missing: {url}")
        elif target.suffix.lower() not in {".webp", ".jpg", ".jpeg", ".png", ".avif"}:
            errors.append(f"{product_id}: unsupported image format: {url}")
for product_id in audit:
    if product_id not in registry:
        errors.append(f"{product_id}: rights review has unknown product")
print(f"Products: {len(registry)}; pending images: {len(pending)}; errors: {len(errors)}")
for message in errors:
    print("ERROR:", message)
if pending:
    print("PENDING:", ", ".join(pending))
sys.exit(1 if errors else 0)
