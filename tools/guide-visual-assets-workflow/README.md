# Guide Visual Assets Workflow

Workflow portable et hybride pour enrichir les pages guides avec le bon type de visuel, sans imposer un SVG à chaque page.

## Principe

Chaque guide est routé vers l'un de ces trois modes :

- `editorial_image` : image générique / éditoriale de contexte ;
- `functional_diagram` : schéma utile pour un mécanisme, une décision ou une circulation ;
- `no_visual` : aucun visuel si rien n'apporte de valeur réelle.

Le workflow préfère une image éditoriale pour le visuel principal d'un guide et réserve les diagrammes aux cas où la structure elle-même doit être visualisée.

## Règles fortes

- ne jamais transformer un tableau HTML en image ;
- ne jamais générer une matrice comparative en SVG ;
- ne pas recopier une liste sous forme de visuel ;
- ne pas inventer de produit, logo, interface, prix, mesure ou test ;
- une image éditoriale ne doit pas être utilisée comme preuve factuelle ;
- `no_visual` est une sortie valide ;
- conserver le statut d'indexation existant.

## Images éditoriales

Usage recommandé : hero ou respiration éditoriale.

Direction par défaut :

- appareil E Ink générique non brandé ;
- environnement de travail, étude, lecture ou annotation ;
- composition simple et crédible ;
- aucun texte dans l'image ;
- aucun logo ;
- pas de faux screenshot ;
- pas de copie approximative d'un modèle réel ;
- ratio horizontal `16:9` ou `3:2` ;
- `webp` en priorité.

## Diagrammes fonctionnels

Types autorisés :

- `decision_tree`
- `process_flow`
- `size_comparison`
- `cost_breakdown`
- `checklist`
- `timeline`
- `ecosystem_map`

Les diagrammes sont générés depuis des manifests versionnés et restent régénérables.

## Installation

Copier ce dossier dans le repo cible et créer les manifests sous :

`.content/visuals/`

## Manifest

Le manifest est la source de vérité.

Exemple `editorial_image` :

```json
{
  "page_url": "/guides/choisir-bloc-notes-numerique/",
  "asset_mode": "editorial_image",
  "visual_goal": "contextualiser le choix d'un bloc-notes numérique dans un environnement de travail",
  "placement": "hero",
  "aspect_ratio": "3:2",
  "prompt": "Editorial photograph of a generic unbranded e-paper writing tablet with stylus on a calm modern desk, natural daylight, premium magazine aesthetic, no logos, no readable text, no identifiable commercial product",
  "negative_constraints": [
    "no logos",
    "no readable text",
    "no fake UI",
    "no recognizable branded product"
  ],
  "output": "assets/guides/choisir-bloc-notes-numerique/hero.webp",
  "alt": "Tablette à encre électronique générique et stylet sur un bureau de travail."
}
```

Exemple `functional_diagram` :

```json
{
  "page_url": "/guides/annoter-pdf-tablette-e-ink/",
  "asset_mode": "functional_diagram",
  "type": "process_flow",
  "visual_goal": "montrer le parcours d'un PDF de l'import jusqu'à la vérification du fichier exporté",
  "output": "assets/guides/annoter-pdf-tablette-e-ink/pdf-workflow.svg",
  "alt": "Schéma du parcours d'un PDF importé, annoté, exporté puis vérifié."
}
```

Exemple `no_visual` :

```json
{
  "page_url": "/guides/example/",
  "asset_mode": "no_visual",
  "reason": "la page contient déjà les représentations nécessaires et aucun visuel complémentaire n'améliore la compréhension"
}
```

## QA

Le contrôle doit vérifier le mode choisi et non exiger automatiquement une image sur chaque page.

Le skill complet se trouve dans `SKILL.md`.
