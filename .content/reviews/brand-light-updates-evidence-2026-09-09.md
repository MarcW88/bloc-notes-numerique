# Evidence brief — 8 brand LIGHT_UPDATE pages

Date: 9 septembre 2026
Workflow: `brand-content-workflow`
Scope: uniquement les 8 URLs confirmées `LIGHT_UPDATE` par AUDIT individuel.

## 1. `/marques/`
Intent: orienter vers le bon écosystème sans refaire le comparatif général.
Valeur originale: expliquer le centre de gravité de chaque marque et envoyer vers le hub pertinent.

Claims / sources:
- reMarkable current range — https://remarkable.com/fr-fr — VERIFIED — positionnement spécialisé et gamme actuelle.
- BOOX current range — https://shop.boox.com/collections/all-products/reading-tools — VERIFIED — Android / formats / familles.
- Kindle Scribe 2025+ cloud connections — https://digprjsurvey.amazon.com/csad/help/node/Tuar1obhcxaS8hVUKd — VERIFIED — Google Drive, OneDrive, OneNote sur Scribe 2025+.
- Kobo Elipsa 2E current — https://www.kobo.com/be/fr/eReaders — VERIFIED — 10,3 pouces, Stylus 2, carnets/cloud.
- Supernote note organization — https://supernote.com/pages/note-system-everything-you-need-to-stay-organized — VERIFIED — headings, keywords, stars, links, handwriting recognition.

Decision: conserver le plan court actuel; corriger uniquement la couverture de preuves visible.

## 2. `/marques/remarkable/abonnement-connect/`
Intent: décider si Connect fait réellement partie du coût et du workflow.
Valeur originale: distinguer ce qui fonctionne sans abonnement de ce que Connect ajoute réellement.

Claims / sources:
- Connect pricing/features — https://remarkable.com/shop/connect/pricing — VERIFIED — built-in features without subscription; limited vs unlimited cloud/sync; Convert to Notebook; Meeting Notes Tool; AI convert/share; handwriting search; create/edit in apps; integrations.
- Connect overview — https://remarkable.com/shop/connect — VERIFIED — handwriting search, unlimited cloud storage and sync, integrations, AI-powered tools.
- About Connect support — https://support.remarkable.com/articles/Knowledge/About-Connect-Subscription — VERIFIED — unlimited storage/sync and app functionality.
- Cancellation behavior — https://remarkable.com/shop/connect/pricing — VERIFIED — files remain stored but stop syncing after 50 days without edits; creating/editing in mobile/desktop apps no longer available.

Decision: LIGHT_UPDATE; no architectural rewrite.

## 3. `/marques/remarkable/remarkable-2/`
Intent: comprendre le statut d'un produit discontinué et juger occasion/reconditionné.
Valeur originale: séparer arrêt commercial et maintien logiciel.

Claims / sources:
- reMarkable 2 — https://remarkable.com/products/remarkable-2 — VERIFIED — Discontinued, accessories still available, regular software updates continue.
- current range context — https://remarkable.com/fr-fr — VERIFIED — Paper Pure / Paper Pro Move / Paper Pro current context.

Decision: conserver la structure; ajouter maintenance logicielle et maillage review/gamme.

## 4. `/marques/remarkable/remarkable-2-avis/`
Intent: répondre à « est-elle encore recommandable en 2026 ? » avec un avis documentaire.
Valeur originale: jugement conditionnel fondé sur statut 2026 + essais indépendants historiques.

Claims / sources:
- official status/support — https://remarkable.com/products/remarkable-2 — VERIFIED.
- TechRadar review — https://www.techradar.com/reviews/remarkable-2-tablet — SUPPORTED for observed writing/design experience.
- WIRED review — https://www.wired.com/review/remarkable-2/ — SUPPORTED.
- Tom's Guide review — https://www.tomsguide.com/reviews/remarkable-2-review — SUPPORTED.

Decision: conserver verdict/architecture; renforcer maillage vers fiche, occasion et gamme actuelle.

## 5. `/marques/remarkable/alternatives/`
Intent: choisir une alternative selon la raison de quitter reMarkable.
Valeur originale: alternative conditionnelle, pas classement unique.

Primary sources:
- reMarkable current range — https://remarkable.com/fr-fr — VERIFIED.
- BOOX current range — https://shop.boox.com/collections/all-products/reading-tools — VERIFIED.
- Supernote note system — https://supernote.com/pages/note-system-everything-you-need-to-stay-organized — VERIFIED.
- Kindle Scribe cloud/workflow — https://digprjsurvey.amazon.com/csad/help/node/Tuar1obhcxaS8hVUKd — VERIFIED.
- Kobo Elipsa 2E — https://www.kobo.com/be/fr/eReaders — VERIFIED.

Decision: conserver logique par frustration; ajouter sources et liens Kindle/Kobo.

## 6. `/marques/boox/alternatives/`
Intent: choisir une alternative quand la flexibilité Android devient une friction.
Valeur originale: inclure explicitement le cas où il vaut mieux rester chez BOOX.

Primary sources: mêmes sources multi-marques que ci-dessus, avec BOOX comme source de départ.
Decision: conserver plan; corriger preuves concurrentes et maillage de retour vers BOOX.

## 7. `/marques/boox/boox-note-air/`
Intent: comprendre pourquoi choisir la famille Note Air / Note Air5 C plutôt qu'une autre famille BOOX.
Valeur originale: traduire le passage Note Air4 C -> Note Air5 C en conséquence d'achat.

Claims / sources:
- Note Air5 C — https://shop.boox.com/products/noteair5c — VERIFIED — 10,3 Kaleido 3, 300/150 ppp, Android 15, 6/64 Go, microSD, Google Play, Pen3, keyboard cover, EinkWise.
- Note Air4 C — https://shop.boox.com/products/noteair4c — VERIFIED — Android 13, 6/64 Go, microSD, Pen Plus.

Decision: LIGHT_UPDATE; approfondir le différentiel générationnel sans transformer la page en comparatif général.

## 8. `/marques/boox/boox-tab-ultra/`
Intent: déterminer si la logique « tablet PC E Ink » du Tab Ultra C Pro garde du sens en 2026.
Valeur originale: contextualiser Android 12, clavier+trackpad, caméra, microSD face aux familles plus récentes.

Claims / sources:
- Tab Ultra C Pro — https://shop.boox.com/products/tabultracpro — VERIFIED — still orderable/documented, Android 12, 6/128 Go, 16 MP camera, microSD, magnetic keyboard with trackpad.
- Note Air5 C — https://shop.boox.com/products/noteair5c — VERIFIED — Android 15, 10,3 pouces.
- Tab X C — https://shop.boox.com/products/tabxc — VERIFIED — 13,3 pouces color, Android 13, keyboard support.

Decision: LIGHT_UPDATE; clarify commercial/generation status and internal alternatives.

## Cross-page constraints
- no fake hands-on.
- no price claims required for publication; dynamic prices remain excluded from core copy.
- preserve all `noindex,follow`.
- no new ranking or scoring.
- no structural cloning introduced by the update.
- after rendering: `validate_brands.py` + individual `PUBLISH_REVIEW` for all 8 pages.