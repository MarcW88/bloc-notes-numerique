# Bons plans — Publish review

Date : 2026-09-10
Workflow : `.agents/skills/deal-analysis-workflow/SKILL.md`
Mode : `PUBLISH_REVIEW`
Scope : `/bons-plans/` + 7 pages avec registre deals.

## Résultat substantiel

`PASS — READY_FOR_HUMAN_VALIDATION`

Ce PASS concerne les gates éditoriaux, factuels et de cohérence inter-pages inspectés après le `CLUSTER_AUDIT` et les corrections.

## Gates contrôlés

- intention de chaque page satisfaite ;
- distinction claire entre offre active, prix à surveiller, offre expirée, sold out et événement futur ;
- prix de référence documentés lorsqu'une économie est revendiquée ;
- aucune offre sold out présentée comme achetable ;
- aucun faux compte à rebours ou sentiment d'urgence ;
- aucun « meilleur prix » ou « prix historique » non défendable ;
- aucune recommandation dictée par la commission ;
- aucune transformation des pages Bons plans en comparatifs produits ;
- valeur éditoriale conservée sans dépendre des liens affiliés ;
- sources et registres synchronisés pour les pages corrigées ;
- conflits BOOX conservés comme contradictions au lieu d'être artificiellement résolus ;
- architectures éditoriales suffisamment distinctes dans le cluster ;
- `deal_content.py` synchronisé avec les HTML pour éviter une régression lors de la régénération ;
- aucun placeholder `Contenu à rédiger` ou `Contenu en préparation` trouvé dans le dépôt ;
- `noindex,follow` conservé sur les pages du cluster.

## Statut page par page après corrections

| URL | Résultat |
|---|---|
| `/bons-plans/` | PASS — navigation hub cohérente |
| `/bons-plans/bloc-notes-numerique/` | PASS — hub live réaligné sur les registres marque |
| `/bons-plans/remarkable/` | PASS — preuve reconditionné modernisée, bundles conservés |
| `/bons-plans/kindle-scribe/` | PASS — aucune correction substantielle requise |
| `/bons-plans/kobo-elipsa/` | PASS — aucune correction substantielle requise |
| `/bons-plans/boox/` | PASS — conflit de références Air4 C qualifié, Air5 C checkout-sensitive |
| `/bons-plans/bloc-notes-numerique-occasion/` | PASS — statut BOOX corrigé en sold out et sources reconditionné actualisées |
| `/bons-plans/black-friday/` | PASS — baselines documentées et événement maintenu NOT_STARTED |

## Gate machine / GitHub Actions

Le dépôt contient `.github/workflows/validate-deal-workflow.yml`, déclenché sur les pushes `main` touchant les registres, le contenu générateur ou `/bons-plans/**`.

Ce workflow :

1. compile `deal_content.py`, `apply_deal_content.py` et `validate_deal_workflow.py` ;
2. exécute `python validate_deal_workflow.py` ;
3. exécute `python apply_deal_content.py` ;
4. vérifie l'idempotence via `git diff --exit-code -- _generate.py AGENTS.md bons-plans`.

Le connecteur GitHub utilisé pour cette revue ne remonte pas les runs déclenchés par `push` via son endpoint de runs par commit ; il ne permet donc pas de confirmer ici le résultat console du run. Les conditions observables du validateur ont été contrôlées directement sur les fichiers, mais ce document ne prétend pas remplacer un résultat CI réel.

## Indexation

Conserver `noindex,follow`.

Le PASS éditorial ne vaut pas instruction d'indexer. L'indexation reste soumise à validation humaine explicite et instruction explicite de rendre les pages indexables.
