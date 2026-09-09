# Guide CLUSTER_AUDIT — 23 pages restantes

Date: 2026-09-09
Workflow: `guide-analysis-workflow / CLUSTER_AUDIT`
Scope: toutes les pages `/guides/` sauf `/guides/ocr-manuscrit/`, déjà auditée, corrigée et passée en `PASS — READY_FOR_HUMAN_VALIDATION`.

Aucune page du scope n'a été réécrite pendant ce cluster audit. Aucune décision d'indexation n'est prise ici.

## Synthèse

| Décision | Nombre |
|---|---:|
| KEEP | 19 |
| LIGHT_UPDATE | 1 |
| DEEP_REWRITE | 3 |
| MERGE | 0 |
| NOINDEX | 0 |

Le cluster ne présente pas l'industrialisation généralisée observée précédemment sur d'autres catégories. Les guides partagent naturellement quelques conventions éditoriales — réponse initiale, limites, prochaine étape, sources — mais la majorité possède une logique pédagogique propre au sujet.

Le principal signal d'industrialisation est concentré sur les trois pages cloud dédiées : Google Drive, OneDrive et Dropbox. Leurs facts sont utiles et souvent spécifiques, mais leur architecture reste trop clairement dérivée d'un même squelette `niveau/mode d'intégration → fabricants → test → décision`.

---

# Matrice page par page

| URL | Type dominant | Décision | Confiance | Motif principal |
|---|---|---|---|---|
| `/guides/choisir-bloc-notes-numerique/` | CHOICE | KEEP | HIGH | Cadre parent clair : workflow → critères éliminatoires → critères de confort → comparatifs. Ne classe pas directement les produits. |
| `/guides/liseuse-ou-bloc-notes-numerique/` | CHOICE | KEEP | HIGH | Décision de catégorie autonome, fondée sur lecture vs création/organisation/export ; frontière claire avec `/usages/lecture-et-prise-de-notes/`. |
| `/guides/tablette-classique-ou-tablette-e-ink/` | CHOICE / EXPLAINER | KEEP | HIGH | Arbitrage centré sur nature des tâches et comportement de l'écran ; ne duplique ni le comparatif E Ink ni le guide physique de l'encre électronique. |
| `/guides/taille-ecran-bloc-notes-numerique/` | CHOICE | KEEP | HIGH | Critère autonome basé sur document principal, zoom et mobilité ; handoff propre vers le comparatif A4. |
| `/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/` | CHOICE / EXPLAINER | KEEP | HIGH | Décision originale fondée sur perte d'information en niveaux de gris ; distincte du comparatif couleur. |
| `/guides/bloc-notes-numerique-avec-ou-sans-abonnement/` | CHOICE | KEEP | HIGH | Analyse le niveau de dépendance et le plan de sortie plutôt qu'un simple oui/non ; distincte du comparatif sans abonnement. |
| `/guides/prix-bloc-notes-numerique/` | CHOICE | KEEP | HIGH | Référence du coût de configuration et du coût récurrent, avec prix datés et handoff vers comparatifs budget/bons plans. |
| `/guides/tablette-e-ink/` | EXPLAINER | KEEP | HIGH | Explique la catégorie et ses familles ; délègue le mécanisme physique à `encre-electronique-fonctionnement` et le choix de produits au comparatif. |
| `/guides/encre-electronique-fonctionnement/` | EXPLAINER | KEEP | HIGH | Mécanisme physique cohérent et autonome : particules, bistabilité, refresh/ghosting, couleur, front light. |
| `/guides/latence-ecriture/` | EXPLAINER | KEEP | HIGH | Décompose la chaîne de latence et critique correctement les chiffres sans protocole comparable ; logique spécifique au critère. |
| `/guides/autonomie-tablette-e-ink/` | EXPLAINER / CHOICE | KEEP | HIGH | Explique pourquoi l'usage prime sur mAh/« semaines » et fournit un scénario de comparaison utile. |
| `/guides/formats-fichiers-compatibles/` | EXPLAINER / CHOICE | KEEP | HIGH | Très bonne distinction import / lecture / annotation / export / DRM ; sert de parent aux guides PDF/export. |
| `/guides/exporter-notes/` | HOW_TO / CHOICE | KEEP | HIGH | Centré sur le résultat et le format de sortie ; frontière claire avec transfert et synchronisation. |
| `/guides/synchroniser-notes-cloud/` | EXPLAINER / HOW_TO | KEEP | HIGH | Clarifie sync vs copie/export, direction, conflits et sauvegarde ; bon parent des trois guides fournisseurs. |
| `/guides/bloc-notes-numerique-google-drive/` | HOW_TO / COMPATIBILITY | DEEP_REWRITE | HIGH | URL justifiée, facts utiles, mais architecture trop proche des pages OneDrive/Dropbox. Recentrer sur la logique propre à Drive : source vs copie, Kobo/Kindle, app Android et Google ecosystem. |
| `/guides/bloc-notes-numerique-onedrive/` | HOW_TO / COMPATIBILITY | DEEP_REWRITE | HIGH | URL justifiée, mais même squelette fournisseur. Recentrer sur Microsoft 365, tenants, autorisations, MFA, OneNote/Office et workflow entreprise. |
| `/guides/bloc-notes-numerique-dropbox/` | HOW_TO / COMPATIBILITY | DEEP_REWRITE | HIGH | URL justifiée, mais architecture fournisseur répétée. Recentrer sur neutralité fichiers, arborescence, sync de dossiers et usage multi-plateforme. |
| `/guides/ecosysteme-ouvert-ou-ferme/` | CHOICE / EXPLAINER | KEEP | HIGH | Sépare correctement ouverture applicative et portabilité des données ; arbitrage spécialisé vs Android réellement distinct. |
| `/guides/annoter-pdf-tablette-e-ink/` | HOW_TO / CHOICE | KEEP | HIGH | Page consolidée et forte : fichier entrant → lisibilité → outils → export → méthode. La fusion de l'ancienne page Usage PDF renforce son rôle. |
| `/guides/convertir-notes-manuscrites-en-texte/` | HOW_TO | LIGHT_UPDATE | HIGH | URL distincte de l'OCR après correction de celui-ci, mais resserrer le rôle procédural et remplacer les formulations Kindle « modèles récents » par la qualification exacte 2025+ lorsque nécessaire. |
| `/guides/organiser-notes-numeriques/` | HOW_TO | KEEP | HIGH | Méthode documentaire autonome : retrouver, dossiers, titres, tags/liens, inbox et archives. Ne dépend pas d'un produit. |
| `/guides/transfert-notes-vers-ordinateur/` | HOW_TO | KEEP | HIGH | Se concentre sur les canaux de transfert et la confidentialité ; l'export reste correctement délégué au guide voisin. |
| `/guides/imprimer-notes-numeriques/` | HOW_TO | KEEP | HIGH | Guide étroit mais justifié : export intermédiaire, dimensions, couleur, test papier et impression. Pas de duplication substantielle avec export/transfert. |

