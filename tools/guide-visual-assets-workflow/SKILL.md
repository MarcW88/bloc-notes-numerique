---
name: guide-visual-assets-workflow
description: Workflow hybride pour choisir, créer, intégrer et valider les visuels des pages guides. Le workflow route chaque page vers une image éditoriale générique, un schéma fonctionnel ou aucun visuel. Il privilégie les images éditoriales pour enrichir la lecture et réserve les SVG aux mécanismes, décisions ou relations qui gagnent réellement à être schématisés. Il interdit les tableaux redessinés, faux produits, faux screenshots, logos inventés et mesures non sourcées.
---

# Guide Visual Assets Workflow

## Objectif

Ajouter des visuels qui améliorent réellement la lecture, la compréhension ou la décision sans répéter le contenu déjà présent.

Le workflow ne part jamais du principe qu'un guide doit recevoir un SVG.

Principe :

> **contenu -> inventaire de l'existant -> besoin visuel -> routing -> production -> intégration -> QA**

## 1. Routing obligatoire

Chaque guide reçoit un `asset_mode` parmi :

- `editorial_image`
- `functional_diagram`
- `no_visual`

La décision doit être prise avant de choisir un format de fichier ou un type de rendu.

### `editorial_image`

À privilégier lorsque la page a surtout besoin de :

- respirer visuellement ;
- contextualiser un usage ;
- donner une présence éditoriale au guide ;
- matérialiser un environnement de travail, d'étude, de lecture ou de prise de notes ;
- illustrer un concept sans prétendre représenter un produit précis.

C'est le mode par défaut pour un visuel principal de guide lorsque aucun mécanisme ne nécessite un schéma.

Exemples :

- bureau sobre avec tablette E Ink générique et stylet ;
- scène de lecture et prise de notes ;
- document PDF annoté sur un appareil non brandé ;
- environnement étudiant ou professionnel ;
- illustration conceptuelle autour de la couleur, de la concentration, de l'autonomie ou du cloud.

### `functional_diagram`

À utiliser uniquement lorsqu'une représentation structurelle apporte une compréhension que l'image éditoriale ne peut pas fournir aussi clairement.

Types autorisés :

- `decision_tree`
- `process_flow`
- `size_comparison`
- `cost_breakdown`
- `checklist`
- `timeline`
- `ecosystem_map`

Exemples :

- circulation d'un PDF import -> annotation -> export ;
- OCR manuscrit -> correction -> réutilisation ;
- synchronisation appareil -> cloud -> ordinateur ;
- arbre de décision avec ou sans abonnement ;
- comparaison réellement spatiale de tailles d'écran.

### `no_visual`

À utiliser lorsque :

- le contenu est déjà suffisamment illustré ;
- le seul visuel possible répéterait un tableau, une liste ou un encadré ;
- une image générique serait seulement décorative ;
- aucune représentation complémentaire ne simplifie la compréhension.

`no_visual` est un résultat valide et ne doit jamais être traité comme un échec du workflow.

## 2. Priorité éditoriale

Pour le visuel principal d'un guide, appliquer cet ordre :

1. `editorial_image` si une image de contexte améliore réellement la page ;
2. `functional_diagram` si le sujet contient un mécanisme, une bifurcation ou une relation qui mérite un schéma ;
3. `no_visual` si aucune option n'ajoute de valeur.

Ne pas générer un diagramme uniquement parce qu'il est plus facile à automatiser.

## 3. Inventaire de l'existant

Avant toute génération, lire la page complète et inventorier :

- tableaux HTML ;
- listes ;
- checklists ;
- encadrés ;
- étapes ;
- illustrations existantes ;
- données chiffrées ;
- captures ou médias déjà présents.

Un nouveau visuel doit avoir une fonction distincte de ces éléments.

## 4. Règle de non-redondance

Un visuel est interdit s'il reproduit essentiellement la même information qu'un tableau HTML, une liste ou un encadré, même avec une mise en page différente.

Si la page possède déjà un tableau comparatif :

- conserver le tableau en HTML ;
- pour `editorial_image`, illustrer le contexte ou l'usage plutôt que les cellules du tableau ;
- pour `functional_diagram`, choisir un angle différent : chemin de décision, mécanisme, circulation d'un fichier, relation entre composants ou représentation spatiale ;
- sinon choisir `no_visual`.

`decision_matrix` et toute représentation tabulaire en image ou SVG sont interdites.

## 5. Règles `editorial_image`

Une image éditoriale ne doit pas être utilisée comme source factuelle.

### Autorisé

- appareils génériques non brandés ;
- scènes de travail réalistes mais non présentées comme un test ;
- bureaux, sacs, salles de cours, réunions, lecture, annotation ;
- stylisation éditoriale cohérente avec le design du site ;
- représentations conceptuelles légères.

