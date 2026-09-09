# Comparison workflow evaluation

URL: `/comparatifs/bloc-notes-numerique-professionnel/`
Comparison type: `BEST_FOR_USE_CASE`
Evaluation date: 2026-09-09
Status: **FAIL**
Publication: **KEEP NOINDEX**

## Scope

This audit applies `.agents/skills/comparison-editorial-publish-gate/SKILL.md` as a mirror of the actual `comparison-content-workflow` used by this repository. It evaluates the complete chain from `comparison_products.py` and `comparison_pages.py` through `.content/comparisons/bloc-notes-numerique-professionnel.json` to the generated HTML.

The target decision is: **choose a digital notebook for professional work involving meetings, PDFs, exports and work tools**.

## Pipeline consistency

- `comparison_products.py → comparison_pages.py`: **PASS** — the configured products and criterion scores exist in the product baseline.
- `comparison_pages.py → JSON`: **PASS** — intent, products, weights and ranking are reproduced in the generated methodology record.
- `JSON → HTML`: **PASS** — ranking order and displayed product-level verdicts are consistent with the generated record. Note: display rounding hides some of the already-small gaps.
- regeneration durability: **FAIL** — the current generator does not persist the Evidence Ledger, equivalence analysis, candidate exclusions, hard gates, total solution cost or ranking confidence/sensitivity. Adding those only by hand to the generated JSON would not survive regeneration.

## Workflow phases

- Routing & search intent: **PASS**
- Product universe: **UNPROVABLE**
- Equivalence engine: **UNPROVABLE**
- Evidence ledger: **UNPROVABLE**
- Criteria: **PASS**
- Weighting: **FAIL**
- Scoring: **FAIL**
- Hard gates: **FAIL**
- Total solution cost: **UNPROVABLE**
- Rank justification: **FAIL**
- Honest comparison: **FAIL**
- Affiliate value: **PASS**
- Fact-check: **PASS for the core product facts checked; does not validate the numeric scores**
- Search intent QA & linking: **PASS**
- Writing / SEO / GEO: **FAIL for publication readiness**

## Detailed evaluation

### 1. Routing & search intent — PASS

The page has a distinct commercial-decision role. It ranks concrete products for professional work, whereas `/usages/prise-de-notes-professionnelle/` explains when an E Ink notebook is useful at work, the workflow to test and the criteria that matter before ranking products.

The current criteria are broadly aligned with the stated job: organization, export, PDF, applications, writing, simplicity and functions without subscription.

### 2. Product Universe — UNPROVABLE

The record contains five `ELIGIBLE` products but no trace of the candidate set that was considered before selection, no `EXCLUDED` products and no exclusion reasons.

The gate therefore cannot prove that the universe was constructed before the winner was known, nor that obvious alternatives were considered and rejected for a decision-related reason rather than simply omitted.

This is not proof that the current five products are wrong. It is proof that the Product Universe phase of the workflow is not auditable from the persisted data.

### 3. Equivalence Engine — UNPROVABLE

No equivalence relation is persisted between the candidates.

That matters here because the products do not offer exactly the same proposition:

- BOOX Go 10.3 (Gen II) Lumi is an Android 15 ePaper tablet with Google Play / third-party apps and front light;
- Supernote Manta uses a specialized Android-based system focused on writing and organization and explicitly positions its software as subscription-free;
- BOOX Note Air5 C adds color, Android 15, third-party apps and optional keyboard-oriented workflows;
- reMarkable products use a more closed, purpose-built software ecosystem with optional Connect services.

A global score can still be useful, but the workflow requires the comparability assumptions to be explicit before averaging these propositions.

### 4. Evidence Ledger — UNPROVABLE

All 35 criterion scores in this comparison are marked `VERIFIED`, while every justification says that the numeric score is an `editorial normalization`.

This conflates two different objects:

1. a fact can be verified by an official source;
2. the translation of that fact into `8/10`, `9/10` or `10/10` remains an editorial inference.

Example: BOOX officially documents Android 15, Google Play / third-party apps, PDF support and an included stylus for the Go 10.3 (Gen II) Lumi. BOOX Help also documents note export to PNG/PDF/.note. Those facts support a strong apps/export proposition, but they do not independently verify the scores `apps = 10` and `export = 10`.

Likewise, Supernote officially documents headings, keywords, stars, links, navigation features and no subscription. These support its organization/no-subscription positioning but do not independently verify `organization = 10` or `writing = 10`.

Sources checked during this evaluation:

- https://shop.boox.com/products/go103gen2lumi
- https://help.boox.com/hc/en-us/articles/8569373888788-Handwritten-Notes
- https://supernote.com/products/supernote-manta
- https://support.supernote.com/en_US/organizing/1759244-using-titles-keywords-and-stars
- https://support.supernote.com/en_US/organizing/2126285-untitled-article
- https://shop.boox.com/products/noteair5c
- https://remarkable.com/products/remarkable-paper/pro/details/features
- https://remarkable.com/shop/connect/pricing

### 5. Criteria — PASS

The criteria are materially connected to the professional job and differ from the generic overall comparison.

