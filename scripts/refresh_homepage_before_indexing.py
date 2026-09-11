from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


def replace_section(html: str, eyebrow: str, replacement: str) -> str:
    pattern = re.compile(
        r'<section class="section(?: section--alt)?">\s*'
        r'<div class="container">\s*'
        r'<div class="section-heading">\s*'
        rf'<p class="eyebrow">{re.escape(eyebrow)}</p>.*?</section>',
        re.S,
    )
    updated, count = pattern.subn(replacement.strip(), html, count=1)
    if count != 1:
        raise RuntimeError(f"Section introuvable ou ambiguë: {eyebrow!r} (matches={count})")
    return updated


html = INDEX.read_text(encoding="utf-8")

comparison_section = r'''
<section class="section">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Comparer</p>
      <h2>Cinq écosystèmes à mettre face à face</h2>
      <p>Comparez d’abord la manière de travailler, les limites et l’écosystème. Le prix vient ensuite, une fois la configuration réellement utile définie.</p>
    </div>
    <div class="table-wrapper">
      <table class="comp-table">
        <thead>
          <tr>
            <th>Écosystème</th>
            <th>À considérer si…</th>
            <th>Compromis principal</th>
            <th>Commencer ici</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>reMarkable</strong></td>
            <td>vous privilégiez l’écriture, l’annotation et une interface volontairement simple</td>
            <td>écosystème plus fermé qu’une tablette Android</td>
            <td><a href="/marques/remarkable/">Voir la gamme</a></td>
          </tr>
          <tr>
            <td><strong>Kindle Scribe</strong></td>
            <td>vous lisez beaucoup dans l’écosystème Kindle et voulez aussi écrire</td>
            <td>outils de notes moins structurés que sur les appareils les plus spécialisés</td>
            <td><a href="/marques/kindle-scribe/">Voir l’analyse</a></td>
          </tr>
          <tr>
            <td><strong>BOOX</strong></td>
            <td>vous avez besoin d’Android, d’applications tierces ou de workflows PDF avancés</td>
            <td>davantage de réglages et une courbe d’apprentissage plus élevée</td>
            <td><a href="/marques/boox/avis/">Lire l’avis documentaire</a></td>
          </tr>
          <tr>
            <td><strong>Kobo Elipsa</strong></td>
            <td>lecture Kobo, annotation et carnets doivent rester réunis dans le même appareil</td>
            <td>positionnement davantage centré sur la lecture</td>
            <td><a href="/marques/kobo-elipsa/">Voir l’analyse</a></td>
          </tr>
          <tr>
            <td><strong>Supernote</strong></td>
            <td>vous privilégiez l’organisation des notes manuscrites et un outil centré sur l’écriture</td>
            <td>moins polyvalent qu’un environnement Android ouvert</td>
            <td><a href="/marques/supernote/">Voir l’analyse</a></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="text-align:center;margin-top:24px;">
      <a href="/comparatifs/meilleur-bloc-notes-numerique/" class="btn btn-secondary">Voir notre sélection 2026</a>
    </div>
  </div>
</section>
'''

profiles_section = r'''
<section class="section section--alt">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">Profils d’usage</p>
      <h2>Partez de votre contrainte, pas d’un modèle</h2>
      <p>Ces profils orientent vers les sélections les plus utiles avant de comparer des appareils un par un.</p>
    </div>
    <div class="usage-grid">
      <a href="/comparatifs/bloc-notes-numerique-professionnel/" class="usage-card">
        <span class="content-type type-comparatif">Professionnel</span>
        <h3 style="margin-top:12px;">Réunions, PDF et travail quotidien</h3>
        <p>Priorité à la rapidité de capture, l’export, la synchronisation et la continuité avec vos outils de travail.</p>
      </a>
      <a href="/comparatifs/bloc-notes-numerique-etudiant/" class="usage-card">
        <span class="content-type type-comparatif">Étudiant</span>
        <h3 style="margin-top:12px;">Cours, révisions et documents</h3>
        <p>Comparez prise de notes, lecture de PDF, organisation des matières, poids et coût total.</p>
      </a>
      <a href="/comparatifs/bloc-notes-numerique-couleur/" class="usage-card">
        <span class="content-type type-comparatif">Couleur</span>
        <h3 style="margin-top:12px;">Graphiques, surlignages et codes visuels</h3>
        <p>À privilégier lorsque la couleur transporte une information utile, pas seulement pour l’esthétique.</p>
      </a>
      <a href="/comparatifs/bloc-notes-numerique-sans-abonnement/" class="usage-card">
        <span class="content-type type-comparatif">Sans abonnement</span>
        <h3 style="margin-top:12px;">Éviter les coûts récurrents</h3>
        <p>Vérifiez ce qui reste disponible sans formule payante : notes locales, export, cloud et applications compagnon.</p>
      </a>
      <a href="/comparatifs/bloc-notes-numerique-a4/" class="usage-card">
        <span class="content-type type-comparatif">Grand format</span>
        <h3 style="margin-top:12px;">PDF, plans et pages denses</h3>
        <p>Pour ceux qui veulent réduire le zoom et conserver davantage de document visible à l’écran.</p>
      </a>
      <a href="/comparatifs/bloc-notes-numerique-pas-cher/" class="usage-card">
        <span class="content-type type-comparatif">Budget</span>
        <h3 style="margin-top:12px;">Limiter le coût sans acheter au hasard</h3>
        <p>Comparez la configuration complète : appareil, stylet, protection et services réellement nécessaires.</p>
      </a>
    </div>
    <div style="text-align:center;margin-top:24px;">
      <a href="/comparatifs/" class="btn btn-ghost">Voir tous les comparatifs</a>
    </div>
  </div>
</section>
'''

