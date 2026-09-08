#!/usr/bin/env python3
from pathlib import Path
import json
import re
from brand_pages import PAGES
from brand_data import VERIFIED_AT, BRANDS

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '.content' / 'brands'
REVIEWS = ROOT / '.content' / 'reviews'
OUT.mkdir(parents=True, exist_ok=True)
REVIEWS.mkdir(parents=True, exist_ok=True)

H2_RE = re.compile(r'<h2\b[^>]*>(.*?)</h2>', re.S | re.I)
LINK_RE = re.compile(r'<a\b[^>]*href="(/[^"]+)"', re.I)
SOURCE_RE = re.compile(r'<a\b[^>]*href="(https?://[^"]+)"', re.I)
TAG_RE = re.compile(r'<[^>]+>', re.S)


def text(raw):
    return re.sub(r'\s+', ' ', TAG_RE.sub(' ', raw)).strip()


def slug_for(url):
    rel = url.strip('/')
    return rel.replace('/', '--') or 'home'

for url, spec in PAGES.items():
    path = ROOT / url.strip('/') / 'index.html'
    html = path.read_text(encoding='utf-8')
    article = re.search(r'<article class="content-main">(.*?)</article>', html, re.S)
    body = article.group(1) if article else ''
    record = {
        'url': url,
        'title': spec['title'],
        'page_type': spec['page_type'],
        'brand': spec['brand'],
        'verified_at': VERIFIED_AT,
        'h2': [text(x) for x in H2_RE.findall(body)],
        'internal_links': LINK_RE.findall(body),
        'unique_internal_targets': sorted(set(LINK_RE.findall(body))),
        'official_sources': SOURCE_RE.findall(body),
        'noindex_follow': 'name="robots" content="noindex,follow"' in html,
        'analysis_documentary': 'analyse documentaire' in text(body).lower(),
    }
    (OUT / f'{slug_for(url)}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')

    review = f'''# Brand QA — {url}\n\n- Page type: `{spec['page_type']}`\n- Brand: `{spec['brand']}`\n- Sources verified: {VERIFIED_AT}\n- H2 count: {len(record['h2'])}\n- Internal links: {len(record['internal_links'])}\n- Unique targets: {len(record['unique_internal_targets'])}\n- Official sources: {len(record['official_sources'])}\n- Robots: `noindex,follow`\n\n## Editorial gates\n\n- Entity / range / ecosystem: represented in source data and rendered according to page type.\n- Fact-check: official manufacturer sources are recorded; source presence does not by itself prove every claim.\n- Review integrity: no first-hand test may be inferred unless explicitly documented.\n- Humanizer / natural writing / anti-AI-slop / GEO: require editorial review and are not automatically marked PASS by this file.\n\n## Status\n\n`DRAFT_READY`\n'''
    (REVIEWS / f'{slug_for(url)}-brand.md').write_text(review, encoding='utf-8')

for key, brand in BRANDS.items():
    summary = {
        'brand': key,
        'name': brand['name'],
        'positioning': brand['positioning'],
        'current_range': brand['current_range'],
        'ecosystem': brand['ecosystem'],
        'strengths': brand['strengths'],
        'limits': brand['limits'],
        'choose': brand['choose'],
        'avoid': brand['avoid'],
        'verified_at': VERIFIED_AT,
    }
    (OUT / f'entity-{key}.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')

print(f'generated metadata for {len(PAGES)} brand pages')
