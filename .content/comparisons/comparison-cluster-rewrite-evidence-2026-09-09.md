# Evidence + briefs — réécriture du cluster `/comparatifs/`

Date de recherche : 9 septembre 2026  
Workflow : `comparison-content-workflow`  
Handoff : `.content/reviews/comparison-cluster-audit-2026-09-09.md`

## Règles communes

- Les faits matériels, fonctions, gammes, prix et abonnements sont vérifiés d'abord auprès des fabricants.
- Les jugements d'expérience sont qualifiés à partir de tests indépendants nommés lorsqu'ils sont nécessaires à la recommandation.
- Aucune page ne revendique de test physique propriétaire.
- Les prix et bundles sont des snapshots et restent freshness-sensitive.
- Aucun des 13 nouveaux contenus n'utilise un scoring numérique ou une pondération obligatoire.
- La commission d'affiliation ne participe jamais à la sélection ni au verdict.
- `noindex,follow` reste obligatoire pendant la validation.

## Sources transversales principales

### reMarkable
- Gamme actuelle / prix France : https://remarkable.com/fr-FR/shop/compare
- Paper Pure : https://remarkable.com/products/remarkable-paper/pure
- Paper Pro : https://remarkable.com/products/remarkable-paper/pro
- Connect : https://remarkable.com/shop/connect/pricing

### BOOX
- Go 10.3 Gen II / Lumi : https://shop.boox.com/products/go103gen2
- Note Air5 C : https://shop.boox.com/products/noteair5c
- Note Max : https://shop.boox.com/products/notemax
- Tab X C : https://shop.boox.com/products/tabxc

### Supernote
- Manta : https://supernote.com/pages/supernote-manta
- Nomad : https://supernote.com/pages/supernote-nomad
- Note system : https://supernote.com/pages/note-system-everything-you-need-to-stay-organized
- Private Cloud beta : https://support.supernote.com/setting-up-your-own-supernote-private-cloud-beta

### Kindle
- Identification des Scribe actuels : https://digprjsurvey.amazon.com/csad/help/node/GK33S847NN4V6Y83
- Nouvelles fonctions Scribe : https://www.aboutamazon.com/news/devices/kindle-scribe-new-features
- Colorsoft : https://www.aboutamazon.com/news/devices/new-amazon-kindle-scribe-color

### Kobo
- Elipsa 2E : https://ereader.kobo.com/fr-fr/products/kobo-elipsa-2e
- Compatibilité stylet : https://ereader.kobo.com/fr-fr/collections/ereaders-with-kobo-stylus-compatibility

### Autres candidats
- PocketBook InkPad One, prix/firmware août 2026 : https://pocketbook.de/en/news/more-ways-to-take-notes-new-firmware-update-for-the-pocketbook-inkpad-one
- Fujitsu Quaderno A4 : https://sdmgr.fmworld.net/digital-paper/product.html

### Tests indépendants utilisés
- Android Central — Best E Ink tablet 2026 : https://www.androidcentral.com/best-e-ink-tablet
- TechRadar — BOOX Note Air5 C : https://www.techradar.com/tablets/ereaders/onyx-boox-note-air5-c-review
- WIRED — affordable digital notebooks 2026 : https://www.wired.com/story/affordable-digital-notebook-comparison-2026/
- ZDNET France — Paper Pure vs BOOX Go 10.3 Lumi : https://www.zdnet.fr/guide-achat/remarkable-paper-pure-vs-boox-go-10-3-lumi-2e-generation-quelle-tablette-choisir-pour-le-travail-496047.htm
- eWritable — reMarkable vs BOOX : https://ewritable.net/remarkable-vs-boox-which-are-the-best-e-ink-tablets/
- eWritable — reMarkable vs Supernote : https://ewritable.net/remarkable-vs-supernote-which-is-the-best-e-ink-tablet/
- Connect — PocketBook InkPad One : https://www.connect.de/testbericht/pocketbook-inkpad-one-test-ereader-review-3213274.html
- Forbes Vetted — Kindle Scribe vs reMarkable : https://www.forbes.com/sites/forbes-personal-shopper/article/remarkable-2-tablet-vs-amazon-kindle-scribe/

---

# Briefs spécifiques

## `/comparatifs/bloc-notes-numerique-a4/`

**Décision :** choisir un grand écran pour PDF/documents A4, pas simplement le meilleur carnet général.  
**Angle :** expliquer d'abord ce que signifie réellement « A4 » sur E Ink.  
**Candidats décisionnels :** Note Max, Tab X C, Fujitsu Quaderno A4, Paper Pro comme compromis.  
**Thèse :** Note Max par défaut en monochrome ; Tab X C si couleur/front light ; Quaderno comme spécialiste à disponibilité régionale ; Paper Pro si le compromis mobilité/focus prime.  
**Anti-pattern :** ne pas appeler tout 10,3 pouces « A4 ».

## `/comparatifs/bloc-notes-numerique-sans-abonnement/`

**Décision :** comprendre ce qui fonctionne réellement sans coût mensuel.  
**Angle :** séparer appareil, cloud et services tiers.  
**Thèse :** Supernote est le choix le plus net ; BOOX est très fort mais les apps tierces peuvent coûter ; reMarkable fonctionne sans Connect mais certaines fonctions avancées sont payantes.  
**Anti-pattern :** binaire « abonnement / aucun abonnement » sans détail fonctionnel.

