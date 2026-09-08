# Rapport de contrôle — standard guide Prix

```yaml
url: /guides/encre-electronique-fonctionnement/
reviewed_at: 2026-09-08
structural_quality_gate: PASS
content_status: DRAFT_READY
indexing_status: noindex
quality_reference: /guides/prix-bloc-notes-numerique/
page_role_in_standard: must meet price-guide quality floor
```

## 1. Profondeur sémantique mesurable

- Contenu utile hors navigation et hors section Sources : **948 mots**.
- H2 substantiels : **7**.
- Tableaux : **0**.
- Les sections trop courtes, mono-paragraphe non développé ou tableaux sans contexte sont bloquants dans `validate_guide_quality.py`.

### Détail par section

- `Des particules chargées forment les pixels visibles` — 122 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `Pourquoi une page statique consomme si peu` — 132 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `Pourquoi le rafraîchissement est plus lent et produit du ghosting` — 122 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `Comment la couleur est-elle ajoutée à l’E Ink ?` — 124 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `Écran réfléchissant et front light ne sont pas contradictoires` — 128 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `Pourquoi l’écriture peut sembler rapide malgré l’E Ink` — 115 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `Ce que ce fonctionnement change lors d’un achat` — 76 mots ; 2 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).

## 2. Maillage interne

- Liens internes contextuels : **7**.
- Cibles uniques : **6**.

- `/comparatifs/tablette-e-ink/`
- `/guides/autonomie-tablette-e-ink/`
- `/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/`
- `/guides/choisir-bloc-notes-numerique/`
- `/guides/latence-ecriture/`
- `/guides/tablette-e-ink/`

Le gate exige au minimum 4 liens contextuels et 3 cibles distinctes, sauf modification explicite du standard.

## 3. Sources et factualité

- Sources externes officielles identifiables : **3**.
- Les fonctions variables sont rédigées avec leurs marques, générations ou conditions lorsque celles-ci sont nécessaires à la précision.
- Aucune expérience directe, mesure propriétaire ou résultat de test n'est déduit automatiquement par ce script.
- Le fact-check éditorial reste une passe distincte : la présence d'une source n'est pas, à elle seule, une preuve que toute affirmation est correcte.

## 4. Content refresh / conservation

- Pour les anciens guides, les angles utiles ont été conservés lorsque cohérents avec le nouveau standard ; l'enrichissement porte sur contexte, exemples, limites, entités et prochaine étape.
- Pour les pages initialement vides, le contenu est construit depuis le brief et non depuis un simple gabarit H2.
- La page Prix reste la référence de densité et de valeur décisionnelle, sans imposer une longueur artificiellement identique à chaque tutoriel.

## 5. Natural writing / Humanizer / General writing

Ces passes ont été appliquées pendant la réécriture éditoriale mais **ne sont pas déclarées PASS par déduction automatique**. Le script contrôle uniquement des signaux structurels observables. La validation humaine finale doit encore vérifier le rythme, les répétitions, les transitions et le ton dans le rendu.

## 6. Anti-AI-slop

Le gate structurel bloque le principal défaut du précédent lot : H2 très courts, tableaux sans explication et maillage quasi absent. Il ne prétend pas détecter l'origine d'un texte. Toute formulation générique ou mécanique relevée lors de la lecture finale doit être corrigée avant publication.

## 7. SEO / GEO

- Une réponse initiale autonome est exigée par le quality gate.
- Les H2 doivent couvrir des sous-questions distinctes et suffisamment développées.
- Les tableaux doivent être introduits et interprétés.
- Les entités et sources sont explicites dans le corps lorsqu'elles soutiennent une décision ou un mécanisme.
- Le maillage dirige vers des guides, usages, comparatifs ou pages marques selon l'étape suivante du lecteur.

## 8. Technique

- `noindex,follow` : **PASS**.
- HTML généré depuis `_generate.py` et les modules de contenu, pas modifié uniquement à la main dans les pages générées.
- Les liens internes sont validés séparément dans le workflow CI.

## 9. Blockers observés

- Aucun blocker du quality gate.

## Verdict

**PASS structurel — DRAFT_READY.** Ce verdict signifie que la page atteint le plancher de profondeur défini à partir du guide Prix. Il ne remplace pas la validation humaine finale et n'autorise ni retrait du `noindex`, ni publication, ni déploiement.
