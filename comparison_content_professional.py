from comparison_methodology import PROFESSIONAL_METHOD as M
from comparison_pages import COMPARISON_PAGES
from comparison_products import COMPARISON_PRODUCTS
from comparison_editorial_strategy import COMPARISON_EDITORIAL_STRATEGIES

SLUG = "bloc-notes-numerique-professionnel"
P = COMPARISON_PAGES[SLUG]
STRATEGY = COMPARISON_EDITORIAL_STRATEGIES[SLUG]


def total(pid, weights=None):
    weights = weights or P["weights"]
    return sum(M["scores"][pid][c]["score"] * weights[c] for c in weights) / 100


def link_for(pid):
    return {
        "boox_go_lumi": "/marques/boox/",
        "supernote_manta": "/marques/supernote/",
        "boox_air5c": "/marques/boox/",
        "remarkable_pro": "/marques/remarkable/remarkable-paper-pro/",
        "remarkable_pure": "/marques/remarkable/",
    }[pid]


ranking = sorted(P["products"], key=lambda pid: total(pid), reverse=True)

criteria_rows = "".join(
    f"""<tr><td>{M['criteria_definitions'][cid]['label']}</td><td>{weight}%</td><td>{M['criteria_definitions'][cid]['weight_rationale']}</td></tr>"""
    for cid, weight in P["weights"].items()
)

score_rows = "".join(
    f"""<tr><td>{M['criteria_definitions'][cid]['label']}</td><td>{M['scores']['boox_go_lumi'][cid]['score']}/10</td><td>{M['scores']['supernote_manta'][cid]['score']}/10</td><td>{M['scores']['boox_air5c'][cid]['score']}/10</td></tr>"""
    for cid in P["weights"]
)

excluded_rows = "".join(
    f"""<tr><td>{item['id'].replace('_', ' ')}</td><td>{item['equivalence']}</td><td>{item['reason']}</td></tr>"""
    for item in M["universe"] if item["status"] == "EXCLUDED"
)

cost_rows = "".join(
    f"""<tr><td>{COMPARISON_PRODUCTS[pid]['name']}</td><td>{data['snapshot']}</td><td>{data['stylus']}</td><td>{data['subscription']}</td></tr>"""
    for pid, data in M["total_solution_cost"]["products"].items()
)

sources = []
seen = set()
for item in M["evidence_ledger"]:
    if item["source"] not in seen:
        seen.add(item["source"])
        sources.append((item["source"], item["claim"]))
source_items = "".join(
    f'<li><a href="{url}" rel="noopener noreferrer">{claim}</a></li>'
    for url, claim in sources
)

score_summary = ", ".join(
    f"{COMPARISON_PRODUCTS[pid]['name']} {total(pid):.2f}/10"
    for pid in ranking
)

