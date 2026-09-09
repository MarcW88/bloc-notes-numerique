"""Durable v2 comparison methodology.

Shared product facts live in comparison_products.py. This file stores the
page-level methodology that must survive metadata regeneration: universe
choices, equivalence, evidence, hard gates, score inferences, TSC, sensitivity
and rank justification.
"""

CHECKED_AT = "2026-09-09"


def ev(eid, pid, criteria, claim, value, source, evidence_class="VERIFIED"):
    return {
        "id": eid, "product_id": pid, "criteria": criteria, "claim": claim,
        "value": value, "source": source, "checked_at": CHECKED_AT,
        "evidence_class": evidence_class,
    }


def sc(score, refs, why):
    return {
        "score": score,
        "evidence_class": "INFERRED",
        "evidence_refs": refs,
        "justification": why,
    }


CRITERIA = {
    "organization": ("Organisation des notes", "Capacité documentée à structurer, retrouver et naviguer dans les notes de travail.", "Critère central quand les notes s'accumulent entre réunions, projets et dossiers."),
    "export": ("Export et interopérabilité", "Capacité documentée à faire sortir notes et documents vers des formats ou services utilisables hors de l'appareil.", "Un appareil professionnel ne doit pas transformer les notes en silo."),
    "pdf": ("PDF et annotation", "Compatibilité et outils documentés pour lire, annoter et réexporter des documents.", "Rapports, dossiers et ordres du jour constituent un cas d'usage professionnel fréquent."),
    "apps": ("Applications et intégrations", "Accès documenté à des applications tierces ou à des intégrations de travail.", "Important lorsque le workflow dépend d'outils externes, sans en faire un besoin universel."),
    "writing": ("Workflow d'écriture", "Outils natifs documentés pour écrire, sélectionner, structurer et retravailler des notes manuscrites, sans mesurer une sensation de stylet non testée.", "La capture manuscrite reste au cœur du job."),
    "simplicity": ("Simplicité opérationnelle", "Inférence éditoriale sur l'étendue et la complexité du logiciel nécessaire pour accomplir le job.", "La friction logicielle compte au quotidien mais reste secondaire face à l'interopérabilité."),
    "no_sub": ("Fonctions sans abonnement", "Part des fonctions centrales accessibles sans abonnement constructeur obligatoire.", "Le coût récurrent compte sans être le premier déterminant de cette page généraliste."),
}

