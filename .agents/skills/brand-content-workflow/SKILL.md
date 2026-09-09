---
name: brand-content-workflow
description: Workflow générique pour créer, récupérer, structurer et valider des pages marque SEO/GEO à forte valeur éditoriale et commerciale. Utiliser pour les hubs de marque, pages produit, analyses/reviews, services, accessoires et alternatives. Le workflow impose une cartographie d'entités, une gamme actuelle vérifiée, un ecosystem map, un positionnement de marque explicite et une QA spécifique aux pages commerciales sans inventer de tests ni d'expérience produit.
---

# Brand Content Workflow

## Objectif

Construire des pages marque qui aident réellement un lecteur à comprendre une marque, un produit ou un écosystème et à prendre une décision informée.

Une bonne page marque doit permettre de comprendre, selon son type :

> Quels produits sont actuellement dans la gamme ?  
> Quelle est la logique de l'écosystème ?  
> Quelles différences changent réellement la décision ?  
> Pour quels usages la marque ou le produit est-il adapté ou non ?  
> Quelle est la prochaine information utile à consulter ?

Principe central :

> **Entités avant prose. Gamme actuelle avant recommandation. Écosystème avant positionnement. Valeur lecteur avant structure SEO.**

La prose finale ne doit jamais expliquer au lecteur la stratégie éditoriale de la page. Les notions de hub, maillage, SEO, GEO, intention ou architecture servent au travail interne, pas au texte publié.

---

# 1. Entrées obligatoires

Lire avant toute production :

- instructions du repo (`AGENTS.md`, `README`, etc.) ;
- `brand-workflow.config.yaml` ;
- page cible existante ;
- source de vérité éditoriale ;
- architecture des pages marque ;
- pages produits associées ;
- pages comparatifs associées ;
- pages guides / usages associées ;
- données sémantiques si disponibles ;
- informations officielles actuelles de la marque ;
- page de référence qualitative définie par `quality_reference` ;
- `.agents/skills/brand-editorial-publish-gate/SKILL.md` avant la validation finale.

Réutiliser les skills existants lorsqu'ils sont présents :

- `search-intent`
- `content-refresh`
- `affiliate-value`
- `fact-check`
- `internal-linking-audit`
- `natural-writing`
- `humanizer`
- `general-writing`
- `anti-ai-slop`
- `seo-drift`
- `seo-technical`
- `seo-best-practices`
- `editorial-qa`
- `comparison-content-workflow`
- `guide-content-workflow`
- `brand-editorial-publish-gate`

Les skills hérités d'un autre projet servent de grille méthodologique. Ne pas reprendre leur langue, leur domaine, leurs exemples ou leurs quotas éventuels comme contraintes de rédaction pour bloc-notes-numeriques.fr.

---

# 2. Routing obligatoire

Classer la page avant de rédiger.

## DIRECTORY

Fonction :
- aider à comprendre les grandes différences entre marques ;
- orienter vers la marque ou le type de produit pertinent ;
- éviter de reproduire un comparatif exhaustif.

## BRAND_HUB

Exemple :

`/marques/remarkable/`

Fonction :
- définir la marque ;
- présenter la gamme actuelle ;
- cartographier l'écosystème ;
- expliquer les forces et limites qui changent réellement le choix ;
- orienter naturellement vers les produits, comparatifs, guides ou usages pertinents.

## PRODUCT

Exemple :

`/marques/remarkable/paper-pro/`

Fonction :
- présenter un produit précis ;
- vérifier sa génération et son statut ;
- expliquer les caractéristiques qui changent réellement la décision ;
- montrer à qui il convient ou non ;
- relier vers comparatifs et alternatives lorsque cela aide le lecteur.

## REVIEW

Exemple :

`/marques/remarkable/paper-pro-avis/`

Fonction :
- analyser un produit ;
- distinguer clairement desk research, prise en main et test réel ;
- présenter un jugement éditorial proportionnel au niveau de preuve ;
- expliquer les forces, limites, usages et alternatives sans simuler un test.

Si aucun test réel n'existe :
- ne pas utiliser de langage de test ;
- ne pas présenter de scores mesurés ;
- utiliser « analyse documentaire », « analyse éditoriale » ou équivalent lorsque cette précision est nécessaire ;
- ne pas répéter cette précaution dans chaque section.

## SERVICE

Exemple :

`/marques/remarkable/connect/`

Fonction :
- expliquer un service, abonnement ou logiciel ;
- détailler ce qui est inclus ou non ;
- expliquer le coût, les limites, l'impact sur le workflow et la dépendance éventuelle.

