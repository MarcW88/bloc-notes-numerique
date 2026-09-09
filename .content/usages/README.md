# Usage content records

Ce dossier contient la source de vérité éditoriale des pages sous `/usages/`.

Chaque page doit disposer d'un fichier `<slug>.json` dérivé de `_template.json` avant rédaction. Le fichier conserve le cadrage d'intention, le JTBD, les circonstances, les workflows réels, les critères hiérarchisés, les contre-indications, les familles de solutions, le registre de preuves et les handoffs vers les guides ou comparatifs.

## Pages actuelles

- `prise-de-notes-professionnelle`
- `prise-de-notes-etudiant`
- `prise-de-notes-reunion`
- `annotation-pdf`
- `lecture-et-prise-de-notes`
- `dessin`
- `remplacer-cahiers-papier`

## Frontière éditoriale

- `/usages/` explique le besoin et les critères liés au job.
- `/comparatifs/` classe les produits.
- `/guides/` explique un critère, une technologie ou une procédure.
- `/marques/` documente les écosystèmes et produits.

Un fichier usage ne doit pas contenir de ranking produit comme source de vérité. Lorsqu'un classement est nécessaire, le workflow doit passer la main à `comparison-content-workflow`.

## Niveau de preuve

Les statuts autorisés dans les analyses JTBD sont :

- `OBSERVED`
- `SUPPORTED`
- `INFERRED`
- `HYPOTHESIS`
- `UNKNOWN`

Sans interview ou donnée utilisateur, une motivation émotionnelle/sociale ne doit pas être présentée comme un comportement observé.

## Statuts de production

`JTBD_READY` → `EVIDENCE_READY` → `DRAFT_READY` → `QA_IN_PROGRESS` → `HUMAN_APPROVED` → `PUBLISHABLE`.

`REVISION_REQUIRED` peut intervenir à tout moment. Les pages restent `noindex,follow` jusqu'à validation humaine explicite.
