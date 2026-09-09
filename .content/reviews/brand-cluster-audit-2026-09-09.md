# Brand CLUSTER_AUDIT — `/marques/`

Date : 9 septembre 2026  
Mode : `CLUSTER_AUDIT`  
Workflow : `.agents/skills/brand-analysis-workflow/SKILL.md`

## Scope

Audit de l'ensemble des 18 URLs déclarées dans `brand_pages.py` :

- 1 `DIRECTORY` ;
- 5 `BRAND_HUB` ;
- 4 `PRODUCT` ;
- 3 `REVIEW` ;
- 1 `SERVICE` ;
- 2 `ACCESSORY_HUB` ;
- 2 `ALTERNATIVES`.

Le contrôle porte sur les sorties réellement rendues et les métadonnées persistées, pas uniquement sur les fonctions de rendu génériques. Les pages restent `noindex,follow`.

## Résultat cluster

**Pas de blocker cluster imposant une fusion ou une suppression immédiate.**

Le risque de structure industrialisée détecté précédemment sur les hubs Kindle, Kobo, Supernote et BOOX est désormais corrigé dans les sorties rendues. Les sous-pages utilisent encore des renderers partagés à certains endroits, mais les passes d'enrichissement ont suffisamment différencié leurs architectures finales pour qu'un `DEEP_REWRITE` global ne soit pas justifié.

Les faiblesses restantes concernent principalement :

1. fraîcheur et profondeur de la page `reMarkable Connect` par rapport au hub reMarkable désormais plus récent ;
2. séparation et maillage entre les paires `PRODUCT` / `REVIEW`, surtout reMarkable 2 ;
3. couverture de sources des pages `ALTERNATIVES`, qui recommandent plusieurs écosystèmes mais ne documentent pas encore chaque alternative avec une source primaire équivalente ;
4. statut actuel et navigation des anciennes familles BOOX ;
5. couverture documentaire du directory `/marques/` sur les cinq écosystèmes.

## Matrice de décision

| URL | Type | Décision | Confiance | Motif principal |
|---|---|---|---|---|
| `/marques/` | DIRECTORY | `LIGHT_UPDATE` | HIGH | rôle clair et distinct du comparatif général, mais la section sources actuellement rendue couvre surtout reMarkable/BOOX alors que la page décrit cinq écosystèmes |
| `/marques/remarkable/` | BRAND_HUB | `KEEP` | HIGH | PUBLISH_REVIEW passé ; architecture spécifique et Connect actualisé au 9 septembre 2026 |
| `/marques/boox/` | BRAND_HUB | `KEEP` | HIGH | hub déjà reconstruit autour des familles, Android, formats et workflow documentaire ; rôle distinct de l'avis marque |
| `/marques/kindle-scribe/` | BRAND_HUB | `KEEP` | HIGH | PUBLISH_REVIEW passé ; architecture bibliothèque → variantes → circulation des documents → arbitrages |
| `/marques/kobo-elipsa/` | BRAND_HUB | `KEEP` | HIGH | PUBLISH_REVIEW passé ; architecture centrée sur la différence livres / PDF / carnets et leur export |
| `/marques/supernote/` | BRAND_HUB | `KEEP` | HIGH | PUBLISH_REVIEW passé ; architecture centrée sur Manta/Nomad, organisation des notes et InkHub |
| `/marques/remarkable/remarkable-paper-pro/` | PRODUCT | `KEEP` | HIGH | fiche produit spécifique, centrée sur matériel, Connect, accessoires et limites ; distincte de la review |
| `/marques/remarkable/remarkable-paper-pro-avis/` | REVIEW | `KEEP` | HIGH | vraie synthèse critique avec plusieurs essais indépendants ; séparation nette avec la fiche produit |
| `/marques/remarkable/remarkable-2/` | PRODUCT | `LIGHT_UPDATE` | HIGH | page utile sur le statut discontinué et l'occasion, mais maillage trop faible vers la review et les alternatives actuelles |
| `/marques/remarkable/remarkable-2-avis/` | REVIEW | `LIGHT_UPDATE` | HIGH | intention d'avis distincte et sources indépendantes présentes, mais la proximité avec la fiche produit doit être encore mieux matérialisée par le maillage et le cadrage |
| `/marques/remarkable/abonnement-connect/` | SERVICE | `LIGHT_UPDATE` | HIGH | structure pertinente, mais le hub reMarkable contient désormais des informations Connect plus fraîches et plus détaillées ; la page service doit redevenir la source la plus complète du cluster |
| `/marques/remarkable/accessoires/` | ACCESSORY_HUB | `KEEP` | HIGH | architecture spécifique aux générations Marker/Folio/Type Folio et forte couverture officielle |
| `/marques/remarkable/alternatives/` | ALTERNATIVES | `LIGHT_UPDATE` | HIGH | intention claire par raison de quitter reMarkable, mais couverture de sources insuffisamment équilibrée pour Supernote/Kindle/Kobo et maillage incomplet vers certains face-à-face |
| `/marques/boox/boox-note-air/` | PRODUCT | `LIGHT_UPDATE` | MEDIUM-HIGH | rôle autonome autour de Note Air5 C, mais le hub BOOX couvre déjà une partie des mêmes arbitrages ; renforcer la profondeur produit, les différences de génération et le maillage |
| `/marques/boox/boox-tab-ultra/` | PRODUCT | `LIGHT_UPDATE` | MEDIUM-HIGH | page utile pour une famille plus ancienne, mais le statut commercial/générationnel et la comparaison avec Note Air5 C / Tab X C doivent rester le cœur de la page |
| `/marques/boox/avis/` | REVIEW | `KEEP` | HIGH | rôle très distinct du hub : firmware, garantie, retours, compte ONYX, confidentialité et confiance marque ; sources indépendantes présentes |
| `/marques/boox/accessoires/` | ACCESSORY_HUB | `KEEP` | HIGH | architecture propre à BOOX, matrice de compatibilité par modèle et sources produit/accessoires dédiées |
| `/marques/boox/alternatives/` | ALTERNATIVES | `LIGHT_UPDATE` | HIGH | logique de sortie de BOOX pertinente, mais les alternatives recommandées doivent être documentées avec des sources primaires propres et davantage reliées aux pages Kindle/Kobo/Supernote |

