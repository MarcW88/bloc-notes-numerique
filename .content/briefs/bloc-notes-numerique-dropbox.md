---
url: /guides/bloc-notes-numerique-dropbox/
slug: bloc-notes-numerique-dropbox
status: QA_IN_PROGRESS
guide_type: how-to / compatibility
primary_keyword: bloc-notes numérique Dropbox
search_intent: comprendre comment conserver une logique de dossiers Dropbox sans multiplier les copies
 audience: utilisateur Dropbox, multi-plateforme ou Kobo
last_researched: 2026-09-09
refresh_level: deep_rewrite
---

## Décision éditoriale

- Décision issue du cluster audit : `DEEP_REWRITE`.
- Question centrale : Dropbox doit-il synchroniser une arborescence, transporter des documents ou seulement recevoir les exports ?
- Valeur propre : traiter Dropbox comme une couche de fichiers neutre entre plateformes et résoudre le risque de doublons.
- Valeur à préserver : facts actuels sur reMarkable, Supernote, Kobo et BOOX ; distinction import/export/sync.
- Hors périmètre : présenter Dropbox comme une synchronisation universelle des carnets ou inventer une intégration Kindle native.

## Angle et structure issue de la recherche

La page est reconstruite autour de l'arborescence de fichiers :

1. partir d'une structure Dropbox existante ;
2. traiter Supernote comme synchronisation de dossiers ;
3. traiter Kobo comme canal de documents compatibles ;
4. expliquer reMarkable comme entrée/sortie distincte de son propre cloud ;
5. expliquer la double flexibilité BOOX bibliothèque cloud + Android ;
6. signaler l'absence de Dropbox parmi les connexions cloud Kindle Scribe 2025+ documentées ;
7. poser une règle de nommage et de version pour éviter les doublons.

## Registre de preuves vérifié le 9 septembre 2026

- reMarkable import/export/cloud : https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files
- Supernote Dropbox/Drive : https://support.supernote.com/en_US/transfer-files
- Kobo Dropbox : https://help.kobo.com/hc/en-us/articles/360033830114-Add-books-to-your-eReader-using-Dropbox
- BOOX cloud tiers : https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage
- Kindle Scribe 2025+ connexions documentées : https://digprjsurvey.amazon.com/csad/help/node/Tuar1obhcxaS8hVUKd

## Risques

- Kobo : qualifier les modèles et les DRM.
- Dropbox : ne pas confondre copie de fichier et synchronisation du format natif de notes.
- BOOX : plusieurs chemins possibles peuvent créer de l'ambiguïté sur la version de référence.

`noindex,follow` doit rester actif jusqu'à validation humaine explicite.
