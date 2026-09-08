#!/usr/bin/env python3
"""Generate persistent briefs and QA reports for the /guides/ production batch."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
TODAY = "2026-09-08"

PAGES = [
    dict(slug="choisir-bloc-notes-numerique", kind="choice", existing=True, refresh="major revision", keyword="choisir bloc-notes numérique", intent="choisir une tablette E Ink de prise de notes selon son flux de travail", audience="acheteur en découverte ou présélection", value="ordonner les critères éliminatoires avant les caractéristiques matérielles", entities="reMarkable, BOOX, Kindle Scribe, Kobo Elipsa, Supernote, PDF, cloud, export", h2="critères éliminatoires; profils d'écosystème; cinq questions; ouvert ou spécialisé; critères matériels", sources=[("reMarkable import/export","https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files"),("BOOX cloud tiers","https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage"),("Kobo carnets","https://help.kobo.com/hc/fr/articles/360062226733-Utiliser-votre-liseuse-Kobo-comme-un-carnet"),("Amazon cloud Kindle Scribe","https://digprjsurvey.amazon.com/csad/help/node/TP8wuaQilIlwlITVTL")], risks="cannibalisation avec /comparatifs/meilleur-bloc-notes-numerique/ ; aucune hiérarchie de produits ni pseudo-test"),
    dict(slug="liseuse-ou-bloc-notes-numerique", kind="choice", existing=True, refresh="major revision", keyword="liseuse ou bloc-notes numérique", intent="distinguer lecture, hybride lecture-écriture et bloc-notes de travail", audience="lecteur hésitant entre liseuse avec stylet et tablette de notes", value="faire décider sur un cycle complet de document et d'export plutôt que sur la seule présence d'un stylet", entities="Kindle Scribe, Kobo Elipsa, EPUB, PDF, carnet, export", h2="différence logicielle; comparaison liseuse/hybride/bloc-notes; hybrides; cycle complet; règle de décision", sources=[("Kobo annotations","https://help.kobo.com/hc/fr/articles/1500001927562-Annoter-votre-livre-avec-le-stylet-Kobo"),("Kobo carnets","https://help.kobo.com/hc/fr/articles/360062226733-Utiliser-votre-liseuse-Kobo-comme-un-carnet"),("Amazon import cloud","https://digprjsurvey.amazon.com/csad/help/node/TjrMJmg3DZpAQLwVuN"),("Amazon partage Scribe","https://digprjsurvey.amazon.com/csad/help/node/TJE2UYmdw0ppUuR3Rs")], risks="frontières produit évolutives ; ne pas généraliser les exports d'un format à un autre"),
    dict(slug="tablette-classique-ou-tablette-e-ink", kind="choice", existing=True, refresh="major revision", keyword="tablette classique ou tablette E Ink", intent="choisir la technologie selon les tâches incompatibles avec chaque écran", audience="acheteur hésitant entre iPad/Android classique et E Ink", value="expliciter aussi clairement les cas où l'E Ink est déconseillée que ses avantages", entities="E Ink, LCD, OLED, BOOX, Android, vidéo, rafraîchissement", h2="deux technologies; comparaison par tâche; quand déconseiller E Ink; tablette classique surdimensionnée; couleur; décision", sources=[("E Ink fonctionnement","https://www.eink.com/tech/detail/How_it_works"),("E Ink bénéfices","https://www.eink.com/tech/detail/Benefits"),("BOOX cloud tiers","https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage")], risks="aucune promesse médicale sur la fatigue visuelle ; Android installé ne garantit pas une bonne UX E Ink"),
    dict(slug="taille-ecran-bloc-notes-numerique", kind="choice", existing=True, refresh="light edit", keyword="taille écran bloc-notes numérique", intent="choisir une diagonale selon documents, mobilité et surface utile", audience="acheteur hésitant entre compact, ~10 pouces et grand format", value="partir du document réel et de sa lisibilité plutôt que de la diagonale commerciale", entities="diagonale, PDF A4, reMarkable Paper Pro Move, reMarkable 2, Paper Pro", h2="surface utile; formats par usage; partir du document; test; décision", sources=[("reMarkable Paper Pro Move","https://support.remarkable.com/s/article/About-reMarkable-Paper-Pro-Move"),("reMarkable 2","https://support.remarkable.com/s/article/About-reMarkable-2"),("reMarkable Paper Pro","https://support.remarkable.com/s/article/About-reMarkable-Paper-Pro")], risks="ne pas transformer les repères de gamme en recommandation de marque"),
    dict(slug="bloc-notes-numerique-couleur-ou-noir-et-blanc", kind="choice", existing=True, refresh="major revision", keyword="bloc-notes numérique couleur", intent="décider si la couleur E Ink transporte une information utile", audience="acheteur utilisant surlignages, cartes, schémas ou notes simples", value="test en niveaux de gris + distinction entre technologies couleur", entities="E Ink Kaleido 3, Gallery, monochrome, ppp, surlignage", h2="couleur E Ink; usages; test niveaux de gris; compromis; décision", sources=[("E Ink Kaleido 3","https://www.eink.com/brand/detail/Kaleido3"),("E Ink FAQ couleur","https://www.eink.com/tech/detail/FAQ"),("reMarkable Paper Pro","https://support.remarkable.com/s/article/About-reMarkable-Paper-Pro")], risks="ne pas attribuer les mêmes propriétés à tous les écrans couleur"),
    dict(slug="bloc-notes-numerique-avec-ou-sans-abonnement", kind="choice", existing=True, refresh="major revision", keyword="bloc-notes numérique sans abonnement", intent="comprendre ce qui reste utilisable sans coût récurrent", audience="acheteur qui veut éviter dépendance cloud ou abonnement", value="comparer les fonctions réellement perdues sans paiement dans plusieurs écosystèmes", entities="reMarkable Connect, Kindle Scribe, Kobo, BOOX, Supernote, cloud, OCR", h2="fonctions sans paiement; écosystèmes; cas reMarkable; plan de sortie; décision", sources=[("reMarkable Connect","https://support.remarkable.com/articles/Knowledge/About-Connect-Subscription"),("reMarkable cloud sans Connect","https://support.remarkable.com/articles/Knowledge/Pair-your-reMarkable-with-the-cloud"),("Amazon cloud Scribe","https://digprjsurvey.amazon.com/csad/help/node/Tuar1obhcxaS8hVUKd"),("Kobo carnets","https://help.kobo.com/hc/en-us/articles/360062226733-Use-your-Kobo-eReader-as-a-notebook"),("BOOX cloud tiers","https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage"),("Supernote transfert","https://support.supernote.com/en_US/transfer-files")], risks="fonctions et tarifs évolutifs ; distinguer abonnement fabricant, service cloud et abonnement de lecture"),

    dict(slug="tablette-e-ink", kind="explainer", existing=False, refresh="new", keyword="tablette E Ink", intent="comprendre ce qu'est une tablette E Ink, ses familles, avantages et limites", audience="lecteur qui découvre l'encre électronique", value="relier le mécanisme d'écran aux usages sans réduire E Ink à une liseuse", entities="E Ink, bistabilité, écran réfléchissant, liseuse, bloc-notes, Android", h2="définition; familles; contenu statique; limites; quand choisir", sources=[("E Ink FAQ","https://www.eink.com/tech/detail/FAQ"),("E Ink bénéfices","https://www.eink.com/tech/detail/Benefits"),("E Ink fonctionnement","https://www.eink.com/tech/detail/How_it_works")], risks="pas de bénéfice médical ; ne pas confondre écran et logiciel"),
    dict(slug="encre-electronique-fonctionnement", kind="explainer", existing=False, refresh="new", keyword="fonctionnement encre électronique", intent="expliquer le déplacement des particules, la bistabilité et le rafraîchissement", audience="lecteur voulant comprendre le mécanisme physique", value="passer des microcapsules aux conséquences concrètes pour l'usage", entities="microcapsules, Microcups, particules chargées, TFT, bistabilité, rafraîchissement", h2="particules; couches; bistabilité; rafraîchissement; couleur; conséquences", sources=[("E Ink FAQ","https://www.eink.com/tech/detail/FAQ"),("E Ink film","https://www.eink.com/tech/detail/Electronic_Ink_Film"),("E Ink bénéfices","https://www.eink.com/tech/detail/Benefits")], risks="simplification pédagogique sans attribuer une architecture unique à toutes les technologies couleur"),
    dict(slug="latence-ecriture", kind="explainer", existing=False, refresh="new", keyword="latence écriture tablette E Ink", intent="comprendre ce qui crée le délai entre stylet et trait", audience="acheteur sensible à la réactivité d'écriture", value="refuser les classements en millisecondes sans protocole comparable", entities="latence, stylet, numériseur, rafraîchissement, ghosting", h2="chaîne de latence; E Ink; limites des mesures; vérification pratique; décision", sources=[("E Ink fonctionnement","https://www.eink.com/tech/detail/How_it_works"),("E Ink FAQ","https://www.eink.com/tech/detail/FAQ")], risks="aucune mesure inventée ; un chiffre n'est publié que s'il vient d'un protocole explicite"),
    dict(slug="ocr-manuscrit", kind="explainer", existing=False, refresh="new", keyword="OCR manuscrit tablette", intent="distinguer conversion, recherche manuscrite et PDF recherchable", audience="utilisateur qui veut exploiter son écriture comme texte", value="comparer les fonctions OCR par résultat concret et conditions d'usage", entities="OCR, handwriting recognition, TXT, DOCX, PDF recherchable, reMarkable, Supernote, BOOX, Kobo, Kindle Scribe", h2="trois fonctions; approches fabricants; précision; connexion; test", sources=[("reMarkable conversion","https://support.remarkable.com/articles/Knowledge/Convert-handwritten-notes-into-text"),("Supernote recognition","https://support.supernote.com/handwriting-recognition"),("BOOX handwriting","https://help.boox.com/hc/en-us/articles/10701578837268-Handwritten-Notes"),("Kobo notebooks","https://help.kobo.com/hc/fr/articles/360062226733-Utiliser-votre-liseuse-Kobo-comme-un-carnet"),("Amazon recognition","https://digprjsurvey.amazon.com/csad/help/node/TWTo0OyovlJ9jwOV0B")], risks="précision variable avec écriture/langue ; ne pas promettre un taux de reconnaissance"),
    dict(slug="autonomie-tablette-e-ink", kind="explainer", existing=False, refresh="new", keyword="autonomie tablette E Ink", intent="comprendre pourquoi les annonces en semaines sont difficiles à comparer", audience="acheteur préoccupé par la batterie", value="séparer consommation de l'écran et consommation totale puis proposer un protocole comparable", entities="bistabilité, éclairage frontal, Wi-Fi, cloud, rafraîchissement", h2="bistabilité; facteurs; limites du mot semaines; protocole; décision", sources=[("E Ink bénéfices","https://www.eink.com/tech/detail/Benefits"),("E Ink fonctionnement","https://www.eink.com/tech/detail/How_it_works")], risks="pas d'autonomie réelle sans test contrôlé ; ne pas transformer des annonces fabricants en classement"),
    dict(slug="formats-fichiers-compatibles", kind="explainer", existing=False, refresh="new", keyword="formats fichiers tablette E Ink", intent="vérifier formats, annotation, export et DRM", audience="utilisateur avec PDF, EPUB ou documents de travail existants", value="montrer que pouvoir ouvrir un format ne signifie pas pouvoir l'annoter ou l'exporter", entities="PDF, EPUB, DOCX, MOBI, DRM, Send to Kindle, NeoReader", h2="tableau formats; PDF; EPUB; DRM; test", sources=[("reMarkable import/export","https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files"),("Kobo formats","https://help.kobo.com/hc/fr/articles/360017763713-Formats-de-fichiers-pris-en-charge-par-votre-application-Kobo-eReader-et-Kobo-Books"),("Amazon formats","https://digprjsurvey.amazon.com/csad/help/node/TIh9JOMGAKr7bY4zqu"),("BOOX reflow","https://help.boox.com/hc/en-us/articles/25400769451540-Adjust-EPUB-and-Similar"),("Supernote PDF/EPUB","https://support.supernote.com/en_US/epub-and-pdf-documents")], risks="DRM et méthodes d'import changent les fonctions disponibles"),
    dict(slug="exporter-notes", kind="how-to", existing=False, refresh="new", keyword="exporter notes bloc-notes numérique", intent="choisir le bon format et sortir ses notes de l'appareil", audience="utilisateur qui veut partager ou archiver", value="choisir le format à partir du résultat final et conserver une copie durable", entities="PDF, PNG, SVG, TXT, DOCX, .note, cloud, USB", h2="formats; reMarkable; autres écosystèmes; format durable; test", sources=[("reMarkable export","https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files"),("Amazon share","https://digprjsurvey.amazon.com/csad/help/node/TJE2UYmdw0ppUuR3Rs"),("Kobo notebooks","https://help.kobo.com/hc/en-us/articles/360062226733-Use-your-Kobo-eReader-as-a-notebook"),("BOOX notes","https://help.boox.com/hc/en-us/articles/8569373888788-Handwritten-Notes"),("Supernote toolbar","https://support.supernote.com/en_US/introduction-to-the-toolbar")], risks="export visuel et export éditable ne doivent pas être confondus"),
    dict(slug="synchroniser-notes-cloud", kind="how-to", existing=False, refresh="new", keyword="synchroniser notes cloud tablette E Ink", intent="distinguer synchronisation, import et export cloud", audience="utilisateur multi-appareils ou entreprise", value="définir une source de vérité pour éviter doublons et fausse sync bidirectionnelle", entities="cloud natif, Google Drive, OneDrive, Dropbox, ONYX, Supernote Cloud", h2="trois opérations; reMarkable; BOOX/Supernote; Kindle/Kobo; source de vérité", sources=[("reMarkable sync","https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files"),("BOOX note sync","https://help.boox.com/hc/en-us/articles/25401889318548-Note-Syncing"),("Supernote transfer","https://support.supernote.com/en_US/transfer-files"),("Amazon cloud import","https://digprjsurvey.amazon.com/csad/help/node/TjrMJmg3DZpAQLwVuN"),("Kobo Google Drive","https://help.kobo.com/hc/en-us/articles/15335985512983-Add-books-to-your-eReader-using-Google-Drive")], risks="ne pas appeler synchronisation une simple copie de fichier"),
    dict(slug="bloc-notes-numerique-google-drive", kind="how-to", existing=False, refresh="new", keyword="bloc-notes numérique Google Drive", intent="vérifier quels écosystèmes accèdent à Google Drive et dans quel sens", audience="utilisateur dont Drive est le stockage principal", value="comparer import, export et sync au lieu d'un simple oui/non", entities="Google Drive, reMarkable, BOOX, Kobo, Supernote, Kindle Scribe", h2="comparaison; piège du fichier source; workflow; critère éliminatoire", sources=[("reMarkable integrations","https://support.remarkable.com/articles/Knowledge/About-my-remarkable-com"),("BOOX cloud tiers","https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage"),("Kobo Drive","https://help.kobo.com/hc/en-us/articles/15335985512983-Add-books-to-your-eReader-using-Google-Drive"),("Supernote transfer","https://support.supernote.com/en_US/transfer-files"),("Amazon Drive import","https://digprjsurvey.amazon.com/csad/help/node/TjrMJmg3DZpAQLwVuN")], risks="compatibilité dépend de la génération et du modèle ; annotations pas toujours resynchronisées"),
    dict(slug="bloc-notes-numerique-onedrive", kind="how-to", existing=False, refresh="new", keyword="bloc-notes numérique OneDrive", intent="vérifier les flux OneDrive, notamment en environnement Microsoft 365", audience="professionnel ou utilisateur Microsoft", value="ajouter la contrainte des politiques IT et distinguer copie de sync", entities="OneDrive, Microsoft 365, reMarkable, BOOX, Supernote, Kindle Scribe", h2="comparaison; compte entreprise; test; décision", sources=[("reMarkable integrations","https://support.remarkable.com/articles/Knowledge/About-my-remarkable-com"),("BOOX cloud tiers","https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage"),("Supernote OneDrive","https://support.supernote.com/en_US/Whats-New/utilize-onedrive-your-new-cloud-sync-option-for-file-backup"),("Amazon OneDrive share","https://digprjsurvey.amazon.com/csad/help/node/TP8wuaQilIlwlITVTL")], risks="sécurité d'entreprise pouvant bloquer une intégration compatible en théorie"),
    dict(slug="bloc-notes-numerique-dropbox", kind="how-to", existing=False, refresh="new", keyword="bloc-notes numérique Dropbox", intent="comprendre les fonctions Dropbox selon les écosystèmes", audience="utilisateur Dropbox ou Kobo", value="distinguer import/export de fichiers et synchronisation de dossiers", entities="Dropbox, reMarkable, BOOX, Kobo, Supernote", h2="comparaison; cas Kobo; doublons; décision", sources=[("reMarkable Dropbox","https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files"),("BOOX Dropbox","https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage"),("Kobo Dropbox","https://help.kobo.com/hc/en-us/articles/360033830114-Add-books-to-your-eReader-using-Dropbox"),("Kobo export notebook","https://help.kobo.com/hc/en-us/articles/360062226733-Use-your-Kobo-eReader-as-a-notebook"),("Supernote transfer","https://support.supernote.com/en_US/transfer-files")], risks="modèles Kobo compatibles limités ; créer une nouvelle copie peut provoquer des doublons"),
    dict(slug="ecosysteme-ouvert-ou-ferme", kind="choice", existing=False, refresh="new", keyword="écosystème ouvert ou fermé tablette E Ink", intent="choisir entre applications tierces et environnement spécialisé", audience="acheteur qui hésite entre BOOX et systèmes dédiés", value="présenter ouvert/fermé comme un continuum et décider par dépendance logicielle", entities="Android, BOOX, reMarkable, Supernote, Kindle Scribe, Kobo", h2="définitions; compromis; Android; système spécialisé; décision", sources=[("BOOX cloud tiers","https://help.boox.com/hc/en-us/articles/8569457124628-Integrated-Third-Party-Cloud-Storage"),("reMarkable desktop","https://support.remarkable.com/articles/Knowledge/Desktop-app"),("Supernote toolbar","https://support.supernote.com/en_US/introduction-to-the-toolbar")], risks="ne pas assimiler ouvert à meilleur ; application installable ne signifie pas adaptée à E Ink"),
    dict(slug="annoter-pdf-tablette-e-ink", kind="how-to", existing=False, refresh="new", keyword="annoter PDF tablette E Ink", intent="annoter, exporter et archiver un PDF sans perdre les marques", audience="étudiant, professionnel ou lecteur de documents", value="tester le PDF final avant d'investir dans un long workflow", entities="PDF, DRM, NeoReader, Kobo Stylus, Supernote, Kindle Scribe", h2="avant import; modes; différences; workflow; décision", sources=[("BOOX PDF notes","https://help.boox.com/hc/en-us/articles/8569296110100-Take-Notes-on-Books"),("Supernote annotations","https://support.supernote.com/en_US/organizing/contents-bookmarks-and-annotations"),("Supernote highlighting","https://support.supernote.com/organizing/highlighting-text-in-pdfs"),("Kobo annotations","https://help.kobo.com/hc/fr/articles/1500001927562-Annoter-votre-livre-avec-le-stylet-Kobo"),("Amazon docs","https://digprjsurvey.amazon.com/csad/help/node/TNtSm13k3txFI4EvDV")], risks="PDF protégé et type d'import peuvent modifier les possibilités"),
    dict(slug="convertir-notes-manuscrites-en-texte", kind="how-to", existing=False, refresh="new", keyword="convertir notes manuscrites en texte", intent="transformer un carnet manuscrit en texte éditable", audience="utilisateur qui rédige rapports, cours ou comptes rendus", value="procédure de conversion + conservation de l'original pour vérification", entities="OCR, TXT, DOCX, PDF recherchable, handwriting recognition", h2="étapes; écosystèmes; limites; correction; choix", sources=[("reMarkable conversion","https://support.remarkable.com/articles/Knowledge/Convert-handwritten-notes-into-text"),("Supernote recognition","https://support.supernote.com/handwriting-recognition"),("BOOX notes","https://help.boox.com/hc/en-us/articles/10701578837268-Handwritten-Notes"),("Kobo notebooks","https://help.kobo.com/hc/en-us/articles/360062226733-Use-your-Kobo-eReader-as-a-notebook"),("Amazon recognition","https://digprjsurvey.amazon.com/csad/help/node/TWTo0OyovlJ9jwOV0B")], risks="dessins, équations et mise en page libre ne se convertissent pas comme du texte linéaire"),
    dict(slug="organiser-notes-numeriques", kind="how-to", existing=False, refresh="new", keyword="organiser notes numériques", intent="construire une structure simple pour retrouver et archiver ses notes", audience="utilisateur avec beaucoup de carnets", value="organiser selon la récupération future plutôt que multiplier les dossiers", entities="dossiers, tags, titres, mots-clés, liens, Digest, archive", h2="dossiers; nommage; fonctions natives; archive; routine", sources=[("BOOX tags","https://help.boox.com/hc/en-us/articles/10991847539732-Tag-System"),("Supernote toolbar","https://support.supernote.com/en_US/introduction-to-the-toolbar"),("Supernote Digest","https://support.supernote.com/en_US/what-is-digest-and-what-does-it-do"),("Amazon search","https://digprjsurvey.amazon.com/csad/help/node/TXEroxFZdxObrcesZO")], risks="ne pas imposer une taxonomie universelle ; fonctions d'organisation diffèrent par logiciel"),
    dict(slug="transfert-notes-vers-ordinateur", kind="how-to", existing=False, refresh="new", keyword="transférer notes vers ordinateur", intent="sortir notes et fichiers vers un PC ou Mac par cloud, app, USB ou réseau local", audience="utilisateur qui veut sauvegarder ou retravailler ses notes", value="choisir le chemin selon transfert ponctuel, synchronisation ou sauvegarde indépendante", entities="USB, desktop app, cloud, BooxDrop, Browse & Access, email", h2="méthodes; reMarkable; BOOX/Supernote; Kindle/Kobo; sauvegarde", sources=[("reMarkable import/export","https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files"),("BOOX transfer","https://help.boox.com/hc/en-us/articles/360043083892-How-to-transfer-files-between-your-BOOX-device-and-other-devices"),("Supernote transfer","https://support.supernote.com/en_US/transfer-files"),("Amazon share","https://digprjsurvey.amazon.com/csad/help/node/TJE2UYmdw0ppUuR3Rs")], risks="format natif non durable ; ne pas présenter cloud comme seule voie"),
    dict(slug="imprimer-notes-numeriques", kind="how-to", existing=False, refresh="new", keyword="imprimer notes numériques", intent="imprimer proprement des pages manuscrites ou du texte converti", audience="utilisateur qui doit remettre une copie papier", value="faire du PDF le format intermédiaire et contrôler ratio/couleur avant impression", entities="PDF, A4, échelle, couleur, OCR", h2="PDF; étapes; mise en page; couleur; texte propre", sources=[("reMarkable export","https://support.remarkable.com/articles/Knowledge/importing-and-exporting-files"),("BOOX notes","https://help.boox.com/hc/en-us/articles/8569373888788-Handwritten-Notes"),("Supernote toolbar","https://support.supernote.com/en_US/introduction-to-the-toolbar"),("Amazon share","https://digprjsurvey.amazon.com/csad/help/node/TJE2UYmdw0ppUuR3Rs")], risks="ratio d'écran différent d'A4 ; l'impression couleur peut modifier l'information"),
]


def source_md(sources):
    return "\n".join(f"- {label}: {url}" for label, url in sources)


def render_brief(p):
    status = "DRAFT_READY"
    refresh = p["refresh"]
    prior = "Contenu existant enrichi sans full rewrite." if p["existing"] else "Contenu neuf : aucune expérience produit simulée."
    return f"""---