## Contrôle de cannibalisation

### Hubs vs pages spécialisées — PASS

Les hubs actuels ne cherchent plus à remplacer systématiquement leurs sous-pages.

- reMarkable hub : gamme + écosystème + Connect + orientation vers pages spécialisées ;
- BOOX hub : choix de famille, Android, tailles et circulation documentaire ;
- Kindle : bibliothèque et flux de documents ;
- Kobo : comportement par type de contenu ;
- Supernote : organisation et structure des notes.

### reMarkable Paper Pro produit vs avis — PASS

La fiche répond à « qu'est-ce que le Paper Pro et est-ce le bon modèle ? ». La review répond à « que peut-on raisonnablement en penser à partir d'essais indépendants ? ». Les architectures et niveaux de preuve sont distincts.

### reMarkable 2 produit vs avis — PASS AVEC CORRECTIONS

Les deux URLs peuvent rester autonomes :

- produit : statut discontinué, caractéristiques encore pertinentes, accessoires, occasion/reconditionné ;
- avis : jugement 2026, synthèse des essais historiques et impact de l'obsolescence sur la recommandation.

Le risque vient moins du contenu que de leur navigation actuelle. Les deux pages doivent se citer explicitement et orienter vers Paper Pure / gamme actuelle / occasion selon l'intention.

### BOOX hub vs BOOX avis — PASS

La séparation est forte : le hub aide à choisir dans la gamme ; l'avis traite confiance marque, firmware, garantie, retours, cloud et confidentialité.

### Pages alternatives vs comparatifs — PASS

Les pages `ALTERNATIVES` partent de la raison de quitter un écosystème et routent vers une solution. Les comparatifs restent des face-à-face. Pas de `MERGE` recommandé à ce stade.

## Similarité structurelle

### Hubs — PASS

Les anciens rôles répétés « gamme → écosystème → différences → limites → pour qui → alternatives » ne structurent plus Kindle, Kobo et Supernote. Les quatre hubs récemment travaillés ont des progressions propres.

### Produits — PASS AVEC SURVEILLANCE

Le renderer générique `product_page()` conserve un squelette commun en source, mais les sorties réellement rendues de reMarkable 2, BOOX Note Air et BOOX Tab Ultra ont été enrichies avec des plans différents. Aucun `DEEP_REWRITE` n'est imposé uniquement parce que le code de rendu partage une fonction.

Le contrôle doit continuer à porter sur l'HTML final lors des prochaines générations, car une régression des overrides réintroduirait rapidement le template commun.

### Reviews — PASS

Paper Pro, reMarkable 2 et BOOX ont des fonctions éditoriales nettement différentes dans leurs sorties finales. BOOX est notamment une review de marque/confiance et non une simple répétition des caractéristiques produit.

### Accessoires — PASS

Les sorties reMarkable et BOOX sont désormais spécifiques : générations Marker/Folio d'un côté ; compatibilité stylets/claviers/microSD par appareil de l'autre.