UNIVERSE = [
    {"id":"boox_go_lumi","status":"ELIGIBLE","equivalence":"FUNCTIONALLY_COMPARABLE","reason":"10,3 pouces, stylet, PDF, organisation native, Android 15/Google Play et front light : couvre le job généraliste.","source":"https://shop.boox.com/products/go103gen2lumi"},
    {"id":"supernote_manta","status":"ELIGIBLE","equivalence":"FUNCTIONALLY_COMPARABLE","reason":"10,7 pouces, stylet, PDF et organisation manuscrite avancée ; proposition spécialisée mais comparable sur le job.","source":"https://supernote.com/products/supernote-manta"},
    {"id":"remarkable_pure","status":"ELIGIBLE","equivalence":"FUNCTIONALLY_COMPARABLE","reason":"10,3 pouces monochrome, stylet inclus, notes, PDF, export et intégrations dans un écosystème spécialisé.","source":"https://remarkable.com/fr-FR/shop/compare"},
    {"id":"remarkable_pro","status":"ELIGIBLE","equivalence":"FUNCTIONALLY_COMPARABLE","reason":"11,8 pouces couleur, stylet inclus, PDF, organisation et intégrations de travail.","source":"https://remarkable.com/fr-FR/products/remarkable-paper/pro"},
    {"id":"boox_air5c","status":"ELIGIBLE","equivalence":"FUNCTIONALLY_COMPARABLE","reason":"10,3 pouces couleur, stylet, Android 15, Google Play, PDF et clavier optionnel ; plus polyvalent et plus complexe.","source":"https://shop.boox.com/products/noteair5c"},
    {"id":"boox_notemax","status":"EXCLUDED","equivalence":"PARTIALLY_COMPARABLE","reason":"Très pertinent pour PDF A4, mais son format 13,3 pouces, son poids et l'absence de front light en font un cas spécialisé.","source":"https://shop.boox.com/products/notemax","handoff":"/comparatifs/bloc-notes-numerique-a4/"},
    {"id":"kindle_scribe3","status":"EXCLUDED","equivalence":"PARTIALLY_COMPARABLE","reason":"Les modèles récents exportent vers plusieurs services, mais le produit reste davantage centré sur lecture et carnets qu'un environnement d'applications de travail généraliste.","source":"https://digprjsurvey.amazon.com/csad/help/node/TP8wuaQilIlwlITVTL"},
    {"id":"kobo_elipsa","status":"EXCLUDED","equivalence":"PARTIALLY_COMPARABLE","reason":"Carnets et exports sont documentés, mais l'écosystème reste d'abord celui d'une liseuse et certaines annotations de livres ne sont pas exportables.","source":"https://help.kobo.com/hc/fr/articles/360062226733-Utiliser-votre-liseuse-Kobo-comme-un-carnet"},
    {"id":"supernote_nomad","status":"EXCLUDED","equivalence":"PARTIALLY_COMPARABLE","reason":"Très mobile mais 7,8 pouces ; moins adapté au job généraliste incluant une revue régulière de PDF.","source":"https://supernote.com/products/supernote-nomad"},
    {"id":"remarkable_move","status":"EXCLUDED","equivalence":"PARTIALLY_COMPARABLE","reason":"Le format 7,3 pouces privilégie la mobilité ; il n'est pas retenu pour un comparatif professionnel généraliste avec PDF.","source":"https://remarkable.com/fr-FR/products/remarkable-paper/pro-move/details/features"},
]

EVIDENCE = [
    ev("boox_lumi_apps","boox_go_lumi",["apps"],"Android 15, Google Play Store intégré et applications tierces pris en charge.","Android 15 + Google Play","https://shop.boox.com/products/go103gen2lumi"),
    ev("boox_lumi_org","boox_go_lumi",["organization","writing"],"Outlines, tags, lasso et conversion manuscrite sont documentés.","outlines + tags + lasso","https://shop.boox.com/products/go103gen2lumi"),
    ev("boox_lumi_transfer","boox_go_lumi",["export","pdf"],"Synchronisation Onyx Cloud, Google Drive, Dropbox et OneDrive, BOOXDrop et prise en charge PDF.","multi-cloud + BOOXDrop + PDF","https://shop.boox.com/products/go103gen2lumi"),
    ev("boox_lumi_bundle","boox_go_lumi",["no_sub"],"Stylet inclus et cloud Onyx de base documenté sans abonnement BOOX obligatoire pour les fonctions centrales.","stylus included + base cloud","https://shop.boox.com/products/go103gen2lumi"),
    ev("supernote_org","supernote_manta",["organization","writing"],"Headings, keywords, stars et outils de structuration sont documentés.","headings + keywords + stars","https://support.supernote.com/en_US/organizing/1759244-using-titles-keywords-and-stars"),
    ev("supernote_links","supernote_manta",["organization","writing"],"Des liens peuvent pointer vers pages, fichiers ou pages web.","internal/file/web links","https://support.supernote.com/inserting-links-to-notebooks?kb_language=en_US"),
    ev("supernote_transfer","supernote_manta",["export","pdf"],"Transfert via Supernote Cloud, Dropbox, Google Drive, email, USB et outils locaux documenté.","multi-route transfer","https://support.supernote.com/en_US/transfer-files"),
    ev("supernote_platform","supernote_manta",["apps","simplicity"],"Manta utilise Chauvet, un système spécialisé basé sur Android 11.","specialized Android-based OS","https://supernote.com/products/supernote-manta"),
    ev("supernote_no_sub","supernote_manta",["no_sub"],"Supernote annonce des mises à jour logicielles sans abonnement.","no subscription","https://supernote.com/pages/supernote-manta"),
    ev("air5c_apps","boox_air5c",["apps","pdf"],"Android 15, Google Play, applications tierces, split screen et formats PDF/bureautiques documentés.","Android 15 + Google Play + split screen","https://shop.boox.com/products/noteair5c"),
    ev("air5c_transfer","boox_air5c",["export","organization"],"Synchronisation Onyx Cloud et BOOXDrop documentés pour fichiers, notes et annotations.","Onyx sync + BOOXDrop","https://shop.boox.com/products/noteair5c"),
    ev("air5c_keyboard","boox_air5c",["apps"],"Un clavier optionnel est prévu pour emails, courts rapports et édition légère.","optional keyboard cover","https://shop.boox.com/products/noteair5c"),
    ev("remarkable_pro_org","remarkable_pro",["organization","writing"],"Dossiers, tags, recherche et outils de notes sont documentés.","folders + tags + search","https://remarkable.com/products/remarkable-paper/pro/details/features"),
    ev("remarkable_pro_export","remarkable_pro",["export","pdf"],"Export PDF/PNG/SVG, applications et intégrations Drive/Dropbox/OneDrive documentés.","PDF/PNG/SVG + cloud integrations","https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files"),
    ev("remarkable_connect","remarkable_pro",["apps","no_sub"],"Connect ajoute des fonctions avancées de recherche, cloud, apps et intégrations ; les fonctions de base restent disponibles sans abonnement.","advanced workflow partly subscription-gated","https://remarkable.com/shop/connect/pricing"),
    ev("remarkable_pure_bundle","remarkable_pure",["writing","no_sub"],"Paper Pure est vendu avec Marker inclus.","Marker included","https://remarkable.com/fr-FR/shop/compare"),
    ev("remarkable_pure_export","remarkable_pure",["export","pdf","organization"],"Le workflow reMarkable documente import/export, tags, applications et intégrations cloud.","reMarkable export/apps workflow","https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files"),
]