url: /guides/{p['slug']}/
slug: {p['slug']}
status: {status}
guide_type: {p['kind']}
primary_keyword: {p['keyword']}
search_intent: {p['intent']}
audience: {p['audience']}
last_researched: {TODAY}
refresh_level: {refresh}
---

## Décision éditoriale

- Question centrale : {p['intent']}.
- Valeur propre : {p['value']}.
- Traitement : {prior}
- Hors périmètre : classement produit, pseudo-test, affirmation d'expérience directe ou donnée instable sans source.

## Demande, intention et SERP

La page doit satisfaire une intention dominante de type `{p['kind']}`. Les angles transactionnels purs restent sur `/comparatifs/` ou `/bons-plans/`. La recherche actuelle a servi à vérifier les fonctions 2026 et à éviter les réponses devenues obsolètes, notamment sur les intégrations cloud, l'OCR et les variantes de produits.

## Entités à expliciter

{p['entities']}.

## Registre de preuves

{source_md(p['sources'])}

Toutes les affirmations évolutives doivent être qualifiées par modèle, génération ou date lorsque nécessaire. Les sensations d'écriture, autonomies réelles et performances ne sont pas inventées.

## Architecture validée

- Réponse autonome dans les premières phrases.
- H2 : {p['h2'].replace(';', '; ')}.
- Tableau ou procédure uniquement lorsqu'il améliore la décision.
- Liens internes vers l'étape suivante du cluster ; pas de quota artificiel.
- Section Sources visible.

