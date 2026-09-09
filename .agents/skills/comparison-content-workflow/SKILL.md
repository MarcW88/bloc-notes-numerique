---
name: comparison-content-workflow
description: Workflow unique de création et de réécriture des pages /comparatifs/ de bloc-notes-numeriques.fr. Orchestre majoritairement des skills GitHub existants et conserve une méthodologie comparative auditable : intention, univers produit, équivalence, preuves, critères, hard gates, scoring, ranking, rédaction, fact-check et QA. La structure éditoriale doit découler de la décision utilisateur et de la méthode, jamais d'un template de comparatif.
metadata:
  adapted_for: bloc-notes-numeriques.fr
  orchestration_target: ">=80% existing skills"
---

# Comparison Content Workflow

## Rôle

C'est le **seul workflow de production** à utiliser pour créer ou réécrire une URL sous `/comparatifs/`.

Il orchestre des skills existants plutôt que de réimplémenter leur méthode. La logique custom est limitée à ce qui est propre aux comparatifs : univers produit, équivalence, critères, pondération, hard gates, coût total, scoring et ranking.

Principe central :

> **Intention avant univers produit. Preuves avant scoring. Critères avant gagnant. Méthode avant rédaction.**

La page finale doit aider à prendre une décision et rester utile sans liens affiliés.

---

# 1. Entrées obligatoires

Lire :

- `AGENTS.md` ;
- `comparison-workflow.config.yaml` ;
- page cible et contenu existant ;
- `.content/comparisons/<slug>.json` ;
- comparatifs voisins ;
- pages marques, produits, usages et guides pertinentes ;
- données GSC/sémantiques/historiques disponibles ;
- sources actuelles nécessaires à la vérification.

Pour une page existante, commencer obligatoirement par :

`.agents/skills/comparison-analysis-workflow/SKILL.md` en mode `AUDIT`.

Ne pas lancer une réécriture profonde si l'audit conclut `KEEP`, `LIGHT_UPDATE`, `MERGE` ou `NOINDEX` sans raison documentée de changer cette décision.

---

# 2. Chaîne de production fondée sur les skills existants

## 2.1 Intention — `search-intent`

Déterminer requête/topic principal, intention, décision concrète, sous-intentions, contrainte dominante, rôle de l'URL et risque de cannibalisation.

Lorsque des données historiques existent, les utiliser avant d'inférer la cible.

## 2.2 Job-to-be-done — `jobs-to-be-done`

Obligatoire pour les comparatifs orientés contexte ou profil d'usage : étudiant, professionnel, annotation PDF, mobilité, etc.

Les critères doivent partir du travail à accomplir et des contraintes réelles, pas d'un persona décoratif.

## 2.3 Audit/récupération — `content-audit` + `content-refresh`

Pour une page existante :

- préserver les éléments encore utiles ;
- conserver un ranking uniquement s'il résiste à la nouvelle méthode ;
- distinguer correction légère et reconstruction ;
- ne jamais conserver un gagnant simplement parce qu'il était déjà #1.

Pour une nouvelle page : `N/A`.

## 2.4 Recherche et evidence brief — `fact-check`

Construire un registre des affirmations nécessaires avant scoring ou rédaction.

Hiérarchie par défaut : fabricant/support/manuel, distributeur officiel, retailer fiable pour prix ou disponibilité, tests indépendants, puis patterns utilisateurs suffisamment documentés.

Statuts : `VERIFIED`, `SUPPORTED`, `INFERRED`, `USER_PATTERN`, `FIRST_HAND`, `UNKNOWN`, `OUTDATED`, `CONTRADICTED`.

Ne jamais utiliser la mémoire du modèle pour combler `UNKNOWN`.

## 2.5 Jugements d'usage — `evidence-based-reviews`

Obligatoire dès qu'un critère porte sur qualité d'écriture, ergonomie, fluidité, autonomie observée, fiabilité ou autre jugement d'expérience.

Une sensation issue d'un test tiers reste une synthèse externe. Elle ne devient jamais un hands-on propre au site.

## 2.6 Valeur originale — `affiliate-value`

Vérifier avant le ranking :

- critères réellement décisionnels ;
- défauts visibles ;
- alternatives honnêtes ;
- coût réel ;
- absence d'influence des commissions ;
- page utile sans liens affiliés.

---

# 3. Méthodologie comparative

Cette partie est spécifique au workflow comparatif. Elle doit être exécutée **avant** le plan éditorial et la rédaction.

## 3.1 Type méthodologique

Déterminer un type dominant :

- `BEST_OVERALL`
- `USE_CASE`
- `BUDGET`
- `FEATURE_SPECIFIC`
- `HEAD_TO_HEAD`

Le type définit les risques, le périmètre et la méthode. **Il ne définit pas l'architecture éditoriale.**

