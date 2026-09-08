# Guide Visual Assets Workflow

Portable, deterministic visual-generation workflow for editorial guides.

## Why

Use visuals to make decisions, workflows and comparisons easier to understand. Prefer deterministic SVGs over decorative AI images for the first layer of enrichment.

## Install

Copy this folder into any repository and create manifests under `.content/visuals/`.

## Pilot command

```bash
python tools/guide-visual-assets-workflow/scripts/render_visual_assets.py \
  --manifest .content/visuals/choisir-bloc-notes-numerique.json \
  --root .
python apply_guide_visuals.py .content/visuals/choisir-bloc-notes-numerique.json
```

## Manifest fields

- `id`
- `page_url`
- `type`
- `output`
- `after_section_id`
- `alt`
- `caption`
- `canvas`
- `title`
- `subtitle`
- `nodes`
- `edges`

The generated SVG is an artifact. The manifest is the source of truth.
