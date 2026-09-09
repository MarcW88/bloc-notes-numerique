# Deal records

Les fichiers `.content/deals/<slug>.json` sont la source de vérité des pages `/bons-plans/`.

## Règle principale

Ne jamais corriger un prix, une disponibilité ou un statut uniquement dans le HTML. Mettre d'abord à jour le JSON, puis régénérer la page.

## Statuts

- `ACTIVE_VERIFIED` : offre actuelle, prix et disponibilité vérifiés.
- `ACTIVE_STOCK_SENSITIVE` : offre actuelle mais coût final, stock, TVA, variante ou checkout à confirmer.
- `PRICE_WATCH` : prix observé sans preuve suffisante d'une promotion active.
- `EXPIRED` : promotion terminée.
- `SOLD_OUT` : offre promotionnelle non achetable faute de stock.
- `UNVERIFIED` : signal non confirmé.
- `NOT_STARTED` : événement futur.

## Mise à jour

1. Vérifier la source de chaque offre.
2. Mettre à jour `checked_at` uniquement pour les éléments réellement revérifiés.
3. Mettre à jour le prix de référence et sa base si nécessaire.
4. Changer le statut quand l'offre expire, revient en stock ou cesse d'être vérifiable.
5. Mettre à jour `deal_content.py` uniquement si le contexte éditorial doit changer.
6. Exécuter `python apply_deal_content.py`.
7. Exécuter `python validate_deal_workflow.py`.

## Fraîcheur

Le TTL est défini dans chaque fichier et dans `deal-workflow.config.yaml`. Une offre active dépassant son TTL ne doit pas rester présentée comme active sans nouvelle vérification.

## Indexation

Toutes les pages restent en `noindex,follow` jusqu'à décision humaine explicite. Le workflow ne retire jamais cette balise.