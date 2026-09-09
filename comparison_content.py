from comparison_products import COMPARISON_PRODUCTS
from comparison_pages import COMPARISON_PAGES, CRITERIA_LABELS
from comparison_bespoke_output import bespoke_body

# IMPORTANT:
# `render_legacy_comparison` only preserves currently untouched comparison pages.
# It is not the editorial template for new/reworked pages. Any page produced by
# `comparison-content-workflow` must provide a per-URL bespoke body through
# `comparison_bespoke_output.py` (or a future free-form source consumed there).


def link_for(pid):
    return {'remarkable_pure': '/marques/remarkable/', 'remarkable_pro': '/marques/remarkable/remarkable-paper-pro/', 'remarkable_move': '/marques/remarkable/', 'kindle_scribe3': '/marques/kindle-scribe/', 'kindle_colorsoft': '/marques/kindle-scribe/', 'boox_go2': '/marques/boox/', 'boox_go_lumi': '/marques/boox/', 'boox_air5c': '/marques/boox/', 'boox_notemax': '/marques/boox/', 'kobo_elipsa': '/marques/kobo-elipsa/', 'supernote_manta': '/marques/supernote/', 'supernote_nomad': '/marques/supernote/'}[pid]


def why_score(pid, p):
    prod=COMPARISON_PRODUCTS[pid]
    top=sorted(p["weights"].items(), key=lambda x:-x[1])[:3]
    return ", ".join(f"{CRITERIA_LABELS[c].lower()} ({prod['scores'][c]}/10)" for c,_ in top)


