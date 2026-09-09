# Comparison CLUSTER_AUDIT — `/comparatifs/`

Date : 9 septembre 2026  
Workflow : `comparison-analysis-workflow` — mode `CLUSTER_AUDIT`  
Scope : 14 URLs  
Indexation pendant l'audit : **aucun changement — conserver `noindex,follow`**

## Résumé exécutif

Décisions :

- **KEEP : 1**
- **LIGHT_UPDATE : 0**
- **DEEP_REWRITE : 13**
- **MERGE : 0**
- **NOINDEX : 0** comme décision éditoriale définitive

La conclusion ne signifie pas que treize pages sont sans valeur. La majorité possèdent déjà une intention crédible, une sélection de produits exploitable, des sources officielles et des limites produit utiles.

Le `DEEP_REWRITE` est déclenché principalement parce que ces treize URLs utilisent encore le même renderer historique `render_legacy_comparison()`. Celui-ci impose à toutes les pages :

1. « Notre grille place X en tête » ;
2. méthode ;
3. critères pondérés ;
4. classement chiffré ;
5. blocs produit numérotés construits de la même façon ;
6. coût ;
7. limites méthodologiques ;
8. guides suivants ;
9. sources.

Cette architecture est explicitement marquée comme legacy dans `comparison_content.py` et ne doit plus servir de modèle aux pages retravaillées.

À l'inverse, `/comparatifs/meilleur-bloc-notes-numerique/` possède déjà un contenu bespoke issu du nouveau workflow et a passé son `PUBLISH_REVIEW`.

---

# 1. Architecture du cluster : les URLs méritent-elles d'exister ?

## 1.1 Sélections générales

### `/comparatifs/meilleur-bloc-notes-numerique/`

Rôle : choisir un bloc-notes numérique E Ink centré sur la prise de notes et proposer des alternatives selon le workflow.

### `/comparatifs/tablette-e-ink/`

Rôle distinct à conserver : choisir une **tablette E Ink polyvalente**, avec une place plus importante pour lecture, applications, éclairage, couleur et usages proches d'une tablette.

**Pas de merge recommandé.** La première URL est notebook-first ; la seconde doit devenir E-Ink-tablet-first.

---

## 1.2 Comparatifs par contexte

### `/comparatifs/bloc-notes-numerique-professionnel/`

Rôle : recommander des appareils pour réunions, documents, exports, cloud et outils de travail.

La page ne doit pas fusionner avec `/usages/prise-de-notes-professionnelle/` :

- `/usages/` explique si et comment l'outil convient au travail ;
- `/comparatifs/` choisit les produits une fois le besoin établi.

### `/comparatifs/bloc-notes-numerique-etudiant/`

Même séparation avec `/usages/prise-de-notes-etudiant/` : besoin et workflow d'un côté, sélection commerciale de l'autre.

---

## 1.3 Comparatifs par contrainte

### `/comparatifs/bloc-notes-numerique-couleur/`

Rôle distinct : choisir un appareil E Ink **où la couleur a une utilité réelle**.

Il ne doit pas fusionner avec `/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/` : le guide explique le compromis technologique ; le comparatif sélectionne les appareils couleur.

### `/comparatifs/bloc-notes-numerique-a4/`

Rôle distinct : choisir un appareil pour documents A4 / grand format avec le moins de zoom possible.

À distinguer du guide `/guides/taille-ecran-bloc-notes-numerique/` qui explique les tailles.

### `/comparatifs/bloc-notes-numerique-sans-abonnement/`

Rôle distinct : comparer ce qui reste disponible sans paiement récurrent et les différences entre fonctions gratuites, cloud optionnel et services premium.

À distinguer du guide `/guides/bloc-notes-numerique-avec-ou-sans-abonnement/`.

### `/comparatifs/bloc-notes-numerique-pas-cher/`

Rôle distinct : sélectionner des configurations réellement abordables et utilisables.

À distinguer du guide `/guides/prix-bloc-notes-numerique/`, qui explique le budget et le coût de configuration.

---

## 1.4 Head-to-head

Les six duels répondent à des requêtes commerciales distinctes :

- Kindle Scribe vs reMarkable ;
- Kindle Scribe vs Kobo Elipsa ;
- reMarkable vs BOOX ;
- reMarkable vs Supernote ;
- BOOX vs Supernote ;
- Kobo Elipsa vs reMarkable.

