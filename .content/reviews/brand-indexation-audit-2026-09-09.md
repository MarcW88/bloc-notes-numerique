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
| `/marques/remarkable/accessoires/` | ACCESSORY_HUB | INDEX | Enriched with a current-generation compatibility matrix for Paper Pure, Paper Pro Move, Paper Pro and reMarkable 2, including stylets, folios and Type Folio compatibility. |
| `/marques/remarkable/alternatives/` | ALTERNATIVES | INDEX | Distinct commercial-investigation intent by reason to leave reMarkable; useful routing to BOOX, Supernote, Kindle/Kobo and no-subscription choices. |
| `/marques/boox/boox-note-air/` | PRODUCT | INDEX | Current Note Air5 C/family intent is strong and clearly framed around Android, Kaleido 3 and workflow. |
| `/marques/boox/boox-tab-ultra/` | PRODUCT | INDEX | Tab Ultra C Pro is still officially sold/documented; page correctly treats it as an older Android generation and routes toward newer alternatives. |
| `/marques/boox/avis/` | REVIEW | INDEX | Expanded to cover brand-level trust questions: firmware support, warranty, repairs, returns, account/cloud/privacy, independent reviews and customer-service signals. |
| `/marques/boox/accessoires/` | ACCESSORY_HUB | INDEX | Enriched with exact model-by-model mapping for Go 10.3 Gen II, Note Air5 C, Note Max, Tab X C and Tab Ultra C Pro, including stylus, case, keyboard and microSD support. |
| `/marques/boox/alternatives/` | ALTERNATIVES | INDEX | Distinct alternatives intent, with clear reasons to choose reMarkable, Supernote, Kindle/Kobo or remain within BOOX. |

## Summary

- Recommended INDEX: 18 URLs
- KEEP NOINDEX pending enrichment: 0 URLs
- FUSIONNER: 0 URLs

## Enrichment completed before indexation

### `/marques/remarkable/accessoires/`
The page now includes a current-generation compatibility matrix covering Paper Pure, Paper Pro Move, Paper Pro and reMarkable 2. It distinguishes current-generation Marker/Marker Plus from reMarkable 2 pens, maps Sleeve Folio / Book Folio / Type Folio by device, explains the Paper Pro Move Type Folio incompatibility, and adds decision guidance by use case.

### `/marques/boox/accessoires/`
The page now includes a current-model compatibility matrix covering Go 10.3 Gen II, Note Air5 C, Note Max, Tab X C and Tab Ultra C Pro. It maps the current stylus, official cases, official keyboard availability and microSD support, with additional guidance on bundles and second-hand compatibility.

### `/marques/boox/avis/`
The page now covers both device quality and brand-level purchase risk: BOOX's stated firmware-support window, Android-version differences, warranty and repair pathways, return-policy conditions, ONYX account/server behavior, third-party cloud integrations, privacy/logging documentation and independent customer-service signals. Public customer reviews are treated as anecdotal evidence rather than statistics.

## Cannibalisation / merge decision

No mandatory merger is recommended. PRODUCT and REVIEW URLs serve separate intents: factual purchase/specification pages versus evidence-based editorial reviews. The BOOX hub covers the ecosystem and current range, while `/marques/boox/avis/` now addresses brand trust, support, software lifecycle and purchase-risk questions in addition to device experience.

All pages remain `noindex,follow` until the indexation changes are explicitly approved and applied.
