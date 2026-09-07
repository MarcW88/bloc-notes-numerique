#!/usr/bin/env python3
"""Generate all HTML pages for bloc-notes-numerique.fr"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

# ── NAV HTML ──────────────────────────────────────────────────────────────────
NAV = """
<nav class="site-nav" id="site-navigation" aria-label="Navigation principale">
  <div class="nav-item">
    <a href="/comparatifs/" class="nav-link">
      Comparatifs
      <svg class="chevron" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
    </a>
    <div class="dropdown">
      <span class="dropdown-label">Sélections</span>
      <a href="/comparatifs/meilleur-bloc-notes-numerique/">Meilleurs bloc-notes numériques</a>
      <a href="/comparatifs/bloc-notes-numerique-professionnel/">Pour les professionnels</a>
      <a href="/comparatifs/bloc-notes-numerique-etudiant/">Pour les étudiants</a>
      <a href="/comparatifs/bloc-notes-numerique-couleur/">Modèles couleur</a>
      <a href="/comparatifs/bloc-notes-numerique-a4/">Formats A4</a>
      <a href="/comparatifs/bloc-notes-numerique-sans-abonnement/">Sans abonnement</a>
      <a href="/comparatifs/bloc-notes-numerique-pas-cher/">Modèles pas chers</a>
      <div class="dropdown-separator"></div>
      <span class="dropdown-label">Comparer les modèles</span>
      <a href="/comparatifs/kindle-scribe-vs-remarkable/">Kindle Scribe vs reMarkable</a>
      <a href="/comparatifs/kindle-scribe-vs-kobo-elipsa/">Kindle Scribe vs Kobo Elipsa</a>
      <a href="/comparatifs/remarkable-vs-boox/">reMarkable vs Boox</a>
      <a href="/comparatifs/remarkable-vs-supernote/">reMarkable vs Supernote</a>
      <a href="/comparatifs/boox-vs-supernote/">Boox vs Supernote</a>
      <a href="/comparatifs/kobo-elipsa-vs-remarkable/">Kobo Elipsa vs reMarkable</a>
    </div>
  </div>
  <div class="nav-item">
    <a href="/marques/" class="nav-link">
      Marques
      <svg class="chevron" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
    </a>
    <div class="dropdown">
      <a href="/marques/remarkable/">reMarkable</a>
      <a href="/marques/kindle-scribe/">Kindle Scribe</a>
      <a href="/marques/kobo-elipsa/">Kobo Elipsa</a>
      <a href="/marques/boox/">Boox</a>
      <a href="/marques/supernote/">Supernote</a>
    </div>
  </div>
  <div class="nav-item">
    <a href="/usages/" class="nav-link">
      Par usage
      <svg class="chevron" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
    </a>
    <div class="dropdown">
      <a href="/usages/prise-de-notes-professionnelle/">Travail et réunions</a>
      <a href="/usages/prise-de-notes-etudiant/">Études et cours</a>
      <a href="/usages/annotation-pdf/">Annoter des PDF</a>
      <a href="/usages/lecture-et-prise-de-notes/">Lire et prendre des notes</a>
      <a href="/usages/dessin/">Dessiner</a>
      <a href="/usages/remplacer-cahiers-papier/">Remplacer le papier</a>
    </div>
  </div>
  <div class="nav-item">
    <a href="/guides/" class="nav-link">
      Guides
      <svg class="chevron" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
    </a>
    <div class="dropdown">
      <span class="dropdown-label">Bien choisir</span>
      <a href="/guides/choisir-bloc-notes-numerique/">Choisir son bloc-notes numérique</a>
      <a href="/guides/liseuse-ou-bloc-notes-numerique/">Liseuse ou bloc-notes ?</a>
      <a href="/guides/tablette-classique-ou-tablette-e-ink/">Tablette classique ou E Ink ?</a>
      <a href="/guides/prix-bloc-notes-numerique/">Prix et budgets</a>
      <div class="dropdown-separator"></div>
      <span class="dropdown-label">Technologie</span>
      <a href="/guides/tablette-e-ink/">Comprendre l'E Ink</a>
      <a href="/guides/encre-electronique-fonctionnement/">Fonctionnement de l'encre électronique</a>
      <div class="dropdown-separator"></div>
      <span class="dropdown-label">Utilisation</span>
      <a href="/guides/exporter-notes/">Exporter ses notes</a>
      <a href="/guides/annoter-pdf-tablette-e-ink/">Annoter des PDF</a>
      <a href="/guides/synchroniser-notes-cloud/">Synchronisation cloud</a>
    </div>
  </div>
  <div class="nav-item">
    <a href="/bons-plans/" class="nav-link">
      Bons plans
      <svg class="chevron" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
    </a>
    <div class="dropdown">
      <a href="/bons-plans/bloc-notes-numerique/">Tous les bons plans</a>
      <a href="/bons-plans/remarkable/">reMarkable</a>
      <a href="/bons-plans/kindle-scribe/">Kindle Scribe</a>
      <a href="/bons-plans/kobo-elipsa/">Kobo Elipsa</a>
      <a href="/bons-plans/boox/">Boox</a>
      <a href="/bons-plans/bloc-notes-numerique-occasion/">Occasion</a>
      <a href="/bons-plans/black-friday/">Black Friday</a>
    </div>
  </div>
</nav>
"""

HEADER = """
<header class="site-header">
  <div class="header-inner">
    <a href="/" class="site-logo">
      <span class="logo-line1">bloc-notes<span class="logo-pen"></span></span>
      <span class="logo-line2">numériques.fr</span>
    </a>
    {nav}
    <a href="/guides/choisir-bloc-notes-numerique/" class="header-cta">Trouver mon modèle</a>
    <button class="burger" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="site-navigation">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
""".format(nav=NAV)

FOOTER = """
<footer class="site-footer">
  <div class="container">
    <div class="footer-inner">
      <div class="footer-brand">
        <div class="site-logo">
          <span class="logo-line1">bloc-notes</span>
          <span class="logo-line2">numériques.fr</span>
        </div>
        <p class="footer-tagline">Analyses, comparatifs et guides indépendants pour choisir une tablette de prise de notes adaptée à vos usages.</p>
      </div>
      <div class="footer-col">
        <h4>Comparatifs</h4>
        <a href="/comparatifs/meilleur-bloc-notes-numerique/">Meilleurs modèles</a>
        <a href="/comparatifs/bloc-notes-numerique-professionnel/">Professionnels</a>
        <a href="/comparatifs/bloc-notes-numerique-etudiant/">Étudiants</a>
        <a href="/comparatifs/bloc-notes-numerique-sans-abonnement/">Sans abonnement</a>
        <a href="/comparatifs/bloc-notes-numerique-pas-cher/">Pas chers</a>
      </div>
      <div class="footer-col">
        <h4>Marques</h4>
        <a href="/marques/remarkable/">reMarkable</a>
        <a href="/marques/kindle-scribe/">Kindle Scribe</a>
        <a href="/marques/kobo-elipsa/">Kobo Elipsa</a>
        <a href="/marques/boox/">Boox</a>
        <a href="/marques/supernote/">Supernote</a>
        <a href="/accessoires/">Accessoires</a>
      </div>
      <div class="footer-col">
        <h4>Le site</h4>
        <a href="/methode-de-test/">Méthode de test</a>
        <a href="/comment-nous-comparons/">Comment nous comparons</a>
        <a href="/a-propos/">À propos</a>
        <a href="/contact/">Contact</a>
        <a href="/transparence-affiliation/">Transparence affiliation</a>
        <a href="/mentions-legales/">Mentions légales</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 bloc-notes numériques.fr — Tous droits réservés</span>
      <span>Ce site contient des liens affiliés. <a href="/transparence-affiliation/">En savoir plus.</a></span>
    </div>
  </div>