---

# Analyse des frontières internes

## Guide général vs comparatifs

`/guides/choisir-bloc-notes-numerique/` doit rester le cadre de décision : identifier les contraintes avant d'ouvrir les comparatifs. Sa matrice de familles ne constitue pas un ranking et le handoff vers `/comparatifs/meilleur-bloc-notes-numerique/` est cohérent.

Les guides Taille, Couleur, Abonnement et Prix possèdent également chacun une question autonome et renvoient ensuite au comparatif spécialisé lorsque le lecteur a besoin de choisir des modèles.

Aucun merge avec `/comparatifs/` n'est recommandé.

## Tablette E Ink vs fonctionnement de l'encre électronique

Les deux URLs restent justifiées :

- `/guides/tablette-e-ink/` = comprendre la catégorie d'appareil, ses familles et ses compromis pratiques ;
- `/guides/encre-electronique-fonctionnement/` = comprendre le mécanisme électrophorétique, la bistabilité, le refresh et la couleur.

La première renvoie explicitement à la seconde pour la physique détaillée. `KEEP` pour les deux.

## Formats vs annotation PDF vs export

La hiérarchie est saine :

- Formats = que signifie réellement « compatible » ;
- Annotation PDF = effectuer et restituer un workflow PDF ;
- Export = choisir la sortie d'une note/carnet ;
- Transfert = déplacer cette sortie vers un ordinateur ;
- Impression = produire une sortie papier.

