---
name: comparison-content-workflow
description: Workflow générique pour créer, récupérer et valider des comparatifs produits SEO/GEO orientés affiliation. Utiliser pour les pages "meilleur X", "X vs Y", "meilleur X pour Y", "pas cher", "professionnel", "étudiant" et autres pages transactionnelles comparatives. Le workflow impose des critères définis avant le classement, un registre de preuves, un scoring auditable, une justification des recommandations et une QA affiliation/SEO/GEO sans fake test. La méthodologie est commune, mais l'architecture éditoriale doit être spécifique à chaque décision et ne doit jamais être imposée par un template de page.
---

# Comparison Content Workflow

## Objectif

Produire des comparatifs réellement utiles à la décision d'achat, auditables et compatibles avec un modèle d'affiliation.

Le workflow ne doit jamais commencer par :

> "Quels produits voulons-nous recommander ?"

Il commence par :

> "Quelle décision l'utilisateur essaie-t-il de prendre, quels produits sont réellement éligibles, quels critères changent cette décision, et quelles preuves permettent de les comparer ?"

Principes centraux :

> **Critères avant gagnant. Preuves avant scoring. Scoring avant rédaction. Affiliation après décision.**

> **Même méthodologie ne signifie jamais même structure de page. La structure est une conséquence de ce qu'il y a réellement à raconter.**

Une page comparative ne doit pas ressembler à une autre simplement parce qu'elles appartiennent au même dossier `/comparatifs/`. Le workflow peut standardiser la qualité des preuves, du scoring et de la QA ; il ne doit pas standardiser le récit éditorial.

# 1. Entrées obligatoires

Lire avant toute production :
- instructions du repo (`AGENTS.md`, `README`, etc.) ;
- `comparison-workflow.config.yaml` ;
- page cible existante si elle existe ;
- source de vérité éditoriale ;
- analyse sémantique ;
- pages comparatives voisines ;
- pages marques / produits / usages / guides ;
- données marché ou disponibilités si nécessaires ;
- méthodologie de test du site si elle existe ;
- règles d'affiliation ;
- page de référence qualitative définie par `quality_reference`.

Réutiliser les skills existants lorsqu'ils sont présents : `search-intent`, `affiliate-value`, `fact-check`, `content-refresh`, `internal-linking-audit`, `natural-writing`, `humanizer`, `general-writing`, `anti-ai-slop`, `seo-drift`, `seo-technical`, `seo-best-practices`, `editorial-qa`.

# 2. Router le type de comparatif

Choisir un type dominant :
- **Best overall** : meilleur équilibre global.
- **Best for use case** : meilleur produit pour un job-to-be-done précis.
- **Budget** : meilleur compromis sous contrainte de coût.
- **Feature-specific** : meilleure réponse à une caractéristique déterminante.
- **Head-to-head** : comparaison conditionnelle entre deux produits.

Le type de page détermine critères, poids, univers produits et niveau de scoring. Il ne détermine pas automatiquement le plan éditorial.

# 3. Mode RECOVERY ou NEW_CONTENT

## RECOVERY
Si une page existe déjà : conserver les passages utiles, données valides et liens utiles. Conserver le classement uniquement s'il résiste à la nouvelle méthodologie. Ne jamais préserver un gagnant uniquement parce qu'il était déjà #1.

## NEW_CONTENT
Si la page est vide : construire d'abord les données, puis l'angle éditorial, puis seulement la structure et la rédaction.

# 4. Search intent avant sélection produit

Utiliser `search-intent`. Définir requête principale, variantes, intention dominante, sous-intentions, niveau de maturité, contrainte principale, résultat attendu et risque de cannibalisation.

Une requête comme `meilleur bloc-notes numérique étudiant` ne doit pas réutiliser la grille de `meilleur bloc-notes numérique` avec seulement un changement d'introduction. Les critères, poids, tensions décisionnelles et architecture éditoriale peuvent tous changer.

# 5. Product Universe

Construire la liste des produits éligibles avant de choisir les gagnants. Pour chaque produit : marque, modèle, génération, statut actuel, disponibilité, prix si utilisé, stylet inclus ou non, accessoires obligatoires, abonnement éventuel, principales fonctions et sources officielles.

Classer les candidats : `ELIGIBLE`, `CONDITIONALLY_ELIGIBLE`, `OUTDATED`, `NOT_COMPARABLE`, `EXCLUDED`. Documenter toute exclusion. Un produit ne doit pas être ajouté uniquement parce qu'il existe un lien affilié.

# 6. Equivalence Engine

Avant de comparer, déterminer si les produits sont réellement comparables selon job-to-be-done, catégorie fonctionnelle, taille/capacité, workflow, fonctions clés, accessoires nécessaires, logiciel, coûts récurrents, contraintes et public cible.

