---
name: guide-content-workflow
description: Pré-analyser, rédiger et valider les guides SEO/GEO de bloc-notes-numeriques.fr. Utiliser pour toute création ou réécriture sous /guides/, avec recherche documentaire, choix du format éditorial, brief persistant, rédaction HTML et contrôle avant indexation. Ne pas utiliser pour les comparatifs, tests produits, pages de marque ou bons plans.
---

# Workflow de production des guides

Produire des guides utiles et vérifiables sans simuler une expérience produit. Le workflow sépare obligatoirement la pré-analyse de la rédaction afin que les décisions éditoriales restent auditables.

## Entrées

Lire avant de commencer :

- `AGENTS.md` et `DESIGN.md` ;
- la page cible et `_generate.py` ;
- l’analyse sémantique fournie pour le projet, si elle est accessible ;
- les autres pages du cluster afin d’éviter cannibalisation et répétitions ;
- `/guides/prix-bloc-notes-numerique/` comme référence de profondeur éditoriale et de valeur décisionnelle.

Identifier l’URL, le mot-clé principal, l’intention, le public, la place dans le cluster et les liens internes attendus. Si une donnée essentielle manque, faire une hypothèse prudente et la consigner dans le brief.

## Étape 1 — Router le guide

Choisir un seul type dominant puis lire la référence correspondante :

- **Choix et arbitrage** : aide à décider entre options, formats ou budgets. Lire `references/choice-guide.md`.
- **Explication technique** : explique une technologie, une mesure ou une contrainte. Lire `references/explainer-guide.md`.
- **Tutoriel et compatibilité** : décrit une procédure, un transfert ou une intégration. Lire `references/how-to-guide.md`.

Un guide peut contenir des sections secondaires d’un autre type, mais son architecture suit son intention dominante.

## Étape 2 — Pré-analyse

Effectuer la pré-analyse avant toute rédaction :

1. **Demande** : regrouper les variantes réellement pertinentes du fichier sémantique ; écarter les termes hors sujet même si leur volume est élevé.
2. **Intentions** : expliciter la question centrale, les sous-questions et le résultat attendu par le lecteur.
3. **SERP** : examiner les résultats actuels, formats dominants, angles récurrents et lacunes. Ne pas déduire une exigence éditoriale du seul nombre de concurrents qui l’emploient.
4. **Entités** : lister technologies, formats, services, marques et concepts à définir ou comparer.
5. **Preuves** : construire un registre des affirmations avec source, date de consultation, portée et niveau de stabilité.
6. **Différenciation** : formuler la valeur propre de la page en une phrase. Privilégier tableaux de décision, limites concrètes, procédures vérifiables et cas d’usage.
7. **Architecture** : proposer H1, réponse courte initiale, H2/H3, tableau ou étapes lorsque cela améliore réellement la compréhension, FAQ non redondante et liens internes.
8. **Risques** : signaler cannibalisation, données instables, dépendance à une marque, absence de preuve ou besoin de test réel.

Enregistrer le résultat dans `.content/briefs/<slug>.md` selon `references/brief-template.md`. Arrêter après le brief si la demande porte uniquement sur la pré-analyse.

## Étape 3 — Rédaction

Rédiger uniquement à partir du brief validé ou, si l’utilisateur a demandé explicitement la chaîne complète, du brief qui vient d’être produit.

- Répondre à la question principale dans les premières phrases.
- Employer un français naturel, précis et sobre ; varier les longueurs de phrase sans artifices conversationnels.
- Donner à chaque H2 une fonction distincte et une ouverture compréhensible isolément.
- Définir les termes avant de les comparer ou de les utiliser.
- Séparer les faits vérifiés, les déductions éditoriales et les éléments à confirmer.
- Citer les sources au plus près des affirmations importantes dans une section `Sources` visible.
- Ne jamais inventer prix, autonomie mesurée, latence, compatibilité, test, classement ou expérience personnelle.
- Ne pas ajouter de FAQ pour répéter mot pour mot le corps du texte.
- Ajouter des liens internes uniquement lorsqu’ils aident à poursuivre la décision.
- Conserver `noindex,follow` pendant la phase de brouillon.

Intégrer le contenu dans `_generate.py` ou dans un module explicitement chargé par `_generate.py`, puis régénérer les pages. Ne pas éditer seulement le HTML généré.

