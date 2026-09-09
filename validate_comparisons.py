#!/usr/bin/env python3
from pathlib import Path
import json
import math
import re
import sys
from html import unescape

ROOT = Path(__file__).resolve().parent
COMPARISONS = ROOT / '.content' / 'comparisons'

TAG_RE = re.compile(r'<[^>]+>', re.S)
H1_RE = re.compile(r'<h1\b[^>]*>(.*?)</h1>', re.S | re.I)
HEADING_RE = re.compile(r'<h([1-6])\b[^>]*>(.*?)</h\1>', re.S | re.I)
LINK_RE = re.compile(r'<a\b[^>]*href="([^"]+)"', re.I)
SOURCE_RE = re.compile(r'<a\b[^>]*href="https?://', re.I)
CANONICAL_RE = re.compile(r'<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"', re.I)
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S | re.I)
META_DESC_RE = re.compile(r'<meta\b[^>]*name="description"[^>]*content="([^"]*)"', re.I)
ROBOTS_RE = re.compile(r'<meta\b[^>]*name="robots"[^>]*content="([^"]*)"', re.I)

ALLOWED_EVIDENCE = {
    'VERIFIED',
    'SUPPORTED',
    'INFERRED',
    'USER_PATTERN',
    'FIRST_HAND',
    'UNKNOWN',
    'PROHIBITED',
}

RANKABLE_STATUSES = {'ELIGIBLE', 'CONDITIONALLY_ELIGIBLE'}

EDITOR_FACING_PATTERNS = {
    'editor-facing comparison strategy': [
        r'\bce comparatif\b.{0,100}\b(?:sert|doit|permet)\b',
        r'\bcette page\b.{0,100}\b(?:sert|doit|permet)\b',
        r'\bce contenu\b.{0,100}\b(?:sert|doit|permet)\b',
        r'\bmaillage interne\b',
        r'\bintention de recherche\b',
        r'\boptimis(?:er|é|ée|ation) (?:pour )?(?:le )?seo\b',
        r'\boptimis(?:er|é|ée|ation) (?:pour )?(?:le )?geo\b',
    ],
    'template/meta commentary': [
        r'\bdans cet article,? nous allons\b',
        r'\bcette section (?:présente|explique|permet|sert)\b',
        r'\bvoici ce que (?:la page|ce comparatif)\b',
    ],
}

FAKE_HANDS_ON_PATTERNS = [
    r'\bnous avons testé\b',
    r'\blors de notre test\b',
    r'\bpendant notre test\b',
    r'\baprès (?:plusieurs|quelques) semaines? d[’\']utilisation\b',
    r'\bnous avons mesuré\b',
    r'\bnous avons constaté\b',
]

HIGH_SLOP_PATTERNS = {
    'generic filler': [
        r'\bdans un monde où\b',
        r'\bil est important de (?:noter|souligner|comprendre|savoir)\b',
        r'\bil convient de (?:noter|souligner|rappeler)\b',
        r'\bque vous soyez\b',
        r'\ben conclusion\b',
    ],
    'unsupported promotional wording': [
        r'\bsolution idéale\b',
        r'\bchoix parfait\b',
        r'\bexpérience exceptionnelle\b',
        r'\bproduit incontournable\b',
    ],
}

GENERIC_SCORE_PATTERNS = [
    r'^official capabilities reviewed for .+; numeric score is an editorial normalization for .+\.?$',
    r'^score éditorial normalisé à partir (?:des|de) capacités officielles',
    r'^note éditoriale basée sur les caractéristiques officielles',
]


def clean(raw):
    return re.sub(r'\s+', ' ', unescape(TAG_RE.sub(' ', raw))).strip()


def normalized_text(raw):
    return clean(raw).lower().replace('’', "'")


def find_matches(text, patterns):
    return [pattern for pattern in patterns if re.search(pattern, text, re.I)]


def heading_levels(fragment):
    return [int(level) for level, _ in HEADING_RE.findall(fragment)]


