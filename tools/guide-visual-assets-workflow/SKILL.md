---
name: guide-visual-assets-workflow
description: Workflow déterministe pour créer, intégrer et valider des visuels éditoriaux utiles dans des guides : arbres de décision, workflows, checklists, timelines, tailles, décompositions de coûts et cartes d'écosystème. Les visuels sont générés depuis des manifests versionnés, restent régénérables et ne doivent jamais dupliquer un tableau HTML déjà présent.
---

# Guide Visual Assets Workflow

## Objectif

Ajouter des visuels qui améliorent réellement la compréhension et la décision, pas des illustrations décoratives génériques ni des tableaux redessinés en image.

Principe :

> **contenu -> besoin visuel distinct -> manifest -> rendu déterministe -> intégration accessible -> QA**

## Types de visuels prioritaires

- `decision_tree`
- `process_flow`
- `size_comparison`
- `cost_breakdown`
- `checklist`
- `timeline`
- `ecosystem_map`

## Règle de non-redondance

Avant de créer un visuel, inspecter les tableaux, listes et encadrés déjà présents dans la page.

Un visuel est interdit s'il reproduit essentiellement la même information qu'un tableau HTML, même avec des couleurs, icônes ou une mise en page différente.

Si la page possède déjà un tableau comparatif :
- conserver le tableau en HTML ;
- choisir un autre angle visuel : chemin de décision, mécanisme, séquence, circulation d'un fichier, relation entre composants, ordre de vérification ou représentation spatiale ;
- ou ne créer aucun visuel si aucune représentation complémentaire n'apporte de valeur.

`decision_matrix` et toute représentation tabulaire en SVG sont interdits dans ce workflow.

## Workflow

1. Lire la page complète et son brief.
2. Inventorier les représentations déjà présentes : tableaux, listes, encadrés et étapes.
3. Identifier une information qui gagne réellement à être visualisée et qui n'est pas déjà représentée.
4. Refuser un visuel s'il ne fait que répéter un paragraphe, une liste ou un tableau.
5. Choisir un type de visuel non tabulaire.
6. Créer `.content/visuals/<slug>.json`.
7. Utiliser uniquement des affirmations déjà présentes et validées dans la page ou dans ses sources.
8. Générer le SVG avec `scripts/render_visual_assets.py`.
9. Intégrer le visuel dans une balise `<figure>` avec `alt`, `figcaption`, dimensions et lazy loading.
10. Valider avec `scripts/validate_visual_assets.py` ou le validator du site.
11. Conserver le robots meta existant et ne jamais publier/indexer automatiquement.

## Règles éditoriales

- Pas de faux produit, faux screenshot, faux benchmark ou fausse mesure.
- Pas de chiffre non sourcé ajouté uniquement pour remplir un graphique.
- Pas de marque dans un schéma générique si elle n'améliore pas la décision.
- Un arbre de décision doit expliciter les conditions qui font bifurquer le choix.
- Un process flow doit montrer une séquence ou circulation qui n'est pas évidente dans le texte.
- Une checklist visuelle doit hiérarchiser une vérification, pas recopier une liste déjà présente mot pour mot.
- Une comparaison de tailles doit représenter une différence spatiale réelle.
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
- visuel tabulaire ou `decision_matrix` ;
- visuel qui reproduit essentiellement un tableau HTML existant ;
- image externe embarquée dans le SVG ;
- page perd son `noindex` en brouillon ;
- plusieurs copies du même visuel sont injectées.
