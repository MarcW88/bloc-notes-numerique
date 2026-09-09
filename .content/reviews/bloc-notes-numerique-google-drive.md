# Guide PUBLISH_REVIEW — Google Drive

```yaml
url: /guides/bloc-notes-numerique-google-drive/
reviewed_at: 2026-09-09
workflow: guide-analysis-workflow / PUBLISH_REVIEW
prior_decision: DEEP_REWRITE
content_status: QA_IN_PROGRESS
indexing_status: noindex,follow
verdict: PASS — READY_FOR_HUMAN_VALIDATION
```

## Machine validation

- `validate_guide_quality.py` : PASS sur les 24 guides.
- Liens internes contextuels : PASS, toutes les cibles existent.
- Robots : PASS, `noindex,follow` conservé.
- Canonical : cohérente avec l'URL cible.
- Le contenu est généré depuis `guide_content_bespoke.py`, chargé après les modules Guide génériques.

## Intention et rôle

PASS.

La page répond désormais à une question propre : **où reste le fichier maître lorsqu'un bloc-notes travaille avec Google Drive ?** Elle ne se contente plus d'une liste de compatibilités et ne devient pas un comparatif produit.

La logique éditoriale est : fichier de référence → comportements Kindle/Kobo → logique de dossiers Supernote/BOOX → rôle distinct du cloud reMarkable → test de bout en bout → critère éliminatoire.

## Fact-check et fraîcheur

PASS.

Vérifications effectuées le 9 septembre 2026 sur les documentations officielles :

- reMarkable : import/export et upload vers Google Drive ;
- Kindle Scribe 2025+ : import d'une copie depuis Drive, absence de resynchronisation des annotations vers la source, retour d'une copie PDF, formats de partage des carnets ;
- Kobo : Google Drive sur les modèles compatibles pour EPUB/PDF non protégés, DRM à traiter séparément ;
- Supernote : sélection de dossiers à synchroniser avec Google Drive ;
- BOOX : Drive dans le stockage cloud tiers intégré, distinct des autres mécanismes BOOX/Android.

Aucun comportement expérientiel ou hands-on n'est revendiqué.

## Valeur éditoriale et affiliation

PASS.

La page reste utile sans lien marchand : elle fournit une règle de décision, explique les risques de copies concurrentes et propose un test reproductible avec un vrai document. Les marques servent d'exemples de mécanismes, pas de podium.

## Maillage et frontière de cluster

PASS.

- `/guides/synchroniser-notes-cloud/` reste le parent conceptuel sync/copie/sauvegarde.
- `/guides/bloc-notes-numerique-onedrive/` traite l'environnement Microsoft/entreprise.
- `/guides/bloc-notes-numerique-dropbox/` traite l'arborescence de fichiers multi-plateforme.
- `/guides/formats-fichiers-compatibles/` prend la question DRM/formats.
- `/guides/choisir-bloc-notes-numerique/` reprend le lecteur pour le choix global.

Pas de cannibalisation forte détectée.

## Anti-AI-slop / similarité structurelle

PASS.

Le défaut identifié au cluster audit — squelette commun `modes d'intégration → marques → test → décision` — a été supprimé. La page Google Drive est maintenant construite autour du **fichier maître** et utilise Kindle/Kobo comme cas structurants propres à ce service.

## Risques résiduels

- Les intégrations cloud restent sensibles aux mises à jour logicielles ; une nouvelle vérification est nécessaire lors d'une future actualisation.
- La page ne promet pas de coédition ou de synchronisation lorsqu'une source officielle décrit seulement un import/export de copie.

## Verdict

**PASS — READY_FOR_HUMAN_VALIDATION**

Ce PASS ne retire pas `noindex,follow` et n'autorise pas l'indexation sans validation humaine explicite.
