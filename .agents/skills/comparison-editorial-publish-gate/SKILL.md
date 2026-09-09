---
name: comparison-editorial-publish-gate
description: Gate éditorial final obligatoire pour les pages /comparatifs/ de bloc-notes-numeriques.fr. Évalue l'intention, l'univers produit, l'équivalence, les preuves, les critères et pondérations, la cohérence du scoring, la justification du classement, la confiance/E-E-A-T, la qualité GEO, la naturalité, l'affiliation, le SEO éditorial et la préparation à la publication. Ne réécrit pas automatiquement une page en échec.
---

# Comparison Editorial Publish Gate

## Rôle

Ce skill est la dernière barrière éditoriale avant publication d'une page sous `/comparatifs/`.

Il ne sert pas à fabriquer un meilleur score ni à ajouter du texte pour faire passer une checklist. Il sert à répondre à une question plus exigeante :

> **Le classement publié est-il réellement défendable pour la décision que le lecteur essaie de prendre ?**

Une page `FAIL` reste en `noindex,follow` et retourne vers la phase de correction concernée. Une page ne peut passer en indexation qu'après `PASS` de ce gate et validation humaine explicite.

Le principe central du site reste :

> **Critères avant gagnant. Preuves avant scoring. Scoring avant rédaction. Affiliation après décision.**

Aucun score moyen ne compense un blocker méthodologique ou éditorial.

---

# Entrées obligatoires

Lire avant l'audit :

- `AGENTS.md` ;
- `comparison-workflow.config.yaml` ;
- `.agents/skills/comparison-content-workflow/SKILL.md` ;
- la page cible complète ;
- `.content/comparisons/<slug>.json` ;
- l'univers produit et les exclusions ;
- les critères, poids, scores et justifications ;
- les sources associées aux différences qui changent le classement ;
- les pages comparatives voisines susceptibles de cannibaliser la même intention ;
- les pages `/usages/`, `/guides/` et `/marques/` qui définissent le contexte de décision ;
- `/methode-de-test/` et `/comment-nous-comparons/` lorsque disponibles.

Réutiliser, quand pertinent :

- `search-intent`
- `jobs-to-be-done`
- `affiliate-value`
- `fact-check`
- `internal-linking-audit`
- `natural-writing`
- `humanizer`
- `general-writing`
- `anti-ai-slop`
- `seo-drift`
- `seo-best-practices`
- `seo-technical`
- `editorial-qa`

Le publish gate doit évaluer la page telle qu'un lecteur la reçoit. La présence de tableaux, scores, H2, sources ou liens n'est jamais une preuve de qualité en soi.

---

# Gate 0 — Contrat de décision

Identifier explicitement :

- type dominant : `BEST_OVERALL`, `BEST_FOR_USE_CASE`, `BUDGET`, `FEATURE_SPECIFIC` ou `HEAD_TO_HEAD` ;
- requête et décision principale ;
- contraintes déterminantes ;
- résultat recherché par le lecteur ;
- univers produit qui peut raisonnablement satisfaire cette décision ;
- date à laquelle cet univers et les données ont été vérifiés.

PASS lorsque le rôle de la page peut être formulé en une phrase précise.

FAIL si :

- la page ne sait pas quelle décision elle aide à prendre ;
- un comparatif `pour étudiant`, `professionnel`, `sans abonnement`, `pas cher`, etc. réutilise essentiellement la logique d'un comparatif générique ;
- un `HEAD_TO_HEAD` ne précise pas les générations ou produits réellement comparés ;
- la page chevauche fortement un autre comparatif sans angle décisionnel distinct.

---

# Gate 1 — Intention et pertinence éditoriale

PASS lorsque :

- une réponse exploitable arrive tôt ;
- le verdict répond exactement à la requête, pas à une catégorie plus large ;
- chaque grande section modifie ou éclaire la décision ;
- les critères développés correspondent aux vraies tensions du choix ;
- les contenus génériques de guide sont renvoyés vers `/guides/` plutôt que reproduits sans nécessité ;
- les profils et cas d'usage renvoient vers `/usages/` lorsqu'une analyse plus profonde y existe ;
- la page ne parle pas au propriétaire du site de SEO, GEO, maillage, architecture ou stratégie éditoriale.

