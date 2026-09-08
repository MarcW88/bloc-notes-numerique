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
- les autres pages du cluster afin d’éviter cannibalisation et répétitions.

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

Intégrer le contenu dans `_generate.py`, puis régénérer les pages. Ne pas éditer seulement le HTML généré.

## Étape 4 — Contrôles

Vérifier avant remise :

### Exactitude

- chaque information instable possède une source officielle récente ;
- aucune extrapolation n’est présentée comme une donnée mesurée ;
- les limites, exceptions et différences de version sont explicites ;
- les liens et intitulés de sources correspondent réellement aux affirmations.

### SEO

- intention satisfaite sans détour ;
- title, H1 et description distincts et naturels ;
- aucune concurrence évidente avec une autre URL du site ;
- hiérarchie H2/H3 logique, canonical correct et liens internes fonctionnels ;
- vocabulaire secondaire couvert selon son utilité, sans quota ni répétition forcée.

### GEO

- réponse initiale autonome et factuelle ;
- définitions, critères et procédures extractibles hors contexte ;
- sujets et entités nommés explicitement lorsque les pronoms créeraient une ambiguïté ;
- tableaux accompagnés d’une interprétation textuelle ;
- sources primaires identifiables et date de vérification visible.

### Qualité éditoriale

- absence de formules creuses, superlatifs automatiques et transitions mécaniques ;
- pas de paragraphes uniformes ni de succession artificielle de listes ;
- conclusion utile, sans résumé répétitif ni CTA affilié agressif ;
- distinction claire entre analyse documentaire et essai réel.

### Technique

- génération réussie ;
- HTML valide dans les limites du projet ;
- absence de liens internes cassés et d’ancres factices ;
- rendu mobile et desktop vérifié lorsque l’environnement le permet.

## Étape 5 — Statut et validation humaine

Renseigner le brief avec l’un des statuts suivants :

- `BRIEF_READY` : pré-analyse terminée, rédaction non commencée ;
- `DRAFT_READY` : contenu intégré, contrôles automatiques passés ;
- `REVISION_REQUIRED` : problème documenté à corriger ;
- `HUMAN_APPROVED` : validation explicite de l’utilisateur ;
- `PUBLISHABLE` : validation humaine obtenue et exigences techniques passées.

Ne pas retirer `noindex`, publier, fusionner ou déployer sans demande explicite. Une validation d’un lot ne vaut que pour les pages clairement énumérées.

## Traçabilité

Dans le brief, conserver les sources consultées, les décisions de structure, les affirmations exclues faute de preuve et les contrôles effectués. Ne pas stocker de longs extraits protégés ; résumer et conserver les URL.

Ce workflow adapte des principes courants de pipelines éditoriaux publics (séparation recherche/rédaction/QA, validation humaine, contrôles SEO/GEO) aux contraintes propres au site. Les règles de ce dépôt prévalent toujours.
