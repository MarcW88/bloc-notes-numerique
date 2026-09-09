"""Bespoke guide overrides produced after guide-analysis-workflow decisions.

These entries intentionally override broader quality modules only when an audit
finds a page-specific issue. They are loaded last by the guide regeneration
workflow so the corrected editorial architecture remains persistent.
"""

GUIDE_CONTENT_BESPOKE = {
    "/guides/ocr-manuscrit/": """
      <p class="article-answer"><strong>Sur un bloc-notes numérique, « OCR manuscrit » recouvre souvent plusieurs fonctions différentes : convertir l’écriture en texte éditable, indexer l’écriture pour la recherche ou produire un PDF avec une couche de texte.</strong> Techniquement, la reconnaissance de l’écriture manuscrite est souvent distinguée de l’OCR classique ; dans les interfaces grand public, les fabricants emploient toutefois des termes plus larges. Le bon critère n’est donc pas le mot « OCR », mais le résultat que vous devez récupérer.</p>

      <h2 id="fonctions">Conversion, recherche et PDF recherchable répondent à trois besoins différents</h2>
      <p>La conversion transforme ou copie votre écriture sous forme de texte éditable. La recherche manuscrite garde la page visuelle mais crée un index qui permet de retrouver un mot. Le PDF recherchable conserve l’apparence du carnet tout en ajoutant une couche textuelle exploitable sur ordinateur.</p>
      <div class="table-wrapper"><table class="comp-table"><thead><tr><th>Fonction</th><th>Résultat</th><th>Quand elle est utile</th></tr></thead><tbody>
        <tr><td>Conversion</td><td>texte éditable</td><td>compte rendu, email, Word, copier-coller</td></tr>
        <tr><td>Recherche manuscrite</td><td>index des mots reconnus</td><td>retrouver une note sans transformer la page</td></tr>
        <tr><td>PDF recherchable</td><td>écriture visible + couche texte</td><td>archive, recherche et partage du carnet original</td></tr>
      </tbody></table></div>
      <p>Une fiche produit qui indique simplement « OCR » ne dit donc pas encore ce que vous pourrez faire. Avant l’achat, vérifiez le contenu reconnu, la langue, la connexion éventuellement nécessaire et surtout le format qui sort réellement de l’appareil.</p>

      <h2 id="traitement">Le traitement peut être local, connecté ou dépendre du service utilisé</h2>
      <p>Les conditions diffèrent selon les fonctions. reMarkable demande une connexion Wi-Fi et un compte reMarkable pour la conversion manuscrite documentée. BOOX permet la reconnaissance de texte dans l’application Notes et demande de télécharger des paquets pour certaines langues. Supernote propose des notes avec reconnaissance en arrière-plan et des exports textuels selon le type de note.</p>
      <p>Il faut donc éviter les raccourcis du type « l’OCR fonctionne hors ligne chez telle marque ». La bonne question est plus précise : <em>cette fonction exacte, sur ce modèle et cette version logicielle, traite-t-elle ma note sans connexion et dans quel format puis-je récupérer le résultat ?</em></p>
      <p>Si la dépendance au cloud ou à un compte est déterminante, le guide <a href="/guides/bloc-notes-numerique-avec-ou-sans-abonnement/">avec ou sans abonnement</a> complète ce point.</p>

      <h2 id="exemples">Les fabricants illustrent surtout des sorties différentes</h2>
      <p>Chez reMarkable, la conversion peut créer une nouvelle page typée en conservant l’original manuscrit ; une sélection peut aussi être remplacée directement par du texte. Supernote met davantage l’accent sur la reconnaissance intégrée aux notes, la recherche et l’export TXT ou DOCX. BOOX permet de reconnaître une sélection puis d’éditer, copier, partager ou réinsérer le texte dans une note.</p>
      <p>Kobo distingue ses carnets de base et avancés : les carnets avancés peuvent convertir l’écriture et être exportés dans plusieurs formats textuels. Kindle Scribe permet lui aussi la conversion de carnets ; certaines fonctions plus récentes, comme la recherche dans l’écriture manuscrite ou le PDF recherchable lors du partage, sont réservées aux modèles Kindle Scribe sortis en 2025 ou après.</p>
      <p>Ces exemples servent à comprendre les familles de fonctions. Ils ne constituent pas un classement de qualité de reconnaissance : la documentation officielle décrit ce qui est possible, pas quelle marque reconnaît le mieux votre cursive.</p>

      <h2 id="precision">La précision dépend davantage de votre contenu réel que d’un taux générique</h2>
      <p>Langue, cursive, taille des caractères, abréviations, noms propres, mise en page et vocabulaire spécialisé influencent le résultat. Les équations, schémas, flèches et tableaux manuscrits peuvent être mal interprétés ou exclus volontairement. reMarkable et Amazon documentent par exemple des limites sur les diagrammes, dessins ou équations.</p>
      <p>Un pourcentage de précision générique serait donc peu utile sans protocole commun. Le test pertinent consiste à convertir une page représentative de vos vraies notes, puis à mesurer le travail de correction nécessaire avant réutilisation.</p>

      <h2 id="test">Testez la sortie finale, pas seulement l’animation de conversion</h2>
      <ol>
        <li>Écrivez une page réaliste avec titres, cursive, abréviations, nombres et quelques ratures.</li>
        <li>Lancez la fonction réellement visée : conversion, recherche ou export en PDF recherchable.</li>
        <li>Contrôlez les noms propres, nombres, négations et termes techniques.</li>
        <li>Ouvrez le résultat sur l’ordinateur ou dans l’application où il doit finir.</li>
        <li>Comparez le temps de correction au temps qu’aurait demandé une retranscription manuelle.</li>
      </ol>
      <p>Cette méthode évite de choisir un appareil sur une démonstration propre qui ne ressemble pas à vos notes quotidiennes.</p>

      <h2 id="frontiere-conversion">Quand passer au guide de conversion manuscrite</h2>
      <p>Cette page répond à la question <strong>« quelle fonction de reconnaissance me faut-il ? »</strong>. Si votre besoin est déjà clair et que vous voulez maintenant transformer une note en fichier exploitable de bout en bout, le guide <a href="/guides/convertir-notes-manuscrites-en-texte/">convertir ses notes manuscrites en texte</a> traite la procédure, la correction et le choix du format de sortie.</p>
      <p>Si l’OCR n’est qu’un critère parmi d’autres, replacez-le ensuite dans le <a href="/guides/choisir-bloc-notes-numerique/">guide général de choix</a> ou dans le <a href="/comparatifs/meilleur-bloc-notes-numerique/">comparatif des bloc-notes numériques</a>.</p>

      <h2 id="sources">Sources consultées</h2><ul class="source-list">
        <li><a href="https://support.remarkable.com/articles/Knowledge/Convert-handwritten-notes-into-text" rel="noopener noreferrer">reMarkable : conversion manuscrite</a></li>
        <li><a href="https://support.supernote.com/en_US/Tools-Features/handwriting-recognition" rel="noopener noreferrer">Supernote : reconnaissance manuscrite et export</a></li>
        <li><a href="https://help.boox.com/hc/en-us/articles/8569373888788-Handwritten-Notes" rel="noopener noreferrer">BOOX : reconnaissance dans les notes</a></li>
        <li><a href="https://help.kobo.com/hc/en-us/articles/360062226733-Use-your-Kobo-eReader-as-a-notebook" rel="noopener noreferrer">Kobo : carnets et conversion</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TJE2UYmdw0ppUuR3Rs" rel="noopener noreferrer">Amazon : partage et PDF recherchable sur Kindle Scribe</a></li>
        <li><a href="https://digprjsurvey.amazon.com/csad/help/node/TXEroxFZdxObrcesZO" rel="noopener noreferrer">Amazon : recherche manuscrite sur Kindle Scribe 2025+</a></li>
      </ul>
    """,
}
