---
name: comparison-editorial-publish-gate
description: Gate final sévère pour les pages /comparatifs/. Il audite si la décision, le ranking et l'architecture éditoriale peuvent réellement être reconstruits et défendus depuis le comparison-content-workflow. Il refuse les rankings fragiles, les preuves insuffisantes et les structures de pages clonées sans justification.
---

# Comparison Workflow Evaluation Gate

## Rôle

Ce gate évalue un comparatif contre **le `comparison-content-workflow` réellement utilisé dans ce dépôt**.

Question centrale :

> **Peut-on reconstruire et défendre la décision publiée, depuis l'intention jusqu'au ranking et jusqu'au choix de la structure éditoriale ?**

Le référentiel principal est `.agents/skills/comparison-content-workflow/SKILL.md`.

Le Brand gate peut inspirer le niveau de sévérité, jamais la structure de l'audit.

Un blocker méthodologique ou éditorial critique suffit à produire :

- `FAIL`
- `KEEP NOINDEX`

Le gate ne retire jamais `noindex` automatiquement.

---

# 0. Lire le pipeline réel

Lire obligatoirement :

1. `.agents/skills/comparison-content-workflow/SKILL.md` ;
2. `comparison-workflow.config.yaml` ;
3. `comparison_products.py` ;
4. `comparison_pages.py` ;
5. `comparison_methodology.py` ou toute source méthodologique page-spécifique ;
6. `generate_comparison_metadata.py` ;
7. `.content/comparisons/<slug>.json` ;
8. `comparison_content.py` et tout override page-spécifique ;
9. `/comparatifs/<slug>/index.html` ;
10. les comparatifs voisins pertinents ;
11. les pages `/usages/`, `/guides/` et `/marques/` qui peuvent modifier l'interprétation.

L'audit porte sur la cohérence **entre ces couches**, pas seulement sur le HTML.

Statuts d'étape :

- `PASS`
- `FAIL`
- `UNPROVABLE`
- `NOT_APPLICABLE`

Une étape critique `UNPROVABLE` vaut `FAIL`.

---

# 1. Routing & search intent

Vérifier :
- type réel du comparatif ;
- requête et job utilisateur ;
- sous-intentions ;
- contrainte principale ;
- absence de cannibalisation forte avec une autre page.

FAIL si la page spécialisée reprend essentiellement la logique d'un comparatif général ou si le verdict ne répond pas au job stocké.

Retour : **Search intent / routing**.

---

# 2. Product Universe

Vérifier que l'univers a été construit avant le gagnant :
- candidats évidents considérés ;
- génération exacte ;
- statut et disponibilité ;
- raisons d'inclusion ;
- exclusions documentées ;
- affiliation sans influence sur l'univers.

FAIL/UNPROVABLE si seuls les produits finalement classés sont visibles et qu'aucune trace ne montre les candidats réellement considérés puis exclus.

Retour : **Product Universe**.

---

# 3. Equivalence Engine

Pour chaque candidat, retrouver :
- `EXACT`
- `FUNCTIONALLY_COMPARABLE`
- `PARTIALLY_COMPARABLE`
- `NOT_COMPARABLE`

Vérifier catégorie fonctionnelle, workflow, accessoires, logiciel, coûts récurrents et contraintes.

FAIL si une différence de philosophie produit est aplatie en simple score sans traitement de la comparabilité.

Retour : **Equivalence Engine**.

---

# 4. Evidence Ledger

Pour chaque différence qui influence une note importante, retrouver :
- produit ;
- critère ;
- claim factuel ;
- valeur ;
- source ;
- date ;
- classe de preuve.

Classes : `VERIFIED`, `SUPPORTED`, `INFERRED`, `USER_PATTERN`, `FIRST_HAND`, `UNKNOWN`, `PROHIBITED`.

Règle absolue : une source officielle peut vérifier **le fait**, pas automatiquement **la note 8/10**.

FAIL si :
- un score déterminant n'a pas de preuves référencées ;
- fait et note sont confondus ;
- une justification générique remplace le raisonnement ;
- deux produits ont des notes différentes sans différence factuelle explicable.

