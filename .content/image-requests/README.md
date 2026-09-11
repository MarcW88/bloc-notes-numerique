# Requêtes d'images éditoriales

Ce dossier pilote la génération d'images éditoriales via l'API Black Forest Labs (BFL / FLUX.2).

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
5. Le job GitHub Actions appelle BFL avec le secret `BFL_API_KEY`.
6. Le script suit le `polling_url` retourné par BFL jusqu'à ce que l'image soit prête.
7. L'image est téléchargée immédiatement dans `assets/generated/`.
8. Le marqueur du HTML généré est remplacé par un `<figure>`.
9. Le JSON passe à `GENERATED` et les changements sont commités automatiquement.

Si une régénération du site réintroduit le marqueur dans le HTML, le workflow réinsère l'image déjà existante sans relancer BFL et sans nouveau coût.

## Statuts

- `NOT_NEEDED` : aucune image n'apporte assez de valeur.
- `BLOCKED` : une image serait utile mais une génération IA serait trompeuse ou insuffisamment fidèle ; utiliser une vraie photo, capture ou source officielle.
- `PENDING` : génération BFL autorisée et à lancer.
- `GENERATED` : image générée et disponible dans le dépôt.
- `REGENERATE` : forcer une nouvelle génération lors de la prochaine exécution.

## Paramètres

Le modèle par défaut est `FLUX.2 [pro] preview` via `https://api.bfl.ai/v1/flux-2-pro-preview`.

Par défaut :

- 1024 × 672 px ;
- `prompt_upsampling: true` ;
- `seed: null` pour une génération aléatoire ;
- format déterminé par l'extension de `output_path` (`png`, `jpg/jpeg` ou `webp`).

FLUX.2 n'utilise pas de negative prompt : écrire directement dans le prompt ce que l'image doit contenir et la manière dont elle doit être rendue.

## Garde-fous

Ne pas utiliser la génération IA comme représentation fidèle d'un produit précis, d'une interface, d'un logo, d'un benchmark, d'un résultat de test ou d'une expérience hands-on. Les images générées doivent rester des illustrations éditoriales génériques et plausibles.

Par défaut, limiter à zéro ou une image générée par page.