## ACCESSORY_HUB

Exemple :

`/marques/remarkable/accessoires/`

Fonction :
- expliquer les catégories d'accessoires ;
- distinguer nécessaires, utiles et optionnels lorsque cette distinction est pertinente ;
- vérifier les compatibilités ;
- éviter le catalogue sans contexte.

## ALTERNATIVES

Exemple :

`/marques/remarkable/alternatives/`

Fonction :
- expliquer dans quels cas une autre marque ou un autre écosystème répond mieux au besoin ;
- identifier les alternatives cohérentes selon la raison du changement ;
- déléguer une comparaison détaillée à `comparison-content-workflow` lorsque pertinent.

---

# 3. Mode RECOVERY ou NEW_CONTENT

## RECOVERY

Si une page existe déjà :

Conserver :
- faits toujours valides ;
- structure réellement utile ;
- liens pertinents ;
- passages différenciants ;
- tableaux qui simplifient une décision.

Réparer ou supprimer :
- gamme obsolète ;
- entités manquantes ;
- services mal expliqués ;
- positionnement trop vague ;
- maillage pauvre ou artificiel ;
- contenu trop promotionnel ;
- sections ajoutées uniquement pour allonger la page ;
- liens vers anciens modèles non contextualisés ;
- produits discontinués présentés comme actuels ;
- métadiscours éditorial ;
- répétitions de patrons entre pages ;
- phrases génériques qui pourraient s'appliquer à presque n'importe quelle marque.

## NEW_CONTENT

Si page vide ou inexistante :
- produire d'abord les données structurées et le cadrage ;
- déterminer les questions réellement nécessaires ;
- rédiger ensuite sans transformer le cadrage interne en texte utilisateur.

---

# 4. Entity Map obligatoire

Créer avant rédaction :

```yaml
brand:
products:
services:
software:
technologies:
accessories:
integrations:
formats:
use_cases:
competitors:
```

Pour chaque relation importante, expliciter :

`BRAND -> PRODUCT`  
`PRODUCT -> TECHNOLOGY`  
`PRODUCT -> USE_CASE`  
`BRAND -> SOFTWARE`  
`BRAND -> SERVICE`  
`SERVICE -> FEATURE`  
`BRAND -> INTEGRATION`  
`BRAND -> COMPETITOR`

La page ne doit pas seulement contenir les mots : elle doit expliquer leurs relations lorsque celles-ci aident le lecteur.

---

# 5. Current Product Range

Construire la gamme actuelle.

Statuts possibles :

- `CURRENT`
- `PREVIOUS_GENERATION`
- `DISCONTINUED`
- `ANNOUNCED`
- `REGION_SPECIFIC`
- `UNKNOWN`

Pour chaque produit :

- nom exact ;
- génération ;
- date ou période de lancement si utile ;
- statut ;
- taille ;
- technologie ;
- fonctions principales ;
- compatibilités ;
- accessoires ;
- prix actuel si utilisé ;
- source officielle ;
- date de vérification.

Une page hub ne peut pas mélanger générations actuelles et anciennes sans les distinguer.

---

# 6. Brand Proposition

Formuler une proposition interne claire :

> Quelle est la logique propre de cette marque ?

La proposition doit venir de faits vérifiables.

Dimensions possibles : spécialisation, ouverture logicielle, simplicité, lecture, écriture, organisation, cloud, applications tierces, couleur, accessoires et services.

Ne jamais écrire qu'une marque est « la meilleure » sans critères ou comparaison documentée. Préférer une formulation conditionnelle reliant positionnement, usage et limites.

La « proposition de marque » est un outil de cadrage. Elle ne doit pas être injectée telle quelle dans le texte si elle sonne comme un brief marketing ou SEO.

---

# 7. Ecosystem Map

Construire le parcours fonctionnel :

```text
Hardware
↓
Stylus
↓
OS
↓
Notes
↓
PDF
↓
OCR
↓
Cloud
↓
Export
↓
Third-party services
```

Pour chaque étape :
- ce qui est natif ;
- ce qui est optionnel ;
- ce qui dépend d'un abonnement ;
- ce qui nécessite un service tiers ;
- ce qui ne fonctionne pas.

Le but est de comprendre comment les données circulent dans l'écosystème. La page finale n'a pas besoin de reproduire toutes ces étapes si certaines n'aident pas la décision.

---

# 8. Brand Evidence Ledger

