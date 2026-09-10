"""Explicit human-approved publication state for editorial clusters.

Only routes listed here may be switched to ``index,follow`` by
``apply_section_indexation.py``. Any new page created later under these
sections remains ``noindex,follow`` until it receives a new explicit human
approval.

Human approval recorded: 2026-09-10.
"""

INDEXABLE_USAGE_ROUTES = {
    "/usages/",
    "/usages/prise-de-notes-professionnelle/",
    "/usages/prise-de-notes-etudiant/",
    "/usages/prise-de-notes-reunion/",
    "/usages/lecture-et-prise-de-notes/",
    "/usages/dessin/",
    "/usages/remplacer-cahiers-papier/",
}

# /usages/annotation-pdf/ is intentionally excluded: it is a consolidated
# redirect/canonical to /guides/annoter-pdf-tablette-e-ink/.

INDEXABLE_GUIDE_ROUTES = {
    "/guides/",
    "/guides/choisir-bloc-notes-numerique/",
    "/guides/liseuse-ou-bloc-notes-numerique/",
    "/guides/tablette-classique-ou-tablette-e-ink/",
    "/guides/taille-ecran-bloc-notes-numerique/",
    "/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/",
    "/guides/bloc-notes-numerique-avec-ou-sans-abonnement/",
    "/guides/prix-bloc-notes-numerique/",
    "/guides/tablette-e-ink/",
    "/guides/encre-electronique-fonctionnement/",
    "/guides/latence-ecriture/",
    "/guides/ocr-manuscrit/",
    "/guides/autonomie-tablette-e-ink/",
    "/guides/formats-fichiers-compatibles/",
    "/guides/exporter-notes/",
    "/guides/synchroniser-notes-cloud/",
    "/guides/bloc-notes-numerique-google-drive/",
    "/guides/bloc-notes-numerique-onedrive/",
    "/guides/bloc-notes-numerique-dropbox/",
    "/guides/ecosysteme-ouvert-ou-ferme/",
    "/guides/annoter-pdf-tablette-e-ink/",
    "/guides/convertir-notes-manuscrites-en-texte/",
    "/guides/organiser-notes-numeriques/",
    "/guides/transfert-notes-vers-ordinateur/",
    "/guides/imprimer-notes-numeriques/",
}

INDEXABLE_DEAL_ROUTES = {
    "/bons-plans/",
    "/bons-plans/bloc-notes-numerique/",
    "/bons-plans/remarkable/",
    "/bons-plans/kindle-scribe/",
    "/bons-plans/kobo-elipsa/",
    "/bons-plans/boox/",
    "/bons-plans/bloc-notes-numerique-occasion/",
    "/bons-plans/black-friday/",
}

INDEXABLE_ROUTES_BY_SCOPE = {
    "usages": INDEXABLE_USAGE_ROUTES,
    "guides": INDEXABLE_GUIDE_ROUTES,
    "deals": INDEXABLE_DEAL_ROUTES,
}

SCOPE_ROOTS = {
    "usages": "usages",
    "guides": "guides",
    "deals": "bons-plans",
}

HUMAN_VALIDATED_AT = "2026-09-10"
EXPLICIT_INDEXATION_APPROVED_AT = "2026-09-10"