### Interdit

- faux modèle identifiable ;
- copie approximative d'un reMarkable, Kindle, BOOX, Supernote ou Kobo présentée comme le vrai produit ;
- logo inventé ou déformé ;
- faux screenshot d'interface ;
- faux benchmark ;
- texte lisible généré dans l'image ;
- tableau ou infographie textuelle redessinée ;
- prix, autonomie, dimensions ou statistiques créés par l'image ;
- personne présentée comme ayant testé le produit si aucun test réel n'existe.

### Direction artistique par défaut

Sauf instruction contraire du site :

- style éditorial premium, sobre et crédible ;
- lumière naturelle ;
- palette neutre cohérente avec le site ;
- composition simple ;
- peu d'objets ;
- aucun texte intégré à l'image ;
- aucun logo ;
- aucun branding fabricant ;
- éviter l'esthétique stock-photo et le rendu publicitaire agressif ;
- préférer un cadrage horizontal pour les héros de guides.

### Format recommandé

- `webp` en priorité ;
- `png` si transparence ou besoin spécifique ;
- ratio recommandé hero : `16:9` ou `3:2` ;
- conserver une version source si le générateur le permet ;
- `alt` descriptif lié à la fonction éditoriale de l'image.

## 6. Règles `functional_diagram`

- ne jamais transformer un tableau en image ;
- ne pas ajouter de chiffre uniquement pour remplir un graphique ;
- utiliser seulement des affirmations déjà présentes et validées dans le contenu ou ses sources ;
- un arbre de décision doit contenir de vraies conditions ;
- un process flow doit montrer une séquence ou circulation non évidente ;
- une checklist visuelle doit hiérarchiser une vérification, pas recopier une liste mot pour mot ;
- une comparaison de tailles doit représenter une différence spatiale réelle ;
- le SVG doit rester lisible sur mobile grâce au `viewBox`.

## 7. Manifest

La source de vérité est `.content/visuals/<slug>.json`.

Champs communs :

```json
{
  "page_url": "/guides/example/",
  "asset_mode": "editorial_image",
  "visual_goal": "contextualiser la prise de notes en mobilité",
  "placement": "hero",
  "alt": "Tablette E Ink générique et stylet utilisés dans un environnement de travail sobre."
}
```

Pour `editorial_image`, ajouter notamment :

- `prompt` ;
- `negative_constraints` ;
- `aspect_ratio` ;
- `output` ;
- `style_reference` si disponible.

Pour `functional_diagram`, ajouter :

- `type` ;
- `title` ;
- `subtitle` ;
- les données nécessaires au type (`nodes`, `steps`, `layers`, etc.) ;
- `output`.

Pour `no_visual`, ajouter :

- `reason` ;
- éventuellement `revisit_if`.

## 8. Workflow de production

1. Lire la page complète et son brief.
2. Inventorier les représentations déjà présentes.
3. Définir le `visual_goal` en une phrase.
4. Router vers `editorial_image`, `functional_diagram` ou `no_visual`.
5. Vérifier la non-redondance.
6. Créer ou mettre à jour le manifest.
7. Produire l'asset selon son mode.
8. Intégrer dans une balise `<figure>` lorsque le visuel est dans le corps de page.
9. Ajouter `alt`, dimensions, lazy loading et légende si pertinente.
10. Vérifier le rendu mobile.
11. Exécuter la QA.
12. Conserver le robots meta existant et ne jamais publier/indexer automatiquement.

## 9. QA

### PASS seulement si

- le `visual_goal` est distinct d'un élément déjà présent ;
- le mode choisi est justifié ;
- l'image éditoriale n'introduit aucun faux fait ;
- le diagramme apporte une relation ou séquence réellement utile ;
- `alt` est présent ;
- le fichier existe ;
- la page reste accessible et responsive ;
- le `noindex` est conservé lorsqu'il est requis.

### FAIL si

- tableau ou matrice redessiné en image ;
- visuel qui duplique un tableau HTML existant ;
- image éditoriale avec faux produit identifiable ;
- logo ou interface inventé ;
- texte généré dans l'image utilisé comme information ;
- faux test ou fausse expérience ;
- donnée non sourcée ajoutée par le visuel ;
- diagramme choisi uniquement parce qu'il est automatisable ;
- image purement décorative sans `visual_goal` ;
- plusieurs copies du même visuel sont injectées ;
- page perd son `noindex` en brouillon.

## 10. Principe de publication

Le workflow visuel ne décide jamais de l'indexation ou de la publication.

Une image générée ou un diagramme validé peut être intégré dans une page `noindex,follow` sans changer son statut.