Créer un registre avec : Entity, Claim, Source, Date, Status, Freshness.

Statuts : `VERIFIED`, `SUPPORTED`, `INFERRED`, `UNKNOWN`, `OUTDATED`, `CONTRADICTED`.

Vérifier en priorité : gamme actuelle, services, abonnement, export, cloud, formats, applications, accessoires, compatibilités, prix et disponibilité.

---

# 9. Couverture BRAND_HUB

Ne pas utiliser une architecture fixe comme template obligatoire.

Le contenu doit couvrir uniquement les éléments nécessaires parmi :

- ce qui différencie concrètement la marque ;
- gamme actuelle et générations importantes ;
- conséquences de l'écosystème sur les usages ;
- logiciels, services ou abonnements qui changent la décision ;
- forces et limites démontrables ;
- profils ou situations pour lesquels la marque est adaptée ou moins adaptée ;
- alternatives pertinentes ;
- prochaines pages utiles ;
- sources et niveau de preuve.

L'ordre, le nombre de sections et le format dépendent de l'intention. Un tableau n'est utilisé que s'il facilite une comparaison réelle.

---

# 10. Couverture PRODUCT

Ne pas reproduire automatiquement la même structure d'un produit à l'autre.

Traiter en priorité :

- statut et génération lorsque cela compte ;
- caractéristiques qui changent réellement l'achat ;
- workflow et compatibilités ;
- contraintes ou limites ;
- coût total ou accessoires lorsque pertinents ;
- à qui le produit convient ou non ;
- alternative logique lorsque nécessaire ;
- sources.

Ne pas transformer la page en fiche constructeur recopiée ni en mini-review si une page `REVIEW` existe déjà.

---

# 11. Couverture REVIEW

Si test réel documenté : méthodologie, conditions, durée, limites, résultats, observations et verdict peuvent être utilisés proportionnellement aux preuves disponibles.

Sinon :
- mention explicite mais sobre du niveau de preuve ;
- aucune formulation du type « nous avons testé » ;
- aucun score simulant une mesure ;
- aucune sensation d'écriture présentée comme vécue ;
- distinguer faits, déductions et retours utilisateurs agrégés lorsqu'ils sont réellement sourcés ;
- produire un jugement éditorial utile, pas une simple répétition de la page `PRODUCT`.

---

# 12. Couverture SERVICE

Traiter selon pertinence : définition, fonctions, gratuit/payant, fonctionnement sans service, coût actuel, impact sur les données, limites, alternatives et décision.

Toujours distinguer fonction cœur, confort, dépendance et lock-in éventuel lorsque ces notions changent réellement l'usage.

---

# 13. Couverture ACCESSORY_HUB

Classer les accessoires lorsque pertinent : `REQUIRED`, `RECOMMENDED`, `OPTIONAL`, `COSMETIC`.

Expliquer compatibilité, génération, valeur réelle, coût et alternatives. Ne pas créer une liste commerciale sans hiérarchie ni imposer toutes les catégories sur chaque marque.

---

# 14. Couverture ALTERNATIVES

Partir des raisons concrètes de quitter la marque : prix, ouverture, lecture, apps, couleur, format, workflow, abonnement, compatibilité.

Router ensuite les alternatives par besoin. Pour une vraie comparaison multi-produits, déléguer le scoring à `comparison-content-workflow`.

Ne pas refaire un classement générique déjà traité dans `/comparatifs/`.

---

# 15. Choose / avoid

Utiliser des recommandations « pour qui / moins adapté » uniquement lorsqu'elles apportent une vraie décision.

Aucun nombre minimum de cas n'est imposé. Deux situations précises valent mieux que cinq formulations génériques.

Les limites ne doivent pas être édulcorées pour préserver la conversion.

---

# 16. Internal Linking

Le maillage est contextuel, pas quantitatif.

Ajouter un lien uniquement lorsqu'il constitue une prochaine étape logique : modèle associé, ancienne génération utile, review, comparatif, alternative, accessoire, service, guide, usage, bon plan ou page prix.

Ne jamais imposer un minimum de liens internes ou de cibles uniques. Une phrase ne doit pas exister uniquement pour accueillir un lien.

Les notions de « hub profond » et de « maillage » restent internes au workflow et ne doivent jamais apparaître dans la prose utilisateur.

---

# 17. Affiliate Value

Utiliser `affiliate-value` et vérifier : utilité sans CTA, limites visibles, alternatives honnêtes, absence de fausse urgence, prix et disponibilité datés, disclosure claire, recommandation indépendante de la commission.

