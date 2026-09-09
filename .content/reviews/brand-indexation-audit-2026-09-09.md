# Final brand indexation audit — 2026-09-09

Scope: `/marques/`

This audit is the human publication/indexation review performed after the machine validator and editorial publish gate. It does not remove `noindex,follow` automatically.

| URL | Page type | Decision | Rationale |
|---|---|---|---|
| `/marques/` | DIRECTORY | INDEX | Useful comparative gateway; distinct from the global comparison and brand hubs. |
| `/marques/remarkable/` | BRAND_HUB | INDEX | Strong entity/ecosystem hub with current range, Connect, limitations and routing. |
| `/marques/boox/` | BRAND_HUB | INDEX | Strong Android/ecosystem hub with current range and clear differentiation. |
| `/marques/kindle-scribe/` | BRAND_HUB | INDEX | Distinct Kindle/Scribe ecosystem intent; current range and cloud workflow are useful. |
| `/marques/kobo-elipsa/` | BRAND_HUB | INDEX | Distinct Kobo Elipsa ecosystem intent with reading, notes, PDF and cloud limitations. |
| `/marques/supernote/` | BRAND_HUB | INDEX | Distinct Supernote entity intent; organisation/repairability/ecosystem positioning is useful. |
| `/marques/remarkable/remarkable-paper-pro/` | PRODUCT | INDEX | Product/specification and purchase-decision intent is clearly separated from the review page. |
| `/marques/remarkable/remarkable-2/` | PRODUCT | INDEX | Legacy/discontinued-product intent remains useful for owners and second-hand/reconditioned buyers. |
| `/marques/remarkable/remarkable-paper-pro-avis/` | REVIEW | INDEX | Independent-source review intent; differentiated from the product specification page. |
| `/marques/remarkable/remarkable-2-avis/` | REVIEW | INDEX | Independent-source legacy review; differentiated from ownership/specification page. |
| `/marques/remarkable/abonnement-connect/` | SERVICE | INDEX | Clear subscription/service intent and standalone decision value. |
| `/marques/remarkable/accessoires/` | ACCESSORY_HUB | KEEP NOINDEX | Search intent exists, but current editorial value is still too generic. Add an exact compatibility matrix by current model and concrete accessory names before indexation. |
| `/marques/remarkable/alternatives/` | ALTERNATIVES | INDEX | Distinct commercial-investigation intent by reason to leave reMarkable; useful routing to BOOX, Supernote, Kindle/Kobo and no-subscription choices. |
| `/marques/boox/boox-note-air/` | PRODUCT | INDEX | Current Note Air5 C/family intent is strong and clearly framed around Android, Kaleido 3 and workflow. |
| `/marques/boox/boox-tab-ultra/` | PRODUCT | INDEX | Tab Ultra C Pro is still officially sold/documented; page correctly treats it as an older Android generation and routes toward newer alternatives. |
| `/marques/boox/avis/` | REVIEW | KEEP NOINDEX | Current page is a product/ecosystem review, while the generic `BOOX avis` intent also includes brand reputation, support, updates and after-sales. Expand this before indexation. |
| `/marques/boox/accessoires/` | ACCESSORY_HUB | KEEP NOINDEX | Search intent exists, but current page lacks a concrete model-by-model compatibility matrix and exact accessory mapping. Enrich before indexation. |
| `/marques/boox/alternatives/` | ALTERNATIVES | INDEX | Distinct alternatives intent, with clear reasons to choose reMarkable, Supernote, Kindle/Kobo or remain within BOOX. |

## Summary

- Recommended INDEX: 15 URLs
- KEEP NOINDEX pending targeted enrichment: 3 URLs
- FUSIONNER: 0 URLs

## Pages to enrich before indexation

### `/marques/remarkable/accessoires/`
Add a current-generation compatibility matrix covering at minimum Paper Pure, Paper Pro Move, Paper Pro and reMarkable 2, with Marker/Marker Plus, Folio/Book Folio and Type Folio compatibility and whether each accessory is included, optional or incompatible.

### `/marques/boox/accessoires/`
Add a current-model compatibility matrix covering at minimum Go 10.3 Gen II, Note Air5 C, Note Max, Tab X C and Tab Ultra C Pro. Map current styluses, keyboard covers, cases and microSD support by exact model.

### `/marques/boox/avis/`
Expand beyond device flexibility: include software-update policy where documentable, customer support/after-sales, warranty/repair pathways, privacy/account ecosystem where relevant, recurring user complaints and strengths from independent sources, and clearly separate product experience from merchant/service reputation.

## Cannibalisation / merge decision

No mandatory merger is recommended. PRODUCT and REVIEW URLs now serve separate intents: factual purchase/specification pages versus evidence-based editorial reviews. The BOOX hub and BOOX review can also coexist once the review page covers brand-level trust/support intent rather than duplicating the hub.

All pages should remain `noindex,follow` until the recommended indexation changes are explicitly approved and applied.