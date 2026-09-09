# Brand analysis — `/marques/boox/`

Date : 9 septembre 2026  
Mode : `AUDIT`  
Workflow : `.agents/skills/brand-analysis-workflow/SKILL.md`

## Décision

**DEEP_REWRITE**  
Confiance : **HIGH**

La page possède une vraie base éditoriale et une fonction autonome, mais elle ne doit pas être considérée comme finale. Le principal blocker n'est pas la longueur ni le manque de mots-clés : c'est une architecture éditoriale fortement industrialisée, partagée presque à l'identique avec plusieurs autres hubs marques, à laquelle s'ajoutent quelques problèmes de fraîcheur et de périmètre dans la gamme BOOX.

La page reste `noindex,follow`.

---

## 1. `content-audit`

Décision interne : **UPDATE / major revision**, mappée vers `DEEP_REWRITE` au niveau du workflow brand.

### Valeur déjà présente

- positionnement BOOX autour d'Android et de l'ouverture logicielle ;
- tableau de modèles utile ;
- distinction couleur / noir et blanc / tailles d'écran ;
- présence de limites réelles ;
- explication de NeoReader, Notes, cloud et applications tierces ;
- liens vers Note Air, Tab Ultra, avis, accessoires, alternatives et comparatifs ;
- sources officielles identifiées.

### Problème principal

La page donne l'impression d'avoir été produite à partir d'un squelette de hub de marque puis remplie avec les données BOOX. Cette structure masque ce qui devrait être le vrai angle de la page : **comprendre une gamme BOOX particulièrement complexe et déterminer quelles différences matérielles et logicielles changent réellement le choix**.

---

## 2. `search-intent`

### Primary intent

**Commercial investigation / brand orientation.**

Le lecteur doit pouvoir comprendre l'univers BOOX et savoir vers quelle famille de tablette de prise de notes s'orienter.

### Primary topic

`BOOX` / `tablette BOOX` dans le contexte de bloc-notes numériques et tablettes E Ink de prise de notes.

### User decision

Le problème n'est pas seulement « BOOX est-il bien ? ». Le lecteur doit surtout déterminer :

- quelle famille BOOX correspond à son usage ;
- si Android apporte une vraie valeur dans son workflow ;
- quelle taille, couleur, lumière frontale, version Android et compatibilité accessoires sont nécessaires ;
- quand BOOX devient trop complexe par rapport à reMarkable, Kindle, Kobo ou Supernote.

### Frontière avec `/marques/boox/avis/`

Le hub doit expliquer **la gamme et l'écosystème**. La page `/marques/boox/avis/` doit conserver la couche **jugement marque, support, garantie, mises à jour, retours et confiance achat**.

Pas de fusion recommandée.

### Gap d'intention

Le titre et le H1 utilisent `BOOX` de manière large, alors que le tableau ne représente qu'une sélection de tablettes orientées prise de notes. La page doit expliciter son périmètre plutôt que laisser entendre qu'elle couvre toute la gamme BOOX, qui comprend aussi d'autres liseuses et formats.

---

## 3. `content-refresh`

Causes principales :

- `Weak structure`
- `Generic prose`
- `Outdated / incomplete range detail`
- `Trust gap` sur certains jugements de marque
- `Template-like cluster structure`

Niveau : **Major revision / deep rewrite**.

Conserver les faits et passages utiles. Reconstruire l'architecture autour du vrai problème de choix BOOX plutôt que réécrire chaque phrase à l'identique sous de nouveaux H2.

---

## 4. `affiliate-value`

### PASS partiel

La page reste utile sans liens affiliés : elle contient des caractéristiques, limites, compatibilités et alternatives. Elle n'est pas une simple description marchand.

### Valeur à renforcer

La page devrait fournir une aide à la décision que la boutique BOOX ne donne pas directement :

- choix par taille et type d'écran ;
- couleur vs noir et blanc ;
- lumière frontale vs absence de lumière ;
- Android 15 vs Android 13 vs Android 12 ;
- BSR / fluidité et applications tierces ;
- clavier / microSD / stylet ;
- grand PDF A4 vs mobilité ;
- raison de choisir une autre marque.

Le tableau actuel est une bonne base, mais il ne suffit pas encore à résoudre cette complexité.