La page doit rester utile si tous les liens affiliés sont supprimés.

---

# 18. Fact-check

Utiliser `fact-check` pour vérifier noms, générations, dimensions, technologies, compatibilités, OS, services, cloud, formats, accessoires, prix, abonnements, disponibilité et fin de commercialisation.

---

# 19. GEO Entity Pass

Contrôler explicitement les relations utiles : marque → produit, marque → logiciel, marque → service, marque → intégration, produit → technologie, produit → usage, produit → limitation, produit → alternative, marque → concurrent.

La page doit être facile à comprendre et à citer parce que les relations sont explicites, pas parce qu'elle répète artificiellement les noms d'entités ou ajoute des FAQ génériques.

---

# 20. Finition éditoriale

Exécuter : `natural-writing`, `humanizer`, `general-writing`, `anti-ai-slop`.

Utiliser `seo-drift` lorsque l'objectif est de comparer une version à un baseline antérieur ou de vérifier une régression après modification. Ne pas l'utiliser comme substitut à la QA éditoriale.

La finition doit supprimer le métadiscours, les transitions de remplissage, les symétries artificielles, les structures répétées et les phrases applicables à n'importe quelle marque.

---

# 21. SEO

Utiliser `seo-best-practices` et `seo-technical` et vérifier title, H1, intent, entities, canonical, robots, maillage, breadcrumbs, structured data si pertinent, indexation des anciennes générations et cannibalisation.

Aucun nombre minimum de mots, H2/H3, tableaux ou liens ne peut servir de proxy de qualité SEO.

---

# 22. Validation automatique + publish gate

Exécuter d'abord :

```bash
python3 validate_brands.py
```

Le contrôle automatique vérifie uniquement des blockers détectables : structure HTML de base, sécurité `noindex` en brouillon, métadiscours évident, faux langage de test, quelques signaux génériques à haut risque, présence d'une source, disclosure documentaire d'une review et couverture sémantique minimale par type de page.

Le script ne doit jamais déclarer automatiquement :

- Fact-check complet PASS ;
- E-E-A-T / Trust PASS ;
- GEO PASS ;
- Humanizer PASS ;
- positionnement juste ;
- valeur originale suffisante ;
- cannibalisation résolue ;
- page publiable.

Après le script, exécuter obligatoirement :

`.agents/skills/brand-editorial-publish-gate/SKILL.md`

Le publish gate évalue intention, valeur originale, preuves, Trust/E-E-A-T observable, GEO, pertinence éditoriale, ton français, anti-AI-slop, SEO et adéquation au type de page.

Un PASS machine n'autorise jamais l'indexation.

---

# 23. Échecs automatiques

FAIL si : génération ancienne présentée comme actuelle, produit discontinué non signalé, marque décrite uniquement en termes promotionnels, faux test, sensation produit inventée, service payant présenté comme gratuit, abonnement omis s'il change l'usage, affirmation importante non vérifiée présentée comme certaine, absence de valeur originale au-delà des sources marchandes, métadiscours éditorial dans la prose utilisateur, signaux anti-AI-slop `HIGH` non corrigés, intention principale non satisfaite, cannibalisation forte non résolue ou page rendue indexable avant validation humaine.

---

# 24. Statuts

- `ENTITY_MAP_READY`
- `RANGE_READY`
- `ECOSYSTEM_READY`
- `DRAFT_READY`
- `QA_IN_PROGRESS`
- `MACHINE_VALIDATED`
- `REVISION_REQUIRED`
- `PUBLISH_GATE_PASS`
- `HUMAN_APPROVED`
- `PUBLISHABLE`

`MACHINE_VALIDATED` n'implique jamais `PUBLISH_GATE_PASS`.

---

# 25. Publication

Par défaut : conserver `noindex,follow`, ne pas publier et ne pas déployer une page comme indexable.

Conditions cumulatives avant retrait du `noindex` :

1. `validate_brands.py` ne retourne aucun blocker ;
2. `brand-editorial-publish-gate` retourne `PASS` et `READY FOR HUMAN VALIDATION` ;
3. validation humaine explicite.

---

# 26. Fichiers persistants

Pour chaque marque, conserver entity map, product range, ecosystem, evidence ledger, positioning, internal link map et date de recherche dans `.content/brands/`.

Pour chaque page, conserver les éléments d'audit dans `.content/reviews/` lorsque le workflow les génère.

La prose finale ne doit jamais être la seule source expliquant l'écosystème de la marque.
