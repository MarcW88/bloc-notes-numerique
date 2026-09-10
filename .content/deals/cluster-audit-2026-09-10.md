# Bons plans — Cluster audit

Date : 2026-09-10
Workflow : `.agents/skills/deal-analysis-workflow/SKILL.md`
Mode : `CLUSTER_AUDIT`
Scope : `/bons-plans/` et les 7 pages disposant d'un registre `.content/deals/*.json`.

## Conclusion du cluster

Le cluster possède des rôles éditoriaux suffisamment distincts. Aucun `DEEP_REWRITE`, `MERGE` ou `NOINDEX` supplémentaire n'est justifié.

Les composants visuels sont partagés, mais la pensée éditoriale n'est pas clonée : le hub traite l'état du marché, les pages marque traitent leurs problèmes commerciaux propres, l'occasion traite l'état/garantie/canal, et Black Friday traite la préparation temporelle de l'événement.

Décisions :

| URL | Type | Décision | Motif principal |
|---|---|---|---|
| `/bons-plans/` | directory/navigation | KEEP | Hub de navigation sans claim de prix propre ; rôles des sous-pages clairement séparés. |
| `/bons-plans/bloc-notes-numerique/` | LIVE_DEALS | LIGHT_UPDATE | Hub à réaligner sur les statuts et preuves des pages marque ; ajout BOOX Air5 C et Kindle Scribe comme prix à surveiller, correction Air4 C. |
| `/bons-plans/remarkable/` | BRAND_DEALS | LIGHT_UPDATE | Structure et offre solides ; source du canal reconditionné à remplacer par la boutique officielle actuelle. |
| `/bons-plans/kindle-scribe/` | BRAND_DEALS | KEEP | Distinction correcte entre génération 2024, historique de baisse et Colorsoft 2026 ; aucune offre expirée présentée comme active. |
| `/bons-plans/kobo-elipsa/` | BRAND_DEALS | KEEP | Prix catalogue correctement traité comme `PRICE_WATCH`, pas comme promotion ; rôle distinct et contenu utile malgré l'absence de deal actif. |
| `/bons-plans/boox/` | BRAND_DEALS | LIGHT_UPDATE | Note Air4 C sold out et références barrées officielles contradictoires ; Note Air5 C sensible au bundle/TVA/checkout. |
| `/bons-plans/bloc-notes-numerique-occasion/` | SECOND_HAND | LIGHT_UPDATE | BOOX Used Note Series affiché à 359 € mais sold out ; sources reMarkable/Kobo reconditionné à moderniser. |
| `/bons-plans/black-friday/` | EVENT_DEALS | KEEP après correction préalable | Baselines produits désormais documentées ; événement `NOT_STARTED` et aucune remise 2026 prédite. |

## Corrections appliquées

### Hub général

- mise à jour au 10 septembre 2026 ;
- reMarkable Paper Pro + Marker Plus + Book Folio conservé en `ACTIVE_VERIFIED` à 849 € contre 898 € séparément ;
- BOOX Note Air5 C ajouté en `ACTIVE_STOCK_SENSITIVE` à 529,99 €, avec référence barrée utilisée uniquement comme signal secondaire ;
- BOOX Note Air4 C conservé à 499,99 € mais `SOLD_OUT`, sans pourcentage ni référence unique tant que les pages BOOX se contredisent ;
- Kindle Scribe 2024 16 Go ajouté en `PRICE_WATCH` à partir de 389 € hors frais, sans le présenter comme promotion Amazon ;
- Kobo Elipsa 2E conservée en `PRICE_WATCH` à 399,99 €.

### reMarkable

- prix et bundles revalidés ;
- source reconditionné remplacée par la boutique officielle actuelle ;
- structure éditoriale conservée.

### BOOX

- Note Air4 C : 499,99 €, sold out ;
- conflit de prix barré conservé explicitement : 549,99 € sur la collection et 629,98 € sur la fiche produit ;
- aucun pourcentage de remise publié pour le Note Air4 C ;
- Note Air5 C : 529,99 € avec prix final à contrôler selon bundle, TVA et checkout ;
- page centrée sur l'intégrité de l'offre et non sur un ranking produit.

### Occasion / reconditionné

- reMarkable : boutique reconditionnée officielle actuelle ;
- Kobo : collection certifiée reconditionnée officielle ; exemples visibles sold out lors du contrôle ;
- BOOX Used Note Series : 359 € conservé comme repère de canal, statut corrigé en `SOLD_OUT` ;
- checklist et logique de décote conservées.

### Black Friday

Correction réalisée avant ce cluster audit :

- suppression du faux `reference_price` de 0 € utilisé pour représenter la date ;
- date déplacée dans le registre de preuves ;
- ajout de baselines produits datées ;
- aucun deal Black Friday 2026 présenté comme actif avant l'événement.

## Cohérence inter-pages

### Hub général vs pages marque

Le hub peut reprendre les offres principales, mais uniquement comme synthèse. Les pages marque conservent le détail de leur preuve, de leurs limites et de leur contexte commercial.

### Black Friday vs hub live

Black Friday reste une page événementielle et temporelle. Avant l'événement, elle conserve des baselines et une méthode de contrôle ; elle ne doit pas recopier le hub comme une liste de deals actifs.

### Occasion vs pages marque

La page Occasion traite le canal, l'état, la garantie et la décote. Les pages marque peuvent mentionner le reconditionné, mais ne doivent pas dupliquer la checklist d'achat d'occasion.

## Similarité structurelle

Aucun blocker d'industrialisation substantielle après correction :

- hub général : offres/statuts → faux bons plans → acheter/attendre → watchlist ;
- reMarkable : prix de référence → bundles → reconditionné → attendre ;
- Kindle Scribe : repères → historique → seuil → choix du modèle ;
- Kobo : prix repère → intérêt d'une baisse → reconditionné → positionnement ;
- BOOX : Air4/conflict → Air5/checkout → conditions d'une offre exploitable ;
- Occasion : canaux → checklist → jugement du prix ;
- Black Friday : date → baselines → méthode → préparation.

Les structures répondent à des questions différentes et ne résultent pas d'un squelette unique.

## Indexation

Toutes les pages restent en `noindex,follow`.

Aucune indexation automatique n'est autorisée par ce cluster audit. Une future indexation exige : validateur sans blocker, `PUBLISH_REVIEW` PASS, validation humaine explicite et instruction explicite de rendre la page indexable.

## État avant PUBLISH_REVIEW

- corrections éditoriales appliquées ;
- registres `.content/deals/*.json` alignés avec les pages corrigées ;
- `deal_content.py` synchronisé afin qu'une régénération ne restaure pas les anciennes versions ;
- aucune action destructive recommandée.