Aucune paire n'est un doublon exact d'une autre URL. Le problème porte sur le **niveau de comparaison** : certaines requêtes sont marque-vs-marque mais le renderer actuel compare seulement un modèle de chaque marque.

---

# 2. Findings transversaux

## 2.1 Industrialisation éditoriale — FAIL cluster

Toutes les URLs sauf `/meilleur-bloc-notes-numerique/` utilisent encore le renderer legacy.

Conséquences :

- même ouverture ;
- mêmes H2 fonctionnels ;
- même table de critères ;
- même table de ranking ;
- mêmes blocs « À privilégier pour / La limite à ne pas masquer » ;
- mêmes paragraphes coût / limites / suite ;
- différences principalement obtenues par changement des produits, poids et scores.

Cela suffit à déclencher `DEEP_REWRITE` selon le workflow, car la différenciation éditoriale n'est pas produite par l'intention de chaque URL.

## 2.2 Ancien scoring : utile comme donnée historique, pas comme architecture

`comparison_pages.py` contient encore les anciens poids/rankings. Ils peuvent servir comme **hypothèses historiques** à challenger mais ne doivent plus dicter la page.

Pour les futures réécritures :

- scoring optionnel ;
- poids optionnels ;
- verdict conditionnel autorisé ;
- un tableau peut rester si c'est la meilleure forme pour cette décision ;
- les scores ne doivent pas être traités comme des mesures vérifiées.

## 2.3 Search intent : cluster globalement défendable

Les requêtes correspondent à des décisions distinctes. Aucune fusion n'est justifiée uniquement par le partage des mêmes marques ou produits.

Les frontières à rendre explicites sont :

- notebook-first vs E-Ink-tablet-first ;
- usage professionnel/étudiant vs pages `/usages/` ;
- couleur/A4/abonnement/prix vs guides explicatifs ;
- marque-vs-marque vs modèle-vs-modèle dans les head-to-head.

## 2.4 Marché 2026 : plusieurs pages doivent reconsidérer leur scope

Les recherches récentes montrent une gamme plus large que celle couverte par certains anciens univers :

- reMarkable Paper Pure, Paper Pro et Paper Pro Move ;
- Kindle Scribe 3e génération, Scribe Colorsoft et variante sans front light ;
- BOOX Go 10.3 Gen II / Lumi, Note Air5 C, Note Max et autres grands formats ;
- Supernote Manta et Nomad ;
- Kobo Elipsa 2E ;
- nouveaux entrants ou alternatives à examiner selon requête : PocketBook InkPad One, Paperslate, Fujitsu Quaderno A4, etc.

L'objectif n'est pas de rendre chaque univers exhaustif. Les candidats supplémentaires ne sont examinés que s'ils peuvent changer la décision.

Sources publiques récentes utilisées pour contrôler le contexte marché / intention :

- Android Central, « Best E Ink tablet », 9 juillet 2026 — https://www.androidcentral.com/best-e-ink-tablet
- WIRED, digital notebook comparison, 10 juin 2026 — https://www.wired.com/story/affordable-digital-notebook-comparison-2026/
- Forbes Vetted, Kindle Scribe vs reMarkable Paper Pure, 3 juin 2026 — https://www.forbes.com/sites/forbes-personal-shopper/article/remarkable-2-tablet-vs-amazon-kindle-scribe/
- ZDNET France, Paper Pure vs BOOX Go 10.3 Lumi, mis à jour le 2 septembre 2026 — https://www.zdnet.fr/guide-achat/remarkable-paper-pure-vs-boox-go-10-3-lumi-2e-generation-quelle-tablette-choisir-pour-le-travail-496047.htm
- eWritable, reMarkable vs BOOX, 31 mars 2026 — https://ewritable.net/remarkable-vs-boox-which-are-the-best-e-ink-tablets/
- eWritable, reMarkable vs Supernote, 24 mars 2026 — https://ewritable.net/remarkable-vs-supernote-which-is-the-best-e-ink-tablet/
- Frandroid, liseuses couleur 2026, 24 juillet 2026 — https://www.frandroid.com/guide-dachat/2583405_meilleures-liseuses-couleur
- Liseuses.net, PocketBook InkPad One, 11 février 2026 — https://www.liseuses.net/pocketbook-inkpad-one/
- Liseuses.net, liseuses pour étudiants, 25 mars 2026 — https://www.liseuses.net/liseuse-etudiant/

