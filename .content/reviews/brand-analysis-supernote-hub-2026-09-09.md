# Brand analysis — `/marques/supernote/`

Date : 9 septembre 2026  
Mode : `AUDIT`  
Workflow : `.agents/skills/brand-analysis-workflow/SKILL.md`

## Décision

**DEEP_REWRITE**  
Confiance : **HIGH**

Le hub Supernote a une identité éditoriale forte dans ses faits — organisation des notes, Manta/Nomad, réparabilité, reconnaissance manuscrite — mais pas encore dans son architecture. Il reprend presque exactement le squelette utilisé pour Kindle Scribe, Kobo Elipsa et BOOX. Il présente aussi un petit retard de fraîcheur : les mises à jour Chauvet de juin 2026 ont introduit notamment **InkHub**, qui modifie légèrement la façon de présenter l’écosystème logiciel.

La page reste `noindex,follow`.

---

## 1. `content-audit`

Décision interne : **UPDATE / major revision**, mappée vers `DEEP_REWRITE`.

### Valeur déjà présente

- positionnement très identifiable autour des notes liées et de l’organisation de connaissances ;
- distinction Manta / Nomad ;
- mention de la modularité, batterie remplaçable et stockage extensible ;
- reconnaissance manuscrite et exports texte ;
- limites explicites : pas de couleur, pas de lumière frontale, écosystème moins généraliste que BOOX ;
- maillage vers reMarkable, BOOX, sans abonnement, professionnel et organisation des notes ;
- sources Supernote officielles.

### Problème principal

Supernote possède justement des différences assez fortes pour justifier un plan propre : liens internes entre notes, headings, keywords, étoiles, digest, reconnaissance, modularité, stockage, InkHub. Pourtant le hub les force dans les mêmes blocs « écosystème / forces / limites / pour qui » que les autres marques. La structure sous-exploite donc l’originalité réelle de la marque.

---

## 2. `search-intent`

### Primary intent

**Commercial investigation / knowledge-work fit.**

### Primary topic

`Supernote`, principalement Manta et Nomad dans le contexte des e-notebooks de prise de notes.

### User decision

Le lecteur doit déterminer :

- Manta ou Nomad selon surface et mobilité ;
- si l’organisation avancée des notes justifie Supernote face à une approche plus simple ;
- si l’absence d’éclairage et de couleur est compatible avec son usage ;
- si la modularité et la réparabilité ont une vraie valeur pour lui ;
- si l’écosystème spécialisé suffit sans Android ouvert ;
- comment ses notes, documents et ressources circulent entre Supernote, cloud et outils externes.

### Frontière éditoriale

Le hub doit expliquer l’écosystème et le choix de gamme. Les duels détaillés contre reMarkable et BOOX restent dans `/comparatifs/`.

Pas de fusion recommandée.

---

## 3. `content-refresh`

Causes :

- `Template-like cluster structure`
- `Generic prose`
- `Weak structure`
- `Outdated / incomplete ecosystem detail`
- `Trust gap` limité sur la supériorité implicite de l’organisation des notes

Niveau : **Major revision / deep rewrite**.

---

## 4. `affiliate-value`

### PASS de base

La page apporte une information décisionnelle réelle même sans affiliation : différences de format, limitations matérielles, modularité et organisation des notes.

### Valeur à renforcer

Le meilleur angle n’est pas une liste de forces. Il faut montrer **comment Supernote transforme une masse de notes manuscrites en système navigable** :

- headings ;
- liens entre notes/pages ;
- mots-clés et étoiles ;
- reconnaissance manuscrite ;
- exports ;
- digest / ressources ;
- InkHub et évolution du système ;
- différence entre Manta et Nomad dans ce workflow.

La modularité doit aussi être reliée à des conséquences concrètes : batterie remplaçable, microSD, évolution matérielle annoncée selon modèle.

---

## 5. `fact-check` / evidence ledger

| Claim / élément | Statut | Action |
|---|---|---|
| Manta : 10,7″, 300 ppp, sans éclairage | VERIFIED | conserver |
| Nomad : format compact, 300 ppp, sans éclairage | VERIFIED | préciser la taille si utile au choix |
| Stockage 32 Go + microSD jusqu’à 2 To sur les modèles actuels | VERIFIED | ajouter dans la matrice décisionnelle |
| Batterie remplaçable / conception modulaire sur Manta et Nomad | VERIFIED | conserver, en évitant de promettre une réparabilité illimitée |
| Chauvet est basé sur Android 11 mais spécialisé | VERIFIED | conserver |
| Reconnaissance manuscrite en temps réel et export TXT/DOCX | VERIFIED | conserver |
| Supernote Cloud, Dropbox, Google Drive et transferts locaux | VERIFIED / SUPPORTED | conserver avec distinction des rôles |
| InkHub ajouté dans Chauvet en juin 2026 | VERIFIED, MISSING | ajouter comme évolution de l’écosystème |
| « organisation des notes particulièrement poussée » | SUPPORTED / EDITORIAL | garder comme synthèse mais l’ancrer dans les fonctions concrètes |
| « workflow sans abonnement pour la reconnaissance manuscrite » | SUPPORTED | éviter d’en faire une promesse absolue sur toutes les fonctions futures |

