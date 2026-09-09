# Inventaire des skills — workflows Usages

Date : 9 septembre 2026

Scope : `/usages/`

Objectif : garantir que `usage-analysis-workflow` et `usage-content-workflow` restent des **orchestrateurs** et que la méthode repose majoritairement sur des skills existants/vendored. Cible : **>= 80 % de méthodologie issue de skills réutilisés**, avec une couche custom <= 20 % limitée aux règles propres au rôle éditorial des pages `/usages/`.

## Les deux seuls workflows user-facing

- `usage-analysis-workflow` — diagnostiquer et décider avec `AUDIT`, `CLUSTER_AUDIT`, `PUBLISH_REVIEW` ;
- `usage-content-workflow` — produire ou corriger uniquement après décision d'analyse pour une page existante.

Le workflow de rédaction ne possède plus son propre publish gate et ne décide plus seul de l'ampleur d'une réécriture.

## Stack principale réutilisée

| Étape | Skill local | Provenance / réutilisation | Rôle dans `/usages/` |
|---|---|---|---|
| Audit de contenu | `seo-content-audit` / `content-audit` | `rampstackco/claude-skills` pour la brique SEO audit + skill partagé existant | KEEP/UPDATE/MERGE/REDIRECT/REMOVE, préservation de valeur |
| Keyword / intent / clustering | `seo-keyword` + `search-intent` | `rampstackco/claude-skills` pour `seo-keyword` + skill partagé existant | intention, cluster, rôle de l'URL, chevauchements |
| Job réel | `jobs-to-be-done` | `wondelai/skills` | circonstances, progrès, forces de changement, current hires |
| Refresh ciblé | `content-refresh` | skill partagé du stack éditorial existant | ampleur et nature d'une mise à jour |
| Vérification factuelle | `fact-check` | skill partagé du workflow recovery | capacités, compatibilités, facts instables, niveau de certitude |
| Expérience / review | `evidence-based-reviews` | `rampstackco/claude-skills` | uniquement pour claims expérientiels/jugements importants |
| Valeur affiliée | `affiliate-value` | skill partagé du workflow affiliate recovery | utilité sans commission, compromis, limites, alternatives |
| Brief | `content-brief-authoring` | `rampstackco/claude-skills` | transformer intent/JTBD/preuves en architecture bespoke |
| Rédaction | `content-and-copy` | `rampstackco/claude-skills` | structure, substance, rédaction |
| Maillage | `internal-linking-audit` | skill SEO partagé existant | prochaine étape logique, sans quota |
| Humanisation | `humanizer` | skill GitHub externe déjà importé | retirer patterns artificiels sans changer les faits |
| Édition finale | `general-writing` | `msimchowitz/writing-skills` | clarté, voix, concision |
| Anti-templating | `anti-ai-slop` | skill GitHub externe déjà importé | détecter prose générique et structures interchangeables |
| On-page | `seo-onpage` | `rampstackco/claude-skills` | title, meta, structure et on-page réellement applicable |
| SEO technique | `seo-technical` / `seo-best-practices` | skills SEO externes déjà vendored/réutilisés | canonical, robots, crawlabilité, données structurées |
| QA finale | `editorial-qa` | skill éditorial partagé existant | intention, originalité, factualité, naturel, utilité |

## Preuves de provenance présentes dans le repo

Plusieurs skills vendored portent directement leur upstream dans leur frontmatter. Exemples :

- `seo-content-audit` → `https://github.com/rampstackco/claude-skills/tree/main/skills/seo-content-audit` ;
- `seo-keyword` → `https://github.com/rampstackco/claude-skills/tree/main/skills/seo-keyword` ;
- `jobs-to-be-done` → `wondelai/skills` ;
- `content-brief-authoring`, `content-and-copy`, `evidence-based-reviews`, `seo-onpage` → stack Rampstack déjà vendored ;
- `general-writing` → `msimchowitz/writing-skills`.

Les autres briques listées sont réutilisées du stack commun du repo plutôt que recréées spécifiquement pour `/usages/`.

## Ce qui est réellement custom

La couche custom des workflows `/usages/` est limitée à cinq responsabilités :

1. **orchestration** des skills dans le bon ordre ;
2. **job-to-page fit** — vérifier qu'un job/circonstance justifie une URL autonome ;
3. **frontière de rôle** — distinguer usage, comparatif, guide et marque ;
4. **workflow → critères** — vérifier que les critères viennent de frictions réelles du job et non des specs disponibles ;
5. **cluster structure review** — détecter cannibalisation et architecture industrialisée entre pages usages.

Ces règles sont propres au site et ne remplacent aucun skill générique.

## Pourquoi la cible 80/20 est respectée

La chaîne utilise **17 briques spécialisées réutilisées** et ne crée qu'une couche d'orchestration + cinq contrôles de domaine. Aucun agent custom n'a été créé pour refaire :

- keyword research ;
- content audit ;
- JTBD ;
- fact-check ;
- evidence review ;
- content brief ;
- rédaction ;
- humanisation ;
- SEO ;
- internal linking ;
- QA éditoriale.

La proportion 80/20 doit être comprise comme une règle de **responsabilité méthodologique**, pas comme un faux score calculé sur le nombre de lignes de Markdown.

## Corrections apportées au workflow de rédaction

La version précédente était déjà solide sur le JTBD mais mélangeait pré-analyse, rédaction et validation finale. Elle proposait aussi une architecture éditoriale en dix blocs qui, répétée à l'échelle du cluster, pouvait devenir un template de production.

La version actuelle :

- exige `usage-analysis-workflow / AUDIT` avant correction d'une page existante ;
- réserve `KEEP` à l'absence de rédaction ;
- distingue `LIGHT_UPDATE` et `DEEP_REWRITE` ;
- préserve explicitement la valeur existante ;
- construit le plan via `content-brief-authoring` à partir du job et des preuves ;
- interdit une architecture fixe par type d'usage ;
- retourne vers `usage-analysis-workflow / PUBLISH_REVIEW` après production.

## Règle de maintenance

Avant d'ajouter une logique custom :

1. vérifier si un skill local couvre déjà le besoin ;
2. vérifier son upstream/provenance lorsque disponible ;
3. préférer enrichir/réutiliser un skill générique plutôt que créer un agent `/usages/` supplémentaire ;
4. n'ajouter du custom que si la règle est réellement spécifique au rôle des pages `/usages/` de bloc-notes-numeriques.fr.

Ne jamais ajouter au workflow :

- quotas de mots ;
- quotas de H2/H3 ;
- quotas de liens ;
- score artificiel de qualité ;
- plan fixe par usage ;
- nombre obligatoire d'étapes JTBD ;
- ranking produit ;
- deuxième copie des checklists des skills appelés.