PROFESSIONAL_CONTENT = f"""
<p class="article-answer"><strong>Le meilleur bloc-notes numérique professionnel dépend moins d'un podium que de votre manière de travailler.</strong> Dans notre grille de base, le BOOX Go 10.3 (Gen II) Lumi arrive à 8,75/10 et le Supernote Manta à 8,70/10. Cet écart de 0,05 point n'est pas assez robuste pour déclarer BOOX vainqueur en toutes circonstances : <strong>BOOX prend l'avantage si vous avez besoin d'applications, de Google Play et de plusieurs voies d'export ; Supernote devient plus cohérent si votre travail repose surtout sur l'organisation manuscrite, les liens entre notes et un environnement plus spécialisé.</strong> Avant même ce duel, la politique IT de votre entreprise peut rendre un appareil inadapté.</p>

<h2 id="it">Avant le classement : votre politique IT peut déjà décider</h2>
<p>Dans un usage professionnel, certaines contraintes ne devraient jamais être réduites à quelques points dans une moyenne. Si votre entreprise interdit Google Play, un cloud personnel, un service constructeur non approuvé ou l'installation d'applications non gérées, un appareil peut être éliminé même s'il obtient le meilleur score théorique.</p>
<p>Notre grille conserve donc deux hard gates propres à votre contexte : <strong>l'appareil doit respecter les règles IT et cloud de l'organisation</strong>, et <strong>toute application métier indispensable doit être réellement compatible</strong>. Ces deux vérifications se font avant l'achat, pas après lecture du podium.</p>
<p>C'est la première différence avec un comparatif grand public : un produit très ouvert peut être un avantage dans une PME et un problème dans un environnement fortement administré.</p>

<h2 id="duel">Le vrai duel : ouverture logicielle ou organisation manuscrite ?</h2>
<p>Le classement de tête s'explique presque entièrement par cette tension. BOOX et Supernote ne proposent pas seulement deux niveaux de qualité différents ; ils incarnent deux façons de construire un outil de travail.</p>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Votre priorité</th><th>BOOX Go 10.3 Lumi</th><th>Supernote Manta</th></tr></thead><tbody>
<tr><td>Installer des applications et rester proche d'un environnement Android</td><td><strong>Avantage net</strong> : Android 15 et Google Play documentés</td><td>Écosystème plus spécialisé</td></tr>
<tr><td>Multiplier les voies d'export et les services</td><td><strong>Avantage</strong> : cloud, BOOXDrop et environnement Android</td><td>Plusieurs transferts existent, mais l'ouverture applicative est moindre</td></tr>
<tr><td>Structurer des carnets complexes</td><td>Outlines, tags et outils de notes</td><td><strong>Avantage</strong> : headings, keywords, stars et liens entre contenus</td></tr>
<tr><td>Rester dans un outil volontairement spécialisé</td><td>Plus de possibilités, donc aussi plus de réglages</td><td><strong>Avantage</strong> si la simplicité du périmètre est recherchée</td></tr>
<tr><td>Utiliser l'appareil dans l'obscurité</td><td><strong>Front light documenté</strong></td><td>Pas de front light</td></tr>
</tbody></table></div>

<h3>Pourquoi BOOX passe devant dans la grille de base</h3>
<p>Le Go Lumi marque surtout des points sur les applications et l'export. Pour un professionnel qui doit connecter son bloc-notes à plusieurs outils, cette ouverture peut réduire davantage de frictions que la qualité intrinsèque de l'organisation manuscrite. C'est le scénario dans lequel son léger avantage global a du sens.</p>
<p>Cette ouverture est aussi sa limite : davantage de possibilités signifie davantage de réglages, de dépendances et de questions de conformité. Si votre IT filtre les applications ou les clouds, l'avantage peut disparaître complètement.</p>

<h3>Pourquoi Supernote peut être le meilleur choix malgré sa deuxième place</h3>
<p>Supernote documente des outils d'organisation qui ont une vraie conséquence sur un carnet de travail : headings, keywords, stars et liens entre pages ou fichiers. Pour quelqu'un qui transforme ses notes de réunion en système de référence, cette architecture peut peser davantage que Google Play.</p>
<p>Il devient donc premier dès que l'organisation ou l'écriture gagne quelques points de poids. Son compromis est inverse de BOOX : moins d'ouverture généraliste, mais un environnement plus concentré sur le manuscrit structuré.</p>

<h2 id="branches">Les autres modèles ne jouent pas exactement la même partie</h2>
<p>Le BOOX Note Air5 C, le reMarkable Paper Pro et le Paper Pure restent dans le classement parce qu'ils peuvent répondre au même job professionnel, mais chacun introduit une autre branche de décision.</p>

<h3>BOOX Note Air5 C : quand la couleur et le clavier deviennent utiles</h3>
<p>Le Note Air5 C reste très proche du Go Lumi sur les fonctions Android, l'export et le PDF. Son intérêt apparaît lorsque la couleur, le split screen ou le clavier optionnel font réellement partie du workflow. Si vous cherchez surtout un cahier de réunion simple, cette polyvalence supplémentaire peut au contraire ajouter du poids et de la complexité sans résoudre un problème important.</p>

<h3>reMarkable : quand un environnement plus cadré est une qualité</h3>
<p>Paper Pro et Paper Pure sont moins ouverts que BOOX, mais ce n'est pas automatiquement un défaut. reMarkable documente dossiers, tags, recherche, exports standards et intégrations avec Google Drive, Dropbox et OneDrive. Paper Pro ajoute un grand écran couleur et une lumière de lecture ; Paper Pure reste plus sobre et monochrome.</p>
<p>Le compromis se déplace alors vers l'écosystème : Connect est optionnel, mais plusieurs fonctions professionnelles avancées — recherche manuscrite, cloud illimité, édition dans les apps ou certaines intégrations — en dépendent. Pour certaines équipes, ce cadre est rassurant ; pour d'autres, il est trop restrictif.</p>

<h2 id="score">Pourquoi 0,05 point ne doit pas devenir un verdict absolu</h2>
<p>Les scores servent à rendre nos arbitrages visibles, pas à simuler une précision de laboratoire. Avec la pondération de base, le repère est : {score_summary}.</p>
<p>La différence entre les trois premiers vient de quelques critères très ciblés :</p>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Critère</th><th>BOOX Go Lumi</th><th>Supernote Manta</th><th>BOOX Note Air5 C</th></tr></thead><tbody>{score_rows}</tbody></table></div>
<p>Nous avons donc testé la sensibilité du résultat. En déplaçant seulement 5 points du poids des applications vers l'écriture, Supernote passe à 8,95 contre 8,65 pour le Go Lumi. Le même basculement se produit si ces 5 points vont vers l'organisation. À l'inverse, si l'on renforce encore le poids des applications, BOOX consolide son avance.</p>
<p>Le statut correct n'est donc pas <em>ROBUST_WINNER</em>, mais <strong>CONDITIONAL_WINNER</strong>. Cette nuance doit rester visible même si le tableau numérique conserve un ordre de classement.</p>

<h2 id="cout-exclusions">Ce que le score ne doit pas absorber artificiellement</h2>
<p>Deux sujets restent volontairement à côté de la moyenne : le coût réel et les produits qui ont été considérés puis exclus.</p>

<h3>Un prix officiel n'est pas encore un coût comparable</h3>
<p>Les boutiques consultées n'affichent pas toutes la même devise, les mêmes taxes ni les mêmes bundles. Nous refusons donc de fabriquer une note de coût très précise à partir de bases qui ne le sont pas.</p>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Modèle</th><th>Prix officiel observé</th><th>Stylet</th><th>Abonnement</th></tr></thead><tbody>{cost_rows}</tbody></table></div>
<p>Le bon contrôle consiste à comparer une configuration réellement utilisable. Pour Supernote, la page produit consultée ne liste pas de stylet dans le contenu de la boîte ; pour reMarkable, le Marker est inclus ; BOOX indique également un stylet inclus sur les modèles retenus. Ces éléments doivent être revérifiés au moment de l'achat.</p>

<h3>Certains appareils ont été exclus parce qu'ils racontent une autre décision</h3>
<p>Un produit absent du classement n'est pas nécessairement inférieur. Certains modèles ont été examinés puis sortis parce qu'ils répondent mieux à un comparatif plus spécifique.</p>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Produit considéré</th><th>Comparabilité</th><th>Pourquoi il n'est pas classé ici</th></tr></thead><tbody>{excluded_rows}</tbody></table></div>

<h2 id="methode">Comment lire cette analyse — et ses limites</h2>
<p>Cette page est une <strong>analyse documentaire</strong>, pas un test physique commun des cinq appareils. Les caractéristiques issues des fabricants sont conservées comme faits vérifiés lorsqu'elles sont confirmées par une source officielle. Les notes sur 10 sont ensuite des inférences éditoriales qui appliquent une grille au job professionnel ; une source peut prouver qu'une fonction existe, pas qu'elle vaut objectivement 8 ou 9 sur 10.</p>
<p>Les critères utilisés restent auditables, mais ils ne dictent pas la structure de la page. Ils sont pondérés ainsi :</p>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Critère</th><th>Poids</th><th>Pourquoi il compte ici</th></tr></thead><tbody>{criteria_rows}</tbody></table></div>
<p>Nous n'avons pas mesuré la latence, l'autonomie réelle ou la sensation d'écriture. Les politiques IT, la compatibilité exacte d'une application métier et les prix régionaux doivent aussi être vérifiés dans votre contexte.</p>
<p>Si votre question est encore de savoir <em>si</em> un bloc-notes numérique a du sens au travail, commencez par <a href="/usages/prise-de-notes-professionnelle/">le guide d'usage professionnel</a>. Si vos documents sont proches de l'A4, le <a href="/comparatifs/bloc-notes-numerique-a4/">comparatif grand format</a> répond à une autre décision. Pour le chemin des fichiers, consultez aussi <a href="/guides/exporter-notes/">le guide sur l'export des notes</a>.</p>

<h2 id="sources">Sources officielles consultées</h2><ul class="source-list">{source_items}</ul>
<p><small>Données et sources vérifiées le 9 septembre 2026. Les prix, services et compatibilités peuvent évoluer.</small></p>
"""