---

# 3. Décision URL par URL

## 3.1 `/comparatifs/meilleur-bloc-notes-numerique/`

**Décision : KEEP**  
Confiance : HIGH

### Pourquoi

- nouvelle structure bespoke ;
- scope E Ink explicite ;
- recommandation par défaut + alternatives conditionnelles ;
- marché 2026 reconsidéré ;
- sources officielles + indépendantes ;
- pas de faux hands-on ;
- `PUBLISH_REVIEW` déjà passé.

### À préserver

Tout le nouveau dispositif. Ne pas le transformer en template pour les autres comparatifs.

### Prochaine étape

Aucune réécriture. Le réévaluer seulement après traitement des pages voisines si une frontière de rôle change.

---

## 3.2 `/comparatifs/tablette-e-ink/`

**Décision : DEEP_REWRITE**  
Confiance : HIGH

### Rôle à conserver

Comparatif **E Ink polyvalent**, différent du bloc-notes numérique général.

### Blockers

- renderer industrialisé ;
- le scope éditorial « tablette E Ink » est plus large que le texte legacy ;
- la page doit expliquer pourquoi ouverture Android, lecture, front light, couleur et apps pèsent davantage ici ;
- la sélection doit être revalidée face aux appareils 2026 actuels.

### Direction

Construire la page autour des **familles de tablettes E Ink** : carnet focalisé, liseuse avec stylet, Android E Ink, grand format, couleur — puis recommander selon le degré de polyvalence recherché.

---

## 3.3 `/comparatifs/bloc-notes-numerique-professionnel/`

**Décision : DEEP_REWRITE**  
Confiance : HIGH

### Rôle à conserver

Choisir un appareil pour un workflow de travail réel.

### Valeur existante

Le scope BOOX / Supernote / reMarkable est cohérent et les critères organisation/export/PDF/apps sont pertinents comme point de départ.

### Blockers

- renderer cloné ;
- « professionnel » ne doit pas se résumer à augmenter les poids organisation/export ;
- le choix doit partir de situations de travail : réunions, PDF, annotation, partage, apps métier, cloud, clavier, environnement sombre, confidentialité selon données disponibles ;
- le scope doit être revalidé face aux gammes 2026.

### Direction

Une architecture par **workflow professionnel** est plus logique qu'un podium générique. ZDNET compare par exemple Paper Pure et BOOX Go 10.3 Lumi précisément sur le travail, ce qui confirme que focus vs ouverture est une décision centrale.

---

## 3.4 `/comparatifs/bloc-notes-numerique-etudiant/`

**Décision : DEEP_REWRITE**  
Confiance : HIGH

### Rôle à conserver

Choisir un appareil pour cours, PDF, révision, mobilité et budget.

### Blockers

- renderer cloné ;
- sélection à reconsidérer avec les entrants accessibles 2026 ;
- le coût doit comparer la configuration réellement utilisable ;
- les besoins varient fortement entre notes de cours, manuels PDF, lecture et apps universitaires.

### Research à intégrer

Le marché étudiant 2026 inclut aussi des propositions comme Paperslate dans certains guides et PocketBook InkPad One atteint 299 € sur le segment grand écran, donc l'ancien univers ne peut pas être repris sans vérification.

### Direction

Partir des **scénarios étudiants qui changent le choix** : PDF lourds, lecture, apps, budget, mobilité, organisation sur plusieurs semestres.

---

## 3.5 `/comparatifs/bloc-notes-numerique-couleur/`

**Décision : DEEP_REWRITE**  
Confiance : HIGH

### Rôle à conserver

Comparer les appareils de notes E Ink couleur.

### Valeur existante

Paper Pro, Note Air5 C, Scribe Colorsoft et Paper Pro Move forment déjà un noyau crédible.

### Blockers

- renderer généraliste ;
- la page doit d'abord répondre à « à quoi la couleur sert-elle vraiment ? » ;
- technologies et compromis diffèrent : couleur, contraste, front light, taille, apps, mobilité ;
- d'autres formats couleur doivent être examinés uniquement s'ils changent une recommandation.

### Direction

Organiser autour des **usages de la couleur** : code visuel de notes, PDF, lecture illustrée, grand écran, mobilité, apps. Ne pas prétendre que couleur = meilleure écriture.

---

## 3.6 `/comparatifs/bloc-notes-numerique-a4/`

