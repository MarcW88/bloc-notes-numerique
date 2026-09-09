# Usage cluster — PUBLISH_REVIEW

Date : 9 septembre 2026

Mode : `usage-analysis-workflow / PUBLISH_REVIEW`

Scope : cluster `/usages/` après application du `usage-content-workflow` et du merge validé de l'annotation PDF.

## Verdict global

**PASS — READY_FOR_HUMAN_VALIDATION**

Ce PASS est éditorial et technique. Il n'autorise pas automatiquement l'indexation. Les URLs Usage actives conservent `noindex,follow` jusqu'à validation humaine et instruction explicite d'indexer.

## Gate machine

- `validate_usage_workflow.py` : PASS via le workflow `Regenerate usage cluster` run `34378067809`.
- application idempotente des contenus reviewés : PASS ;
- badge visible `Par usage` : PASS ;
- date de vérification visible alignée au 9 septembre 2026 : PASS ;
- `noindex,follow` préservé sur les routes Usage : PASS ;
- aucune donnée de ranking produit dans les registres Usage : PASS.

## Gate 1 — rôle éditorial des URLs

### `/usages/prise-de-notes-professionnelle/`

PASS.

La page traite désormais la continuité documentaire professionnelle : documents entrants, notes, règles IT, organisation, archive et handoff. Elle ne sélectionne pas de produits et renvoie explicitement le choix produit au comparatif professionnel.

La frontière avec Réunion est explicite : la page Réunion traite le moment de capture et le suivi immédiat ; Professionnel couvre le workflow de travail plus large.

### `/usages/prise-de-notes-etudiant/`

PASS.

La page définit d'abord les supports de cours, le choix remplacement/complement, les ruptures import/cours/révisions/sortie et les arbitrages PDF-budgets-apps. Le comparatif étudiant reste propriétaire du choix de modèles.

### `/usages/prise-de-notes-reunion/`

PASS.

Le Little Hire, la première minute, les décisions/actions et l'après-réunion forment désormais la colonne vertébrale. La page ne duplique plus le workflow professionnel général.

### `/usages/lecture-et-prise-de-notes/`

PASS.

La page ne constitue plus une seconde version du guide `liseuse-ou-bloc-notes-numerique`. Elle suit le job spécifique `contenu entrant → annotation → idée personnelle → récupération → sortie`, avec possibilité explicite de conserver deux appareils lorsque l'unification n'apporte pas de valeur.

### `/usages/dessin/`

PASS.

Le contenu reste centré sur le continuum `croquis → dessin structuré → illustration`, les outils, la couleur et l'export. Il est distinct du guide couleur et du comparatif de modèles couleur.

### `/usages/remplacer-cahiers-papier/`

PASS / KEEP.

Le contenu conserve son rôle autonome de décision de migration, accepte le papier et le système hybride comme alternatives et utilise les guides organisation/export/cloud comme sous-problèmes.

### `/usages/annotation-pdf/`

MERGED — PASS.

La valeur éditoriale spécifique à l'usage a été consolidée dans `/guides/annoter-pdf-tablette-e-ink/`, notamment le test `PDF entrant → annotation → PDF sortant` et les contre-indications E Ink.

L'ancienne route :

- reste `noindex,follow` ;
- canonicalise vers le guide ;
- applique une redirection immédiate compatible avec le site statique ;
- n'est plus présente dans le hub ni dans le dropdown Usage ;
- ne reçoit plus de liens internes HTML depuis le site.

Sur un hébergement permettant des redirections HTTP, une 301 serveur resterait préférable à long terme, mais son absence n'est pas bloquante ici puisque l'ancienne URL Usage n'est pas publiée/indexée.

## Gate 2 — JTBD et utilité sans produit

PASS.

Les pages répondent à un job avant de parler de solution. Les alternatives hors E Ink sont conservées lorsque plausibles : papier, ordinateur, tablette LCD, liseuse existante, tablette graphique ou combinaison de plusieurs outils.

Aucune page Usage ne transforme son JTBD en classement de produits.

## Gate 3 — critères et contre-indications

PASS.

Les critères sont dérivés des frictions réelles propres au job :

- Professionnel : IT, interopérabilité, organisation, handoff ;
- Étudiant : supports, PDF, révisions, budget, applications ;
- Réunion : immédiateté, récupération, sortie ;
- Lecture : DRM, annotations, idées indépendantes, récupération ;
- Dessin : outils, calques, surface, couleur, export ;
- Remplacement papier : capture, organisation, sauvegarde, sortie, coût.

