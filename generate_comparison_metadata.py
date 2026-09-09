#!/usr/bin/env python3
from pathlib import Path
import json

from comparison_pages import COMPARISON_PAGES
from comparison_products import COMPARISON_PRODUCTS
from comparison_methodology import COMPARISON_METHODS, CHECKED_AT

ROOT = Path(__file__).resolve().parent
D = ROOT / ".content" / "comparisons"
D.mkdir(parents=True, exist_ok=True)


def weighted_total(scores, weights):
    return round(sum(scores[c]["score"] * weights[c] for c in weights) / 100, 3)


for slug, p in COMPARISON_PAGES.items():
    method = COMPARISON_METHODS.get(slug)
    researched_at = CHECKED_AT if method else "2026-09-08"

    payload = {
        "schema_version": 2 if method else 1,
        "slug": slug,
        "url": f"/comparatifs/{slug}/",
        "researched_at": researched_at,
        "status": "DRAFT_READY",
        "intent": {
            "query": p["query"],
            "type": p["type"],
            "user_job": p["job"],
        },
        "criteria": [],
        "product_universe": [],
        "scores": {},
        "ranking": [],
        "affiliate_commission_used_in_ranking": False,
        "methodology_note": (
            "Desk-research scoring. Product facts can be VERIFIED; numeric scores are editorial INFERENCES "
            "derived from those facts, not hands-on measurements."
        ),
    }

    if method:
        payload["decision_contract"] = method["decision_contract"]
        for cid, weight in p["weights"].items():
            meta = method["criteria_definitions"][cid]
            payload["criteria"].append({
                "id": cid,
                "label": meta["label"],
                "weight": weight,
                "definition": meta["definition"],
                "weight_rationale": meta["weight_rationale"],
            })

        for item in method["universe"]:
            pr = COMPARISON_PRODUCTS.get(item["id"])
            row = dict(item)
            if pr:
                row["name"] = pr["name"]
                row["price_snapshot"] = pr["price"]
            payload["product_universe"].append(row)

        payload["scores"] = method["scores"]
        for pid in p["products"]:
            score = weighted_total(method["scores"][pid], p["weights"])
            payload["ranking"].append({"product_id": pid, "score": score})
        payload["ranking"].sort(key=lambda item: item["score"], reverse=True)
        for i, item in enumerate(payload["ranking"], 1):
            item["rank"] = i

        payload["evidence_ledger"] = method["evidence_ledger"]
        payload["hard_gates"] = method["hard_gates"]
        payload["total_solution_cost"] = method["total_solution_cost"]
        payload["sensitivity"] = method["sensitivity"]
        payload["ranking_confidence"] = {
            "label": method["sensitivity"]["winner_stability"],
            "confidence": method["sensitivity"]["confidence"],
            "base_margin": method["sensitivity"]["base_margin"],
        }
        payload["rank_justification"] = method["rank_justification"]
        payload["editorial_verdict"] = method["editorial_verdict"]
        payload["excluded_products"] = [
            item["id"] for item in method["universe"] if item["status"] not in {"ELIGIBLE", "CONDITIONALLY_ELIGIBLE"}
        ]
    else:
        payload["criteria"] = [
            {"id": c, "label": c, "weight": w}
            for c, w in p["weights"].items()
        ]
        for pid in p["products"]:
            pr = COMPARISON_PRODUCTS[pid]
            payload["product_universe"].append({
                "id": pid,
                "name": pr["name"],
                "status": "ELIGIBLE",
                "source": pr["source"],
                "price_snapshot": pr["price"],
            })
            payload["scores"][pid] = {
                c: {
                    "score": pr["scores"][c],
                    "evidence_class": "INFERRED",
                    "fact_source": pr["source"],
                    "justification": (
                        f"Legacy editorial normalization for {c} based on the official product source. "
                        "This page still requires a v2 Evidence Ledger before publication."
                    ),
                }
                for c in p["weights"]
            }

        for rank, (pid, score) in enumerate(p["ranking"], 1):
            payload["ranking"].append({"rank": rank, "product_id": pid, "score": score})

    (D / f"{slug}.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("metadata", slug, "schema", payload["schema_version"])
