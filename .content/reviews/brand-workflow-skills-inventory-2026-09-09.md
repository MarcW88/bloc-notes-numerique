# Inventaire des skills et workflows — pages marques

Date : 9 septembre 2026  
Scope : `bloc-notes-numeriques.fr`, avec focus sur `/marques/`.

## Objectif

Réduire la complexité opérationnelle à **deux workflows brand visibles** :

1. `brand-content-workflow` pour créer ou réécrire ;
2. `brand-analysis-workflow` pour auditer, comparer le cluster et effectuer le gate final.

Les deux workflows doivent orchestrer majoritairement des skills déjà éprouvés dans d'autres dépôts GitHub. Les méthodes génériques ne doivent pas être recopiées dans les workflows brand.

## Principe de réutilisation

Pour les pages marques, les étapes substantielles sont déléguées à des skills existants : intention, audit, refresh, valeur affiliée, fact-check, preuves des reviews, maillage, édition, anti-slop et SEO.

La logique spécifique au site est limitée à :

- la frontière entre les types d'URLs `/marques/` ;
- la construction d'un plan propre à chaque URL à partir de l'intention et des preuves ;
- le contrôle inter-pages de similarité structurelle ;
- la décision finale `KEEP / LIGHT_UPDATE / DEEP_REWRITE / MERGE / NOINDEX` ;
- la sécurité `noindex,follow` avant validation humaine.

Sur cette base, plus de 80 % des étapes méthodologiques des workflows finaux reposent sur des skills existants ou adaptés de dépôts existants.

---

## Inventaire des skills existants avant nettoyage

| Skill / workflow | Provenance | Usage actuel | Décision |
|---|---|---|---|
| `academic-voice` | stack externe `msimchowitz/writing-skills` | sous-passe d'édition | KEEP ; utilisé indirectement via Humanizer |
| `affiliate-value` | hérité de `MarcW88/italiaanse-percolator` | valeur originale et intégrité affiliation | KEEP ; brique centrale brand et autres workflows |
| `anti-ai-slop` | upstream `ch040602/anti-ai-slop` | détection de sorties génériques/template-like | KEEP ; brique centrale des deux workflows brand |
| `better-usage` | stack externe `msimchowitz/writing-skills` | précision sémantique de la prose | KEEP ; utilisé indirectement via Humanizer |
| `brand-content-workflow` | custom bloc-notes-numeriques.fr | ancien workflow de production brand | REPLACE IN PLACE par le workflow final d'orchestration |
| `brand-editorial-publish-gate` | custom bloc-notes-numeriques.fr | ancien gate final brand | REMOVE ; absorbé par `brand-analysis-workflow` mode `PUBLISH_REVIEW` |
| `comparison-content-workflow` | workflow spécialisé du site | comparatifs | KEEP ; hors scope du nettoyage brand |
| `content-refresh` | hérité de `MarcW88/italiaanse-percolator` | niveau de récupération d'une page | KEEP ; appelé par brand-analysis/content et d'autres workflows |
| `deal-content-workflow` | workflow spécialisé du site | bons plans | KEEP ; hors scope brand |
| `editorial-qa` | hérité de `MarcW88/italiaanse-percolator` | QA finale générique | KEEP ; partagé entre plusieurs types de pages |
| `fact-check` | hérité de `MarcW88/italiaanse-percolator` | hiérarchie de sources et validation des claims | KEEP ; brique centrale brand et autres workflows |
| `general-writing` | upstream `msimchowitz/writing-skills` | édition finale, clarté, voix, anti-slop | KEEP ; brique centrale de finition brand |
| `guide-content-workflow` | workflow spécialisé du site | guides | KEEP ; hors scope brand |
| `humanizer` | stack externe `msimchowitz/writing-skills`, elle-même issue de travaux publics Humanizer | édition globale sans inventer de faits | KEEP ; brique centrale de finition brand |
| `internal-linking-audit` | hérité de `MarcW88/italiaanse-percolator` | maillage contextuel | KEEP ; partagé entre workflows |
| `jobs-to-be-done` | upstream `wondelai/skills/jobs-to-be-done`, adapté au site | pages `/usages/` | KEEP ; hors scope brand |
| `natural-writing` | hérité de `MarcW88/italiaanse-percolator`, spécifique NL | finition néerlandaise | KEEP pour compatibilité avec d'autres workflows ; RETIRÉ de la chaîne brand FR |
| `non-autoregressive-writing-pass` | stack externe `msimchowitz/writing-skills` | revue globale titres/transitions après draft | KEEP ; utilisé indirectement via Humanizer/general-writing |
| `search-intent` | hérité de `MarcW88/italiaanse-percolator` | intention, rôle URL, cannibalisation | KEEP ; brique centrale brand |
| `seo-best-practices` | skill externe, metadata `agent-skills` | SEO éditorial/technique général | KEEP ; n'utiliser que les règles applicables au site statique |
| `seo-drift` | skill externe ; implémentation inspirée de `claude-seo`/SE Ranking | comparaison baseline/régression | KEEP ; optionnel en brand, utile ailleurs |
| `seo-technical` | skill externe SEO technique stack-agnostic | crawl/index/schema/canonical | KEEP ; brique SEO brand et site-wide |
| `site-design-review` | workflow spécialisé du site + Playwright | audit design/visuel | KEEP ; hors scope brand |
| `trust-content-workflow` | workflow spécialisé du site | pages de confiance | KEEP ; hors scope brand |
| `usage-content-workflow` | workflow spécialisé du site | pages `/usages/` | KEEP ; hors scope brand |
| `writing-cadence` | stack externe `msimchowitz/writing-skills` | cadence/rythme de prose | KEEP ; utilisé indirectement via Humanizer |

