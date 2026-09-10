#!/usr/bin/env python3
"""Apply the deliberately small Phase-1 product-card pilot to comparison pages."""

from __future__ import annotations

import re
from pathlib import Path

from product_cards import load_pilot, load_registry, render_section

ROOT = Path(__file__).resolve().parent
STYLE_TAG = '<link rel="stylesheet" href="/assets/product-cards.css">'
SCRIPT_TAG = '<script src="/assets/product-affiliate.js" defer></script>'


def strip_previous_block(text: str, slug: str) -> str:
    pattern = re.compile(
        rf'\n?<!-- PRODUCT_PILOT:{re.escape(slug)}:START -->.*?'
        rf'<!-- PRODUCT_PILOT:{re.escape(slug)}:END -->\n?',
        re.S,
    )
    return pattern.sub("\n", text)


def ensure_asset_tag(text: str, tag: str, before: str) -> str:
    if tag in text:
        return text
    if before not in text:
        raise SystemExit(f"Could not place asset tag before {before}")
    return text.replace(before, f"  {tag}\n{before}", 1)


def apply_page(slug: str, config: dict, registry: dict[str, dict]) -> None:
    page = ROOT / "comparatifs" / slug / "index.html"
    if not page.exists():
        raise SystemExit(f"Missing pilot comparison page: {page}")

    text = page.read_text(encoding="utf-8")
    text = strip_previous_block(text, slug)
    text = ensure_asset_tag(text, STYLE_TAG, "</head>")
    text = ensure_asset_tag(text, SCRIPT_TAG, "</body>")

    missing = [product_id for product_id in config["products"] if product_id not in registry]
    if missing:
        raise SystemExit(f"{slug}: missing products in registry: {', '.join(missing)}")

    anchor_id = config["insert_before_heading_id"]
    anchor = re.search(rf'<h2\s+id="{re.escape(anchor_id)}"[^>]*>', text, re.I)
    if not anchor:
        raise SystemExit(f"{slug}: insertion heading #{anchor_id} not found")

    block = render_section(slug, config, registry)
    text = text[:anchor.start()] + block + "\n\n" + text[anchor.start():]
    page.write_text(text, encoding="utf-8")
    print(f"product cards applied: {slug} ({len(config['products'])} cards)")


def main() -> None:
    registry = load_registry()
    pilot = load_pilot()
    for slug, config in pilot.items():
        apply_page(slug, config, registry)


if __name__ == "__main__":
    main()
