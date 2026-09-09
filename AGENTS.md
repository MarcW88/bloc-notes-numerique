# Instructions du dépôt

Ce dépôt contient le site éditorial et d’affiliation bloc-notes-numeriques.fr.

## Design

Pour toute création, modification ou revue de l’interface :

1. Lire `DESIGN.md` avant de modifier le frontend.
2. Utiliser le skill `.agents/skills/site-design-review/SKILL.md` pour toute demande d’audit, de critique, de polish ou de validation visuelle.
3. Préserver une esthétique de média éditorial spécialisé. Ne pas transformer le site en landing page SaaS, en catalogue e-commerce ou en comparateur affilié agressif.
4. Réutiliser les composants et tokens existants avant d’en créer de nouveaux.
5. Vérifier au minimum les rendus mobile et desktop lorsque l’environnement permet de lancer le site.
6. Lors d’un audit, ne pas corriger automatiquement les problèmes sauf si la demande inclut explicitement l’implémentation.

## Qualité et confiance

- Distinguer clairement le contenu éditorial des liens affiliés.
- Ne pas inventer de tests, mesures, prix, avis utilisateurs ou expériences produit.
- Afficher les limites et le niveau de preuve aussi clairement que les avantages.
- Conserver une hiérarchie HTML sémantique et une navigation accessible.
- Respecter les commandes de build, lint et test définies par le projet lorsqu’elles seront disponibles.

## Production éditoriale — Guides

Pour toute création ou réécriture d’un guide sous `/guides/` :

1. Utiliser `.agents/skills/guide-content-workflow/SKILL.md`.
2. Séparer la pré-analyse, la rédaction et la validation ; conserver le brief dans `.content/briefs/`.
3. Vérifier les informations susceptibles d’évoluer auprès de sources officielles avant publication.
4. Ne jamais présenter une synthèse documentaire comme un test produit.
5. Ne retirer `noindex` qu’après validation humaine du contenu final.
6. Après rédaction, exécuter dans l’ordre la chaîne de contrôle définie dans le skill : intention, valeur affiliée, fact-check, natural-writing, maillage interne, Humanizer, general-writing, anti-AI-slop, contrôle de dérive, SEO technique, SEO éditorial et editorial QA.
7. Une page ne peut être fusionnée ou indexée que si le rapport de contrôle se termine par `PASS`.

## Production éditoriale — Pages Par usage

Pour toute création ou réécriture sous `/usages/` :

1. Utiliser `.agents/skills/usage-content-workflow/SKILL.md`.
2. Utiliser `.agents/skills/jobs-to-be-done/SKILL.md` pendant la pré-analyse afin de partir des circonstances, du progrès recherché et du workflow réel plutôt que d’un persona générique ou d’une liste de fonctionnalités.
3. Créer ou mettre à jour `.content/usages/<slug>.json` avant la rédaction ; ce fichier est la source de vérité du cadrage usage.
4. Respecter la frontière éditoriale : `/usages/` explique le besoin et les critères ; `/comparatifs/` classe les produits ; `/guides/` explique une technologie, un critère ou une procédure ; `/marques/` documente un écosystème ou un produit.
5. Ne pas faire de scoring ou de ranking produit dans une page usage. Si un classement devient nécessaire, passer la main à `comparison-content-workflow`.
6. Distinguer `OBSERVED`, `SUPPORTED`, `INFERRED`, `HYPOTHESIS` et `UNKNOWN`. Ne jamais présenter une motivation supposée comme un comportement utilisateur observé.
7. Considérer les alternatives hors E Ink et les situations où le bloc-notes numérique n’est pas le bon outil.
8. Conserver `noindex,follow` jusqu’à validation humaine explicite.
9. Après rédaction, exécuter la chaîne de QA définie dans `usage-content-workflow`, y compris le contrôle anti-cannibalisation avec les comparatifs et guides proches.

## Production éditoriale — Comparatifs et marques

