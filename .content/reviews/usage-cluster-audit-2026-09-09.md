# Usage cluster audit — 9 septembre 2026

Mode : `usage-analysis-workflow / CLUSTER_AUDIT`

Scope : les 7 URLs éditoriales sous `/usages/`.

Aucune page n'est réécrite par ce rapport. Aucun merge, redirect ou changement d'indexation n'est automatique.

## Résultat global

| URL | Décision | Confiance | Motif principal |
|---|---|---:|---|
| `/usages/prise-de-notes-professionnelle/` | `DEEP_REWRITE` | HIGH | rôle utile mais architecture fortement clonée avec Étudiant et chevauchement à clarifier avec Réunion |
| `/usages/prise-de-notes-etudiant/` | `DEEP_REWRITE` | HIGH | excellent JTBD et séparation du comparatif, mais architecture industrialisée |
| `/usages/prise-de-notes-reunion/` | `LIGHT_UPDATE` | HIGH | job autonome et contenu utile ; différenciation/navigation à renforcer par rapport au professionnel |
| `/usages/annotation-pdf/` | `MERGE` | HIGH | duplication substantielle avec `/guides/annoter-pdf-tablette-e-ink/` |
| `/usages/lecture-et-prise-de-notes/` | `DEEP_REWRITE` | MEDIUM-HIGH | URL justifiée, mais contenu trop proche du guide `liseuse-ou-bloc-notes-numerique` et du template Usage |
| `/usages/dessin/` | `LIGHT_UPDATE` | HIGH | job et architecture déjà distincts ; surtout freshness factuelle et polish |
| `/usages/remplacer-cahiers-papier/` | `KEEP` | HIGH | job de migration clair, valeur autonome et architecture suffisamment spécifique |

Synthèse :

- `KEEP` : 1
- `LIGHT_UPDATE` : 2
- `DEEP_REWRITE` : 3
- `MERGE` : 1
- `NOINDEX` : 0 comme décision éditoriale définitive

Toutes les pages restent actuellement `noindex,follow` pendant cette phase de travail.

---

# 1. Carte des jobs du cluster

## Professionnel

Job : capturer, organiser, retrouver et faire sortir les notes dans un environnement de travail, avec contraintes d'export et d'IT.

Rôle légitime et distinct du comparatif professionnel, qui choisit des produits.

## Étudiant

Job : centraliser notes manuscrites, supports de cours et révisions sur un semestre, en tenant compte des PDF, applications et contraintes de budget/mobilité.

Rôle légitime et clairement distinct du comparatif étudiant.

## Réunion

Job : capturer décisions/actions sans interrompre l'échange, puis retrouver et partager une sortie exploitable après la réunion.

C'est un sous-job du professionnel, mais suffisamment précis et répétitif pour justifier une URL autonome si la page reste centrée sur le moment réunion et l'après-réunion.

## Annotation PDF

Job déclaré : lire, annoter puis récupérer un PDF exploitable ailleurs.

Ce job est valide, mais l'URL actuelle double largement le guide pratique qui traite déjà du même flux, des mêmes hard gates et des mêmes étapes.

## Lecture + prise de notes

Job : faire cohabiter bibliothèque, annotations liées aux lectures et notes/carnets réutilisables.

Ce job est plus large que la simple comparaison `liseuse vs bloc-notes` et mérite une URL propre, à condition de recentrer la page sur la réutilisation des idées produites par la lecture plutôt que sur une seconde comparaison de catégories.

## Dessin

Job : capturer/développer une idée visuelle, du croquis rapide au dessin plus structuré, avec décision sur calques, transformations, couleur et export.

Rôle très distinct du guide couleur et des comparatifs produits.

## Remplacer les cahiers papier

Job : décider si une migration du papier vers le numérique réduit réellement les frictions de classement, récupération, sauvegarde et partage, sans sacrifier la capture rapide.

Rôle autonome et bien cadré.

---

# 2. Signal principal : industrialisation structurelle partielle

L'ancien workflow a laissé une structure récurrente dans les records et dans les pages :

- `workflow` ou équivalent ;
- `critères` ;
- `familles de solutions` ;
- `contre-indications` ;
- `suite`.

Le problème n'est pas que ces sujets soient interdits : ils peuvent être utiles dans plusieurs pages. Le signal problématique apparaît lorsque leur présence et leur ordre semblent décidés avant l'analyse du job.

### Cas le plus fort

Étudiant et Professionnel ont pratiquement la même charpente :

`situations → workflow → critères → familles → fonctions surévaluées → contre-indications → suite`.

