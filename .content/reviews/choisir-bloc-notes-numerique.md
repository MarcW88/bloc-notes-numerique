# Rapport de contrôle avant publication

```yaml
url: /guides/choisir-bloc-notes-numerique/
slug: choisir-bloc-notes-numerique
brief_status: HUMAN_APPROVED
draft_commit: 95ba0e7fc025a0b2b1c6cf356ce2e700955f1b23
reviewed_at: 2026-09-08
final_status: PASS
indexing_status: noindex
```

## 1. Content refresh adapté au neuf

- Éléments du brief conservés : choix par flux de travail, absence de classement produit, limites sur la sensation d’écriture et l’autonomie.
- Lacunes corrigées : coût total, scénario d’export complet et critères éliminatoires.
- Éléments différés : prix, verdicts et performances réelles, faute de test ou de données datées.

## 2. Search intent

- Intention : aider à choisir un type de bloc-notes numérique selon l’usage.
- Fonction : guide pilier, distinct du comparatif des meilleurs modèles.
- Réponse principale suffisamment précoce : PASS.
- Cannibalisation : les requêtes « meilleur » et « comparatif » restent réservées à `/comparatifs/`.

## 3. Affiliate value

- Utile sans liens affiliés : PASS.
- Critères, limites et alternatives : flux documentaire, export, écosystème, coût total et tablette classique.
- Niveau de preuve : aucune recommandation de modèle ni expérience de test revendiquée.

## 4. Fact-check

| Affirmation | Statut | Source | Correction |
|---|---|---|---|
| BOOX Go 10.3 repose sur Android et propose Google Play | Vérifiée | BOOX, page produit officielle | Aucune |
| reMarkable 2 est un appareil spécialisé autour des notes et documents | Vérifiée | reMarkable Support | Formulation limitée à l’organisation du produit |
| Kobo et Kindle Scribe proposent des fonctions d’annotation ou de carnets | Vérifiée | Aides officielles Kobo et Amazon | Aucune |
| Sensation d’écriture et autonomie réelles | Non vérifiables sans protocole | N/A | Aucun verdict, limites explicites |

Confiance globale : élevée pour les fonctions citées, prudente pour toute expérience d’usage.

## 5. Natural writing

- Passages modifiés : introduction, distinction ouvert/fermé et section des erreurs.
- Faits et intention préservés : PASS.

## 6. Internal linking

| Source | Cible | Ancre | Région | Statut |
|---|---|---|---|---|
| Guide | `/guides/taille-ecran-bloc-notes-numerique/` | taille d’écran | Conclusion | PASS |
| Guide | `/guides/formats-fichiers-compatibles/` | formats compatibles | Conclusion | PASS |
| Guide | `/guides/ecosysteme-ouvert-ou-ferme/` | écosystème ouvert ou fermé | Conclusion | PASS |

## 7. Humanizer

- Patterns constatés : contraste binaire, labels gras répétitifs et cadence trop régulière.
- Corrections : formulation directe, paragraphes continus et variation des transitions.
- Dépendances appliquées : better-usage / academic-voice / writing-cadence / non-autoregressive-writing-pass.

## 8. General writing

- Cohérence globale : progression besoin, critères, profils, erreurs, vérification finale.
- Titres, transitions et rythme : PASS après suppression des formulations mécaniques.

## 9. Anti-AI-slop

| Fragment précis | Pattern | Gravité | Correction | Statut |
|---|---|---|---|---|
| « moins ouvert ou fermé que… » | contraste ornemental | Moyenne | décision formulée par compatibilité | Corrigé |
| Trois paragraphes avec labels gras | gabarit répétitif | Moyenne | labels intégrés dans la prose | Corrigé |
| « Tous les critères essentiels » | promesse générique | Faible | description spécifique aux critères couverts | Corrigé |

## 10. SEO drift

- Brief vs premier brouillon : intention, exclusions et sources conservées.
- Premier brouillon vs version finale : aucune entité ni étape de décision supprimée.
- Suppressions expliquées : PASS, seules les tournures génériques ou mécaniques ont été remplacées.

## 11. SEO technique

- Canonical : auto-référent et absolu.
- Robots : `noindex,follow`, conformément au statut prépublication.
- HTML et titres : un H1, niveaux H1 puis H2, title de 58 caractères, description de 153 caractères.
- Liens : cibles internes existantes, ancres descriptives.
- Données structurées : fil d’Ariane présent dans le gabarit ; validation externe différée au déploiement.

## 12. SEO éditorial

- Title/H1/intention : alignés sur le choix selon l’usage.
- Structure et couverture : critères matériels, logiciels et économiques couverts sans classement.
- Sur-optimisation : aucune répétition forcée du mot-clé détectée.

## 13. GEO

- Réponse autonome : oui, dès le premier paragraphe.
- Extractibilité : listes, tableau comparatif et checklist.
- Entités et sources : reMarkable, BOOX, Kobo et Amazon reliés à leurs pages officielles.

## 14. Editorial QA

- Intent : PASS
- Original affiliate value : PASS
- Factuality : PASS
- Natural language : PASS
- SEO preservation : PASS
- User usefulness : PASS

## 15. Lecture en ordre rendu

- Desktop : PASS, ordre du DOM relu via rendu texte Pandoc.
- Mobile : PASS, même contenu et même ordre sémantique ; règles responsives vérifiées dans le gabarit.
- Contradictions ou ruptures restantes : aucune détectée.

## Verdict

`PASS`

Risque résiduel : les fonctions logicielles devront être revérifiées avant toute mise à jour future. La page reste en `noindex` jusqu’à décision humaine de publication.