SCORES = {
    "boox_go_lumi": {
        "organization":sc(8,["boox_lumi_org"],"Outlines, tags et lasso offrent une organisation solide, mais moins structurée autour des liens et mots-clés que Supernote."),
        "export":sc(10,["boox_lumi_transfer","boox_lumi_apps"],"Multi-cloud, BOOXDrop, nombreux formats et liberté applicative donnent la sortie la plus ouverte du groupe."),
        "pdf":sc(9,["boox_lumi_transfer"],"Écran 10,3 pouces et prise en charge PDF riche ; moins confortable qu'un très grand format pour les documents complexes."),
        "apps":sc(10,["boox_lumi_apps"],"Android 15 et Google Play constituent l'offre applicative la plus ouverte parmi les candidats retenus."),
        "writing":sc(8,["boox_lumi_org"],"Outils natifs complets pour capturer et retravailler des notes, sans prétendre mesurer une sensation d'écriture."),
        "simplicity":sc(6,["boox_lumi_apps","boox_lumi_org"],"L'ouverture Android augmente les possibilités mais aussi les réglages et choix par rapport aux OS spécialisés."),
        "no_sub":sc(10,["boox_lumi_bundle"],"Les fonctions centrales documentées ne nécessitent pas d'abonnement BOOX obligatoire."),
    },
    "supernote_manta": {
        "organization":sc(10,["supernote_org","supernote_links"],"Headings, keywords, stars et liens fournissent la structure manuscrite la plus poussée du groupe."),
        "export":sc(9,["supernote_transfer"],"Plusieurs clouds, email, USB et transfert local offrent une très bonne interopérabilité malgré l'absence d'un écosystème d'apps généraliste."),
        "pdf":sc(9,["supernote_transfer"],"Le format 10,7 pouces et les workflows documentaires conviennent bien à l'annotation sans constituer un format A4."),
        "apps":sc(5,["supernote_platform"],"Le système est spécialisé et intégré, mais n'offre pas la liberté Google Play d'un BOOX."),
        "writing":sc(10,["supernote_org","supernote_links"],"Les outils de structuration et manipulation des notes sont au cœur du produit ; aucune sensation de stylet non testée n'est utilisée."),
        "simplicity":sc(8,["supernote_platform"],"Un OS spécialisé est plus ciblé qu'Android généraliste tout en conservant de nombreuses fonctions avancées."),
        "no_sub":sc(10,["supernote_no_sub"],"Le fabricant annonce explicitement l'absence d'abonnement pour le logiciel et les mises à jour."),
    },
    "boox_air5c": {
        "organization":sc(8,["air5c_transfer"],"Organisation et synchronisation solides, sans différenciation documentaire supérieure à Supernote."),
        "export":sc(10,["air5c_transfer","air5c_apps"],"Android, services cloud et BOOXDrop rendent les sorties et transferts très ouverts."),
        "pdf":sc(9,["air5c_apps"],"10,3 pouces, PDF et split screen répondent bien à la revue documentaire."),
        "apps":sc(10,["air5c_apps","air5c_keyboard"],"Android 15, Google Play et clavier optionnel en font l'option la plus proche d'une tablette de productivité légère."),
        "writing":sc(8,["air5c_apps"],"Les outils de notes sont complets ; aucune note ne repose sur une sensation d'écriture non testée."),
        "simplicity":sc(5,["air5c_apps","air5c_keyboard"],"Couleur, apps et clavier multiplient les usages mais aussi la complexité par rapport aux appareils spécialisés."),
        "no_sub":sc(10,["air5c_transfer"],"Les fonctions de base BOOX documentées ne requièrent pas d'abonnement constructeur."),
    },
    "remarkable_pro": {
        "organization":sc(8,["remarkable_pro_org"],"Dossiers, tags et recherche offrent une organisation claire, moins relationnelle que les headings et liens de Supernote."),
        "export":sc(7,["remarkable_pro_export","remarkable_connect"],"Les exports standards sont bons, mais une partie du workflow cloud et cross-device avancé dépend de Connect."),
        "pdf":sc(9,["remarkable_pro_export"],"Le grand écran et l'export PDF en font un candidat solide pour documents et annotations."),
        "apps":sc(3,["remarkable_connect"],"Des intégrations de travail existent, mais reMarkable OS n'est pas une plateforme d'applications généraliste."),
        "writing":sc(9,["remarkable_pro_org"],"Outils natifs de notes riches, sans affirmation de sensation d'écriture issue d'un faux test."),
        "simplicity":sc(9,["remarkable_pro_org"],"OS spécialisé et centré sur notes et documents, donc plus simple à cadrer qu'un Android ouvert."),
        "no_sub":sc(8,["remarkable_connect"],"Le cœur fonctionne sans Connect, mais plusieurs fonctions professionnelles avancées sont liées à l'abonnement."),
    },
    "remarkable_pure": {
        "organization":sc(8,["remarkable_pure_export"],"Le workflow de dossiers, tags et applications reste solide pour un appareil de notes spécialisé."),
        "export":sc(7,["remarkable_pure_export","remarkable_connect"],"Exports standards et intégrations disponibles, avec des fonctions cloud avancées liées à Connect."),
        "pdf":sc(8,["remarkable_pure_export"],"Le 10,3 pouces reste adapté au PDF courant mais offre moins d'espace que Paper Pro."),
        "apps":sc(3,["remarkable_connect"],"Écosystème spécialisé avec intégrations plutôt qu'applications tierces généralistes."),
        "writing":sc(9,["remarkable_pure_bundle"],"Appareil centré sur le manuscrit avec Marker inclus ; le score n'est pas présenté comme une mesure de sensation."),
        "simplicity":sc(10,["remarkable_pure_export"],"Le périmètre logiciel volontairement ciblé minimise les choix et réglages par rapport aux plateformes ouvertes."),
        "no_sub":sc(8,["remarkable_connect"],"Fonctions principales sans abonnement, avec plusieurs fonctions cloud ou d'intégration liées à Connect."),
    },
}

