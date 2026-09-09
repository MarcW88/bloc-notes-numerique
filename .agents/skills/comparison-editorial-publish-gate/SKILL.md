---
name: comparison-editorial-publish-gate
description: Gate final pour les pages /comparatifs/. Il n'est pas dérivé du Brand gate : il audite, étape par étape, si la page et son classement peuvent réellement être justifiés par le comparison-content-workflow et par les artefacts qui l'ont produit.
---

# Comparison Workflow Evaluation Gate

## Rôle

Ce gate évalue la conformité d'un comparatif au **workflow Comparison réellement utilisé dans ce dépôt**.

Il ne demande pas seulement si le texte est agréable ou si le HTML est propre. Il demande :

> **Peut-on reconstruire et défendre la décision publiée en suivant le comparison-content-workflow, depuis l'intention jusqu'au ranking final ?**

Le référentiel principal est `.agents/skills/comparison-content-workflow/SKILL.md`.

Le `brand-editorial-publish-gate` ne doit pas servir de structure d'audit pour les comparatifs. Il peut inspirer le niveau de sévérité général, mais les phases, les preuves et les blockers ci-dessous viennent du workflow Comparison.

Un seul blocker méthodologique suffit à produire `FAIL` et `KEEP NOINDEX`.

---

# 0. Lire le pipeline réel avant l'évaluation

Pour chaque page, lire obligatoirement :

1. `.agents/skills/comparison-content-workflow/SKILL.md` ;
2. `comparison-workflow.config.yaml` ;
3. `comparison_products.py` — baseline produit partagée et scores disponibles ;
4. `comparison_pages.py` — intention, produits retenus, poids et ranking par page ;
5. `generate_comparison_metadata.py` — manière dont les données sont persistées ;
6. `.content/comparisons/<slug>.json` — snapshot méthodologique généré ;
7. `comparison_content.py` — transformation du ranking en contenu éditorial ;
8. `/comparatifs/<slug>/index.html` — résultat reçu par le lecteur ;
9. les pages proches `/comparatifs/`, `/usages/`, `/guides/` et `/marques/` si elles peuvent modifier l'intention ou la décision.

L'audit doit vérifier la cohérence **entre ces couches**, pas seulement la page HTML.

Si une information importante n'est pas persistée alors que le workflow exige qu'elle le soit, ne pas supposer que l'étape a eu lieu. Utiliser `UNPROVABLE`, ce qui vaut `FAIL` lorsqu'il s'agit d'une étape nécessaire au ranking.

Statuts d'étape :

- `PASS`
- `FAIL`
- `UNPROVABLE`
- `NOT_APPLICABLE`

---

# 1. Router le type de comparatif

Référence : sections 2 et 4 du `comparison-content-workflow`.

Identifier :

- `best_overall`
- `best_for_use_case`
- `budget`
- `feature_specific`
- `head_to_head`

Vérifier que `comparison_pages.py`, le JSON et le texte final décrivent le même type et le même job utilisateur.

PASS si la décision principale peut être formulée clairement et si les critères peuvent être reliés à cette décision.

FAIL si :

- la page spécialisée reprend essentiellement la logique d'un `best_overall` ;
- le job stocké ne correspond pas au verdict ;
- un `head_to_head` compare implicitement d'autres variantes ou générations que celles déclarées ;
- l'intention réelle est mieux satisfaite par une autre page existante.

Retour en cas d'échec : **workflow Comparison — Search intent / routing**.

---

# 2. Auditer le Product Universe

Référence : section 5.

Le workflow impose de construire l'univers avant de choisir les gagnants.

Évaluer :

- candidats évidents considérés ;
- génération exacte ;
- statut actuel ;
- disponibilité pertinente ;
- raison d'inclusion ;
- exclusions documentées ;
- absence d'influence de l'affiliation sur l'univers.

Dans l'implémentation actuelle, `comparison_pages.py` contient directement la liste `products`. Cela ne prouve pas à lui seul qu'un univers plus large a été étudié.

PASS si les candidats importants et les exclusions peuvent être reconstruits.

UNPROVABLE/FAIL si le fichier ne contient que les produits finalement classés et qu'aucune trace ne montre quels candidats ont été considérés puis exclus.

Retour : **workflow Comparison — Product Universe**.

---

# 3. Auditer l'Equivalence Engine

Référence : section 6.

Pour les candidats, déterminer si la comparaison est :

- `EXACT`
- `FUNCTIONALLY_COMPARABLE`
- `PARTIALLY_COMPARABLE`
- `NOT_COMPARABLE`

Vérifier que :