Ces pages se citent mais ne répondent pas à la même tâche. Aucun merge.

## OCR vs conversion manuscrite

La correction de `/guides/ocr-manuscrit/` clarifie désormais le rôle : choisir/comprendre la fonction de reconnaissance. `/guides/convertir-notes-manuscrites-en-texte/` reste la procédure de transformation et correction jusqu'au fichier final.

La page Conversion conserve encore quelques formulations proches de l'ancien OCR et un claim Kindle générique « modèles récents ». `LIGHT_UPDATE`, pas de merge.

## Cloud générique vs fournisseurs

`/guides/synchroniser-notes-cloud/` est un bon parent conceptuel : sync, direction, conflits, sauvegarde et copie.

Les trois URLs fournisseur sont sémantiquement légitimes. Elles ont de vraies différences :

- Google Drive : Kobo/Kindle, source vs copie, intégration Android ;
- OneDrive : Microsoft 365, tenant, permissions entreprise, OneNote/Office ;
- Dropbox : neutralité fichiers, dossiers et usage multi-plateforme.

Le problème n'est donc **pas la cannibalisation de sujet** mais la construction éditoriale encore trop symétrique. Garder les URLs, reconstruire les architectures.

---

# Similarité structurelle du cluster

## Similarités acceptables

Plusieurs Guides se terminent par une règle de décision ou une prochaine étape et possèdent une section Sources. Cela correspond à la fonction éditoriale du site et ne suffit pas à constituer une industrialisation.

Les tableaux sont également utilisés lorsque la question se prête réellement à une grille : taille, couleur, formats, autonomie, etc. Ils ne contiennent pas les mêmes critères ni la même fonction sémantique.

## Similarité problématique

Les pages Google Drive, OneDrive et Dropbox conservent un motif visible :

1. expliquer ce que signifie la compatibilité avec le service ;
2. présenter une matrice de modes/niveaux ;
3. passer en revue des fabricants ;
4. proposer un test ;
5. conclure par le rôle du service dans le choix.

Le contenu propre au service existe, mais l'architecture semble encore avoir été décidée avant le research spécifique. Cela justifie `DEEP_REWRITE` au sens structurel du workflow.

`DEEP_REWRITE` ne signifie pas repartir de zéro : les facts, sources, limites, exemples fabricants et distinctions import/export/sync actuels doivent être préservés lorsqu'ils restent vérifiés.

---

# Priorité de correction recommandée

1. `/guides/bloc-notes-numerique-onedrive/` — plus grande opportunité de différenciation via entreprise/Microsoft 365/permissions.
2. `/guides/bloc-notes-numerique-google-drive/` — différencier autour de source/copie, Kobo/Kindle et Android.
3. `/guides/bloc-notes-numerique-dropbox/` — différencier autour des dossiers, neutralité et flux multi-plateforme.
4. `/guides/convertir-notes-manuscrites-en-texte/` — `LIGHT_UPDATE` après le nouvel OCR.

Les 19 `KEEP` ne doivent pas être réécrits par réflexe. Une future passe de fraîcheur peut corriger un fact évolutif sans changer leur décision structurelle.

---

# Hub `/guides/`

Le hub liste actuellement les 24 guides dans une grille plate. Ce point n'entraîne aucune décision de contenu individuelle, mais la prochaine revue design/IA devrait probablement regrouper les entrées par fonction : choisir, comprendre la technologie, fichiers/export, cloud, méthodes de travail.

---

# Indexation

Toutes les pages Guide restent actuellement sous la politique de brouillon `noindex,follow`.

Le présent CLUSTER_AUDIT n'autorise aucune indexation. Chaque page corrigée doit ensuite passer par :

`guide-content-workflow` → `guide-analysis-workflow / PUBLISH_REVIEW` → validation humaine → instruction explicite d'indexation.

## Conclusion

`19 KEEP / 1 LIGHT_UPDATE / 3 DEEP_REWRITE / 0 MERGE / 0 NOINDEX`

Le cluster est globalement solide. La correction prioritaire est qualitative et structurelle, concentrée sur les trois guides cloud fournisseur, et non une réécriture massive des Guides.
