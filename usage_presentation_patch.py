#!/usr/bin/env python3
"""Small presentation patch applied after Usage editorial rendering."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
fp = ROOT / "usages" / "index.html"
html = fp.read_text(encoding="utf-8")
html = html.replace(
    '<a href="/usages/prise-de-notes-professionnelle/" class="hub-link"><span>Travail et réunions</span>',
    '<a href="/usages/prise-de-notes-professionnelle/" class="hub-link"><span>Travail / usage professionnel</span>',
)
fp.write_text(html, encoding="utf-8")
print("usage hub role labels aligned")