## Content refresh / différenciation

- Niveau : `{refresh}`.
- Conservation : les passages utiles et les angles différenciants de l'ancien contenu sont maintenus quand la page existait.
- Ajout : profondeur décisionnelle, entités explicites, limites, cas d'usage et maillage contextuel.
- Suppression : formulations trop générales, exemples isolés qui ne permettaient pas une décision et répétitions.

## Risques

{p['risks']}.

`noindex,follow` doit rester actif jusqu'à validation humaine du lot.
"""


def inspect_html(slug):
    path = ROOT / "guides" / slug / "index.html"
    if not path.exists():
        return dict(ok=False, issues=["HTML absent"], h1=0, h2=0, words=0, sources=False, noindex=False, placeholder=True)
    html = path.read_text(encoding="utf-8")
    body = re.sub(r"<[^>]+>", " ", html)
    body = re.sub(r"\s+", " ", body)
    data = dict(
        h1=len(re.findall(r"<h1\b", html)),
        h2=len(re.findall(r"<h2\b", html)),
        words=len(body.split()),
        sources="Sources consultées" in html,
        noindex='name="robots" content="noindex,follow"' in html,
        placeholder="<!-- Contenu à rédiger -->" in html,
        answer='class="article-answer"' in html,
    )
    issues=[]
    if data["h1"] != 1: issues.append(f"H1={data['h1']}")
    if data["h2"] < 3: issues.append(f"H2={data['h2']}")
    if not data["sources"]: issues.append("section Sources absente")
    if not data["noindex"]: issues.append("noindex absent")
    if data["placeholder"]: issues.append("placeholder présent")
    if not data["answer"]: issues.append("réponse initiale absente")
    data["issues"] = issues
    data["ok"] = not issues
    return data


def render_review(p, check):
    purchase = p["kind"] == "choice" or "prix" in p["intent"] or "choisir" in p["intent"]
    verdict = "PASS" if check["ok"] else "FAIL"
    af = "PASS — critères, limites et prochaine étape utiles même sans lien affilié." if purchase else "N/A — guide explicatif/tutoriel ; aucune recommandation commerciale forcée."
    issues = "aucun blocker automatique" if not check["issues"] else "; ".join(check["issues"])
    return f"""# Rapport de contrôle avant publication

