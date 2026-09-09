# Human validation — comparison cluster

Date: 9 septembre 2026
Scope: `/comparatifs/`
Human decision: **APPROVED**
Publication state: **KEEP_NOINDEX**

## Validation

The full comparison cluster has been reviewed after:

- `comparison-analysis-workflow / CLUSTER_AUDIT`;
- individual `comparison-content-workflow` rewrites where required;
- machine validation;
- `comparison-analysis-workflow / PUBLISH_REVIEW`.

The 14 comparison pages are approved editorially in their current bespoke form.

## Approved URLs

- `/comparatifs/meilleur-bloc-notes-numerique/`
- `/comparatifs/tablette-e-ink/`
- `/comparatifs/bloc-notes-numerique-professionnel/`
- `/comparatifs/bloc-notes-numerique-etudiant/`
- `/comparatifs/bloc-notes-numerique-couleur/`
- `/comparatifs/bloc-notes-numerique-a4/`
- `/comparatifs/bloc-notes-numerique-sans-abonnement/`
- `/comparatifs/bloc-notes-numerique-pas-cher/`
- `/comparatifs/kindle-scribe-vs-remarkable/`
- `/comparatifs/kindle-scribe-vs-kobo-elipsa/`
- `/comparatifs/remarkable-vs-boox/`
- `/comparatifs/remarkable-vs-supernote/`
- `/comparatifs/boox-vs-supernote/`
- `/comparatifs/kobo-elipsa-vs-remarkable/`

## Conditions retained

- All pages remain `noindex,follow`.
- Human editorial approval does not imply indexation approval.
- Indexation requires a separate explicit instruction.
- Freshness-sensitive claims such as prices, bundles, availability, subscriptions and fast-moving product ranges should be rechecked if publication is delayed materially.

## Branch / merge note

The approved comparison work is already present on `main`; no additional merge is required for the approved implementation.

Open PR #11 (`comparison-editorial-publish-gate`) predates the final skill-first comparison methodology and still contains the superseded scoring/hard-gate-heavy v2 approach. It must not be merged into the current `main` without reconciliation because it would reintroduce rules deliberately removed from the final workflow.
