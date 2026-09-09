# Usage Analysis Workflow — AUDIT

Date : 9 septembre 2026
URL : `/usages/dessin/`
Mode : `AUDIT`

## Décision

**LIGHT_UPDATE**

Confiance : **HIGH**

Indexation : **KEEP_NOINDEX** pendant les corrections et jusqu'au `PUBLISH_REVIEW` + validation humaine explicite.

## Résumé

La page possède un job autonome et une vraie valeur éditoriale : elle distingue correctement croquis / schémas / dessin de réflexion d'une illustration avancée, considère les alternatives hors E Ink et ne transforme pas la page en classement produit.

Contrairement au pilote `/usages/prise-de-notes-etudiant/`, la structure n'est pas suffisamment industrialisée pour justifier `DEEP_REWRITE`. Le début de page suit une logique propre au dessin : définition du job → outils de manipulation → rôle réel de la couleur. Des blocs plus génériques (`critères`, `familles`, `contre-indications`, `suite`) restent partagés avec d'autres pages usages, mais ils ne dominent pas toute l'architecture.

La correction recommandée est donc ciblée : fraîcheur des preuves, renforcement de la frontière entre croquis et création avancée, mise à jour du rôle de Supernote Atelier, quelques améliorations de maillage/positionnement et suppression de formulations trop génériques si nécessaire.

## Gates

| Gate | Résultat | Notes |
|---|---|---|
| Intention | PASS | Intention informative claire : évaluer l'E Ink pour le dessin et ses limites. |
| Job-to-page fit | PASS | Le job "capturer et développer une idée visuelle" justifie une URL autonome. |
| JTBD | PASS | Croquis, schémas, corrections et export sont bien distingués de l'illustration finalisée. |
| Usage vs comparatif | PASS | Aucun ranking produit. La page explique le besoin avant de renvoyer vers un comparatif couleur. |
| Usage vs guide | PASS avec vigilance | Le guide couleur explique la technologie/choix couleur vs N&B ; la page dessin applique cette question au workflow créatif. |
| Critères dérivés du job | PASS | Sélection/transformation, calques, surface, couleur et export changent réellement le workflow. |
| Alternatives hors E Ink | PASS | iPad/tablette LCD, tablette graphique et papier sont explicitement considérés. |
| Contre-indications | PASS | Peinture numérique, animation, couleurs fidèles, nombreuses couches, zoom/pan intensifs. |
| Evidence / factuality | LIGHT UPDATE | Base solide mais certaines preuves/outils ont évolué en 2026. |
| Affiliate value | PASS | Page utile sans aucun lien affilié ni modèle gagnant. |
| Internal linking | PASS avec amélioration possible | Handoff couleur cohérent ; possibilité de mieux relier les pages Supernote/BOOX lorsque l'outil de dessin est pertinent. |
| Structural similarity | PASS avec warning | Quelques blocs communs au cluster, mais la logique initiale est spécifique au dessin. |
| Anti-AI-slop | PASS avec warning | Pas de clonage dominant ; alléger les formulations génériques du type "quelle famille de solution choisir" si elles se répètent dans le cluster. |
| SEO technique | PASS | canonical correct, `noindex,follow` conservé. |

## Valeur existante à préserver

- opening answer très clair sur la frontière croquis / illustration avancée ;
- distinction entre différents jobs derrière le mot « dessiner » ;
- priorité donnée aux outils logiciels et non à la seule fiche stylet ;
- réflexion sur couleur, calques, transformation et export ;
- alternatives LCD/tablette graphique/papier ;
- contre-indications explicites ;
- absence de classement produit ;
- sources primaires Supernote, BOOX et E Ink.

## Corrections recommandées

### 1. Actualiser la partie Supernote Atelier

La page s'appuie encore sur la documentation initiale d'Atelier. En juin 2026, Supernote a documenté une mise à jour d'Atelier incluant notamment un pencil brush retravaillé, une opacité réglable pour la couche de référence, une plage de niveaux de gris élargie et le partage vers InkHub.

Ces évolutions ne changent pas le verdict général, mais renforcent la pertinence de Supernote pour le croquis et justifient une mise à jour factuelle ciblée.

### 2. Ne pas sur-généraliser la couleur E Ink depuis Gallery 3

Gallery 3 peut servir d'exemple technologique, mais la page ne doit pas laisser entendre qu'il représente à lui seul l'expérience couleur des appareils de prise de notes actuels. Garder une formulation technologique prudente et renvoyer au guide couleur pour le détail des implémentations.

### 3. Renforcer le test de décision propre au dessin

La page pourrait rendre encore plus explicite le point de bascule :

- croquis rapide / diagramme → E Ink plausible ;
- croquis structuré avec transformations/calques simples → outil spécialisé comme Atelier potentiellement pertinent ;
- illustration avec couleurs précises, nombreux pinceaux, animation ou workflow Adobe/Procreate → tablette créative plus logique.

Il ne faut pas transformer ce continuum en tableau obligatoire si la prose est plus naturelle.

### 4. Réduire les blocs génériques si le cluster audit confirme leur répétition

Les sections `critères`, `familles`, `contre-indications`, `suite` sont justifiées ici, mais leur formulation est partagée par plusieurs pages `/usages/`. Pendant le `CLUSTER_AUDIT`, vérifier si les intitulés et l'ordre doivent être diversifiés. Ce point seul ne justifie pas un deep rewrite sur cette URL.

### 5. Taxonomie visuelle

Le hero affiche actuellement `Guide` alors que la page appartient à `/usages/`. À corriger transversalement vers `Usage` / `Par usage` lors d'une passe dédiée, sans confondre ce point UI avec une faiblesse de contenu.

## Preuves actuelles vérifiées pendant l'audit

- Supernote Atelier reste une application de dessin dédiée et documente sélection/transformation, jusqu'à cinq calques et zoom.
- Une mise à jour Atelier de juin 2026 ajoute des améliorations pertinentes au dessin (pencil brush, référence/opacité, niveaux de gris, partage InkHub).
- La frontière éditoriale avec le guide couleur reste valide : `/usages/dessin/` traite le job créatif ; `/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/` traite le choix de technologie/couleur.

## Handoff

`LIGHT_UPDATE` → `usage-content-workflow`

Scope limité :

1. actualiser les preuves/outils ;
2. resserrer quelques formulations ;
3. renforcer le continuum croquis → illustration avancée ;
4. préserver l'architecture et la majorité du texte ;
5. retourner vers `usage-analysis-workflow / PUBLISH_REVIEW`.

Ne pas réécrire la page à partir de zéro.
