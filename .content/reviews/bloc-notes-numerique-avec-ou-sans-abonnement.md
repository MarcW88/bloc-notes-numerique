# Rapport de contrôle — standard guide Prix

```yaml
url: /guides/bloc-notes-numerique-avec-ou-sans-abonnement/
reviewed_at: 2026-09-08
structural_quality_gate: PASS
content_status: DRAFT_READY
indexing_status: noindex
quality_reference: /guides/prix-bloc-notes-numerique/
page_role_in_standard: must meet price-guide quality floor
```

## 1. Profondeur sémantique mesurable

- Contenu utile hors navigation et hors section Sources : **1128 mots**.
- H2 substantiels : **7**.
- Tableaux : **2**.
- Les sections trop courtes, mono-paragraphe non développé ou tableaux sans contexte sont bloquants dans `validate_guide_quality.py`.

### Détail par section

- `« Sans abonnement » recouvre plusieurs situations différentes` — 135 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `Testez six fonctions essentielles hors formule payante` — 163 mots ; 2 paragraphe(s) ; 1 tableau(x) ; 0 liste(s).
- `reMarkable Connect : un cas où il faut regarder fonction par fonction` — 171 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `Kindle, Kobo, BOOX et Supernote ont d’autres modèles de dépendance` — 192 mots ; 2 paragraphe(s) ; 1 tableau(x) ; 0 liste(s).
- `Préparez un plan de sortie des données avant l’achat` — 138 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `Transformez le prix mensuel en coût d’usage réel` — 119 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `La règle de décision` — 88 mots ; 2 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).

## 2. Maillage interne

- Liens internes contextuels : **6**.
- Cibles uniques : **6**.

- `/comparatifs/bloc-notes-numerique-sans-abonnement/`
- `/guides/choisir-bloc-notes-numerique/`
- `/guides/exporter-notes/`
- `/guides/formats-fichiers-compatibles/`
- `/guides/prix-bloc-notes-numerique/`
- `/marques/remarkable/abonnement-connect/`

Le gate exige au minimum 4 liens contextuels et 3 cibles distinctes, sauf modification explicite du standard.

## 3. Sources et factualité

- Sources externes officielles identifiables : **6**.
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
