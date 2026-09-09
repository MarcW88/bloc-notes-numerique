# Guide workflows — skills inventory

Date: 2026-09-09
Scope: `/guides/`

## Objectif

Les deux workflows Guide doivent rester des orchestrateurs : la méthodologie générique est déléguée aux skills réutilisés ; le custom ne couvre que ce qui est spécifique au rôle éditorial du cluster `/guides/`.

## Skills réutilisés / vendored

| Responsabilité | Skill principal | Origine / rôle |
|---|---|---|
| Audit keep/update/merge | `seo-content-audit` | Rampstack vendored |
| Recherche / clustering / intent | `seo-keyword` | Rampstack vendored |
| Analyse fine de l'intention | `search-intent` | skill existant du dépôt |
| Diagnostic de refresh | `content-refresh` | skill existant du dépôt |
| Vérification factuelle | `fact-check` | skill existant du dépôt |
| Jugements expérientiels si nécessaires | `evidence-based-reviews` | skill existant / vendored |
| Valeur éditoriale affiliée | `affiliate-value` | skill existant du dépôt |
| Brief page par page | `content-brief-authoring` | Rampstack vendored |
| Rédaction | `content-and-copy` | Rampstack vendored |
| Maillage | `internal-linking-audit` | skill existant du dépôt |
| Humanisation | `humanizer` | skill existant du dépôt |
| Style global | `general-writing` | skill existant du dépôt |
| Audit de patterns génériques | `anti-ai-slop` | skill existant du dépôt |
| SEO on-page | `seo-onpage` | Rampstack / skill vendored |
| SEO technique | `seo-technical` | skill existant du dépôt |
| Contrôle de dérive si baseline | `seo-drift` | skill existant du dépôt |
| QA éditoriale | `editorial-qa` | skill existant du dépôt |

## Couche custom volontairement limitée

Le custom des workflows Guide est limité à cinq responsabilités :

1. router la page en `CHOICE`, `EXPLAINER`, `HOW_TO` ou hybride uniquement comme grille de risques ;
2. contrôler la frontière avec `/usages/`, `/comparatifs/` et `/marques/` ;
3. contrôler l'intégrité pédagogique propre au type de guide ;
4. calibrer la fraîcheur selon la stabilité du sujet ;
5. détecter le clonage structurel spécifique au cluster et mapper vers `KEEP / LIGHT_UPDATE / DEEP_REWRITE / MERGE / NOINDEX`.

Le custom ne réimplémente ni recherche keyword, ni fact-check, ni rédaction, ni SEO, ni humanisation, ni QA générale.

## Architecture finale

| Besoin utilisateur | Workflow |
|---|---|
| analyser une page Guide existante | `guide-analysis-workflow / AUDIT` |
| analyser l'ensemble du cluster | `guide-analysis-workflow / CLUSTER_AUDIT` |
| créer ou corriger un guide | `guide-content-workflow` |
| gate final après rédaction | `guide-analysis-workflow / PUBLISH_REVIEW` |

## Règle anti-industrialisation

Les références `choice-guide.md`, `explainer-guide.md` et `how-to-guide.md` sont désormais des grilles de questions. Elles ne peuvent imposer ni ordre de sections, ni nombre de H2/H3, ni tableau, FAQ, checklist ou nombre d'étapes.

Le plan final doit être produit après l'intention et les preuves via `content-brief-authoring`.

## Gate machine

`validate_guide_quality.py` ne mesure plus la qualité via :

- minimum de mots ;
- minimum de H2 ;
- minimum de liens ;
- minimum de sources ;
- minimum de prose autour d'un tableau.

Il contrôle uniquement des incohérences détectables automatiquement : structure HTML essentielle, placeholders, H1, title/meta, canonical, `noindex,follow`, IDs/ancres et liens internes cassés. La profondeur, la factualité et la qualité restent des gates du `PUBLISH_REVIEW`.

## Conclusion 80/20

La grande majorité des responsabilités méthodologiques est déléguée à des skills existants, dont plusieurs vendored directement depuis des repos publics comme Rampstack. La couche custom reste cantonnée au routing, aux frontières de catégorie et aux risques éditoriaux spécifiques au cluster Guide. Cela respecte l'objectif d'architecture `>=80% existing skills` sans chercher à transformer ce ratio en métrique artificielle de lignes de code.
