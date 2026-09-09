# Comparison methodology records

Les fichiers `.content/comparisons/<slug>.json` sont la source de vérité méthodologique des pages `/comparatifs/`.

Ils doivent expliquer pourquoi le classement existe, indépendamment du texte final.

## Principe

> Critères avant gagnant. Preuves avant scoring. Scoring avant rédaction. Affiliation après décision.

Le HTML ne doit jamais être la seule trace de :

- l'intention et du job utilisateur ;
- l'univers produit considéré ;
- des exclusions ;
- des critères et poids ;
- des hard gates ;
- des preuves ;
- des notes et de leurs justifications ;
- du classement ;
- des incertitudes ;
- de la date de recherche.

## Validation automatique

`python3 validate_comparisons.py` contrôle uniquement les blockers détectables automatiquement : intégrité du registre, somme des poids, exclusion de la commission, couverture des scores, cohérence mathématique du ranking, structure HTML, noindex, faux langage hands-on, métadiscours et quelques patterns éditoriaux à haut risque.

Le validateur n'impose aucun nombre minimum de mots, H2/H3, tableaux ou liens internes.

Un `PASS` automatique ne signifie pas que la page est publiable.

## Publish gate manuel obligatoire

Après le validateur, exécuter :

`.agents/skills/comparison-editorial-publish-gate/SKILL.md`

Ce gate doit notamment juger :

- la complétude réelle de l'univers produit ;
- l'équivalence des candidats ;
- la pertinence des critères ;
- la robustesse des pondérations ;
- la qualité spécifique des justifications de notes ;
- la sensibilité du gagnant à des poids raisonnablement différents ;
- les hard gates et le coût total ;
- la cohérence entre scoring, verdict et texte ;
- la transparence sur les limites et le niveau de preuve ;
- l'indépendance du ranking vis-à-vis de l'affiliation ;
- la naturalité, le GEO, le SEO éditorial et la cannibalisation.

Un seul blocker suffit à maintenir la page en `noindex,follow`.

## Point d'attention sur `VERIFIED`

Une source officielle peut vérifier un fait produit. Elle ne vérifie pas automatiquement une note éditoriale de `8/10` ou `9/10`.

Le registre doit distinguer la preuve du fait et l'inférence qui transforme ce fait en score. Une justification générique du type « capacités officielles consultées, score normalisé éditorialement » ne suffit pas à défendre une différence de note entre deux produits.
