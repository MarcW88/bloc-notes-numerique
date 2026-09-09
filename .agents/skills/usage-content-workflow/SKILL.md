---
name: usage-content-workflow
description: Pré-analyser, rédiger et valider les pages SEO/GEO sous /usages/ de bloc-notes-numeriques.fr. Utiliser pour les pages centrées sur un contexte ou un job-to-be-done : étudiant, professionnel, réunion, annotation PDF, lecture, dessin, remplacement du papier, etc. Ne pas utiliser pour classer des produits, expliquer une technologie ou rédiger une page de marque.
---

# Usage Content Workflow

## Objectif

Produire des pages `/usages/` qui expliquent **dans quelles situations un bloc-notes numérique est pertinent, quelles contraintes changent réellement l'expérience et quel type de solution convient**, sans transformer la page en comparatif produit déguisé.

Principe de séparation :

- `/usages/` = comprendre le besoin, le workflow et les critères ;
- `/comparatifs/` = choisir et classer des produits ;
- `/guides/` = expliquer une technologie, un critère ou une procédure ;
- `/marques/` = documenter un écosystème, une gamme ou un produit.

Une page usage doit rester utile même si aucun produit précis n'est cité.

## Entrées obligatoires

Lire avant toute production :

- `AGENTS.md` et `DESIGN.md` ;
- `.agents/skills/jobs-to-be-done/SKILL.md` ;
- la page cible et `_generate.py` ;
- l'analyse sémantique du projet si elle est accessible ;
- les autres pages `/usages/` ;
- les guides, comparatifs et pages marques susceptibles de répondre à une sous-question ;
- `/guides/prix-bloc-notes-numerique/` comme référence de profondeur et de valeur décisionnelle, sans en copier la structure.

Créer ou mettre à jour `.content/usages/<slug>.json` avant la rédaction.

## Étape 1 — Définir le rôle exact de la page

Documenter :

- URL et requête principale ;
- intention dominante ;
- situation ou contexte central ;
- niveau de maturité du lecteur ;
- résultat attendu ;
- page comparative la plus proche ;
- guides proches ;
- risque de cannibalisation.

### Gate anti-cannibalisation

Une page usage ne doit pas répondre à « quel modèle est le meilleur ? » par un classement.

Exemple :

- `/usages/prise-de-notes-etudiant/` explique les situations d'étude, workflows, contraintes, critères et types de solutions ;
- `/comparatifs/bloc-notes-numerique-etudiant/` compare et classe des modèles pour ces critères.

Si les deux pages pourraient conserver le même H1, le même tableau central et la même conclusion en changeant seulement quelques mots, le cadrage échoue.

## Étape 2 — Analyse JTBD

Utiliser `jobs-to-be-done` avant toute sélection de produit.

Pour le job principal et les jobs secondaires, documenter :

1. **Circumstances** — quand, où et avec quels supports le besoin apparaît ;
2. **Progress** — progrès recherché ;
3. **Outcome** — résultat concret attendu ;
4. **Functional jobs** ;
5. **Emotional jobs** ;
6. **Social jobs** ;
7. **Push / Pull / Anxiety / Habit** ;
8. **Current hires** — papier, ordinateur, tablette LCD, smartphone, liseuse, impression, bricolages, non-consommation ;
9. **Big Hire / Little Hire** — achat initial vs usage répété.

Ne pas transformer « étudiant », « professionnel » ou « dessinateur » en pseudo-persona générique. Les circonstances priment sur les attributs démographiques.

### Gate de preuve JTBD

Sans interview utilisateur ou donnée comportementale, les dimensions émotionnelles/sociales et certains pains restent des hypothèses éditoriales. Les enregistrer comme `HYPOTHESIS` ou `INFERRED`. Ne jamais écrire « les étudiants veulent… » sans preuve suffisante.

## Étape 3 — Cartographier le workflow réel

Décomposer le job en séquence d'usage, par exemple :

- entrée : recevoir/importer un document ou ouvrir un carnet ;
- travail : écrire, annoter, lire, dessiner ;
- organisation : classer, retrouver, lier, rechercher ;
- sortie : exporter, partager, imprimer ou synchroniser ;
- continuité : reprendre le travail sur un autre appareil ou quelques jours plus tard.

Pour chaque étape, noter :

- tâche ;
- friction actuelle ;
- conséquence si elle échoue ;
- caractéristique ou capacité qui peut réduire cette friction ;
- niveau de preuve.

Le workflow réel sert à éviter les listes de fonctionnalités sans relation avec l'usage.

## Étape 4 — Transformer le job en critères

Classer chaque critère :

- `MUST_HAVE` ;
- `HIGH` ;
- `CONDITIONAL` ;
- `LOW` ;
- `CONTRAINDICATION`.

Chaque critère doit expliquer **ce qu'il change dans le job**.

Exemples possibles : taille d'écran, poids, annotation PDF, latence, organisation, OCR, recherche, cloud, applications, autonomie, couleur, export, abonnement, coût total.

Ne pas attribuer de score produit dans cette étape.

## Étape 5 — Définir les familles de solutions adaptées

La page usage peut distinguer des types de solutions, par exemple :

- appareil minimaliste centré sur l'écriture ;
- appareil ouvert avec applications ;
- grand écran orienté PDF ;
- appareil couleur ;
- liseuse avec prise de notes ;
- tablette LCD classique ;
- papier ou solution hybride.

