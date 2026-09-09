#!/usr/bin/env python3
from pathlib import Path
import re

from comparison_content import COMPARISON_CONTENT
from comparison_content_professional import PROFESSIONAL_CONTENT

ROOT = Path(__file__).resolve().parent
COMPARISON_CONTENT = dict(COMPARISON_CONTENT)
COMPARISON_CONTENT["bloc-notes-numerique-professionnel"] = PROFESSIONAL_CONTENT

for slug, body in COMPARISON_CONTENT.items():
    page = ROOT / "comparatifs" / slug / "index.html"
    if not page.exists():
        raise SystemExit(f"Missing comparison page: {page}")
    html = page.read_text(encoding="utf-8")
    m = re.search(r'(<article class="content-main">)(.*?)(</article>)', html, re.S)
    if not m:
        raise SystemExit(f"article.content-main missing: {slug}")
    html = html[:m.start(2)] + "\n      " + body + "\n    " + html[m.end(2):]

    if slug == "bloc-notes-numerique-professionnel":
        html = re.sub(
            r'<title>.*?</title>',
            '<title>Meilleur bloc-notes numérique professionnel : BOOX, Supernote ou reMarkable ?</title>',
            html,
            count=1,
            flags=re.S,
        )
        html = re.sub(
            r'<meta name="description" content="[^"]*">',
            '<meta name="description" content="Comparatif professionnel : BOOX, Supernote et reMarkable selon applications, organisation, PDF, export, contraintes IT et coût réel.">',
            html,
            count=1,
        )
        html = re.sub(
            r'<h1>.*?</h1>',
            '<h1>Meilleur bloc-notes numérique professionnel : BOOX, Supernote ou reMarkable ?</h1>',
            html,
            count=1,
            flags=re.S,
        )
        html = re.sub(
            r'<p class="lead">.*?</p>',
            '<p class="lead">BOOX si les applications et l’ouverture priment, Supernote si l’organisation manuscrite compte davantage : un comparatif conditionnel fondé sur des sources officielles.</p>',
            html,
            count=1,
            flags=re.S,
        )
        html = re.sub(
            r'<span class="page-meta-item">.*?</span>',
            '<span class="page-meta-item">Vérifié le 9 septembre 2026</span>',
            html,
            count=1,
            flags=re.S,
        )

    if '<!-- Contenu à rédiger -->' in html:
        raise SystemExit(f"Placeholder still present: {slug}")
    if 'name="robots" content="noindex,follow"' not in html:
        raise SystemExit(f"noindex removed: {slug}")
    page.write_text(html, encoding="utf-8")
    print("updated", slug)
