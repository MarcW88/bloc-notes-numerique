# Catalogue : 12 visuels locaux sur 12

Les deux derniers modèles, Supernote Manta A5 X2 et Nomad A6 X2 blanc, disposent désormais de visuels officiels locaux optimisés en WebP 900 × 900. Les 10 images et la mise en page agrandie déjà publiées sont préservées.

| Produit | Image locale | Statut |
|---|---|---|
| reMarkable Paper Pure | /assets/products/remarkable-paper-pure.webp | Intégrée |
| reMarkable Paper Pro | /assets/products/remarkable-paper-pro.webp | Intégrée |
| reMarkable Paper Pro Move | /assets/products/remarkable-paper-pro-move.webp | Intégrée |
| BOOX Note Air5 C | /assets/products/boox-note-air5-c.webp | Intégrée |
| BOOX Go 10.3 (Gen II) | /assets/products/boox-go-10-3-gen2.webp | Intégrée |
| BOOX Go 10.3 Gen II Lumi | /assets/products/boox-go-10-3-lumi.webp | Intégrée |
| BOOX Note Max | /assets/products/boox-note-max.webp | Intégrée |
| BOOX Tab X C | /assets/products/boox-tab-x-c.webp | Intégrée |
| Kindle Scribe (3e génération) | /assets/products/kindle-scribe-3.webp | Intégrée |
| Kobo Elipsa 2E | /assets/products/kobo-elipsa-2e.webp | Intégrée |
| Supernote Manta | /assets/products/supernote-manta.webp | Intégrée |
| Supernote Nomad | /assets/products/supernote-nomad.webp | Intégrée |

## Provenance

Les originaux proviennent des fiches officielles Supernote et sont conservés dans `.content/products/photo-sources-20261029.json` avec URL, attribution, empreinte SHA256 et transformation. Vues avant/arrière vérifiées visuellement, générations A5 X2 et A6 X2 exactes. Retrait du bandeau de prix design au-dessus des appareils et cadrage sur fond blanc, sans modification de leur écran ou de leur boîtier. Aucune image IA.

À la demande explicite du propriétaire, les deux sources sont enregistrées comme `MANUFACTURER_PUBLIC`, avec `rights_checked: false` et `rights_status: not_verified_owner_requested_use`. Cette provenance publique ne constitue pas une licence de reproduction vérifiée. Les autres dix entrées conservent leur statut. Le validateur distingue les deux cas et impose de conserver source, original, attribution et contexte.

## HTML mis à jour

- `boutique/index.html`
- `comparatifs/bloc-notes-numerique-etudiant/index.html`
- `comparatifs/bloc-notes-numerique-pas-cher/index.html`
- `comparatifs/bloc-notes-numerique-professionnel/index.html`
- `comparatifs/bloc-notes-numerique-sans-abonnement/index.html`
- `comparatifs/boox-vs-supernote/index.html`
- `comparatifs/remarkable-vs-supernote/index.html`
- `usages/prise-de-notes-etudiant/index.html`
- `usages/prise-de-notes-professionnelle/index.html`

## Validation

- 12 WebP locaux, valides, distincts, 900 × 900.
- Boutique : 12 images, aucun placeholder « Photographie indisponible ».
- Liens Amazon identiques avant/après sur tous les HTML modifiés.
- validate_product_cards.py all : réussi.
- validate_inline_affiliate_links.py : réussi.
- validate_publication_indexation.py : réussi.
- 8 tests unitaires : réussis, dont 4 couvrant la distinction entre provenance et autorisation.
- git diff --check : réussi.
- CSS existant préservé : 300 × 260 px dans la boutique, 210 × 220 px pour les listes desktop, images contenues et mobile empilé.
