# Guide PUBLISH_REVIEW — Dropbox

```yaml
url: /guides/bloc-notes-numerique-dropbox/
reviewed_at: 2026-09-09
workflow: guide-analysis-workflow / PUBLISH_REVIEW
prior_decision: DEEP_REWRITE
content_status: QA_IN_PROGRESS
indexing_status: noindex,follow
verdict: PASS — READY_FOR_HUMAN_VALIDATION
```

## Machine validation

- `validate_guide_quality.py` : PASS sur les 24 guides.
- Liens internes contextuels : PASS.
- Robots : PASS, `noindex,follow` conservé.
- Canonical : cohérente avec l'URL cible.
- Source persistante : `guide_content_bespoke.py`.

## Intention et rôle

PASS.

La page répond à une tâche propre : **utiliser Dropbox comme couche de fichiers et d'arborescence sans perdre le contrôle des versions**. Elle ne se limite plus à lister les marques compatibles.

## Fact-check et fraîcheur

PASS.

Vérifications effectuées le 9 septembre 2026 :

- reMarkable : Dropbox comme intégration de fichiers et destination d'export ;
- Supernote : autorisation Dropbox et sélection de dossiers/sous-dossiers à synchroniser ;
- Kobo : ajout de PDF/EPUB non protégés via Dropbox sur les modèles compatibles ;
- BOOX : Dropbox dans le stockage cloud tiers intégré et possibilité d'une seconde voie via Android ;
- Kindle Scribe 2025+ : les connexions cloud actuellement documentées par Amazon concernent Google Drive, Microsoft OneDrive et OneNote, pas Dropbox.

La page ne transforme pas cette absence documentée en affirmation sur toutes les méthodes de transfert Kindle.

## Valeur éditoriale et affiliation

PASS.

La page apporte une méthode indépendante des liens marchands : définir la version de référence, choisir une méthode principale, nommer les copies annotées et tester le workflow avec plusieurs fichiers.

## Maillage et frontière de cluster

PASS.

- `/guides/synchroniser-notes-cloud/` reste le parent des mécanismes de sync.
- `/guides/bloc-notes-numerique-google-drive/` traite le fichier maître dans l'écosystème Google.
- `/guides/bloc-notes-numerique-onedrive/` traite Microsoft 365 et les contraintes IT.
- `/guides/formats-fichiers-compatibles/` récupère DRM et types de documents.

La séparation des trois URLs fournisseur reste justifiée.

## Anti-AI-slop / similarité structurelle

PASS.

La structure Dropbox est maintenant propre au sujet : **arborescence existante → sync de dossiers Supernote → canal documentaire Kobo → entrée/sortie reMarkable → flexibilité BOOX → absence de Dropbox dans les connexions Kindle documentées → règle anti-doublons**.

Le squelette fournisseur commun identifié lors du cluster audit n'est plus présent.

## Risques résiduels

- Les intégrations peuvent évoluer avec les firmwares.
- Les workflows de copie et de format natif restent à distinguer selon le type de contenu.

## Verdict

**PASS — READY_FOR_HUMAN_VALIDATION**

Ce PASS ne retire pas `noindex,follow` et n'autorise pas l'indexation sans validation humaine explicite.
