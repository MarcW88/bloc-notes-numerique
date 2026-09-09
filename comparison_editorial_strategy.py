"""Page-specific editorial strategy for comparison pages.

The comparison methodology is shared. The editorial architecture is not.
Each entry explains what the page has to teach and why its structure should
follow that decision story rather than a cluster-wide template.
"""

COMPARISON_EDITORIAL_STRATEGIES = {
    "bloc-notes-numerique-professionnel": {
        "editorial_thesis": (
            "Le vrai choix professionnel n'oppose pas un meilleur appareil à des moins bons : "
            "il oppose surtout l'ouverture applicative de BOOX à l'organisation manuscrite de Supernote, "
            "avec la politique IT de l'entreprise comme filtre préalable."
        ),
        "decision_tensions": [
            "ouverture applicative et Google Play vs environnement spécialisé",
            "interopérabilité et multi-cloud vs organisation manuscrite structurée",
            "polyvalence vs simplicité",
            "score moyen vs hard gates IT propres à l'entreprise",
            "écart numérique de 0,05 point vs faible robustesse réelle du gagnant",
        ],
        "architecture_rationale": (
            "La page doit commencer par le filtre IT, puis développer le duel BOOX/Supernote qui explique "
            "l'essentiel de la décision. Les autres modèles sont traités comme des branches du choix plutôt "
            "que comme cinq fiches de longueur identique. La sensibilité du scoring est expliquée après le "
            "dilemme éditorial, car elle sert à démontrer pourquoi le verdict est conditionnel. Le coût, les "
            "exclusions et la méthode viennent ensuite comme contrôles de décision, pas comme sections imposées."
        ),
        "must_tell": [
            "un hard gate IT peut rendre le classement sans objet pour une entreprise donnée",
            "BOOX et Supernote sont presque ex aequo mais ne représentent pas la même philosophie de travail",
            "une variation raisonnable des poids inverse le gagnant",
            "Note Air5 C, Paper Pro et Paper Pure répondent à des branches de besoin différentes",
            "les prix officiels observés ne sont pas assez homogènes pour devenir une fausse note de coût précise",
            "les tests physiques ne sont pas revendiqués",
        ],
        "can_omit": [
            "une fiche symétrique complète pour chacun des cinq produits",
            "un long chapitre de méthodologie avant d'expliquer le dilemme",
            "un podium présenté comme vérité universelle",
            "une répétition textuelle de toutes les lignes du tableau de scores",
        ],
        "preferred_story_order": [
            "verdict conditionnel",
            "hard gates IT",
            "duel ouverture BOOX vs organisation Supernote",
            "branches alternatives selon le besoin",
            "sensibilité et lecture correcte du score",
            "coût réel et produits exclus",
            "méthode, limites et sources",
        ],
    }
}
