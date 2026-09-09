---
name: brand-editorial-publish-gate
description: Gate éditorial final obligatoire pour les pages /marques/ de bloc-notes-numeriques.fr. Évalue l'intention, la valeur originale, les preuves, la confiance/E-E-A-T, la qualité GEO, la pertinence éditoriale, le ton français, les signaux de contenu générique ou AI-slop, le SEO éditorial et la préparation à la publication. Ne réécrit pas automatiquement une page en échec.
---

# Brand Editorial Publish Gate

## Rôle

Ce skill est la dernière barrière éditoriale avant publication d'une page sous `/marques/`.

Il ne sert pas à produire davantage de texte. Il sert à décider si une page mérite d'être publiée.

Une page `FAIL` reste en `noindex,follow` et retourne vers la phase de correction concernée. Une page ne peut passer en indexation qu'après `PASS` de ce gate et validation humaine explicite.

## Principe central

Évaluer la page comme un lecteur et non comme un livrable SEO.

La page doit accomplir son rôle sans expliquer sa propre stratégie éditoriale. Le texte final ne doit pas parler de « page marque », de « hub », de « maillage », de « contenu », de « SEO », de « GEO », d'« intention de recherche » ou de la manière dont l'article a été construit, sauf lorsqu'une information méthodologique est réellement utile au lecteur (par exemple expliquer qu'une analyse repose sur de la documentation plutôt que sur un test physique).

La présence de H2, de liens, de tableaux ou de mots-clés n'est jamais une preuve de qualité en soi.

---

# Entrées obligatoires

Lire avant l'audit :

- `AGENTS.md` ;
- `brand-workflow.config.yaml` ;
- `.agents/skills/brand-content-workflow/SKILL.md` ;
- la page cible complète ;
- son type dans `brand_pages.py` ;
- les données de preuve associées dans `.content/brands/` quand elles existent ;
- les pages voisines susceptibles de cannibaliser la même intention ;
- les sources utilisées pour les affirmations susceptibles d'évoluer.

Réutiliser, quand pertinent, les skills existants :

- `search-intent`
- `affiliate-value`
- `fact-check`
- `internal-linking-audit`
- `natural-writing`
- `humanizer`
- `general-writing`
- `anti-ai-slop`
- `seo-best-practices`
- `editorial-qa`

Les anciens skills provenant d'autres projets servent de grille de contrôle, pas de source de ton, de langue ou de règles spécifiques à leur ancien domaine.

---

# Gate 0 — Contrat de page

Identifier avant toute évaluation :

- type : `DIRECTORY`, `BRAND_HUB`, `PRODUCT`, `REVIEW`, `SERVICE`, `ACCESSORY_HUB` ou `ALTERNATIVES` ;
- question ou décision principale du lecteur ;
- ce que cette URL doit apporter que les autres URLs du site n'apportent pas ;
- niveau de preuve disponible : documentation officielle, sources tierces, retours utilisateurs sourcés, test réel.

FAIL si le rôle de la page ne peut pas être formulé en une phrase claire ou s'il chevauche essentiellement une autre page existante.

---

# Gate 1 — Intention et pertinence

PASS lorsque :

- l'information attendue arrive assez tôt ;
- chaque grande section répond à une question réelle du lecteur ou modifie une décision ;
- le contenu ne dérive pas vers un guide générique, un comparatif complet ou une fiche constructeur ;
- la page respecte la frontière entre `/marques/`, `/comparatifs/`, `/guides/` et `/usages/` ;
- aucune section n'existe uniquement pour placer une variante de mot-clé, un lien interne ou un nombre arbitraire de sous-titres.

Questions de contrôle :

1. Que comprend ou décide le lecteur après cette section qu'il ne pouvait pas comprendre avant ?
2. Si la section disparaît, la page perd-elle réellement de la valeur ?
3. Le passage répond-il au lecteur ou explique-t-il le travail de l'éditeur ?

Tout passage de métadiscours éditorial inutile est un blocker.

---

# Gate 2 — Valeur originale et utilité

Appliquer le principe :

> La page doit rester utile si tous les liens affiliés sont supprimés.

PASS lorsque la page apporte au moins une vraie couche d'interprétation au-delà des sources fabricant :

- conséquences pratiques d'une caractéristique ;
- compatibilités ou incompatibilités importantes ;
- compromis ;
- contexte de gamme ou génération ;
- coûts ou dépendances qui changent la décision ;
- alternatives pertinentes avec raison explicite ;
- distinction entre caractéristiques importantes et secondaires.

