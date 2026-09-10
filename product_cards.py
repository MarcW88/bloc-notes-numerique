#!/usr/bin/env python3
"""Render reusable editorial product cards from the central product registry."""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY_PATH = ROOT / ".content" / "products" / "registry.json"
PILOT_PATH = ROOT / ".content" / "products" / "pilot-comparisons.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_registry() -> dict[str, dict]:
    return load_json(REGISTRY_PATH)["products"]


def load_pilot() -> dict[str, dict]:
    return load_json(PILOT_PATH)["pages"]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def render_card(product_id: str, product: dict, placement: str) -> str:
    image = product.get("image", {})
    image_url = (image.get("url") or "").strip()
    image_html = ""
    if image_url:
        image_html = (
            '<div class="product-card__media">'
            f'<img src="{esc(image_url)}" alt="{esc(product["name"])}" loading="lazy" decoding="async">'
            "</div>"
        )

    specs = "".join(
        '<div class="product-card__spec">'
        f'<dt>{esc(item["label"])}</dt><dd>{esc(item["value"])}</dd>'
        "</div>"
        for item in product.get("specs", [])[:5]
    )

    amazon = product.get("amazon", {})
    affiliate_url = (amazon.get("affiliate_url") or "").strip()
    if affiliate_url:
        commerce_html = (
            f'<a class="product-card__cta" href="{esc(affiliate_url)}" '
            'target="_blank" rel="sponsored nofollow noopener noreferrer" '
            f'data-affiliate-link="amazon" data-product-id="{esc(product_id)}" '
            f'data-placement="{esc(placement)}">Voir le prix sur Amazon →</a>'
            '<span class="product-card__disclosure">Lien rémunéré</span>'
        )
    else:
        commerce_html = (
            f'<a class="product-card__internal" href="{esc(product["internal_url"])}">'
            "Voir notre analyse →</a>"
        )

    return (
        f'<article class="product-card" data-product-id="{esc(product_id)}">'
        f'{image_html}'
        '<div class="product-card__body">'
        f'<h3 class="product-card__title">{esc(product["name"])}</h3>'
        f'<p class="product-card__best"><strong>À privilégier pour :</strong> {esc(product["best_for"])}</p>'
        f'<dl class="product-card__specs">{specs}</dl>'
        f'<div class="product-card__actions">{commerce_html}</div>'
        "</div></article>"
    )


def render_section(page_slug: str, config: dict, registry: dict[str, dict]) -> str:
    cards = "".join(
        render_card(product_id, registry[product_id], page_slug)
        for product_id in config["products"]
    )
    return (
        f'<!-- PRODUCT_PILOT:{esc(page_slug)}:START -->\n'
        f'<section class="product-card-section" data-product-pilot="true" data-product-placement="{esc(page_slug)}">\n'
        f'  <h2 id="{esc(config["section_id"])}">{esc(config["section_title"])}</h2>\n'
        f'  <p class="product-card-section__intro">{esc(config["intro"])}</p>\n'
        f'  <div class="product-card-grid product-card-grid--{len(config["products"])}">{cards}</div>\n'
        '</section>\n'
        f'<!-- PRODUCT_PILOT:{esc(page_slug)}:END -->'
    )
