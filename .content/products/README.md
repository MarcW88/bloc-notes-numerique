# Product registry — Phase 1

This registry centralizes product presentation so a product is configured once and can be reused across selected editorial pages.

## Current operating mode (no Amazon API)

1. Keep editorial specs and `best_for` in `registry.json`.
2. Paste a SiteStripe link into `amazon.affiliate_url` when it is available. Until then, the card shows only the internal editorial link; no fake or non-affiliate Amazon CTA is rendered.
3. Add an image only when its provenance is explicit:
   - `OWN`: an image owned by the site, usually stored under `/assets/products/`;
   - `MANUFACTURER_AUTHORIZED`: a manufacturer image whose reuse rights were checked (`rights_checked: true`);
   - `AMAZON_CREATORS_API`: reserved for the future API integration. The image stays remote and must not be downloaded into the repo.
4. Do not scrape Amazon product pages or copy Amazon-hosted images into the repository.
5. Run `python apply_product_cards.py`, then `python validate_product_cards.py`.

## Pilot scope

Only three comparison URLs are enabled in `pilot-comparisons.json`:

- `/comparatifs/meilleur-bloc-notes-numerique/` — 3 cards;
- `/comparatifs/bloc-notes-numerique-professionnel/` — 3 cards;
- `/comparatifs/kindle-scribe-vs-remarkable/` — 2 cards.

Changing that scope is an explicit editorial decision: the validator fails if cards appear on other comparison pages.

## Commerce rules

- No static Amazon price is stored in Phase 1.
- Amazon CTAs render only when an actual `affiliate_url` exists.
- Affiliate links use `rel="sponsored nofollow noopener noreferrer"`.
- One card equals at most one main commercial link.
- Clicks emit an `affiliate_click` event to `window.dataLayer` when present and always emit an `affiliate:click` browser event. This makes GTM/analytics integration possible without coupling the cards to one analytics provider.

## Future Creators API mode

The registry deliberately separates editorial data from commerce/media data. When Creators API access becomes available, a sync layer can populate ASIN, affiliate URL, availability and remote image URL while keeping editorial recommendations under site control.