</footer>
"""

def html_page(title, description, breadcrumb_html, content_html, canonical="/"):
    depth = canonical.count("/") - 1
    css_path = ("../" * depth) + "style.css" if depth > 0 else "style.css"
    js_path = ("../" * depth) + "site.js" if depth > 0 else "site.js"
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="noindex,follow">
  <link rel="canonical" href="https://bloc-notes-numeriques.fr{canonical}">
  <link rel="stylesheet" href="{css_path}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
</head>
<body>
{HEADER}
<main>
{breadcrumb_html}
{content_html}
</main>
{FOOTER}
<script src="{js_path}" defer></script>
</body>
</html>"""

def breadcrumb(*items):
    """items = list of (label, url) or just label for last"""
    parts = []
    for i, item in enumerate(items):
        if isinstance(item, tuple):
            parts.append(f'<a href="{item[1]}">{item[0]}</a>')
        else:
            parts.append(f'<span>{item}</span>')
        if i < len(items) - 1:
            parts.append('<span class="sep">/</span>')
    return f'<div class="container"><div class="page-breadcrumb"><a href="/">Accueil</a><span class="sep">/</span>{" ".join(parts)}</div></div>'

def hub_page(title, desc, canonical, crumbs, intro, links):
    links_html = "\n".join(
        f'<a href="{url}" class="hub-link"><span>{label}</span><span class="hub-link-arrow">→</span></a>'
        for label, url in links
    )
    content = f"""
<section class="page-hero">
  <div class="container">
    <h1>{title}</h1>
    <p class="lead">{intro}</p>
    <div class="page-meta">
      <span class="update-tag">Mis à jour régulièrement</span>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="hub-grid">
      {links_html}
    </div>
  </div>
</section>
"""
    return html_page(title, desc, crumbs, content, canonical)

def content_page(title, desc, canonical, crumbs, page_type=""):
    type_badge = f'<span class="content-type type-{page_type.lower()}">{page_type}</span>' if page_type else ""
    content = f"""
<section class="page-hero">
  <div class="container">
    {type_badge}
    <h1>{title}</h1>
    <p class="lead">{desc}</p>
    <div class="page-meta">
      <span class="update-tag">Mis à jour régulièrement</span>
      <span class="page-meta-item">Contenu en préparation</span>
    </div>
  </div>
</section>
<div class="container">
  <div class="content-layout">
    <article class="content-main">
      <!-- Contenu à rédiger -->
    </article>
    <aside class="content-sidebar">
      <div class="sidebar-box sidebar-toc">
        <h4>Sommaire</h4>
        <!-- Sommaire généré dynamiquement -->
      </div>
      <div class="sidebar-box">
        <h4>Affiliation</h4>
        <p class="affiliation-note">Ce site contient des liens affiliés. Nos recommandations restent indépendantes. <a href="/transparence-affiliation/">En savoir plus.</a></p>
      </div>
      <a href="/guides/choisir-bloc-notes-numerique/" class="btn btn-primary" style="width:100%;justify-content:center;">Trouver mon modèle</a>
    </aside>
  </div>
</div>
"""
    return html_page(title, desc, crumbs, content, canonical)

def test_page(title, desc, canonical, crumbs, product_name, score="—"):
    content = f"""
<section class="page-hero">
  <div class="container">
    <span class="content-type type-test">Analyse produit</span>
    <h1>{title}</h1>
    <p class="lead">{desc}</p>
    <div class="page-meta">
      <span class="update-tag">Analyse en préparation</span>
    </div>
  </div>
</section>
<div class="container">
  <div class="content-layout">
    <article class="content-main">
      <div class="product-summary">
        <div class="product-summary-header">Résumé — {product_name}</div>
        <div class="product-summary-body">
          <div class="summary-row"><span class="summary-label">Idéal pour</span><span class="summary-val">À compléter</span></div>
          <div class="summary-row"><span class="summary-label">À éviter si</span><span class="summary-val">À compléter</span></div>
          <div class="summary-row"><span class="summary-label">Principal avantage</span><span class="summary-val">À compléter</span></div>
          <div class="summary-row"><span class="summary-label">Principale limite</span><span class="summary-val">À compléter</span></div>
          <div class="summary-row"><span class="summary-label">Prix constaté</span><span class="summary-val">— €</span></div>
        </div>
      </div>
      <p class="draft-notice">Cette page est en préparation. Aucun verdict ni lien marchand ne sera publié avant vérification des informations.</p>
      <!-- Contenu du test à rédiger -->
    </article>
    <aside class="content-sidebar">
      <div class="sidebar-box">
        <h4>Note globale</h4>
        <div class="score-display">
          <span class="score-num">{score}</span>
          <span class="score-max">/10</span>
        </div>
        <div class="score-bars">
          <div class="score-bar-item">
            <span class="score-bar-label"><span>Écriture</span><span>—</span></span>
            <div class="score-bar-track"><div class="score-bar-fill" style="width:0%"></div></div>
          </div>
          <div class="score-bar-item">
            <span class="score-bar-label"><span>Écran</span><span>—</span></span>
            <div class="score-bar-track"><div class="score-bar-fill" style="width:0%"></div></div>
          </div>
          <div class="score-bar-item">
            <span class="score-bar-label"><span>Autonomie</span><span>—</span></span>
            <div class="score-bar-track"><div class="score-bar-fill" style="width:0%"></div></div>
          </div>
          <div class="score-bar-item">
            <span class="score-bar-label"><span>Logiciel &amp; export</span><span>—</span></span>
            <div class="score-bar-track"><div class="score-bar-fill" style="width:0%"></div></div>
          </div>
          <div class="score-bar-item">
            <span class="score-bar-label"><span>Rapport qualité-prix</span><span>—</span></span>
            <div class="score-bar-track"><div class="score-bar-fill" style="width:0%"></div></div>
          </div>
        </div>
      </div>
      <div class="sidebar-box sidebar-toc">
        <h4>Sommaire</h4>
      </div>
      <div class="sidebar-box">
        <h4>Affiliation</h4>
        <p class="affiliation-note">Ce site contient des liens affiliés. <a href="/transparence-affiliation/">En savoir plus.</a></p>
      </div>
    </aside>
  </div>
</div>
"""
    return html_page(title, desc, crumbs, content, canonical)

