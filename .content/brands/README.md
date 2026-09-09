# Brand editorial validation

Les fichiers de `.content/brands/` documentent les données, preuves et cadrages utilisés par les pages `/marques/`.

Pour les pages marques, il existe deux workflows :

- `.agents/skills/brand-analysis-workflow/SKILL.md` pour l'audit, le contrôle de cluster et le gate final ;
- `.agents/skills/brand-content-workflow/SKILL.md` pour la création ou la réécriture.

La présence d'un fichier de données ou un PASS machine ne constitue pas une validation éditoriale.

Avant validation humaine, chaque URL terminée doit passer par `brand-analysis-workflow` en mode `PUBLISH_REVIEW` et obtenir :

`PASS — READY_FOR_HUMAN_VALIDATION`

Le validateur `validate_brands.py` contrôle uniquement les blockers détectables automatiquement. Il ne remplace ni l'analyse sémantique, ni le fact-check, ni la revue inter-pages.

Toutes les pages restent `noindex,follow` jusqu'à validation humaine explicite et instruction explicite de les rendre indexables.
