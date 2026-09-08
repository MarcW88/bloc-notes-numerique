# Rapport de contrôle avant publication

```yaml
url: /guides/prix-bloc-notes-numerique/
slug: prix-bloc-notes-numerique
brief_status: QA_IN_PROGRESS
reviewed_at: 2026-09-08
final_status: PASS
publication_status: DRAFT_READY
indexing_status: noindex
branch: refresh-guide-prix
```

## 1. Content refresh

Refresh level : **Major revision**, plan validé humainement le 8 septembre 2026.

### Conservé
- le principe du coût total plutôt que du prix d’appel ;
- le tableau des postes de coût ;
- la logique des paniers équivalents ;
- la séparation entre budget structurel et promotions ;
- la section sur les économies qui ne déplacent pas le problème.

### Modifié
- la section trop abstraite « Deux prix officiels pour cadrer le calcul » est remplacée par des configurations officielles datées ;
- la page répond désormais explicitement à « combien coûte réellement un bloc-notes numérique ? » ;
- le coût récurrent est comparé au coût initial sur une durée choisie ;
- les passerelles vers les comparatifs de prix et sans abonnement sont explicites.

### Ajouté
- repères officiels Kobo et reMarkable ;
- comparaison de configurations avec accessoires ;
- formule de coût total extractible ;
- section sur les situations où payer plus cher répond à un besoin réel ;
- liens contextuels vers les prochaines étapes transactionnelles.

Aucun élément validé du brief n’a été supprimé sans raison.

## 2. Search intent

- Primary query : `prix bloc-notes numérique`.
- Intent : information commerciale / préparation de budget.
- User decision : déterminer le panier réellement nécessaire avant de comparer les modèles ou les promotions.
- Correct page type : guide de choix.
- La page ne devient pas un classement « meilleur produit » et ne vise pas les requêtes de prix propres à une marque.
- Cannibalisation : séparation maintenue avec `/comparatifs/`, les pages marques et `/bons-plans/`.

**PASS**.

## 3. Affiliate value

La page reste utile sans aucun lien affilié : elle donne une méthode de calcul, des postes à vérifier, des configurations comparables, des limites et des cas où un surcoût est ou non justifié.

Les liens vers les comparatifs servent de prochaine étape après définition du budget ; ils ne remplacent pas la valeur éditoriale du guide.

Aucun classement n’est influencé par une commission et aucune expérience produit directe n’est revendiquée.

**PASS**.

## 4. Fact-check

Sources primaires revérifiées le 8 septembre 2026.

| Affirmation | Statut | Source | Action |
|---|---|---|---|
| Kobo Elipsa 2E affiché à 399,99 € | CONFIRMED | https://ereader.kobo.com/fr-fr/products/kobo-elipsa-2e | Prix daté dans le texte |
| Écran Kobo Elipsa 2E de 10,3 pouces | CONFIRMED | https://ereader.kobo.com/fr-fr/products/kobo-elipsa-2e | Conservé |
| SleepCover Elipsa 2E affiché à 69,99 € | CONFIRMED | https://ereader.kobo.com/nl-be/products/kobo-elipsa-2e | Prix daté dans le texte |
| Paper Pure à partir de 399 € avec Marker inclus | CONFIRMED | https://remarkable.com/fr-FR/shop/compare | Prix daté dans le tableau |
| Paper Pro + Marker Plus à 699 € | CONFIRMED | https://remarkable.com/fr-FR/products/remarkable-paper/pro | Conservé |
| Paper Pro + Book Folio à 849 € | CONFIRMED | https://remarkable.com/fr-FR/products/remarkable-paper/pro | Conservé |
| Paper Pro + Type Folio à 899 € | CONFIRMED | https://remarkable.com/fr-FR/products/remarkable-paper/pro | Conservé |
| Connect à 3,99 €/mois ou 39,90 €/an | CONFIRMED | https://remarkable.com/de-AT/shop/connect | Présenté comme tarif euro consulté, pas comme prix garanti |
| 3,99 € × 36 mois = 143,64 € | CONFIRMED | calcul arithmétique | Hypothèse « tarif inchangé » visible |
| 39,90 € × 3 ans = 119,70 € | CONFIRMED | calcul arithmétique | Hypothèse « tarif inchangé » visible |

### Point de vigilance Kobo

La page officielle Kobo contient actuellement des indications contradictoires sur l’inclusion du Stylet Kobo 2 selon les blocs de la page. La révision ne s’appuie donc pas sur l’inclusion du stylet pour calculer un panier Kobo. Elle utilise uniquement le prix de l’appareil et le prix séparé de la SleepCover, tous deux vérifiables.

**Overall confidence : élevée.**

## 5. Natural writing

- suppression de la comparaison artificielle « prix d’un appareil vs prix mensuel d’un service » comme pivot de la page ;
- formulations promotionnelles évitées ;
- les exemples servent la décision et non la démonstration de gamme ;
- aucune conclusion générique ou récapitulation artificielle ajoutée.

**PASS**.

## 6. Internal linking

Liens contextuels ajoutés ou conservés :