def has_heading_jump(levels):
    if not levels:
        return False
    previous = levels[0]
    for level in levels[1:]:
        if level > previous + 1:
            return True
        previous = level
    return False


def as_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def generic_score_justification(text):
    text = re.sub(r'\s+', ' ', (text or '').strip().lower())
    return any(re.search(pattern, text, re.I) for pattern in GENERIC_SCORE_PATTERNS)


def expected_score(record, product_id):
    score_map = record.get('scores', {}).get(product_id, {})
    total = 0.0
    for criterion in record.get('criteria', []):
        criterion_id = criterion.get('id')
        weight = criterion.get('weight')
        item = score_map.get(criterion_id, {})
        score = item.get('score')
        if not as_number(weight) or not as_number(score):
            return None
        total += score * weight / 10.0
    return total


def score_decimal_places(value):
    if not isinstance(value, float):
        return 0
    text = f'{value:.10f}'.rstrip('0').rstrip('.')
    return len(text.split('.', 1)[1]) if '.' in text else 0


failures = {}
warnings = {}
records = sorted(COMPARISONS.glob('*.json'))

if not records:
    print('FAIL — no comparison methodology records found')
    raise SystemExit(1)

for fp in records:
    record = json.loads(fp.read_text(encoding='utf-8'))
    slug = fp.stem
    url = record.get('url') or f'/comparatifs/{slug}/'
    issues = []
    notes = []

    # Source-of-truth integrity.
    if record.get('slug') != slug:
        issues.append(f'slug mismatch: {record.get("slug")!r}')

    intent = record.get('intent')
    if not isinstance(intent, dict) or not intent.get('query') or not intent.get('type') or not intent.get('user_job'):
        issues.append('intent contract incomplete (query/type/user_job required)')

    criteria = record.get('criteria')
    if not isinstance(criteria, list) or not criteria:
        issues.append('criteria missing')
        criteria = []

    criterion_ids = [c.get('id') for c in criteria]
    if any(not cid for cid in criterion_ids) or len(criterion_ids) != len(set(criterion_ids)):
        issues.append('criterion ids missing or duplicated')

    weights = [c.get('weight') for c in criteria]
    if any(not as_number(weight) or weight <= 0 for weight in weights):
        issues.append('criterion weights must be positive numbers')
    elif not math.isclose(sum(weights), 100.0, abs_tol=0.001):
        issues.append(f'criterion weights sum to {sum(weights)}, expected 100')

    if record.get('affiliate_commission_used_in_ranking') is not False:
        issues.append('affiliate commission must be explicitly excluded from ranking')

    universe = record.get('product_universe')
    if not isinstance(universe, list) or not universe:
        issues.append('product universe missing')
        universe = []

    universe_by_id = {}
    for product in universe:
        product_id = product.get('id')
        if not product_id:
            issues.append('product universe contains product without id')
            continue
        if product_id in universe_by_id:
            issues.append(f'duplicate product id in universe: {product_id}')
        universe_by_id[product_id] = product
        if not product.get('name'):
            issues.append(f'{product_id}: product name missing')
        if not product.get('status'):
            issues.append(f'{product_id}: product status missing')
        if product.get('status') in RANKABLE_STATUSES and not product.get('source'):
            issues.append(f'{product_id}: rankable product has no source')

    ranking = record.get('ranking')
    if not isinstance(ranking, list) or not ranking:
        issues.append('ranking missing')
        ranking = []

    ranks = [item.get('rank') for item in ranking]
    ranked_ids = [item.get('product_id') for item in ranking]
    if any(not isinstance(rank, int) for rank in ranks):
        issues.append('ranking contains invalid rank values')
    elif ranks != list(range(1, len(ranking) + 1)):
        issues.append(f'ranks must be contiguous starting at 1, got {ranks}')

    if len(ranked_ids) != len(set(ranked_ids)):
        issues.append('ranking contains duplicate products')

    score_map = record.get('scores')
    if not isinstance(score_map, dict):
        issues.append('scores missing')
        score_map = {}

    generic_justifications = []
    inferred_but_marked_verified = []

    for product_id in ranked_ids:
        product = universe_by_id.get(product_id)
        if product is None:
            issues.append(f'ranked product absent from universe: {product_id}')
            continue
        if product.get('status') not in RANKABLE_STATUSES:
            issues.append(f'{product_id}: ranked despite non-rankable status {product.get("status")}')

        product_scores = score_map.get(product_id)
        if not isinstance(product_scores, dict):
            issues.append(f'{product_id}: score map missing')
            continue

        for criterion in criteria:
            criterion_id = criterion.get('id')
            item = product_scores.get(criterion_id)
            if not isinstance(item, dict):
                issues.append(f'{product_id}/{criterion_id}: score entry missing')
                continue

            score = item.get('score')
            if not as_number(score) or score < 0 or score > 10:
                issues.append(f'{product_id}/{criterion_id}: score must be between 0 and 10')

            evidence = item.get('evidence_class')
            if evidence not in ALLOWED_EVIDENCE:
                issues.append(f'{product_id}/{criterion_id}: invalid evidence class {evidence!r}')
            if evidence == 'PROHIBITED':
                issues.append(f'{product_id}/{criterion_id}: PROHIBITED evidence cannot support a published score')

            justification = (item.get('justification') or '').strip()
            if not justification:
                issues.append(f'{product_id}/{criterion_id}: score justification missing')
            elif generic_score_justification(justification):
                generic_justifications.append(f'{product_id}/{criterion_id}')

            if evidence == 'VERIFIED' and 'editorial normalization' in justification.lower():
                inferred_but_marked_verified.append(f'{product_id}/{criterion_id}')

    # Mathematical integrity: the stored ranking must be reproducible from the stored weights/scores.
    calculated = []
    for item in ranking:
        product_id = item.get('product_id')
        stored = item.get('score')
        calc = expected_score(record, product_id)
        if not as_number(stored):
            issues.append(f'{product_id}: ranking score missing or invalid')
            continue
        if calc is None:
            continue
        if not math.isclose(stored, calc, abs_tol=0.011):
            issues.append(f'{product_id}: stored ranking score {stored} does not match recalculated {calc:.3f}')
        calculated.append((product_id, calc))

        if score_decimal_places(stored) > 1:
            notes.append(f'{product_id}: ranking stores {stored}; verify that displayed precision does not imply false certainty')

    if calculated:
        expected_order = [product_id for product_id, _ in sorted(calculated, key=lambda pair: pair[1], reverse=True)]
        actual_order = [product_id for product_id, _ in calculated]
        if actual_order != expected_order:
            issues.append(f'ranking order does not match recalculated scores: expected {expected_order}, got {actual_order}')

    if generic_justifications:
        notes.append(
            f'{len(generic_justifications)} score justifications are generic boilerplate; '
            'comparison-editorial-publish-gate must treat an important unsupported note as a blocker'
        )

    if inferred_but_marked_verified:
        notes.append(
            f'{len(inferred_but_marked_verified)} scores are marked VERIFIED while their justification calls the score an editorial normalization; '
            'verify fact evidence vs score inference separately'
        )

    if 'hard_gates' not in record:
        notes.append('no explicit hard_gates field in methodology record; verify eliminatory constraints manually')

    excluded = [p for p in universe if p.get('status') not in RANKABLE_STATUSES]
    if not excluded:
        notes.append('no excluded/conditional candidate recorded; verify that the product universe was considered before ranking')

    researched_at = record.get('researched_at')
    if not researched_at:
        issues.append('researched_at missing')

    # User-facing page integrity.
    page = ROOT / url.strip('/') / 'index.html'
    if not page.exists():
        failures[url] = issues + ['page missing']
        if notes:
            warnings[url] = notes
        continue

    html = page.read_text(encoding='utf-8')
    raw_html_lower = html.lower()
    article_match = re.search(r'<article class="content-main">(.*?)</article>', html, re.S | re.I)
    if not article_match:
        issues.append('article.content-main missing')
        failures[url] = issues
        if notes:
            warnings[url] = notes
        continue

    body = article_match.group(1)
    body_text = normalized_text(body)

    if '<!-- contenu à rédiger -->' in raw_html_lower or 'contenu en préparation' in raw_html_lower:
        issues.append('placeholder/preparation marker remains')

    robots = ROBOTS_RE.search(html)
    if not robots or 'noindex' not in robots.group(1).lower():
        issues.append('draft must remain noindex until human validation')

    titles = TITLE_RE.findall(html)
    if len(titles) != 1 or not clean(titles[0]):
        issues.append('missing or invalid title')

    descriptions = META_DESC_RE.findall(html)
    if len(descriptions) != 1 or not clean(descriptions[0]):
        issues.append('missing or invalid meta description')

    canonicals = CANONICAL_RE.findall(html)
    if len(canonicals) != 1:
        issues.append('missing or duplicate canonical')

    h1s = [clean(x) for x in H1_RE.findall(html)]
    if len(h1s) != 1:
        issues.append(f'expected exactly one H1, found {len(h1s)}')

    editorial_levels = ([1] if len(h1s) == 1 else []) + heading_levels(body)
    if has_heading_jump(editorial_levels):
        issues.append('article heading hierarchy skips a level')

    for label, patterns in EDITOR_FACING_PATTERNS.items():
        if find_matches(body_text, patterns):
            issues.append(f'{label} detected')

    for label, patterns in HIGH_SLOP_PATTERNS.items():
        if find_matches(body_text, patterns):
            issues.append(f'high-risk generic writing pattern: {label}')

    if find_matches(body_text, FAKE_HANDS_ON_PATTERNS):
        issues.append('unsupported first-hand test language detected')

    # No arbitrary H2/link/source count. We only block total absence of evidence/navigation primitives.
    if len(SOURCE_RE.findall(body)) == 0:
        issues.append('no external source found in article')

    internal_links = [href for href in LINK_RE.findall(body) if href.startswith('/')]
    if not internal_links:
        notes.append('no internal link found; verify useful next-step navigation manually')

    # Ranked products should normally be represented in the reader-facing analysis.
    for product_id in ranked_ids:
        product_name = (universe_by_id.get(product_id) or {}).get('name')
        if product_name and product_name.lower() not in body_text:
            notes.append(f'{product_name}: ranked product name not found verbatim in article; verify rendering/alias manually')

    # Tight score margins need a conditionality check; this is intentionally a warning for the manual gate.
    if len(ranking) >= 2 and as_number(ranking[0].get('score')) and as_number(ranking[1].get('score')):
        margin = ranking[0]['score'] - ranking[1]['score']
        if margin <= 0.3:
            notes.append(f'top-two score margin is only {margin:.2f}; manual gate must test sensitivity and avoid false certainty')

    if issues:
        failures[url] = issues
    if notes:
        warnings[url] = notes

if warnings:
    print('WARNINGS — comparison publish-gate review required')
    for url, notes in warnings.items():
        print('WARN', url)
        for note in notes:
            print('  -', note)
    print()

if failures:
    print('FAIL — machine-detectable comparison blockers found')
    for url, issues in failures.items():
        print('FAIL', url)
        for issue in issues:
            print('  -', issue)
    print()
    print('A machine PASS is only a structural/mathematical floor. Run comparison-editorial-publish-gate and obtain human validation before removing noindex.')
    raise SystemExit(1)

print(f'PASS: {len(records)} comparison pages have no machine-detectable publication blockers')
print('NEXT: run .agents/skills/comparison-editorial-publish-gate/SKILL.md on every page before human validation and indexation')