Attribuer : `EXACT`, `FUNCTIONALLY_COMPARABLE`, `PARTIALLY_COMPARABLE`, `NOT_COMPARABLE`. Pour les comparaisons partielles, expliciter les dimensions non comparables.

# 7. Evidence Ledger

Aucune note ne doit être attribuée avant création du registre de preuves.

| Product | Criterion | Claim | Value | Source | Date | Evidence class |
|---|---|---|---|---|---|---|

Classes :
- `VERIFIED` — source primaire actuelle ;
- `SUPPORTED` — source secondaire crédible ;
- `INFERRED` — conclusion raisonnable depuis plusieurs faits ;
- `USER_PATTERN` — expérience agrégée de plusieurs utilisateurs ;
- `FIRST_HAND` — uniquement si l'utilisateur a fourni un vrai test ;
- `UNKNOWN` — non vérifié ;
- `PROHIBITED` — ne doit pas être publié.

Ne jamais transformer `INFERRED` ou `USER_PATTERN` en expérience directe.

# 8. Définir les critères AVANT le classement

Construire les critères depuis l'intention, le JTBD, les sous-questions, les contraintes et les différences réellement décisionnelles. Exemples : qualité d'écriture, annotation PDF, organisation, export, OCR, cloud, applications, taille, couleur, autonomie, lecture, simplicité, coût total, abonnement, accessoires, réparabilité, disponibilité.

Un critère doit être pertinent pour l'intention, comparable, mesurable ou analysable et soutenu par des preuves.

# 9. Pondération

Définir le poids des critères avant calcul. La somme des poids = 100. Documenter pourquoi le poids change selon l'intention.

**Interdit :** modifier les poids après avoir vu quel produit gagne, sauf erreur méthodologique explicitement documentée.

# 10. Normalisation et scoring

Utiliser une échelle stable, par exemple 0–10. Pour chaque score, conserver valeur, justification, evidence class, références vers les preuves et éventuelle pénalité d'incertitude.

Pour des poids exprimés en pourcentage dont la somme vaut 100 :

`total = Σ(normalized_score × criterion_weight) / 100`

Le résultat reste ainsi sur la même échelle 0–10 que les scores par critère.

La source peut vérifier le fait ; elle ne vérifie jamais automatiquement la note éditoriale. Les scores numériques issus d'un jugement doivent donc être distingués des faits du Evidence Ledger.

Facteurs de confiance optionnels : VERIFIED 1.00, SUPPORTED 0.95, INFERRED 0.85, USER_PATTERN 0.80. UNKNOWN est interdit pour un critère important.

Le ranking final doit conserver score brut, score ajusté et niveau de confiance.

# 11. Hard Gates

Certains critères sont éliminatoires : produit non disponible, fonction indispensable absente, incompatibilité avec le besoin, génération obsolète, données essentielles non vérifiables, prix dépassant une contrainte explicite ou abonnement obligatoire incompatible avec l'intention.

Un produit qui échoue un hard gate ne doit pas gagner grâce à un bon score moyen.

# 12. Total Solution Cost

Comparer le coût de la configuration réellement utilisable :

`TSC = appareil + accessoire obligatoire + protection nécessaire + abonnement utile + consommables + autres coûts indispensables`

Éviter de comparer un appareil nu à un bundle complet. Les coûts non indispensables ne doivent pas être ajoutés mécaniquement.

# 13. Sensitivity & confidence

Lorsque l'écart entre les premiers produits est faible ou lorsque plusieurs pondérations sont discutables, tester des variations raisonnables des poids.

Classer le verdict, par exemple :
- `ROBUST_WINNER` — le même #1 résiste aux variations raisonnables ;
- `CONDITIONAL_WINNER` — le #1 dépend de la priorité donnée à certains critères ;
- `NO_CLEAR_WINNER` — la précision du scoring ne justifie pas un podium affirmatif.

Le texte final doit refléter cette confiance. Une différence de quelques centièmes ne doit jamais devenir un "gagnant incontestable".

# 14. Rank Justification

Chaque produit classé doit répondre à : pourquoi il est présent, pour qui il est recommandé, pour qui il ne l'est pas, avantage principal, limitation principale, critère qui fait réellement bouger la décision, alternative logique et pourquoi il est classé à cette position.

Pour le #1, expliquer ce qu'il gagne **et ce qu'il ne gagne pas**. Un "meilleur" absolu sans critères explicites est interdit.

# 15. Honest Comparison Standard

Le comparatif doit montrer les désavantages du produit recommandé, éviter le cherry-picking, distinguer différence de spec et différence d'usage, distinguer prix affiché et coût réel, distinguer test réel et desk research, distinguer fait/déduction/opinion et signaler les données instables.