However, the professional usage page itself identifies company IT policy, cloud authorization and handling of sensitive data as possible **hard gates**. Those should not be absorbed into a generic `apps` or `export` score when they are eliminatory for a specific work environment.

### 6. Weighting — FAIL

The weights sum to 100 and are plausible, but the repository does not persist a criterion-by-criterion rationale sufficient to prove why these exact weights were chosen before seeing the winner.

More importantly, the ranking is highly sensitive.

Baseline:

| Product | Score |
| --- | ---: |
| BOOX Go 10.3 (Gen II) Lumi | 8.75 |
| Supernote Manta | 8.70 |
| BOOX Note Air5 C | 8.65 |

The 0.05-point lead of BOOX over Manta decomposes as follows:

| Criterion | BOOX contribution vs Manta |
| --- | ---: |
| Organization | -0.40 |
| Export | +0.20 |
| PDF | 0.00 |
| Apps | +0.75 |
| Writing | -0.30 |
| Simplicity | -0.20 |
| No subscription | 0.00 |
| **Net** | **+0.05** |

A single reasonable five-point shift reverses the winner. For example, reducing `apps` from 15% to 10% and increasing `writing` from 15% to 20% produces approximately:

- Supernote Manta: **8.95**
- BOOX Go 10.3 (Gen II) Lumi: **8.65**

Similarly, moving five points from `apps` to `simplicity` also makes Manta the winner.

The current page may therefore state that BOOX leads **under this specific weighting**, but it cannot yet present BOOX as a robust professional winner without a documented sensitivity/confidence result.

### 7. Scoring — FAIL

The score calculation itself is mechanically reproducible and correct:

`total = Σ(score × weight) / 100`

The blocker is not arithmetic. It is score justification.

Every score is supported by the same generic pattern: official capabilities reviewed, then numeric editorial normalization. The workflow requires the deciding scores to state which concrete, sourced difference explains the value relative to competitors.

This is especially important for the cells that determine the top three:

- BOOX Go Lumi: `export 10`, `apps 10`, `organization 8`, `writing 8`, `simplicity 6`;
- Supernote Manta: `organization 10`, `writing 10`, `apps 5`, `simplicity 8`;
- BOOX Note Air5 C: `export 10`, `apps 10`, `simplicity 5`.

Until those mappings are justified specifically, the ranking is numerically consistent but not methodologically defensible enough for publication.

### 8. Hard Gates — FAIL

No `hard_gates` are persisted or applied before averaging.

For this exact professional intent, the site already recognizes potentially eliminatory constraints such as:

- company IT / security policy;
- unauthorized personal cloud or external synchronization;
- required work application unavailable on the device;
- required PDF/export path incompatible with the organization;
- confidential-data constraints.

A device that cannot satisfy one of these requirements should be eliminated for that user rather than merely lose a few tenths in `apps` or `export`.

### 9. Total Solution Cost — UNPROVABLE

The page correctly warns readers to compare the usable configuration rather than the bare device, but that calculation is not persisted.

The candidates are currently shown with heterogeneous price bases (EUR, USD, possible duties/import, different included accessories). reMarkable also documents that some professional cloud/integration functionality is tied to Connect, whereas Supernote explicitly states no subscription for software updates/features in its product positioning.

Cost is not a weighted criterion in this professional ranking, so this does not directly invalidate the arithmetic. It does mean the workflow cannot prove that the professional solution cost was consistently assessed.

### 10. Rank Justification — FAIL

The page explains the winner mainly by repeating its three highest weighted scores. It does not explain the decisive trade-off against the #2.

The actual decision is much more useful when expressed as:

- BOOX Go Lumi gains primarily from open apps and export flexibility;
- Supernote Manta gains primarily from organization, writing and simplicity;
- the final difference is only 0.05 under the current weighting.

That is the core professional trade-off, and it should drive the verdict.

The current #1 paragraph therefore does not satisfy the workflow's requirement to explain **why #1 beats #2, what #1 does not win, and when #2 becomes the better choice**.

### 11. Honest Comparison Standard — FAIL

Positive points already present:

- the page explicitly states that it is desk research, not a physical test;
- important limitations are shown;
- affiliate commission is stated as excluded from ranking;
- the page warns that the best product depends on the user's blocking criterion.

The blocker is confidence calibration: a 0.05 lead is still introduced as a straightforward #1 without showing that modest, plausible changes in weighting reverse the result.

The ranking should therefore be presented as conditional until the weighting rationale and sensitivity analysis are documented.

### 12. Architecture / writing — FAIL for publication readiness

The article has a useful decision structure and avoids fabricated hands-on claims.

However:

- the visible hero still says `Contenu en préparation`;
- several product blocks are highly symmetrical and mostly repeat score summaries;
- the #1/#2 trade-off is less explicit than the raw scoring actually allows;
- rounded display scores (`8.8`, `8.7`, `8.7`) hide the already-small gaps and can imply more confidence than the methodology supports.

These are not reasons to add more sections. They are reasons to make the existing decision logic more explicit after the methodological blockers are fixed.

### 13. Affiliate Value — PASS

