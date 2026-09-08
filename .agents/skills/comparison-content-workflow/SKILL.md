---
name: comparison-content-workflow
description: Workflow générique pour créer, récupérer et valider des comparatifs produits SEO/GEO orientés affiliation. Utiliser pour les pages "meilleur X", "X vs Y", "meilleur X pour Y", "pas cher", "professionnel", "étudiant" et autres pages transactionnelles comparatives. Le workflow impose des critères définis avant le classement, un registre de preuves, un scoring auditable, une justification des recommandations et une QA affiliation/SEO/GEO sans fake test.
---

# Comparison Content Workflow

## Objectif

Produire des comparatifs réellement utiles à la décision d'achat, auditables et compatibles avec un modèle d'affiliation.

Le workflow ne doit jamais commencer par :

> "Quels produits voulons-nous recommander ?"

Il commence par :

> "Quelle décision l'utilisateur essaie-t-il de prendre, quels produits sont réellement éligibles, quels critères changent cette décision, et quelles preuves permettent de les comparer ?"

Principe central :

> **Critères avant gagnant. Preuves avant scoring. Scoring avant rédaction. Affiliation après décision.**

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

Le type de page détermine critères, poids, univers produits, architecture et niveau de scoring.

# 3. Mode RECOVERY ou NEW_CONTENT

## RECOVERY
Si une page existe déjà : conserver les passages utiles, données valides et liens utiles. Conserver le classement uniquement s'il résiste à la nouvelle méthodologie. Ne jamais préserver un gagnant uniquement parce qu'il était déjà #1.

## NEW_CONTENT
Si la page est vide : construire d'abord les données, rédiger ensuite.

# 4. Search intent avant sélection produit

Utiliser `search-intent`. Définir requête principale, variantes, intention dominante, sous-intentions, niveau de maturité, contrainte principale, résultat attendu et risque de cannibalisation.

Une requête comme `meilleur bloc-notes numérique étudiant` ne doit pas réutiliser la grille de `meilleur bloc-notes numérique` avec seulement un changement d'introduction. Les critères et poids doivent changer.

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

Utiliser une échelle stable, par exemple 0–10. Pour chaque score, conserver valeur, justification, evidence class et éventuelle pénalité d'incertitude.

`criterion_score = normalized_score × criterion_weight`

`total = Σ criterion_score / 10`

Facteurs de confiance optionnels : VERIFIED 1.00, SUPPORTED 0.95, INFERRED 0.85, USER_PATTERN 0.80. UNKNOWN est interdit pour un critère important.

Le ranking final doit conserver score brut, score ajusté et niveau de confiance.

# 11. Hard Gates

Certains critères sont éliminatoires : produit non disponible, fonction indispensable absente, incompatibilité avec le besoin, génération obsolète, données essentielles non vérifiables, prix dépassant une contrainte explicite ou abonnement obligatoire incompatible avec l'intention.

Un produit qui échoue un hard gate ne doit pas gagner grâce à un bon score moyen.

# 12. Total Solution Cost

Comparer le coût de la configuration réellement utilisable :

`TSC = appareil + accessoire obligatoire + protection nécessaire + abonnement utile + consommables + autres coûts indispensables`

Éviter de comparer un appareil nu à un bundle complet. Les coûts non indispensables ne doivent pas être ajoutés mécaniquement.

# 13. Rank Justification

Chaque produit classé doit répondre à : pourquoi il est présent, pour qui il est recommandé, pour qui il ne l'est pas, avantage principal, limitation principale, critère qui fait réellement bouger la décision, alternative logique et pourquoi il est classé à cette position.

Pour le #1, expliquer ce qu'il gagne **et ce qu'il ne gagne pas**. Un "meilleur" absolu sans critères explicites est interdit.

# 14. Honest Comparison Standard

Le comparatif doit montrer les désavantages du produit recommandé, éviter le cherry-picking, distinguer différence de spec et différence d'usage, distinguer prix affiché et coût réel, distinguer test réel et desk research, distinguer fait/déduction/opinion et signaler les données instables.

La commission d'affiliation ne peut jamais influencer inclusion, score, classement ou formulation des défauts.

# 15. Architecture éditoriale

Une page "best X" peut contenir : réponse rapide/sélection, méthodologie, tableau de comparaison, critères déterminants, produits classés, profils, limites/exclusions, coût total, comment choisir, liens vers guides/usages/marques, sources/fraîcheur.