## 3.2 Product Universe

Lister les candidats pertinents avant le gagnant. Pour chaque produit : modèle, génération, statut, disponibilité, configuration utile, prix si pertinent, accessoires obligatoires, abonnement, fonctions clés et sources.

Statuts possibles : `ELIGIBLE`, `CONDITIONALLY_ELIGIBLE`, `OUTDATED`, `NOT_COMPARABLE`, `EXCLUDED`.

Toute exclusion doit être documentée.

## 3.3 Equivalence Engine

Évaluer la comparabilité selon job-to-be-done, taille/capacité, workflow, fonctions clés, logiciel, accessoires, coûts récurrents et contraintes.

Statuts : `EXACT`, `FUNCTIONALLY_COMPARABLE`, `PARTIALLY_COMPARABLE`, `NOT_COMPARABLE`.

Une comparaison partielle doit expliciter ce qui ne l'est pas.

## 3.4 Critères avant classement

Construire les critères depuis l'intention, le JTBD, les différences réelles et les preuves disponibles.

Un critère doit être pertinent, comparable et suffisamment étayé. Ne pas ajouter un critère uniquement pour différencier artificiellement des produits.

## 3.5 Pondération

Définir les poids avant calcul. Si une pondération est utilisée, la somme = 100.

Interdit : ajuster les poids après avoir vu le gagnant, sauf correction méthodologique explicitement documentée.

## 3.6 Hard Gates

Documenter les contraintes éliminatoires : fonction indispensable absente, incompatibilité, génération obsolète, prix hors contrainte, disponibilité insuffisante, abonnement obligatoire incompatible, etc.

Un produit qui échoue un hard gate ne gagne pas grâce à une moyenne élevée.

## 3.7 Total Solution Cost

Lorsque le coût change la décision :

`TSC = appareil + accessoire nécessaire + abonnement utile + autres coûts indispensables`

Ne pas comparer un appareil nu à un bundle complet sans normalisation ou avertissement.

## 3.8 Scoring

Si un scoring est pertinent, utiliser une échelle stable et conserver pour chaque note : valeur, justification, niveau de preuve et incertitude éventuelle.

Aucun score important ne doit reposer sur `UNKNOWN`.

Le scoring est un outil d'aide à la décision, pas une façade de précision mathématique.

## 3.9 Ranking et justification

Pour chaque produit classé : expliquer pourquoi il est là, pour qui, limite principale, critère qui change la décision, alternative logique et raison de sa position.

Pour le #1, expliquer aussi ce qu'il ne gagne pas.

Un `HEAD_TO_HEAD` peut aboutir à un verdict conditionnel plutôt qu'à un « gagnant absolu » si l'intention le justifie.

---

# 4. Construction libre mais justifiée du plan

Le plan est construit **après** intention, preuves et méthode comparative.

Pour chaque section proposée, pouvoir répondre :

1. quelle question ou décision cette section résout-elle ?
2. quelles preuves ou données la soutiennent ?
3. quel élément de la méthode ou du ranking explique sa présence ?
4. pourquoi mérite-t-elle une section autonome ?

Si ces réponses sont faibles, supprimer ou fusionner la section.

## Interdiction de template par type de comparatif

Il est interdit d'imposer :

- un nombre fixe de H2/H3 ;
- un ordre standard `verdict → tableau → produit 1 → produit 2 → méthode → FAQ` ;
- une fiche produit symétrique obligatoire ;
- un tableau obligatoire ;
- une FAQ automatique ;
- une conclusion automatique ;
- un minimum de mots ou de liens.

Deux `BEST_OVERALL` ou deux `HEAD_TO_HEAD` peuvent avoir des architectures différentes lorsque les décisions et preuves diffèrent.

---

# 5. Rédaction depuis les preuves et la méthode

Le draft doit rester dans les limites de l'evidence brief et de la méthodologie persistée.

Règles :

- chaque claim important doit être traçable ;
- les scores doivent être expliqués par des faits ou jugements documentés ;
- afficher les limites du gagnant aussi clairement que ses avantages ;
- distinguer différence de spec et différence d'usage ;
- distinguer prix affiché et coût total ;
- ne pas simuler de test physique ;
- ne pas transformer une inférence éditoriale en fait ;
- ne pas adapter le verdict à la commission ;
- ne pas écrire une section uniquement pour placer un mot-clé, un produit ou un CTA.

La prose finale ne parle pas de SEO, GEO, maillage, intention, page type ou stratégie éditoriale.

---

# 6. Fact-check post-draft — `fact-check`

Après rédaction :

1. réextraire les claims vérifiables ;
2. comparer avec l'evidence brief ;
3. vérifier les comparatifs (« plus léger », « moins cher », « plus ouvert », etc.) ;
4. qualifier ou supprimer `UNKNOWN` ;
5. corriger `OUTDATED` et `CONTRADICTED` ;
6. vérifier que les prix et disponibilités sont datés ;
7. s'assurer qu'aucun test tiers n'est devenu une expérience propre.