Retour : **Evidence Ledger + Fact-check**.

---

# 5. Critères

Pour chaque critère :
- lien explicite avec l'intention ;
- définition stable ;
- rôle réel dans la décision ;
- comparabilité ;
- preuve disponible ;
- absence de doublon conceptuel.

FAIL si une baseline partagée change implicitement de sens selon la page.

Retour : **Critères avant classement**.

---

# 6. Pondérations

Vérifier :
- somme = 100 ;
- poids défendables avant résultat ;
- adaptation réelle au job ;
- aucun ajustement opportuniste pour conserver un gagnant.

Lorsque le top 2 est proche, appliquer la sensibilité prévue par le workflow.

Si une variation raisonnable inverse le #1 :
- le ranking calculé peut rester ;
- la confiance doit baisser ;
- le verdict doit devenir conditionnel.

FAIL si un gagnant clair est affirmé malgré un résultat sensible.

Retour : **Pondération / Sensitivity**.

---

# 7. Normalisation & scoring

Formule attendue sur une échelle 0–10 :

`total = Σ(score × poids) / 100`

Vérifier :
- notes 0–10 ;
- evidence refs ;
- justification spécifique ;
- score final recalculable ;
- ranking cohérent ;
- JSON cohérent avec les sources ;
- HTML cohérent avec le JSON ;
- niveau de confiance proportionné aux preuves.

FAIL si la précision numérique dépasse la précision réelle des données.

Retour : **Normalisation / Scoring**.

---

# 8. Hard Gates

Rechercher les contraintes éliminatoires propres à la requête :
- fonction indispensable ;
- incompatibilité ;
- disponibilité ;
- budget maximal ;
- abonnement ;
- politique IT / sécurité ;
- donnée essentielle non vérifiable.

Un produit qui échoue un hard gate ne doit pas gagner par moyenne.

Retour : **Hard Gates**.

---

# 9. Total Solution Cost

Lorsque pertinent, vérifier :

`TSC = appareil + accessoires indispensables + protection nécessaire + abonnement utile/obligatoire + autres coûts nécessaires`

FAIL si des configurations non équivalentes sont présentées comme comparables ou si une précision de prix artificielle masque taxes, import, bundle ou abonnement.

Retour : **Total Solution Cost**.

---

# 10. Rank Justification

Pour chaque produit classé, vérifier :
- pourquoi il est présent ;
- pour qui il est pertinent ;
- pour qui il ne l'est pas ;
- avantage décisif ;
- limite décisive ;
- alternative logique ;
- raison de sa position.

Pour le #1 : expliquer ce qu'il gagne **et ce qu'il ne gagne pas**.

FAIL si la justification répète seulement les trois plus grosses notes.

Retour : **Rank Justification**.

---

# 11. Honest Comparison Standard

Vérifier :
- défauts visibles du gagnant ;
- absence de cherry-picking ;
- distinction spec / conséquence ;
- prix affiché / coût réel ;
- desk research / test physique ;
- fait / déduction / jugement ;
- données instables datées ;
- commission sans influence.

FAIL en cas de faux test, certitude disproportionnée ou défaut majeur masqué.

Retour : **Honest Comparison**.

---

# 12. Editorial Thesis

Référence : `comparison-content-workflow`, étape **Définir la thèse éditoriale avant le plan**.

Rechercher dans les données persistées :
- `editorial_thesis` ;
- `decision_tensions` ;
- `must_tell` ;
- `can_omit`.

Puis vérifier que la page raconte effectivement cette thèse.

PASS si le comparatif possède une idée éditoriale spécifique qui explique ce que le lecteur doit comprendre au-delà du tableau de scores.

FAIL si :
- aucune thèse spécifique n'est identifiable ;
- la thèse pourrait être copiée sur plusieurs autres comparatifs en changeant seulement les noms ;
- la page ajoute du volume pour masquer l'absence d'enseignement éditorial ;
- le texte raconte principalement la mécanique du scoring au lieu de la décision.

Retour : **Editorial Thesis**.

---

# 13. Architecture éditoriale adaptative

