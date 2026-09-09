# Validation d'indexation — cluster comparatifs

Date : 9 septembre 2026

## Décision

Le cluster `/comparatifs/` a déjà passé :

- le `CLUSTER_AUDIT` ;
- les réécritures nécessaires via `comparison-content-workflow` ;
- les `PUBLISH_REVIEW` ;
- la validation humaine éditoriale ;
- la revue visuelle Playwright desktop/mobile.

Le 9 septembre 2026, une instruction humaine explicite a été donnée pour **indexer les pages comparatifs**.

## Routes approuvées

L'approbation couvre le hub `/comparatifs/` et les 14 pages comparatives actuellement publiées. La liste technique exacte est maintenue dans `comparison_publication.py`.

Ces routes doivent utiliser :

`<meta name="robots" content="index,follow">`

## Garde-fou

Cette validation ne vaut pas pour de futures URLs ajoutées à `/comparatifs/`.

Toute nouvelle page doit rester `noindex,follow` jusqu'à :

1. `PUBLISH_REVIEW` PASS ;
2. validation humaine ;
3. instruction explicite d'indexation ;
4. ajout explicite de sa route au manifeste `comparison_publication.py`.
