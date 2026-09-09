"""Per-URL editorial overrides for comparison pages.

This module is deliberately small. `comparison_content.py` contains a legacy
renderer for comparison pages that have not yet been reviewed with the new
workflow. Once a page is produced or deeply rewritten through
`comparison-content-workflow`, its final article body belongs here (or in a
future free-form source consumed here) so CI cannot re-impose the legacy
scoring/template structure.

Do not add a page-type template to this file. Each override must be specific to
one URL and come from that page's brief/evidence/recommendation logic.
"""

BESPOKE_COMPARISON_CONTENT: dict[str, str] = {}


def bespoke_body(slug: str, fallback: str) -> str:
    """Return bespoke editorial content when a reviewed override exists."""
    body = BESPOKE_COMPARISON_CONTENT.get(slug)
    if body is None:
        return fallback
    body = body.strip()
    if not body:
        raise ValueError(f"Empty bespoke comparison content: {slug}")
    return body