Référence : `comparison-content-workflow`, étape **Architecture éditoriale adaptative — aucun template obligatoire**.

Le gate ne vérifie PAS la présence d'une liste fixe de sections.

Il doit au contraire demander :

> **Pourquoi cette page a-t-elle cette structure précise ?**

Rechercher `architecture_rationale` dans la source durable.

Comparer ensuite la page à plusieurs comparatifs voisins pertinents.

### PASS si

- l'ordre des blocs suit le vrai chemin de décision ;
- les sections existent parce qu'elles servent la thèse ;
- la longueur des blocs suit l'importance éditoriale ;
- les produits peuvent être traités de manière asymétrique ;
- certains blocs standards sont omis lorsqu'ils n'apportent rien ;
- un tableau synthétise sans être paraphrasé ligne par ligne ;
- une structure similaire à une page voisine est explicitement justifiable par une logique décisionnelle similaire.

### FAIL si

- le plan est manifestement cloné d'une autre page ;
- plusieurs pages suivent automatiquement `méthode → critères → classement → produit 1 → produit 2 → profils → coût → limites → sources` ;
- les mêmes H2 reviennent cluster-wide sans nécessité sémantique ;
- chaque produit reçoit le même nombre de paragraphes et les mêmes sous-parties par symétrie ;
- un bloc existe seulement parce que le générateur sait le produire ;
- la page pourrait être recréée en remplaçant les noms, scores, avantages et limites dans un gabarit commun ;
- la méthodologie prend plus de place que l'interprétation sans raison ;
- une section vide de valeur est conservée pour atteindre une longueur, un nombre de H2 ou une structure attendue.

### Important

La diversité éditoriale ne signifie pas variation décorative.

Ne jamais forcer une structure différente uniquement pour "faire différent". Si deux comparatifs ont réellement la même logique décisionnelle, une structure proche peut être correcte — mais le rapport doit expliquer pourquoi.

Retour : **Architecture éditoriale**.

---

# 14. Rédaction et valeur décisionnelle

Évaluer :
- interprétation réelle des preuves ;
- arbitrages concrets ;
- limites ;
- alternatives ;
- profil adapté / non adapté seulement lorsqu'utile ;
- absence de fiche constructeur reformulée ;
- absence de blocs artificiellement symétriques.

FAIL si le texte final peut être remplacé par une fiche constructeur + score sans perte significative de valeur décisionnelle.

Retour : **Rédaction / valeur décisionnelle**.

---

# 15. Affiliate Value

Utiliser `affiliate-value`.

PASS si :
- page utile sans liens affiliés ;
- commission absente de l'univers, des poids, scores et ranking ;
- défauts visibles ;
- produits non affiliés non pénalisés ;
- prix datés ;
- aucune fausse urgence ;
- disclosure cohérente.

Retour : **Affiliate Value**.

---

# 16. Fact-check

Rejouer `fact-check` sur les faits qui influencent :
- score ;
- hard gate ;
- coût ;
- ranking ;
- verdict.

FAIL si un fait déterminant est `UNVERIFIED`, `CONTRADICTED` ou `OUTDATED` sans effet explicite sur le verdict.

Retour : **Fact-check**.

---

# 17. Search Intent QA & Internal Linking

Vérifier :
- ranking toujours aligné ;
- #1 compatible avec hard gates ;
- pas de cannibalisation forte ;
- liens uniquement lorsqu'ils aident la prochaine décision ;
- aucun quota de liens ;
- structure non déformée pour placer des liens internes.

Retour : **Search Intent QA / Internal Linking**.

---

# 18. Finition, SEO & GEO

Exécuter/réutiliser :
- `natural-writing`
- `humanizer`
- `general-writing`
- `anti-ai-slop`
- `seo-drift`
- `seo-best-practices`
- `seo-technical`
- `editorial-qa`

Le SEO ne doit jamais imposer un template de H2 cluster-wide.

Le `seo-drift` doit vérifier :
- données → ranking ;
- ranking → texte ;
- `editorial_thesis` → architecture ;
- absence de normalisation progressive des pages vers une même structure.

Pour GEO : relations explicites `produit → critère → conséquence → profil`, sources identifiables et verdict proportionné à la confiance.