**Décision : DEEP_REWRITE — PRIORITÉ TRÈS HAUTE**  
Confiance : HIGH

### Rôle à conserver

Choisir un appareil pour afficher et annoter des documents A4 avec moins de zoom.

### Blockers majeurs

- le terme « A4 » est actuellement traité comme un simple critère `large` ;
- plusieurs produits de l'ancien classement sont des 10,2–10,3 pouces ou 11,8 pouces et ne sont pas réellement des équivalents A4 ;
- le marché comporte des appareils 13,3 pouces ou proches du format A4 qui méritent une analyse dédiée ;
- le confort PDF, le poids et l'absence éventuelle de front light doivent être centraux.

### Candidats à examiner

- BOOX Note Max ;
- BOOX Tab X C / grands formats actuels si toujours pertinents au moment du research ;
- Fujitsu Quaderno A4 ;
- autres vrais grands formats stylet disponibles sur le marché cible.

Paper Pro peut rester comme compromis 11,8 pouces, mais ne doit pas être présenté comme équivalent à un écran A4 sans explication.

### Direction

Commencer par **ce que signifie A4 sur un écran E Ink**, puis séparer vrai grand format et compromis plus mobile.

---

## 3.7 `/comparatifs/bloc-notes-numerique-sans-abonnement/`

**Décision : DEEP_REWRITE — PRIORITÉ TRÈS HAUTE**  
Confiance : HIGH

### Rôle à conserver

Comparer ce que l'utilisateur peut réellement faire sans paiement mensuel.

### Blockers

- un ranking global est peu adapté : la question porte d'abord sur les fonctions gratuites et payantes ;
- « sans abonnement » ne signifie pas toujours qu'une marque possède zéro offre payante ; il faut distinguer abonnement obligatoire, optionnel et fonctions perdues sans abonnement ;
- reMarkable Connect doit être décrit avec nuance : présence d'un abonnement ne signifie pas que l'appareil est inutilisable sans lui.

### Direction

Créer une **matrice fonctionnelle sans abonnement** : notes, export, cloud, recherche, handwriting conversion, apps, synchro, stockage/limitations. Puis recommander selon ce qui reste gratuit.

Le scoring n'est probablement pas nécessaire.

---

## 3.8 `/comparatifs/bloc-notes-numerique-pas-cher/`

**Décision : DEEP_REWRITE — PRIORITÉ TRÈS HAUTE**  
Confiance : HIGH

### Rôle à conserver

Trouver une configuration E Ink à stylet réellement abordable.

### Blockers

- le marché prix évolue vite ;
- l'ancien univers est trop centré sur les marques historiques du site ;
- la configuration complète compte : stylet, accessoires nécessaires, taxes/import éventuels ;
- PocketBook InkPad One est annoncé à 299 € et doit au minimum être considéré ;
- Supernote Nomad est affiché à partir de 299 $ US hors droits selon la région dans les données internes et demande une comparaison équitable du panier.

### Direction

Définir des **paliers de budget** et vérifier ce que l'on obtient réellement à chaque palier. Le prix est central ici, contrairement au comparatif général.

---

## 3.9 `/comparatifs/kindle-scribe-vs-remarkable/`

**Décision : DEEP_REWRITE**  
Confiance : HIGH

### Rôle à conserver

Décider entre une liseuse Kindle qui écrit et un carnet reMarkable qui lit des documents.

### Valeur existante

Le contraste lecture vs écriture est déjà le bon axe.

### Blockers

- renderer head-to-head générique ;
- la gamme Kindle 2026 et la gamme reMarkable ont plusieurs variantes ;
- le couple principal doit être explicité : Scribe 3e génération vs Paper Pure pour le match général, avec renvoi vers Colorsoft / Paper Pro lorsque couleur ou grand format change la décision.

### Evidence marché

Forbes Vetted a publié en juin 2026 un comparatif hands-on Scribe vs Paper Pure et arrive lui aussi à une décision essentiellement conditionnelle : lecture/backlight côté Kindle, écriture/focus côté reMarkable.

### Direction

Construire le duel autour de **lire d'abord vs écrire d'abord**, front light, écosystème de livres, document markup et organisation.

---

## 3.10 `/comparatifs/kindle-scribe-vs-kobo-elipsa/`

**Décision : DEEP_REWRITE**  
Confiance : HIGH

### Rôle à conserver

Comparer deux liseuses grand format avec stylet.