The record explicitly states `affiliate_commission_used_in_ranking: false`, the article says commissions do not enter the calculation, product limits remain visible and the sidebar links to the affiliation-transparency page.

No evidence was found in the current pipeline that commissions alter weights or ranking.

### 14. Fact-check — PASS for core product facts, not for numeric scores

The main factual direction of the top candidates was checked against current official sources on 2026-09-09:

- BOOX Go 10.3 (Gen II) Lumi: Android 15, Google Play / third-party apps, front light, PDF/document support and included stylus confirmed;
- BOOX notes: export to PNG/PDF/.note confirmed by BOOX Help;
- Supernote Manta: specialized Android-based OS, broad document support, desktop/mobile partner apps and no-subscription positioning confirmed;
- Supernote organizational mechanisms such as headings, keywords, stars and links are documented by Supernote Support;
- BOOX Note Air5 C: Android 15, Google Play / third-party apps, PDF support, color screen, front light and optional keyboard workflow confirmed;
- reMarkable: PDF import/export and cloud/app capabilities confirmed; current Connect documentation shows that some enhanced cloud/work features are subscription-linked.

This fact-check does **not** turn the numeric editorial scores into verified measurements.

### 15. Search Intent QA & Internal Linking — PASS

The professional comparison remains distinct from the professional usage page. It links onward to product/brand pages and supporting guides.

A direct contextual link back to `/usages/prise-de-notes-professionnelle/` could improve the decision path for readers who have not yet defined their hard gates, but its absence is not by itself a publish blocker.

### 16. Writing / SEO / GEO — FAIL for publication readiness

The page has a clear entity structure and a quotable verdict, but the current verdict is insufficiently conditioned for a highly sensitive ranking.

For GEO/citability, the preferred relationship should be explicit:

`professional need → decisive criterion → verified capability → editorial score → conditional recommendation`

At present, the `verified capability → score` step is not sufficiently documented.

The visible `Contenu en préparation` marker is also incompatible with final publication.

### 17. Persistence / regeneration — FAIL

This is a structural blocker.

`generate_comparison_metadata.py` currently regenerates the JSON using only the product list, product-level source, generic scores, weights and ranking. It does not durably preserve:

- candidate exclusions;
- equivalence status;
- criterion-level evidence ledger;
- specific score rationale;
- hard gates;
- total solution cost;
- sensitivity / confidence.

Fixing only the JSON would therefore create a false sense of methodological completeness: the next regeneration could erase the work.

## Blockers

1. **Product Universe** — considered/excluded candidates and exclusion reasons are not persisted.
2. **Equivalence Engine** — comparability between specialized notebooks, open Android tablets and reMarkable ecosystems is not persisted.
3. **Evidence Ledger / Scoring** — score facts and score inference are conflated; all decisive score justifications are generic.
4. **Weighting** — the #1 is highly sensitive and the exact weight rationale is not auditable.
5. **Hard Gates** — professional IT/security/cloud/application constraints are not applied before the average.
6. **Rank Justification** — the #1 does not explain the decisive trade-off against #2 despite a 0.05-point gap.
7. **Honest Comparison** — confidence in the winner is not calibrated to the sensitivity of the ranking.
8. **Persistence** — the current metadata generator cannot durably store the methodological fields needed to resolve the blockers.
9. **Publication readiness** — the visible page still contains `Contenu en préparation`.

## Required corrections

1. Return to **Product Universe**: persist considered candidates, exclusions and reasons in the durable source of truth.
2. Return to **Equivalence Engine**: record whether each candidate is exactly, functionally or partially comparable for the professional job.
3. Return to **Evidence Ledger**: attach concrete evidence to the criterion differences that change the ranking; distinguish verified fact from inferred score.
4. Return to **Weighting**: document why each professional weight is appropriate before the result, then persist a sensitivity result/confidence level.
5. Return to **Hard Gates**: add professional eliminators such as company IT/security/cloud compatibility and required-app compatibility where applicable.
6. Return to **Total Solution Cost** if retained as part of the decision: normalize required accessories, subscriptions and regional price caveats rather than showing heterogeneous sticker prices only.
7. Return to **Rank Justification**: rewrite the top verdict around BOOX openness/export versus Supernote organization/writing/simplicity, and make the recommendation conditional if the sensitivity remains high.
8. Update **`generate_comparison_metadata.py` / durable source data** so all new methodology fields survive regeneration.
9. Regenerate the page, remove the preparation marker only when the methodological blockers are resolved, then rerun the full gate.

## Residual risks

- Product availability, pricing and subscription terms are volatile and require refresh before publication.
- A professional user's company policy can override the global ranking entirely.
- The 0–10 score scale is editorial; displaying hundredths in persisted ranking data should not be interpreted as laboratory precision.
- The current market universe may be reasonable, but it cannot be declared complete until exclusions are documented.

## Decision

**KEEP NOINDEX**

The comparison is mechanically coherent and already transparent about desk research, but it does not yet satisfy the full `comparison-content-workflow` at publish-gate severity. It is **not READY FOR HUMAN VALIDATION** until the methodological blockers above are resolved.