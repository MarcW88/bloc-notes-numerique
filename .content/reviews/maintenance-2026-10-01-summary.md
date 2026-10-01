# Maintenance éditoriale — 1 octobre 2026

Main récupéré dans un nouveau checkout : 5b798c38648fdc32a9bbb0f2f6742b2dca9b7951. Prepare --max-pages 10 : dix pages lues et auditées, avec sources web primaires consultées le 1 octobre. Les dix audits ont été enregistrés via record avant les modifications de contenu. Les empreintes enregistrées sont celles du contenu audité avant correction.

| Page | Décision | Travail |
|---|---|---|
| /bons-plans/black-friday/ | LIGHT_UPDATE | Air6 dans la surveillance, prix du 10 septembre conservés comme historiques, aucune garantie quotidienne |
| /comparatifs/bloc-notes-numerique-a4/ | LIGHT_UPDATE | Source Fujitsu réparée ; chiffres non revérifiables retirés |
| /guides/annoter-pdf-tablette-e-ink/ | LIGHT_UPDATE | Source BOOX remplacée ; précision d’export non confirmée retirée |
| /marques/boox/ | LIGHT_UPDATE | Air6 Android16 actuel, Air5 précédent ; anciens liens documentation retirés |
| /usages/annotation-pdf/ | KEEP | Consolidation existante, noindex et canonical Guide préservés |
| /bons-plans/bloc-notes-numerique-occasion/ | LIGHT_UPDATE | Stock BOOX non confirmé ; 359€ historique, pas offre active |
| /comparatifs/bloc-notes-numerique-couleur/ | LIGHT_UPDATE | Air6 documentaire, test Air5 limité à cette génération |
| /guides/autonomie-tablette-e-ink/ | KEEP | Explication et limites documentaires conservées, aucun essai inventé |
| /marques/boox/accessoires/ | LIGHT_UPDATE | Compatibilité clavier Air6/Air5 attachée au SKU actuel |
| /usages/dessin/ | LIGHT_UPDATE | Atelier juin2026 version1.1.78 ; source Notes BOOX remplacée |

Les corrections utilisent les cinq paires de workflows existantes et leurs skills spécialisés. Sources, preuves, incertitudes, valeur à préserver et handoffs figurent dans chaque rapport de page. Les huit corrections ont été régénérées depuis les sources Python, avec modules produits et liens affiliés existants. Registres Deal/Comparison/Usage et métadonnées Brand mis à jour. Aucun changement structurel, suppression, merge, URL, canonical ou indexation.

## Validation et limites

PASS : guides, comparatifs, usages, deals, modules produits, indexation, hreflang ; Brand restreint aux deux pages du lot ; liens internes, canonical et robots des huit sorties ; git diff --check. Deux KEEP et toutes les sorties HTML hors lot conservées identiques à main.

Échecs globaux préexistants à traiter séparément : validate_brands signale /marques/boox/boox-note-air/ sans concept de limitations ; validate_inline_affiliate_links signale /marques/kindle-scribe/ sans CTA attendu. Ces fichiers sont byte-identiques à main. Warnings Deal : cinq offres périmées sur remarkable, bloc-notes-numerique et boox, hors pages auditées. Aucun test matériel ni rendu navigateur réalisé. PUBLISH_REVIEW des huit corrections : PASS — READY_FOR_HUMAN_VALIDATION sur leur périmètre, pas certification verte de tout le site.

## Lots ouverts

PR #11 : https://github.com/MarcW88/bloc-notes-numerique/pull/11, proposition méthodologique comparatifs et pilote professionnel, en attente de décision humaine. Pas d’audit des pages A4/couleur dans cette PR ; pas de duplication de ce pilote. Chevauchement des registres Comparison A4/couleur pouvant demander une résolution de conflit. La méthode non fusionnée n’a pas été appliquée.

Les prix et stocks restent valables uniquement pour une vérification datée et sa durée de validité ; cette maintenance ne constitue pas une veille quotidienne Black Friday. Aucun service IA ni API modèle payante séparée utilisé. Ce lot reste à valider et fusionner humainement.
