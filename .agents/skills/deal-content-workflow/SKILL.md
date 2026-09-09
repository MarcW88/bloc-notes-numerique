---
name: deal-content-workflow
description: Produit et maintient des pages de bons plans, promotions, baisses de prix, occasion et événements commerciaux sans inventer d'offres. Utilise une preuve de prix datée, une classification de fraîcheur et des garde-fous d'affiliation.
---

# Deal Content Workflow

## Principe

Un bon plan n'est pas un prix barré. Une page `/bons-plans/` doit répondre à quatre questions dans cet ordre :

1. **L'offre existe-t-elle réellement maintenant ?**
2. **Le prix de référence est-il défendable ?**
3. **L'économie est-elle réelle et utile pour le lecteur ?**
4. **Le produit reste-t-il pertinent malgré la promotion ?**

Le workflow s'inspire de la discipline de preuve de `mardab96/ecommerce-claude-skills` pour les promotions et de principes de transparence affiliée présents dans `Affitor/affiliate-skills`, mais il est adapté à un média d'affiliation : il n'analyse pas la marge du marchand et ne cherche jamais à maximiser la commission.

## Types de pages

- `LIVE_DEALS` : sélection multi-marques du moment.
- `BRAND_DEALS` : promotions et baisses de prix d'une marque ou gamme.
- `EVENT_DEALS` : Black Friday, Prime Day ou événement comparable.
- `SECOND_HAND` : occasion, reconditionné, refurbished, open-box.

## Source de vérité

Avant la rédaction, créer ou mettre à jour `.content/deals/<slug>.json`.

Ce fichier doit contenir au minimum :

- `page_type`
- `status`
- `checked_at`
- `freshness_policy`
- `intent`
- `reference_prices`
- `offers`
- `watchlist`
- `evidence_ledger`
- `editorial`
- `qa`

Ne jamais publier une offre qui n'existe que dans le texte final mais pas dans le registre de preuve.

## Classification des offres

Utiliser uniquement :

- `ACTIVE_VERIFIED` : prix et disponibilité vérifiés auprès d'une source exploitable.
- `ACTIVE_STOCK_SENSITIVE` : prix visible mais disponibilité ou coût final dépend du stock, du pays ou du checkout.
- `PRICE_WATCH` : prix observé, sans preuve suffisante qu'il s'agit d'une promotion.
- `EXPIRED` : promotion terminée.
- `SOLD_OUT` : prix promotionnel visible mais stock épuisé.
- `UNVERIFIED` : signal trouvé mais non confirmé.
- `NOT_STARTED` : événement futur.

Une offre `ACTIVE_VERIFIED` doit avoir `merchant`, `price`, `currency`, `checked_at` et `source`.

## Prix de référence

Ordre de préférence :

1. prix constructeur actuel hors promotion ;
2. prix constructeur précédent clairement daté ;
3. somme documentée des éléments d'un bundle ;
4. historique de prix fourni par une source spécialisée ;
5. prix barré marchand, uniquement comme signal secondaire.

Ne jamais calculer une réduction à partir d'un prix de référence dont l'origine n'est pas documentée.

## Calcul

Lorsque `price` et `reference_price` sont présents :

`discount_pct = (reference_price - price) / reference_price * 100`

Arrondir l'affichage, mais conserver les valeurs brutes dans le JSON.

Ne pas reprendre mécaniquement le pourcentage marketing affiché par le marchand.

## Fraîcheur

Valeurs recommandées :

- `LIVE_DEALS` : 48 h pour une offre active ; 7 jours pour une page sans offre.
- `BRAND_DEALS` : 72 h pour une offre active ; 7 jours pour une page de veille.
- `EVENT_DEALS` : 24 h pendant l'événement ; 14 jours avant son ouverture.
- `SECOND_HAND` : 14 jours pour les canaux et repères généraux ; une annonce précise exige une vérification beaucoup plus récente.

Une offre qui dépasse son TTL ne doit plus être présentée comme active sans nouvelle vérification.

## Workflow de production

### 1. Intent

Définir si le lecteur cherche une offre immédiatement achetable, un seuil de prix, une période promotionnelle ou un achat d'occasion.

### 2. Discovery

Collecter pour chaque signal : produit exact, variante, vendeur, prix, frais connus, bundle, disponibilité, pays, date/heure et URL source.

### 3. Promo evidence review

Appliquer `references/promo-evidence.md` : distinguer prix observé, prix de référence et promotion réelle.

### 4. Product context

Réutiliser les faits validés du `brand-content-workflow` ou des sources officielles. Une réduction ne transforme pas un produit inadapté en recommandation.

### 5. Affiliate value

Exécuter `affiliate-value`. La page doit rester utile si tous les liens affiliés disparaissent.

### 6. Rédaction

Le texte doit indiquer :

- ce qui est réellement vérifié ;
- ce qui n'est qu'un prix à surveiller ;
- la date de contrôle ;
- pour qui l'offre a du sens ;
- les compromis ;
- quand attendre est préférable.

### 7. Expiration

Lors d'une mise à jour, une offre qui n'est plus confirmée passe à `UNVERIFIED`, `SOLD_OUT` ou `EXPIRED`. Retirer les formulations d'urgence et CTA promotionnels associés.

### 8. QA

Exécuter dans l'ordre :

1. `fact-check`
2. `affiliate-value`
3. `brand-content-workflow` lorsque la page est liée à une marque
4. `content-refresh`
5. `internal-linking-audit`
6. `natural-writing`
7. `humanizer`
8. `general-writing`
9. `anti-ai-slop`
10. contrôle SEO éditorial/technique et GEO
11. `editorial-qa`
12. `validate_deal_workflow.py`

## Garde-fous

- Aucun faux compte à rebours.
- Aucun « meilleur prix » sans base comparable.
- Aucun prix inventé ou extrapolé.
- Aucun deal périmé présenté comme actif.
- Aucun ranking dépendant d'une commission.
- Aucun lien affilié sans transparence ; utiliser `rel="sponsored"` lorsque nécessaire.
- Ne pas appeler une baisse de prix « historique » sans historique vérifiable.
- Ne pas transformer une page de bons plans en comparatif produit.
- Conserver `noindex,follow` jusqu'à validation humaine explicite.

## Handoff

Si la question devient « quel produit choisir ? », renvoyer au `comparison-content-workflow`.
Si la question devient « comment fonctionne ce produit ? », renvoyer au `brand-content-workflow` ou à un guide.
Si la question devient « quel budget prévoir en général ? », renvoyer au guide prix plutôt que de gonfler la page de promotions.