- la catégorie fonctionnelle est comparable pour le job ;
- les différences d'écosystème ne sont pas réduites à un simple score sans explication ;
- un produit ne reçoit pas un `0/10` pour une fonction hors de son rôle sans que cette non-comparabilité soit discutée ;
- bundles, accessoires et variantes ne créent pas une comparaison trompeuse.

Si aucune équivalence n'est persistée, cette étape est `UNPROVABLE` pour les comparatifs où la comparabilité n'est pas évidente.

Retour : **workflow Comparison — Equivalence Engine**.

---

# 4. Auditer l'Evidence Ledger

Référence : section 7.

Le workflow stipule : **aucune note avant le registre de preuves**.

Pour chaque différence qui influence un score important, retrouver :

- produit ;
- critère ;
- claim ou valeur factuelle ;
- source ;
- date ;
- classe de preuve.

Classes du workflow :

- `VERIFIED`
- `SUPPORTED`
- `INFERRED`
- `USER_PATTERN`
- `FIRST_HAND`
- `UNKNOWN`
- `PROHIBITED`

### Règle critique de l'implémentation actuelle

`generate_comparison_metadata.py` marque actuellement les notes comme `VERIFIED` tout en expliquant que le score numérique est une `editorial normalization`.

Une source officielle peut vérifier **le fait utilisé pour noter**. Elle ne vérifie pas automatiquement **la note 8/10 ou 9/10**.

Le gate doit donc séparer :

1. preuve du fait ;
2. règle ou raisonnement qui transforme ce fait en note.

FAIL si une note déterminante n'a qu'une justification générique du type :

> `Official capabilities reviewed ... numeric score is an editorial normalization ...`

FAIL si le registre ne permet pas d'expliquer pourquoi deux produits obtiennent des notes différentes sur un critère important.

Retour : **workflow Comparison — Evidence Ledger**, puis éventuellement `fact-check`.

---

# 5. Auditer les critères

Référence : section 8.

Pour chaque critère :

- lien explicite avec l'intention ;
- rôle réel dans la décision ;
- définition stable ;
- possibilité de comparer les candidats ;
- preuve disponible ;
- absence de doublon conceptuel avec un autre critère.

Les scores partagés dans `comparison_products.py` peuvent être réutilisés entre plusieurs pages seulement si le critère conserve le même sens.

FAIL si un critère change implicitement de définition selon la page tout en réutilisant la même note de baseline.

Retour : **workflow Comparison — critères avant classement**.

---

# 6. Auditer les pondérations

Référence : section 9.

Vérifier :

- somme = 100 ;
- poids adaptés au job ;
- différence réelle entre comparatif général et comparatif spécialisé ;
- aucune modification opportuniste pour faire gagner un produit ;
- justification possible avant de regarder le résultat.

### Sensibilité

Lorsque le #1 et le #2 sont proches, tester si une variation raisonnable des poids discutables inverse le résultat.

Si oui :

- le classement peut rester calculé ;
- mais le verdict doit devenir conditionnel ;
- la confiance doit baisser ;
- un langage de « gagnant clair » devient un blocker.

Retour : **workflow Comparison — Pondération**.

---

# 7. Auditer la normalisation et le scoring

Référence : section 10.

L'implémentation actuelle utilise des scores 0–10 stockés dans `comparison_products.py`, puis applique les poids de `comparison_pages.py`.

La moyenne pondérée attendue sur une échelle 0–10 est :

`total = Σ(score × poids) / 100`

Vérifier :

- toutes les notes nécessaires sont disponibles ;
- notes entre 0 et 10 ;
- score final recalculable ;
- ordre du ranking cohérent avec le calcul ;
- JSON cohérent avec `comparison_pages.py` ;
- HTML cohérent avec le ranking ;
- justification spécifique pour les notes qui font basculer le résultat ;
- distinction entre preuve factuelle et normalisation éditoriale ;
- niveau de confiance réduit lorsque la preuve est inférée ou incomplète.

FAIL si le ranking est seulement hardcodé sans pouvoir être reproduit depuis les données persistées.

FAIL si une différence de quelques centièmes est présentée comme une précision objective alors que la notation reste éditoriale.

Retour : **workflow Comparison — Normalisation et scoring**.

---

# 8. Auditer les Hard Gates

Référence : section 11.

Rechercher les contraintes éliminatoires propres à la requête :

- fonction indispensable absente ;
- incompatibilité ;
- produit obsolète ou indisponible ;
- budget maximal ;
- abonnement incompatible avec l'intention ;
- donnée essentielle non vérifiable.

Un hard gate doit être appliqué avant la moyenne.

Si le workflow exige un hard gate pertinent mais qu'aucune trace n'existe dans les données, `UNPROVABLE` = `FAIL`.

