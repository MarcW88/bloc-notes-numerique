# Vérification visuelle avec Playwright

## Installation

Depuis la racine du dépôt :

```bash
npm install
npm run visual:install
```

La seconde commande télécharge la version de Chromium attendue par la version de Playwright verrouillée dans `package-lock.json`.

## Audit des pages marques

```bash
npm run visual:brands
```

Le script lance le site statique localement, visite toutes les pages sous `/marques/` en desktop et mobile, puis écrit dans `.artifacts/design-review/` :

- une capture pleine page par URL et viewport ;
- une capture du menu mobile ouvert ;
- `report.json`, avec les erreurs de console, débordements horizontaux, titres masqués, liens du sommaire et dimensions de la sidebar.

Inspecter les captures avec un outil de lecture d’image. Le rapport automatique aide à trouver les pages à regarder en priorité, mais ne remplace pas le jugement visuel.

## Routes ponctuelles

Pour limiter le contrôle à une ou plusieurs pages :

```bash
node .agents/skills/site-design-review/scripts/run-visual-review.mjs \
  --route /marques/remarkable/ \
  --route /marques/boox/avis/
```

Options utiles :

- `--base-url https://example.com` contrôle un déploiement existant sans lancer le serveur local ;
- `--output chemin` change le dossier des captures ;
- `--port 4173` change le port du serveur local.

Le script renvoie un code non nul seulement en cas d’échec technique empêchant le contrôle. Les constats de design restent à qualifier dans l’audit.

## Exécution dans GitHub

Le workflow `.github/workflows/visual-design-review.yml` lance le même contrôle sur les pull requests qui modifient les pages marques ou leur frontend. Il peut aussi être déclenché manuellement. Les captures et le rapport sont disponibles dans l’artifact `brand-design-review` pendant 14 jours.