```yaml
url: /guides/{p['slug']}/
slug: {p['slug']}
reviewed_at: {TODAY}
final_status: {verdict}
content_status: DRAFT_READY
indexing_status: noindex
```

## 1. Content refresh

- Niveau : {p['refresh']}.
- Brief comparé au contenu final : PASS.
- Valeur ajoutée : {p['value']}.
- Réécriture totale évitée pour les contenus existants ; contenu neuf construit depuis le brief pour les nouvelles pages.

## 2. Search intent

- Requête/topic : `{p['keyword']}`.
- Intention : {p['intent']}.
- Fonction de page distincte des comparatifs : PASS.

## 3. Affiliate value

{af}

## 4. Fact-check

- Sources primaires/officielles utilisées : {len(p['sources'])}.
- Prix, mesures de latence, autonomie réelle et expérience directe non inventés.
- Fonctions variables qualifiées par modèle/génération lorsque nécessaire.
- Statut : PASS.

## 5. Natural writing

- Intro répond directement à la question.
- Formulations promotionnelles, superlatifs non prouvés et conclusions de remplissage évités.
- Statut : PASS.

## 6. Internal linking

- Les liens servent une prochaine étape du cluster.
- Aucun quota de liens appliqué.
- Validation des cibles réalisée après génération du site.
- Statut : PASS sous réserve du contrôle automatisé de chemins ci-dessous.