Leurs contenus et JTBD sont différents, mais la forme reste industrialisée. Cela justifie `DEEP_REWRITE` avec préservation d'une large part de la matière existante.

### Cas intermédiaire

Réunion, PDF, Lecture et Remplacement papier reprennent plusieurs fonctions du même squelette mais possèdent des angles plus spécifiques.

Le niveau de correction dépend donc de la force réelle du job et de la duplication inter-catégories, pas d'un quota de sections identiques.

### Cas le plus sain

Dessin se structure naturellement autour de :

`définition du dessin → outils → couleur → critères → solutions/limites`.

La pensée de la page est suffisamment spécifique pour éviter une reconstruction complète.

---

# 3. Risques de cannibalisation inter-catégories

## Étudiant vs Comparatif étudiant — PAS DE MERGE

Usage : quels supports, workflows, critères et alternatives comptent pendant les études ?

Comparatif : quels appareils choisir pour ces contraintes ?

La séparation est saine. Le contenu Usage doit simplement perdre sa structure clonée.

## Professionnel vs Comparatif professionnel — PAS DE MERGE

Même logique : Usage définit le workflow et les hard gates ; Comparatif choisit les produits.

## Professionnel vs Réunion — CONSERVER LES DEUX, MAIS CLARIFIER

Le professionnel est le workflow large de travail : documents, notes, organisation, export, politiques IT.

Réunion doit être strictement centré sur : préparation minimale, capture en temps réel, décisions/actions, récupération et partage post-réunion.

La navigation actuelle entretient une ambiguïté : le menu nomme la page professionnelle `Travail et réunions`, tandis que la page Réunion existe séparément. Recommandation future : renommer le lien professionnel en `Travail` ou `Usage professionnel` et exposer `Réunions` séparément.

## Annotation PDF vs Guide annotation PDF — MERGE RECOMMANDÉ

Les deux pages traitent déjà :

- compatibilité/restrictions du PDF ;
- import ;
- taille et zoom ;
- annotation ;
- export/persistance ;
- archivage / récupération sur ordinateur.

Le guide pratique est la meilleure URL cible car l'intention `annoter un PDF sur E Ink` est intrinsèquement procédurale et le guide possède déjà plus de profondeur opérationnelle.

### Handoff recommandé

- préserver dans le guide les bons passages de la page Usage sur l'adéquation du flux documentaire, les contre-indications et le test `PDF entrant → PDF sortant` ;
- après validation humaine, rediriger éventuellement `/usages/annotation-pdf/` vers `/guides/annoter-pdf-tablette-e-ink/` ;
- ne rien merger ni rediriger automatiquement pendant le cluster audit.

## Lecture + prise de notes vs Guide liseuse/bloc-notes — CONSERVER, MAIS RECADRER

Le guide tranche une catégorie : `liseuse, hybride ou bloc-notes ?`.

La page Usage doit traiter un job différent : comment les lectures produisent-elles des annotations et des notes que l'utilisateur doit retrouver/réutiliser ?

Le contenu actuel glisse trop souvent vers le choix de catégorie et reprend les mêmes questions de DRM, bibliothèque et familles d'appareils. `DEEP_REWRITE` recommandé pour reconstruire la page autour de :

- contenu entrant ;
- annotation pendant la lecture ;
- capture d'idées séparées ;
- récupération des passages ;
- transformation en synthèse/fiche/projet ;
- quand deux appareils restent plus rationnels qu'un seul.

## Dessin vs Guide couleur — PAS DE MERGE

Dessin = workflow créatif et limites d'E Ink.

Guide couleur = décider si la couleur transporte une information suffisamment importante pour justifier un écran couleur.

## Remplacement papier vs Guides organisation/export/cloud — PAS DE MERGE

La page Usage traite la décision de migration dans son ensemble ; les guides traitent les sous-problèmes. Bonne architecture de handoff.

---

# 4. Décisions détaillées

## `/usages/prise-de-notes-professionnelle/` — `DEEP_REWRITE`

### Préserver

- hard gates export / politiques IT ;
- alternatives ordinateur/tablette LCD ;
- cycle entrée → capture → organisation → sortie ;
- sources actuelles ;
- distinction avec le comparatif.

### Reconstruire

- architecture pour qu'elle ne reproduise plus Étudiant ;
- faire partir la page des types de continuité professionnelle qui cassent réellement : données sensibles, documents entrants, notes de réunion, archive, handoff vers collègues ;
- séparer plus clairement le scope de la page Réunion.

## `/usages/prise-de-notes-etudiant/` — `DEEP_REWRITE`

Décision déjà confirmée par l'audit pilote.

