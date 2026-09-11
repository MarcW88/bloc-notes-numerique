# Automatisation d'images — BFL + GitHub Actions

Cette intégration génère des images éditoriales avec l'API Black Forest Labs (BFL) et FLUX.2 [pro]. Aucun Mac, runner self-hosted, ComfyUI ou Draw Things n'est nécessaire.

## Architecture

```text
Agent éditorial
  ↓
editorial-image-planner
  ↓
.content/image-requests/<page>.json
  ↓
GitHub Actions
  ↓ seulement si une image est explicitement approuvée
BFL FLUX.2 [pro] API
  ↓
assets/generated/*
  ↓
insertion dans le HTML + commit automatique
```

Une modification de page ne suffit pas à déclencher une génération. Une requête doit être explicitement approuvée avec `required: true`, `allow_ai_generation: true`, `truth_risk: LOW` et `status: PENDING` ou `REGENERATE`.

## Secret GitHub

Le dépôt attend un secret Actions nommé exactement :

```text
BFL_API_KEY
```

Il se configure dans :

`Settings → Secrets and variables → Actions → Repository secrets`

La clé n'est jamais écrite dans le dépôt ni affichée dans les logs par le script.

## Modèle et endpoint

Le workflow utilise par défaut :

```text
https://api.bfl.ai/v1/flux-2-pro-preview
```

Le modèle peut être changé en modifiant `BFL_API_URL` dans `.github/workflows/generate-editorial-images.yml`.

## Créer une requête

Utiliser `.agents/skills/editorial-image-planner/SKILL.md`, puis copier `.content/image-requests/_template.json` vers un fichier comme :

`.content/image-requests/prise-de-notes-reunion-editorial.json`

Exemple :

```json
{
  "id": "prise-de-notes-reunion-editorial",
  "page": "usages/prise-de-notes-reunion/index.html",
  "slot": "editorial",
  "required": true,
  "reason": "Montrer un contexte réel de réunion sans prétendre représenter un produit précis.",
  "allow_ai_generation": true,
  "truth_risk": "LOW",
  "status": "PENDING",
  "marker": "<!-- EDITORIAL_IMAGE:prise-de-notes-reunion-editorial -->",
  "output_path": "assets/generated/prise-de-notes-reunion-editorial.png",
  "prompt": "Photorealistic editorial photograph of a professional taking handwritten notes on a generic unbranded E Ink tablet during a small meeting, realistic office, natural window light, candid documentary framing, realistic proportions and materials, blank or non-readable screen content, no visible logo or watermark",
  "alt": "Prise de notes sur une tablette E Ink générique pendant une réunion",
  "caption": "",
  "width": 1024,
  "height": 672,
  "prompt_upsampling": true,
  "seed": null,
  "generated_at": null
}
```

Le marqueur doit aussi exister dans la source de vérité qui génère la page :

```html
<!-- EDITORIAL_IMAGE:prise-de-notes-reunion-editorial -->
```

## Exécution

Au push sur `main` :

1. le job `plan` valide les requêtes sans utiliser la clé API ;
2. s'il n'y a rien à faire, le workflow s'arrête ;
3. si une requête est `PENDING` ou `REGENERATE`, le job `generate` appelle BFL ;
4. le script utilise le `polling_url` renvoyé par BFL jusqu'au statut `Ready` ;
5. l'URL signée du résultat est téléchargée immédiatement dans `assets/generated/` ;
6. le marqueur HTML est remplacé par un `<figure>` responsive ;
7. le JSON passe à `GENERATED` et conserve l'identifiant de requête BFL ;
8. GitHub commit les changements avec `[skip ci]`.

Si une régénération du site remet le marqueur dans le HTML, le script réutilise l'image existante sans appeler BFL et sans coût supplémentaire.

## Régénérer une image

Passer simplement la requête à :

```json
"status": "REGENERATE"
```

Le prochain run remplace l'image existante.

## Cas à bloquer

Pour une image qui devrait montrer un vrai produit, une interface exacte, un logo, un résultat de test ou une preuve hands-on :

```json
"required": true,
"allow_ai_generation": false,
"status": "BLOCKED"
```

La demande reste documentée mais aucune génération BFL n'a lieu.

## Exécution manuelle

Le workflow peut aussi être lancé depuis :

`Actions → Generate approved editorial images with BFL → Run workflow`

Le validateur peut être lancé localement sans clé :

```bash
python3 scripts/generate_bfl_images.py --check-only
```

La génération réelle nécessite `BFL_API_KEY` dans l'environnement ou le secret GitHub Actions.