RANK_JUSTIFICATION = {
    "boox_go_lumi":{"best_for":"professionnels qui ont besoin d'applications tierces, de plusieurs voies d'export et d'un écran monochrome éclairé","not_for":"équipes dont l'IT interdit Google Play, certains clouds ou les appareils Android non gérés","decisive_advantage":"applications et interopérabilité","decisive_limit":"complexité et dépendance aux règles IT de l'organisation","alternative":"supernote_manta","position_reason":"gagne de très peu grâce aux apps et à l'export ; ce n'est pas un gagnant robuste si l'organisation manuscrite pèse davantage"},
    "supernote_manta":{"best_for":"professionnels qui structurent beaucoup d'idées, comptes rendus et connaissances manuscrites","not_for":"utilisateurs qui doivent installer des applications Android généralistes ou ont besoin d'un front light","decisive_advantage":"organisation manuscrite et workflow d'écriture","decisive_limit":"écosystème applicatif plus spécialisé","alternative":"boox_go_lumi","position_reason":"quasi ex aequo ; devient premier dès que l'organisation ou l'écriture gagne quelques points de poids"},
    "boox_air5c":{"best_for":"professionnels qui veulent couleur, Google Play, split screen et clavier optionnel","not_for":"utilisateurs qui privilégient légèreté et simplicité","decisive_advantage":"polyvalence Android et couleur","decisive_limit":"poids et complexité supérieurs","alternative":"boox_go_lumi","position_reason":"très proche du Go Lumi mais pénalisé par une simplicité moindre dans ce job généraliste"},
    "remarkable_pro":{"best_for":"professionnels qui veulent un grand écran couleur et un environnement de notes spécialisé","not_for":"workflows dépendant de nombreuses applications tierces ou refusant un abonnement pour certaines fonctions avancées","decisive_advantage":"grand écran et simplicité de l'écosystème","decisive_limit":"ouverture applicative faible et dépendance partielle à Connect","alternative":"boox_air5c","position_reason":"bon outil documentaire mais nettement derrière sur apps et export dans la grille professionnelle retenue"},
    "remarkable_pure":{"best_for":"professionnels qui veulent un appareil monochrome simple pour notes et documents","not_for":"applications métier, grands PDF ou workflows très ouverts","decisive_advantage":"simplicité","decisive_limit":"ouverture et taille plus limitées","alternative":"remarkable_pro","position_reason":"cohérent pour un workflow minimaliste, mais moins complet sur PDF et intégrations que les candidats de tête"},
}