FAIL si la page est essentiellement une reformulation de fiches officielles, un catalogue d'avantages/inconvénients génériques ou une succession de tableaux sans interprétation.

Ne jamais fabriquer de valeur originale en inventant une expérience, une mesure, un consensus utilisateur ou une précision non sourcée.

---

# Gate 3 — Preuves et factualité

Extraire les affirmations importantes et les classer :

- `VERIFIED` : confirmé par une source primaire ou documentation officielle ;
- `SUPPORTED` : soutenu par une source fiable mais indirecte ;
- `INFERRED` : interprétation éditoriale raisonnable à partir de faits cités ;
- `UNKNOWN` : non vérifié ;
- `OUTDATED` : ancien ou plus applicable ;
- `CONTRADICTED` : contredit par une meilleure source.

PASS lorsque :

- les caractéristiques, générations, compatibilités, services, prix lorsqu'ils sont mentionnés et statuts produit sont vérifiés ;
- les comparaisons factuelles sont démontrables ;
- les interprétations sont reconnaissables comme telles ;
- les incertitudes restent visibles ;
- les informations volatiles ont une date de vérification exploitable.

FAIL si une affirmation importante est `UNKNOWN`, `OUTDATED` ou `CONTRADICTED` sans qualification claire.

---

# Gate 4 — Trust / E-E-A-T observable

Ne pas ajouter artificiellement des phrases d'autorité ou d'expertise.

Évaluer uniquement des signaux observables de confiance :

- qui porte la responsabilité éditoriale peut être identifié au niveau du site ou de la page ;
- la méthode est compréhensible lorsque le type de page l'exige ;
- les sources importantes sont traçables ;
- le niveau de preuve est honnête ;
- affiliation et intérêt commercial sont transparents ;
- les limites sont aussi visibles que les bénéfices ;
- une analyse documentaire n'est jamais présentée comme un test ;
- une expérience utilisateur externe n'est jamais transformée en expérience propre ;
- les recommandations ont des critères compréhensibles.

Pour une `REVIEW` sans test physique, la page doit expliciter sobrement qu'il s'agit d'une analyse documentaire ou éditoriale. Elle ne doit pas imiter le langage d'un test hands-on.

FAIL en cas de faux signal d'expérience, d'autorité fabriquée ou de méthodologie trompeuse.

---

# Gate 5 — GEO / qualité des entités

Le GEO n'est pas une excuse pour ajouter des FAQ, des définitions ou des répétitions artificielles.

PASS lorsque :

- les entités principales sont nommées sans ambiguïté ;
- les relations utiles sont explicites : `marque -> produit`, `produit -> technologie`, `produit -> usage`, `service -> fonction`, `accessoire -> compatibilité`, `marque -> alternative` ;
- les passages importants peuvent être compris hors contexte immédiat sans dépendre d'un vague « il », « celui-ci » ou « cette solution » ;
- les faits et les conséquences sont reliés dans des phrases claires ;
- les distinctions entre générations et modèles sont explicites ;
- la page contient des informations suffisamment précises pour être citées sans devenir télégraphique ou répétitive.

FAIL si l'optimisation GEO produit du texte artificiel, une accumulation de définitions évidentes ou des formulations écrites pour un moteur plutôt que pour une personne.

---

# Gate 6 — Ton, registre et pertinence éditoriale

Voix cible pour bloc-notes-numeriques.fr :

- français naturel ;
- média éditorial spécialisé ;
- précis et sobre ;
- compétent sans posture d'expert auto-proclamé ;
- utile à quelqu'un qui choisit, utilise ou compare un bloc-notes numérique ;
- ni discours de consultant SEO, ni fiche marketing de marque, ni catalogue marchand.

FAIL notamment pour :

- métadiscours : « cette page doit », « une page marque sert à », « cette section permet de », « pour le SEO/GEO », « le maillage » ;
- commentaires destinés au propriétaire du site plutôt qu'au lecteur ;
- phrases qui décrivent l'architecture éditoriale au lieu de donner l'information ;
- ton promotionnel sans preuve ;
- abstractions vagues ;
- transitions de remplissage ;
- répétition mécanique de la même structure dans chaque section.

Préférer un fait concret ou une conséquence pratique à une phrase d'encadrement.

---

# Gate 7 — Anti-AI-slop et naturalité

Utiliser `anti-ai-slop`, puis `humanizer`/`natural-writing` seulement sur les passages réellement problématiques.

Rechercher notamment :

