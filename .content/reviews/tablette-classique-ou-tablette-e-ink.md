# Rapport de contrôle avant publication

```yaml
url: /guides/tablette-classique-ou-tablette-e-ink/
slug: tablette-classique-ou-tablette-e-ink
brief_status: HUMAN_APPROVED
draft_commit: 95ba0e7fc025a0b2b1c6cf356ce2e700955f1b23
reviewed_at: 2026-09-08
final_status: PASS
indexing_status: noindex
```

## 1. Content refresh adapté au neuf

- Éléments du brief conservés : E Ink pour contenu statique, tablette classique pour vitesse et multimédia.
- Lacunes corrigées : tâches éliminatoires, applications Android et compromis explicites.
- Éléments différés : modèles, prix et bénéfices médicaux.

## 2. Search intent

- Intention : choisir entre deux familles de tablettes selon les tâches.
- Fonction : qualifier l’adéquation de l’E Ink, sans sélectionner un produit.
- Réponse principale suffisamment précoce : PASS.
- Cannibalisation : les requêtes transactionnelles restent dans `/comparatifs/`.

## 3. Affiliate value

- Utile sans liens affiliés : PASS.
- Critères, limites et alternatives : écriture, lecture, couleur, vidéo, applications et export.
- Niveau de preuve : recommandation de technologie seulement, conditionnée par les usages.

## 4. Fact-check

| Affirmation | Statut | Source | Correction |
|---|---|---|---|
| BOOX Go 10.3 combine E Ink, Android et Google Play | Vérifiée | BOOX, page produit officielle | Aucune |
| reMarkable annonce une autonomie exprimée en semaines selon l’usage | Vérifiée | reMarkable Support | Attribution et réserve conservées |
| Les formats et DRM Kobo comportent des limites | Vérifiée | Kobo Help | Aucune |
| Mécanisme physique détaillé de l’encre électronique | Source insuffisante dans le brief | N/A | Détail supprimé ; effet d’usage décrit sans pseudo-précision |
| Bénéfice médical ou réduction de fatigue visuelle | Non revendiqué | N/A | Hors périmètre respecté |

Confiance globale : élevée pour les caractéristiques citées, prudente pour l’expérience applicative.

## 5. Natural writing

- Passages modifiés : introduction, explication des écrans et sources.
- Faits et intention préservés : PASS.

## 6. Internal linking

| Source | Cible | Ancre | Région | Statut |
|---|---|---|---|---|
| Guide | `/guides/choisir-bloc-notes-numerique/` | critères d’un bloc-notes numérique | Conclusion | PASS |
| Guide | `/guides/tablette-e-ink/` | technologie E Ink | Conclusion | PASS |

## 7. Humanizer

- Patterns constatés : contraste abstrait, pseudo-précision technique et titre avec ponctuation répétitive.
- Corrections : décision par tâches, mécanisme retiré faute de source adaptée, titre naturel.
- Dépendances appliquées : better-usage / academic-voice / writing-cadence / non-autoregressive-writing-pass.

## 8. General writing

- Cohérence globale : technologies, usages, choix E Ink, choix classique, compromis, test final.
- Titres, transitions et rythme : PASS.

## 9. Anti-AI-slop

| Fragment précis | Pattern | Gravité | Correction | Statut |
|---|---|---|---|---|
| « Le choix dépend moins de… » | contraste ornemental | Moyenne | consigne concrète sur les tâches indispensables | Corrigé |
| Explication des pigments sans source dédiée | pseudo-précision | Élevée | mécanisme supprimé | Corrigé |
| Titre avec tiret cadratin | signal de gabarit | Faible | deux-points | Corrigé |

## 10. SEO drift

- Brief vs premier brouillon : bénéfices, limites et exclusions respectés.
- Premier brouillon vs version finale : couverture des usages et entités conservée.
- Suppressions expliquées : PASS, le mécanisme non suffisamment sourcé a été retiré.

## 11. SEO technique

- Canonical : auto-référent et absolu.
- Robots : `noindex,follow`.
- HTML et titres : un H1, niveaux H1/H2, title de 57 caractères, description de 155 caractères.
- Liens : cibles internes existantes, ancres descriptives.
- Données structurées : fil d’Ariane du gabarit ; validation externe différée au déploiement.

## 12. SEO éditorial

- Title/H1/intention : comparaison et décision explicites.
- Structure et couverture : usages statiques et dynamiques, logiciel, limites et test.
- Sur-optimisation : aucune répétition forcée détectée.

## 13. GEO

- Réponse autonome : oui, avec les deux cas dès l’ouverture.
- Extractibilité : tableau par usage, liste des compromis et test en trois questions.
- Entités et sources : BOOX, reMarkable et Kobo reliés à leurs documentations officielles.

## 14. Editorial QA

- Intent : PASS
- Original affiliate value : PASS
- Factuality : PASS
- Natural language : PASS
- SEO preservation : PASS
- User usefulness : PASS

## 15. Lecture en ordre rendu

- Desktop : PASS, ordre du DOM relu via rendu texte Pandoc.
- Mobile : PASS, même ordre sémantique et règles responsives du gabarit contrôlées.
- Contradictions ou ruptures restantes : aucune détectée.

## Verdict

`PASS`

Risque résiduel : le comportement des applications Android sur E Ink varie selon le modèle et la version. La page reste en `noindex` jusqu’à décision humaine de publication.
