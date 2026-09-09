# Inventaire des skills — workflows comparatifs

Date : 9 septembre 2026

Scope : `/comparatifs/`

Objectif : garantir que `comparison-analysis-workflow` et `comparison-content-workflow` restent des orchestrateurs et que la méthode repose majoritairement sur des skills GitHub existants. La cible est **>= 80 % de méthodologie issue de skills existants**, avec une couche custom limitée à l'orchestration et aux règles spécifiques au cluster comparatifs de bloc-notes-numeriques.fr.

## Stack principale

| Étape | Skill local | Provenance | Statut | Rôle dans les comparatifs |
|---|---|---|---|---|
| Audit existant / cannibalisation | `seo-content-audit` | `rampstackco/claude-skills` | vendored + adapté | KEEP/UPDATE/MERGE/REDIRECT/DELETE, préservation de la valeur existante |
| Intent / cluster / SERP | `seo-keyword` | `rampstackco/claude-skills` | vendored + adapté | requête cible, intention, clustering, chevauchement |
| Contexte d'usage | `jobs-to-be-done` | `wondelai/skills` | adapté | circonstances, job réel, contraintes et alternatives |
| Preuves des reviews/buying guides | `evidence-based-reviews` | `rampstackco/claude-skills` | adapté | tiers de preuve, absence de faux hands-on, méthodologie honnête |
| Vérification des faits | `fact-check` | réutilisé du workflow de recovery existant | réutilisé | facts, prix, générations, compatibilités, statut des claims |
| Valeur affiliée | `affiliate-value` | réutilisé du workflow `italiaanse-percolator` | réutilisé | valeur originale, limites, alternatives, indépendance de la commission |
| Brief d'une page | `content-brief-authoring` | `rampstackco/claude-skills` | vendored + adapté | decision brief, scope, critères, preuves, angle, outline spécifique |
| Rédaction / édition | `content-and-copy` | `rampstackco/claude-skills` | vendored + adapté | hook, structure, voix, substance, closing |
| Humanisation | `humanizer` | skill GitHub externe, basé sur la taxonomie Wikipedia Signs of AI Writing | réutilisé | retirer les patterns artificiels sans inventer de faits |
| Édition finale | `general-writing` | `msimchowitz/writing-skills` | réutilisé | clarté, voix, concision, house-style |
| Détection de slop / templating | `anti-ai-slop` | skill GitHub externe déjà importé | réutilisé | structure générique, symétrie, artefact interchangeable |
| On-page SEO | `seo-onpage` | `rampstackco/claude-skills` | vendored + adapté | title, meta, H1, structure, liens, schema honnête |
| SEO technique | `seo-technical` | skill SEO externe déjà importé | réutilisé | canonical, robots, crawlabilité, structured data |
| QA éditoriale | `editorial-qa` | workflow de recovery existant | réutilisé | intention, originalité, factualité, naturel, utilité |

## Répartition réelle

La chaîne principale de production contient 14 briques spécialisées. Les étapes custom ne remplacent aucune de ces méthodes.

Custom conservé uniquement pour :

1. orchestrer les skills dans le bon ordre ;
2. vérifier que le scope/candidat est crédible pour la requête ;
3. vérifier que les critères existent avant la recommandation ;
4. vérifier que le verdict est explicable et conditionnel lorsque nécessaire ;
5. comparer la structure et le rôle des pages du cluster afin de détecter l'industrialisation.

Le custom ne doit pas imposer :

- un Product Universe exhaustif ;
- une Equivalence Engine formelle ;
- des hard gates sur toutes les pages ;
- un Total Solution Cost sur toutes les pages ;
- un scoring ;
- une pondération ;
- un ranking numérique ;
- un template éditorial.

Ces outils restent disponibles **uniquement lorsqu'ils améliorent la décision**.

## Corrections apportées après le premier test

Le premier `comparison-analysis-workflow` était trop custom et transformait plusieurs mécanismes optionnels en conditions quasi académiques de publication. Cela pouvait produire un `DEEP_REWRITE` simplement parce qu'un score éditorial n'était pas triangulé comme une mesure scientifique.

La version actuelle corrige ce biais :

- `evidence-based-reviews` détermine le niveau de preuve adapté au type de claim ;
- une spec officielle vérifie un fait mais pas une sensation d'usage ;
- un score éditorial, lorsqu'il existe, reste un jugement éditorial et n'est pas présenté comme une mesure ;
- le scoring est optionnel ;
- les poids sont optionnels ;
- les hard gates sont conditionnels ;
- le coût total n'est approfondi que s'il change réellement la décision ;
- `DEEP_REWRITE` est réservé aux problèmes structurants : mauvaise intention, sélection inadéquate, recommandation injustifiable, faible valeur, obsolescence majeure ou architecture industrialisée.

## Règle de maintenance

Avant d'ajouter une nouvelle logique custom à l'un des deux workflows :

1. vérifier si un skill local couvre déjà le besoin ;
2. vérifier sa provenance et sa fraîcheur ;
3. rechercher un skill GitHub amont plus complet si nécessaire ;
4. n'ajouter du custom que si la règle est réellement spécifique à `/comparatifs/` sur bloc-notes-numeriques.fr.

Les deux seuls workflows user-facing restent :

- `comparison-analysis-workflow` — diagnostiquer et décider ;
- `comparison-content-workflow` — produire ou corriger.
