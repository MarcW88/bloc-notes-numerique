# Automatisation d'images — Draw Things + GitHub

Cette intégration génère des images **localement sur le Mac** avec Draw Things. Elle n'utilise pas d'API d'image payante.

## Architecture

```text
Agent éditorial
  ↓
editorial-image-planner
  ↓
.content/image-requests/<page>.json
  ↓
GitHub Actions : validation légère sur ubuntu
  ↓ seulement si un travail est réellement requis
Runner self-hosted macOS
  ↓
Draw Things HTTP API sur localhost:7860
  ↓
assets/generated/*.png
  ↓
insertion dans le HTML + commit automatique
```

Une modification de page ne suffit pas à déclencher une génération. Une requête doit être explicitement approuvée avec `required: true`, `allow_ai_generation: true`, `truth_risk: LOW` et `status: PENDING` ou `REGENERATE`.

## Étape 1 — Draw Things

1. Ouvrir Draw Things sur le Mac.
2. Sélectionner le modèle local souhaité. Pour ce Mac 16 Go, FLUX.2 Klein 4B est le choix prévu par défaut.
3. Activer le serveur API local en mode HTTP.
4. Utiliser le port `7860`.
5. Laisser Draw Things ouvert pendant les générations.

Le workflow appelle :

```text
http://127.0.0.1:7860/sdapi/v1/txt2img
```

Les paramètres par défaut du projet sont volontairement prudents : 768×512, 4 steps, une image à la fois.

## Étape 2 — enregistrer le Mac comme runner GitHub

Dans le dépôt GitHub :

`Settings → Actions → Runners → New self-hosted runner`

Choisir :

- macOS ;
- ARM64 pour un Mac Apple Silicon.

GitHub affiche ensuite quelques commandes spécifiques au dépôt. Les exécuter dans Terminal sur le Mac. Ces commandes contiennent un token temporaire ; ne pas le stocker dans le dépôt.

Une fois configuré, démarrer le runner avec la commande indiquée par GitHub. Le workflow recherche les labels standards :

```text
self-hosted, macOS, ARM64
```

Le runner et Draw Things doivent être actifs au moment où une génération est nécessaire. Les pushes qui n'ont aucune image à générer ou réinsérer restent sur le job GitHub léger et ne mobilisent pas le Mac.

## Étape 3 — créer une requête d'image

Utiliser :

`.agents/skills/editorial-image-planner/SKILL.md`

Puis copier :

`.content/image-requests/_template.json`

vers un fichier comme :

`.content/image-requests/prise-de-notes-reunion-editorial.json`

Exemple minimal :

```json
{
  "id": "prise-de-notes-reunion-editorial",
  "page": "usages/prise-de-notes-reunion/index.html",
  "slot": "editorial",
  "required": true,
  "reason": "Montrer le contexte réel d'une réunion sans prétendre représenter un produit précis.",
  "allow_ai_generation": true,
  "truth_risk": "LOW",
  "status": "PENDING",
  "marker": "<!-- EDITORIAL_IMAGE:prise-de-notes-reunion-editorial -->",
  "output_path": "assets/generated/prise-de-notes-reunion-editorial.png",
  "prompt": "Photorealistic editorial photograph of a professional taking handwritten notes on a generic unbranded E Ink tablet during a small meeting, realistic office, natural window light, candid documentary framing, realistic proportions and materials, no readable text, no logo, no watermark, no CGI look",
  "negative_prompt": "readable text, logo, watermark, brand name, distorted hands, deformed objects, CGI, illustration",
  "alt": "Prise de notes sur une tablette E Ink générique pendant une réunion",
  "caption": "",
  "width": 768,
  "height": 512,
  "steps": 4,
  "guidance_scale": 1.0,
  "seed": -1,
  "batch_count": 1,
  "generated_at": null
}
```

Le marqueur doit aussi être ajouté à la **source de vérité** qui génère la page :

```html
<!-- EDITORIAL_IMAGE:prise-de-notes-reunion-editorial -->
```

## Ce qui se passe ensuite

Au push sur `main` :

1. le job `plan` valide les JSON ;
2. s'il n'y a rien à faire, le workflow s'arrête ;
3. si une requête est `PENDING`, le job local démarre sur le Mac ;
4. Draw Things génère une seule image ;
5. le PNG est enregistré sous `assets/generated/` ;
6. le marqueur est remplacé dans le HTML par un `<figure>` responsive ;
7. la requête passe à `GENERATED` ;
8. GitHub commit les changements avec `[skip ci]` pour éviter une boucle.

Si une régénération ultérieure du site remet le marqueur dans le HTML, le script voit que le PNG existe déjà et le réinsère sans refaire tourner le modèle.

## Régénérer une image

Changer simplement :

```json
"status": "REGENERATE"
```

puis pousser le fichier. Le PNG existant sera remplacé.

## Cas à bloquer

Pour une image qui devrait montrer un vrai produit, une interface exacte, un logo, un résultat de test ou une preuve hands-on :

```json
"required": true,
"allow_ai_generation": false,
"status": "BLOCKED"
```

La demande reste documentée mais Draw Things ne génère rien.

## Exécution manuelle

Le workflow peut aussi être lancé depuis :

`Actions → Generate approved editorial images with Draw Things → Run workflow`

En local dans le dépôt :

```bash
python3 scripts/generate_drawthings_images.py --check-only
python3 scripts/generate_drawthings_images.py
```

La deuxième commande nécessite que Draw Things et son serveur HTTP soient actifs.