Pour `A vs B` : verdict rapide conditionnel, différences qui comptent, tableau, critères comparés, coût total, pour qui choisir A, pour qui choisir B, verdict final, sources.

# 16. Rédaction produit

Chaque bloc produit doit apporter de la décision, pas recopier une fiche constructeur. Structure possible : verdict, pourquoi il se distingue, avantage déterminant, limite déterminante, pour qui, pour qui non, alternative, CTA.

Éviter les fiches symétriques artificielles si les produits nécessitent des explications différentes.

# 17. Affiliate Value

Utiliser `affiliate-value`. La page doit rester utile si tous les liens affiliés disparaissent. Vérifier : commission non prise en compte dans le ranking, défauts visibles, alternatives honnêtes, aucune fausse urgence/disponibilité, prix datés, disclosure claire.

# 18. Fact-check obligatoire

Utiliser `fact-check` après la première rédaction. Vérifier dimensions, écran, autonomie annoncée, formats, compatibilités, cloud, stylet, accessoires, prix, abonnements, génération, disponibilité et comparaisons telles que plus rapide / plus léger / moins cher.

Statuts : `CONFIRMED`, `PARTIAL`, `UNVERIFIED`, `CONTRADICTED`, `OUTDATED`.

# 19. Search Intent QA

Après rédaction : le ranking répond-il réellement à la requête ? Les poids reflètent-ils l'intention ? Le #1 est-il cohérent avec les hard gates ? Une autre page du site répond-elle mieux à l'intention ? Le contenu est-il devenu trop générique ?

# 20. Internal Linking

Utiliser `internal-linking-audit`. Prévoir selon pertinence : guides explicatifs, usages, marques, fiches modèles, autres comparatifs, prix/budget, abonnements, technologie. Le comparatif est un hub décisionnel, pas une impasse commerciale.

# 21. Finition éditoriale

Exécuter ensuite `natural-writing`, `humanizer`, `general-writing`, `anti-ai-slop`, `seo-drift`.

Le `seo-drift` compare aussi critères initiaux, poids, scores et ranking final. Toute modification du classement sans modification documentée des données ou de la méthode est un blocker.

# 22. SEO

Utiliser `seo-best-practices` et `seo-technical`. Vérifier title, H1, réponse initiale, sous-intentions, entités, maillage, canonical, robots, données structurées si pertinentes et crawlabilité.

# 23. GEO

Vérifier verdict autonome, relations explicites produit → usage, critères lisibles, méthodologie résumable, tableaux interprétés, sources identifiables, entités complètes et datation des prix/informations instables.

Préférer « Le modèle A est le meilleur choix pour X parce que… » à « Le modèle A est le meilleur. »

# 24. Comparison Quality Gate

Le contrôle automatique peut vérifier présence d'une méthodologie, fichier de scoring, somme des poids = 100, produits classés présents dans les données, score justifié, source pour les critères majeurs, hard gates documentés, maillage, sources, tableaux contextualisés, limites et noindex si brouillon.

Il ne doit jamais déclarer automatiquement fact-check PASS, qualité du ranking PASS, Humanizer PASS, GEO PASS ou affiliation éthique PASS.

# 25. Échecs automatiques

FAIL si : gagnant choisi avant critères, poids modifiés pour produire un gagnant, commission dans le scoring, score sans justification, produit obsolète classé sans justification, hard gate ignoré, configurations non équivalentes comparées, fake test, avantage comparatif non vérifié, défauts significatifs masqués, données importantes sans date, page marchande déguisée, maillage quasi absent ou source de vérité non mise à jour.

# 26. Statuts

`UNIVERSE_READY`, `EVIDENCE_READY`, `SCORING_READY`, `DRAFT_READY`, `QA_IN_PROGRESS`, `REVISION_REQUIRED`, `HUMAN_APPROVED`, `PUBLISHABLE`.

Le ranking peut être `SCORING_READY` avant qu'une ligne éditoriale ne soit écrite.

# 27. Publication

Par défaut : conserver `noindex` si configuré ; ne pas merger, publier ou déployer. Autorisation explicite nécessaire.

# 28. Fichiers persistants

Pour chaque comparatif, `.content/comparisons/<slug>.json` doit conserver intent, univers, exclusions, critères, poids, hard gates, evidence ledger, scores, classement, niveau de confiance et date de recherche.

Le texte final ne doit jamais être la seule source expliquant pourquoi le ranking existe.
