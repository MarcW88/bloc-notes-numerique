#!/usr/bin/env python3
"""Validate the /usages/ editorial workflow infrastructure.

This validator intentionally checks only observable structural rules. It does
not claim that JTBD research, fact-checking, Humanizer, SEO or GEO quality have
passed.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

EXPECTED_USAGE_SLUGS = {
    "prise-de-notes-professionnelle",
    "prise-de-notes-etudiant",
    "prise-de-notes-reunion",
    "annotation-pdf",
    "lecture-et-prise-de-notes",
    "dessin",
    "remplacer-cahiers-papier",
}

REQUIRED_RECORD_KEYS = {
    "slug",
    "page_url",
    "status",
    "intent",
    "jtbd",
    "workflow_map",
    "criteria",
    "solution_families",
    "contraindications",
    "evidence_ledger",
    "editorial",
    "qa",
}

FORBIDDEN_RECORD_KEYS = {
    "ranking",
    "rankings",
    "ranked_products",
    "scores",
    "product_scores",
    "winner",
}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def walk_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from walk_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_keys(child)


def main() -> None:
    required_files = [
        ROOT / ".agents/skills/jobs-to-be-done/SKILL.md",
        ROOT / ".agents/skills/jobs-to-be-done/LICENSE",
        ROOT / ".agents/skills/usage-content-workflow/SKILL.md",
        ROOT / ".content/usages/_template.json",
        ROOT / ".content/usages/README.md",
        ROOT / "usage-workflow.config.yaml",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required_files if not path.exists()]
    if missing:
        fail("missing workflow files: " + ", ".join(missing))

    template_path = ROOT / ".content/usages/_template.json"
    try:
        template = json.loads(template_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid usage template JSON: {exc}")

    missing_keys = REQUIRED_RECORD_KEYS - set(template)
    if missing_keys:
        fail("usage template missing keys: " + ", ".join(sorted(missing_keys)))

    usage_root = ROOT / "usages"
    if not usage_root.exists():
        fail("usages/ directory is missing")

    actual_slugs = {
        path.name
        for path in usage_root.iterdir()
        if path.is_dir() and (path / "index.html").exists()
    }
    missing_slugs = EXPECTED_USAGE_SLUGS - actual_slugs
    if missing_slugs:
        fail("missing current usage routes: " + ", ".join(sorted(missing_slugs)))

    noindex_failures = []
    for slug in sorted(EXPECTED_USAGE_SLUGS):
        page = usage_root / slug / "index.html"
        html = page.read_text(encoding="utf-8")
        if 'name="robots" content="noindex,follow"' not in html:
            noindex_failures.append(slug)
    if noindex_failures:
        fail("usage pages missing noindex,follow: " + ", ".join(noindex_failures))

    records_dir = ROOT / ".content/usages"
    for record_path in sorted(records_dir.glob("*.json")):
        if record_path.name == "_template.json":
            continue
        try:
            record = json.loads(record_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"{record_path}: invalid JSON: {exc}")

        missing = REQUIRED_RECORD_KEYS - set(record)
        if missing:
            fail(f"{record_path}: missing keys {', '.join(sorted(missing))}")

        forbidden = FORBIDDEN_RECORD_KEYS & set(walk_keys(record))
        if forbidden:
            fail(
                f"{record_path}: product-ranking data belongs in comparison workflow: "
                + ", ".join(sorted(forbidden))
            )

        slug = record.get("slug")
        if slug and slug not in actual_slugs:
            fail(f"{record_path}: slug {slug!r} has no matching /usages/ page")

        page_url = record.get("page_url", "")
        if slug and page_url != f"/usages/{slug}/":
            fail(f"{record_path}: page_url does not match slug")

    print(
        "PASS: usage workflow infrastructure is valid; "
        f"{len(EXPECTED_USAGE_SLUGS)} current usage pages remain noindex,follow."
    )
    print(
        "NOTE: this structural PASS does not imply JTBD, fact-check, editorial, SEO or GEO PASS."
    )


if __name__ == "__main__":
    main()
