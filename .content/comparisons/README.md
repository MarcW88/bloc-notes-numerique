# Comparison methodology records

Les fichiers `.content/comparisons/<slug>.json` sont les snapshots méthodologiques générés pour les pages `/comparatifs/`.

Leur rôle est de rendre le ranking auditable. Ils ne doivent cependant pas être considérés isolément : dans l'implémentation actuelle, le pipeline est réparti entre plusieurs fichiers.

## Pipeline réel

1. `comparison_products.py` — baseline produit partagée, sources, prix repérés, forces/limites et scores par critère.
2. `comparison_pages.py` — intention par page, job utilisateur, produits retenus, poids et ranking.
3. `generate_comparison_metadata.py` — transforme ces données en `.content/comparisons/<slug>.json`.
4. `comparison_content.py` — transforme le ranking en contenu éditorial.
5. `comparatifs/<slug>/index.html` — sortie reçue par le lecteur.

L'évaluation doit donc vérifier la cohérence de bout en bout et ne jamais auditer seulement le HTML.

## Principe du workflow Comparison

> Critères avant gagnant. Preuves avant scoring. Scoring avant rédaction. Affiliation après décision.

Le référentiel complet est :

`.agents/skills/comparison-content-workflow/SKILL.md`

Le gate final est :

`.agents/skills/comparison-editorial-publish-gate/SKILL.md`

Malgré son nom de publish gate, ce skill est un **workflow d'évaluation de conformité au comparison-content-workflow**. Il n'est pas dérivé du Brand gate.

## Ce que le JSON devrait pouvoir prouver

Selon le workflow Comparison, la méthodologie devrait permettre de reconstruire :

- intention et type de comparatif ;
- univers produit considéré ;
- exclusions ;
- équivalence/comparabilité ;
- Evidence Ledger ;
- critères ;
- pondérations ;
- scores et justification de leur normalisation ;
- hard gates ;
- coût total lorsque pertinent ;
- ranking ;
- niveau de confiance ;
- date de recherche.

Si une étape critique n'est pas persistée, le gate peut la classer `UNPROVABLE`. Il ne doit jamais supposer qu'elle a été correctement réalisée.

## Point critique de l'implémentation actuelle

`generate_comparison_metadata.py` recrée les JSON à partir de `comparison_products.py` et `comparison_pages.py`.

Cela signifie qu'une information ajoutée uniquement à la main dans un JSON — par exemple une exclusion, un hard gate ou un Evidence Ledger — risque d'être écrasée au prochain run si elle n'existe pas dans une source durable utilisée par le générateur.

La durabilité de la méthode fait donc partie de l'évaluation.

## Preuve factuelle ≠ note éditoriale

Une source officielle peut confirmer un fait produit. Elle ne confirme pas automatiquement qu'un appareil mérite `8/10` ou `9/10`.

Le workflow d'évaluation doit distinguer :

1. le fait utilisé comme preuve ;
2. le raisonnement qui transforme ce fait en score ;
3. le poids donné au critère ;
4. l'impact de ce score sur le ranking.

Une justification générique du type « capacités officielles consultées, score normalisé éditorialement » ne suffit pas lorsqu'une note change le classement.

## Validation automatique

`python3 validate_comparisons.py` vérifie la cohérence mécanique du pipeline actuel :

- `comparison_pages.py` ↔ JSON ;
- `comparison_products.py` ↔ scores JSON ;
- recalcul du score pondéré ;
- ordre du ranking ;
- cohérence JSON ↔ HTML ;
- robots/noindex et structure SEO de base ;
- faux langage hands-on et quelques blockers détectables automatiquement.

Il n'impose aucun quota de mots, H2/H3, tableaux ou liens.

Il émet aussi des warnings lorsque des phases du workflow Comparison ne sont pas persistées ou restent impossibles à prouver automatiquement.

Un `PASS` machine ne signifie jamais que la page est publiable.

## Evaluation manuelle obligatoire

Après le validateur, exécuter le `Comparison Workflow Evaluation Gate`.

Il suit les étapes du workflow Comparison :

1. routing / search intent ;
2. Product Universe ;
3. Equivalence Engine ;
4. Evidence Ledger ;
5. critères ;
6. pondération ;
7. scoring ;
8. Hard Gates ;
9. Total Solution Cost ;
10. Rank Justification ;
11. Honest Comparison Standard ;
12. architecture/rédaction ;
13. Affiliate Value ;
14. fact-check ;
15. Search Intent QA / Internal Linking ;
16. finition / SEO / GEO ;
17. persistance et régénération ;
18. décision de publication.

Un seul blocker critique ou une phase nécessaire `UNPROVABLE` suffit à maintenir la page en `noindex,follow`.
