# Comparison PUBLISH_REVIEW — cluster `/comparatifs/`

Date : 9 septembre 2026  
Workflow : `comparison-analysis-workflow` — mode `PUBLISH_REVIEW`  
Scope : les 13 URLs classées `DEEP_REWRITE` par le `CLUSTER_AUDIT`  
Référence déjà validée : `/comparatifs/meilleur-bloc-notes-numerique/`

# Résultat global

**PASS — READY_FOR_HUMAN_VALIDATION**

Les 13 pages ont été réécrites via `comparison-content-workflow`, avec evidence/brief spécifique, source éditoriale bespoke, registre de décision sans scoring obligatoire, puis contrôle machine et review éditoriale.

Le run GitHub Actions `Regenerate comparison cluster` #24 (`34353732632`) a exécuté :

1. application des contenus sur les 14 pages ;
2. préservation des métadonnées méthodologiques ;
3. `validate_comparisons.py` ;
4. résultat : `PASS: comparison pages have no machine-detectable publication blockers`.

Le validateur confirme également que scoring, poids, ranking et TSC sont optionnels.

Toutes les pages restent en `noindex,follow`.

---

# Gates transversaux

## Intent / rôle — PASS

Les frontières de cluster issues du `CLUSTER_AUDIT` sont respectées :

- `meilleur-bloc-notes-numerique` reste notebook-first ;
- `tablette-e-ink` est tablet-first / polyvalence ;
- pro et étudiant choisissent des produits après le cadrage d'usage ;
- couleur, A4, sans abonnement et budget répondent à des contraintes distinctes ;
- les head-to-head répondent à des choix explicites entre écosystèmes/marques.

Aucun merge supplémentaire n'est nécessaire à ce stade.

## Evidence / factualité — PASS avec freshness warnings

- facts produits : sources fabricant en priorité ;
- jugements d'usage : sources indépendantes nommées quand nécessaires ;
- aucun test physique propriétaire revendiqué ;
- incertitudes de prix, bundle et disponibilité conservées dans le texte ;
- les anciens scores `VERIFIED` ont été supprimés des 13 registres réécrits.

Warnings de fraîcheur : gammes BOOX/Kindle/reMarkable, prix régionaux, bundles Kobo, disponibilité Fujitsu Quaderno.

## Affiliate value — PASS

Chaque page conserve une décision utile si les liens affiliés disparaissent :

- choix conditionnels ;
- limites explicites ;
- situations où un autre appareil devient meilleur ;
- prix/bundles qualifiés ;
- pas de classement influencé par une commission.

## Anti-AI-slop / structure cluster — PASS

Le renderer historique n'est plus utilisé par les 14 URLs existantes. Il ne reste qu'en safety fallback pour un futur slug non migré.

Contrôle des architectures finales :

- A4 : définition du format → routes grand format → Note Max → Tab X C → Quaderno → compromis compact ;
- sans abonnement : définition du coût récurrent → fonctions gratuites → Supernote → BOOX → reMarkable → règle de décision ;
- budget : deux types de gagnants budget → configurations → PocketBook → Paper Pure → bundles → occasion ;
- reMarkable vs BOOX : philosophie → priorités → modèles équivalents → écriture → cloud → verdict ;
- reMarkable vs Supernote : vieillissement des notes → choix → duel Pure/Manta → gammes → abonnement → verdict ;
- BOOX vs Supernote : rôle de chaque écosystème → après l'écriture → duel proche → Note Air5 C → long terme → verdict ;
- tablette E Ink : familles de produit → Note Air5 C → Android → alternatives → couleur ;
- professionnel : après la réunion → workflows → Go Lumi → Paper Pure → Manta → clavier ;
- étudiant : supports de cours → sélection → budget → PDF → apps → lecture ;
- couleur : utilité de la couleur → quatre approches → Air5 C → Paper Pro → Scribe → Move ;
- Kindle vs reMarkable : décision courte → origine des deux produits → lecture → notes → générations → cloud ;
- Kindle vs Kobo : bibliothèque → différences → Kindle → Kobo → PDF ;
- Kobo vs reMarkable : job principal → face-à-face → Elipsa → Pure → Paper Pro → verdict.

Ces différences sont substantielles et découlent des décisions propres à chaque URL, pas d'une substitution de produits dans le même plan.

## SEO/on-page — PASS en état draft/noindex

- title spécifique par page ;
- H1 spécifique ;
- lead spécifique ;
- un seul H1 ;
- canonical conforme ;
- sources externes visibles ;
- liens internes présents lorsqu'ils répondent à une prochaine question ;
- aucun quota de H2, mots ou liens utilisé comme gate.

## Technical — PASS

`validate_comparisons.py` a passé le cluster. `apply_comparison_content.py` hard-fail si `noindex,follow` disparaît.

---