- introductions qui reformulent simplement le H1 ;
- phrases génériques applicables à n'importe quelle marque ;
- paragraphes de longueur et de rythme trop uniformes ;
- séries systématiques de trois éléments sans raison ;
- symétrie artificielle avantages / limites ;
- « il est important de », « il convient de », « en conclusion », « dans un monde où », « que vous soyez » ;
- surusage de « cohérent », « pertinent », « essentiel », « clé », « se distingue », « écosystème » lorsque ces mots remplacent une explication concrète ;
- conclusions qui résument sans ajouter de décision ;
- listes créées uniquement pour donner une impression de structure ;
- répétitions de patrons identiques entre plusieurs pages du même type.

La correction doit préserver les faits, l'intention, les liens utiles et le niveau de preuve. Elle ne doit jamais ajouter des détails inventés pour rendre le texte « plus humain ».

FAIL si des signaux `HIGH` d'anti-AI-slop restent dans le corps principal.

---

# Gate 8 — SEO éditorial

Contrôler sans quota artificiel :

- title, H1 et sujet principal cohérents ;
- réponse alignée sur l'intention ;
- H2/H3 correspondant à de vrais sous-problèmes ;
- absence de keyword stuffing ;
- absence de section créée uniquement pour un synonyme ;
- ancres internes descriptives et contextuelles ;
- maillage limité aux prochaines étapes réellement utiles ;
- risque de cannibalisation traité ;
- données structurées cohérentes avec le contenu réellement visible ;
- canonical, robots et métadonnées corrects.

Ne jamais imposer un nombre minimum de mots, de H2, de tableaux ou de liens internes comme critère de qualité.

---

# Gate 9 — Contrôle par type de page

## DIRECTORY

Le lecteur doit pouvoir comprendre les différences entre marques et choisir où poursuivre. Ne pas transformer la page en mini-comparatif exhaustif.

## BRAND_HUB

Doit expliquer la logique de la marque, la gamme actuelle, les différences de générations importantes, l'écosystème et les limites qui changent le choix. Le hub route naturellement vers les sous-pages sans expliquer qu'il « sert de hub ».

## PRODUCT

Doit répondre à la question « est-ce que ce modèle convient à mon besoin ? ». Prioriser les caractéristiques qui changent réellement l'achat, les compatibilités, les limites et les alternatives.

## REVIEW

Doit produire un jugement éditorial argumenté proportionnel au niveau de preuve. Sans test réel, ne pas simuler une expérience de test. Les forces et limites doivent découler d'éléments précis, pas de catégories génériques.

## SERVICE

Doit expliquer ce qui est inclus, ce qui reste possible sans le service, les dépendances, coûts ou limites et dans quels cas le service change réellement le workflow.

## ACCESSORY_HUB

Doit clarifier compatibilités, accessoires nécessaires ou optionnels et coût total. Éviter le catalogue d'accessoires sans contexte.

## ALTERNATIVES

Doit commencer par les raisons concrètes de quitter l'écosystème, puis proposer les alternatives selon ces raisons. Ne pas refaire un classement générique déjà traité dans `/comparatifs/`.

---

# Gate 10 — Publication

Statuts possibles :

- `PASS`
- `FAIL`

Aucun score moyen ne peut compenser un blocker.

## Blockers absolus

- faux test ou fausse expérience ;
- affirmation importante non vérifiée présentée comme certaine ;
- métadiscours éditorial manifeste dans le contenu utilisateur ;
- contenu essentiellement dérivé d'un marchand sans valeur ajoutée ;
- cannibalisation forte non résolue ;
- intention principale non satisfaite ;
- signaux anti-AI-slop de sévérité `HIGH` non corrigés ;
- absence de transparence sur le niveau de preuve d'une review ;
- page indexable avant validation humaine explicite.

## Output obligatoire

```md
# Brand editorial publish gate

URL: ...
Page type: ...
Status: PASS | FAIL

## Blockers
- ...

## Gate results
- Intent & relevance: PASS | FAIL
- Original value: PASS | FAIL
- Evidence & factuality: PASS | FAIL
- Trust / E-E-A-T: PASS | FAIL
- GEO / entities: PASS | FAIL
- Tone & editorial relevance: PASS | FAIL
- Anti-AI-slop: PASS | FAIL
- SEO editorial: PASS | FAIL
- Page-type fit: PASS | FAIL

## Required corrections
1. ...

## Residual risks
- ...

## Publication decision
KEEP NOINDEX | READY FOR HUMAN VALIDATION
```

Un `FAIL` ne déclenche pas automatiquement une réécriture complète. Retourner uniquement vers les skills correspondant aux gates en échec, corriger, puis relancer le publish gate.