- Pour les comparatifs, utiliser `.agents/skills/comparison-content-workflow/SKILL.md` et conserver la logique critères → preuves → scoring → classement.
- Pour les pages marques, produits et écosystèmes, utiliser `.agents/skills/brand-content-workflow/SKILL.md`.
- Ne jamais faire varier une recommandation, un score ou un classement en fonction d’une commission d’affiliation.

## Production éditoriale — Comparatifs : publish gate obligatoire

Pour toute création, récupération, réécriture ou validation sous `/comparatifs/` :

1. Déterminer explicitement le type `BEST_OVERALL`, `BEST_FOR_USE_CASE`, `BUDGET`, `FEATURE_SPECIFIC` ou `HEAD_TO_HEAD` avant de rédiger.
2. Créer ou mettre à jour `.content/comparisons/<slug>.json` avant la rédaction ; ce fichier est la source de vérité du contrat de décision, de l’univers produit, des exclusions, critères, poids, preuves, scores et classement.
3. Construire l’univers produit avant de choisir le gagnant. Toute exclusion importante doit être justifiée ; l’existence ou l’absence d’affiliation ne peut décider de l’inclusion.
4. Ne jamais imposer un nombre minimum de mots, H2/H3, tableaux ou liens internes comme proxy de qualité. La structure doit découler des arbitrages du lecteur.
5. Distinguer la preuve d’un fait de la justification d’une note : une source officielle peut vérifier une fonction, mais ne vérifie pas automatiquement un `9/10`. Les justifications génériques de scores ne suffisent pas pour défendre un ranking.
6. Définir les critères et poids avant le classement, appliquer les hard gates avant la moyenne, comparer le coût total lorsque pertinent et tester la sensibilité du gagnant lorsque les scores sont proches ou les poids discutables.
7. Le verdict éditorial doit rester cohérent avec le scoring : expliquer pourquoi le #1 gagne, ce qu’il ne gagne pas, dans quels cas une alternative devient meilleure et éviter le langage absolu lorsque l’écart est fragile.
8. Après rédaction ou correction, exécuter : intention/JTBD → univers et équivalence → registre de preuves → critères/pondérations → scoring/hard gates/coût total → fact-check → valeur affiliée → maillage → natural-writing/Humanizer → anti-AI-slop → dérive SEO → SEO éditorial/technique → GEO → editorial QA → `python3 validate_comparisons.py` → `.agents/skills/comparison-editorial-publish-gate/SKILL.md`.
9. `validate_comparisons.py` contrôle uniquement les blockers détectables automatiquement et l’intégrité mathématique. Un PASS du script ne signifie jamais que le classement est éditorialement défendable.
10. Le rapport `comparison-editorial-publish-gate` doit se terminer par `PASS` et `READY FOR HUMAN VALIDATION`. Un seul blocker suffit à maintenir la page en `noindex,follow`.
11. Ne retirer `noindex` qu’après validation humaine explicite du contenu final.

## Production éditoriale — Pages marques : publish gate obligatoire

Pour toute création, récupération, réécriture ou validation sous `/marques/` :

1. Déterminer explicitement le type `DIRECTORY`, `BRAND_HUB`, `PRODUCT`, `REVIEW`, `SERVICE`, `ACCESSORY_HUB` ou `ALTERNATIVES` avant de rédiger.
2. Ne jamais imposer un nombre minimum de mots, de H2/H3, de tableaux ou de liens internes comme proxy de qualité. La structure doit découler du besoin du lecteur.
3. Éviter tout métadiscours destiné à l’éditeur du site dans le texte utilisateur : ne pas expliquer qu’une page « sert de hub », qu’une section sert le SEO/GEO, qu’un passage crée du maillage ou qu’une page doit accomplir un rôle éditorial.
4. Toute recommandation doit distinguer faits vérifiés, interprétation éditoriale et expérience réelle. Sans preuve de test physique, une review reste une analyse documentaire ou éditoriale et ne doit jamais imiter un test hands-on.
5. Après rédaction ou correction, exécuter : intention et rôle de page → valeur originale/affiliée → fact-check et niveau de preuve → Trust/E-E-A-T observable → qualité GEO et relations d’entités → pertinence éditoriale → français naturel/tone of voice → anti-AI-slop + Humanizer → SEO éditorial/technique → `python3 validate_brands.py` → `.agents/skills/brand-editorial-publish-gate/SKILL.md`.
6. `validate_brands.py` contrôle uniquement les blockers détectables automatiquement. Un PASS du script ne signifie jamais que la page est publiable.
7. Le rapport `brand-editorial-publish-gate` doit se terminer par `PASS` et `READY FOR HUMAN VALIDATION`. Un seul blocker suffit à maintenir la page en `noindex,follow`.
8. Ne retirer `noindex` qu’après validation humaine explicite du contenu final.