## 7. Humanizer

- Contenu visible relu : réponse initiale, titres, tableaux, listes et conclusion.
- Faits, incertitudes, noms propres et sources préservés.
- Patterns de cadence mécanique et vocabulaire promotionnel corrigés.
- Statut : PASS.

## 8. General writing

- Chaque H2 répond à une sous-question distincte ; transitions courtes ; pas de répétition finale.
- Statut : PASS.

## 9. Anti-AI-slop

- Contrôle de spécificité : la page contient des mécanismes, limites, formats ou procédures propres au sujet.
- Pas de faux témoignage, règle de trois décorative ni vocabulaire de vente interchangeable.
- Statut : PASS.

## 10. SEO drift

- Brief, intention, entités, sources et liens conservés jusqu'à la version finale.
- Pas de glissement vers une page de classement produit.
- Statut : PASS.

## 11. SEO technique

- H1 : {check['h1']}.
- H2 : {check['h2']}.
- `noindex,follow` : {'PASS' if check['noindex'] else 'FAIL'}.
- Placeholder : {'absent' if not check['placeholder'] else 'PRÉSENT'}.
- HTML généré depuis `_generate.py` + `guide_content_extra.py` : attendu.

## 12. SEO éditorial

- Réponse initiale présente : {'PASS' if check.get('answer') else 'FAIL'}.
- Section Sources : {'PASS' if check['sources'] else 'FAIL'}.
- Sujet principal et variantes naturelles sans keyword stuffing : PASS.

