#!/usr/bin/env python3
from pathlib import Path
import re
from brand_pages import PAGES
from brand_data import VERIFIED_AT

ROOT = Path(__file__).resolve().parent


def html_path(url):
    rel = url.strip('/')
    return ROOT / rel / 'index.html' if rel else ROOT / 'index.html'


def replace_first(pattern, repl, text, flags=0, required=True):
    out, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if required and count != 1:
        raise SystemExit(f'Expected one match for {pattern!r}, got {count}')
    return out


for url, page_data in PAGES.items():
    page = html_path(url)
    if not page.exists():
        raise SystemExit(f'Missing brand page: {page}')

    html = page.read_text(encoding='utf-8')
    title = page_data['title']
    description = page_data['description']
    body = page_data['body'].strip()

    html = replace_first(r'<title>.*?</title>', f'<title>{title}</title>', html, re.S)
    html = replace_first(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{description}">',
        html,
    )
    html = replace_first(r'<h1>.*?</h1>', f'<h1>{title}</h1>', html, re.S)
    html = replace_first(
        r'<p class="lead">.*?</p>',
        f'<p class="lead">{description}</p>',
        html,
        re.S,
    )

    article_section = f'''\n<section class="section">\n  <div class="container">\n    <div class="content-layout">\n      <article class="content-main">\n      {body}\n      </article>\n    </div>\n  </div>\n</section>\n'''

    main_pattern = r'(<section class="page-hero">.*?</section>)(.*?)(</main>)'
    m = re.search(main_pattern, html, re.S)
    if not m:
        raise SystemExit(f'Unable to locate hero/main boundary: {url}')
    html = html[:m.end(1)] + article_section + html[m.start(3):]

    html = html.replace(
        '<span class="page-meta-item">Contenu en préparation</span>',
        f'<span class="page-meta-item">Sources vérifiées le {VERIFIED_AT}</span>'
    )

    if '<!-- Contenu à rédiger -->' in html:
        raise SystemExit(f'Placeholder still present: {url}')
    if 'name="robots" content="noindex,follow"' not in html:
        raise SystemExit(f'noindex removed: {url}')
    if '<article class="content-main">' not in html:
        raise SystemExit(f'content-main absent after render: {url}')

    page.write_text(html, encoding='utf-8')
    print('updated', url)
