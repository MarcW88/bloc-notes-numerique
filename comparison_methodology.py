"""Durable page-level comparison methodology.

This module complements comparison_products.py (shared product baseline) and
comparison_pages.py (query/weights/ranking configuration). It stores the parts
of comparison-content-workflow that must survive metadata regeneration:
universe decisions, equivalence, evidence, hard gates, page-specific score
rationales, total-solution-cost notes, sensitivity and rank justification.
"""

CHECKED_AT = "2026-09-09"

PROFESSIONAL_METHOD = {
    "schema_version": 2,
    "slug": "bloc-notes-numerique-professionnel",
    "decision_contract": {
        "type": "best_for_use_case",
        "query": "meilleur bloc-notes numérique professionnel",
        "user_job": "gérer réunions, PDF, exports et outils de travail",
        "decision": "choisir un appareil E Ink de travail pour capturer des notes, annoter des documents et les réintégrer dans un environnement professionnel",
        "non_goals": [
            "remplacer un PC pour les tableurs, présentations complexes ou visioconférences",
            "désigner un meilleur appareil universel indépendamment des contraintes IT",
        ],
    },
    "criteria_definitions": {
        "organization": {
            "label": "Organisation des notes",
            "definition": "Capacité documentée à structurer, retrouver et naviguer dans des notes de travail.",
            "weight_rationale": "Critère central pour un volume de notes réparti entre réunions, projets et dossiers.",
        },
        "export": {
            "label": "Export et interopérabilité",
            "definition": "Capacité documentée à faire sortir notes et documents vers des formats ou services utilisables hors de l'appareil.",
            "weight_rationale": "Un appareil professionnel ne doit pas transformer les notes en silo.",
        },
        "pdf": {
            "label": "PDF et annotation",
            "definition": "Compatibilité et outils documentés pour lire, annoter et réexporter des documents.",
            "weight_rationale": "Les dossiers, rapports et ordres du jour constituent un cas d'usage professionnel fréquent.",
        },
        "apps": {
            "label": "Applications et intégrations",
            "definition": "Accès à des applications tierces ou à des intégrations de travail documentées.",
            "weight_rationale": "Important lorsque le workflow dépend d'outils externes, sans en faire un besoin universel.",
        },
        "writing": {
            "label": "Workflow d'écriture",
            "definition": "Outils natifs documentés pour écrire, sélectionner, structurer et retravailler des notes manuscrites. Ne mesure pas une sensation de stylet non testée.",
            "weight_rationale": "La capture manuscrite reste le coeur du job, mais aucune note hands-on n'est utilisée.",
        },
        "simplicity": {
            "label": "Simplicité opérationnelle",
            "definition": "Inférence éditoriale sur l'étendue et la complexité du logiciel nécessaire pour accomplir le job.",
            "weight_rationale": "La friction logicielle compte au quotidien mais reste secondaire face à l'interopérabilité.",
        },
        "no_sub": {
            "label": "Fonctions sans abonnement",
            "definition": "Part des fonctions centrales accessibles sans abonnement constructeur obligatoire.",
            "weight_rationale": "Le coût récurrent compte, mais il n'est pas le premier déterminant d'une page professionnelle généraliste.",
        },
    },
    "universe": [
        {"id":"boox_go_lumi","status":"ELIGIBLE","equivalence":"FUNCTIONALLY_COMPARABLE","reason":"10,3 pouces, stylet, PDF, organisation native, Android 15/Google Play et front light : couvre le job généraliste.","source":"https://shop.boox.com/products/go103gen2lumi"},
        {"id":"supernote_manta","status":"ELIGIBLE","equivalence":"FUNCTIONALLY_COMPARABLE","reason":"10,7 pouces, stylet, PDF et organisation manuscrite avancée ; proposition plus spécialisée que BOOX mais comparable sur le job.","source":"https://supernote.com/products/supernote-manta"},
        {"id":"boox_air5c","status":"ELIGIBLE","equivalence":"FUNCTIONALLY_COMPARABLE","reason":"10,3 pouces couleur, stylet, Android 15, Google Play, PDF et clavier optionnel ; plus lourd et plus polyvalent.","source":"https://shop.boox.com/products/noteair5c"},
        {"id":"remarkable_pro","status":"ELIGIBLE","equivalence":"FUNCTIONALLY_COMPARABLE","reason":"11,8 pouces couleur, stylet inclus, PDF, organisation et intégrations de travail ; écosystème spécialisé.","source":"https://remarkable.com/fr-FR/products/remarkable-paper/pro"},
        {"id":"remarkable_pure","status":"ELIGIBLE","equivalence":"FUNCTIONALLY_COMPARABLE","reason":"10,3 pouces monochrome, stylet inclus et même logique reMarkable de notes, export et intégrations.","source":"https://remarkable.com/fr-FR/shop/compare"},
        {"id":"boox_notemax","status":"EXCLUDED","equivalence":"PARTIALLY_COMPARABLE","reason":"Très pertinent pour PDF A4, mais son format 13,3 pouces, ses 615 g et l'absence de front light en font un cas spécialisé traité dans le comparatif A4.","source":"https://shop.boox.com/products/notemax","handoff":"/comparatifs/bloc-notes-numerique-a4/"},
        {"id":"kindle_scribe3","status":"EXCLUDED","equivalence":"PARTIALLY_COMPARABLE","reason":"Les modèles récents exportent vers OneNote/Drive/OneDrive, mais le produit reste davantage centré sur lecture et carnets que sur un environnement d'applications de travail généraliste.","source":"https://digprjsurvey.amazon.com/csad/help/node/TP8wuaQilIlwlITVTL"},
        {"id":"kobo_elipsa","status":"EXCLUDED","equivalence":"PARTIALLY_COMPARABLE","reason":"Carnets et exports sont documentés, mais certaines annotations de livres ne sont pas exportables et l'écosystème est d'abord celui d'une liseuse.","source":"https://help.kobo.com/hc/fr/articles/360062226733-Utiliser-votre-liseuse-Kobo-comme-un-carnet"},
        {"id":"supernote_nomad","status":"EXCLUDED","equivalence":"PARTIALLY_COMPARABLE","reason":"Très mobile mais 7,8 pouces ; moins adapté au job généraliste incluant revue régulière de PDF.","source":"https://supernote.com/products/supernote-nomad"},
        {"id":"remarkable_move","status":"EXCLUDED","equivalence":"PARTIALLY_COMPARABLE","reason":"Le format 7,3 pouces privilégie la mobilité ; il n'est pas retenu pour un comparatif professionnel généraliste avec PDF.","source":"https://remarkable.com/fr-FR/products/remarkable-paper/pro-move/details/features"},
    ],
    "hard_gates": [
        {"id":"current_and_documented","scope":"UNIVERSAL","rule":"Le modèle doit être actuel et documenté par une source officielle consultable.","failure_effect":"EXCLUDE"},
        {"id":"handwriting_pdf_core","scope":"UNIVERSAL","rule":"Le modèle doit permettre la prise de notes manuscrites et la lecture/annotation de PDF.","failure_effect":"EXCLUDE"},
        {"id":"standard_exit_path","scope":"UNIVERSAL","rule":"Le workflow doit disposer d'au moins une sortie documentée vers un format ou service utilisable hors de l'appareil.","failure_effect":"EXCLUDE"},
        {"id":"company_it_policy","scope":"USER_SPECIFIC","rule":"Le cloud, les comptes et applications nécessaires doivent être autorisés par la politique IT de l'organisation.","failure_effect":"USER_MUST_EXCLUDE","note":"Le comparatif ne peut pas vérifier la politique de chaque entreprise ; ce gate doit rester visible dans le verdict."},
        {"id":"required_business_app","scope":"USER_SPECIFIC","rule":"Si une application métier précise est indispensable, sa disponibilité et sa compatibilité doivent être confirmées avant achat.","failure_effect":"USER_MUST_EXCLUDE"},
    ],
    "evidence_ledger": [
        {"id":"boox_lumi_apps","product_id":"boox_go_lumi","criteria":["apps"],"claim":"Android 15, Google Play Store intégré et applications tierces prises en charge.","value":"Android 15 + Google Play","source":"https://shop.boox.com/products/go103gen2lumi","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"boox_lumi_org","product_id":"boox_go_lumi","criteria":["organization","writing"],"claim":"Outlines, tags, lasso et conversion manuscrite sont documentés pour l'organisation des notes.","value":"outlines + tags + lasso","source":"https://shop.boox.com/products/go103gen2lumi","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"boox_lumi_transfer","product_id":"boox_go_lumi","criteria":["export","pdf"],"claim":"Synchronisation vers Onyx Cloud, Google Drive, Dropbox et OneDrive, plus transfert BOOXDrop ; prise en charge de nombreux formats dont PDF.","value":"multi-cloud + BOOXDrop + PDF","source":"https://shop.boox.com/products/go103gen2lumi","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"boox_lumi_bundle","product_id":"boox_go_lumi","criteria":["no_sub"],"claim":"Le stylet est inclus et BOOX documente 10 Go de cloud Onyx gratuits ; aucune souscription BOOX obligatoire n'est annoncée pour les fonctions de base.","value":"stylus included + free Onyx cloud","source":"https://shop.boox.com/products/go103gen2lumi","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"supernote_org","product_id":"supernote_manta","criteria":["organization","writing"],"claim":"Supernote documente headings, keywords, stars et liens pour structurer et naviguer dans les carnets.","value":"headings + keywords + stars + links","source":"https://support.supernote.com/en_US/organizing/1759244-using-titles-keywords-and-stars","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"supernote_links","product_id":"supernote_manta","criteria":["organization","writing"],"claim":"Des liens peuvent pointer vers pages, fichiers récents, autres fichiers ou pages web.","value":"internal/file/web links","source":"https://support.supernote.com/inserting-links-to-notebooks?kb_language=en_US","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"supernote_transfer","product_id":"supernote_manta","criteria":["export","pdf"],"claim":"Transfert documenté via Supernote Cloud, Dropbox, Google Drive, email, USB, Browse & Access et Supernote Linking.","value":"multi-route transfer","source":"https://support.supernote.com/en_US/transfer-files","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"supernote_platform","product_id":"supernote_manta","criteria":["apps","simplicity"],"claim":"Manta utilise Chauvet, un système spécialisé basé sur Android 11 ; le produit est présenté comme orienté écriture.","value":"specialized Android-based OS","source":"https://supernote.com/products/supernote-manta","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"supernote_no_sub","product_id":"supernote_manta","criteria":["no_sub"],"claim":"Supernote annonce des mises à jour logicielles sans abonnement.","value":"no subscription","source":"https://supernote.com/pages/supernote-manta","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"air5c_apps","product_id":"boox_air5c","criteria":["apps","pdf"],"claim":"Android 15, Google Play, applications tierces, split screen et formats bureautiques/PDF sont documentés.","value":"Android 15 + Google Play + split screen","source":"https://shop.boox.com/products/noteair5c","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"air5c_transfer","product_id":"boox_air5c","criteria":["export","organization"],"claim":"BOOX documente synchronisation Onyx Cloud et transferts BOOXDrop pour fichiers, notes et annotations.","value":"Onyx sync + BOOXDrop","source":"https://shop.boox.com/products/noteair5c","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"air5c_keyboard","product_id":"boox_air5c","criteria":["apps"],"claim":"Un clavier optionnel est prévu pour emails, courts rapports et édition légère de feuilles ou présentations.","value":"optional keyboard cover","source":"https://shop.boox.com/products/noteair5c","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"remarkable_pro_org","product_id":"remarkable_pro","criteria":["organization","writing"],"claim":"Dossiers, tags, recherche et outils de notes sont documentés sur Paper Pro.","value":"folders + tags + search","source":"https://remarkable.com/products/remarkable-paper/pro/details/features","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"remarkable_pro_export","product_id":"remarkable_pro","criteria":["export","pdf"],"claim":"Export PDF/PNG/SVG, email, applications desktop/mobile et intégrations Drive/Dropbox/OneDrive sont documentés.","value":"PDF/PNG/SVG + cloud integrations","source":"https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"remarkable_connect","product_id":"remarkable_pro","criteria":["apps","no_sub"],"claim":"Connect ajoute recherche manuscrite, cloud illimité, apps éditables et intégrations/outils de travail ; les fonctions de base restent disponibles sans abonnement.","value":"advanced workflow partly subscription-gated","source":"https://remarkable.com/shop/connect/pricing","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"remarkable_pure_bundle","product_id":"remarkable_pure","criteria":["writing","no_sub"],"claim":"Paper Pure est vendu avec Marker inclus ; l'appareil utilise l'écosystème reMarkable.","value":"Marker included","source":"https://remarkable.com/fr-FR/shop/compare","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
        {"id":"remarkable_pure_export","product_id":"remarkable_pure","criteria":["export","pdf","organization"],"claim":"Les fonctions reMarkable d'import/export, tags, apps et intégrations s'appliquent au workflow de la gamme actuelle.","value":"reMarkable export/apps workflow","source":"https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files","checked_at":CHECKED_AT,"evidence_class":"VERIFIED"},
    ],
    "scores": {
        "boox_go_lumi": {
            "organization":{"score":8,"evidence_class":"INFERRED","evidence_refs":["boox_lumi_org"],"justification":"Outlines, tags et lasso offrent une organisation solide, mais moins structurée autour des liens/keywords que Supernote."},
            "export":{"score":10,"evidence_class":"INFERRED","evidence_refs":["boox_lumi_transfer","boox_lumi_apps"],"justification":"Multi-cloud, BOOXDrop, nombreux formats et liberté applicative donnent la sortie la plus ouverte du groupe."},
            "pdf":{"score":9,"evidence_class":"INFERRED","evidence_refs":["boox_lumi_transfer"],"justification":"Écran 10,3 pouces et prise en charge PDF/annotation riche ; moins confortable qu'un très grand format pour documents complexes."},
            "apps":{"score":10,"evidence_class":"INFERRED","evidence_refs":["boox_lumi_apps"],"justification":"Android 15 et Google Play constituent l'offre applicative la plus ouverte parmi les candidats retenus."},
            "writing":{"score":8,"evidence_class":"INFERRED","evidence_refs":["boox_lumi_org"],"justification":"Outils natifs complets pour capturer et retravailler des notes, sans prétendre mesurer la sensation d'écriture."},
            "simplicity":{"score":6,"evidence_class":"INFERRED","evidence_refs":["boox_lumi_apps","boox_lumi_org"],"justification":"L'ouverture Android augmente les possibilités mais aussi les réglages et choix par rapport aux OS spécialisés."},
            "no_sub":{"score":10,"evidence_class":"INFERRED","evidence_refs":["boox_lumi_bundle"],"justification":"Les fonctions centrales et le cloud Onyx de base ne nécessitent pas d'abonnement BOOX documenté."}
        },
        "supernote_manta": {
            "organization":{"score":10,"evidence_class":"INFERRED","evidence_refs":["supernote_org","supernote_links"],"justification":"Headings, keywords, stars et liens fournissent la structure manuscrite la plus poussée du groupe."},
            "export":{"score":9,"evidence_class":"INFERRED","evidence_refs":["supernote_transfer"],"justification":"Plusieurs clouds, email, USB et transfert local offrent une très bonne interopérabilité, malgré l'absence d'un écosystème d'apps généraliste."},
            "pdf":{"score":9,"evidence_class":"INFERRED","evidence_refs":["supernote_transfer"],"justification":"Le format 10,7 pouces et les workflows documentaires Supernote conviennent bien à l'annotation ; ce n'est pas un format A4."},
            "apps":{"score":5,"evidence_class":"INFERRED","evidence_refs":["supernote_platform"],"justification":"Le système est spécialisé et intégré, mais n'offre pas la liberté Google Play d'un BOOX."},
            "writing":{"score":10,"evidence_class":"INFERRED","evidence_refs":["supernote_org","supernote_links"],"justification":"Les outils de structuration et manipulation de notes sont au coeur du produit ; aucune sensation de stylet non testée n'est utilisée."},
            "simplicity":{"score":8,"evidence_class":"INFERRED","evidence_refs":["supernote_platform"],"justification":"OS spécialisé plus ciblé qu'Android généraliste, tout en conservant de nombreuses fonctions avancées."},
            "no_sub":{"score":10,"evidence_class":"INFERRED","evidence_refs":["supernote_no_sub"],"justification":"Le fabricant annonce explicitement l'absence d'abonnement pour les mises à jour et le logiciel."}
        },
        "boox_air5c": {
            "organization":{"score":8,"evidence_class":"INFERRED","evidence_refs":["air5c_transfer"],"justification":"Organisation et synchronisation solides, mais pas de différenciation documentaire supérieure à Supernote."},
            "export":{"score":10,"evidence_class":"INFERRED","evidence_refs":["air5c_transfer","air5c_apps"],"justification":"Android, services cloud et BOOXDrop rendent les sorties et transferts très ouverts."},
            "pdf":{"score":9,"evidence_class":"INFERRED","evidence_refs":["air5c_apps"],"justification":"10,3 pouces, PDF et split screen répondent bien à la revue documentaire."},
            "apps":{"score":10,"evidence_class":"INFERRED","evidence_refs":["air5c_apps","air5c_keyboard"],"justification":"Android 15, Google Play et clavier optionnel en font l'option la plus proche d'une tablette de productivité légère."},
            "writing":{"score":8,"evidence_class":"INFERRED","evidence_refs":["air5c_apps"],"justification":"Les outils de notes sont complets ; aucune note ne repose sur une sensation d'écriture non testée."},
            "simplicity":{"score":5,"evidence_class":"INFERRED","evidence_refs":["air5c_apps","air5c_keyboard"],"justification":"BSR, couleur, apps et clavier multiplient les usages mais aussi la complexité par rapport aux appareils spécialisés."},
            "no_sub":{"score":10,"evidence_class":"INFERRED","evidence_refs":["air5c_transfer"],"justification":"Les fonctions de base BOOX et la synchronisation Onyx documentée ne requièrent pas d'abonnement constructeur."}
        },
        "remarkable_pro": {
            "organization":{"score":8,"evidence_class":"INFERRED","evidence_refs":["remarkable_pro_org"],"justification":"Dossiers, tags et recherche offrent une organisation claire, moins relationnelle que les headings/links de Supernote."},
            "export":{"score":7,"evidence_class":"INFERRED","evidence_refs":["remarkable_pro_export","remarkable_connect"],"justification":"Les exports standards sont bons, mais une partie du workflow cloud et cross-device avancé dépend de Connect."},
            "pdf":{"score":9,"evidence_class":"INFERRED","evidence_refs":["remarkable_pro_export"],"justification":"Grand écran 11,8 pouces et export PDF en font un candidat solide pour documents et annotations."},
            "apps":{"score":3,"evidence_class":"INFERRED","evidence_refs":["remarkable_connect"],"justification":"Des intégrations de travail existent, mais reMarkable OS n'est pas une plateforme d'applications généraliste."},
            "writing":{"score":9,"evidence_class":"INFERRED","evidence_refs":["remarkable_pro_org"],"justification":"Outils natifs de notes et édition manuscrite riches ; aucune affirmation de sensation d'écriture issue d'un faux test."},
            "simplicity":{"score":9,"evidence_class":"INFERRED","evidence_refs":["remarkable_pro_org"],"justification":"OS spécialisé et centré sur notes/documents, donc plus simple à cadrer qu'un Android ouvert."},
            "no_sub":{"score":8,"evidence_class":"INFERRED","evidence_refs":["remarkable_connect"],"justification":"Le coeur fonctionne sans Connect, mais plusieurs fonctions professionnelles avancées sont réservées à l'abonnement."}
        },
        "remarkable_pure": {
            "organization":{"score":8,"evidence_class":"INFERRED","evidence_refs":["remarkable_pure_export"],"justification":"Le workflow reMarkable de dossiers/tags/apps reste solide pour un appareil de notes spécialisé."},
            "export":{"score":7,"evidence_class":"INFERRED","evidence_refs":["remarkable_pure_export","remarkable_connect"],"justification":"Exports standards et intégrations disponibles, avec des fonctions cloud avancées liées à Connect."},
            "pdf":{"score":8,"evidence_class":"INFERRED","evidence_refs":["remarkable_pure_export"],"justification":"Le 10,3 pouces reste adapté au PDF courant mais offre moins d'espace que Paper Pro."},
            "apps":{"score":3,"evidence_class":"INFERRED","evidence_refs":["remarkable_connect"],"justification":"Écosystème spécialisé avec intégrations plutôt qu'applications tierces généralistes."},
            "writing":{"score":9,"evidence_class":"INFERRED","evidence_refs":["remarkable_pure_bundle"],"justification":"Appareil centré sur le manuscrit avec Marker inclus ; le score n'est pas présenté comme mesure de sensation."},
            "simplicity":{"score":10,"evidence_class":"INFERRED","evidence_refs":["remarkable_pure_export"],"justification":"Le périmètre logiciel volontairement ciblé minimise les choix et réglages par rapport aux plateformes ouvertes."},
            "no_sub":{"score":8,"evidence_class":"INFERRED","evidence_refs":["remarkable_connect"],"justification":"Fonctions principales sans abonnement, mais certaines fonctions cloud/recherche/intégration restent liées à Connect."}
        }
    },
    "total_solution_cost": {
        "applies": true,
        "included_in_score": false,
        "comparison_basis":"configuration minimale permettant la prise de notes manuscrites",
        "reason_not_scored":"Les boutiques officielles n'affichent pas toutes une base régionale comparable et les taxes/imports varient. Le coût est traité comme overlay décisionnel plutôt que fausse note précise.",
        "products": {
            "boox_go_lumi":{"snapshot":"429,99–449,99 $ US selon les pages officielles consultées","stylus":"inclus","subscription":"aucun abonnement BOOX obligatoire documenté","confidence":"LOW_PRICE_VOLATILITY"},
            "supernote_manta":{"snapshot":"459 $ US sur la page produit consultée","stylus":"non listé dans le contenu de la boîte ; vérifier le panier avec un stylet","subscription":"aucun abonnement Supernote annoncé","confidence":"MEDIUM"},
            "boox_air5c":{"snapshot":"499,99 $ US sur la page produit consultée","stylus":"BOOX Pen3 inclus","subscription":"aucun abonnement BOOX obligatoire documenté","confidence":"MEDIUM"},
            "remarkable_pro":{"snapshot":"à partir de 649 €","stylus":"Marker inclus","subscription":"Connect optionnel mais plusieurs fonctions avancées en dépendent","confidence":"HIGH"},
            "remarkable_pure":{"snapshot":"à partir de 399 €","stylus":"Marker inclus","subscription":"Connect optionnel mais plusieurs fonctions avancées en dépendent","confidence":"HIGH"}
        }
    },
    "sensitivity": {
        "base_winner":"boox_go_lumi",
        "base_margin":0.05,
        "winner_stability":"CONDITIONAL_WINNER",
        "confidence":"MEDIUM",
        "scenarios":[
            {"id":"writing_plus5_apps_minus5","change":"apps 15→10 ; writing 15→20","winner":"supernote_manta","scores":{"supernote_manta":8.95,"boox_go_lumi":8.65,"boox_air5c":8.55}},
            {"id":"organization_plus5_apps_minus5","change":"apps 15→10 ; organization 20→25","winner":"supernote_manta","scores":{"supernote_manta":8.95,"boox_go_lumi":8.65,"boox_air5c":8.55}},
            {"id":"apps_plus5_writing_minus5","change":"apps 15→20 ; writing 15→10","winner":"boox_go_lumi","scores":{"boox_go_lumi":8.85,"boox_air5c":8.75,"supernote_manta":8.45}}
        ],
        "interpretation":"Le classement de tête dépend du poids accordé aux applications par rapport à l'organisation/écriture. Le #1 doit donc être présenté comme conditionnel."
    },
    "rank_justification": {
        "boox_go_lumi":{"best_for":"professionnels qui ont besoin d'applications tierces, de plusieurs voies d'export et d'un écran monochrome éclairé","not_for":"équipes dont l'IT interdit Google Play, certains clouds ou les appareils Android non gérés","decisive_advantage":"applications et interopérabilité","decisive_limit":"complexité et dépendance aux règles IT de l'organisation","alternative":"supernote_manta","position_reason":"gagne de très peu dans la grille de base grâce aux apps/export ; ne constitue pas un gagnant robuste si l'organisation manuscrite pèse davantage"},
        "supernote_manta":{"best_for":"professionnels qui structurent beaucoup d'idées, comptes rendus et connaissances manuscrites","not_for":"utilisateurs qui doivent installer des applications Android généralistes ou ont besoin d'un front light","decisive_advantage":"organisation manuscrite et workflow d'écriture","decisive_limit":"écosystème applicatif plus spécialisé","alternative":"boox_go_lumi","position_reason":"quasi ex aequo ; devient #1 dès que l'organisation ou l'écriture gagne quelques points de poids"},
        "boox_air5c":{"best_for":"professionnels qui veulent couleur, Google Play, split screen et clavier optionnel","not_for":"utilisateurs qui privilégient légèreté et simplicité","decisive_advantage":"polyvalence Android et couleur","decisive_limit":"poids et complexité supérieurs","alternative":"boox_go_lumi","position_reason":"très proche du Go Lumi mais pénalisé par une simplicité moindre dans ce job généraliste"},
        "remarkable_pro":{"best_for":"professionnels qui veulent un grand écran couleur et un environnement de notes spécialisé","not_for":"workflows dépendant de nombreuses applications tierces ou refusant un abonnement pour certaines fonctions avancées","decisive_advantage":"grand écran et simplicité de l'écosystème","decisive_limit":"ouverture applicative faible et dépendance partielle à Connect","alternative":"boox_air5c","position_reason":"bon outil documentaire mais nettement derrière sur apps/export dans la grille professionnelle retenue"},
        "remarkable_pure":{"best_for":"professionnels qui veulent un appareil monochrome simple pour notes et documents","not_for":"applications métier, grands PDF ou workflows très ouverts","decisive_advantage":"simplicité","decisive_limit":"ouverture et taille plus limitées","alternative":"remarkable_pro","position_reason":"cohérent pour un workflow minimaliste, mais moins complet sur PDF et intégrations que les candidats de tête"}
    },
    "editorial_verdict": {
        "label":"CONDITIONAL_WINNER",
        "primary":"BOOX Go 10.3 (Gen II) Lumi si les applications, Google Play et l'interopérabilité sont prioritaires.",
        "alternative":"Supernote Manta si l'organisation manuscrite, les liens entre notes et un workflow plus spécialisé comptent davantage.",
        "it_gate":"Dans une entreprise, la politique IT/cloud peut inverser le choix avant même le scoring."
    }
}

COMPARISON_METHODS = {PROFESSIONAL_METHOD["slug"]: PROFESSIONAL_METHOD}