Préserver le JTBD semestre, PDF, apps, budget, alternatives et handoffs. Reconstruire l'ordre éditorial autour des vrais arbitrages étudiants plutôt que du template Usage.

## `/usages/prise-de-notes-reunion/` — `LIGHT_UPDATE`

### Pourquoi pas DEEP_REWRITE

Le job est déjà beaucoup plus précis : le texte s'intéresse au Little Hire, au démarrage immédiat, aux décisions/actions et à la sortie post-réunion.

### Corriger

- renforcer encore l'après-réunion comme colonne vertébrale ;
- supprimer quelques passages génériques communs au professionnel ;
- clarifier navigation et maillage avec la page professionnelle ;
- vérifier les fonctions/OCR actuelles au moment de la mise à jour.

## `/usages/annotation-pdf/` — `MERGE`

Cible recommandée : `/guides/annoter-pdf-tablette-e-ink/`.

Ne pas réécrire séparément la page Usage avant décision humaine sur le merge.

## `/usages/lecture-et-prise-de-notes/` — `DEEP_REWRITE`

### Préserver

- distinction bibliothèque / PDF / carnets ;
- DRM comme hard gate ;
- idée qu'un appareil unique n'est pas toujours rationnel ;
- sources et alternatives.

### Reconstruire

- retirer le rôle de seconde page `liseuse vs bloc-notes` ;
- centrer le job sur le passage `lecture → annotation → idée → note réutilisable` ;
- dériver la structure de ce flux au lieu du template `critères/familles/contre-indications`.

## `/usages/dessin/` — `LIGHT_UPDATE`

Décision déjà confirmée par l'audit pilote.

Conserver la structure spécifique et actualiser surtout les capacités créatives/logiciels, puis simplifier les blocs encore hérités du template lorsque cela améliore le flux.

## `/usages/remplacer-cahiers-papier/` — `KEEP`

La page possède le meilleur niveau d'autonomie après Dessin :

- décision de migration explicite ;
- papier considéré comme concurrent légitime ;
- cycle de vie de la note ;
- système hybride autorisé ;
- aucune promesse environnementale ou économique universelle ;
- guides utilisés comme sous-problèmes et non dupliqués.

Aucun changement éditorial substantiel nécessaire au stade du cluster audit.

---

# 5. Findings transversaux hors contenu principal

## Badge visible

Les pages `/usages/` utilisent actuellement le badge visuel `Guide`. Cela brouille légèrement la séparation éditoriale désormais formalisée entre `/usages/` et `/guides/`.

Recommandation : lors de la prochaine passe design/production, utiliser `Par usage` ou `Usage` comme label visible.

## Hub `/usages/`

Le hub contient bien les 7 URLs, mais sa description utilise encore le langage `Nos recommandations ciblées` et `faire le bon choix`, qui rapproche le hub d'un comparateur. Une future passe légère pourrait mieux expliquer que cette section aide d'abord à définir les contraintes avant le choix produit.

## Navigation principale

Le dropdown `Par usage` n'expose que 6 entrées et omet la page Réunion, tandis que la page professionnelle y est libellée `Travail et réunions`. Cela crée une collision de rôle à corriger si Réunion est conservée comme URL autonome.

---

# 6. Ordre de traitement recommandé

1. Décision humaine sur `annotation-pdf` : valider ou refuser le `MERGE` avant toute production.
2. `prise-de-notes-professionnelle` — `DEEP_REWRITE`.
3. `prise-de-notes-etudiant` — `DEEP_REWRITE`.
4. `lecture-et-prise-de-notes` — `DEEP_REWRITE`.
5. `prise-de-notes-reunion` — `LIGHT_UPDATE`.
6. `dessin` — `LIGHT_UPDATE`.
7. `remplacer-cahiers-papier` — `KEEP`, donc aucune production.
8. Une fois les corrections terminées : `usage-analysis-workflow / PUBLISH_REVIEW` sur le cluster corrigé.
9. Validation humaine explicite avant toute indexation.

---

# 7. Conclusion

Le cluster n'a pas un problème de qualité générale : les JTBD, alternatives, contre-indications et registres de preuve sont globalement solides.

Le principal héritage à corriger est **l'architecture éditoriale répétée** de l'ancien workflow, combinée à deux frontières inter-catégories à clarifier :

- `annotation-pdf` est trop proche de son guide et devrait être consolidé ;
- `lecture-et-prise-de-notes` doit rester autonome mais être davantage différencié du guide `liseuse-ou-bloc-notes`.

Le nouveau système d'analyse produit donc des décisions différenciées et ne recommande pas une réécriture totale du cluster.