## Production éditoriale — Bons plans

Pour toute création, réécriture ou actualisation sous `/bons-plans/` :

1. Utiliser `.agents/skills/deal-content-workflow/SKILL.md`.
2. Créer ou mettre à jour `.content/deals/<slug>.json` avant de modifier le texte : prix, disponibilité, statut et date de contrôle doivent être documentés.
3. Distinguer strictement `ACTIVE_VERIFIED`, `ACTIVE_STOCK_SENSITIVE`, `PRICE_WATCH`, `EXPIRED`, `SOLD_OUT`, `UNVERIFIED` et `NOT_STARTED`.
4. Un prix barré marchand ne suffit jamais à prouver une remise. Documenter le prix de référence et sa base avant d'afficher une économie ou un pourcentage.
5. Une offre qui dépasse son TTL ne peut plus être présentée comme active sans nouvelle vérification.
6. Les pages de bons plans n'effectuent pas de ranking produit selon la commission. Le choix produit reste dans `/comparatifs/` ; la page deal juge l'offre, pas la valeur absolue du produit.
7. Les liens affiliés doivent rester transparents et utiliser `rel="sponsored"` lorsque nécessaire.
8. Utiliser `content-refresh`, `fact-check`, `affiliate-value`, `internal-linking-audit`, `natural-writing`, `humanizer`, `anti-ai-slop` et `editorial-qa` conformément au workflow.
9. Conserver `noindex,follow` jusqu'à validation humaine explicite.

## Production éditoriale — Pages de confiance du site

Pour toute création ou réécriture de `/methode-de-test/`, `/comment-nous-comparons/`, `/a-propos/`, `/contact/`, `/transparence-affiliation/` ou `/mentions-legales/` :

1. Utiliser `.agents/skills/trust-content-workflow/SKILL.md`.
2. Mettre à jour `.content/trust/<slug>.json` avant la rédaction ; ce registre est la source de vérité des claims institutionnels.
3. Ne jamais affirmer un test physique sans `DIRECT_OBSERVATION`, ni utiliser « notre équipe », « nos experts » ou équivalent sans preuve `OWNER_CONFIRMED`.
4. Définir concrètement l'indépendance éditoriale au lieu d'utiliser un slogan absolu ; les commissions ne doivent jamais modifier un score ou un classement.
5. Pour l'affiliation, expliquer qu'une transaction éligible peut générer une commission sans promettre un « même prix » ou une absence de coût non vérifiable.
6. Les informations inconnues doivent rester `UNKNOWN` ou `NEEDS_OWNER_INPUT`, jamais être complétées par supposition.
7. `/mentions-legales/` reste `LEGAL_PENDING` tant que les informations de l'éditeur, de l'hébergeur, des traitements de données et autres données légales n'ont pas été confirmées.
8. Exécuter `fact-check`, `affiliate-value` lorsque pertinent, `natural-writing`, `humanizer`, `general-writing`, `anti-ai-slop`, `internal-linking-audit`, `editorial-qa`, puis `validate_trust_workflow.py`.
9. Conserver `noindex,follow` jusqu'à validation humaine explicite ; une validation éditoriale n'entraîne jamais automatiquement l'indexation.