Questions de contrôle :

1. Quel arbitrage concret cette section clarifie-t-elle ?
2. Le passage explique-t-il une différence entre les candidats ou seulement le marché en général ?
3. Si le nom des produits disparaît, le texte reste-t-il générique au point de pouvoir être copié sur n'importe quel comparatif ?

FAIL si la majorité du contenu pourrait vivre dans un guide générique sans perdre de sens.

---

# Gate 2 — Univers produit et exclusions

Un classement n'est défendable que si l'univers comparé l'est aussi.

Pour chaque candidat pertinent, déterminer :

- génération exacte ;
- statut actuel ;
- disponibilité pertinente pour la cible ;
- catégorie fonctionnelle ;
- raison d'inclusion ou d'exclusion ;
- source permettant de vérifier ces éléments.

PASS lorsque :

- les candidats évidents et actuels ont été considérés ;
- toute exclusion importante est justifiée ;
- un ancien modèle n'est pas classé comme s'il représentait la gamme actuelle sans raison ;
- l'absence d'affiliation n'exclut pas un produit pertinent ;
- un produit n'est pas inclus seulement parce qu'il est monétisable.

FAIL si un concurrent directement pertinent manque sans explication, si un produit obsolète est classé sans justification, ou si l'univers semble construit après le choix du gagnant.

Un audit de marché exhaustif n'est pas toujours nécessaire, mais l'univers doit être suffisamment complet pour rendre le verdict honnête.

---

# Gate 3 — Équivalence et comparabilité

Classer les relations entre candidats :

- `EXACT`
- `FUNCTIONALLY_COMPARABLE`
- `PARTIALLY_COMPARABLE`
- `NOT_COMPARABLE`

PASS lorsque :

- les produits sont comparés sur des dimensions réellement communes ;
- les différences de catégorie ou d'écosystème sont expliquées ;
- une comparaison partielle reste présentée comme partielle ;
- les bundles et configurations sont ramenés à une base utile au lecteur ;
- les produits ne gagnent pas grâce à des fonctions qui n'ont aucun rapport avec la décision ciblée.

FAIL si :

- deux produits fondamentalement différents sont réduits à une moyenne artificielle ;
- une fonction absente parce qu'elle n'appartient pas au même job est traitée comme un simple « 0/10 » sans contexte ;
- le comparatif de prix oppose un appareil nu à un bundle complet sans correction ;
- un écart de génération rend une comparaison trompeuse.

---

# Gate 4 — Preuves et factualité

Extraire les affirmations qui changent la décision ou le classement et les classer :

- `VERIFIED` : source primaire actuelle ;
- `SUPPORTED` : source secondaire fiable ;
- `INFERRED` : interprétation éditoriale raisonnable à partir de faits vérifiés ;
- `USER_PATTERN` : motif agrégé depuis plusieurs retours utilisateurs identifiables ;
- `FIRST_HAND` : observation directe réellement documentée ;
- `UNKNOWN` : non vérifié ;
- `OUTDATED` : information devenue obsolète ;
- `CONTRADICTED` : contredit par une meilleure source ;
- `PROHIBITED` : ne doit pas être publié.

PASS lorsque :

- les caractéristiques qui influencent le ranking sont sourcées ;
- les prix, abonnements, disponibilités et générations sont datés lorsqu'ils sont volatils ;
- les comparaisons « plus léger », « moins cher », « plus ouvert », « meilleur pour le PDF », etc. peuvent être retracées ;
- une inférence reste identifiable comme analyse et non comme mesure ;
- les inconnues importantes réduisent le niveau de confiance ou empêchent le produit de gagner.

FAIL si une affirmation déterminante est `UNKNOWN`, `OUTDATED` ou `CONTRADICTED` sans qualification claire.

### Règle spéciale sur les scores

Le niveau de preuve d'un **fait** et le niveau de preuve d'une **note éditoriale** ne sont pas la même chose.

Une source officielle peut vérifier qu'une fonction existe ; elle ne « vérifie » pas automatiquement qu'un produit mérite `9/10`.

Une justification comme :

> « Official capabilities reviewed; numeric score is an editorial normalization. »