### Alternatives — PASS AVEC SURVEILLANCE

Les deux pages partagent naturellement un mécanisme « raison de changer → alternative », mais les raisons concrètes diffèrent suffisamment dans les sorties rendues. Le problème actuel est davantage la couverture de preuves que la structure.

## Evidence / factualité

### Points forts

- `Paper Pro avis` dispose de sources officielles et de plusieurs tests indépendants.
- `BOOX avis` documente firmware, garantie, retours, compte, cloud et confidentialité, avec triangulation externe.
- les hubs récemment réécrits datent leurs claims au 9 septembre 2026.
- les pages accessoires utilisent des sources officielles spécifiques aux accessoires et modèles.

### Gaps à corriger

1. `/marques/remarkable/abonnement-connect/` doit intégrer la documentation Connect actuelle explicitement et reprendre les fonctions 2026 déjà vérifiées dans le hub.
2. `/marques/remarkable/alternatives/` doit ajouter une source primaire Supernote, Kindle et Kobo pour les raisons de recommandation qui les concernent.
3. `/marques/boox/alternatives/` doit ajouter des sources primaires reMarkable, Supernote, Kindle et Kobo, plutôt que de reposer principalement sur la documentation BOOX.
4. `/marques/` doit conserver une couverture documentaire représentative des cinq marques ; la limite de sources ne doit pas couper systématiquement les derniers écosystèmes de la liste.
5. Les pages BOOX Note Air et Tab Ultra doivent continuer à dater explicitement leur statut/génération, car la gamme BOOX évolue rapidement.

## Maillage

### À renforcer en priorité

- `reMarkable 2` → `reMarkable 2 avis` ;
- `reMarkable 2 avis` → fiche `reMarkable 2`, page occasion et gamme actuelle ;
- `Connect` → hub reMarkable et Paper Pro/Paper Pure lorsque la dépendance au service change la décision ;
- `reMarkable alternatives` → Kindle/Kobo lorsqu'ils sont cités comme solutions de lecture ;
- `BOOX alternatives` → pages Kindle/Kobo et comparatifs appropriés ;
- `BOOX Note Air` et `Tab Ultra` → hub BOOX, avis BOOX et pages/familles alternatives pertinentes.

Aucun quota de liens n'est recommandé.

## Priorités de production après audit

### Priorité 1

`LIGHT_UPDATE`

- `/marques/remarkable/abonnement-connect/`
- `/marques/`

Objectif : corriger fraîcheur et couverture documentaire avant de toucher aux pages déjà solides.

### Priorité 2

`LIGHT_UPDATE`

- `/marques/remarkable/remarkable-2/`
- `/marques/remarkable/remarkable-2-avis/`
- `/marques/remarkable/alternatives/`
- `/marques/boox/alternatives/`

Objectif : mieux séparer les parcours et renforcer preuves + maillage.

### Priorité 3

`LIGHT_UPDATE`

- `/marques/boox/boox-note-air/`
- `/marques/boox/boox-tab-ultra/`

Objectif : statut/génération, profondeur propre au produit et maillage vers le hub/avis/alternatives.

### KEEP

Aucune production substantielle recommandée pour :

- `/marques/remarkable/`
- `/marques/boox/`
- `/marques/kindle-scribe/`
- `/marques/kobo-elipsa/`
- `/marques/supernote/`
- `/marques/remarkable/remarkable-paper-pro/`
- `/marques/remarkable/remarkable-paper-pro-avis/`
- `/marques/remarkable/accessoires/`
- `/marques/boox/avis/`
- `/marques/boox/accessoires/`

## MERGE / NOINDEX

Aucun `MERGE` ni `NOINDEX` supplémentaire n'est recommandé par ce CLUSTER_AUDIT sur la seule base du contenu actuel.

Cette décision est éditoriale. Si des données GSC montrent ultérieurement qu'une page spécialisée n'a aucune demande, aucun lien externe, aucune impression et aucun rôle de parcours, `content-audit` pourra reconsidérer son maintien. En l'absence de telles données dans l'entrée de cet audit, aucune fusion ou suppression n'est inventée.

## Prochaine étape

Pour chaque URL marquée `LIGHT_UPDATE`, lancer d'abord `brand-analysis-workflow / AUDIT` individuel, puis `brand-content-workflow` uniquement si l'audit individuel confirme la modification. Les pages `KEEP` ne doivent pas être réécrites par réflexe.

Après toute modification : fact-check post-draft → finition éditoriale → maillage → SEO → editorial QA → `PUBLISH_REVIEW` → validation humaine.

`noindex,follow` reste en place jusqu'à instruction explicite d'indexation.
