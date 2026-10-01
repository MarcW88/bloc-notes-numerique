# AUDIT — /bons-plans/bloc-notes-numerique-occasion/

Date : 2026-10-01. Base main : 5b798c38648fdc32a9bbb0f2f6742b2dca9b7951.
Workflow : `.agents/skills/deal-analysis-workflow/SKILL.md`, mode AUDIT. Type/risque : SECOND_HAND.
Décision : **LIGHT_UPDATE**. Audit terminé avant toute modification du contenu.
Empreinte auditée : `130b2fbb51e31123003cbf983813784bd01cd30853f7f18796f45a1cb2f53abe`.

## Intention, valeur et périmètre

Comparer occasion/reconditionné à état, garantie et configuration équivalents.

Valeur à préserver : Checklist écran, batterie, stylet, compte et garantie ; comparaison au neuf sans promesse de décote universelle.

La frontière de catégorie est respectée : le contenu aide la tâche ci-dessus, pas un podium affilié générique. Données GSC, trafic, conversions, backlinks et entretiens : UNKNOWN, indisponibles dans le dépôt. Aucun gain SEO ou déclin supposé.

## Findings et preuves

P1 : BOOX « actuellement en rupture » non confirmé par la fiche actuelle. Le « Sold Out » récupéré concerne Palma 3 dans la navigation ; plusieurs variantes Note sont listées, sans preuve suffisante de stock de chacune.

| Claim / statut | Source | Consultation |
|---|---|---|
| UNKNOWN : stock par variante ; prix affiché et subtotal différents | https://euroshop.boox.com/products/copy-of-used-devices | 2026-10-01 |
| VERIFIED : exemple Libra 2 épuisé, non assimilable à une Elipsa avec stylet | https://ereader.kobo.com/fr-fr/collections/certified-refurbished-ereaders | 2026-10-01 |
| VERIFIED : canal officiel reconditionné, pas de prix/stock de chaque modèle | https://remarkable.com/fr-FR/shop/refurbished/remarkable-paper-pro | 2026-10-01 |

Limites : Batterie des appareils d’occasion et garantie de chaque vendeur UNKNOWN. Pas de déduction juridique sur garantie obligatoire.

## Contrôles éditoriaux et techniques réellement effectués

Lecture du contenu complet et des liens du main local. Intention/search-intent et seo-keyword : cible explicite du H1/registre ; aucune volumétrie inventée. Content-audit/seo-content-audit : décision fondée sur contenu et preuves, pas ancienneté. Fact-check : confrontation des claims instables aux sources ci-dessus, avec erreurs de récupération conservées. Evidence-based-reviews : specs utilisées pour faits, jugements documentaires qualifiés, pas d’observation propre ni de synthèse utilisateurs inventée. JTBD lorsqu’utile : circonstance et sortie recherchée, inférences distinctes d’observations.

Affiliate-value : Checklist écran, batterie, stylet, compte et garantie ; comparaison au neuf sans promesse de décote universelle. reste utile sans aucun lien rémunéré. Internal-linking-audit : toutes les destinations internes de cette page existent ; le lien via ancienne route PDF est distingué d’un lien cassé. SEO/on-page/technical : un title, une description, H1 et canonical présents ; robots d’origine `index,follow` ; canonical `https://bloc-notes-numeriques.fr/bons-plans/bloc-notes-numerique-occasion/`. Ces valeurs doivent rester identiques.

Anti-ai-slop et editorial-qa : tableaux et composants communs servent des contraintes différentes ; autonomie explique la consommation, PDF organise la tâche, A4 arbitre une surface, couleur arbitre un écosystème, accessoires établit compatibilités, occasion contrôle risque/état. Comparaison des H2 voisins (tablette-e-ink, encre-electronique-fonctionnement, lecture-et-prise-de-notes, bons-plans/boox) : pas de reconstruction nécessaire pour imiter un template. Pas de faux test, de scoring imposé ou de quota. Les erreurs localisées ci-dessus suffisent à justifier LIGHT_UPDATE sans DEEP_REWRITE.