n'est pas suffisante à elle seule pour défendre une note. La justification doit citer la différence concrète qui explique pourquoi le score est supérieur, inférieur ou égal à celui des concurrents.

FAIL si les notes importantes reposent sur des justifications génériques ou circulaires.

---

# Gate 5 — Critères et pondérations

Pour chaque critère, vérifier :

- lien avec l'intention ;
- caractère décisionnel ;
- comparabilité ;
- définition suffisamment claire ;
- poids justifiable ;
- preuve disponible.

La somme des poids doit être 100, mais **100 n'est qu'une condition mathématique, pas une preuve de qualité**.

PASS lorsque les poids peuvent être expliqués avant de connaître le gagnant.

FAIL si :

- un critère important pour l'intention est absent ;
- un critère secondaire reçoit un poids disproportionné uniquement parce qu'il favorise le gagnant ;
- plusieurs critères mesurent presque la même chose et doublent artificiellement leur influence ;
- les poids ont manifestement été ajustés pour modifier le résultat sans changement documenté de méthode ou de données ;
- un comparatif spécialisé reprend les poids du comparatif général sans justification.

### Test de sensibilité

Lorsque deux produits sont proches, poser au minimum la question :

> Une variation raisonnable des poids des critères discutables inverse-t-elle le #1 ?

Si oui, le verdict doit être plus conditionnel et le niveau de confiance réduit. Un « gagnant clair » n'est pas acceptable si le classement dépend d'un choix de pondération fragile.

---

# Gate 6 — Scoring et cohérence mathématique

PASS lorsque :

- tous les produits classés possèdent les scores nécessaires ;
- les scores restent dans l'échelle définie ;
- les justifications sont spécifiques ;
- le calcul du score final correspond aux poids publiés/persistés ;
- le ranking est trié selon les scores calculés, sauf règle documentée ;
- toute pénalité de confiance est explicite ;
- aucun hard gate n'est contourné par une bonne moyenne.

FAIL si :

- le score affiché ne peut pas être recalculé ;
- le ranking ne correspond pas aux scores ;
- une note existe sans justification ;
- le même texte générique justifie des notes différentes ;
- un produit échoue une contrainte éliminatoire mais reste gagnant ;
- des données `UNKNOWN` soutiennent silencieusement un score déterminant.

Ne pas confondre précision numérique et précision méthodologique. Un `8,35/10` n'est pas plus fiable qu'un `8/10` si les critères sous-jacents sont éditoriaux et approximatifs.

---

# Gate 7 — Verdict, ranking et justification du gagnant

Chaque produit classé doit permettre de comprendre :

- pourquoi il est présent ;
- pour qui il constitue une bonne option ;
- pour qui il convient moins ;
- avantage réellement déterminant ;
- limite réellement déterminante ;
- alternative logique ;
- raison de sa position par rapport au produit juste au-dessus et juste en dessous lorsque cela aide la décision.

Pour le #1 :

- expliquer ce qu'il gagne ;
- expliquer ce qu'il ne gagne pas ;
- indiquer le profil pour lequel le #2 ou une autre alternative devient meilleur ;
- éviter le langage absolu si l'écart est faible ou dépend de poids discutables.

FAIL si le gagnant est annoncé comme évident alors que les scores sont presque équivalents, si les limites importantes sont minimisées, ou si le texte recommande un produit pour des raisons absentes du scoring.

### Head-to-head

Un `A vs B` ne doit pas nécessairement produire un vainqueur universel.

PASS lorsque le verdict peut être conditionnel :

- choisir A si X ;
- choisir B si Y.

FAIL si un score global écrase artificiellement deux propositions de valeur différentes alors que la bonne décision dépend clairement du profil.

---

# Gate 8 — Hard gates et coût total

Vérifier les contraintes éliminatoires pertinentes :

- disponibilité ;
- fonction indispensable ;
- compatibilité ;
- génération ;
- données essentielles vérifiables ;
- budget maximal ;
- abonnement obligatoire incompatible ;
- autre contrainte explicitement liée à l'intention.

PASS lorsque les hard gates sont appliqués avant le ranking.