---

## 5. `fact-check` / evidence ledger

| Claim / élément | Statut | Action |
|---|---|---|
| Go 10.3 Gen II : Android 15, 10,3", sans front light | VERIFIED | conserver |
| Go 10.3 Gen II Lumi : Android 15 avec front light | VERIFIED, MISSING | ajouter : cette variante change directement la décision pour un utilisateur qui veut un éclairage |
| Note Air5 C : Android 15, 10,3" Kaleido 3, clavier optionnel, microSD | VERIFIED | conserver / approfondir comme point de repère principal |
| Note Max : 13,3", Android 13, 300 ppp, sans front light | VERIFIED | conserver |
| Tab X C : 13,3" couleur, Android 13 | VERIFIED | conserver |
| Tab Ultra C Pro : Android 12 | VERIFIED | conserver avec contexte générationnel |
| Tab Ultra C Pro : statut « actuel » | CONTRADICTED / CHANNEL-SENSITIVE | la fiche officielle permet encore l'achat alors que certaines collections officielles le signalent sold out ; qualifier la disponibilité |
| « Pen Plus, Pen3 ou InkSense selon les appareils » | PARTIAL | préciser les noms réellement utilisés par modèle : InkSense Plus, Pen3, InkSpire, etc. |
| « BOOX = liberté Android » | SUPPORTED pour les tablettes de prise de notes actuelles | expliciter le périmètre : la marque BOOX au sens large ne doit pas être réduite sans nuance à Android |

### Sources prioritaires utilisées

- BOOX Go 10.3 Gen II / Lumi : `https://shop.boox.com/products/go103gen2`
- BOOX Note Air5 C : `https://shop.boox.com/products/noteair5c`
- BOOX Note Max : `https://shop.boox.com/products/notemax`
- BOOX Tab X C : `https://shop.boox.com/products/tabxc`
- BOOX Tab Ultra C Pro : `https://shop.boox.com/products/tabultracpro`
- BOOX all products / handwriting tools : `https://shop.boox.com/collections/all-products/handwriting-tools`

---

## 6. `evidence-based-reviews`

La page n'est pas une `REVIEW`, mais elle contient des jugements importants : « principal avantage », « plus grande complexité », « avantage majeur ».

Ces jugements sont plausibles et cohérents avec les essais indépendants, mais les sources visibles du hub sont actuellement presque exclusivement officielles.

### Recommandation

Pour les jugements structurants :

- soit ajouter une triangulation indépendante limitée et nommée ;
- soit présenter clairement le point comme une synthèse éditoriale et router le lecteur vers `/marques/boox/avis/` pour l'évaluation détaillée.

Sources indépendantes pertinentes identifiées pendant l'audit : Les Numériques, ZDNET et autres tests récents du Note Air5 C.

---

## 7. `internal-linking-audit`

### PASS

La page relie correctement vers :

- familles Note Air et Tab Ultra ;
- avis BOOX ;
- accessoires ;
- alternatives ;
- reMarkable vs BOOX ;
- BOOX vs Supernote ;
- guide écosystèmes ouverts / fermés.

### Amélioration

Réduire le bloc final de liens en vrac et déplacer davantage de liens dans les moments de décision : PDF, Android, accessoires, grand format, alternative minimaliste, support/avis.

Aucun quota nécessaire.

---

## 8. `anti-ai-slop` — audit individuel

Niveau local : **MEDIUM**.  
Niveau cluster : **HIGH**.

### Signaux visibles

- headings génériques et interchangeables : « Les points qui font réellement la différence », « Les limites à vérifier avant d'acheter », « À qui cette marque convient-elle le mieux ? » ;
- séries presque toujours organisées par groupes de trois ;
- formulations abstraites qui pourraient être transposées vers une autre marque ;
- phrase de transition générique : « Si une de ces limites touche une tâche indispensable... » ;
- bloc de sortie standardisé.

Ces éléments ne seraient pas forcément bloquants isolément. Ils deviennent un blocker lorsqu'on compare la page aux hubs voisins.

---

## 9. Contrôle custom — similarité structurelle du cluster

### Résultat : FAIL

