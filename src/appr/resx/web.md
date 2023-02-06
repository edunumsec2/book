# World Wide Web

Le **World Wide Web** (WWW), littéralement la « toile (d’araignée) mondiale », est un système qui permet de consulter avec un navigateur, à travers l'Internet, des pages accessibles sur des sites.

## Historique

Pendant ses premières décennies (jusque dans les années 90), seuls les universitaires, les militaires, certaines entreprises
et une communauté d'enthousiastes (largement issue du mouvement hippie) utilisaient Internet.
Les utilisations principales étaient le *chat* (par un terminal), la connexion sur un ordinateur
à distance, l'email et le transfert de fichiers entre ordinateurs.

Pour aller chercher un fichier se trouvant sur un autre ordinateur, il fallait savoir exactement
sur quelle machine celui-ci se trouvait et où il se situait dans cette machine. Il fallait donc
établir des listes de ressources et de leur location dont la maintenance et l'utilisation étaient fastidieuses.

C'est en voulant résoudre ce problème que Tim Berners-Lee, un scientifique anglais du Conseil Européen de la Recherche Nucléaire (CERN)
à Genève, a développé les technologies du Web entre 1989 et 1991. Celles-ci se sont rapidement développées après que le CERN les ait
gratuitement mises à disposition du public. Des centres de recherche, universités, entreprises (d'informatique et de média) et d'autres
organisations ont créé leur site web afin de pouvoir facilement diffuser des informations par ce canal. Ceci offrait un usage supplémentaire
de l'ordinateur dont les foyers se sont équipés massivement, diffusant ainsi l'accès à Internet au sein de la population américaine et européenne.

## Les technologies du Web

Le web repose sur trois technologies mises ensemble et qui permettent de naviguer dans une "toile" de documents.
La première, l'URL, spécifie un format permettant de spécifier la localisation d'un document. La seconde, le protocole HTTP,
permet de demander et de recevoir un document identifié par son URL. La troisième, le langage HTML, permet de décrire
le contenu d'un document (une page web) pouvant contenir des liens vers d'autres documents spécifiés par leur URL.  

Ces trois technologies sont rassemblées dans un *navigateur web*, un programme qui permet de

1. spécifier une page web à visiter en indiquant son URL, typiquement dans une barre de navigation
1. demander la page web au serveur correspondant et la réceptionner en utilisant le protocole HTTP
1. afficher le contenu de la page web (décrite au format HTML), y compris les liens cliquables permettant d'afficher d'autres pages web.

### URL

L'URL (*Uniform Resource Locator*) est une manière de spécifier la localisation d'un document disponible sur Internet.
Un exemple d'URL peut être par exemple "https://www.champignons.ch/fichiers/fr/contact.html".

Une URL comporte trop parties, qui sont les suivantes dans notre exemple |https|://www.champignons.ch|/fichiers/fr/contact.html|.  {itodo}`mettre en couleur les trois parties`
Autrement dit, une URL se compose généralement de la manière suivante:

*protocol*:*hôte*/*chemin*  

1. Le *protocole*, dans notre exemple `https`, indique le protocole utilisé pour avoir accès à la ressource. Pour le web, ce protocole est toujours `http`ou `https`, sa version sécurisée. Mais l'URL étant aussi utilisée en dehors du web, il y a d'autres protocoles possibles, par exemple `ftp` pour faire du transfert de fichier.

1. L'*hôte* spécifie la machine (ou le serveur) où aller chercher le fichier. Cela peut être un nom de domaine, mais également une adresse IP

1. Le *chemin* indique quel fichier on souhaite obtenir de la part du serveur. On part de la racine "/" (connue du serveur) et on descend dans l'arborescence selon les répertoires indiqués. Par exemple `/fichiers/fr/contact.html` est le fichier `contact.html` qui se trouve dans le répertoire  `fr` qui se trouve lui-même dans le répertoire `fichiers`.  {itodo}`ajouter une illustration`

Dans le protocole HTTP, si le chemin est un répertoire (et pas un fichier), le fichier par défaut index.html présent dans ce répertoire est envoyé par le serveur.

### HTTP

HTTP (acronyme de HyperText Transfer Protocol) est le protocole qui régit la manière dont un client web (par exemple le navigateur web de Alice) et un serveur web (par exemple le site www.champignons.ch) vont interagir l'un avec l'autre.

Par exemple si le client demande au serveur de lui envoyer la page web `accueil.html`, il lui enverra requête GET suivante:

`GET accueil.html HTTP/1.1`

ce qui signifie "envoie-moi la page accueil.html avec la version 1.1 du protocole HTTP". S'il trouve la page en question, le
serveur pourra alors envoyer la réponse suivante:

`HTTP/1.1 200 OK` suivie de diverses informations ainsi que la page web demandée. Le code `200 OK` indique que la requête peut
être honorée.

Si la page `accueil.html` n'existe pas, alors le serveur pourra l'indiquer au client en envoyant la réponse suivante:

`HTTP/1.1 404 Not Found`

Le navigateur web pourra alors afficher l'"erreur 404" au pour l'utilisateur.

```{figure} media/erreur404.png
---
width: 500
align: center
---
Le serveur retourne un message d'erreur s'affiche lorsqu'on demande une page qui n'existe pas. 
```

Il y a d'autres sortes de requêtes que le client peut envoyer au serveur, par exemple `POST`pour envoyer une information du client au serveur, utilisé par exemple lorsqu'on remplit un formulaire en ligne.

Si un utilisateur utilise le protocole HTTP pour surfer sur le web, une tierce personne qui a accès au trafic sur Internet peut savoir quelle page web a été visitée par cet utilisateur et ce que le serveur lui a envoyé comme information (par exemple des messages privés). C'est pourquoi on utilise généralement plutôt le protocole HTTPS qui encrypte les requêtes et réponses HTTP. Ainsi un observateur peut toujours savoir avec quel site on communique lorsqu'on surfe sur le web en regardant l'entête IP, mais ne pourra pas connaître les détails des pages demandées et transmises.

### HTML

HTML (HyperText Markup Language) est un langage de description des pages web. Il permet de spécifier le contenu et l'apparence d'une
page web afin que le navigateur web puisse l'afficher. Supposons par exemple que le site www.champignons.ch envoie à Alice une
page web contenant le nom d'un champignon ainsi qu'une photo de celui-ci. Une manière de décrire cette page avec le langage HTML serait la suivante:

```html
<html>
<body>
 <h1 style="color:red"> L’amanite tue-mouche </h1>
 <p> L’amanite tue-mouche est très belle mais très dangereuse ! </p>
 <img src="photo.jpg" height="250" />
</body>
</html>
```

Les éléments de cette page sont indiqués par des *balises* indiquées par des crochets pointus (`<>`) et peuvent être imbriqués les uns dans les autres. Ainsi la page (entre `<body>` et `</body>`) contient un titre (entre `<h1>` et `</h1>`) de couleur rouge, un paragraphe de texte (entre `<p>` et `</p>`) ainsi qu'une image (`<img>`) disponible dans le fichier `photo.jpg` et de hauteur 250 pixels. Cette page pourra ainsi être affichée de la manière suivante dans le navigateur web.

```{image} media/renduhtml.png
---
width: 300
align: center
---
```

La plupart des navigateurs web permettent de visualiser le *code  HTML* des pages visitées. Un aspect important de la création de sites web consiste à écrire du code HTML qui sera mis sur le serveur pour être transmis au visiteur du site web. Cela peut se faire en écrivant directement du code HTML dans un fichier texte, ou à l'aide d'un outil de création de sites web qui se charge d'écrire le code HTML selon les indications données par la personne concevant le site.

## Les évolutions du Web

### Le Web dynamique

Au début, les pages web étaient des fichiers HTML stockés sur les serveurs. C'est ce qu'on appelle le
web *statique*. Si les sites web statiques existent
toujours, par exemple modulo-info.ch, beaucoup de sites web sont dynamiques,
c'est-à-dire que le fichier HTML est généré par le site au moment où la requête est faite.
Cela permet de servir une page différente selon l'utilisateur ou selon les arguments de la requête qui
sont des indications supplémentaires ajoutée à la requête après l'URL.

```{micro}
Effectuer une recherche sur un navigateur web et consulter la barre de navigation. Quels sont les arguments de votre requête et pouvez-vous en comprendre la signification?
```

```{exercise}
Parmi les sites web suivants, lesquels ont besoin d'être dynamiques et lesquels peuvent se contenter de fournir un
contenu statique?

1. Un site d'achats en ligne
1. Un site indiquant les horaires d'ouverture et de fermeture d'un magasin. 
1. Un site de consultation du catalogue d'une bibliothèque
1. Un site de présentation d'une entreprise
1. Un site avec les documents d'un cours universitaire ou scolaire
1. Un site d'e-banking

Pour les sites qui peuvent être statiques, quelles possibilités supplémentaires pourraient être offertes par
un site dynamique. 
```

{itodo}`parler de javascript et du web dynamique côté client?`

### Le Web 2.0

Le web 2.0 fait référence à la tendance, initiée au débit des années 2000, de proposer des pages web permettant aux internautes
de contribuer du contenu, et pas uniquement de lire des fichiers comme c'était le cas jusqu'alors. Les blogs, forums, wikis, et les réseaux sociaux font
partie de ce développement qui voit exploser l'aspect participatif du web. Ce n'est en effet plus nécessaire de connaître la syntaxe HTML et d'avoir
son propre serveur pour mettre du contenu à disposition des internautes de la planète.

{itodo}`développer ?`