Pour le prix, comparer lorsque pertinent le **coût de la solution réellement utilisable** : appareil, stylet/accessoire obligatoire, protection nécessaire, abonnement utile ou obligatoire, autres coûts indispensables.

FAIL si un produit paraît moins cher uniquement parce que des éléments nécessaires ont été omis ou si un hard gate connu est absorbé dans une moyenne.

---

# Gate 9 — Trust / E-E-A-T observable

Ne pas fabriquer de posture d'expertise.

Évaluer les signaux observables :

- la méthode de comparaison est compréhensible ;
- les critères et leurs conséquences sont explicites ;
- les sources importantes sont traçables ;
- le niveau de preuve est honnête ;
- affiliation et intérêt commercial sont transparents ;
- limites et contre-indications sont visibles ;
- une analyse documentaire n'est jamais présentée comme un test ;
- les retours utilisateurs externes ne deviennent jamais une expérience propre ;
- les incertitudes méthodologiques sont visibles lorsque le classement est serré.

FAIL en cas de faux signal hands-on, de certitude disproportionnée ou de score présenté comme une mesure objective alors qu'il s'agit d'une normalisation éditoriale.

---

# Gate 10 — Affiliation et indépendance du ranking

La page doit rester utile si tous les liens affiliés disparaissent.

PASS lorsque :

- la commission n'entre ni dans l'univers, ni dans les poids, ni dans les scores, ni dans le classement ;
- un produit sans programme peut être recommandé ;
- les défauts d'un produit affilié restent aussi visibles que ceux des autres ;
- l'ordre des CTA ne donne pas une impression différente du ranking sans explication ;
- les prix et disponibilités ne créent pas de fausse urgence ;
- les liens commerciaux sont identifiés conformément à la politique du site.

FAIL si la monétisation semble avoir modifié inclusion, exclusion, formulation ou verdict.

---

# Gate 11 — GEO / entités et citabilité

Le GEO n'est pas une excuse pour produire des mini-réponses répétitives.

PASS lorsque :

- les produits et générations sont nommés sans ambiguïté ;
- les relations `produit -> critère -> conséquence -> usage` sont explicites ;
- les verdicts peuvent être compris hors contexte immédiat ;
- les tableaux sont interprétés dans le texte ;
- les distinctions entre produits sont formulées avec assez de précision pour être citées ;
- la méthode reste résumable ;
- les informations instables sont datées.

FAIL si la page multiplie les définitions évidentes, les répétitions de noms de produits ou les formulations télégraphiques uniquement pour une supposée optimisation LLM.

---

# Gate 12 — Ton, registre et anti-AI-slop

Voix cible :

- français naturel ;
- média éditorial spécialisé ;
- précis, sobre et comparatif ;
- compétent sans posture d'expert auto-proclamé ;
- orienté arbitrage ;
- ni fiche marketing, ni comparateur de prix agressif, ni rapport de consultant SEO.

Utiliser `anti-ai-slop`, puis `humanizer` / `natural-writing` uniquement sur les passages réellement problématiques.

FAIL notamment pour :

- introductions qui reformulent le H1 ;
- paragraphes génériques applicables à tous les produits ;
- répétition mécanique `avantage / limite / pour qui` lorsque les produits nécessitent des explications différentes ;
- mêmes longueurs, mêmes transitions et même cadence pour chaque bloc produit ;
- « il est important de », « il convient de », « en conclusion », « dans un monde où », « que vous soyez » ;
- abus de « meilleur », « idéal », « parfait », « incontournable », « se distingue » sans critère précis ;
- symétrie artificielle entre deux produits dans un head-to-head ;
- conclusion qui répète simplement le classement ;
- métadiscours : « dans ce comparatif nous avons optimisé », « cette section sert à », « pour le SEO/GEO », « le maillage ».

FAIL si des signaux `HIGH` d'anti-AI-slop restent dans le corps principal.

---

# Gate 13 — SEO éditorial et cannibalisation

Contrôler sans quota artificiel :

- title, H1 et requête cohérents ;
- réponse initiale adaptée à l'intention ;
- H2/H3 correspondant à de vrais arbitrages ;
- absence de keyword stuffing ;
- ancres internes descriptives ;
- maillage vers les prochaines étapes réellement utiles ;
- distinction claire avec les autres comparatifs ;
- canonical, robots et données structurées cohérents ;
- absence de section créée uniquement pour ajouter un mot-clé ou un lien.

