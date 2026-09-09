# Brand Analysis — `/marques/`

Date : 9 septembre 2026  
Mode : `AUDIT`  
Type : `DIRECTORY`

## Décision

**`LIGHT_UPDATE` — confiance HIGH**

La page a une fonction autonome claire : orienter vers un écosystème avant de choisir un modèle. Elle ne doit ni devenir un classement ni dupliquer le comparatif général.

## Valeur déjà présente

- distinction lisible des cinq univers ;
- bonne séparation avec `/comparatifs/meilleur-bloc-notes-numerique/` ;
- critères de choix simples et utiles ;
- liens directs vers les cinq hubs ;
- architecture courte et spécifique au rôle de directory.

## Blocker principal

La section Sources affirme que les cinq écosystèmes ont été vérifiés, mais le HTML rendu ne conserve que des sources reMarkable et BOOX. Les claims Kindle Scribe, Kobo Elipsa et Supernote sont donc insuffisamment représentés dans la preuve visible.

Ce problème vient probablement de la limite appliquée par `sources_html()` plutôt que d'un manque de données global dans le dépôt, mais le résultat utilisateur reste incomplet.

## Factualité

- reMarkable / BOOX : `VERIFIED` via sources officielles visibles ;
- Kindle / Kobo / Supernote : claims cohérents avec les hubs récemment vérifiés, mais la preuve primaire n'est pas visible sur cette page ; statut de publication actuel : `SUPPORTED`, à remonter en `VERIFIED` dans la page elle-même.

## Cannibalisation

**PASS.** Le directory explique quel écosystème explorer ; les hubs expliquent chaque marque et les comparatifs classent ou confrontent des produits.

## Structure / AI-slop

**PASS.** Le plan est justifié par le rôle de directory et n'est pas un clone des hubs.

## Unknowns

Aucune donnée GSC spécifique à cette URL n'a été fournie dans cet audit. Aucun besoin de fusion ou suppression ne peut donc être inféré à partir du trafic.

## Actions nécessaires

1. garantir au moins une source primaire représentative pour Kindle Scribe, Kobo Elipsa et Supernote dans la sortie finale ;
2. conserver la structure actuelle ;
3. ne pas ajouter de ranking ou de score de marque ;
4. conserver les liens vers le comparatif général et le guide de choix.

## Prochaine étape

`brand-content-workflow` en correction légère uniquement, puis `PUBLISH_REVIEW`.

La page reste `noindex,follow`.