Retour : **Finition / SEO / GEO**.

---

# 19. Persistance & régénération

Toute donnée nécessaire au ranking ou à l'architecture éditoriale doit survivre à la régénération.

PASS seulement si la source durable conserve, selon pertinence :
- univers / exclusions ;
- équivalence ;
- evidence ledger ;
- hard gates ;
- TSC ;
- scores ;
- sensitivity / confidence ;
- rank justification ;
- `editorial_thesis` ;
- `decision_tensions` ;
- `architecture_rationale` ;
- `must_tell` ;
- `can_omit`.

FAIL si une future régénération peut écraser la méthodologie ou remettre un template générique.

Retour : **Architecture de données / régénération**.

---

# 20. Publication

Le contrôle machine prouve seulement la cohérence détectable automatiquement.

Le gate humain termine par :
- `PASS` seulement si toutes les phases nécessaires passent ;
- `FAIL` si une phase critique échoue ou est `UNPROVABLE` ;
- `KEEP NOINDEX` tant qu'un blocker existe ;
- `READY FOR HUMAN VALIDATION` seulement après résolution de tous les blockers.

Ne jamais retirer `noindex` automatiquement.

---

# Blockers absolus

- intention non alignée ;
- univers impossible à défendre ;
- candidat majeur omis sans justification ;
- comparabilité non traitée ;
- score déterminant sans preuve traçable ;
- fait vérifié confondu avec score éditorial ;
- poids opportunistes ;
- score non reproductible ;
- hard gate ignoré ;
- coût réel trompeur ;
- gagnant absolu malgré sensibilité forte ;
- faux test ;
- commission influençant inclusion/note/ranking ;
- divergence données / JSON / HTML ;
- données méthodologiques non persistées ;
- absence de thèse éditoriale sur une page substantielle ;
- structure clonée d'un comparatif voisin sans justification ;
- symétrie de blocs imposée par générateur ;
- quota de mots/H2/tableaux/liens utilisé comme critère de qualité ;
- page indexable avant validation humaine explicite.

---

# Output obligatoire

Créer le rapport dans `.content/reviews/comparisons/<slug>.md`.

```md
# Comparison workflow evaluation

URL: ...
Comparison type: ...
Status: PASS | FAIL
Publication: KEEP NOINDEX | READY FOR HUMAN VALIDATION

## Pipeline consistency
- sources → JSON: PASS | FAIL
- JSON → HTML: PASS | FAIL
- regeneration durability: PASS | FAIL

## Methodology
- Routing & search intent: PASS | FAIL | UNPROVABLE
- Product universe: PASS | FAIL | UNPROVABLE
- Equivalence engine: PASS | FAIL | UNPROVABLE
- Evidence ledger: PASS | FAIL | UNPROVABLE
- Criteria: PASS | FAIL
- Weighting & sensitivity: PASS | FAIL
- Scoring: PASS | FAIL | UNPROVABLE
- Hard gates: PASS | FAIL | UNPROVABLE | NOT_APPLICABLE
- Total solution cost: PASS | FAIL | UNPROVABLE | NOT_APPLICABLE
- Rank justification: PASS | FAIL
- Honest comparison: PASS | FAIL

## Editorial strategy
- Editorial thesis: PASS | FAIL | UNPROVABLE
- Adaptive architecture: PASS | FAIL
- Decision value / writing: PASS | FAIL
- Neighbour-page structural comparison: PASS | FAIL

## QA
- Affiliate value: PASS | FAIL
- Fact-check: PASS | FAIL
- Search intent QA & linking: PASS | FAIL
- Writing / SEO / GEO: PASS | FAIL

## Blockers
1. ...

## Required corrections
1. Return to workflow step X: ...

## Residual risks
- ...

## Decision
KEEP NOINDEX | READY FOR HUMAN VALIDATION
```

Ne pas réécrire automatiquement toute la page après un `FAIL`. Revenir uniquement aux étapes du `comparison-content-workflow` responsables du blocker, mettre à jour les sources durables, régénérer, puis relancer l'évaluation complète.