---

# 7. Revalidation du ranking

Après rédaction, recalculer ou revérifier la logique de classement à partir des données persistées.

Blocker si :

- la prose affirme un gagnant différent du ranking sans justification ;
- le ranking a changé sans changement documenté de données, critères, poids ou hard gate ;
- un produit exclu devient recommandé dans le texte ;
- le verdict final contredit les limites ou scénarios présentés.

Utiliser `seo-drift` lorsqu'un baseline avant/après est disponible pour contrôler aussi la dérive de critères, poids, scores et ranking.

---

# 8. Finition éditoriale — stack externe

Utiliser dans cet ordre :

1. `humanizer` ;
2. `general-writing` ;
3. `anti-ai-slop`.

Pour les pages françaises, `natural-writing` n'est pas une étape obligatoire car le skill présent est spécifique au néerlandais.

La finition peut modifier la structure et le rythme mais ne peut ajouter aucun fait ou modifier le ranking sans preuve.

Contrôler particulièrement :

- blocs produits artificiellement symétriques ;
- mêmes avantages/limites sur toutes les fiches ;
- rule of three systématique ;
- verdicts génériques ;
- transitions recyclées ;
- conclusion qui répète le classement sans apporter de décision ;
- structure interchangeable avec un autre comparatif.

---

# 9. Maillage — `internal-linking-audit`

Ajouter uniquement les liens qui servent une prochaine question : marque, produit, usage, guide, service, prix, technologie, autre comparatif.

Aucun quota.

---

# 10. SEO / GEO

Utiliser `seo-technical` et `seo-best-practices` pour les règles applicables.

Vérifier title, H1, intention, canonical, robots, entités, structured data honnête, tableaux contextualisés, relations explicites produit → usage et méthodologie résumable.

Aucun nombre de mots, headings, tableaux ou liens n'est un KPI de qualité.

---

# 11. QA générique — `editorial-qa`

La page doit passer intention, valeur originale, factualité, naturel, SEO et utilité sans affiliation.

Un comparatif peut être factuellement correct et quand même échouer si son ranking n'aide pas réellement à décider.

---

# 12. Gate final — `comparison-analysis-workflow` / `PUBLISH_REVIEW`

Une fois le draft stable, appeler :

`.agents/skills/comparison-analysis-workflow/SKILL.md` en mode `PUBLISH_REVIEW`.

Cette étape :

- exécute `python3 validate_comparisons.py` ;
- recontrôle intention, preuves, univers, équivalence, critères, hard gates, scoring et ranking ;
- compare la structure aux comparatifs voisins ;
- cherche l'industrialisation éditoriale et méthodologique.

Résultat attendu avant validation humaine :

`PASS — READY_FOR_HUMAN_VALIDATION`

Sinon :

`FAIL — KEEP_NOINDEX`

---

# 13. Persistance

`.content/comparisons/<slug>.json` doit rester la source de vérité méthodologique et conserver, selon pertinence :

- intent/JTBD ;
- product universe et exclusions ;
- équivalence ;
- evidence ledger ;
- critères et poids ;
- hard gates ;
- Total Solution Cost ;
- scores et justifications ;
- ranking ;
- niveau de confiance ;
- date de recherche ;
- statut.

Le texte final ne doit jamais être le seul endroit où le ranking est expliqué.

---

# 14. Indexation

Par défaut, conserver `noindex,follow`.

Le workflow n'est jamais autorisé à retirer `noindex` automatiquement.

Conditions cumulatives :

1. `validate_comparisons.py` sans blocker ;
2. `comparison-analysis-workflow / PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` ;
3. validation humaine explicite ;
4. instruction explicite de rendre la page indexable.

---

# 15. Résumé de l'orchestration

```text
PAGE EXISTANTE
  comparison-analysis-workflow / AUDIT
        ↓
search-intent + jobs-to-be-done si pertinent
        ↓
content-audit + content-refresh
        ↓
fact-check → evidence brief
        ↓
evidence-based-reviews pour jugements d'usage
        ↓
affiliate-value
        ↓
product universe → equivalence → critères → hard gates
        ↓
pondération → TSC → scoring → ranking
        ↓
PLAN SPÉCIFIQUE À LA DÉCISION
        ↓
rédaction depuis preuves et méthode
        ↓
fact-check + revalidation ranking
        ↓
humanizer → general-writing → anti-ai-slop
        ↓
internal-linking-audit → SEO/GEO → editorial-qa
        ↓
comparison-analysis-workflow / PUBLISH_REVIEW
        ↓
validation humaine
```

Le workflow orchestre ; il ne remplace pas ses skills spécialisés.
