#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_manifest(path: str) -> dict:
    manifest = Path(path)
    if not manifest.is_absolute():
        manifest = ROOT / manifest
    return json.loads(manifest.read_text(encoding="utf-8"))


def page_path(page_url: str) -> Path:
    return ROOT / page_url.strip("/") / "index.html"


def figure_html(spec: dict) -> str:
    asset_url = "/" + spec["output"].lstrip("/")
    width = int(spec.get("canvas", {}).get("width", 1200))
    height = int(spec.get("canvas", {}).get("height", 900))
    visual_id = spec["id"]
    return f'''\n      <!-- visual:start:{visual_id} -->
      <figure class="guide-visual guide-visual--{spec['type']}" data-visual-id="{visual_id}">
        <img src="{asset_url}" alt="{spec['alt']}" loading="lazy" decoding="async" width="{width}" height="{height}">
        <figcaption>{spec['caption']}</figcaption>
      </figure>
      <!-- visual:end:{visual_id} -->\n'''


def apply(spec: dict) -> None:
    page = page_path(spec["page_url"])
    if not page.exists():
        raise SystemExit(f"Missing guide page: {page}")

    asset = ROOT / spec["output"]
    if not asset.exists():
        raise SystemExit(f"Generated visual asset missing: {asset}")

    html = page.read_text(encoding="utf-8")
    if 'name="robots" content="noindex,follow"' not in html:
        raise SystemExit("Pilot page lost noindex,follow")

    visual_id = re.escape(spec["id"])
    block_re = re.compile(
        rf"\s*<!-- visual:start:{visual_id} -->.*?<!-- visual:end:{visual_id} -->\s*",
        re.S,
    )
    html = block_re.sub("\n", html)

    section_id = re.escape(spec["after_section_id"])
    heading = re.search(rf'<h2\s+id="{section_id}"[^>]*>.*?</h2>', html, re.S | re.I)
    if not heading:
        raise SystemExit(f"Insertion section not found: {spec['after_section_id']}")

    next_h2 = re.search(r"<h2\b", html[heading.end():], re.I)
    if not next_h2:
        raise SystemExit("Could not find following H2 for insertion")
    insert_at = heading.end() + next_h2.start()

    html = html[:insert_at] + figure_html(spec) + html[insert_at:]
    page.write_text(html, encoding="utf-8")
    print(f"injected {spec['id']} into {spec['page_url']}")


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: apply_guide_visuals.py .content/visuals/<slug>.json")
    apply(load_manifest(sys.argv[1]))


if __name__ == "__main__":
    main()