def write(path, content):
    full = os.path.join(BASE, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {path}")

# ── HOMEPAGE ─────────────────────────────────────────────────────────────────
homepage = html_page(
    "Bloc-notes numériques — Comparatifs, analyses et guides",
    "Trouvez le bloc-notes numérique adapté à votre usage grâce à des comparatifs, analyses documentées et guides sur reMarkable, Kindle Scribe, Boox, Kobo Elipsa et Supernote.",
    "",
    """
<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-content">
        <span class="hero-tag">Comparatifs &amp; guides indépendants</span>
        <h1 class="hero-title">Le bon bloc-notes numérique,<br>selon votre manière de travailler.</h1>
        <p class="lead hero-desc">Comparatifs, analyses documentées et guides pour choisir une tablette de prise de notes réellement adaptée à vos usages.</p>
        <div class="hero-actions">
          <a href="/comparatifs/meilleur-bloc-notes-numerique/" class="btn btn-primary btn-lg">Comparer les meilleurs modèles</a>
          <a href="/guides/choisir-bloc-notes-numerique/" class="btn btn-secondary btn-lg">Trouver mon bloc-notes numérique</a>
        </div>
      </div>
      <div class="hero-visual">
        <div class="paper-study" aria-hidden="true"><span></span><span></span><span></span></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Par usage</p>
      <h2>Quel est votre besoin principal ?</h2>
      <p>Chaque usage a ses exigences. Trouvez le modèle adapté à votre situation.</p>
    </div>
    <div class="usage-grid">
      <a href="/usages/prise-de-notes-professionnelle/" class="usage-card">
        <div class="usage-icon"><svg viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></div>
        <h3>Pour le travail</h3>
        <p>Réunions, annotations, organisation de projets.</p>
      </a>
      <a href="/usages/prise-de-notes-etudiant/" class="usage-card">
        <div class="usage-icon"><svg viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></div>
        <h3>Pour les études</h3>
        <p>Cours, révisions, prise de notes manuscrite.</p>
      </a>
      <a href="/usages/annotation-pdf/" class="usage-card">
        <div class="usage-icon"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg></div>
        <h3>Annoter des PDF</h3>
        <p>Documents, articles, contrats, livres numériques.</p>
      </a>
      <a href="/usages/lecture-et-prise-de-notes/" class="usage-card">
        <div class="usage-icon"><svg viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg></div>
        <h3>Lire et prendre des notes</h3>
        <p>Lecture longue, résumés, fiches de lecture.</p>
      </a>
      <a href="/usages/dessin/" class="usage-card">
        <div class="usage-icon"><svg viewBox="0 0 24 24"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/><path d="M2 2l7.586 7.586"/><circle cx="11" cy="11" r="2"/></svg></div>
        <h3>Dessiner</h3>
        <p>Croquis, schémas, mind maps, créativité.</p>
      </a>
      <a href="/usages/remplacer-cahiers-papier/" class="usage-card">
        <div class="usage-icon"><svg viewBox="0 0 24 24"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg></div>
        <h3>Remplacer le papier</h3>
        <p>Zéro papier, organisation numérique, durabilité.</p>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Comparatif</p>
      <h2>Cinq modèles à comparer</h2>
      <p>Une grille de comparaison commune, complétée au fur et à mesure de nos vérifications.</p>
    </div>
    <div class="table-wrapper">
      <table class="comp-table">
        <thead>
          <tr>
            <th>Modèle</th>
            <th>Idéal pour</th>
            <th>Écran</th>
            <th>Couleur</th>
            <th>Abonnement</th>
            <th>Prix</th>
            <th>Verdict</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>reMarkable Paper Pro</strong></td>
            <td>Écriture, annotation</td>
            <td>11,8″ E Ink</td>
            <td><span class="badge badge-primary">Couleur</span></td>
            <td>Optionnel</td>
            <td>— €</td>
            <td>Positionnement à vérifier</td>
          </tr>
          <tr>
            <td><strong>Kindle Scribe</strong></td>
            <td>Lecture &amp; notes</td>
            <td>10,2″ E Ink</td>
            <td><span class="badge badge-neutral">N&amp;B</span></td>
            <td>Non</td>
            <td>— €</td>
            <td>Positionnement à vérifier</td>
          </tr>
          <tr>
            <td><strong>Boox Note Air 4</strong></td>
            <td>Android ouvert</td>
            <td>10,3″ E Ink</td>
            <td><span class="badge badge-primary">Couleur</span></td>
            <td>Non</td>
            <td>— €</td>
            <td>Positionnement à vérifier</td>
          </tr>
          <tr>
            <td><strong>Kobo Elipsa 2E</strong></td>
            <td>Lecture enrichie</td>
            <td>10,3″ E Ink</td>
            <td><span class="badge badge-neutral">N&amp;B</span></td>
            <td>Non</td>
            <td>— €</td>
            <td>Positionnement à vérifier</td>
          </tr>
          <tr>
            <td><strong>Supernote A5X2</strong></td>
            <td>Écriture précise</td>
            <td>10,2″ E Ink</td>
            <td><span class="badge badge-neutral">N&amp;B</span></td>
            <td>Non</td>
            <td>— €</td>
            <td>Positionnement à vérifier</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="text-align:center;margin-top:24px;">
      <a href="/comparatifs/meilleur-bloc-notes-numerique/" class="btn btn-secondary">Voir le comparatif complet</a>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Profils d’usage</p>
      <h2>Les positionnements à documenter</h2>
    </div>
    <div class="reco-grid">
      <div class="reco-card">
        <div class="reco-card-badge">Écriture et couleur</div>
        <div class="reco-card-img" aria-hidden="true"><span class="product-silhouette"></span></div>
        <div class="reco-card-body">
          <h3>reMarkable Paper Pro</h3>
          <div class="reco-meta">
            <div class="reco-pro">Sensation d'écriture inégalée</div>
            <div class="reco-con">Écosystème fermé</div>
          </div>
          <div class="reco-price">— €</div>
          <div class="reco-actions">
            <a href="/marques/remarkable/remarkable-paper-pro-avis/" class="btn btn-ghost">Lire l’analyse</a>
            <span class="btn btn-accent btn-disabled" aria-disabled="true">Prix à venir</span>
          </div>
        </div>
      </div>
      <div class="reco-card">
        <div class="reco-card-badge accent">Environnement ouvert</div>
        <div class="reco-card-img" aria-hidden="true"><span class="product-silhouette product-silhouette--wide"></span></div>
        <div class="reco-card-body">
          <h3>Boox Tab Ultra C Pro</h3>
          <div class="reco-meta">
            <div class="reco-pro">Android ouvert, apps tierces</div>
            <div class="reco-con">Interface plus complexe</div>
          </div>
          <div class="reco-price">— €</div>
          <div class="reco-actions">
            <a href="/marques/boox/avis/" class="btn btn-ghost">Lire l’analyse</a>
            <span class="btn btn-accent btn-disabled" aria-disabled="true">Prix à venir</span>
          </div>
        </div>
      </div>
      <div class="reco-card">
        <div class="reco-card-badge neutral">Lecture et annotation</div>
        <div class="reco-card-img" aria-hidden="true"><span class="product-silhouette product-silhouette--compact"></span></div>
        <div class="reco-card-body">
          <h3>Kindle Scribe</h3>
          <div class="reco-meta">
            <div class="reco-pro">Prix accessible, écosystème Amazon</div>
            <div class="reco-con">Fonctions notes limitées</div>
          </div>
          <div class="reco-price">— €</div>
          <div class="reco-actions">
            <a href="/marques/kindle-scribe/" class="btn btn-ghost">Lire l’analyse</a>
            <span class="btn btn-accent btn-disabled" aria-disabled="true">Prix à venir</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Comparaisons populaires</p>
      <h2>Hésitez-vous entre deux modèles ?</h2>
      <p>Ces pages vous aident à trancher selon votre usage précis.</p>
    </div>
    <div class="vs-grid">
      <a href="/comparatifs/kindle-scribe-vs-remarkable/" class="vs-row">
        <div class="vs-brand">Kindle Scribe</div>
        <div class="vs-sep">VS</div>
        <div class="vs-brand vs-brand-right">reMarkable</div>
      </a>
      <a href="/comparatifs/remarkable-vs-boox/" class="vs-row">
        <div class="vs-brand">reMarkable</div>
        <div class="vs-sep">VS</div>
        <div class="vs-brand vs-brand-right">Boox</div>
      </a>
      <a href="/comparatifs/kobo-elipsa-vs-remarkable/" class="vs-row">
        <div class="vs-brand">Kobo Elipsa</div>
        <div class="vs-sep">VS</div>
        <div class="vs-brand vs-brand-right">reMarkable</div>
      </a>
    </div>
    <div style="text-align:center;margin-top:24px;">
      <a href="/comparatifs/" class="btn btn-ghost">Toutes les comparaisons</a>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Derniers contenus</p>
      <h2>Tests et guides récents</h2>
    </div>
    <div class="content-grid">
      <a href="/marques/remarkable/remarkable-paper-pro-avis/" class="content-card">
        <div class="content-card-img"></div>
        <div class="content-card-body">
          <span class="content-type type-test">Analyse</span>
          <h3>reMarkable Paper Pro — Avis complet</h3>
          <p>Analyse détaillée de l'expérience d'écriture, de l'écran et de l'écosystème.</p>
          <span class="content-date">Contenu en préparation</span>
        </div>
      </a>
      <a href="/comparatifs/meilleur-bloc-notes-numerique/" class="content-card">
        <div class="content-card-img"></div>
        <div class="content-card-body">
          <span class="content-type type-comparatif">Comparatif</span>
          <h3>Quel bloc-notes numérique choisir ?</h3>
          <p>Notre sélection des meilleures tablettes de prise de notes.</p>
          <span class="content-date">Contenu en préparation</span>
        </div>
      </a>
      <a href="/guides/choisir-bloc-notes-numerique/" class="content-card">
        <div class="content-card-img"></div>
        <div class="content-card-body">
          <span class="content-type type-guide">Guide</span>
          <h3>Comment choisir son bloc-notes numérique ?</h3>
          <p>Tous les critères à connaître avant d'acheter.</p>
          <span class="content-date">Contenu en préparation</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="section-heading" style="max-width:600px;margin-left:auto;margin-right:auto;text-align:center;">
      <p class="eyebrow">Méthodologie</p>
      <h2>Comment évaluons-nous les bloc-notes numériques ?</h2>
      <p>Chaque recommandation devra indiquer clairement son niveau de preuve et les informations effectivement vérifiées.</p>
    </div>
    <div class="method-grid">
      <div class="method-card">
        <div class="method-num">01</div>
        <h4>Qualité d'écriture</h4>
        <p>Latence, sensation du stylet, précision, comportement en écriture rapide.</p>
      </div>
      <div class="method-card">
        <div class="method-num">02</div>
        <h4>Organisation &amp; export</h4>
        <p>Structure des notes, formats d'export, OCR, synchronisation cloud.</p>
      </div>
      <div class="method-card">
        <div class="method-num">03</div>
        <h4>Confort de lecture</h4>
        <p>Qualité de l'écran E Ink, éclairage, lisibilité des PDF, fatigue oculaire.</p>
      </div>
      <div class="method-card">
        <div class="method-num">04</div>
        <h4>Coût réel</h4>
        <p>Prix d'achat, abonnements, accessoires nécessaires, durée de vie estimée.</p>
      </div>
    </div>
    <div style="text-align:center;">
      <a href="/methode-de-test/" class="btn btn-secondary">Lire notre méthodologie complète</a>
    </div>
    <div style="text-align:center;margin-top:24px;">
      <span class="handnote">Notre avis : le meilleur écran n'implique pas nécessairement le meilleur outil de prise de notes.</span>
    </div>
  </div>
</section>
""",
    "/"
)

write("/index.html", homepage)

# ── COMPARATIFS ───────────────────────────────────────────────────────────────
write("/comparatifs/index.html", hub_page(
    "Comparatifs de bloc-notes numériques",
    "Tous nos comparatifs de tablettes E Ink et bloc-notes numériques. Trouvez le meilleur modèle selon votre usage et votre budget.",
    "/comparatifs/",
    breadcrumb("Comparatifs"),
    "Nos comparatifs indépendants pour vous aider à choisir le bloc-notes numérique adapté à votre situation.",
    [
        ("Meilleurs bloc-notes numériques", "/comparatifs/meilleur-bloc-notes-numerique/"),
        ("Pour les professionnels", "/comparatifs/bloc-notes-numerique-professionnel/"),
        ("Pour les étudiants", "/comparatifs/bloc-notes-numerique-etudiant/"),
        ("Modèles couleur", "/comparatifs/bloc-notes-numerique-couleur/"),
        ("Formats A4", "/comparatifs/bloc-notes-numerique-a4/"),
        ("Sans abonnement", "/comparatifs/bloc-notes-numerique-sans-abonnement/"),
        ("Modèles pas chers", "/comparatifs/bloc-notes-numerique-pas-cher/"),
        ("Kindle Scribe vs reMarkable", "/comparatifs/kindle-scribe-vs-remarkable/"),
        ("Kindle Scribe vs Kobo Elipsa", "/comparatifs/kindle-scribe-vs-kobo-elipsa/"),
        ("reMarkable vs Boox", "/comparatifs/remarkable-vs-boox/"),
        ("reMarkable vs Supernote", "/comparatifs/remarkable-vs-supernote/"),
        ("Boox vs Supernote", "/comparatifs/boox-vs-supernote/"),
        ("Kobo Elipsa vs reMarkable", "/comparatifs/kobo-elipsa-vs-remarkable/"),
    ]
))

COMPARATIFS = [
    ("/comparatifs/meilleur-bloc-notes-numerique/", "Meilleur bloc-notes numérique — Comparatif & sélection", "Quel bloc-notes numérique choisir ? Notre grille comparative des tablettes E Ink pour la prise de notes.", "comparatif"),
    ("/comparatifs/tablette-e-ink/", "Meilleure tablette E Ink — Comparatif", "Comparaison des principales tablettes E Ink pour comprendre leurs usages et leurs limites.", "comparatif"),
    ("/comparatifs/bloc-notes-numerique-professionnel/", "Meilleur bloc-notes numérique pour les professionnels", "Quel bloc-notes numérique choisir pour une utilisation professionnelle ? Notre sélection pour le travail.", "comparatif"),
    ("/comparatifs/bloc-notes-numerique-etudiant/", "Meilleur bloc-notes numérique pour les étudiants", "Quel bloc-notes numérique choisir pour les études ? Notre comparatif pour les étudiants.", "comparatif"),
    ("/comparatifs/bloc-notes-numerique-couleur/", "Meilleur bloc-notes numérique couleur", "Comparatif des bloc-notes numériques avec écran couleur E Ink.", "comparatif"),
    ("/comparatifs/bloc-notes-numerique-a4/", "Meilleur bloc-notes numérique A4", "Sélection des tablettes de prise de notes au format A4.", "comparatif"),
    ("/comparatifs/bloc-notes-numerique-sans-abonnement/", "Meilleur bloc-notes numérique sans abonnement", "Bloc-notes numériques fonctionnels sans abonnement mensuel.", "comparatif"),
    ("/comparatifs/bloc-notes-numerique-pas-cher/", "Meilleur bloc-notes numérique pas cher", "Les meilleures tablettes E Ink à petit prix pour la prise de notes.", "comparatif"),
    ("/comparatifs/kindle-scribe-vs-remarkable/", "Kindle Scribe vs reMarkable — Lequel choisir ?", "Comparaison détaillée entre le Kindle Scribe et le reMarkable. Quelle tablette convient le mieux à votre usage ?", "comparatif"),
    ("/comparatifs/kindle-scribe-vs-kobo-elipsa/", "Kindle Scribe vs Kobo Elipsa — Comparatif", "Kindle Scribe ou Kobo Elipsa ? Notre analyse comparative pour vous aider à choisir.", "comparatif"),
    ("/comparatifs/remarkable-vs-boox/", "reMarkable vs Boox — Comparatif complet", "reMarkable ou Boox ? Deux philosophies différentes : écosystème fermé vs Android ouvert.", "comparatif"),
    ("/comparatifs/remarkable-vs-supernote/", "reMarkable vs Supernote — Comparatif", "reMarkable ou Supernote ? Deux appareils dédiés à l'écriture avec des approches distinctes.", "comparatif"),
    ("/comparatifs/boox-vs-supernote/", "Boox vs Supernote — Lequel choisir ?", "Boox ou Supernote : notre comparatif pour les amateurs de prise de notes précise.", "comparatif"),
    ("/comparatifs/kobo-elipsa-vs-remarkable/", "Kobo Elipsa vs reMarkable — Comparatif", "Kobo Elipsa ou reMarkable ? Lecture et annotation vs écriture pure.", "comparatif"),
]

for path, title, desc, ptype in COMPARATIFS:
    crumbs = breadcrumb(("Comparatifs", "/comparatifs/"), title.split("—")[0].strip())
    write(path + "index.html", content_page(title, desc, path, crumbs, "Comparatif"))

# ── MARQUES ───────────────────────────────────────────────────────────────────
write("/marques/index.html", hub_page(
    "Marques de bloc-notes numériques",
    "Découvrez tous nos tests, comparatifs et guides par marque : reMarkable, Kindle Scribe, Boox, Kobo Elipsa et Supernote.",
    "/marques/",
    breadcrumb("Marques"),
    "Tout ce que vous devez savoir sur chaque marque : tests, modèles, accessoires et écosystème.",
    [
        ("reMarkable", "/marques/remarkable/"),
        ("Kindle Scribe", "/marques/kindle-scribe/"),
        ("Kobo Elipsa", "/marques/kobo-elipsa/"),
        ("Boox", "/marques/boox/"),
        ("Supernote", "/marques/supernote/"),
    ]
))

# reMarkable hub
write("/marques/remarkable/index.html", hub_page(
    "reMarkable — Tests, comparatifs et guides",
    "Tout sur reMarkable : Paper Pro, reMarkable 2, abonnement Connect, accessoires et alternatives.",
    "/marques/remarkable/",
    breadcrumb(("Marques", "/marques/"), "reMarkable"),
    "Le hub reMarkable : modèles disponibles, tests, comparatifs, accessoires compatibles et questions fréquentes.",
    [
        ("reMarkable Paper Pro", "/marques/remarkable/remarkable-paper-pro/"),
        ("reMarkable 2", "/marques/remarkable/remarkable-2/"),
        ("Avis reMarkable 2", "/marques/remarkable/remarkable-2-avis/"),
        ("Avis reMarkable Paper Pro", "/marques/remarkable/remarkable-paper-pro-avis/"),
        ("Abonnement Connect", "/marques/remarkable/abonnement-connect/"),
        ("Accessoires reMarkable", "/marques/remarkable/accessoires/"),
        ("Alternatives à reMarkable", "/marques/remarkable/alternatives/"),
    ]
))

REMARKABLE_PAGES = [
    ("/marques/remarkable/remarkable-paper-pro/", "reMarkable Paper Pro — Fiche technique et présentation", "Découvrez le reMarkable Paper Pro : caractéristiques, fonctionnalités et pour qui c'est fait."),
    ("/marques/remarkable/remarkable-2/", "reMarkable 2 — Fiche technique et présentation", "Le reMarkable 2 : caractéristiques, fonctionnalités et comparaison avec le Paper Pro."),
    ("/marques/remarkable/remarkable-2-avis/", "reMarkable 2 — Avis et analyse complète", "Analyse détaillée du reMarkable 2 : écriture, écran, logiciel et limites."),
    ("/marques/remarkable/remarkable-paper-pro-avis/", "reMarkable Paper Pro — Avis et analyse complète", "Analyse du reMarkable Paper Pro : écriture, écran couleur, logiciel et limites."),
    ("/marques/remarkable/abonnement-connect/", "Abonnement reMarkable Connect — Vaut-il le coup ?", "Faut-il souscrire à l'abonnement Connect de reMarkable ? Notre analyse détaillée."),
    ("/marques/remarkable/accessoires/", "Accessoires reMarkable — Stylets, housses et étuis", "Les meilleurs accessoires compatibles avec reMarkable 2 et Paper Pro."),
    ("/marques/remarkable/alternatives/", "Alternatives à reMarkable — Que choisir à la place ?", "Les meilleures alternatives au reMarkable : Boox, Supernote, Kindle Scribe et Kobo Elipsa."),
]

for path, title, desc in REMARKABLE_PAGES:
    crumbs = breadcrumb(("Marques", "/marques/"), ("reMarkable", "/marques/remarkable/"), title.split("—")[0].strip())
    is_test = "avis" in path.lower()
    if is_test:
        product = "reMarkable Paper Pro" if "paper-pro" in path else "reMarkable 2"
        write(path + "index.html", test_page(title, desc, path, crumbs, product))
    else:
        write(path + "index.html", content_page(title, desc, path, crumbs))

# Boox hub
write("/marques/boox/index.html", hub_page(
    "Boox — Tests, comparatifs et guides",
    "Tout sur Boox : Note Air, Tab Ultra, avis, accessoires et alternatives.",
    "/marques/boox/",
    breadcrumb(("Marques", "/marques/"), "Boox"),
    "Le hub Boox : modèles disponibles, tests, comparatifs et accessoires pour tablettes E Ink sous Android.",
    [
        ("Boox Note Air", "/marques/boox/boox-note-air/"),
        ("Boox Tab Ultra", "/marques/boox/boox-tab-ultra/"),
        ("Avis Boox", "/marques/boox/avis/"),
        ("Accessoires Boox", "/marques/boox/accessoires/"),
        ("Alternatives à Boox", "/marques/boox/alternatives/"),
    ]
))

BOOX_PAGES = [
    ("/marques/boox/boox-note-air/", "Boox Note Air — Fiche technique et présentation", "Tout sur le Boox Note Air : caractéristiques, fonctionnalités et avis."),
    ("/marques/boox/boox-tab-ultra/", "Boox Tab Ultra — Fiche technique et présentation", "Le Boox Tab Ultra : la tablette E Ink Android la plus complète du marché."),
    ("/marques/boox/avis/", "Boox — Avis et analyses", "Analyses des tablettes Boox : Note Air, Tab Ultra et comparaisons."),
    ("/marques/boox/accessoires/", "Accessoires Boox — Stylets et housses compatibles", "Les meilleurs accessoires pour vos tablettes Boox."),
    ("/marques/boox/alternatives/", "Alternatives à Boox — Que choisir à la place ?", "Les meilleures alternatives à Boox selon votre usage et votre budget."),
]

for path, title, desc in BOOX_PAGES:
    crumbs = breadcrumb(("Marques", "/marques/"), ("Boox", "/marques/boox/"), title.split("—")[0].strip())
    write(path + "index.html", content_page(title, desc, path, crumbs))

# Simple brand pages
BRAND_SIMPLE = [
    ("/marques/kindle-scribe/", "Kindle Scribe — Tests, avis et comparatifs", "Tout sur le Kindle Scribe : avis, comparatifs et guides d'achat.", "Kindle Scribe"),
    ("/marques/kobo-elipsa/", "Kobo Elipsa — Tests, avis et comparatifs", "Tout sur le Kobo Elipsa : avis, comparatifs et guides d'achat.", "Kobo Elipsa"),
    ("/marques/supernote/", "Supernote — Tests, avis et comparatifs", "Tout sur Supernote : avis, comparatifs et guides d'achat.", "Supernote"),
]

for path, title, desc, brand in BRAND_SIMPLE:
    crumbs = breadcrumb(("Marques", "/marques/"), brand)
    related = {
        "Kindle Scribe": [
            ("Kindle Scribe vs reMarkable", "/comparatifs/kindle-scribe-vs-remarkable/"),
            ("Kindle Scribe vs Kobo Elipsa", "/comparatifs/kindle-scribe-vs-kobo-elipsa/"),
            ("Liseuse ou bloc-notes numérique ?", "/guides/liseuse-ou-bloc-notes-numerique/"),
        ],
        "Kobo Elipsa": [
            ("Kobo Elipsa vs reMarkable", "/comparatifs/kobo-elipsa-vs-remarkable/"),
            ("Kindle Scribe vs Kobo Elipsa", "/comparatifs/kindle-scribe-vs-kobo-elipsa/"),
            ("Lire et prendre des notes", "/usages/lecture-et-prise-de-notes/"),
        ],
        "Supernote": [
            ("reMarkable vs Supernote", "/comparatifs/remarkable-vs-supernote/"),
            ("Boox vs Supernote", "/comparatifs/boox-vs-supernote/"),
            ("Prendre des notes au travail", "/usages/prise-de-notes-professionnelle/"),
        ],
    }
    write(path + "index.html", hub_page(
        title, desc, path, crumbs,
        f"Le hub {brand} : tout ce que vous devez savoir avant d'acheter.",
        related[brand]
    ))

# ── USAGES ────────────────────────────────────────────────────────────────────
write("/usages/index.html", hub_page(
    "Bloc-notes numérique par usage — Guides et recommandations",
    "Trouvez le meilleur bloc-notes numérique selon votre usage : travail, études, annotation PDF, dessin.",
    "/usages/",
    breadcrumb("Par usage"),
    "Chaque usage a ses exigences. Nos recommandations ciblées pour vous aider à faire le bon choix.",
    [
        ("Travail et réunions", "/usages/prise-de-notes-professionnelle/"),
        ("Études et cours", "/usages/prise-de-notes-etudiant/"),
        ("Prise de notes en réunion", "/usages/prise-de-notes-reunion/"),
        ("Annoter des PDF", "/usages/annotation-pdf/"),
        ("Lire et prendre des notes", "/usages/lecture-et-prise-de-notes/"),
        ("Dessiner", "/usages/dessin/"),
        ("Remplacer les cahiers papier", "/usages/remplacer-cahiers-papier/"),
    ]
))

USAGES = [
    ("/usages/prise-de-notes-professionnelle/", "Bloc-notes numérique pour le travail et les réunions", "Quel bloc-notes numérique choisir pour une utilisation professionnelle ? Notre guide et nos recommandations."),
    ("/usages/prise-de-notes-etudiant/", "Bloc-notes numérique pour les étudiants", "Quel bloc-notes numérique est le mieux adapté aux études ? Notre guide complet pour les étudiants."),
    ("/usages/prise-de-notes-reunion/", "Prendre des notes en réunion avec un bloc-notes numérique", "Quel appareil choisir pour optimiser votre prise de notes en réunion ?"),
    ("/usages/annotation-pdf/", "Annoter des PDF avec un bloc-notes numérique", "Les meilleures tablettes E Ink pour annoter, surligner et commenter des PDF."),
    ("/usages/lecture-et-prise-de-notes/", "Lire et prendre des notes avec une tablette E Ink", "Quelle tablette permet de lire et annoter efficacement ?"),
    ("/usages/dessin/", "Dessiner avec un bloc-notes numérique", "Croquis, schémas et créativité : les meilleures tablettes E Ink pour dessiner."),
    ("/usages/remplacer-cahiers-papier/", "Remplacer ses cahiers papier par un bloc-notes numérique", "Comment passer au zéro papier ? Notre guide pour choisir le bon outil."),
]

for path, title, desc in USAGES:
    crumbs = breadcrumb(("Par usage", "/usages/"), title)
    write(path + "index.html", content_page(title, desc, path, crumbs, "Guide"))

# ── GUIDES ────────────────────────────────────────────────────────────────────
write("/guides/index.html", hub_page(
    "Guides — Choisir et utiliser un bloc-notes numérique",
    "Tous nos guides pour choisir, configurer et utiliser un bloc-notes numérique. Technologie E Ink, formats, export, synchronisation.",
    "/guides/",
    breadcrumb("Guides"),
    "Nos guides pratiques pour comprendre la technologie E Ink et faire le meilleur choix.",
    [
        ("Choisir son bloc-notes numérique", "/guides/choisir-bloc-notes-numerique/"),
        ("Liseuse ou bloc-notes numérique ?", "/guides/liseuse-ou-bloc-notes-numerique/"),
        ("Tablette classique ou E Ink ?", "/guides/tablette-classique-ou-tablette-e-ink/"),
        ("Taille d'écran", "/guides/taille-ecran-bloc-notes-numerique/"),
        ("Couleur ou noir et blanc ?", "/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/"),
        ("Avec ou sans abonnement ?", "/guides/bloc-notes-numerique-avec-ou-sans-abonnement/"),
        ("Prix et budgets", "/guides/prix-bloc-notes-numerique/"),
        ("Comprendre la technologie E Ink", "/guides/tablette-e-ink/"),
        ("Fonctionnement de l'encre électronique", "/guides/encre-electronique-fonctionnement/"),
        ("Latence et écriture", "/guides/latence-ecriture/"),
        ("OCR et manuscrit", "/guides/ocr-manuscrit/"),
        ("Autonomie des tablettes E Ink", "/guides/autonomie-tablette-e-ink/"),
        ("Formats de fichiers compatibles", "/guides/formats-fichiers-compatibles/"),
        ("Exporter ses notes", "/guides/exporter-notes/"),
        ("Synchronisation cloud", "/guides/synchroniser-notes-cloud/"),
        ("Google Drive", "/guides/bloc-notes-numerique-google-drive/"),
        ("OneDrive", "/guides/bloc-notes-numerique-onedrive/"),
        ("Dropbox", "/guides/bloc-notes-numerique-dropbox/"),
        ("Écosystème ouvert ou fermé ?", "/guides/ecosysteme-ouvert-ou-ferme/"),
        ("Annoter des PDF sur tablette E Ink", "/guides/annoter-pdf-tablette-e-ink/"),
        ("Convertir notes manuscrites en texte", "/guides/convertir-notes-manuscrites-en-texte/"),
        ("Organiser ses notes numériques", "/guides/organiser-notes-numeriques/"),
        ("Transférer ses notes vers l'ordinateur", "/guides/transfert-notes-vers-ordinateur/"),
        ("Imprimer ses notes numériques", "/guides/imprimer-notes-numeriques/"),
    ]
))

GUIDES = [
    ("/guides/choisir-bloc-notes-numerique/", "Comment choisir son bloc-notes numérique ?", "Tous les critères essentiels pour bien choisir votre tablette E Ink de prise de notes."),
    ("/guides/liseuse-ou-bloc-notes-numerique/", "Liseuse ou bloc-notes numérique — Quelle différence ?", "Liseuse ou tablette de prise de notes : comment choisir selon votre usage principal ?"),
    ("/guides/tablette-classique-ou-tablette-e-ink/", "Tablette classique ou tablette E Ink — Laquelle choisir ?", "iPad ou tablette E Ink ? Notre comparaison honnête pour vous aider à décider."),
    ("/guides/taille-ecran-bloc-notes-numerique/", "Quelle taille d'écran pour un bloc-notes numérique ?", "A5, A4, 10 ou 13 pouces : notre guide pour choisir le bon format selon votre usage."),
    ("/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/", "Bloc-notes numérique couleur ou noir et blanc ?", "Faut-il investir dans un écran couleur E Ink ? Notre analyse objective."),
    ("/guides/bloc-notes-numerique-avec-ou-sans-abonnement/", "Bloc-notes numérique avec ou sans abonnement ?", "Les abonnements des tablettes E Ink valent-ils vraiment le coup ? Notre analyse."),
    ("/guides/prix-bloc-notes-numerique/", "Prix des bloc-notes numériques — Quel budget prévoir ?", "Combien coûte un bon bloc-notes numérique ? Budget d'entrée, moyen et premium."),
    ("/guides/tablette-e-ink/", "Comprendre la technologie E Ink", "Qu'est-ce qu'une tablette E Ink ? Fonctionnement, avantages et limites expliqués simplement."),
    ("/guides/encre-electronique-fonctionnement/", "Comment fonctionne l'encre électronique ?", "Le principe de l'encre électronique expliqué : microcapsules, bistabilité et consommation énergétique."),
    ("/guides/latence-ecriture/", "Latence d'écriture sur tablette E Ink — Ce qu'il faut savoir", "Qu'est-ce que la latence d'écriture et comment impacte-t-elle votre expérience ?"),
    ("/guides/ocr-manuscrit/", "OCR et reconnaissance de l'écriture manuscrite", "Comment fonctionne la reconnaissance de texte manuscrit sur les tablettes E Ink ?"),
    ("/guides/autonomie-tablette-e-ink/", "Autonomie des tablettes E Ink — Ce qu'il faut savoir", "Combien de temps dure la batterie d'un bloc-notes numérique ? Notre guide complet."),
    ("/guides/formats-fichiers-compatibles/", "Formats de fichiers compatibles avec les bloc-notes numériques", "PDF, EPUB, DOCX, PNG : quels formats acceptent les tablettes E Ink ?"),
    ("/guides/exporter-notes/", "Comment exporter ses notes depuis un bloc-notes numérique ?", "Toutes les méthodes pour exporter, sauvegarder et partager vos notes numériques."),
    ("/guides/synchroniser-notes-cloud/", "Synchronisation cloud des notes — Guide complet", "Comment synchroniser vos notes numériques avec le cloud ? Toutes les solutions."),
    ("/guides/bloc-notes-numerique-google-drive/", "Bloc-notes numérique et Google Drive — Compatibilité", "Quelles tablettes E Ink fonctionnent avec Google Drive ? Notre guide de compatibilité."),
    ("/guides/bloc-notes-numerique-onedrive/", "Bloc-notes numérique et OneDrive — Compatibilité", "Quelles tablettes E Ink sont compatibles avec Microsoft OneDrive ?"),
    ("/guides/bloc-notes-numerique-dropbox/", "Bloc-notes numérique et Dropbox — Compatibilité", "Quelles tablettes E Ink fonctionnent avec Dropbox ?"),
    ("/guides/ecosysteme-ouvert-ou-ferme/", "Écosystème ouvert ou fermé — Quelle tablette choisir ?", "Android ouvert (Boox) vs écosystème propriétaire (reMarkable) : les vraies différences."),
    ("/guides/annoter-pdf-tablette-e-ink/", "Annoter des PDF sur tablette E Ink — Guide pratique", "Comment annoter efficacement des PDF sur votre tablette E Ink ? Toutes les méthodes."),
    ("/guides/convertir-notes-manuscrites-en-texte/", "Convertir ses notes manuscrites en texte", "Comment transformer votre écriture manuscrite en texte numérique grâce à l'OCR ?"),
    ("/guides/organiser-notes-numeriques/", "Organiser ses notes numériques efficacement", "Dossiers, tags, liens : comment structurer vos notes pour retrouver facilement l'information."),
    ("/guides/transfert-notes-vers-ordinateur/", "Transférer ses notes vers l'ordinateur", "Comment envoyer vos notes depuis votre tablette E Ink vers votre ordinateur ?"),
    ("/guides/imprimer-notes-numeriques/", "Imprimer ses notes numériques", "Comment imprimer les notes créées sur un bloc-notes numérique ?"),
]

for path, title, desc in GUIDES:
    crumbs = breadcrumb(("Guides", "/guides/"), title)
    write(path + "index.html", content_page(title, desc, path, crumbs, "Guide"))

# ── BONS PLANS ────────────────────────────────────────────────────────────────
write("/bons-plans/index.html", hub_page(
    "Bons plans — Bloc-notes numériques en promotion",
    "Les meilleures offres et promotions sur les tablettes E Ink et bloc-notes numériques.",
    "/bons-plans/",
    breadcrumb("Bons plans"),
    "Les meilleures offres du moment sur les bloc-notes numériques, vérifiées régulièrement.",
    [
        ("Tous les bons plans", "/bons-plans/bloc-notes-numerique/"),
        ("Offres reMarkable", "/bons-plans/remarkable/"),
        ("Offres Kindle Scribe", "/bons-plans/kindle-scribe/"),
        ("Offres Kobo Elipsa", "/bons-plans/kobo-elipsa/"),
        ("Offres Boox", "/bons-plans/boox/"),
        ("Occasion", "/bons-plans/bloc-notes-numerique-occasion/"),
        ("Black Friday", "/bons-plans/black-friday/"),
    ]
))

BONS_PLANS = [
    ("/bons-plans/bloc-notes-numerique/", "Bons plans bloc-notes numériques — Promotions en cours", "Toutes les promotions et réductions sur les tablettes E Ink."),
    ("/bons-plans/remarkable/", "Bons plans reMarkable — Meilleures offres", "Les meilleures offres sur reMarkable Paper Pro et reMarkable 2."),
    ("/bons-plans/kindle-scribe/", "Bons plans Kindle Scribe — Promotions", "Les meilleures offres sur le Kindle Scribe."),
    ("/bons-plans/kobo-elipsa/", "Bons plans Kobo Elipsa — Promotions", "Les meilleures offres sur le Kobo Elipsa."),
    ("/bons-plans/boox/", "Bons plans Boox — Promotions et offres", "Les meilleures offres sur les tablettes Boox."),
    ("/bons-plans/bloc-notes-numerique-occasion/", "Bloc-notes numérique d'occasion — Guide d'achat", "Acheter un bloc-notes numérique d'occasion : quoi vérifier et où acheter."),
    ("/bons-plans/black-friday/", "Black Friday — Bloc-notes numériques", "Les meilleures offres Black Friday sur les tablettes E Ink."),
]

for path, title, desc in BONS_PLANS:
    crumbs = breadcrumb(("Bons plans", "/bons-plans/"), title.split("—")[0].strip())
    write(path + "index.html", content_page(title, desc, path, crumbs))

# ── ACCESSOIRES ───────────────────────────────────────────────────────────────
write("/accessoires/index.html", hub_page(
    "Accessoires pour bloc-notes numériques",
    "Stylets, housses, étuis, protections d'écran et accessoires pour tablettes E Ink.",
    "/accessoires/",
    breadcrumb("Accessoires"),
    "Les meilleurs accessoires pour votre bloc-notes numérique : stylets, housses, protections et plus.",
    [
        ("Stylets", "/accessoires/stylets/"),
        ("Housses et étuis", "/accessoires/housses-etuis/"),
        ("Pointes de stylet", "/accessoires/pointes-stylet/"),
        ("Claviers", "/accessoires/claviers/"),
        ("Protections d'écran", "/accessoires/protections-ecran/"),
        ("Accessoires reMarkable", "/accessoires/remarkable/"),
        ("Accessoires Kindle Scribe", "/accessoires/kindle-scribe/"),
        ("Accessoires Boox", "/accessoires/boox/"),
    ]
))

ACCESSOIRES = [
    ("/accessoires/stylets/", "Meilleurs stylets pour tablettes E Ink", "Notre sélection des meilleurs stylets pour bloc-notes numériques."),
    ("/accessoires/housses-etuis/", "Meilleures housses et étuis pour tablettes E Ink", "Protégez votre investissement avec nos housses recommandées."),
    ("/accessoires/pointes-stylet/", "Pointes de stylet — Guide et sélection", "Quelles pointes de stylet choisir pour votre tablette E Ink ?"),
    ("/accessoires/claviers/", "Claviers compatibles avec les tablettes E Ink", "Ajoutez un clavier Bluetooth à votre bloc-notes numérique."),
    ("/accessoires/protections-ecran/", "Meilleures protections d'écran pour tablettes E Ink", "Protégez l'écran de votre tablette E Ink avec les bonnes protections."),
    ("/accessoires/remarkable/", "Accessoires reMarkable — Stylets, housses et plus", "Tous les accessoires officiels et compatibles pour reMarkable."),
    ("/accessoires/kindle-scribe/", "Accessoires Kindle Scribe — Sélection", "Stylets, housses et accessoires pour le Kindle Scribe."),
    ("/accessoires/boox/", "Accessoires Boox — Stylets et housses", "Les meilleurs accessoires pour vos tablettes Boox."),
]

for path, title, desc in ACCESSOIRES:
    crumbs = breadcrumb(("Accessoires", "/accessoires/"), title.split("—")[0].strip())
    write(path + "index.html", content_page(title, desc, path, crumbs))

# ── FOOTER PAGES ──────────────────────────────────────────────────────────────
FOOTER_PAGES = [
    ("/methode-de-test/", "Notre méthode de test — bloc-notes numériques.fr", "Comment testons-nous les bloc-notes numériques ? Notre protocole complet."),
    ("/comment-nous-comparons/", "Comment nous comparons les produits", "Notre méthodologie de comparaison des tablettes E Ink et bloc-notes numériques."),
    ("/a-propos/", "À propos — bloc-notes numériques.fr", "Qui sommes-nous ? Notre équipe et notre engagement pour des tests indépendants."),
    ("/contact/", "Contact — bloc-notes numériques.fr", "Contactez l'équipe de bloc-notes numériques.fr."),
    ("/transparence-affiliation/", "Transparence sur l'affiliation — bloc-notes numériques.fr", "Comment fonctionne notre modèle d'affiliation et comment préservons-nous notre indépendance."),
    ("/mentions-legales/", "Mentions légales — bloc-notes numériques.fr", "Mentions légales, politique de confidentialité et conditions d'utilisation."),
]

for path, title, desc in FOOTER_PAGES:
    slug = path.strip("/").replace("-", " ").title()
    crumbs = breadcrumb(slug)
    write(path + "index.html", content_page(title, desc, path, crumbs))

print("\n✅ Toutes les pages ont été générées.")
