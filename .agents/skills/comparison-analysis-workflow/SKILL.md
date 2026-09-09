---
name: comparison-analysis-workflow
description: Workflow unique d'analyse des pages /comparatifs/ de bloc-notes-numeriques.fr. Audite une page ou le cluster, contrôle intention, univers produit, équivalence, preuves, critères, scoring, ranking, valeur affiliée, AI-slop, SEO et cannibalisation, puis décide KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX. En mode PUBLISH_REVIEW, sert de gate final avant validation humaine.
metadata:
  adapted_for: bloc-notes-numeriques.fr
  orchestration_target: ">=80% existing skills"
---

# Comparison Analysis Workflow

## Rôle

C'est le **seul workflow d'analyse** à utiliser pour les URLs sous `/comparatifs/`.

Il ne réécrit pas la page par défaut. Il orchestre majoritairement les skills spécialisés déjà présents dans le dépôt et ajoute uniquement les contrôles propres aux comparatifs : intégrité méthodologique du ranking, équivalence des produits, hard gates, coût total, dérive du scoring et similarité structurelle du cluster.

Les autres types de pages conservent leurs workflows propres.

## Modes

### `AUDIT`
Mode par défaut pour une URL existante. Retourne un diagnostic, une décision et un handoff sans produire la nouvelle page.

### `CLUSTER_AUDIT`
Analyse plusieurs URLs `/comparatifs/` ensemble afin de détecter cannibalisation, critères recyclés, rankings mécaniques, duplication de rôle et industrialisation de structure.

### `PUBLISH_REVIEW`
Gate final après rédaction. Il vérifie la page, sa méthodologie et son contexte de cluster, exécute le validateur machine et retourne soit :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS ne retire jamais `noindex,follow` automatiquement.

---

# 1. Entrées

Lire avant l'audit :

- `AGENTS.md` ;
- `comparison-workflow.config.yaml` ;
- page cible et comparatifs voisins ;
- `.content/comparisons/<slug>.json` ;
- pages marques, produits, usages et guides nécessaires pour comprendre le périmètre ;
- données GSC, sémantiques ou historiques disponibles ;
- sources actuelles lorsque gamme, prix, disponibilité ou fonctions peuvent avoir évolué.

Ne jamais inventer une donnée absente pour compléter le scoring ou l'audit.

---

# 2. Chaîne de skills obligatoire

L'analyse doit d'abord exécuter les skills existants plutôt que recopier leurs checklists.

## 2.1 `content-audit`

Vérifier si l'URL possède encore une fonction autonome, une demande identifiable et une valeur éditoriale distincte. Identifier obsolescence, contenu marchand, duplication, faiblesse structurelle et potentiel de récupération.

## 2.2 `search-intent`

Déterminer : requête/topic principal, intention, décision réelle du lecteur, rôle de l'URL, sous-intentions et chevauchements avec les autres comparatifs.

## 2.3 `jobs-to-be-done`

Obligatoire pour les comparatifs orientés usage, métier ou contexte (`étudiant`, `professionnel`, etc.). Vérifier que les critères partent du travail à accomplir et non d'un persona générique ou du classement d'une autre page.

## 2.4 `content-refresh`

Si la page mérite une mise à jour, diagnostiquer `Intent drift`, `Outdated`, `Weak structure`, `Generic prose`, `Cannibalization`, `Trust gap`, `Merchant duplication` ou `Thin value`, puis distinguer correction légère et révision majeure.

## 2.5 `affiliate-value`

Vérifier que le comparatif reste utile si tous les liens affiliés disparaissent, que les défauts sont visibles et que commissions, disponibilité marchande ou préférence commerciale n'influencent pas inclusion, score ou ranking.

## 2.6 `fact-check`

Extraire les claims, vérifier les facts produits, prix, générations, compatibilités, abonnements et comparaisons. Les inconnues restent visibles.

## 2.7 `evidence-based-reviews`

À utiliser dès qu'un score ou un verdict repose sur ergonomie, qualité d'écriture, fluidité, autonomie observée, fiabilité ou autre expérience non réductible à une spec. Ne jamais convertir un test tiers en expérience propre au site.

