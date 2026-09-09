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
