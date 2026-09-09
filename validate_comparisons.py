#!/usr/bin/env python3
from pathlib import Path
import json
import math
import re
import sys
from html import unescape

from comparison_pages import COMPARISON_PAGES
from comparison_products import COMPARISON_PRODUCTS
from comparison_methodology import COMPARISON_METHODS

ROOT = Path(__file__).resolve().parent
COMPARISONS = ROOT / ".content" / "comparisons"

TAG_RE = re.compile(r"<[^>]+>", re.S)
H1_RE = re.compile(r"<h1\b[^>]*>(.*?)</h1>", re.S | re.I)
HEADING_RE = re.compile(r"<h([1-6])\b[^>]*>(.*?)</h\1>", re.S | re.I)
SOURCE_RE = re.compile(r'<a\b[^>]*href="https?://', re.I)
CANONICAL_RE = re.compile(r'<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"', re.I)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
META_DESC_RE = re.compile(r'<meta\b[^>]*name="description"[^>]*content="([^"]*)"', re.I)
ROBOTS_RE = re.compile(r'<meta\b[^>]*name="robots"[^>]*content="([^"]*)"', re.I)

ALLOWED_EVIDENCE = {
    "VERIFIED", "SUPPORTED", "INFERRED", "USER_PATTERN",
    "FIRST_HAND", "UNKNOWN", "PROHIBITED",
}
RANKABLE = {"ELIGIBLE", "CONDITIONALLY_ELIGIBLE"}

FAKE_HANDS_ON_PATTERNS = [
    r"\bnous avons testé\b",
    r"\blors de notre test\b",
    r"\bpendant notre test\b",
    r"\baprès (?:plusieurs|quelques) semaines? d[’']utilisation\b",
    r"\bnous avons mesuré\b",
    r"\bnous avons constaté\b",
]
EDITOR_FACING_PATTERNS = [
    r"\bmaillage interne\b",
    r"\bintention de recherche\b",
    r"\boptimis(?:er|é|ée|ation) (?:pour )?(?:le )?seo\b",
    r"\boptimis(?:er|é|ée|ation) (?:pour )?(?:le )?geo\b",
]
HIGH_SLOP_PATTERNS = [
    r"\bdans un monde où\b",
    r"\bil est important de (?:noter|souligner|comprendre|savoir)\b",
    r"\bil convient de (?:noter|souligner|rappeler)\b",
    r"\bque vous soyez\b",
    r"\ben conclusion\b",
    r"\bsolution idéale\b",
    r"\bchoix parfait\b",
    r"\bproduit incontournable\b",
]
GENERIC_SCORE_PATTERNS = [
    r"^official capabilities reviewed for .+; numeric score is an editorial normalization for .+\.?$",
    r"^score éditorial normalisé à partir (?:des|de) capacités officielles",
    r"^note éditoriale basée sur les caractéristiques officielles",
]


def clean(raw):
    return re.sub(r"\s+", " ", unescape(TAG_RE.sub(" ", raw))).strip()


def normalized_text(raw):
    return clean(raw).lower().replace("’", "'")


def is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def json_weighted_score(record, product_id):
    score_map = record.get("scores", {}).get(product_id, {})
    total = 0.0
    for criterion in record.get("criteria", []):
        cid = criterion.get("id")
        weight = criterion.get("weight")
        entry = score_map.get(cid)
        if not isinstance(entry, dict) or not is_number(weight) or not is_number(entry.get("score")):
            return None
        total += entry["score"] * weight
    return total / 100.0


def has_heading_jump(levels):
    if not levels:
        return False
    previous = levels[0]
    for level in levels[1:]:
        if level > previous + 1:
            return True
        previous = level
    return False


def is_generic_justification(text):
    normalized = re.sub(r"\s+", " ", (text or "").strip().lower())
    return any(re.search(pattern, normalized, re.I) for pattern in GENERIC_SCORE_PATTERNS)


failures = {}
warnings = {}
expected_slugs = set(COMPARISON_PAGES)
record_paths = {p.stem: p for p in COMPARISONS.glob("*.json")}