Ne jamais imposer un minimum de mots, de H2, de tableaux ou de liens internes comme preuve de qualité.

FAIL en cas de cannibalisation forte non résolue ou de promesse SERP différente de la décision réellement traitée.

---

# Gate 14 — Contrôle par type

## BEST_OVERALL

Doit représenter le meilleur compromis pour une intention générale explicitement définie. Le #1 ne doit pas être présenté comme universellement supérieur. Les grands profils qui inversent le choix doivent être visibles.

## BEST_FOR_USE_CASE

Les critères et poids doivent être dérivés du job-to-be-done. Un comparatif spécialisé qui ne change que l'introduction par rapport au `BEST_OVERALL` est `FAIL`.

## BUDGET

Le budget doit être une contrainte réelle, pas une simple colonne de prix. Vérifier coût total, seuil, compromis nécessaires et exclusions. Une baisse de prix temporaire ne doit pas redéfinir silencieusement un classement evergreen.

## FEATURE_SPECIFIC

La caractéristique ciblée doit réellement dominer la décision, sans effacer les hard gates nécessaires à un produit utilisable.

## HEAD_TO_HEAD

Doit expliquer les différences qui font choisir A ou B. Un verdict conditionnel est souvent plus honnête qu'un gagnant absolu. Les générations, configurations et prix comparés doivent être explicites.

---

# Gate 15 — Publication

Statuts possibles :

- `PASS`
- `FAIL`

Un seul blocker suffit à maintenir la page en `noindex,follow`.

## Blockers absolus

- gagnant choisi avant critères ;
- univers produit manifestement incomplet ou biaisé ;
- produit non comparable classé sans qualification ;
- score important sans justification concrète ;
- fait déterminant non vérifié présenté comme certain ;
- niveau de preuve d'une note confondu avec la simple existence d'une source fabricant ;
- poids opportunistes ou double comptage de critères ;
- ranking impossible à recalculer ou incohérent avec les scores ;
- hard gate ignoré ;
- verdict absolu construit sur un écart fragile sans avertissement ;
- fake test ou fausse expérience ;
- commission influençant l'univers, le scoring, le classement ou la formulation ;
- défaut significatif du gagnant masqué ;
- contenu essentiellement générique ou dérivé de marchands sans interprétation ;
- cannibalisation forte non résolue ;
- métadiscours éditorial manifeste ;
- signaux anti-AI-slop de sévérité `HIGH` ;
- page indexable avant validation humaine explicite.

## Output obligatoire

```md
# Comparison editorial publish gate

URL: ...
Comparison type: ...
Status: PASS | FAIL

## Decision contract
- Query: ...
- User decision: ...
- Product universe reviewed: ...
- Research date: ...

## Blockers
- ...

## Gate results
- Intent & relevance: PASS | FAIL
- Product universe: PASS | FAIL
- Equivalence: PASS | FAIL
- Evidence & factuality: PASS | FAIL
- Criteria & weighting: PASS | FAIL
- Scoring integrity: PASS | FAIL
- Ranking justification: PASS | FAIL
- Hard gates / total cost: PASS | FAIL
- Trust / E-E-A-T: PASS | FAIL
- Affiliate independence: PASS | FAIL
- GEO / entities: PASS | FAIL
- Tone / anti-AI-slop: PASS | FAIL
- SEO editorial / cannibalization: PASS | FAIL
- Comparison-type fit: PASS | FAIL

## Ranking integrity
- Recalculated ranking matches stored ranking: YES | NO
- Winner robust to reasonable weighting variation: YES | NO | NOT TESTED
- Important UNKNOWN data: ...
- Score margin requiring caution: ...

## Required corrections
1. ...

## Residual risks
- ...

## Publication decision
KEEP NOINDEX | READY FOR HUMAN VALIDATION
```

Un `FAIL` ne déclenche pas automatiquement une réécriture globale. Corriger uniquement les gates en échec, mettre à jour `.content/comparisons/<slug>.json` lorsque la méthode ou les preuves changent, régénérer la page, puis relancer le publish gate.
