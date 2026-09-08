# Rapport de contrôle avant publication

```yaml
url: /guides/liseuse-ou-bloc-notes-numerique/
slug: liseuse-ou-bloc-notes-numerique
brief_status: HUMAN_APPROVED
draft_commit: 95ba0e7fc025a0b2b1c6cf356ce2e700955f1b23
reviewed_at: 2026-09-08
final_status: PASS
indexing_status: noindex
```

## 1. Content refresh adapté au neuf

- Éléments du brief conservés : lecture dominante, écriture régulière et cas hybride.
- Lacunes corrigées : format, circulation des fichiers et test de décision sur une semaine.
- Éléments différés : classement de modèles et prix.

## 2. Search intent

- Intention : distinguer liseuse, hybride et bloc-notes numérique.
- Fonction : page de choix de catégorie, pas guide d’achat de liseuses.
- Réponse principale suffisamment précoce : PASS.
- Cannibalisation : aucune recommandation « meilleur produit ».

## 3. Affiliate value

- Utile sans liens affiliés : PASS.
- Critères, limites et alternatives : lecture, notes longues, PDF, transport et export.
- Niveau de preuve : orientation par usage, sans verdict commercial.

## 4. Fact-check

| Affirmation | Statut | Source | Correction |
|---|---|---|---|
| Les modèles Kobo compatibles annotent certains EPUB et PDF non protégés | Vérifiée | Kobo Help | Limites de format conservées |
| Kobo propose des carnets sur les modèles compatibles | Vérifiée | Kobo Help | Aucune |
| Kindle Scribe propose lecture et carnets | Vérifiée | Amazon Help | Aucune |
| Un stylet garantit un export universel | Faux en général | Documentation variable selon produit | Le texte avertit explicitement de vérifier l’export |

Confiance globale : élevée dans le périmètre décrit.

## 5. Natural writing

- Passages modifiés : titre, description et explication de la différence essentielle.
- Faits et intention préservés : PASS.

## 6. Internal linking

| Source | Cible | Ancre | Région | Statut |
|---|---|---|---|---|
| Navigation globale | Hubs guides et marques | Ancres descriptives | En-tête/pied | PASS |

Le guide ne force pas de liens contextuels sans page fille directement nécessaire à la décision.

## 7. Humanizer

- Patterns constatés : opposition trop symétrique et ponctuation de titre typée gabarit.
- Corrections : relation directe entre matériel, logiciel et circulation des fichiers ; titre avec deux-points.
- Dépendances appliquées : better-usage / academic-voice / writing-cadence / non-autoregressive-writing-pass.

## 8. General writing

- Cohérence globale : différence, comparaison, hybrides, deux profils, méthode de décision.
- Titres, transitions et rythme : PASS.

## 9. Anti-AI-slop

| Fragment précis | Pattern | Gravité | Correction | Statut |
|---|---|---|---|---|
| « La différence ne vient donc pas seulement… » | contraste négatif générique | Moyenne | mécanismes nommés directement | Corrigé |
| Titre avec tiret cadratin | signal de gabarit | Faible | titre interrogatif naturel | Corrigé |

## 10. SEO drift

- Brief vs premier brouillon : segmentation liseuse, hybride et bloc-notes respectée.
- Premier brouillon vs version finale : exemples Kobo et Kindle conservés.
- Suppressions expliquées : PASS, aucune information décisionnelle supprimée.

## 11. SEO technique

- Canonical : auto-référent et absolu.
- Robots : `noindex,follow`.
- HTML et titres : un H1, hiérarchie H1/H2, title de 55 caractères, description de 152 caractères.
- Liens : liens externes officiels avec `rel="noopener noreferrer"`.
- Données structurées : fil d’Ariane du gabarit ; validation externe différée au déploiement.

## 12. SEO éditorial

- Title/H1/intention : alignés sur la comparaison recherchée.
- Structure et couverture : besoins, hybrides, cas de choix et méthode.
- Sur-optimisation : aucune répétition artificielle détectée.

## 13. GEO

- Réponse autonome : oui.
- Extractibilité : réponse courte, tableau et listes de critères.
- Entités et sources : Kobo et Amazon cités avec documentation officielle.

## 14. Editorial QA

- Intent : PASS
- Original affiliate value : PASS
- Factuality : PASS
- Natural language : PASS
- SEO preservation : PASS
- User usefulness : PASS

## 15. Lecture en ordre rendu

- Desktop : PASS, ordre du DOM relu via rendu texte Pandoc.
- Mobile : PASS, contenu identique et règles responsives du gabarit contrôlées.
- Contradictions ou ruptures restantes : aucune détectée.

## Verdict

`PASS`

Risque résiduel : les fonctions des appareils hybrides évoluent. La page reste en `noindex` jusqu’à décision humaine de publication.