# Revue URL par URL

## `/comparatifs/bloc-notes-numerique-a4/`

**PASS — READY_FOR_HUMAN_VALIDATION**

- Intent : PASS
- Evidence : PASS
- Affiliate value : PASS
- Structure : PASS
- Technical : PASS
- Warning : Fujitsu Quaderno techniquement pertinent mais disponibilité/garantie France à revérifier.

## `/comparatifs/bloc-notes-numerique-sans-abonnement/`

**PASS — READY_FOR_HUMAN_VALIDATION**

- distingue appareil, cloud et services tiers ;
- Supernote/BOOX/reMarkable traités avec nuances ;
- prix/fonctions Connect freshness-sensitive.

## `/comparatifs/bloc-notes-numerique-pas-cher/`

**PASS — READY_FOR_HUMAN_VALIDATION**

- coût de configuration plutôt que prix nu ;
- PocketBook vs Paper Pure répond à deux décisions budget distinctes ;
- warning : prix et bundle doivent rester fraîchement vérifiés.

## `/comparatifs/remarkable-vs-boox/`

**PASS — READY_FOR_HUMAN_VALIDATION**

- marque-vs-marque réellement couvert ;
- pas de gagnant universel ;
- gammes et équivalences qualifiées.

## `/comparatifs/remarkable-vs-supernote/`

**PASS — READY_FOR_HUMAN_VALIDATION**

- simplicité vs knowledge notebook ;
- couleur/front light et abonnement traités comme discriminants ;
- expérience d'écriture non présentée comme mesure propriétaire.

## `/comparatifs/boox-vs-supernote/`

**PASS — READY_FOR_HUMAN_VALIDATION**

- ouverture Android vs spécialisation manuscrite ;
- largeur de gamme BOOX intégrée ;
- verdict conditionnel explicite.

## `/comparatifs/tablette-e-ink/`

**PASS — READY_FOR_HUMAN_VALIDATION**

- rôle distinct du comparatif général ;
- structure par familles de tablette ;
- Note Air5 C recommandé pour polyvalence, pas comme meilleur carnet universel.

## `/comparatifs/bloc-notes-numerique-professionnel/`

**PASS — READY_FOR_HUMAN_VALIDATION**

- workflow après réunion au centre ;
- Paper Pure/Manta/BOOX répondent à des situations professionnelles différentes ;
- warning : aucune conclusion de conformité IT/sécurité universelle.

## `/comparatifs/bloc-notes-numerique-etudiant/`

**PASS — READY_FOR_HUMAN_VALIDATION**

- supports de cours avant marque ;
- budget et format PDF pris en compte ;
- pas de persona étudiant artificiellement unique.

## `/comparatifs/bloc-notes-numerique-couleur/`

**PASS — READY_FOR_HUMAN_VALIDATION**

- couleur évaluée selon son utilité ;
- formats/apps/lecture/mobilité produisent des recommandations distinctes ;
- aucun postulat couleur = meilleure écriture.

## `/comparatifs/kindle-scribe-vs-remarkable/`

**PASS — READY_FOR_HUMAN_VALIDATION**

- reader-first vs notebook-first ;
- générations Kindle actuelles qualifiées ;
- verdict conditionnel.

## `/comparatifs/kindle-scribe-vs-kobo-elipsa/`

**PASS — READY_FOR_HUMAN_VALIDATION**

- bibliothèque existante comme critère principal ;
- pas de faux vainqueur universel ;
- warning : bundle Kobo Stylus 2 à vérifier au panier.

## `/comparatifs/kobo-elipsa-vs-remarkable/`

**PASS — READY_FOR_HUMAN_VALIDATION**

- reader-first vs notebook-first très explicite ;
- Paper Pro traité comme variation de besoin et non comme simple upgrade dans le duel.

---

# Risques résiduels non bloquants

1. **Prix et bundles** — plusieurs marques modifient fréquemment prix, promos et contenu de boîte.
2. **Régions** — BOOX/Supernote peuvent afficher des prix en dollars et Fujitsu est plus difficile à acheter directement en France.
3. **Gammes rapides** — BOOX et Kindle évoluent vite ; revalider génération et disponibilité lors d'une actualisation future.
4. **Hands-on** — aucun test physique propriétaire n'est revendiqué. Un futur test interne devra être documenté séparément avant d'ajouter une expérience à la première personne.
5. **Kobo Stylus 2** — wording de bundle pas parfaitement cohérent entre pages officielles consultées ; conserver la demande de vérification au panier.

# Gate indexation

Le cluster est **READY_FOR_HUMAN_VALIDATION**, mais reste intégralement `noindex,follow`.

Ne rendre une URL indexable qu'après :

1. validation humaine explicite de la page ou du lot ;
2. instruction explicite de retirer le noindex pour la ou les URLs concernées.