### Sources prioritaires utilisées

- Supernote Manta : `https://supernote.com/products/supernote-manta`
- Supernote Nomad : `https://supernote.com/products/supernote-nomad`
- Supernote — évolution des noms : `https://supernote.com/blogs/supernote-blog/an-explanation-of-supernote-product-naming-evolution`
- Supernote — handwriting recognition : `https://support.supernote.com/en_US/Tools-Features/handwriting-recognition`
- Supernote — transferts : `https://support.supernote.com/en_US/transfer-files`
- Supernote — changelog Manta & Nomad : `https://support.supernote.com/en_US/changelog-for-manta-and-nomad`

---

## 6. `evidence-based-reviews`

Le hub contient des jugements importants sur l’expérience d’écriture, l’organisation et la modularité.

Le test WIRED du Supernote A5 X2 Manta confirme plusieurs points structurants sans remplacer les sources officielles : forte expérience d’écriture, organisation logicielle riche, microSD et conception modulaire ; il souligne aussi l’absence de couleur et certaines limites périphériques. Cette source peut trianguler les jugements éditoriaux.

Source identifiée : WIRED — `Review: Supernote A5 X2 Manta Digital Notebook` (2025).

Aucun langage de test propriétaire ne doit être ajouté sans expérience physique documentée.

---

## 7. `internal-linking-audit`

### PASS

Les liens actuels sont pertinents et orientent vers les vrais arbitrages : reMarkable, BOOX, sans abonnement, professionnel, organisation des notes.

### Amélioration

Déplacer les liens dans les moments d’arbitrage :

- système de notes → guide organisation ;
- applications tierces → BOOX ;
- simplicité / focus → reMarkable ;
- coût récurrent → comparatif sans abonnement.

Éviter un bloc final qui joue le rôle de sitemap éditorial.

---

## 8. `anti-ai-slop`

Niveau local : **MEDIUM**  
Niveau cluster : **HIGH**

Signaux :

- même liste de H2 que Kindle et Kobo ;
- phrase « Le nom de la marque ne suffit pas pour choisir… » réutilisée ;
- paragraphe identique sur la circulation d’un document ;
- blocs forces / limites / profils interchangeables ;
- phrase standard « Si une de ces limites touche une tâche indispensable… » ;
- listes systématiques de trois éléments.

Supernote est pourtant la marque du cluster pour laquelle cette standardisation est particulièrement dommageable : ses fonctions de structuration des notes devraient définir l’architecture.

---

## 9. Contrôle custom — similarité structurelle du cluster

### Résultat : FAIL

Supernote partage avec Kindle Scribe, Kobo Elipsa et BOOX la même architecture éditoriale fondamentale et plusieurs transitions quasi identiques.

Le workflow impose `DEEP_REWRITE` lorsqu’un squelette commun semble précéder l’intention et les preuves. Le blocker est donc substantiel même si le contenu factuel est déjà utile.

reMarkable est actuellement mieux différencié structurellement dans le cluster.

---

## 10. SEO / technique

### PASS technique en brouillon

- `noindex,follow` présent ;
- canonical cohérent ;
- title / H1 alignés ;
- intention de marque claire ;
- sources officielles présentes.

### À revoir pendant la réécriture

Le title « Manta, Nomad, notes liées et comparatifs » est déjà plus spécifique que les H2. La future structure doit tenir cette promesse en mettant les **notes liées / organisation** au centre plutôt qu’en les enfouissant dans une table d’écosystème.

---

## 11. `editorial-qa`

- **Intent** : PARTIAL/PASS.
- **Original affiliate value** : PASS de base.
- **Factuality** : PARTIAL/PASS — données principales solides, InkHub manque à la fraîcheur 2026.
- **Evidence honesty** : PASS.
- **Natural / purpose-built writing** : FAIL au niveau cluster.
- **User usefulness** : PASS de base, mais potentiel nettement supérieur.

---

## 12. Architecture recommandée pour le handoff

Ce plan est spécifique à Supernote.

1. **Supernote vaut surtout le détour si vos notes doivent devenir un système navigable.**
2. **Manta ou Nomad : la taille change plus que la fiche technique.**
3. **Comment Supernote relie une note à une autre** : headings, liens, keywords, étoiles, recherche, reconnaissance.
4. **Faire circuler les documents sans transformer l’appareil en tablette Android généraliste.**
5. **Réparabilité, batterie et microSD : ce que la modularité change vraiment sur la durée.**
6. **InkHub et Chauvet : un écosystème spécialisé qui continue d’évoluer.**
7. **Les trois raisons concrètes de choisir autre chose** : lumière/couleur, apps tierces, lecture commerciale dominante.

---

## 13. Handoff

**Next workflow : `brand-content-workflow`**  
Mode recommandé : `RECOVERY / DEEP_REWRITE`.

À préserver : facts Manta/Nomad, organisation des notes, modularité, limites, sources et maillage.

À ajouter / reconstruire : InkHub, conséquences concrètes de la microSD/batterie, architecture centrée sur les notes liées, suppression des blocs génériques communs au cluster.

Aucun contenu de la page n’a été modifié pendant cet audit.