from brand_data import VERIFIED_AT, BRAND_SOURCES, BRANDS

def internal_link(url, label):
    return f'<a href="{url}">{label}</a>'

def sources_html(keys, limit=None):
    rows, seen = [], set()
    for key in keys:
        for label, url in BRAND_SOURCES[key]:
            if url in seen:
                continue
            seen.add(url)
            rows.append(f'<li><a href="{url}" rel="noopener noreferrer">{label}</a></li>')
            if limit and len(rows) >= limit:
                return '<ul class="source-list">' + "".join(rows) + "</ul>"
    return '<ul class="source-list">' + "".join(rows) + "</ul>"

def range_table(brand):
    rows = []
    for name, status, format_, positioning, limit in BRANDS[brand]["current_range"]:
        label = {"CURRENT":"Actuel","CURRENT_DOCUMENTED":"Actuel / encore documenté","PREVIOUS_GENERATION":"Génération précédente","DISCONTINUED":"Arrêté"}.get(status,status)
        rows.append(f"<tr><td><strong>{name}</strong></td><td>{label}</td><td>{format_}</td><td>{positioning}</td><td>{limit}</td></tr>")
    return '<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Modèle</th><th>Statut</th><th>Format</th><th>Positionnement</th><th>Limite à connaître</th></tr></thead><tbody>'+"".join(rows)+"</tbody></table></div>"

def ecosystem_table(brand):
    rows = "".join(f"<tr><td><strong>{layer}</strong></td><td>{desc}</td></tr>" for layer,desc in BRANDS[brand]["ecosystem"])
    return '<div class="table-wrapper"><table class="comp-table"><thead><tr><th>Couche</th><th>Ce qu’il faut comprendre</th></tr></thead><tbody>'+rows+"</tbody></table></div>"

def bullets(items):
    return "<ul>"+"".join(f"<li>{x}</li>" for x in items)+"</ul>"

def brand_hub(brand, extra_links, custom=""):
    b=BRANDS[brand]
    return f'''
<p class="article-answer"><strong>{b["name"]} se distingue surtout par {b["positioning"]}.</strong> Cette page ne repose pas sur un test physique unique : elle synthétise la gamme et les fonctions vérifiées auprès des sources officielles au {VERIFIED_AT}, puis les relie aux usages et comparatifs du site.</p>
<h2 id="positionnement">Ce qui distingue {b["name"]}</h2>
<p>{b["name"]} n’est pas seulement un logo posé sur plusieurs écrans E Ink. La cohérence de la marque se lit dans la relation entre le matériel, le stylet, le logiciel, les services cloud et les possibilités d’export. C’est cette chaîne complète qui détermine si l’écosystème convient à votre manière de travailler.</p>
<p>{custom or "Le bon point de départ consiste donc à regarder les tâches que vous répétez : écrire, annoter, retrouver, transférer et partager. La fiche technique vient ensuite."}</p>
<h2 id="gamme">La gamme actuelle et les générations à distinguer</h2>
<p>La gamme a été vérifiée sur les pages officielles. Nous distinguons volontairement les produits actuels des générations précédentes : mélanger les deux fausserait les comparaisons de prix, de compatibilité et de logiciel.</p>
{range_table(brand)}
<p>Le statut compte particulièrement pour les accessoires et services. Un stylet, un étui ou une fonction cloud compatible avec une génération ne l’est pas nécessairement avec la suivante.</p>
<h2 id="ecosysteme">Comment fonctionne l’écosystème {b["name"]}</h2>
<p>Pour juger la marque, suivez un document depuis son arrivée jusqu’à sa sortie. Le tableau ci-dessous résume ce parcours et les points où l’écosystème ouvre ou limite le workflow.</p>
{ecosystem_table(brand)}
<p>Pour approfondir cette question, le guide sur {internal_link("/guides/ecosysteme-ouvert-ou-ferme/","les écosystèmes ouverts et fermés")} et celui sur {internal_link("/guides/exporter-notes/","l’export des notes")} permettent de comparer les logiques sans se limiter à une marque.</p>
<h2 id="forces">Les forces réelles de la marque</h2><p>Ces forces ne sont utiles que si elles correspondent à vos tâches. Elles ne constituent pas un classement absolu.</p>{bullets(b["strengths"])}
<h2 id="limites">Les limites à connaître avant d’acheter</h2><p>Une page marque utile doit aussi permettre d’écarter l’écosystème.</p>{bullets(b["limits"])}<p>Si l’une d’elles touche une fonction indispensable, consultez directement les {internal_link("/comparatifs/","comparatifs multi-marques")}.</p>
<h2 id="pour-qui">Pour qui {b["name"]} est cohérent — et pour qui il l’est moins</h2><p><strong>À privilégier si :</strong></p>{bullets(b["choose"])}<p><strong>À éviter si :</strong></p>{bullets(b["avoid"])}
<h2 id="suite">Quels contenus consulter ensuite ?</h2><p>Une page marque doit servir de hub.</p><ul>{''.join(f'<li>{internal_link(url,label)}</li>' for label,url in extra_links)}</ul><p>Vous pouvez aussi repartir de votre usage : {internal_link("/usages/prise-de-notes-professionnelle/","travail et réunions")}, {internal_link("/usages/prise-de-notes-etudiant/","études")}, {internal_link("/usages/annotation-pdf/","annotation de PDF")} ou {internal_link("/usages/lecture-et-prise-de-notes/","lecture et prise de notes")}.</p>
<h2 id="documents">Ce qu’il faut vérifier avec vos propres documents</h2><p>Le meilleur moyen de valider un écosystème est de partir de fichiers réels plutôt que d’une liste de fonctions. Prenez un PDF typique, une note manuscrite et un document que vous devez partager avec un collègue. Vérifiez comment chacun entre dans l’appareil, comment il est classé, puis sous quelle forme il ressort.</p><p>Cette vérification révèle des différences que les fiches produit résument mal : une intégration cloud peut n’être qu’un import de copie, une annotation peut rester attachée à un format propriétaire, et une application tierce peut exister tout en étant peu agréable sur E Ink. Le guide sur {internal_link("/guides/transfert-notes-vers-ordinateur/","le transfert vers l’ordinateur")} complète ce test de workflow.</p>
<h2 id="decision-marque">La marque doit-elle décider de l’achat ?</h2><p>La marque sert surtout à réduire l’univers des choix. Une fois les incompatibilités éliminées, revenez au modèle précis : taille d’écran, couleur, éclairage, génération, stylet et coût total peuvent modifier la décision à l’intérieur d’un même écosystème.</p><p>Autrement dit, choisissez d’abord un environnement de travail compatible, puis un appareil. Cela évite de rester fidèle à une marque alors qu’un modèle concurrent répond mieux à une contrainte concrète.</p>
<h2 id="sources">Sources officielles consultées</h2><p>Les informations susceptibles d’évoluer ont été vérifiées le {VERIFIED_AT}.</p>{sources_html([brand],6)}
'''