Retour : **workflow Comparison — Hard Gates**.

---

# 9. Auditer le Total Solution Cost

Référence : section 12.

Applicable lorsque le coût change la décision, notamment `budget`, `sans abonnement`, certains comparatifs étudiant/professionnel et toute comparaison de bundles différents.

Vérifier si nécessaire :

`TSC = appareil + accessoires indispensables + protection nécessaire + abonnement utile/obligatoire + autres coûts nécessaires`

FAIL si :

- un appareil nu est comparé à un bundle complet sans correction ;
- un accessoire indispensable disparaît du coût ;
- un abonnement obligatoire est traité comme optionnel ;
- la note `cost` ne peut pas être reliée à une configuration comparable.

Retour : **workflow Comparison — Total Solution Cost**.

---

# 10. Auditer le Rank Justification

Référence : section 13.

Pour chaque produit classé, vérifier que l'on peut expliquer :

- pourquoi il est présent ;
- pour qui il est recommandé ;
- pour qui il ne l'est pas ;
- avantage principal ;
- limitation principale ;
- critère qui déplace réellement la décision ;
- alternative logique ;
- raison de sa position.

Pour le #1, le texte doit expliquer ce qu'il gagne **et ce qu'il ne gagne pas**.

Une phrase qui répète uniquement les trois plus grosses notes n'est pas une justification suffisante si elle n'explique pas la différence avec le #2.

Pour un `head_to_head`, un verdict conditionnel peut être plus correct qu'un vainqueur universel.

Retour : **workflow Comparison — Rank Justification**.

---

# 11. Auditer l'Honest Comparison Standard

Référence : section 14.

Vérifier :

- défauts visibles du gagnant ;
- absence de cherry-picking ;
- distinction spec / conséquence d'usage ;
- distinction prix affiché / coût réel ;
- distinction desk research / test physique ;
- distinction fait / déduction / jugement ;
- données instables datées ;
- commission sans influence sur inclusion, score ou classement.

FAIL en cas de faux test, défaut majeur masqué, certitude non proportionnée aux preuves ou avantage comparatif non démontré.

Retour : **workflow Comparison — Honest Comparison Standard**.

---

# 12. Auditer l'architecture éditoriale et la rédaction produit

Référence : sections 15 et 16.

Ne pas imposer de quotas de mots, H2, tableaux ou liens.

Évaluer si le contenu rend le ranking compréhensible :

- verdict assez tôt ;
- critères réellement interprétés ;
- produit expliqué par ses arbitrages ;
- limites concrètes ;
- profil adapté / non adapté ;
- alternatives ;
- pas de blocs artificiellement symétriques si les différences exigent autre chose.

FAIL si le texte final peut être remplacé par une fiche constructeur + score sans perte significative de valeur décisionnelle.

Retour : **workflow Comparison — Architecture / rédaction**.

---

# 13. Auditer l'Affiliate Value

Référence : section 17.

Utiliser `affiliate-value`.

PASS si :

- la page reste utile sans liens affiliés ;
- commission absente des poids/scores/ranking ;
- défauts visibles ;
- produits non affiliés non pénalisés ;
- prix datés ;
- aucune fausse urgence ;
- disclosure cohérente avec la politique du site.

Retour : **workflow Comparison — Affiliate Value**.

---

# 14. Auditer le Fact-check

Référence : section 18.

Rejouer `fact-check` sur les faits qui influencent :

- scores ;
- hard gates ;
- coût ;
- ranking ;
- verdict.

Statuts utiles :

- `CONFIRMED`
- `PARTIAL`
- `UNVERIFIED`
- `CONTRADICTED`
- `OUTDATED`

FAIL si un fait déterminant est `UNVERIFIED`, `CONTRADICTED` ou `OUTDATED` sans effet explicite sur le score ou le verdict.

Retour : **Fact-check + Evidence Ledger**.

---

# 15. Auditer Search Intent QA et Internal Linking

Référence : sections 19 et 20.

Vérifier :

- ranking toujours aligné avec la requête après rédaction ;
- #1 compatible avec les hard gates ;
- absence de cannibalisation forte avec un comparatif voisin ;
- liens vers guides/usages/marques seulement lorsqu'ils aident la prochaine décision ;
- comparatif non transformé en impasse commerciale.

Retour : **Search Intent QA / Internal Linking**.

---

# 16. Auditer la finition, le SEO et le GEO

Référence : sections 21 à 23.

Exécuter ou réutiliser :

- `natural-writing`
- `humanizer`
- `general-writing`
- `anti-ai-slop`
- `seo-drift`
- `seo-best-practices`
- `seo-technical`
- `editorial-qa`

