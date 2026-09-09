#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
FAIL = []
WARN = []

ALLOWED_EVIDENCE = {
    'VERIFIED', 'SUPPORTED', 'INFERRED', 'USER_PATTERN', 'FIRST_HAND',
    'UNKNOWN', 'OUTDATED', 'CONTRADICTED'
}


def fail(label):
    FAIL.append(label)


for fp in sorted((ROOT / '.content' / 'comparisons').glob('*.json')):
    try:
        data = json.loads(fp.read_text(encoding='utf-8'))
    except Exception as exc:
        fail(f'{fp.name}: invalid json ({exc})')
        continue

    slug = data.get('slug') or fp.stem
    url = data.get('url')
    intent = data.get('intent')
    criteria = data.get('criteria')
    universe = data.get('product_universe')
    scores = data.get('scores')
    ranking = data.get('ranking')

    if not isinstance(url, str) or not url.startswith('/comparatifs/'):
        fail(f'{fp.name}: comparison url')
    if not isinstance(intent, dict) or not intent.get('query') or not intent.get('user_job'):
        fail(f'{fp.name}: intent')

    if not isinstance(criteria, list) or not criteria:
        fail(f'{fp.name}: criteria')
        criteria = []
    criterion_ids = [c.get('id') for c in criteria if isinstance(c, dict)]
    if len(criterion_ids) != len(criteria) or any(not x for x in criterion_ids):
        fail(f'{fp.name}: criterion ids')
    if len(set(criterion_ids)) != len(criterion_ids):
        fail(f'{fp.name}: duplicate criteria')
    weights = [c.get('weight') for c in criteria if isinstance(c, dict)]
    if len(weights) != len(criteria) or any(not isinstance(w, (int, float)) for w in weights):
        fail(f'{fp.name}: criterion weights')
    elif abs(sum(weights) - 100) > 1e-9:
        fail(f'{fp.name}: weights must sum to 100')

    if not isinstance(universe, list) or len(universe) < 2:
        fail(f'{fp.name}: product universe')
        universe = []
    universe_ids = [p.get('id') for p in universe if isinstance(p, dict)]
    if len(universe_ids) != len(universe) or any(not x for x in universe_ids):
        fail(f'{fp.name}: product ids')
    if len(set(universe_ids)) != len(universe_ids):
        fail(f'{fp.name}: duplicate product ids')
    for product in universe:
        if not isinstance(product, dict):
            continue
        if not product.get('name') or not product.get('status'):
            fail(f'{fp.name}: incomplete product universe entry')
        if product.get('status') in {'ELIGIBLE', 'CONDITIONALLY_ELIGIBLE'} and not product.get('source'):
            fail(f'{fp.name}: eligible product without source ({product.get("id")})')

    if data.get('affiliate_commission_used_in_ranking') is not False:
        fail(f'{fp.name}: affiliate commission must not affect ranking')

    if not isinstance(scores, dict) or not scores:
        fail(f'{fp.name}: scores')
        scores = {}
    if not isinstance(ranking, list) or not ranking:
        fail(f'{fp.name}: ranking')
        ranking = []

    ranking_ids = []
    for row in ranking:
        if not isinstance(row, dict):
            fail(f'{fp.name}: malformed ranking row')
            continue
        product_id = row.get('product_id')
        ranking_ids.append(product_id)
        if product_id not in universe_ids:
            fail(f'{fp.name}: ranked product outside universe ({product_id})')
        if not isinstance(row.get('rank'), int) or row.get('rank') < 1:
            fail(f'{fp.name}: invalid rank ({product_id})')
        if not isinstance(row.get('score'), (int, float)):
            fail(f'{fp.name}: missing ranking score ({product_id})')

        product_scores = scores.get(product_id)
        if not isinstance(product_scores, dict):
            fail(f'{fp.name}: scores missing for ranked product ({product_id})')
            continue
        for criterion_id in criterion_ids:
            cell = product_scores.get(criterion_id)
            if not isinstance(cell, dict):
                fail(f'{fp.name}: score missing {product_id}/{criterion_id}')
                continue
            value = cell.get('score')
            evidence = cell.get('evidence_class')
            justification = cell.get('justification')
            if not isinstance(value, (int, float)) or not (0 <= value <= 10):
                fail(f'{fp.name}: invalid score {product_id}/{criterion_id}')
            if evidence not in ALLOWED_EVIDENCE:
                fail(f'{fp.name}: invalid evidence class {product_id}/{criterion_id}')
            if evidence in {'UNKNOWN', 'CONTRADICTED', 'OUTDATED'}:
                fail(f'{fp.name}: unstable evidence used in ranking {product_id}/{criterion_id}')
            if not isinstance(justification, str) or not justification.strip():
                fail(f'{fp.name}: score without justification {product_id}/{criterion_id}')

    if len(set(ranking_ids)) != len(ranking_ids):
        fail(f'{fp.name}: duplicate ranked products')
    ranks = [r.get('rank') for r in ranking if isinstance(r, dict) and isinstance(r.get('rank'), int)]
    if ranks and sorted(ranks) != list(range(1, len(ranks) + 1)):
        fail(f'{fp.name}: non-contiguous ranking')

    if not data.get('methodology_note'):
        WARN.append(f'{fp.name}: methodology note absent')

    page = ROOT / 'comparatifs' / slug / 'index.html'
    if not page.exists():
        fail(f'{fp.name}: page missing')
        continue
    html = page.read_text(encoding='utf-8')
    article = re.search(r'<article class="content-main">(.*?)</article>', html, re.S | re.I)
    if not article:
        fail(f'{slug}: article.content-main')
        continue
    body = article.group(1)

    if '<!-- Contenu à rédiger -->' in body or 'Contenu en préparation' in body:
        fail(f'{slug}: placeholder')
    if 'name="robots" content="noindex,follow"' not in html:
        fail(f'{slug}: noindex removed')
    if len(re.findall(r'<h1\b', html, re.I)) != 1:
        fail(f'{slug}: expected exactly one H1')
    if not re.search(r'<link rel="canonical" href="https://bloc-notes-numeriques\.fr/comparatifs/[^\"]+/">', html, re.I):
        fail(f'{slug}: canonical')
    if not re.search(r'href="https?://', body, re.I):
        fail(f'{slug}: no external evidence source rendered')

    fake_hands_on = re.search(
        r'\b(?:nous avons testé|nous avons mesuré|après (?:plusieurs|quelques) (?:jours|semaines) de test|lors de notre test)\b',
        re.sub(r'<[^>]+>', ' ', body),
        re.I,
    )
    if fake_hands_on:
        fail(f'{slug}: possible undocumented hands-on language')

if WARN:
    print('\n'.join('WARN ' + x for x in WARN))
if FAIL:
    print('\n'.join('FAIL ' + x for x in FAIL))
    sys.exit(1)

print('PASS: comparison pages have no machine-detectable methodology or publication blockers')
print('NEXT: run .agents/skills/comparison-analysis-workflow/SKILL.md in PUBLISH_REVIEW mode before human validation and indexation')