| Cible | Fonction | Statut |
|---|---|---|
| `/guides/bloc-notes-numerique-avec-ou-sans-abonnement/` | comprendre le coût récurrent | PASS |
| `/guides/taille-ecran-bloc-notes-numerique/` | vérifier si un surcoût de taille est nécessaire | PASS |
| `/comparatifs/bloc-notes-numerique-pas-cher/` | poursuivre avec une contrainte de budget | PASS |
| `/comparatifs/meilleur-bloc-notes-numerique/` | comparer après définition du panier | PASS |
| `/comparatifs/bloc-notes-numerique-sans-abonnement/` | poursuivre si coût récurrent refusé | PASS |
| `/bons-plans/bloc-notes-numerique/` | séparer promotion et budget structurel | PASS |

Les cibles existent dans l’architecture du repo. Aucun lien n’est ajouté pour atteindre un quota.

## 7. Humanizer

Relecture de la réponse initiale, des H2, des tableaux, des procédures et de la fin de page.

- pas de faux enthousiasme ;
- pas de claim d’expérience directe ;
- pas de règle de trois artificielle imposée au contenu ;
- les listes conservées sont des procédures ou des ensembles de référence utiles ;
- le vocabulaire reste concret : prix, panier, stylet, protection, abonnement, durée.

Les éléments globaux de navigation et de footer ne sont pas réécrits dans ce refresh.

**PASS**.

## 8. General writing

Progression finale : réponse immédiate → repères de prix → postes de coût → paniers comparables → durée → arbitrage du surcoût → économies → prochaine étape.

Les sections n’ont pas toutes la même forme et chaque H2 répond à une question distincte du lecteur.

**PASS**.

## 9. Anti-AI-slop

| Fragment / risque | Diagnostic | Correction / statut |
|---|---|---|
| ancienne section « Deux prix officiels pour cadrer le calcul » | exemple trop mince pour l’intention | remplacée par une grille de configurations |
| catégories génériques de prix | risque de taxonomie marketing inventée | aucune fourchette « entrée / milieu / premium » ajoutée |
| listes de prix | risque de catalogue périssable | limitées à des exemples officiels datés servant une comparaison précise |
| « payer plus cher » | risque de justification promotionnelle | toujours relié à une contrainte concrète et contrebalancé par les cas où le surcoût est inutile |

Aucun constat d’origine IA n’est formulé ; le contrôle porte uniquement sur la crédibilité et la spécificité du texte.

**PASS**.

## 10. SEO drift adapté au refresh

Comparaison entre brief initial, page initiale, plan de refresh validé et version finale :

- intent `prix bloc-notes numérique` conservée ;
- coût total conservé et renforcé ;
- séparation avec les bons plans conservée ;
- aucune bascule vers « meilleur bloc-notes numérique » ;
- les liens existants utiles sont conservés et de nouvelles prochaines étapes sont ajoutées ;
- aucune source validée n’est supprimée sans remplacement plus précis.

Le diff de branche ne touche que le brief, le bloc correspondant dans `_generate.py` et le HTML généré de cette URL.

**PASS**.

## 11. SEO technique

- canonical auto-référent : PASS ;
- `noindex,follow` maintenu pendant le brouillon : PASS ;
- un seul H1 : PASS ;
- hiérarchie H1 → H2 sans saut : PASS ;
- title et meta description cohérents avec l’intention : PASS ;
- contenu source synchronisé dans `_generate.py` : PASS ;
- liens contextuels vers des URLs existantes : PASS.

Les éventuelles améliorations globales du template (Open Graph, schema Article/BreadcrumbList, etc.) ne sont pas introduites sur une seule URL dans ce refresh afin de ne pas créer d’incohérence de template. Elles restent un sujet technique transversal du site.

## 12. SEO éditorial

- requête principale traitée dès le H1 et les premières phrases ;
- sous-intentions couvertes : coût réel, accessoires, abonnement, coût sur durée, économies ;
- exemples de marques utilisés comme preuves, pas comme classement ;
- aucune sur-optimisation ni répétition forcée de variantes.

**PASS**.

## 13. GEO

- réponse initiale autonome : PASS ;
- définition opérationnelle du coût total : PASS ;
- formule extractible : PASS ;
- tableaux avec entités explicites et dates : PASS ;
- distinction entre faits officiels, calculs et conseil éditorial : PASS ;
- sources primaires identifiables : PASS.

## 14. Editorial QA

- Intent : PASS
- Original affiliate value : PASS
- Factuality : PASS
- Natural language : PASS
- SEO preservation : PASS
- User usefulness : PASS

La page permet désormais de calculer un meilleur budget même si tous les liens affiliés sont supprimés.

## 15. Lecture complète en ordre rendu

La page HTML finale a été relue intégralement dans l’ordre du document après la dernière modification. La structure de contenu et les classes responsives globales restent inchangées.

Un rendu navigateur mobile/desktop de la branche n’est pas disponible dans l’environnement connecté actuel. Ce point est donc conservé comme contrôle visuel préalable à un éventuel statut `PUBLISHABLE`, sans bloquer le statut de brouillon `DRAFT_READY`.

## Verdict

`PASS` — contenu révisé conforme au plan validé et prêt comme brouillon. La page reste en `noindex,follow`, sur la branche `refresh-guide-prix`, sans fusion ni publication.