## Scope et prochaine étape

Reclasser BOOX UNVERIFIED, retirer la disponibilité négative certaine. Séparer le repère historique de 359 € d’une offre actuelle ; ne promouvoir aucune variante. Actualiser le contrôle des canaux Kobo/reMarkable.

URL, canonical, état d’indexation, consolidation existante et fichiers de publication : à préserver. MERGE/NOINDEX ne sont pas recommandés ici. Validation humaine du lot via PR ; aucune fusion automatique.

## Brief de correction / CONTENT_HANDOFF

Target et lecteur : Comparer occasion/reconditionné à état, garantie et configuration équivalents.
Mandatory fixes : Reclasser BOOX UNVERIFIED, retirer la disponibilité négative certaine. Séparer le repère historique de 359 € d’une offre actuelle ; ne promouvoir aucune variante. Actualiser le contrôle des canaux Kobo/reMarkable.
Preserved value : Checklist écran, batterie, stylet, compte et garantie ; comparaison au neuf sans promesse de décote universelle.
Plan : conserver l’architecture actuelle ; corriger uniquement le paragraphe, la ligne du tableau ou la source impliqués, puis la date pertinente. Pas de FAQ ou nouvelle fiche symétrique.
Claims/sources : tableau ci-dessus ; UNKNOWN n’est pas un fait publiable.
Do not change : URL, canonical, robots, autre contenu du lot KEEP, publication humaine historique.
Expected state : correction sourcée puis PUBLISH_REVIEW ; en attente de validation humaine du changement.
Offers/status : Black Friday NOT_STARTED, baseline historique PRICE_WATCH ; occasion BOOX UNVERIFIED, Kobo exemple SOLD_OUT, reMarkable canal PRICE_WATCH. Aucune nouvelle offre ACTIVE.


## Content workflow et PUBLISH_REVIEW — 1 octobre 2026

La correction légère est appliquée dans le module Python existant du type de page, puis régénérée. Le fact-check après rédaction confronte les nouvelles affirmations aux sources datées de cet audit. La génération Air6 est distinguée de l’Air5 ; aucune expérience de test du 5 n’est attribuée au 6. Les prix historiques ne sont pas convertis en offres actives. Les compatibilités restent attachées au SKU et au modèle.

Passes rédactionnelles : general-writing (conserver la réponse initiale et des conditions de choix concrètes), humanizer (retirer la promesse de suivi quotidien et les certitudes de stock), anti-ai-slop (pas de nouvelle architecture répétée, FAQ ou scoring), evidence-based-reviews (documentaire, aucun test physique), SEO/on-page/internal-linking (destinations existantes et métadonnées de publication préservées), editorial-qa (pas de nouvelle image nécessaire pour ces corrections de faits). La valeur à préserver décrite dans AUDIT reste présente. Aucun rendu visuel dans un navigateur ni essai sur matériel n’a été effectué.

Contrôles exécutés : validate_guide_quality, validate_comparisons, validate_usage_workflow, validate_deal_workflow, validate_product_cards all, validate_publication_indexation et validate_hreflang passent. validate_brands passe sur les deux pages auditées ; son lancement global échoue sur boox-note-air, page inchangée hors lot (concept « limitations »). validate_inline_affiliate_links global échoue sur la page Kindle Scribe inchangée hors lot ; les liens des pages modifiées ont été régénérés par le script existant. Le validateur Deal signale également cinq offres périmées sur trois pages hors lot. Ces résultats globaux ne sont pas présentés comme verts. Contrôle direct du lot : liens internes, canonical et robots conservés ; les deux pages KEEP et toutes les pages hors lot sont identiques à main.

PUBLISH_REVIEW : **PASS — READY_FOR_HUMAN_VALIDATION**, pour la correction éditoriale de cette page seulement. Validation humaine et résolution des blocages globaux signalés requises avant fusion selon les contrôles du dépôt.
