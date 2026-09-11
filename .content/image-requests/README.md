# Requêtes d'images éditoriales

Ce dossier pilote la génération locale d'images avec Draw Things.

## Principe

Aucune image n'est générée automatiquement à partir du simple fait qu'une page existe ou qu'elle a été modifiée. La décision éditoriale est faite en amont avec `.agents/skills/editorial-image-planner/SKILL.md`.

Le moteur ne traite que les fichiers JSON qui remplissent simultanément ces conditions :

- `required: true`
- `allow_ai_generation: true`
- `truth_risk: LOW`
- `status: PENDING` ou `status: REGENERATE`

Les requêtes `NOT_NEEDED` et `BLOCKED` sont ignorées.

## Cycle de vie

1. L'agent ou l'éditeur juge si l'image est réellement utile.
2. Il crée `.content/image-requests/<slug>-<slot>.json` à partir de `_template.json`.
3. Il place le `marker` dans la source de vérité de la page.
4. Le workflow GitHub détecte la requête.
5. Si un travail est nécessaire, le job de génération est envoyé au runner macOS local.
6. Le script appelle l'API HTTP locale de Draw Things.
7. L'image est enregistrée sous `assets/generated/`.
8. Le marqueur du HTML généré est remplacé par un `<figure>`.
9. Le JSON passe à `GENERATED` et les changements sont commités automatiquement.

Si une régénération du site réintroduit le marqueur dans le HTML, le workflow réinsère l'image déjà existante sans relancer Draw Things.

## Statuts

- `NOT_NEEDED` : aucune image n'apporte assez de valeur.
- `BLOCKED` : une image serait utile mais une génération IA serait trompeuse ou insuffisamment fidèle ; utiliser une vraie photo, capture ou source officielle.
- `PENDING` : génération locale autorisée et à lancer.
- `GENERATED` : image générée et disponible dans le dépôt.
- `REGENERATE` : forcer une nouvelle génération lors de la prochaine exécution.

## Garde-fous

Ne pas utiliser la génération IA comme représentation fidèle d'un produit précis, d'une interface, d'un logo, d'un benchmark, d'un résultat de test ou d'une expérience hands-on. Les images générées doivent rester des illustrations éditoriales génériques et plausibles.

Par défaut, limiter à zéro ou une image générée par page.