## 2.8 `internal-linking-audit`

Vérifier que les liens servent une prochaine question logique : page marque, produit, usage, guide, autre comparatif, prix, service ou alternative. Aucun quota.

## 2.9 `anti-ai-slop`

Rechercher structure trop symétrique, fiches produits interchangeables, verdicts génériques, répétition de formulations et pages qui semblent générées à partir d'un même squelette.

## 2.10 SEO

Utiliser `seo-technical` pour canonical, robots, indexability, schema et crawlabilité ; `seo-best-practices` pour les règles réellement applicables ; `seo-drift` lorsqu'un avant/après ou une dérive de ranking doit être contrôlé.

## 2.11 `editorial-qa`

Dernière QA générique : intention, originalité, factualité, naturel, SEO et utilité réelle sans affiliation.

---

# 3. Contrôle custom n°1 — intégrité de la comparaison

Le type de comparatif sert de **grille méthodologique**, jamais de template éditorial.

Types dominants :

- `BEST_OVERALL`
- `USE_CASE`
- `BUDGET`
- `FEATURE_SPECIFIC`
- `HEAD_TO_HEAD`

Vérifier :

### Product Universe
- les candidats pertinents ont été considérés avant le gagnant ;
- chaque exclusion est justifiée ;
- les modèles obsolètes ou indisponibles sont qualifiés ;
- aucun produit n'est inclus uniquement parce qu'un lien affilié existe.

### Equivalence
- les produits répondent à un job comparable ;
- les configurations sont comparables ;
- une comparaison partielle explicite ses dimensions non comparables.

### Criteria-before-winner
- les critères découlent de l'intention ;
- les poids ont été définis avant le classement ;
- ils ne sont pas ajustés pour produire un gagnant souhaité.

### Evidence-before-score
- chaque score important possède une justification et un niveau de preuve ;
- une spec officielle ne suffit pas à prouver une sensation d'usage ;
- `UNKNOWN` ne produit pas un score de confiance artificiel.

### Hard gates
- une fonction indispensable absente peut éliminer un produit ;
- un produit ne gagne pas par moyenne s'il échoue une contrainte essentielle de l'intention.

### Total Solution Cost
- lorsque le coût est décisionnel, comparer la configuration réellement utilisable : appareil, stylet, accessoires nécessaires, abonnement utile et autres coûts indispensables ;
- ne pas comparer un appareil nu avec un bundle complet sans le signaler.

### Ranking integrity
- le classement découle des données et de la méthode ;
- le #1 explique aussi ce qu'il ne gagne pas ;
- toute variation de ranking entre versions doit être reliée à une donnée, un critère, un poids ou un hard gate documenté.

Une rupture substantielle de cette chaîne entraîne `DEEP_REWRITE` même si la prose est correcte.

---

# 4. Contrôle custom n°2 — adéquation de la méthode à l'intention

Le même produit peut légitimement gagner plusieurs comparatifs. Ce n'est pas un problème si les critères le démontrent.

Le FAIL intervient lorsque des pages différentes réutilisent sans justification :

- le même univers produit ;
- les mêmes critères ;
- les mêmes poids ;
- le même ordre de recommandations ;
- les mêmes hard gates ;
- la même logique de verdict ;

alors que leurs intentions diffèrent.

Exemple : `meilleur bloc-notes numérique étudiant` ne doit pas être `meilleur bloc-notes numérique` avec une nouvelle introduction. Les critères doivent refléter l'usage étudiant si cet usage change réellement la décision.

---

# 5. Contrôle custom n°3 — similarité structurelle du cluster

En `AUDIT`, comparer la page avec les comparatifs les plus proches. En `CLUSTER_AUDIT` et `PUBLISH_REVIEW`, examiner le cluster pertinent.

Comparer :

- fonctions et ordre des H2/H3 ;
- forme des verdicts ;
- ordre des produits ;
- blocs produits symétriques ;
- emplacement systématique des tableaux, méthodologies, CTA et conclusions ;
- transitions recyclées ;
- mêmes listes « pour qui / pas pour qui » ;
- mêmes arguments reconditionnés sous plusieurs intentions.

