#!/usr/bin/env python3
from pathlib import Path
import json
import math
import sys

from comparison_methodology import COMPARISON_METHODS
from comparison_pages import COMPARISON_PAGES

ROOT = Path(__file__).resolve().parent
DATA = ROOT / ".content" / "comparisons"

REQUIRED_RANK_FIELDS = {
    "best_for", "not_for", "decisive_advantage", "decisive_limit",
    "alternative", "position_reason"
}
VALID_UNIVERSE_STATUS = {
    "ELIGIBLE", "CONDITIONALLY_ELIGIBLE", "OUTDATED",
    "NOT_COMPARABLE", "EXCLUDED"
}
VALID_EQUIVALENCE = {
    "EXACT", "FUNCTIONALLY_COMPARABLE", "PARTIALLY_COMPARABLE", "NOT_COMPARABLE"
}


def weighted_total(method, page, pid):
    return sum(
        method["scores"][pid][cid]["score"] * weight
        for cid, weight in page["weights"].items()
    ) / 100


def fail(errors, message):
    errors.append(message)


errors = []
warnings = []

for slug, method in COMPARISON_METHODS.items():
    page = COMPARISON_PAGES.get(slug)
    if not page:
        fail(errors, f"{slug}: missing comparison_pages contract")
        continue

    if method.get("schema_version") != 2:
        fail(errors, f"{slug}: methodology must use schema_version 2")

    criterion_ids = set(page["weights"])
    definitions = method.get("criteria_definitions", {})
    if set(definitions) != criterion_ids:
        fail(errors, f"{slug}: criteria_definitions do not match page weights")

    universe = method.get("universe", [])
    if not universe:
        fail(errors, f"{slug}: product universe missing")
    universe_ids = set()
    excluded = []
    for item in universe:
        pid = item.get("id")
        if not pid or pid in universe_ids:
            fail(errors, f"{slug}: missing/duplicate universe id {pid!r}")
            continue
        universe_ids.add(pid)
        if item.get("status") not in VALID_UNIVERSE_STATUS:
            fail(errors, f"{slug}/{pid}: invalid universe status")
        if item.get("equivalence") not in VALID_EQUIVALENCE:
            fail(errors, f"{slug}/{pid}: invalid equivalence class")
        if not item.get("reason") or not item.get("source"):
            fail(errors, f"{slug}/{pid}: universe decision lacks reason/source")
        if item.get("status") not in {"ELIGIBLE", "CONDITIONALLY_ELIGIBLE"}:
            excluded.append(pid)

    if not excluded:
        fail(errors, f"{slug}: no considered-and-excluded candidate is persisted")

    ledger = method.get("evidence_ledger", [])
    ledger_by_id = {}
    for entry in ledger:
        eid = entry.get("id")
        if not eid or eid in ledger_by_id:
            fail(errors, f"{slug}: duplicate/missing evidence id {eid!r}")
            continue
        ledger_by_id[eid] = entry
        for key in ("product_id", "claim", "source", "checked_at", "evidence_class"):
            if not entry.get(key):
                fail(errors, f"{slug}/{eid}: evidence missing {key}")
        if entry.get("evidence_class") not in {"VERIFIED", "SUPPORTED", "USER_PATTERN", "FIRST_HAND"}:
            fail(errors, f"{slug}/{eid}: ledger facts must use factual evidence classes")
        for cid in entry.get("criteria", []):
            if cid not in criterion_ids:
                fail(errors, f"{slug}/{eid}: unknown criterion {cid}")

    scores = method.get("scores", {})
    for pid in page["products"]:
        if pid not in scores:
            fail(errors, f"{slug}/{pid}: missing page-specific scores")
            continue
        for cid in page["weights"]:
            item = scores[pid].get(cid)
            if not item:
                fail(errors, f"{slug}/{pid}/{cid}: score missing")
                continue
            score = item.get("score")
            if not isinstance(score, (int, float)) or score < 0 or score > 10:
                fail(errors, f"{slug}/{pid}/{cid}: invalid score")
            if item.get("evidence_class") == "VERIFIED":
                fail(errors, f"{slug}/{pid}/{cid}: numeric editorial score must not be labelled VERIFIED")
            if item.get("evidence_class") not in {"INFERRED", "USER_PATTERN", "FIRST_HAND"}:
                fail(errors, f"{slug}/{pid}/{cid}: invalid score evidence_class")
            refs = item.get("evidence_refs", [])
            if not refs:
                fail(errors, f"{slug}/{pid}/{cid}: score has no evidence_refs")
            for ref in refs:
                if ref not in ledger_by_id:
                    fail(errors, f"{slug}/{pid}/{cid}: unknown evidence ref {ref}")
            justification = (item.get("justification") or "").strip()
            if len(justification) < 35:
                fail(errors, f"{slug}/{pid}/{cid}: justification too generic/short")

    hard_gates = method.get("hard_gates", [])
    if not hard_gates:
        fail(errors, f"{slug}: hard gates missing")
    if not any(g.get("scope") == "UNIVERSAL" for g in hard_gates):
        fail(errors, f"{slug}: no universal hard gate")
    if not any(g.get("scope") == "USER_SPECIFIC" for g in hard_gates):
        warnings.append(f"{slug}: no user-specific hard gate")

    tsc = method.get("total_solution_cost", {})
    if tsc.get("applies") and not tsc.get("products"):
        fail(errors, f"{slug}: Total Solution Cost applies but product data are missing")
    if tsc.get("applies"):
        missing_tsc = set(page["products"]) - set(tsc["products"])
        if missing_tsc:
            fail(errors, f"{slug}: TSC missing products {sorted(missing_tsc)}")

    ranking = sorted(
        ((pid, weighted_total(method, page, pid)) for pid in page["products"]),
        key=lambda pair: pair[1],
        reverse=True,
    )
    margin = ranking[0][1] - ranking[1][1]
    sensitivity = method.get("sensitivity", {})
    if margin <= 0.30:
        if not sensitivity.get("scenarios"):
            fail(errors, f"{slug}: top margin {margin:.2f} requires sensitivity scenarios")
        if not math.isclose(sensitivity.get("base_margin", -1), margin, abs_tol=0.011):
            fail(errors, f"{slug}: sensitivity base_margin does not match recalculated margin")
        flips = [s for s in sensitivity.get("scenarios", []) if s.get("winner") != ranking[0][0]]
        if flips and sensitivity.get("winner_stability") != "CONDITIONAL_WINNER":
            fail(errors, f"{slug}: sensitivity flips winner but result is not CONDITIONAL_WINNER")

    justifications = method.get("rank_justification", {})
    for pid in page["products"]:
        item = justifications.get(pid, {})
        missing = REQUIRED_RANK_FIELDS - set(item)
        if missing:
            fail(errors, f"{slug}/{pid}: rank justification missing {sorted(missing)}")

    verdict = method.get("editorial_verdict", {})
    if sensitivity.get("winner_stability") == "CONDITIONAL_WINNER":
        if verdict.get("label") != "CONDITIONAL_WINNER" or not verdict.get("alternative"):
            fail(errors, f"{slug}: conditional winner must be reflected in editorial_verdict")

    json_path = DATA / f"{slug}.json"
    if json_path.exists():
        payload = json.loads(json_path.read_text(encoding="utf-8"))
        if payload.get("schema_version") == 2:
            for key in (
                "evidence_ledger", "hard_gates", "total_solution_cost",
                "sensitivity", "ranking_confidence", "rank_justification",
                "excluded_products"
            ):
                if key not in payload:
                    fail(errors, f"{slug}: generated JSON does not persist {key}")

if warnings:
    print("WARNINGS")
    for warning in warnings:
        print(" -", warning)

if errors:
    print("FAIL — comparison workflow v2")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print(f"PASS — comparison workflow v2: {len(COMPARISON_METHODS)} enriched comparison(s)")