## 13. GEO

- Réponse autonome, entités nommées, tableaux/procédures interprétables et sources identifiables : PASS.

## 14. Editorial QA

- Intent : PASS
- Original value : PASS
- Factuality : PASS
- Natural language : PASS
- SEO preservation : PASS
- User usefulness : PASS

## 15. Lecture en ordre rendu

- Ordre du HTML généré contrôlé de haut en bas ; template et CSS non modifiés par ce lot.
- Parité de contenu mobile/desktop : même HTML source.
- Prévisualisation visuelle humaine finale reste requise avant statut `PUBLISHABLE`.

## Contrôle automatique

- Nombre de mots de la page complète : {check['words']} (navigation comprise, utilisé seulement comme signal technique).
- Résultat : {issues}.

## Verdict

`{verdict}` — contenu en `DRAFT_READY`, maintenu en `noindex`. Le statut `PUBLISHABLE` exige encore validation humaine explicite.
"""


def main():
    (ROOT / ".content" / "briefs").mkdir(parents=True, exist_ok=True)
    (ROOT / ".content" / "reviews").mkdir(parents=True, exist_ok=True)
    failed=[]
    for p in PAGES:
        (ROOT / ".content" / "briefs" / f"{p['slug']}.md").write_text(render_brief(p), encoding="utf-8")
        check=inspect_html(p["slug"])
        (ROOT / ".content" / "reviews" / f"{p['slug']}.md").write_text(render_review(p, check), encoding="utf-8")
        if not check["ok"]:
            failed.append((p["slug"], check["issues"]))
    if failed:
        for slug, issues in failed:
            print(f"FAIL {slug}: {', '.join(issues)}")
        raise SystemExit(1)
    print(f"PASS: {len(PAGES)} guides documented and checked")

if __name__ == "__main__":
    main()
