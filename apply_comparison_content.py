#!/usr/bin/env python3
from pathlib import Path
import re
from comparison_content import COMPARISON_CONTENT
ROOT=Path(__file__).resolve().parent
for slug, body in COMPARISON_CONTENT.items():
    page=ROOT/'comparatifs'/slug/'index.html'
    if not page.exists():
        raise SystemExit(f'Missing comparison page: {page}')
    html=page.read_text(encoding='utf-8')
    m=re.search(r'(<article class="content-main">)(.*?)(</article>)', html, re.S)
    if not m:
        raise SystemExit(f'article.content-main missing: {slug}')
    html=html[:m.start(2)]+'\n      '+body+'\n    '+html[m.end(2):]
    if '<!-- Contenu à rédiger -->' in html:
        raise SystemExit(f'Placeholder still present: {slug}')
    if 'name="robots" content="noindex,follow"' not in html:
        raise SystemExit(f'noindex removed: {slug}')
    page.write_text(html,encoding='utf-8')
    print('updated',slug)