Les contre-indications sont explicites et peuvent conduire à ne pas choisir E Ink.

## Gate 4 — preuves et factualité

PASS.

Les facts évolutifs sont adossés à des sources identifiées dans les registres et les pages. Les appréciations/inférences ne sont pas présentées comme des mesures de laboratoire ou une expérience physique propriétaire.

La page Dessin a notamment été rafraîchie avec l'évolution 2026 de Supernote Atelier. Les fonctions BOOX, Kindle, Kobo et reMarkable utilisées pour les handoffs/imports/exports restent attribuées à leurs documentations respectives.

Warning de maintenance : les fonctions cloud, export, OCR et applications créatives sont évolutives et doivent être revérifiées lors d'une future actualisation substantielle.

## Gate 5 — valeur éditoriale et affiliation

PASS.

Les pages restent utiles si tous les liens affiliés sont supprimés. Elles déterminent d'abord si une catégorie d'appareil est appropriée et quand une alternative est meilleure. La sélection de produits reste dans `/comparatifs/`.

## Gate 6 — structure et anti-industrialisation

PASS.

Le principal blocker du CLUSTER_AUDIT est corrigé.

Les architectures finales ne reposent plus sur un ordre réutilisé `workflow → critères → familles → contre-indications → suite` :

- Professionnel : ruptures de continuité → workflows → IT → handoff → limites → choix ;
- Étudiant : supports → remplacement/complement → cassures → arbitrages → révisions → alternatives → produits ;
- Réunion : première minute → décisions/actions → sortie → limites réunions connectées → professionnel ;
- Lecture : entrée → annotation vs idée → récupération → sortie → deux appareils ;
- Dessin : type de dessin → outils 2026 → continuum → couleur → export → limites ;
- Remplacement papier : migration et cycle de vie de la note, conservé en KEEP.

Des composants partagés subsistent (answer box, tableaux, sources, sidebar), ce qui relève du design system et non d'un clonage éditorial.

## Gate 7 — cannibalisation et maillage

PASS.

- Étudiant ↔ comparatif étudiant : rôle distinct ;
- Professionnel ↔ comparatif professionnel : rôle distinct ;
- Professionnel ↔ Réunion : rôles clarifiés et navigation séparée ;
- Lecture ↔ guide liseuse/bloc-notes : rôle recadré ;
- Dessin ↔ guide couleur : rôle distinct ;
- PDF Usage ↔ guide PDF : duplication supprimée par merge ;
- Remplacement papier ↔ guides organisation/export/cloud : relation parent → sous-problèmes conservée.

Le hub `/usages/` présente maintenant six usages actifs et explique que les contraintes de workflow précèdent les comparatifs produits.

## Gate 8 — SEO / technique

PASS pour l'état pré-publication Usage.

- canonical propre sur les six URLs Usage actives ;
- `noindex,follow` conservé ;
- ancienne URL PDF canonicalisée/noindex vers le guide ;
- liens internes vers l'ancienne URL PDF supprimés ;
- date de review mise à jour ;
- taxonomie visible `Par usage` ;
- navigation `Travail` et `Réunions` séparée.

## Résultat par URL

| URL | Résultat après production |
|---|---|
| `/usages/prise-de-notes-professionnelle/` | `PASS — READY_FOR_HUMAN_VALIDATION` |
| `/usages/prise-de-notes-etudiant/` | `PASS — READY_FOR_HUMAN_VALIDATION` |
| `/usages/prise-de-notes-reunion/` | `PASS — READY_FOR_HUMAN_VALIDATION` |
| `/usages/lecture-et-prise-de-notes/` | `PASS — READY_FOR_HUMAN_VALIDATION` |
| `/usages/dessin/` | `PASS — READY_FOR_HUMAN_VALIDATION` |
| `/usages/remplacer-cahiers-papier/` | `PASS` — contenu KEEP déjà humainement approuvé |
| `/usages/annotation-pdf/` | `MERGED` vers `/guides/annoter-pdf-tablette-e-ink/` |

## Next gate

Validation humaine du cluster final.

Aucune URL Usage active ne doit passer en `index,follow` sans instruction explicite distincte d'indexation.