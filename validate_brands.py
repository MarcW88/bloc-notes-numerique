#!/usr/bin/env python3
from pathlib import Path
import re
from brand_pages import PAGES

ROOT = Path(__file__).resolve().parent
TAG_RE = re.compile(r'<[^>]+>', re.S)
H2_RE = re.compile(r'<h2\b[^>]*>(.*?)</h2>', re.S | re.I)
LINK_RE = re.compile(r'<a\b[^>]*href="(/[^"]+)"', re.I)
SOURCE_RE = re.compile(r'<a\b[^>]*href="https?://', re.I)

MIN_H2 = {
    'DIRECTORY': 5,
    'BRAND_HUB': 8,
    'PRODUCT': 8,
    'REVIEW': 9,
    'SERVICE': 7,
    'ACCESSORY_HUB': 7,
    'ALTERNATIVES': 7,
}


def clean(raw):
    return re.sub(r'\s+', ' ', TAG_RE.sub(' ', raw)).strip()

failures = {}
for url, spec in PAGES.items():
    page = ROOT / url.strip('/') / 'index.html'
    issues = []
    if not page.exists():
        failures[url] = ['page missing']
        continue
    html = page.read_text(encoding='utf-8')
    m = re.search(r'<article class="content-main">(.*?)</article>', html, re.S)
    if not m:
        failures[url] = ['article.content-main missing']
        continue
    body = m.group(1)
    body_text = clean(body).lower()
    h2 = [clean(x) for x in H2_RE.findall(body)]
    internal = LINK_RE.findall(body)
    unique = set(internal)
    sources = len(SOURCE_RE.findall(body))

    if '<!-- Contenu à rédiger -->' in html or 'Contenu en préparation' in html:
        issues.append('placeholder/preparation marker remains')
    if 'name="robots" content="noindex,follow"' not in html:
        issues.append('noindex,follow missing')
    if 'class="article-answer"' not in body:
        issues.append('answer-first block missing')
    if len(h2) < MIN_H2.get(spec['page_type'], 7):
        issues.append(f'not enough H2: {len(h2)}')
    if len(internal) < 6:
        issues.append(f'not enough internal links: {len(internal)}')
    if len(unique) < 5:
        issues.append(f'not enough unique internal targets: {len(unique)}')
    if sources < 3:
        issues.append(f'not enough official sources: {sources}')
    if spec['page_type'] != 'DIRECTORY' and not any(k in body_text for k in ['limite', 'à éviter', 'éviter', 'moins adapté']):
        issues.append('meaningful limitation/avoid language missing')
    if spec['page_type'] in {'BRAND_HUB','PRODUCT','REVIEW'} and not any(k in body_text for k in ['à privilégier', 'pour qui', 'cohérent']):
        issues.append('choose/use-case guidance missing')
    if spec['page_type'] == 'REVIEW':
        if 'analyse documentaire' not in body_text:
            issues.append('review is not explicitly documentary')
        if any(k in body_text for k in ['nous avons testé', 'lors de notre test', 'pendant notre test']):
            issues.append('first-hand test wording detected')

    if issues:
        failures[url] = issues

if failures:
    for url, issues in failures.items():
        print('FAIL', url)
        for issue in issues:
            print('  -', issue)
    raise SystemExit(1)

print(f'PASS: {len(PAGES)} brand pages meet the structural quality floor')
