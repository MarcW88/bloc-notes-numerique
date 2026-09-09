---
url: /guides/bloc-notes-numerique-google-drive/
slug: bloc-notes-numerique-google-drive
status: QA_IN_PROGRESS
guide_type: how-to / compatibility
primary_keyword: bloc-notes numérique Google Drive
search_intent: vérifier comment un bloc-notes fait circuler un fichier avec Google Drive et où reste le fichier maître
audience: utilisateur dont Drive est le stockage principal
last_researched: 2026-09-09
refresh_level: deep_rewrite
---

## Décision éditoriale

- Décision issue du cluster audit : `DEEP_REWRITE`.
- Question centrale : avec Google Drive, travaille-t-on sur la source, une copie, une arborescence synchronisée ou une application Android ?
- Valeur propre : faire choisir le bon niveau d'intégration à partir du fichier maître et du workflow réel.
- Valeur à préserver : facts actuels sur reMarkable, Kindle Scribe, Kobo, Supernote et BOOX ; distinction import/export/sync.
- Hors périmètre : classement produit, promesse de coédition non documentée, pseudo-test ou affirmation de compatibilité générique.

## Angle et structure issue de la recherche

La page ne suit plus le squelette commun des pages cloud. Son fil directeur est le devenir du fichier de référence :

1. décider où vit le fichier maître ;
2. expliciter le modèle de copies Kindle Scribe 2025+ ;
3. traiter Kobo comme canal d'entrée de PDF/EPUB personnels ;
4. distinguer la logique de dossiers Supernote/BOOX ;
5. séparer l'intégration Drive du cloud reMarkable ;
6. tester un vrai fichier de bout en bout ;
7. rendre Drive éliminatoire uniquement au niveau d'intégration réellement nécessaire.

## Registre de preuves vérifié le 9 septembre 2026

- reMarkable import/export/cloud : https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files
- Kindle Scribe 2025+ import Drive : https://digprjsurvey.amazon.com/csad/help/node/TjrMJmg3DZpAQLwVuN
- Kindle Scribe 2025+ partage Drive : https://digprjsurvey.amazon.com/csad/help/node/TP8wuaQilIlwlITVTL
- Kobo Google Drive : https://help.kobo.com/hc/en-us/articles/15335985512983-Add-books-to-your-eReader-using-Google-Drive
- Supernote Drive/Dropbox : https://support.supernote.com/en_US/transfer-files
- BOOX cloud tiers : https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage

## Risques

- Kindle : ne pas laisser entendre que les annotations se resynchronisent vers la source ; il s'agit d'une copie.
- Kobo : qualifier les modèles compatibles et les DRM.
- BOOX : ne pas confondre intégration cloud, application Android et synchronisation ONYX.

`noindex,follow` doit rester actif jusqu'à validation humaine explicite.