missing_records = expected_slugs - set(record_paths)
extra_records = set(record_paths) - expected_slugs
if missing_records:
    failures["cluster"] = [f"missing methodology record: {slug}" for slug in sorted(missing_records)]
if extra_records:
    warnings["cluster"] = [f"JSON exists without COMPARISON_PAGES entry: {slug}" for slug in sorted(extra_records)]

for slug, page_spec in COMPARISON_PAGES.items():
    issues = []
    notes = []
    fp = record_paths.get(slug)
    if fp is None:
        continue

    record = json.loads(fp.read_text(encoding="utf-8"))
    schema = record.get("schema_version", 1)
    url = f"/comparatifs/{slug}/"

    # Contract: comparison_pages.py -> generated JSON.
    if record.get("slug") != slug:
        issues.append("JSON slug does not match comparison_pages.py key")
    if record.get("url") != url:
        issues.append("JSON URL does not match comparison route")

    intent = record.get("intent") or {}
    if intent.get("query") != page_spec.get("query"):
        issues.append("JSON query differs from comparison_pages.py")
    if intent.get("type") != page_spec.get("type"):
        issues.append("JSON comparison type differs from comparison_pages.py")
    if intent.get("user_job") != page_spec.get("job"):
        issues.append("JSON user job differs from comparison_pages.py")

    criteria = record.get("criteria") or []
    json_weights = {c.get("id"): c.get("weight") for c in criteria if c.get("id")}
    if json_weights != page_spec.get("weights"):
        issues.append("JSON criteria/weights differ from comparison_pages.py")
    if not math.isclose(sum(page_spec["weights"].values()), 100.0, abs_tol=0.001):
        issues.append("comparison_pages.py weights do not sum to 100")
    if record.get("affiliate_commission_used_in_ranking") is not False:
        issues.append("affiliate commission is not explicitly excluded from ranking")

    # Universe: schema v2 deliberately persists considered-but-excluded candidates.
    universe = record.get("product_universe") or []
    rankable_ids = [p.get("id") for p in universe if p.get("status") in RANKABLE]
    all_ids = [p.get("id") for p in universe]
    if rankable_ids != page_spec.get("products"):
        issues.append("rankable JSON product universe differs from comparison_pages.py products")
    if schema < 2 and all_ids != page_spec.get("products"):
        issues.append("legacy JSON product universe differs from comparison_pages.py products")
    if schema >= 2:
        excluded_ids = [p.get("id") for p in universe if p.get("status") not in RANKABLE]
        if not excluded_ids:
            issues.append("schema v2 must persist considered-but-excluded products")
        if record.get("excluded_products") != excluded_ids:
            issues.append("excluded_products does not match non-rankable universe decisions")
        if any(not p.get("equivalence") for p in universe):
            issues.append("schema v2 universe contains candidate without equivalence class")
        if any(not p.get("reason") for p in universe):
            issues.append("schema v2 universe contains candidate without inclusion/exclusion reason")

    # Score persistence. Legacy pages still mirror comparison_products.py; v2 pages mirror durable methodology.
    score_map = record.get("scores") or {}
    method = COMPARISON_METHODS.get(slug)
    generic_count = 0
    verified_editorial_count = 0

    for pid in page_spec.get("products", []):
        if pid not in COMPARISON_PRODUCTS:
            issues.append(f"unknown product id in comparison_pages.py: {pid}")
            continue
        if not COMPARISON_PRODUCTS[pid].get("source"):
            issues.append(f"{pid}: source missing in comparison_products.py")

        entries = score_map.get(pid)
        if not isinstance(entries, dict):
            issues.append(f"{pid}: JSON score map missing")
            continue

        expected_scores = method["scores"][pid] if method else None
        for cid in page_spec["weights"]:
            entry = entries.get(cid)
            if not isinstance(entry, dict):
                issues.append(f"{pid}/{cid}: JSON score entry missing")
                continue
            score = entry.get("score")
            if not is_number(score) or score < 0 or score > 10:
                issues.append(f"{pid}/{cid}: score must be between 0 and 10")
            if method and score != expected_scores[cid]["score"]:
                issues.append(f"{pid}/{cid}: generated score differs from comparison_methodology.py")
            if not method and score != COMPARISON_PRODUCTS[pid]["scores"].get(cid):
                issues.append(f"{pid}/{cid}: legacy JSON score differs from comparison_products.py baseline")

            evidence = entry.get("evidence_class")
            if evidence not in ALLOWED_EVIDENCE:
                issues.append(f"{pid}/{cid}: invalid evidence class {evidence!r}")
            if evidence == "PROHIBITED":
                issues.append(f"{pid}/{cid}: PROHIBITED evidence cannot support ranking")
            if schema >= 2 and evidence == "VERIFIED":
                issues.append(f"{pid}/{cid}: editorial numeric score cannot be labelled VERIFIED in schema v2")

            justification = (entry.get("justification") or "").strip()
            if not justification:
                issues.append(f"{pid}/{cid}: score justification missing")
            elif is_generic_justification(justification):
                generic_count += 1
            if evidence == "VERIFIED" and "editorial normalization" in justification.lower():
                verified_editorial_count += 1

    if generic_count:
        notes.append(
            f"{generic_count} score justifications are generic normalizations; "
            "upgrade this page to schema v2 before publication"
        )
    if verified_editorial_count:
        notes.append(
            f"{verified_editorial_count} scores conflate verified facts with editorial normalization; "
            "upgrade this page to schema v2 before publication"
        )

    # Ranking is reproducible from the JSON scores actually used by the renderer/generator.
    configured_order = [pid for pid, _ in page_spec.get("ranking", [])]
    json_ranking = record.get("ranking") or []
    json_order = [r.get("product_id") for r in json_ranking]

    recalculated = []
    for pid in page_spec.get("products", []):
        score = json_weighted_score(record, pid)
        if score is None:
            issues.append(f"{pid}: cannot recalculate weighted score from JSON")
        else:
            recalculated.append((pid, score))
    expected_order = [pid for pid, _ in sorted(recalculated, key=lambda pair: pair[1], reverse=True)]
    if json_order != expected_order:
        issues.append("JSON ranking order differs from recalculated JSON score order")

    for row in json_ranking:
        pid = row.get("product_id")
        calc = json_weighted_score(record, pid)
        if calc is None or not is_number(row.get("score")) or not math.isclose(row["score"], calc, abs_tol=0.011):
            issues.append(f"{pid}: JSON ranking score is not reproducible from JSON criteria/scores")

    if schema < 2 and json_order != configured_order:
        issues.append("legacy JSON ranking order differs from comparison_pages.py")
    if schema >= 2 and json_order != configured_order:
        notes.append("schema v2 ranking differs from legacy comparison_pages.py ranking; durable methodology is authoritative")

    if len(json_ranking) >= 2:
        margin = json_ranking[0]["score"] - json_ranking[1]["score"]
        if margin <= 0.30:
            if schema >= 2:
                sensitivity = record.get("sensitivity") or {}
                if not sensitivity.get("scenarios"):
                    issues.append(f"top-two margin is {margin:.2f}/10 but sensitivity analysis is missing")
            else:
                notes.append(
                    f"top-two margin is {margin:.2f}/10; schema v2 sensitivity analysis required before publication"
                )

    # Workflow persistence boundary.
    if schema >= 2:
        for key in (
            "evidence_ledger", "hard_gates", "total_solution_cost", "sensitivity",
            "ranking_confidence", "rank_justification", "excluded_products",
        ):
            if key not in record:
                issues.append(f"schema v2 does not persist required field: {key}")
    else:
        notes.append("legacy schema v1: Evidence Ledger, equivalence, exclusions, hard gates and confidence remain UNPROVABLE")
        if page_spec.get("type") in {"budget", "best_for_use_case"}:
            notes.append("legacy schema v1: Total Solution Cost requires v2 review before publication")

    if not record.get("researched_at"):
        issues.append("researched_at missing")

    # User-facing output: JSON/method -> HTML.
    page = ROOT / "comparatifs" / slug / "index.html"
    if not page.exists():
        issues.append("generated HTML page missing")
    else:
        html = page.read_text(encoding="utf-8")
        article_match = re.search(r'<article class="content-main">(.*?)</article>', html, re.S | re.I)
        if not article_match:
            issues.append("article.content-main missing")
        else:
            body = article_match.group(1)
            body_lower = body.lower()
            body_text = normalized_text(body)
            if "<!-- contenu à rédiger -->" in body_lower or "contenu en préparation" in body_lower:
                issues.append("placeholder/preparation marker remains in article")
            if any(re.search(pattern, body_text, re.I) for pattern in FAKE_HANDS_ON_PATTERNS):
                issues.append("unsupported first-hand test language detected")
            if any(re.search(pattern, body_text, re.I) for pattern in EDITOR_FACING_PATTERNS):
                issues.append("editor-facing SEO/workflow commentary detected")
            if any(re.search(pattern, body_text, re.I) for pattern in HIGH_SLOP_PATTERNS):
                issues.append("high-risk generic/AI-slop wording detected")
            if len(SOURCE_RE.findall(body)) == 0:
                issues.append("no external source found in article")
            article_levels = [int(level) for level, _ in HEADING_RE.findall(body)]
            if has_heading_jump(([1] if H1_RE.search(html) else []) + article_levels):
                issues.append("article heading hierarchy skips a level")
            if schema >= 2:
                verdict = record.get("editorial_verdict", {})
                if verdict.get("label") == "CONDITIONAL_WINNER" and "conditional" not in body_text and "si les" not in body_text:
                    issues.append("conditional ranking confidence is not reflected in article text")

        robots = ROBOTS_RE.search(html)
        if not robots or "noindex" not in robots.group(1).lower():
            issues.append("comparison must remain noindex until human validation")
        if len(TITLE_RE.findall(html)) != 1 or not clean(TITLE_RE.findall(html)[0]):
            issues.append("missing or invalid title")
        if len(META_DESC_RE.findall(html)) != 1 or not clean(META_DESC_RE.findall(html)[0]):
            issues.append("missing or invalid meta description")
        if len(CANONICAL_RE.findall(html)) != 1:
            issues.append("missing or duplicate canonical")
        if len(H1_RE.findall(html)) != 1:
            issues.append("expected exactly one H1")

    if issues:
        failures[url] = issues
    if notes:
        warnings[url] = notes

