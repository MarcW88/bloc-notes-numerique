# Rapport de contrôle — standard guide Prix

```yaml
url: /guides/synchroniser-notes-cloud/
reviewed_at: 2026-09-08
structural_quality_gate: PASS
content_status: DRAFT_READY
indexing_status: noindex
quality_reference: /guides/prix-bloc-notes-numerique/
page_role_in_standard: must meet price-guide quality floor
```

## 1. Profondeur sémantique mesurable

- Contenu utile hors navigation et hors section Sources : **953 mots**.
- H2 substantiels : **7**.
- Tableaux : **1**.
- Les sections trop courtes, mono-paragraphe non développé ou tableaux sans contexte sont bloquants dans `validate_guide_quality.py`.

### Détail par section

- `Ne confondez pas synchronisation et export vers le cloud` — 137 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `Les cinq questions à poser à n’importe quel cloud` — 134 mots ; 2 paragraphe(s) ; 1 tableau(x) ; 0 liste(s).
- `reMarkable : cloud maison et intégrations tierces ont des rôles différents` — 107 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `BOOX et Supernote offrent plus d’une méthode de transfert` — 132 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `La synchronisation crée aussi un risque de conflits` — 129 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `Cloud et sauvegarde ne sont pas synonymes` — 117 mots ; 3 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).
- `La checklist avant de choisir une intégration cloud` — 69 mots ; 2 paragraphe(s) ; 0 tableau(x) ; 0 liste(s).

## 2. Maillage interne

- Liens internes contextuels : **7**.
- Cibles uniques : **7**.

- `/guides/bloc-notes-numerique-avec-ou-sans-abonnement/`
- `/guides/bloc-notes-numerique-dropbox/`
- `/guides/bloc-notes-numerique-google-drive/`
- `/guides/bloc-notes-numerique-onedrive/`
- `/guides/ecosysteme-ouvert-ou-ferme/`
- `/guides/exporter-notes/`
- `/guides/transfert-notes-vers-ordinateur/`

Le gate exige au minimum 4 liens contextuels et 3 cibles distinctes, sauf modification explicite du standard.

## 3. Sources et factualité

- Sources externes officielles identifiables : **5**.
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