PROFESSIONAL_METHOD = {
    "schema_version": 2,
    "slug": "bloc-notes-numerique-professionnel",
    "decision_contract": {
        "type": "best_for_use_case",
        "query": "meilleur bloc-notes numérique professionnel",
        "user_job": "gérer réunions, PDF, exports et outils de travail",
        "decision": "choisir un appareil E Ink de travail pour capturer des notes, annoter des documents et les réintégrer dans un environnement professionnel",
        "non_goals": ["remplacer un PC pour les tâches bureautiques complexes", "désigner un meilleur appareil universel indépendamment des contraintes IT"],
    },
    "criteria_definitions": {cid:{"label":v[0],"definition":v[1],"weight_rationale":v[2]} for cid,v in CRITERIA.items()},
    "universe": UNIVERSE,
    "hard_gates": [
        {"id":"current_and_documented","scope":"UNIVERSAL","rule":"Le modèle doit être actuel et documenté par une source officielle consultable.","failure_effect":"EXCLUDE"},
        {"id":"handwriting_pdf_core","scope":"UNIVERSAL","rule":"Le modèle doit permettre la prise de notes manuscrites et la lecture ou annotation de PDF.","failure_effect":"EXCLUDE"},
        {"id":"standard_exit_path","scope":"UNIVERSAL","rule":"Le workflow doit disposer d'au moins une sortie documentée vers un format ou service utilisable hors de l'appareil.","failure_effect":"EXCLUDE"},
        {"id":"company_it_policy","scope":"USER_SPECIFIC","rule":"Le cloud, les comptes et applications nécessaires doivent être autorisés par la politique IT de l'organisation.","failure_effect":"USER_MUST_EXCLUDE","note":"Ce gate varie selon l'entreprise et reste visible dans le verdict."},
        {"id":"required_business_app","scope":"USER_SPECIFIC","rule":"Si une application métier précise est indispensable, sa disponibilité et sa compatibilité doivent être confirmées avant achat.","failure_effect":"USER_MUST_EXCLUDE"},
    ],
    "evidence_ledger": EVIDENCE,
    "scores": SCORES,
    "total_solution_cost": {
        "applies": True,
        "included_in_score": False,
        "comparison_basis":"configuration minimale permettant la prise de notes manuscrites",
        "reason_not_scored":"Les boutiques officielles n'affichent pas toutes une base régionale comparable et les taxes ou imports varient ; le coût reste un overlay décisionnel.",
        "products": {
            "boox_go_lumi":{"snapshot":"429,99–449,99 $ US selon les pages officielles consultées","stylus":"inclus","subscription":"aucun abonnement BOOX obligatoire documenté","confidence":"LOW_PRICE_VOLATILITY"},
            "supernote_manta":{"snapshot":"459 $ US sur la page produit consultée","stylus":"non listé dans le contenu de la boîte ; vérifier le panier avec un stylet","subscription":"aucun abonnement Supernote annoncé","confidence":"MEDIUM"},
            "boox_air5c":{"snapshot":"499,99 $ US sur la page produit consultée","stylus":"BOOX Pen3 inclus","subscription":"aucun abonnement BOOX obligatoire documenté","confidence":"MEDIUM"},
            "remarkable_pro":{"snapshot":"à partir de 649 €","stylus":"Marker inclus","subscription":"Connect optionnel mais plusieurs fonctions avancées en dépendent","confidence":"HIGH"},
            "remarkable_pure":{"snapshot":"à partir de 399 €","stylus":"Marker inclus","subscription":"Connect optionnel mais plusieurs fonctions avancées en dépendent","confidence":"HIGH"},
        },
    },
    "sensitivity": {
        "base_winner":"boox_go_lumi","base_margin":0.05,"winner_stability":"CONDITIONAL_WINNER","confidence":"MEDIUM",
        "scenarios":[
            {"id":"writing_plus5_apps_minus5","change":"apps 15→10 ; writing 15→20","winner":"supernote_manta","scores":{"supernote_manta":8.95,"boox_go_lumi":8.65,"boox_air5c":8.55}},
            {"id":"organization_plus5_apps_minus5","change":"apps 15→10 ; organization 20→25","winner":"supernote_manta","scores":{"supernote_manta":8.95,"boox_go_lumi":8.65,"boox_air5c":8.55}},
            {"id":"apps_plus5_writing_minus5","change":"apps 15→20 ; writing 15→10","winner":"boox_go_lumi","scores":{"boox_go_lumi":8.85,"boox_air5c":8.75,"supernote_manta":8.45}},
        ],
        "interpretation":"Le classement de tête dépend du poids accordé aux applications par rapport à l'organisation ou l'écriture ; le #1 doit être conditionnel.",
    },
    "rank_justification": RANK_JUSTIFICATION,
    "editorial_verdict": {
        "label":"CONDITIONAL_WINNER",
        "primary":"BOOX Go 10.3 (Gen II) Lumi si les applications, Google Play et l'interopérabilité sont prioritaires.",
        "alternative":"Supernote Manta si l'organisation manuscrite, les liens entre notes et un workflow plus spécialisé comptent davantage.",
        "it_gate":"Dans une entreprise, la politique IT ou cloud peut inverser le choix avant même le scoring.",
    },
}

COMPARISON_METHODS = {PROFESSIONAL_METHOD["slug"]: PROFESSIONAL_METHOD}