BOOX, Kindle Scribe, Kobo Elipsa et Supernote utilisent pratiquement les **mêmes huit fonctions de sections dans le même ordre** :

1. réponse courte / positionnement ;
2. gamme 2026 ;
3. écosystème ;
4. points différenciants ;
5. limites ;
6. profils adaptés / moins adaptés ;
7. modèles et alternatives ;
8. sources.

Plusieurs formulations sont également identiques ou quasi identiques :

- « Le nom de la marque ne suffit pas pour choisir... »
- « La différence la plus utile à examiner est la circulation d'un document... »
- « Si une de ces limites touche une tâche indispensable... »
- « Le choix est cohérent si... » / « Elle est moins adaptée si... »

La structure éditoriale est donc dictée par un squelette partagé davantage que par les questions spécifiques à BOOX.

Ce seul point suffit à déclencher `DEEP_REWRITE` selon le workflow.

---

## 10. SEO / technique

### PASS technique en brouillon

- `noindex,follow` présent ;
- canonical présent et cohérent ;
- title / H1 cohérents ;
- une seule intention globale identifiable ;
- sources et liens internes présents.

### À corriger pendant la réécriture

- clarifier dans title/H1/intro que la page couvre les **tablettes BOOX pertinentes pour la prise de notes**, pas toute la marque au sens large ;
- maintenir la séparation avec `BOOX avis` ;
- éviter un H2 « gamme 2026 » purement générique si une question plus utile organise mieux la gamme ;
- conserver le `noindex` pendant toute la refonte.

---

## 11. `editorial-qa`

### Intent

PARTIAL : la page répond, mais sous une structure trop générique.

### Original affiliate value

PARTIAL/PASS : vraie utilité, mais potentiel de différenciation important encore inexploité.

### Factuality

PARTIAL : majorité des faits solides, mais variante Go 10.3 Gen II Lumi manquante, stylus mapping imprécis et disponibilité Tab Ultra C Pro à qualifier.

### Natural / purpose-built writing

FAIL au niveau cluster : trop de structure réutilisée.

### User usefulness

PASS de base : un lecteur apprend déjà quelque chose. Mais il peut prendre une meilleure décision avec une architecture propre à la complexité BOOX.

---

## 12. Architecture recommandée pour le handoff vers `brand-content-workflow`

Ce n'est **pas un template obligatoire**. C'est le plan qui ressort de cet audit précis.

### 1. BOOX n'est pas un modèle : commencer par choisir une famille

Clarifier le périmètre de la page et montrer que la difficulté BOOX est d'abord la largeur de gamme.

### 2. Les critères qui éliminent immédiatement certains modèles

Une matrice réellement décisionnelle :

- 10,3 vs 13,3 pouces ;
- noir et blanc vs couleur ;
- front light vs sans front light ;
- mobilité vs PDF A4 ;
- clavier ;
- microSD ;
- version Android.

Inclure Go 10.3 Gen II **et** Go 10.3 Gen II Lumi.

### 3. Android change beaucoup de choses, mais pas toujours dans le bon sens

Expliquer concrètement : Google Play, apps métier, optimisation E Ink, BSR, réglages, versions Android et complexité.

### 4. Le vrai test : faire entrer, annoter puis ressortir un document

Conserver ici l'un des meilleurs éléments de la page actuelle : NeoReader, Notes, cloud, fichiers, export et stockage.

### 5. Quel BOOX choisir pour quatre situations réellement différentes

Des scénarios issus des différences matérielles et logicielles, pas une section générique « pour qui / moins adapté ».

### 6. Les quatre vérifications avant achat

Version Android, génération du stylet/accessoires, disponibilité réelle du modèle, canal d'achat/support. Router vers `avis` et `accessoires` pour les détails.

---

## 13. Handoff

**Next workflow : `brand-content-workflow`**  
Mode recommandé : `RECOVERY / DEEP_REWRITE`.

À préserver : faits vérifiés, matrice de modèles après mise à jour, explication du workflow documentaire, limites réelles, maillage pertinent, sources officielles.

À reconstruire : architecture des H2, transition entre blocs, logique « forces / limites / profils », bloc final de liens et cadrage exact de la gamme.

Aucun contenu de la page n'a été modifié pendant cet audit.