### Blockers

- renderer cloné ;
- la décision est surtout une question d'écosystème de lecture, formats, annotation/export et génération matérielle ;
- la page doit éviter de les juger comme des carnets spécialisés au même titre que Supernote/reMarkable.

### Direction

Architecture **bibliothèque Kindle vs Kobo**, puis PDF, notes, export, front light, bundle et limites. Le résultat peut être explicitement conditionnel.

---

## 3.11 `/comparatifs/remarkable-vs-boox/`

**Décision : DEEP_REWRITE — PRIORITÉ HAUTE**  
Confiance : HIGH

### Rôle à conserver

Comparer deux **philosophies de marque**, pas seulement Paper Pure vs Go 10.3 Gen II.

### Blockers

- requête marque-vs-marque mais univers actuel réduit à un modèle par marque ;
- BOOX propose plusieurs familles Android ; reMarkable propose Paper Pure, Paper Pro et Paper Pro Move ;
- un seul score global masque la vraie décision focus vs polyvalence.

### Evidence marché

Les comparatifs récents eWritable et d'autres sources 2026 traitent justement ce match comme une différence de philosophie : reMarkable = outil focalisé ; BOOX = Android ouvert et plus flexible.

### Direction

Comparer les **écosystèmes**, puis proposer des paires pertinentes selon le besoin : monochrome 10 pouces, couleur, mobilité, applications.

---

## 3.12 `/comparatifs/remarkable-vs-supernote/`

**Décision : DEEP_REWRITE — PRIORITÉ HAUTE**  
Confiance : HIGH

### Rôle à conserver

Comparer deux marques spécialisées dans la prise de notes focalisée.

### Blockers

- requête marque-vs-marque réduite actuellement à Paper Pure vs Manta ;
- le match doit intégrer organisation, liens, navigation, simplicité, hardware réparable/durable lorsque sourcé, lumière/couleur, tailles et gammes ;
- Nomad / Paper Pro / Move peuvent changer la réponse selon format et mobilité.

### Evidence marché

Le comparatif eWritable de mars 2026 traite les deux marques comme deux interprétations différentes du carnet numérique et met fortement l'accent sur l'expérience réelle et l'organisation.

### Direction

Pas de gagnant universel : **reMarkable pour focus/simplicité**, **Supernote pour organisation profonde** lorsque les preuves confirment cette distinction.

---

## 3.13 `/comparatifs/boox-vs-supernote/`

**Décision : DEEP_REWRITE — PRIORITÉ HAUTE**  
Confiance : HIGH

### Rôle à conserver

Décider entre un écosystème Android E Ink et un outil de notes spécialisé.

### Blockers

- requête marque-vs-marque mais comparaison actuelle Go 10.3 Gen II vs Manta uniquement ;
- plusieurs BOOX peuvent être le bon équivalent selon taille/couleur/front light ;
- Supernote possède Manta et Nomad ;
- les critères apps, organisation et simplicité doivent conduire un verdict conditionnel, pas un score unique.

### Direction

Architecture centrée sur **ouvrir le workflow à Android ou protéger le workflow de la complexité** ; proposer ensuite les modèles équivalents par format.

---

## 3.14 `/comparatifs/kobo-elipsa-vs-remarkable/`

**Décision : DEEP_REWRITE**  
Confiance : HIGH

### Rôle à conserver

Comparer une liseuse Kobo avec stylet à l'écosystème reMarkable.

### Blockers

- asymétrie de requête : un produit (`Kobo Elipsa`) vs une marque (`reMarkable`) ;
- le renderer choisit Paper Pure sans expliquer pourquoi c'est le comparable principal ;
- le choix réel est lecture Kobo / formats / éclairage vs environnement focalisé de notes reMarkable.

### Direction

Clarifier dès le début que **Paper Pure est le comparable principal**, puis expliquer quand Paper Pro devient pertinent. Ne pas transformer la page en comparaison exhaustive de toutes les gammes.

---

# 4. Matrice de décisions