## `/comparatifs/bloc-notes-numerique-pas-cher/`

**Décision :** choisir une configuration réellement utilisable, pas le prix catalogue le plus bas.  
**Angle :** deux gagnants différents : prix d'entrée vs valeur pour écrire.  
**Thèse :** InkPad One à 329 € avec stylet est l'entrée européenne la moins chère repérée ; Paper Pure à 399 € Marker inclus est plus convaincant pour writing-first.  
**Caveat :** bundles Kobo et prix/taxes BOOX à vérifier.

## `/comparatifs/remarkable-vs-boox/`

**Décision :** focus vs ouverture Android.  
**Angle :** marque-vs-marque et gammes, pas Paper Pure vs un seul BOOX.  
**Thèse :** reMarkable si moins de possibilités est une qualité ; BOOX si apps, front light, couleur ou grands formats sont nécessaires.  
**Anti-pattern :** gagnant universel par moyenne de scores.

## `/comparatifs/remarkable-vs-supernote/`

**Décision :** simplicité immédiate vs profondeur du système de notes.  
**Angle :** comment les notes vieillissent et se retrouvent.  
**Thèse :** reMarkable pour simplicité/couleur/éclairage ; Supernote pour liens, titres, mots-clés et absence d'abonnement constructeur.

## `/comparatifs/boox-vs-supernote/`

**Décision :** ordinateur E Ink flexible vs carnet manuscrit spécialisé.  
**Angle :** ce qui doit se passer après l'écriture.  
**Thèse :** BOOX dès qu'une app/couleur/front light/grand format est requis ; Supernote si l'organisation manuscrite et le focus sont centraux.

## `/comparatifs/tablette-e-ink/`

**Décision :** choisir le niveau de polyvalence.  
**Angle :** familles de tablettes E Ink avant modèles.  
**Thèse :** Note Air5 C est le choix « tablette » polyvalent ; les autres gagnent dès que lecture, focus, organisation ou grand format devient dominant.  
**Frontière :** distinct de `/meilleur-bloc-notes-numerique/`, qui est notebook-first.

## `/comparatifs/bloc-notes-numerique-professionnel/`

**Décision :** faire circuler les notes dans un workflow de travail.  
**Angle :** ce qui arrive après la réunion.  
**Thèse :** Go 10.3 Lumi pour workflow connecté ; Paper Pure pour focus ; Manta pour projets longs ; Air5 C pour apps/couleur.  
**Caveat :** ne pas déduire la conformité IT ou sécurité à partir de l'ouverture Android.

## `/comparatifs/bloc-notes-numerique-etudiant/`

**Décision :** choisir selon les supports de cours, le budget et l'écosystème.  
**Angle :** format des cours avant marque.  
**Thèse :** Paper Pure notes-first ; InkPad One budget/lecture ; Scribe Kindle ; BOOX apps ; Supernote organisation long terme.  
**Anti-pattern :** persona « étudiant » unique.

## `/comparatifs/bloc-notes-numerique-couleur/`

**Décision :** déterminer le travail que la couleur doit accomplir.  
**Angle :** code visuel, PDF, lecture illustrée, apps, mobilité.  
**Thèse :** Air5 C polyvalent ; Paper Pro grand carnet focalisé ; Scribe Colorsoft lecture ; Move mobilité.  
**Anti-pattern :** couleur = meilleure écriture.

## `/comparatifs/kindle-scribe-vs-remarkable/`

**Décision :** liseuse devenue carnet vs carnet devenu outil documentaire.  
**Thèse :** Scribe si lecture >= écriture ; reMarkable si notes/documents de travail > bibliothèque.  
**Scope :** Scribe 3e génération vs Paper Pure comme paire de base, variantes qualifiées.

## `/comparatifs/kindle-scribe-vs-kobo-elipsa/`

**Décision :** choisir une liseuse avec stylet.  
**Angle :** bibliothèque existante en premier.  
**Thèse :** Kindle pour bibliothèque Kindle ; Kobo pour bibliothèque Kobo ; pas de gagnant universel.  
**Caveat :** bundle stylet Kobo à vérifier.

## `/comparatifs/kobo-elipsa-vs-remarkable/`

**Décision :** reader-first vs notebook-first.  
**Thèse :** Elipsa pour lecture Kobo + annotation ; Paper Pure pour carnet et documents de travail.  
**Anti-pattern :** traiter les deux comme deux implémentations identiques du même produit.

---

## Inconnues / limites conservées

1. Aucun test physique propriétaire des produits n'a été réalisé pour ce batch.
2. Les prix BOOX/Supernote peuvent être affichés en dollars ou varier selon région, taxes et livraison.
3. Les pages Kobo consultées ne donnent pas toujours un message parfaitement cohérent sur le bundle du Stylus 2 ; le panier réel doit être revérifié.
4. Fujitsu Quaderno reste pertinent techniquement mais sa distribution/garantie en France est moins simple que les marques distribuées directement en Europe.
5. Les gammes BOOX, Kindle et reMarkable évoluent rapidement ; génération et disponibilité doivent être revalidées lors d'une future actualisation.