## Quality floor obligatoire — référence guide Prix

`/guides/prix-bloc-notes-numerique/` sert de **plancher qualitatif**, pas de gabarit de longueur identique. Une page plus étroite peut être plus courte, mais elle doit offrir le même niveau de contextualisation et d’utilité.

### Une section H2 doit être une unité sémantique complète

- Ne pas publier un H2 important suivi d’un seul petit paragraphe générique.
- Définir ou contextualiser le concept, expliquer son impact et, lorsque pertinent, donner un exemple, une limite ou une conséquence pratique.
- Une section mono-paragraphe n’est acceptable que si le paragraphe est réellement développé et que le sujet ne justifie pas davantage.
- Un H2 ne doit pas exister uniquement pour placer une variante de mot-clé.

### Les tableaux, listes et procédures doivent être interprétés

- Introduire un tableau avant de l’afficher : expliquer ce qu’il compare et pourquoi.
- Ajouter après le tableau une interprétation ou une règle de décision ; ne jamais laisser le tableau conclure seul la section.
- Une procédure doit préciser le résultat attendu, les limites et l’étape suivante utile.

### Profondeur sémantique et entités

- Couvrir les entités du brief lorsqu’elles améliorent réellement la compréhension : technologies, formats, services, marques et concepts associés.
- Pour un sujet transversal, utiliser plusieurs écosystèmes lorsque cela évite de transformer le guide en page d’une seule marque.
- Relier mécanisme et décision : une caractéristique technique doit expliquer ce qu’elle change pour le lecteur.
- Inclure cas limites, contre-indications et situations où le critère devient secondaire.

### Maillage et valeur commerciale

- Construire un parcours réel dans le cluster : guides connexes, usages, marques et comparatifs lorsqu’ils constituent une prochaine étape naturelle.
- Les guides proches de l’achat doivent déboucher vers au moins une étape transactionnelle pertinente sans se transformer eux-mêmes en classement.
- Ne pas ajouter des liens pour un quota ; en revanche une page presque sans maillage interne est considérée comme incomplète.

### Gate structurel

`validate_guide_quality.py` matérialise le plancher observable : profondeur du corps d’article, nombre de sections substantielles, développement des H2, contextualisation des tableaux, diversité du maillage et présence de sources. Ces seuils sont des garde-fous, jamais un substitut à la relecture éditoriale.

Un CI vert ne prouve pas que `humanizer`, `fact-check`, `anti-ai-slop`, SEO ou GEO sont passés. **Aucun de ces contrôles ne peut recevoir `PASS` automatiquement sur la seule base de H1/H2, nombre de mots ou présence d’une source.** Chaque verdict qualitatif doit être fondé sur une passe réellement effectuée et sur des constats visibles dans `.content/reviews/<slug>.md`.

## Étape 4 — Chaîne de contrôle obligatoire après rédaction

Appliquer la même chaîne de finition que pour les `/koopgids/` d’italiaanse-percolator.nl, sans le diagnostic GSC. Chaque passe est distincte. Ne pas déclarer plusieurs contrôles effectués après une simple relecture globale.

1. **`content-refresh` adapté au contenu neuf** : comparer le brief validé au brouillon. Conserver les passages utiles, corriger les lacunes et éviter une réécriture totale sans raison. Produire la liste de ce qui reste, change ou manque.
2. **`search-intent`** : vérifier requête principale, intention, fonction de page, réponse attendue et risque de cannibalisation.
3. **`affiliate-value` lorsque le guide influence un achat** : la page doit rester utile si tous les liens affiliés disparaissent. Vérifier critères, limites, alternatives et niveau de preuve.
4. **`fact-check`** : extraire les affirmations vérifiables dans une passe séparée. Attribuer `CONFIRMED`, `PARTIAL`, `UNVERIFIED`, `CONTRADICTED` ou `OUTDATED`, puis corriger le brouillon.
5. **`natural-writing`** : supprimer seulement les formulations réellement génériques, répétitives ou promotionnelles sans modifier les faits ni l’intention.
6. **`internal-linking-audit`** : vérifier chaque lien existant, les prochaines étapes utiles, les ancres et la présence réelle des cibles. Ne pas ajouter de liens pour atteindre un quota.

### Finition éditoriale obligatoire