La commission d'affiliation ne peut jamais influencer inclusion, score, classement ou formulation des défauts.

# 16. Définir la thèse éditoriale AVANT le plan

Une fois les données stabilisées, formuler une `editorial_thesis` en une ou deux phrases.

Elle doit répondre à :
- quel est le vrai arbitrage de cette page ?
- qu'est-ce qui surprend ou nuance le résultat ?
- quelles deux ou trois tensions expliquent réellement la décision ?
- quel enseignement le lecteur ne trouverait pas dans une simple grille de caractéristiques ?

Exemples de thèses possibles, sans en faire des templates :
- le "meilleur" dépend davantage de l'ouverture logicielle que du matériel ;
- sous un budget donné, les accessoires renversent le classement apparent ;
- deux produits presque ex aequo correspondent en réalité à deux philosophies de travail incompatibles ;
- la taille d'écran est le vrai hard gate, le reste est secondaire ;
- l'absence d'abonnement compte peu tant que certaines fonctions cloud restent réellement accessibles ;
- sur un head-to-head, aucun gagnant global n'existe : deux profils aboutissent à deux choix différents.

Si aucune thèse spécifique n'émerge après analyse, ne pas compenser par une structure générique. Revenir aux données ou accepter qu'une page plus courte soit plus honnête.

# 17. Architecture éditoriale adaptative — aucun template obligatoire

Construire le plan **après** la thèse éditoriale.

Le workflow ne doit jamais imposer une séquence du type :

`méthode → critères → tableau → produit 1 → produit 2 → produit 3 → profils → coût → limites → sources`

Cette structure peut être pertinente pour une page donnée, mais elle n'est jamais un défaut ou un standard à reproduire.

Choisir les blocs uniquement lorsqu'ils servent la décision. Une page peut, par exemple :
- commencer par un verdict conditionnel puis raconter les deux philosophies qui s'opposent ;
- commencer par un hard gate qui élimine la moitié du marché ;
- organiser le contenu autour de trois scénarios d'usage plutôt que d'un podium ;
- raconter pourquoi le classement apparent change dès qu'on ajoute le coût du stylet ou de l'abonnement ;
- traiter d'abord les produits exclus si leur exclusion apprend plus que le classement ;
- utiliser un tableau unique et développer seulement les deux écarts réellement décisifs ;
- consacrer beaucoup plus d'espace au #2 qu'au #1 si c'est lui qui pose le meilleur dilemme éditorial ;
- ne pas créer de bloc par produit si l'histoire se raconte mieux par critères ou profils ;
- réduire fortement la méthodologie visible si elle est déjà expliquée ailleurs et que la page a surtout besoin d'interprétation.

Persistences recommandées :
- `editorial_thesis`
- `decision_tensions`
- `architecture_rationale`
- `must_tell`
- `can_omit`

`architecture_rationale` doit expliquer pourquoi les blocs choisis sont utiles à **cette** page, et pas seulement lister leurs titres.

### Anti-template gate

FAIL éditorial si :
- le plan semble copié d'un comparatif voisin sans raison spécifique ;
- tous les produits reçoivent les mêmes sous-sections par symétrie alors que leurs enjeux diffèrent ;
- un bloc est présent uniquement parce qu'il existe sur les autres comparatifs ;
- la page peut être générée en remplaçant seulement les noms, scores et limites dans une structure commune ;
- la thèse éditoriale n'est pas perceptible dans la hiérarchie du contenu ;
- la méthodologie occupe plus d'espace que l'interprétation sans nécessité particulière.

La diversité éditoriale ne signifie pas variété artificielle. Deux pages peuvent partager une structure si leur logique décisionnelle l'exige réellement ; dans ce cas, `architecture_rationale` doit pouvoir le justifier.

# 18. Rédaction produit et narration

Chaque passage doit apporter de la décision, pas recopier une fiche constructeur.

Ne pas forcer des fiches symétriques. Pour un produit, le point central peut être un hard gate ; pour un autre, une limite de workflow ; pour un troisième, le coût total ; pour un quatrième, une forte dépendance au profil utilisateur.

La longueur d'un bloc doit suivre l'importance de ce qu'il y a à raconter, pas le rang du produit ni un quota de mots.

Les tableaux doivent synthétiser ce qui gagne à être comparé visuellement. Ils ne doivent pas dupliquer le texte et le texte ne doit pas paraphraser ligne par ligne le tableau.

# 19. Affiliate Value

Utiliser `affiliate-value`. La page doit rester utile si tous les liens affiliés disparaissent. Vérifier : commission non prise en compte dans le ranking, défauts visibles, alternatives honnêtes, aucune fausse urgence/disponibilité, prix datés, disclosure claire.

# 20. Fact-check obligatoire