Le `seo-drift` doit aussi vérifier que le ranking n'a pas changé entre les données et le texte sans modification documentée des preuves, poids ou scores.

Pour GEO, vérifier surtout :

- verdict autonome mais conditionné par le besoin ;
- entités/modèles/générations explicites ;
- relation `produit → critère → conséquence → profil` claire ;
- sources identifiables ;
- distinction claire entre score éditorial et fait vérifié.

FAIL si la finition améliore la forme tout en masquant l'incertitude méthodologique.

Retour : **Finition / SEO / GEO**.

---

# 17. Auditer la persistance et la régénération

Cette étape est spécifique à **l'utilisation réelle du workflow dans ce repo**.

`generate_comparison_metadata.py` régénère `.content/comparisons/*.json` depuis `comparison_pages.py` et `comparison_products.py`.

Donc toute preuve, exclusion, hard gate, équivalence, coût total, justification ou niveau de confiance ajouté uniquement à la main dans le JSON peut être perdu au prochain run.

PASS seulement si les informations nécessaires à un ranking défendable sont stockées dans une source de vérité durable ou si le générateur sait les préserver.

FAIL si le rapport de méthode semble complet mais sera écrasé par la prochaine régénération.

Retour : **architecture de données du comparison-content-workflow**.

---

# 18. Publication

Référence : sections 24 à 28.

Le script `validate_comparisons.py` est un contrôle machine de cohérence. Il ne peut pas déclarer la méthodologie éditoriale valide.

Le gate humain doit terminer par :

- `PASS` seulement si toutes les phases nécessaires passent ;
- `FAIL` si une phase critique échoue ou est `UNPROVABLE` ;
- `KEEP NOINDEX` tant qu'un blocker existe ;
- `READY FOR HUMAN VALIDATION` seulement après résolution de tous les blockers.

Ne jamais retirer `noindex` automatiquement.

---

# Blockers absolus

- intention non alignée avec le ranking ;
- univers produit impossible à défendre ;
- candidat majeur omis sans justification ;
- comparabilité non traitée lorsqu'elle change la décision ;
- absence de preuve traçable pour un score déterminant ;
- score éditorial présenté comme `VERIFIED` sans distinguer le fait sous-jacent ;
- justification générique d'une note déterminante ;
- poids opportunistes ou non défendables ;
- score final non reproductible ;
- ranking non cohérent avec le calcul ;
- hard gate pertinent non appliqué ;
- coût réel trompeur pour une page où le budget est déterminant ;
- gagnant absolu alors que la sensibilité montre un résultat fragile ;
- fake test / fausse expérience ;
- commission ayant influencé inclusion, note ou ranking ;
- divergence entre données, JSON et HTML ;
- données méthodologiques essentielles non persistées durablement ;
- page indexable avant validation humaine explicite.

---

# Output obligatoire

Créer le rapport dans `.content/reviews/comparisons/<slug>.md` lorsque le dossier est utilisé.

```md
# Comparison workflow evaluation

URL: ...
Comparison type: ...
Status: PASS | FAIL
Publication: KEEP NOINDEX | READY FOR HUMAN VALIDATION

## Pipeline consistency
- comparison_products.py → comparison_pages.py: PASS | FAIL
- comparison_pages.py → JSON: PASS | FAIL
- JSON → HTML: PASS | FAIL
- regeneration durability: PASS | FAIL

## Workflow phases
- Routing & search intent: PASS | FAIL | UNPROVABLE
- Product universe: PASS | FAIL | UNPROVABLE
- Equivalence engine: PASS | FAIL | UNPROVABLE
- Evidence ledger: PASS | FAIL | UNPROVABLE
- Criteria: PASS | FAIL
- Weighting: PASS | FAIL
- Scoring: PASS | FAIL | UNPROVABLE
- Hard gates: PASS | FAIL | UNPROVABLE | NOT_APPLICABLE
- Total solution cost: PASS | FAIL | UNPROVABLE | NOT_APPLICABLE
- Rank justification: PASS | FAIL
- Honest comparison: PASS | FAIL
- Affiliate value: PASS | FAIL
- Fact-check: PASS | FAIL
- Search intent QA & linking: PASS | FAIL
- Writing / SEO / GEO: PASS | FAIL

## Blockers
1. [workflow step] ...

## Required corrections
1. Return to workflow step X: ...

## Residual risks
- ...

## Decision
KEEP NOINDEX | READY FOR HUMAN VALIDATION
```

Ne pas réécrire automatiquement toute la page après un `FAIL`. Revenir uniquement aux étapes du `comparison-content-workflow` responsables du blocker, mettre à jour les sources de vérité, régénérer, puis relancer l'évaluation complète.