# Persistence architecture: v2 fields must come from durable methodology, not hand-edited JSON.
generator = ROOT / "generate_comparison_metadata.py"
if generator.exists() and COMPARISON_METHODS:
    generator_text = generator.read_text(encoding="utf-8")
    required_tokens = [
        "COMPARISON_METHODS", "evidence_ledger", "hard_gates", "total_solution_cost",
        "sensitivity", "ranking_confidence", "rank_justification", "excluded_products",
    ]
    missing = [token for token in required_tokens if token not in generator_text]
    if missing:
        failures.setdefault("cluster", []).append(
            "generate_comparison_metadata.py does not durably persist v2 methodology: " + ", ".join(missing)
        )

if warnings:
    print("WARNINGS — comparison-content-workflow phases requiring manual evaluation")
    for url, notes in warnings.items():
        print("WARN", url)
        for note in notes:
            print("  -", note)
    print()

if failures:
    print("FAIL — machine-detectable comparison workflow inconsistencies")
    for url, issues in failures.items():
        print("FAIL", url)
        for issue in issues:
            print("  -", issue)
    print()
    print("Machine validation checks reproducibility and detectable blockers. Run the Comparison Workflow Evaluation Gate before publication.")
    sys.exit(1)

print(f"PASS: {len(COMPARISON_PAGES)} comparison pages are mechanically consistent with the current comparison pipeline")
print(f"V2: {len(COMPARISON_METHODS)} enriched comparison(s) use durable methodology data")
print("NEXT: run .agents/skills/comparison-editorial-publish-gate/SKILL.md before publication")