Utiliser `fact-check` après la première rédaction. Vérifier dimensions, écran, autonomie annoncée, formats, compatibilités, cloud, stylet, accessoires, prix, abonnements, génération, disponibilité et comparaisons telles que plus rapide / plus léger / moins cher.

Statuts : `CONFIRMED`, `PARTIAL`, `UNVERIFIED`, `CONTRADICTED`, `OUTDATED`.

# 21. Search Intent QA

Après rédaction : le ranking répond-il réellement à la requête ? Les poids reflètent-ils l'intention ? Le #1 est-il cohérent avec les hard gates ? Une autre page du site répond-elle mieux à l'intention ? Le contenu est-il devenu trop générique ? La structure choisie rend-elle la décision plus claire ou seulement plus longue ?

# 22. Internal Linking

Utiliser `internal-linking-audit`. Prévoir selon pertinence : guides explicatifs, usages, marques, fiches modèles, autres comparatifs, prix/budget, abonnements, technologie. Le comparatif est un hub décisionnel, pas une impasse commerciale.

Ne pas imposer un nombre fixe de liens ni les mêmes destinations sur chaque page.

# 23. Finition éditoriale

Exécuter ensuite `natural-writing`, `humanizer`, `general-writing`, `anti-ai-slop`, `seo-drift`.

Le `seo-drift` compare aussi critères initiaux, poids, scores, ranking final, `editorial_thesis` et architecture. Toute modification du classement sans modification documentée des données ou de la méthode est un blocker. Toute normalisation progressive des plans vers un template commun doit être signalée comme dérive éditoriale.

# 24. SEO

Utiliser `seo-best-practices` et `seo-technical`. Vérifier title, H1, réponse initiale, sous-intentions, entités, maillage, canonical, robots, données structurées si pertinentes et crawlabilité.

Le SEO ne doit jamais imposer les mêmes H2 à tout le cluster. Une sous-intention mérite une section uniquement si elle aide réellement la page cible.

# 25. GEO

Vérifier verdict autonome, relations explicites produit → usage, critères lisibles, méthodologie résumable, sources identifiables, entités complètes et datation des prix/informations instables.

Préférer « Le modèle A est le meilleur choix pour X parce que… » à « Le modèle A est le meilleur. »

La structure GEO doit découler des relations sémantiques réelles de la page, pas d'une checklist identique de blocs.

# 26. Comparison Quality Gate

Le contrôle automatique peut vérifier présence d'une méthodologie, fichier de scoring, somme des poids = 100, produits classés présents dans les données, score justifié, source pour les critères majeurs, hard gates documentés, sources, limites et noindex si brouillon.

Il ne doit jamais imposer :
- un nombre minimum de mots ;
- un nombre minimum de H2 ;
- un nombre minimum de tableaux ;
- un nombre fixe de produits décrits ;
- une séquence de sections ;
- une symétrie entre fiches produit.

Il ne doit jamais déclarer automatiquement fact-check PASS, qualité du ranking PASS, qualité éditoriale PASS, GEO PASS ou affiliation éthique PASS.

# 27. Échecs automatiques et éditoriaux

FAIL si : gagnant choisi avant critères, poids modifiés pour produire un gagnant, commission dans le scoring, score sans justification, produit obsolète classé sans justification, hard gate ignoré, configurations non équivalentes comparées, fake test, avantage comparatif non vérifié, défauts significatifs masqués, données importantes sans date, page marchande déguisée, source de vérité non mise à jour, ou architecture éditoriale manifestement clonée d'une page voisine sans justification.

# 28. Statuts

`UNIVERSE_READY`, `EVIDENCE_READY`, `SCORING_READY`, `EDITORIAL_STRATEGY_READY`, `DRAFT_READY`, `QA_IN_PROGRESS`, `REVISION_REQUIRED`, `HUMAN_APPROVED`, `PUBLISHABLE`.

Le ranking peut être `SCORING_READY` avant qu'une ligne éditoriale ne soit écrite. La rédaction ne doit commencer qu'après `EDITORIAL_STRATEGY_READY` lorsque la page nécessite une narration substantielle.

# 29. Publication

Par défaut : conserver `noindex` si configuré ; ne pas merger, publier ou déployer. Autorisation explicite nécessaire.

# 30. Fichiers persistants

Pour chaque comparatif, `.content/comparisons/<slug>.json` doit conserver au minimum : intent, univers, exclusions, équivalence, critères, poids, hard gates, evidence ledger, scores, classement, niveau de confiance et date de recherche.

Pour les pages éditorialement substantielles, conserver également :
- `editorial_thesis`
- `decision_tensions`
- `architecture_rationale`
- `must_tell`
- `can_omit`

Le texte final ne doit jamais être la seule source expliquant pourquoi le ranking ou le plan éditorial existe.