| URL | Décision | Confiance | Problème principal | Handoff |
|---|---|---:|---|---|
| `/meilleur-bloc-notes-numerique/` | KEEP | HIGH | — | aucun |
| `/tablette-e-ink/` | DEEP_REWRITE | HIGH | rôle large + template | content workflow |
| `/bloc-notes-numerique-professionnel/` | DEEP_REWRITE | HIGH | workflow pro réduit à des poids | content workflow |
| `/bloc-notes-numerique-etudiant/` | DEEP_REWRITE | HIGH | workflow étudiant + marché/budget | content workflow |
| `/bloc-notes-numerique-couleur/` | DEEP_REWRITE | HIGH | couleur traitée comme simple critère | content workflow |
| `/bloc-notes-numerique-a4/` | DEEP_REWRITE | HIGH | scope A4/grand format | content workflow |
| `/bloc-notes-numerique-sans-abonnement/` | DEEP_REWRITE | HIGH | matrice de fonctions nécessaire | content workflow |
| `/bloc-notes-numerique-pas-cher/` | DEEP_REWRITE | HIGH | marché prix + panier réel | content workflow |
| `/kindle-scribe-vs-remarkable/` | DEEP_REWRITE | HIGH | duel lecture vs écriture à reconstruire | content workflow |
| `/kindle-scribe-vs-kobo-elipsa/` | DEEP_REWRITE | HIGH | écosystèmes liseuse | content workflow |
| `/remarkable-vs-boox/` | DEEP_REWRITE | HIGH | marque-vs-marque réduit à 2 modèles | content workflow |
| `/remarkable-vs-supernote/` | DEEP_REWRITE | HIGH | marque-vs-marque réduit à 2 modèles | content workflow |
| `/boox-vs-supernote/` | DEEP_REWRITE | HIGH | marque-vs-marque réduit à 2 modèles | content workflow |
| `/kobo-elipsa-vs-remarkable/` | DEEP_REWRITE | HIGH | produit-vs-marque non explicité | content workflow |

---

# 5. Priorisation recommandée pour la production

Le workflow de production doit être exécuté URL par URL, même si le research peut être mutualisé.

## Vague 1 — scope / risque décisionnel le plus fort

1. `/bloc-notes-numerique-a4/`
2. `/bloc-notes-numerique-sans-abonnement/`
3. `/bloc-notes-numerique-pas-cher/`
4. `/remarkable-vs-boox/`
5. `/remarkable-vs-supernote/`
6. `/boox-vs-supernote/`

Ces pages ont besoin de repenser la forme même de la décision ou le niveau de comparaison.

## Vague 2 — intents forts mais structure à reconstruire

7. `/tablette-e-ink/`
8. `/bloc-notes-numerique-professionnel/`
9. `/bloc-notes-numerique-etudiant/`
10. `/bloc-notes-numerique-couleur/`

## Vague 3 — duels relativement simples

11. `/kindle-scribe-vs-remarkable/`
12. `/kindle-scribe-vs-kobo-elipsa/`
13. `/kobo-elipsa-vs-remarkable/`

Cette priorité n'est pas un ordre SEO ; elle vise à traiter d'abord les pages où le modèle éditorial actuel risque le plus de produire une mauvaise décision.

---

# 6. Règles de handoff vers `comparison-content-workflow`

Pour chacune des 13 URLs :

1. utiliser ce cluster audit comme contexte ;
2. faire un research/evidence brief propre à l'URL ;
3. challenger la sélection actuelle — ne pas la conserver ou la changer automatiquement ;
4. définir les critères avant la recommandation ;
5. décider si scoring/tableau/ranking apporte quelque chose — ne rien imposer ;
6. construire un brief et une architecture spécifiques ;
7. préserver les facts et sources encore valables ;
8. passer fact-check, humanizer, general-writing, anti-ai-slop, seo-onpage, SEO technique et editorial-qa ;
9. persister le contenu dans `comparison_bespoke_output.py` afin que le renderer legacy ne puisse plus le remplacer ;
10. exécuter `comparison-analysis-workflow / PUBLISH_REVIEW` individuellement ;
11. conserver `noindex,follow` jusqu'à validation humaine et instruction explicite d'indexer.

---

# 7. Conclusion

Le cluster **ne nécessite pas de réduction d'URLs à ce stade**. La structure de site est défendable : chaque comparatif peut répondre à une décision distincte.

Le problème est essentiellement éditorial et méthodologique au niveau du rendu actuel : treize pages sont encore générées par un squelette commun dont la logique de scoring précède la rédaction.

La bonne suite n'est donc pas de supprimer ou fusionner massivement, mais de **migrer progressivement ces treize URLs vers des sources bespoke**, chacune construite à partir de son intention, de ses preuves et de sa décision propre.