---

## Skills ajoutés parce qu'ils existent déjà ailleurs et renforcent les workflows

### `content-audit`

Source : `MarcW88/italiaanse-percolator/.agents/skills/content-audit`.

Pourquoi : le skill sait déjà décider `KEEP / UPDATE / MERGE / REDIRECT / REMOVE` avant réécriture et signale explicitement merchant duplication, contenus template-like, pages dont seul le produit change, données obsolètes et faible valeur originale.

Adaptation : langue et exemples généralisés pour bloc-notes-numeriques.fr ; aucune logique de rédaction ajoutée.

### `evidence-based-reviews`

Upstream : `rampstackco/claude-skills/skills/evidence-based-reviews`, déjà réutilisé dans `MarcW88/italiaanse-percolator`.

Pourquoi : méthode mature pour les contenus affiliés sans faux test, avec quatre niveaux de preuve : specs fabricant, synthèse utilisateurs, triangulation experte, hands-on uniquement lorsqu'il existe réellement.

Adaptation : conservation de la discipline de preuve et de la transparence ; suppression des prescriptions juridiques spécifiques aux États-Unis qui ne constituent pas une base légale pour ce site français.

### `brand-analysis-workflow`

Nouveau workflow custom, mais **orchestrateur uniquement**. Il appelle les skills existants ci-dessus, ajoute le contrôle inter-pages propre au cluster marques et remplace l'ancien publish gate indépendant.

---

## Les deux workflows finaux

### 1. `brand-content-workflow`

Chaîne principale :

`brand-analysis/AUDIT → search-intent → content-audit/content-refresh → fact-check/evidence brief → evidence-based-reviews si pertinent → affiliate-value → plan spécifique → rédaction → fact-check → humanizer → general-writing → anti-ai-slop → internal-linking-audit → SEO → editorial-qa → brand-analysis/PUBLISH_REVIEW`

Les seuls blocs réellement custom sont le plan spécifique à l'URL, la persistance du contexte brand et le handoff final.

### 2. `brand-analysis-workflow`

Chaîne principale :

`content-audit → search-intent → content-refresh si UPDATE → affiliate-value → fact-check → evidence-based-reviews si pertinent → internal-linking-audit → anti-ai-slop → SEO → editorial-qa → contrôle structurel inter-pages → décision`

Le contrôle structurel inter-pages est custom parce qu'il répond à un problème propre au cluster : plusieurs pages individuellement correctes peuvent produire ensemble une empreinte éditoriale industrialisée.

---

## Ce qui est supprimé

### `brand-editorial-publish-gate`

Suppression justifiée :

- il est spécifique aux pages marques ;
- sa fonction est entièrement absorbée par `brand-analysis-workflow` en mode `PUBLISH_REVIEW` ;
- le conserver créerait un troisième workflow/gate brand à mémoriser ;
- les contrôles substantiels restent couverts via les skills existants + le nouveau contrôle inter-pages.

Aucun autre workflow de type de page n'est supprimé.

---

## Ce qui n'est volontairement pas supprimé

Même lorsqu'un skill n'est plus appelé directement par la nouvelle chaîne brand, il reste présent s'il est utilisé ou susceptible d'être utilisé par :

- `guide-content-workflow` ;
- `comparison-content-workflow` ;
- `usage-content-workflow` ;
- `deal-content-workflow` ;
- `trust-content-workflow` ;
- `site-design-review` ;
- d'autres tâches site-wide.

C'est notamment le cas de `natural-writing`, `seo-drift`, `jobs-to-be-done` et des sous-skills de la stack Humanizer.

---

## Règle de maintenance

À l'avenir, avant d'ajouter une nouvelle étape aux workflows brand :

1. vérifier si un skill existant du dépôt couvre déjà le besoin ;
2. rechercher l'upstream GitHub ou une brique mature avant de créer du custom ;
3. préférer adapter un skill spécialisé plutôt que dupliquer sa checklist dans le workflow ;
4. n'ajouter du custom que pour une contrainte réellement propre à bloc-notes-numeriques.fr ;
5. ne jamais transformer le type de page en template de rédaction.