recent_section = r'''
<section class="section section--alt">
  <div class="container">
    <div class="section-heading">
      <p class="eyebrow">À lire maintenant</p>
      <h2>Analyses et guides récents</h2>
      <p>Six contenus vérifiés récemment pour passer d’un besoin concret à une shortlist de modèles.</p>
    </div>
    <div class="content-grid">
      <a href="/marques/remarkable/remarkable-paper-pro-avis/" class="content-card">
        <div class="content-card-img"><img src="/assets/generated/prise-de-notes-professionnelle-hero.webp" alt="" loading="lazy" decoding="async" style="width:100%;height:100%;object-fit:cover;"></div>
        <div class="content-card-body">
          <span class="content-type type-test">Analyse documentaire</span>
          <h3>reMarkable Paper Pro : forces et limites</h3>
          <p>Écriture, écran couleur, Connect, prix et profils auxquels le grand format convient réellement.</p>
          <span class="content-date">Sources vérifiées le 8 septembre 2026</span>
        </div>
      </a>
      <a href="/marques/boox/avis/" class="content-card">
        <div class="content-card-img"><img src="/assets/generated/bloc-notes-numerique-avec-ou-sans-abonnement-hero.webp" alt="" loading="lazy" decoding="async" style="width:100%;height:100%;object-fit:cover;"></div>
        <div class="content-card-body">
          <span class="content-type type-test">Analyse documentaire</span>
          <h3>BOOX : liberté Android et complexité</h3>
          <p>Versions Android, applications, cloud, PDF, garantie et compromis à connaître avant de choisir la gamme.</p>
          <span class="content-date">Sources vérifiées le 8 septembre 2026</span>
        </div>
      </a>
      <a href="/comparatifs/meilleur-bloc-notes-numerique/" class="content-card">
        <div class="content-card-img"><img src="/assets/generated/choisir-bloc-notes-numerique-hero.webp" alt="" loading="lazy" decoding="async" style="width:100%;height:100%;object-fit:cover;"></div>
        <div class="content-card-body">
          <span class="content-type type-comparatif">Comparatif 2026</span>
          <h3>Meilleur bloc-notes numérique : lequel choisir ?</h3>
          <p>Notre sélection par usage avec un choix par défaut et les alternatives à privilégier selon votre workflow.</p>
          <span class="content-date">Vérifié le 9 septembre 2026</span>
        </div>
      </a>
      <a href="/guides/prix-bloc-notes-numerique/" class="content-card">
        <div class="content-card-img"><img src="/assets/generated/prix-bloc-notes-numerique-hero.webp" alt="" loading="lazy" decoding="async" style="width:100%;height:100%;object-fit:cover;"></div>
        <div class="content-card-body">
          <span class="content-type type-guide">Guide</span>
          <h3>Quel budget prévoir au total ?</h3>
          <p>Appareil, stylet, protection, abonnements et accessoires : comparez une configuration complète plutôt qu’un prix d’appel.</p>
          <span class="content-date">Vérifié le 8 septembre 2026</span>
        </div>
      </a>
      <a href="/guides/bloc-notes-numerique-couleur-ou-noir-et-blanc/" class="content-card">
        <div class="content-card-img"><img src="/assets/generated/bloc-notes-numerique-couleur-ou-noir-et-blanc-hero.webp" alt="" loading="lazy" decoding="async" style="width:100%;height:100%;object-fit:cover;"></div>
        <div class="content-card-body">
          <span class="content-type type-guide">Guide</span>
          <h3>Couleur ou noir et blanc ?</h3>
          <p>Décidez selon vos documents et la perte d’information réelle en niveaux de gris, pas selon le seul attrait de la couleur.</p>
          <span class="content-date">Vérifié le 8 septembre 2026</span>
        </div>
      </a>
      <a href="/guides/taille-ecran-bloc-notes-numerique/" class="content-card">
        <div class="content-card-img"><img src="/assets/generated/taille-ecran-bloc-notes-numerique-hero.webp" alt="" loading="lazy" decoding="async" style="width:100%;height:100%;object-fit:cover;"></div>
        <div class="content-card-body">
          <span class="content-type type-guide">Guide</span>
          <h3>Quelle taille d’écran choisir ?</h3>
          <p>Petits formats, 10 pouces ou grands écrans : choisissez à partir de vos documents et de votre mobilité.</p>
          <span class="content-date">Vérifié le 8 septembre 2026</span>
        </div>
      </a>
    </div>
    <div style="text-align:center;margin-top:24px;">
      <a href="/guides/" class="btn btn-secondary">Voir tous les guides</a>
    </div>
  </div>
</section>
'''

html = replace_section(html, "Comparatif", comparison_section)
html = replace_section(html, "Profils d’usage", profiles_section)
html = replace_section(html, "Derniers contenus", recent_section)

html = html.replace(
    "<p>Zéro papier, organisation numérique, durabilité.</p>",
    "<p>Classement, sauvegarde, export et passage progressif du papier au numérique.</p>",
)

html = html.replace(
    "<p>Chaque recommandation devra indiquer clairement son niveau de preuve et les informations effectivement vérifiées.</p>",
    "<p>Nos analyses distinguent les informations vérifiées, les observations issues d’essais indépendants et ce que nous n’avons pas testé nous-mêmes.</p>",
)

INDEX.write_text(html, encoding="utf-8")
print("Homepage refreshed:", INDEX)
