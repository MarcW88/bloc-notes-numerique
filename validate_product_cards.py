#!/usr/bin/env python3
"""Machine guards for the intentionally limited comparison affiliate pilot."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / ".content" / "products" / "registry.json"
PILOT = ROOT / ".content" / "products" / "pilot-comparisons.json"
EXPECTED_PILOT = {
    "meilleur-bloc-notes-numerique": 3,
    "bloc-notes-numerique-professionnel": 3,
    "kindle-scribe-vs-remarkable": 2,
}
ALLOWED_IMAGE_SOURCES = {"UNSET", "OWN", "MANUFACTURER_AUTHORIZED", "AMAZON_CREATORS_API"}
ALLOWED_AFFILIATE_HOSTS = {"amazon.fr", "www.amazon.fr", "amazon.com.be", "www.amazon.com.be", "amzn.to"}
FORBIDDEN_COMMERCE_KEYS = {"price", "current_price", "reference_price", "discount", "discount_pct"}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def walk_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_keys(child)


def main() -> None:
    registry_data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    pilot_data = json.loads(PILOT.read_text(encoding="utf-8"))
    products = registry_data.get("products", {})
    pages = pilot_data.get("pages", {})

    if set(pages) != set(EXPECTED_PILOT):
        fail("pilot scope changed without explicit validator update")

    forbidden = FORBIDDEN_COMMERCE_KEYS & set(walk_keys(registry_data))
    if forbidden:
        fail("static commerce data is forbidden in Phase 1 registry: " + ", ".join(sorted(forbidden)))

    for product_id, product in products.items():
        for key in ("name", "internal_url", "image", "amazon", "specs", "best_for"):
            if key not in product:
                fail(f"{product_id}: missing {key}")
        if not product["internal_url"].startswith("/"):
            fail(f"{product_id}: internal_url must be site-relative")
        if not 1 <= len(product.get("specs", [])) <= 5:
            fail(f"{product_id}: keep 1 to 5 decision-useful specs")

        image = product["image"]
        source_type = image.get("source_type")
        image_url = (image.get("url") or "").strip()
        if source_type not in ALLOWED_IMAGE_SOURCES:
            fail(f"{product_id}: invalid image source {source_type}")
        if image_url and source_type == "UNSET":
            fail(f"{product_id}: image URL requires an explicit source type")
        if source_type == "MANUFACTURER_AUTHORIZED" and image_url and not image.get("rights_checked"):
            fail(f"{product_id}: manufacturer image requires rights_checked=true")
        if source_type == "AMAZON_CREATORS_API" and image_url and not image_url.startswith("https://"):
            fail(f"{product_id}: Creators API image must remain a remote HTTPS URL")

        affiliate_url = (product["amazon"].get("affiliate_url") or "").strip()
        if affiliate_url:
            parsed = urlsplit(affiliate_url)
            if parsed.scheme != "https" or parsed.hostname not in ALLOWED_AFFILIATE_HOSTS:
                fail(f"{product_id}: unsupported Amazon/SiteStripe affiliate URL")

    pilot_cards_found = set()
    for page in sorted((ROOT / "comparatifs").glob("*/index.html")):
        text = page.read_text(encoding="utf-8")
        slug = page.parent.name
        if 'data-product-pilot="true"' not in text:
            continue
        pilot_cards_found.add(slug)
        if slug not in EXPECTED_PILOT:
            fail(f"product cards leaked outside pilot scope: {slug}")

    if pilot_cards_found != set(EXPECTED_PILOT):
        fail("pilot cards missing on: " + ", ".join(sorted(set(EXPECTED_PILOT) - pilot_cards_found)))

    for slug, expected_count in EXPECTED_PILOT.items():
        config = pages[slug]
        if len(config.get("products", [])) != expected_count:
            fail(f"{slug}: expected {expected_count} configured products")
        unknown = [pid for pid in config["products"] if pid not in products]
        if unknown:
            fail(f"{slug}: unknown products: {', '.join(unknown)}")

        page = ROOT / "comparatifs" / slug / "index.html"
        text = page.read_text(encoding="utf-8")
        if '<meta name="robots" content="index,follow">' not in text:
            fail(f"{slug}: pilot page is no longer index,follow")
        if text.count('class="product-card"') != expected_count:
            fail(f"{slug}: rendered product-card count mismatch")
        if text.count(f'<!-- PRODUCT_PILOT:{slug}:START -->') != 1 or text.count(f'<!-- PRODUCT_PILOT:{slug}:END -->') != 1:
            fail(f"{slug}: pilot marker count mismatch")
        if '<link rel="stylesheet" href="/assets/product-cards.css">' not in text:
            fail(f"{slug}: product card stylesheet missing")
        if '<script src="/assets/product-affiliate.js" defer></script>' not in text:
            fail(f"{slug}: affiliate click instrumentation missing")

        expected_affiliate_links = sum(
            1 for pid in config["products"] if (products[pid]["amazon"].get("affiliate_url") or "").strip()
        )
        actual_affiliate_links = text.count('data-affiliate-link="amazon"')
        if actual_affiliate_links != expected_affiliate_links:
            fail(f"{slug}: expected {expected_affiliate_links} Amazon CTAs, got {actual_affiliate_links}")
        if actual_affiliate_links:
            affiliate_tags = re.findall(r'<a\b[^>]*data-affiliate-link="amazon"[^>]*>', text, re.I)
            for tag in affiliate_tags:
                rel = re.search(r'rel="([^"]+)"', tag, re.I)
                tokens = set((rel.group(1) if rel else "").lower().split())
                required = {"sponsored", "nofollow", "noopener", "noreferrer"}
                if not required.issubset(tokens):
                    fail(f"{slug}: Amazon CTA missing required rel tokens")

    print("PASS: Phase-1 product-card pilot is limited to 3 comparison URLs")
    print("PASS: cards contain no static Amazon prices and affiliate CTAs are conditional")
    print("PASS: image provenance and Amazon link safeguards are active")


if __name__ == "__main__":
    main()