def render_legacy_comparison(slug):
    """Render untouched legacy pages only.

    This preserves the existing site while pages are progressively audited.
    It must not be used as an editorial skeleton by the production workflow.
    """
    p=COMPARISON_PAGES[slug]
    products=COMPARISON_PRODUCTS
    winner=p['ranking'][0][0]; wp=products[winner]; head=p['type']=='head_to_head'
    intro=(f'<p class="article-answer"><strong>Notre grille place {wp["name"]} en tête pour cette intention.</strong> Ce verdict vient de critères définis avant le classement pour le besoin « {p["job"]} ». Il s’agit d’une analyse documentaire, pas d’un test physique : les notes servent à rendre les arbitrages visibles et non à simuler des mesures de laboratoire.</p>')
    meth=(f'<h2 id="methode">Comment nous avons construit ce comparatif</h2><p>Nous avons d’abord défini l’intention — {p["job"]} — puis sélectionné uniquement des appareils actuellement documentés par leurs fabricants. Les critères ont été pondérés avant le calcul. Une note élevée ne signifie donc pas qu’un produit est meilleur en général : elle signifie qu’il répond mieux à cette requête précise.</p><p>Les scores sont des jugements éditoriaux fondés sur les fonctions vérifiées. Une spécification officielle est traitée comme un fait ; le passage de cette spécification à une note reste une déduction éditoriale. La commission d’affiliation n’entre jamais dans le calcul.</p>')
    rows=''.join(f'<tr><td>{CRITERIA_LABELS[c]}</td><td>{w}%</td><td>{"Critère majeur" if w>=20 else "Critère secondaire"}</td></tr>' for c,w in p['weights'].items())
    crit=(f'<h2 id="criteres">Les critères qui déterminent le classement</h2><p>La pondération évite de produire un classement générique identique sur toutes les pages. Un étudiant, un professionnel ou un lecteur de PDF A4 n’accorde pas la même importance aux mêmes fonctions.</p><div class="table-wrapper"><table class="comp-table"><thead><tr><th>Critère</th><th>Poids</th><th>Rôle</th></tr></thead><tbody>{rows}</tbody></table></div><p>Nous conservons cette grille avec la page dans <code>.content/comparisons/</code>. Si un modèle ou une fonction évolue, le bon processus consiste à mettre à jour la preuve puis à recalculer, pas à déplacer les poids pour conserver le même gagnant.</p>')
    rankrows=''.join(f'<tr><td>{i}</td><td><a href="{link_for(pid)}">{products[pid]["name"]}</a></td><td>{score:.1f}/10</td><td>{products[pid]["best"]}</td><td>{products[pid]["limit"]}</td></tr>' for i,(pid,score) in enumerate(p['ranking'],1))
    ranking=(f'<h2 id="classement">Classement issu de la grille</h2><p>Le tableau ci-dessous synthétise le calcul. Il faut surtout lire la dernière colonne : un produit peut perdre quelques dixièmes au global tout en étant le meilleur choix pour un profil particulier.</p><div class="table-wrapper"><table class="comp-table"><thead><tr><th>#</th><th>Modèle</th><th>Score éditorial</th><th>Point fort</th><th>Limite</th></tr></thead><tbody>{rankrows}</tbody></table></div><p>{wp["name"]} arrive premier grâce notamment à {why_score(winner,p)}. Ce résultat n’efface pas les compromis : {wp["limit"]}.</p>')
    blocks=[]
    for i,(pid,score) in enumerate(p['ranking'][:(2 if head else 4)],1):
        pr=products[pid]
        blocks.append(f'<h2 id="produit-{i}">{i}. {pr["name"]} — pourquoi il se classe ici</h2><p><strong>À privilégier pour :</strong> {pr["best"]}. Dans cette grille, son score est de {score:.1f}/10. Les critères les plus lourds expliquent l’essentiel de sa position : {why_score(pid,p)}.</p><p><strong>La limite à ne pas masquer :</strong> {pr["limit"]}. Cette contrainte peut suffire à choisir un produit moins bien classé si elle touche votre usage central. Le prix repéré dans la source officielle est indiqué comme « {pr["price"]} » ; il doit être revérifié au moment de l’achat, avec les accessoires indispensables.</p><p>Consultez la <a href="{link_for(pid)}">page marque correspondante</a> avant de décider, puis vérifiez le parcours complet de vos fichiers avec le guide sur <a href="/guides/exporter-notes/">l’export des notes</a>.</p>')
    if head:
        a,b=p['products']; pa,pb=products[a],products[b]
        diffrows=''.join(f'<tr><td>{CRITERIA_LABELS[c]}</td><td>{pa["scores"][c]}/10</td><td>{pb["scores"][c]}/10</td><td>{("Avantage "+pa["name"]) if pa["scores"][c]>pb["scores"][c] else (("Avantage "+pb["name"]) if pb["scores"][c]>pa["scores"][c] else "Égalité")}</td></tr>' for c in p['weights'])
        blocks.append(f'<h2 id="face-a-face">Les différences qui doivent réellement faire basculer le choix</h2><p>Le score global est moins utile que les critères où les deux appareils s’écartent. Voici la lecture critère par critère utilisée pour le verdict.</p><div class="table-wrapper"><table class="comp-table"><thead><tr><th>Critère</th><th>{pa["name"]}</th><th>{pb["name"]}</th><th>Lecture</th></tr></thead><tbody>{diffrows}</tbody></table></div><p>Le bon choix est donc conditionnel : privilégiez l’appareil qui gagne sur votre critère bloquant, même s’il termine second au score global.</p>')
    else:
        blocks.append('<h2 id="profils">Quel modèle choisir selon votre profil ?</h2><p>Le classement général ne doit pas devenir une règle universelle. Si votre priorité change, le gagnant peut changer lui aussi. Un lecteur intensif peut préférer Kindle ou Kobo ; un utilisateur d’applications métier regardera BOOX ; un utilisateur qui valorise l’organisation manuscrite peut préférer Supernote ; un workflow volontairement simple peut favoriser reMarkable.</p><p>Avant l’achat, écrivez vos trois tâches hebdomadaires les plus importantes et éliminez tout appareil qui bloque l’une d’elles. Ce filtre est plus utile qu’une différence de quelques dixièmes dans le score.</p>')
    decision='<h2 id="cout">Comparer le coût de la configuration, pas seulement l’appareil</h2><p>Le coût total peut inclure le stylet, l’étui, un clavier, des pointes et un éventuel service récurrent. Les prix ci-dessus proviennent de boutiques officielles mais certaines marques affichent en dollars ou hors droits : nous ne les convertissons pas artificiellement en euros. Utilisez le guide <a href="/guides/prix-bloc-notes-numerique/">prix d’un bloc-notes numérique</a> pour construire des paniers équivalents.</p><p>Pour une page « pas cher » ou « sans abonnement », ce coût réel pèse davantage dans la grille. Sur les autres comparatifs, il reste un critère parmi plusieurs : payer moins pour un appareil qui ne peut pas exporter ou afficher correctement vos PDF n’est pas une économie.</p><h2 id="limites">Ce que ce comparatif ne prétend pas mesurer</h2><p>Nous n’avons pas inventé de test de latence, d’autonomie ou de sensation d’écriture. Lorsqu’une marque publie une donnée, elle peut être citée comme spécification ; nous n’en faisons pas une mesure indépendante. La sensation de stylet, le ghosting perçu et la durée de batterie en conditions réelles doivent être confirmés par un test documenté avant d’être présentés comme expérience propre.</p><p>Les modèles et prix évoluent. La date de recherche est conservée dans le fichier de comparaison afin que la prochaine mise à jour puisse distinguer une donnée fraîche d’un ancien repère.</p><h2 id="suite">Comment finaliser votre choix</h2><p>Si vous hésitez encore, commencez par <a href="/guides/choisir-bloc-notes-numerique/">le guide de choix général</a>, puis vérifiez <a href="/guides/taille-ecran-bloc-notes-numerique/">la taille d’écran</a>, <a href="/guides/bloc-notes-numerique-avec-ou-sans-abonnement/">les fonctions avec ou sans abonnement</a> et <a href="/guides/ecosysteme-ouvert-ou-ferme/">l’ouverture de l’écosystème</a>. Ces guides expliquent les critères ; le présent comparatif les applique à une décision commerciale précise.</p>'
    srcs=[]
    for pid in p['products']:
        pr=products[pid]
        if pr['source'] not in [x[0] for x in srcs]: srcs.append((pr['source'],pr['source_label']))
    sources='<h2 id="sources">Sources officielles consultées</h2><ul class="source-list">'+''.join(f'<li><a href="{u}" rel="noopener noreferrer">{lab}</a></li>' for u,lab in srcs)+'</ul>'
    return intro+meth+crit+ranking+''.join(blocks)+decision+sources


COMPARISON_CONTENT = {
    slug: bespoke_body(slug, render_legacy_comparison(slug))
    for slug in COMPARISON_PAGES
}
