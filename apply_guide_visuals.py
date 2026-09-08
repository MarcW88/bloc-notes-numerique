#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_manifest(path: str) -> dict:
    manifest = Path(path)
    if not manifest.is_absolute():
        manifest = ROOT / manifest
    return json.loads(manifest.read_text(encoding="utf-8"))


def page_path(page_url: str) -> Path:
    return ROOT / page_url.strip("/") / "index.html"


def svg_dimensions(spec: dict) -> tuple[int, int]:
    asset = ROOT / spec["output"]
    svg = asset.read_text(encoding="utf-8")
    match = re.search(r'viewBox="\s*0\s+0\s+([0-9.]+)\s+([0-9.]+)\s*"', svg, re.I)
    if not match:
        raise SystemExit(f"Could not read SVG dimensions: {asset}")
    return int(float(match.group(1))), int(float(match.group(2)))


def asset_dimensions(spec: dict) -> tuple[int, int]:
    if spec.get("asset_mode", "functional_diagram") == "functional_diagram":
        return svg_dimensions(spec)
    width = int(spec.get("width", 1200))
    height = int(spec.get("height", 800))
    return width, height


def figure_html(spec: dict) -> str:
    asset_url = "/" + spec["output"].lstrip("/")
    width, height = asset_dimensions(spec)
    visual_id = spec["id"]
    asset_mode = spec.get("asset_mode", "functional_diagram")
    css_type = spec.get("type", asset_mode)
    caption = spec.get("caption", "")
    caption_html = f"\n  <figcaption>{escape(caption)}</figcaption>" if caption else ""
    return f'''\n<!-- visual:start:{escape(visual_id, quote=True)} -->
<figure class="guide-visual guide-visual--{escape(css_type, quote=True)}" data-visual-id="{escape(visual_id, quote=True)}" data-asset-mode="{escape(asset_mode, quote=True)}">
  <img src="{escape(asset_url, quote=True)}" alt="{escape(spec['alt'], quote=True)}" loading="lazy" decoding="async" width="{width}" height="{height}">{caption_html}
</figure>
<!-- visual:end:{escape(visual_id, quote=True)} -->\n'''


def strip_existing_visuals(html: str) -> str:
    block_re = re.compile(
        r"\s*<!-- visual:start:[^>]+ -->.*?<!-- visual:end:[^>]+ -->\s*",
        re.S,
    )
    return block_re.sub("\n", html)


def apply(spec: dict) -> None:
    page = page_path(spec["page_url"])
    if not page.exists():
        raise SystemExit(f"Missing guide page: {page}")

    html = page.read_text(encoding="utf-8")
    if 'name="robots" content="noindex,follow"' not in html:
        raise SystemExit(f"{page}: noindex,follow missing")

    # Always remove any previously injected guide visual first. This allows a
    # page to move cleanly from a diagram to no_visual or editorial_image.
    html = strip_existing_visuals(html)

    asset_mode = spec.get("asset_mode", "functional_diagram")
    if asset_mode == "no_visual":
        page.write_text(html, encoding="utf-8")
        print(f"removed guide visual from {spec['page_url']} (no_visual)")
        return

    if asset_mode not in {"functional_diagram", "editorial_image"}:
        raise SystemExit(f"Unsupported asset_mode: {asset_mode}")

    asset = ROOT / spec["output"]
    if not asset.exists():
        raise SystemExit(f"Visual asset missing: {asset}")

    if spec.get("after_section_id"):
        section_id = re.escape(spec["after_section_id"])
        heading = re.search(rf'<h2\s+id="{section_id}"[^>]*>.*?</h2>', html, re.S | re.I)
        if not heading:
            raise SystemExit(f"Insertion section not found: {spec['after_section_id']}")
        next_h2 = re.search(r"<h2\b", html[heading.end():], re.I)
        if not next_h2:
            raise SystemExit(f"{page}: could not find following H2")
        insert_at = heading.end() + next_h2.start()
    else:
        headings = list(re.finditer(r"<h2\b[^>]*>.*?</h2>", html, re.S | re.I))
        if len(headings) < 2:
            raise SystemExit(f"{page}: need at least two H2s for generic insertion")
        insert_at = headings[1].start()

    html = html[:insert_at] + figure_html(spec) + html[insert_at:]
    page.write_text(html, encoding="utf-8")
    print(f"injected {spec['id']} into {spec['page_url']}")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        args = [str(path.relative_to(ROOT)) for path in sorted((ROOT / ".content" / "visuals").glob("*.json"))]
    for arg in args:
        apply(load_manifest(arg))


if __name__ == "__main__":
    main()