Pour chaque famille :

- quand elle est pertinente ;
- ce qu'elle résout bien ;
- sa friction principale ;
- quand elle devient un mauvais choix.

Ne pas transformer cette section en podium de produits. Si un classement devient utile, créer un handoff explicite vers `comparison-content-workflow`.

## Étape 6 — Registre de preuves

Pour les affirmations vérifiables, conserver dans le fichier usage :

- claim ;
- source ;
- date ;
- stabilité ;
- evidence class.

Classes : `OBSERVED`, `SUPPORTED`, `INFERRED`, `HYPOTHESIS`, `UNKNOWN`.

Pour les capacités produit ou logiciel susceptibles d'évoluer, privilégier les sources officielles et dater la vérification.

## Étape 7 — Architecture éditoriale

Une page usage complète peut suivre cette logique, à adapter au sujet :

1. réponse initiale autonome ;
2. dans quelles situations cet usage justifie un bloc-notes numérique ;
3. workflow réel et frictions ;
4. critères réellement déterminants ;
5. critères secondaires ou surévalués ;
6. familles de solutions adaptées ;
7. situations où un bloc-notes numérique n'est pas le bon outil ;
8. comment arbitrer selon les variantes du job ;
9. prochaine étape : guides et comparatifs pertinents ;
10. sources.

### Règles de profondeur

- Un H2 important doit définir, expliquer et relier le point au job.
- Un tableau doit être introduit puis interprété.
- Une liste de critères sans hiérarchie ni conséquence pratique est insuffisante.
- Les contre-indications doivent être aussi visibles que les bénéfices.
- La page ne doit pas être une succession artificielle de sections symétriques.

## Étape 8 — Rédaction

Rédiger uniquement après création du fichier `.content/usages/<slug>.json`.

- Répondre au job principal dès les premières phrases.
- Employer un français naturel, précis et sobre.
- Expliquer les compromis plutôt que promettre un appareil « idéal ».
- Distinguer faits, déductions et hypothèses.
- Ne jamais inventer expérience, test, prix, autonomie mesurée ou avis utilisateur.
- Conserver `noindex,follow` pendant toute la phase de brouillon.
- Intégrer le contenu dans `_generate.py` ou un module explicitement importé par `_generate.py`, puis régénérer les pages. Ne pas éditer uniquement le HTML généré.

## Étape 9 — Handoff vers les autres workflows

### Vers `guide-content-workflow`

Utiliser lorsqu'une sous-question mérite une explication autonome : fonctionnement E Ink, OCR, export, synchronisation, taille d'écran, prix, latence, etc.

### Vers `comparison-content-workflow`

Utiliser dès qu'il faut :

- constituer un univers produit ;
- attribuer des critères pondérés ;
- scorer ;
- classer ;
- désigner un « meilleur » modèle.

Le fichier usage peut fournir les critères et contraintes au comparatif, mais ne doit pas stocker un ranking produit comme source de vérité.

### Vers `brand-content-workflow`

Utiliser lorsqu'une question porte principalement sur un écosystème ou une marque.

## Étape 10 — Chaîne de contrôle obligatoire

Après rédaction, exécuter distinctement :

1. `content-refresh` adapté au neuf ;
2. `search-intent` ;
3. `affiliate-value` si la page influence l'achat ;
4. `fact-check` ;
5. `natural-writing` ;
6. `internal-linking-audit` ;
7. `humanizer` ;
8. `general-writing` ;
9. `anti-ai-slop` ;
10. `seo-drift` en comparant le fichier usage, le brouillon initial et la version finale ;
11. `seo-technical` ;
12. `seo-best-practices` ;
13. contrôle GEO ;
14. `editorial-qa` ;
15. lecture complète dans l'ordre rendu.

Le contrôle final doit vérifier en plus :

- que le job n'a pas été remplacé par une liste de specs ;
- que les circonstances sont encore visibles ;
- que les critères restent hiérarchisés ;
- que les contre-indications n'ont pas disparu ;
- que la page ne s'est pas transformée en comparatif.

## Échecs automatiques

Attribuer `FAIL` si :

- le job est formulé uniquement comme « trouver le meilleur bloc-notes pour X » ;
- la page repose surtout sur des caractéristiques démographiques ;
- une motivation utilisateur hypothétique est présentée comme un fait ;
- les critères viennent des produits plutôt que du workflow réel ;
- les alternatives hors E Ink ne sont jamais envisagées ;
- la page classe des produits sans passer par le workflow comparatif ;
- les contre-indications sont absentes ;
- la page usage cannibalise manifestement un comparatif ou un guide ;
- des affirmations produit instables sont non sourcées ;
- le maillage ne mène pas vers les prochaines étapes utiles ;
- `noindex` est retiré sans validation humaine.

## Statuts

- `JTBD_READY` ;
- `EVIDENCE_READY` ;
- `DRAFT_READY` ;
- `QA_IN_PROGRESS` ;
- `REVISION_REQUIRED` ;
- `HUMAN_APPROVED` ;
- `PUBLISHABLE`.

`PUBLISHABLE` exige une validation humaine explicite et le passage des contrôles techniques. Ne pas merger/indexer une page uniquement parce que son fichier usage est complet.
