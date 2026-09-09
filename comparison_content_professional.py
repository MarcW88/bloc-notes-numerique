from comparison_methodology import PROFESSIONAL_METHOD as M
from comparison_pages import COMPARISON_PAGES
from comparison_products import COMPARISON_PRODUCTS

SLUG = "bloc-notes-numerique-professionnel"
P = COMPARISON_PAGES[SLUG]


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

rank_rows = "".join(
    f"""<tr><td>{i}</td><td><a href=\"{link_for(pid)}\">{COMPARISON_PRODUCTS[pid]['name']}</a></td><td>{total(pid):.1f}/10</td><td>{M['rank_justification'][pid]['decisive_advantage']}</td><td>{M['rank_justification'][pid]['decisive_limit']}</td></tr>"""
    for i, pid in enumerate(ranking, 1)
)

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

PROFESSIONAL_CONTENT = f"""
<p class="article-answer"><strong>Il n’y a pas de vainqueur professionnel universel dans cette sélection.</strong> Avec notre pondération de base, le BOOX Go 10.3 (Gen II) Lumi arrive en tête à 8,75/10, juste devant le Supernote Manta à 8,70/10. Cet écart de 0,05 point est trop faible pour présenter BOOX comme un gagnant robuste : <strong>BOOX prend l’avantage si les applications, Google Play et l’interopérabilité sont prioritaires ; Supernote devient plus logique si l’organisation manuscrite et la structuration des notes pèsent davantage.</strong> La politique IT de votre entreprise peut éliminer l’un ou l’autre avant même le scoring.</p>

<h2 id="verdict">Le verdict en une minute</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Profil</th><th>Choix le plus cohérent</th><th>Pourquoi</th></tr></thead><tbody>
<tr><td>Applications métier, plusieurs clouds, environnement Android</td><td><strong>BOOX Go 10.3 (Gen II) Lumi</strong></td><td>Android 15, Google Play, multi-cloud, BOOXDrop et front light.</td></tr>
<tr><td>Comptes rendus, knowledge management manuscrit, liens entre notes</td><td><strong>Supernote Manta</strong></td><td>Headings, keywords, stars et liens structurent particulièrement bien les carnets.</td></tr>
<tr><td>Couleur, split screen et clavier optionnel</td><td><strong>BOOX Note Air5 C</strong></td><td>Android 15, Google Play, écran couleur et accessoire clavier.</td></tr>
<tr><td>Grand écran couleur dans un environnement volontairement spécialisé</td><td><strong>reMarkable Paper Pro</strong></td><td>11,8 pouces, organisation reMarkable, exports standards et intégrations de travail.</td></tr>
<tr><td>Notes et PDF dans l’environnement le plus simple du groupe</td><td><strong>reMarkable Paper Pure</strong></td><td>10,3 pouces monochrome et périmètre logiciel ciblé.</td></tr>
</tbody></table></div>

<h2 id="methode">Ce que nous comparons réellement</h2>
<p>Cette page répond à un job précis : <strong>capturer des notes de travail, annoter des documents et les faire ressortir proprement vers l’environnement professionnel</strong>. Elle ne cherche pas à remplacer un ordinateur pour les tableurs complexes, les présentations, les visioconférences ou le travail collaboratif lourd.</p>
<p>Nous avons séparé deux niveaux de preuve. Les caractéristiques issues des fabricants — Android 15, Google Play, formats d’export, headings, tags, services cloud ou conditions d’abonnement — sont enregistrées comme faits <code>VERIFIED</code>. Les notes sur 10 sont ensuite des <strong>inférences éditoriales</strong> : une source officielle peut prouver qu’une fonction existe, pas qu’elle « vaut » objectivement 9/10.</p>

<h2 id="criteres">Les critères et leurs poids</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Critère</th><th>Poids</th><th>Pourquoi il compte ici</th></tr></thead><tbody>{criteria_rows}</tbody></table></div>
<p>La grille donne volontairement autant de poids à l’organisation qu’à l’export. Les applications comptent, mais moins que ces deux piliers : certains métiers exigent une app précise, d’autres cherchent justement un appareil spécialisé avec moins de logiciels.</p>

<h2 id="classement">Le classement issu de cette grille</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>#</th><th>Modèle</th><th>Score éditorial</th><th>Avantage décisif</th><th>Limite décisive</th></tr></thead><tbody>{rank_rows}</tbody></table></div>
<p>Les scores servent à rendre la pondération visible. Ils ne doivent pas être lus comme des mesures de laboratoire : aucune latence, autonomie réelle ou sensation d’écriture n’a été mesurée par le site.</p>

<h2 id="boox-supernote">Pourquoi BOOX et Supernote sont pratiquement ex aequo</h2>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Critère</th><th>BOOX Go Lumi</th><th>Supernote Manta</th><th>BOOX Note Air5 C</th></tr></thead><tbody>{score_rows}</tbody></table></div>
<p>Le BOOX Go Lumi gagne surtout sur <strong>les applications</strong> et <strong>l’ouverture des transferts</strong>. Supernote reprend du terrain sur <strong>l’organisation</strong>, le <strong>workflow d’écriture</strong> et la simplicité. Cette opposition explique mieux le choix qu’un écart de quelques centièmes.</p>
<p>Le Note Air5 C est presque au même niveau que le Go Lumi sur apps, export et PDF, mais son positionnement couleur, son poids et ses possibilités supplémentaires le rendent un peu moins simple pour ce job généraliste.</p>

<h2 id="sensibilite">Test de sensibilité : le gagnant change-t-il si les priorités bougent ?</h2>
<p>Oui. C’est pourquoi nous classons le résultat <strong>CONDITIONAL_WINNER</strong>.</p>
<ul><li><strong>Grille de base :</strong> BOOX Go Lumi 8,75 ; Supernote Manta 8,70.</li><li><strong>5 points déplacés des applications vers l’écriture :</strong> Supernote Manta 8,95 ; BOOX Go Lumi 8,65.</li><li><strong>5 points déplacés des applications vers l’organisation :</strong> Supernote Manta 8,95 ; BOOX Go Lumi 8,65.</li><li><strong>5 points déplacés de l’écriture vers les applications :</strong> BOOX Go Lumi 8,85 ; BOOX Note Air5 C 8,75 ; Supernote Manta 8,45.</li></ul>
<p>Autrement dit, le bon verdict n’est pas « BOOX est meilleur », mais <strong>« BOOX si l’ouverture applicative est déterminante ; Supernote si la structure manuscrite l’est davantage »</strong>.</p>

<h2 id="hard-gates">Les critères qui peuvent éliminer un appareil avant le score</h2>
<p>Un contexte professionnel comporte des contraintes que la moyenne ne doit jamais masquer. Les cinq modèles classés passent nos trois gates universels : modèle actuel documenté, prise de notes avec PDF et existence d’une sortie vers un format ou service externe.</p>
<p>Deux gates restent propres à votre entreprise. Premièrement, <strong>la politique IT et cloud</strong> : un compte personnel, Google Play, Dropbox ou un cloud constructeur peuvent être interdits. Deuxièmement, <strong>l’application métier obligatoire</strong> : sa présence doit être confirmée avant achat. Un modèle qui échoue l’un de ces deux gates doit être éliminé, même avec un meilleur score moyen.</p>

<h2 id="produits">Quel modèle choisir selon votre workflow ?</h2>
<h3>BOOX Go 10.3 (Gen II) Lumi : pour l’ouverture</h3><p>BOOX documente Android 15, Google Play, outlines, tags, lasso, plusieurs clouds et BOOXDrop. C’est l’option la plus cohérente si votre bloc-notes doit s’insérer dans un environnement logiciel existant. Sa limite est la contrepartie de cette ouverture : davantage de réglages et une validation IT plus importante qu’avec un OS spécialisé.</p>
<h3>Supernote Manta : pour structurer des connaissances manuscrites</h3><p>Supernote documente headings, keywords, stars et liens entre pages, fichiers ou pages web, ainsi que plusieurs méthodes de transfert. Pour des réunions, suivis de projets et carnets de référence, cette architecture peut compter davantage que l’accès à Google Play. Il n’a toutefois pas de front light et son environnement applicatif est plus spécialisé.</p>
<h3>BOOX Note Air5 C : si la couleur ou le clavier comptent</h3><p>Le Note Air5 C ajoute un écran couleur, Android 15, Google Play, split screen et un clavier optionnel. C’est pertinent si l’appareil doit faire un peu plus que prendre des notes. Pour un outil volontairement simple, cette polyvalence peut aussi devenir une contrainte.</p>
<h3>reMarkable Paper Pro et Paper Pure : pour un environnement plus cadré</h3><p>reMarkable documente dossiers, tags, recherche, exports PDF/PNG/SVG et des intégrations avec Google Drive, Dropbox et OneDrive. Paper Pro ajoute un écran 11,8 pouces couleur et une lumière de lecture ; Paper Pure reste plus simple et monochrome. Connect est optionnel, mais plusieurs fonctions professionnelles avancées — recherche manuscrite, cloud illimité, édition dans les apps et certaines intégrations — y sont liées.</p>

<h2 id="cout">Coût réel : ne pas comparer des prix qui ne sont pas équivalents</h2>
<p>Nous n’intégrons pas le prix dans le score professionnel principal, car les boutiques officielles consultées n’utilisent pas toutes la même devise ni la même base de taxes/import. Transformer ces montants en une note précise créerait une fausse comparabilité.</p>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Modèle</th><th>Prix officiel observé</th><th>Stylet</th><th>Abonnement</th></tr></thead><tbody>{cost_rows}</tbody></table></div>
<p>Le point important est la configuration utilisable : pour Supernote, la page produit consultée ne liste pas de stylet dans le contenu de la boîte ; pour reMarkable, le Marker est inclus ; BOOX indique également un stylet inclus sur les modèles retenus. Les prix doivent être revérifiés au moment de l’achat.</p>

<h2 id="exclusions">Les appareils considérés mais non classés</h2>
<p>Ne pas voir un produit dans le top ne signifie pas qu’il est mauvais. Nous avons aussi considéré plusieurs appareils puis les avons sortis du ranking généraliste lorsqu’ils répondaient mieux à une autre décision.</p>
<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Produit</th><th>Comparabilité</th><th>Pourquoi il n’est pas classé ici</th></tr></thead><tbody>{excluded_rows}</tbody></table></div>

<h2 id="limites">Limites de cette analyse</h2>
<p>Il s’agit d’une <strong>analyse documentaire</strong>. Nous n’avons pas testé physiquement ces cinq appareils dans un environnement de travail commun. Les notes de simplicité et de pertinence sont des inférences éditoriales à partir des fonctions documentées. Les politiques IT, la compatibilité exacte d’une application métier et les prix régionaux doivent être vérifiés dans votre contexte.</p>
<p>Si votre besoin principal est plutôt de savoir <em>si</em> un bloc-notes numérique a du sens au travail, commencez par <a href="/usages/prise-de-notes-professionnelle/">le guide d’usage professionnel</a>. Pour des PDF proches de l’A4, consultez le <a href="/comparatifs/bloc-notes-numerique-a4/">comparatif grand format</a>. Pour comprendre les compromis de cloud et d’export, voir <a href="/guides/exporter-notes/">le guide sur l’export des notes</a>.</p>

<h2 id="sources">Sources officielles consultées</h2><ul class="source-list">{source_items}</ul>
<p><small>Données et sources vérifiées le 9 septembre 2026. Les prix et fonctions de services peuvent évoluer.</small></p>
"""
