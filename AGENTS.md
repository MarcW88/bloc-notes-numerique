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

## Production éditoriale — Comparatifs

Pour toute URL sous `/comparatifs/`, il n’existe que deux workflows comparison à choisir :

1. **Analyser / auditer** : `.agents/skills/comparison-analysis-workflow/SKILL.md`.
2. **Créer / réécrire** : `.agents/skills/comparison-content-workflow/SKILL.md`.

Les skills transversaux appelés par ces workflows (`content-audit`, `search-intent`, `jobs-to-be-done`, `affiliate-value`, `fact-check`, `evidence-based-reviews`, `humanizer`, `general-writing`, `anti-ai-slop`, etc.) sont des briques internes. Ne pas créer un nouveau workflow comparatif lorsqu’un de ces skills couvre déjà l’étape.

### Règles obligatoires

1. Une page existante doit passer par `comparison-analysis-workflow` en mode `AUDIT` avant une réécriture substantielle.
2. Déterminer le type `BEST_OVERALL`, `USE_CASE`, `BUDGET`, `FEATURE_SPECIFIC` ou `HEAD_TO_HEAD`, mais utiliser ce type uniquement comme grille méthodologique. **Le type de comparatif ne doit jamais imposer un plan, un ordre de sections, un nombre de H2/H3, un tableau, une FAQ ou des fiches produits symétriques.**
3. Respecter la chaîne décisionnelle : intention → univers produit → équivalence → preuves → critères → hard gates → pondération/TSC si pertinents → scoring → ranking → plan → rédaction.
4. Les critères et poids sont définis avant le gagnant. Ils ne peuvent pas être modifiés pour produire un classement souhaité.
5. Toute exclusion de produit doit être documentée. Aucun produit n'est inclus ou favorisé parce qu'il possède un meilleur lien ou une meilleure commission d'affiliation.
6. Utiliser des sources fiables et actuelles. Les specs reposent d'abord sur le fabricant/documentation ; les jugements d'usage nécessitent des sources indépendantes ou des patterns suffisamment documentés.
7. Ne jamais remplir un trou de preuve avec la connaissance du modèle. Une information reste `UNKNOWN`, est qualifiée ou est supprimée.
8. Le scoring doit être auditable : chaque note importante possède une justification et un niveau de preuve. Une spec ne devient pas automatiquement une preuve d'expérience d'usage.
9. Utiliser les hard gates lorsque l'intention comporte une contrainte éliminatoire. Un produit qui échoue un besoin essentiel ne peut pas gagner par simple moyenne.
10. Comparer le coût de la configuration réellement utilisable lorsque le prix change la décision. Ne pas comparer un appareil nu à un bundle complet sans le signaler.
11. Le #1 doit expliquer ce qu'il gagne et ce qu'il ne gagne pas. Un `HEAD_TO_HEAD` peut avoir un verdict conditionnel plutôt qu'un gagnant absolu.
12. Comparer la structure et la méthode aux comparatifs voisins : réutiliser sans justification les mêmes critères, poids, ordre de produits ou architecture sur des intentions différentes est un signal de production industrialisée et peut imposer `DEEP_REWRITE`.
13. La page doit rester utile si tous les liens affiliés disparaissent. Les défauts significatifs du gagnant ne doivent pas être masqués.
14. Après rédaction, exécuter la chaîne définie dans `comparison-content-workflow`, puis `comparison-analysis-workflow` en mode `PUBLISH_REVIEW`.
15. `validate_comparisons.py` contrôle uniquement les blockers détectables automatiquement. Un PASS machine ne signifie jamais que le ranking ou la page sont publiables.
16. Le `PUBLISH_REVIEW` doit se terminer par `PASS — READY_FOR_HUMAN_VALIDATION`. Un seul blocker maintient la page en `noindex,follow`.
17. Ne retirer `noindex` qu’après validation humaine explicite **et** instruction explicite de rendre la page indexable.
18. Aucun quota de mots, H2/H3, tableaux ou liens internes ne peut servir de proxy de qualité.

## Production éditoriale — Pages marques

Pour toute URL sous `/marques/`, il n’existe que deux workflows brand à choisir :

1. **Analyser / auditer** : `.agents/skills/brand-analysis-workflow/SKILL.md`.
2. **Créer / réécrire** : `.agents/skills/brand-content-workflow/SKILL.md`.

Les skills transversaux appelés par ces workflows (`content-audit`, `search-intent`, `affiliate-value`, `fact-check`, `evidence-based-reviews`, `humanizer`, `general-writing`, `anti-ai-slop`, etc.) sont des briques internes. Ne pas créer un nouveau workflow brand lorsqu’un de ces skills couvre déjà l’étape.

### Règles obligatoires

1. Une page existante doit passer par `brand-analysis-workflow` en mode `AUDIT` avant une réécriture substantielle.
2. Déterminer le type `DIRECTORY`, `BRAND_HUB`, `PRODUCT`, `REVIEW`, `SERVICE`, `ACCESSORY_HUB` ou `ALTERNATIVES`, mais utiliser ce type uniquement comme grille de risque et de frontière éditoriale. **Le type de page ne doit jamais imposer un plan, un ordre de sections, un nombre de H2/H3, un tableau ou une FAQ.**
3. Le plan final doit être construit après l’analyse d’intention et le research/evidence brief. Chaque section doit être justifiable par une question du lecteur et des preuves disponibles.
4. Utiliser des sources fiables et actuelles. Pour les facts produits : fabricant/documentation en priorité ; sources indépendantes pour les jugements ; plusieurs sources utilisateurs seulement pour des patterns suffisamment documentés.
5. Ne jamais remplir un trou de preuve avec la connaissance du modèle. Une information reste `UNKNOWN`, est qualifiée ou est supprimée.
6. Toute recommandation doit distinguer faits vérifiés, interprétation éditoriale, synthèse d’autres sources et expérience réelle. Sans test physique documenté, aucune review ne peut imiter un test hands-on.
7. La page doit conserver une vraie valeur si tous les liens affiliés sont supprimés. Ne pas recopier ou simplement reformuler le fabricant ou un retailer.
8. Comparer la structure avec les pages sœurs : une architecture éditoriale répétée sans justification par l’intention ou les preuves est un signal de production industrialisée et peut imposer `DEEP_REWRITE`.
9. Éviter tout métadiscours destiné à l’éditeur dans le texte utilisateur : SEO, GEO, hub, maillage, intention de recherche, architecture de page ou stratégie éditoriale.
10. Après rédaction, exécuter la chaîne définie dans `brand-content-workflow`, puis `brand-analysis-workflow` en mode `PUBLISH_REVIEW`.
11. `validate_brands.py` contrôle uniquement les blockers détectables automatiquement. Un PASS machine ne signifie jamais que la page est publiable.
12. Le `PUBLISH_REVIEW` doit se terminer par `PASS — READY_FOR_HUMAN_VALIDATION`. Un seul blocker maintient la page en `noindex,follow`.
13. Ne retirer `noindex` qu’après validation humaine explicite **et** instruction explicite de rendre la page indexable.
14. Aucun quota de mots, H2/H3, tableaux ou liens internes ne peut servir de proxy de qualité.

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