Exécuter ensuite, dans cet ordre :

7. **`humanizer` en mode embedded/file** : relire l’intégralité du contenu visible, y compris title, introduction, titres, tableaux, encadrés, libellés et conclusion. Préserver faits, sources, liens et distinctions techniques. Appliquer aussi ses dépendances `better-usage`, `academic-voice`, `writing-cadence` et `non-autoregressive-writing-pass`.
8. **`general-writing`** : passe de style globale avec le minimum de modifications nécessaires. Contrôler cohérence de la voix, transitions, titres, appels et équilibre des sections.
9. **`anti-ai-slop`** : audit de crédibilité fondé sur des passages précis. Chaque constat doit citer le fragment, expliquer le défaut et proposer une correction. Ne jamais prétendre détecter l’origine IA du texte.
10. **`seo-drift` adapté au neuf** : comparer le brief validé, le premier brouillon et la version finale. Documenter toute perte d’intention, de terme utile, de source, de lien, de tableau ou de nuance. Une suppression inexpliquée entraîne un échec.

### Contrôles techniques et gate final

11. **`seo-technical`** : vérifier canonical, robots, balisage, titres, liens, données structurées éventuelles, crawlabilité et HTML généré.
12. **`seo-best-practices`** : vérifier satisfaction de l’intention, title/H1, structure, entités, lisibilité, maillage et absence de sur-optimisation.
13. **Contrôle GEO** : vérifier réponse initiale autonome, définitions et procédures extractibles, entités explicites, tableaux interprétés et sources primaires identifiables.
14. **`editorial-qa`** : rendre le verdict final `PASS` ou `FAIL`. En cas de `FAIL`, nommer le gate bloquant et revenir uniquement à la passe concernée.
15. **Lecture complète en ordre rendu** : lire la page de haut en bas après la dernière modification, en mobile et desktop lorsque le rendu est disponible. Rechercher contradictions voisines, ton recousu, répétitions, avertissements défensifs, pseudo-précision et sections trop symétriques.

Consigner chaque passe dans `.content/reviews/<slug>.md` selon `references/publish-gate-template.md`. L’absence de rapport complet interdit le statut `PUBLISHABLE`.

## Échecs automatiques

Attribuer `FAIL` si l’un des points suivants subsiste :

- expérience directe, test, auteur ou mesure inventés ;
- recommandation plus forte que les preuves ;
- affirmation importante non vérifiée présentée comme certaine ;
- contradictions entre sections ou versions de produit ;
- contenu principalement interchangeable avec une page concurrente ou marchande ;
- H2 important réduit à un fragment de contenu sans profondeur ni raison ;
- tableau ou liste posé sans contexte ni interprétation ;
- maillage presque absent alors que des prochaines étapes existent dans le cluster ;
- clusters de formulations génériques, promotionnelles ou mécaniques relevés par `anti-ai-slop` ;
- suppression inexpliquée d’un élément validé dans le brief ;
- nouvelle cannibalisation, lien interne cassé, canonical/robots incorrect ou HTML invalide ;
- page non relue intégralement dans l’ordre rendu.

## Étape 5 — Statut et validation humaine

Renseigner le brief avec l’un des statuts suivants :

- `BRIEF_READY` : pré-analyse terminée, rédaction non commencée ;
- `DRAFT_READY` : contenu intégré, contrôles automatiques passés ;
- `QA_IN_PROGRESS` : chaîne de contrôle en cours ;
- `REVISION_REQUIRED` : problème documenté à corriger ;
- `HUMAN_APPROVED` : validation explicite de l’utilisateur ;
- `PUBLISHABLE` : validation humaine obtenue et exigences techniques passées.

Ne pas retirer `noindex`, publier, fusionner ou déployer sans demande explicite. Une validation d’un lot ne vaut que pour les pages clairement énumérées.

## Traçabilité

Dans le brief, conserver les sources consultées, les décisions de structure, les affirmations exclues faute de preuve et les contrôles effectués. Ne pas stocker de longs extraits protégés ; résumer et conserver les URL.

Ce workflow adapte des principes courants de pipelines éditoriaux publics (séparation recherche/rédaction/QA, validation humaine, contrôles SEO/GEO) aux contraintes propres au site. Les règles de ce dépôt prévalent toujours.
