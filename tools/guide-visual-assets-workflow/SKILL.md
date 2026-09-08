---
name: guide-visual-assets-workflow
description: Workflow déterministe pour créer, intégrer et valider des visuels éditoriaux utiles dans des guides : arbres de décision, matrices, workflows, checklists, timelines, tailles et décompositions de coûts. Les visuels sont générés depuis des manifests versionnés, restent régénérables et ne doivent pas inventer de données produit.
---

# Guide Visual Assets Workflow

## Objectif

Ajouter des visuels qui améliorent réellement la compréhension et la décision, pas des illustrations décoratives génériques.

Principe :

> **contenu -> besoin visuel -> manifest -> rendu déterministe -> intégration accessible -> QA**

## Types de visuels prioritaires

- `decision_tree`
- `process_flow`
- `decision_matrix`
- `size_comparison`
- `cost_breakdown`
- `checklist`
- `timeline`
- `ecosystem_map`

## Workflow

1. Lire la page complète et son brief.
2. Identifier une information qui gagne réellement à être visualisée.
3. Refuser un visuel s'il ne fait que répéter un paragraphe.
4. Choisir un type de visuel.
5. Créer `.content/visuals/<slug>.json`.
6. Utiliser uniquement des affirmations déjà présentes et validées dans la page ou dans ses sources.
7. Générer le SVG avec `scripts/render_visual_assets.py`.
8. Intégrer le visuel dans une balise `<figure>` avec `alt`, `figcaption`, dimensions et lazy loading.
9. Valider avec `scripts/validate_visual_assets.py` ou le validator du site.
10. Conserver le robots meta existant et ne jamais publier/indexer automatiquement.

## Règles éditoriales

- Pas de faux produit, faux screenshot, faux benchmark ou fausse mesure.
- Pas de chiffre non sourcé ajouté uniquement pour remplir un graphique.
- Pas de marque dans un schéma générique si elle n'améliore pas la décision.
- Un arbre de décision doit expliciter les conditions qui font bifurquer le choix.
- Un tableau transformé en image doit apporter une hiérarchie visuelle supplémentaire.
- Le SVG doit rester lisible sur mobile grâce au `viewBox` et au responsive CSS.
- Le texte important doit aussi exister dans le HTML de la page : le visuel ne doit jamais être la seule source d'information.

## Source de vérité

Le manifest JSON est la source de vérité du visuel. Le SVG généré est un artefact.

Une régénération du contenu éditorial ne doit pas obliger à redessiner manuellement l'image : le post-processeur réinjecte le visuel à partir du manifest.

## Gate

FAIL si :
- asset manquant ;
- `alt` vide ;
- légende absente ;
- SVG sans `viewBox` ;
- données non présentes dans le contenu/source ;
- visuel purement décoratif déclaré comme décisionnel ;
- image externe embarquée dans le SVG ;
- page perd son `noindex` en brouillon ;
- plusieurs copies du même visuel sont injectées.
