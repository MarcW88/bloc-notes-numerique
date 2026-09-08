"""Non-tabular replacements for visual specs that duplicated HTML comparison tables."""

NON_TABULAR_OVERRIDES = {
    "ecosysteme-ouvert-ou-ferme": {
        "type": "decision_tree",
        "title": "Ouvert ou fermé : partez de vos contraintes logicielles",
        "subtitle": "Le bon choix dépend surtout des applications et transferts indispensables.",
        "alt": "Arbre de décision pour choisir entre un écosystème spécialisé et un écosystème plus ouvert selon les applications et intégrations nécessaires.",
        "caption": "Le visuel complète le tableau : il montre le chemin de décision plutôt que de répéter les mêmes critères.",
        "nodes": [
            {"id":"start","x":390,"y":110,"w":420,"h":92,"style":"primary","lines":["Avez-vous besoin","d’applications tierces précises ?"]},
            {"id":"apps_yes","x":90,"y":300,"w":400,"h":105,"style":"muted","lines":["Oui","vérifiez leur disponibilité","et leurs droits d’accès"]},
            {"id":"apps_no","x":710,"y":300,"w":400,"h":105,"style":"muted","lines":["Non","un workflow spécialisé","peut suffire"]},
            {"id":"integrations","x":70,"y":530,"w":440,"h":125,"style":"accent","lines":["Priorité : ouverture","apps, cloud, partage","et intégrations tierces"]},
            {"id":"simplicity","x":690,"y":530,"w":440,"h":125,"style":"accent","lines":["Priorité : simplicité","workflow cohérent","et moins de réglages"]}
        ],
        "edges": [
            {"from":"start","to":"apps_yes","label":"Oui"},
            {"from":"start","to":"apps_no","label":"Non"},
            {"from":"apps_yes","to":"integrations"},
            {"from":"apps_no","to":"simplicity"}
        ]
    },
    "liseuse-ou-bloc-notes-numerique": {
        "type": "decision_tree",
        "title": "Liseuse, hybride ou bloc-notes : partez de l’activité dominante",
        "subtitle": "Le tableau détaille les fonctions ; ce schéma montre la bifurcation de choix.",
        "alt": "Arbre de décision entre liseuse, appareil hybride avec stylet et bloc-notes numérique selon la place de la lecture, de l’écriture et de l’export.",
        "caption": "Utilisez le tableau pour les détails et ce schéma uniquement pour le chemin de décision.",
        "nodes": [
            {"id":"start","x":390,"y":100,"w":420,"h":90,"style":"primary","lines":["Votre activité dominante","est-elle la lecture ?"]},
            {"id":"read_yes","x":80,"y":280,"w":400,"h":105,"style":"muted","lines":["Oui","les notes servent-elles","surtout à commenter ?"]},
            {"id":"read_no","x":720,"y":280,"w":400,"h":105,"style":"muted","lines":["Non","écriture, PDF et export","structurent le travail"]},
            {"id":"reader","x":40,"y":520,"w":300,"h":120,"style":"accent","lines":["Liseuse","lecture d’abord","annotations secondaires"]},
            {"id":"hybrid","x":450,"y":520,"w":300,"h":120,"style":"accent","lines":["Hybride","lecture + stylet","réellement équilibrés"]},
            {"id":"notebook","x":860,"y":520,"w":300,"h":120,"style":"accent","lines":["Bloc-notes","écriture, organisation","et export d’abord"]}
        ],
        "edges": [
            {"from":"start","to":"read_yes","label":"Oui"},
            {"from":"start","to":"read_no","label":"Non"},
            {"from":"read_yes","to":"reader","label":"Oui"},
            {"from":"read_yes","to":"hybrid","label":"Non"},
            {"from":"read_no","to":"notebook"}
        ]
    },
    "tablette-classique-ou-tablette-e-ink": {
        "type": "decision_tree",
        "title": "Tablette classique ou E Ink : identifiez votre contrainte éliminatoire",
        "subtitle": "Ne comparez pas une liste de fonctions : commencez par ce qui doit absolument fonctionner.",
        "alt": "Arbre de décision entre tablette classique et tablette E Ink selon les applications, la vidéo et le temps passé à lire ou écrire.",
        "caption": "Le schéma montre l’ordre de décision ; le tableau HTML conserve la comparaison détaillée.",
        "nodes": [
            {"id":"start","x":390,"y":100,"w":420,"h":90,"style":"primary","lines":["Avez-vous besoin","d’apps, vidéo ou animation ?"]},
            {"id":"classic","x":90,"y":310,"w":400,"h":115,"style":"accent","lines":["Oui","tablette classique","à examiner en priorité"]},
            {"id":"focus","x":710,"y":310,"w":400,"h":115,"style":"muted","lines":["Non","passez-vous surtout","du temps à lire et écrire ?"]},
            {"id":"eink","x":690,"y":540,"w":440,"h":125,"style":"accent","lines":["Oui","E Ink devient cohérent","si le workflow suit"]},
            {"id":"classic2","x":70,"y":540,"w":440,"h":125,"style":"muted","lines":["Non","la polyvalence d’une","tablette classique reste utile"]}
        ],
        "edges": [
            {"from":"start","to":"classic","label":"Oui"},
            {"from":"start","to":"focus","label":"Non"},
            {"from":"focus","to":"eink","label":"Oui"},
            {"from":"focus","to":"classic2","label":"Non"}
        ]
    }
}