Les composants visuels partagés ne sont pas un problème. Le blocker existe lorsque l'architecture éditoriale paraît définie avant l'intention, les preuves et la méthode.

Si substantiel : `DEEP_REWRITE`.

---

# 6. Contrôle de preuves

Hiérarchie par défaut :

1. fabricant, manuel, support officiel ;
2. distributeur officiel ;
3. retailer fiable pour prix/disponibilité ;
4. tests et publications indépendantes nommées ;
5. plusieurs sources utilisateurs pour des patterns d'expérience.

Pour les informations importantes : `VERIFIED`, `SUPPORTED`, `INFERRED`, `USER_PATTERN`, `FIRST_HAND`, `UNKNOWN`, `OUTDATED`, `CONTRADICTED`.

`FIRST_HAND` n'est autorisé qu'avec un test réellement documenté. `UNKNOWN` et `CONTRADICTED` ne deviennent jamais des faits certains.

---

# 7. Décision AUDIT / CLUSTER_AUDIT

Utiliser cinq statuts simples :

### `KEEP`
Méthode, contenu, ranking et rôle encore solides. Pas de modification substantielle requise.

### `LIGHT_UPDATE`
Facts, prix, disponibilité, sources, quelques scores ou passages doivent être mis à jour sans reconstruire la méthode fondamentale.

### `DEEP_REWRITE`
Intent mal servi, univers incomplet, critères/poids inadéquats, ranking non auditable, preuves insuffisantes, architecture générique ou reconstruction importante nécessaire.

### `MERGE`
Une autre URL couvre essentiellement la même décision et la distinction ne justifie pas deux comparatifs.

### `NOINDEX`
La page n'a pas encore assez de valeur, de demande, de preuve ou de méthodologie pour être indexée. Aucune suppression ou redirection n'est appliquée automatiquement.

Pour chaque décision fournir : confiance, valeur existante, blockers, preuves, unknowns, modifications nécessaires et prochaine étape.

Pour `DEEP_REWRITE`, passer la main à `comparison-content-workflow`.

---

# 8. Mode PUBLISH_REVIEW

Exécuter uniquement sur un draft considéré terminé.

## Étape A — validation machine

Exécuter :

```bash
python3 validate_comparisons.py
```

Un PASS machine est seulement un plancher méthodologique et structurel.

## Étape B — gates substantiels

Vérifier au minimum :

- intention satisfaite ;
- univers produit justifié ;
- équivalence documentée ;
- critères et poids cohérents avec l'intention ;
- hard gates respectés ;
- TSC utilisé lorsqu'il change la décision ;
- scoring traçable aux preuves ;
- ranking cohérent et stable par rapport aux données ;
- commissions absentes du ranking ;
- défauts du gagnant visibles ;
- facts importants actuels et sourcés ;
- aucun faux test ;
- pas de merchant rewrite ;
- pas de cannibalisation non résolue ;
- pas de signal `HIGH` d'AI-slop ;
- architecture justifiée par la comparaison ;
- absence de clonage structurel substantiel avec les pages sœurs ;
- title/H1/canonical/robots cohérents ;
- page utile même sans liens affiliés.

## Étape C — résultat

### PASS
Retourner exactement :

`PASS — READY_FOR_HUMAN_VALIDATION`

Lister les éventuels risques mineurs.

### FAIL
Retourner :

`FAIL — KEEP_NOINDEX`

Lister les gates en échec et router vers le skill ou workflow approprié. Un FAIL ne déclenche pas automatiquement une réécriture complète.

---

# 9. Indexation

Par défaut, conserver `noindex,follow`.

Conditions cumulatives avant une future indexation :

1. aucun blocker dans `validate_comparisons.py` ;
2. `PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` ;
3. validation humaine explicite ;
4. instruction explicite de rendre la page indexable.

---

# 10. Ce que ce workflow ne doit pas devenir

Ne pas ajouter : quotas de mots, headings ou liens ; score artificiel de qualité éditoriale ; template fixe par type de comparatif ; générateur de texte ; deuxième copie des checklists maintenues dans les skills appelés.

Sa valeur est l'orchestration, l'audit de la méthodologie comparative, la décision et le contrôle inter-pages.
