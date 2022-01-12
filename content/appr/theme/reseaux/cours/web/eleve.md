# Le World Wide Web 
## Historique
Pendant ses première décennies (jusque dans le année 90), seuls les universitaires, les militaires, certaines entreprises
et une communauté d'enthousiastes (largement issue du mouvement hippie) utilisaient internet.
Les utilisations principales étaient le *chat* (par un terminal), la connection sur un ordinateur
à distance, l'email et le transfert de fichiers entre ordinateurs. 

Pour aller chercher un fichier se trouvant sur un autre ordinateur, il fallait savoir exactement
sur quelle machine celui-ci se trouvait et où il se situait dans cette machine. Il fallait donc
établir des listes de ressources et de leur location dont la maintenance et l'utilisation étaient fastidieuses.

C'est en voulant résoudre ce problème que Tim Berners-Lee, un scientifique anglais du Centre Européen de la Recherche Nucléaire (CERN)
à Genève, a développé les technologies du Web entre 1989 et 1991. Celles-ci se sont rapidement développées après que le CERN les ait
gratuitement mises à disposition du public. Des centres de recherche, universités, entreprises (d'informatique et de média) et d'autres
organisations ont créé leur site web afin de pouvoir facilement diffuser des informations par ce canal. Ceci offrait un usage supplémentaire
de l'ordinateur dont les foyers se sont équippés massivement, diffusant ainsi l'accès à Internet au sein de la population américaine et européenne. 

## Les technologies du Web
Le web repose sur trois technologies mises ensemble et qui permettent de naviguer dans une "toile" de documents. 
La première, l'URL, spécifie un format permettant de spécifier la localisation d'un document. La seconde, le protocole HTTP, 
permet de demander et de recevoir un document identifié par son URL. La troisième, le langage HTML, permet de décrire
le contenu d'un document (une page web) pouvant contenir des liens vers d'autres documents spécifiés par leur URL.  

Ces trois technologies sont rassemblées dans un *navigateur web*, un programme qui permet de
1. spécifier une page web à visiter en indiquant son URL, typiquement dans une barre de navigation
1. demander la page web au serveur correspondant et la réceptionner en utilisant le protocole HTTP
1. afficher le contenu de la page web (décrite au format HTML), y compris les liens cliquables permettant d'afficher d'autres pages web. 


### URL
L'URL (*Uniform Resource Locator*) est une manière de spécifier la localisation d'un document disponible sur Internet.
Une exemple d'URL peut être par exemple "https://www.champignons.ch/fichiers/fr/contact.html". 

Une URL comporte tros parties, qui sont les suivantes dans notre exemple |https|://www.champignons.ch|/fichiers/fr/contact.html|.  [mettre en couleur les trois parties]
Autrement dit, une URL se compose généralement de la manière suivante:

*protocol*:*domaine*/*chemin*

1. Le *protocole*, dans notre exemple `https`, indique le protocole utiliser pour avoir accès à la ressource. Pour le web, ce protocole est toujouts `http`ou `https`, sa version sécurisée. Mais l'URL étant aussi utilisée en dehors du web, il y a d'autres protocoles possibles, par exemple `ftp` pour faire du transfert de fichier. 

1. Le *domaine* spécifie la machine (ou le serveur) où aller chercher le fichier. Cela peut être un nom de domaine, mais également une adresse IP

1. Le *chemin* indique quel fichier on souhaite obtenir de la part du serveur. On part de la racine "/" (connue du serveur) et on descend dans l'arborescence selon répertoires indiqués. Par exemple `/fichiers/fr/contact.html` est le fichier `contact.html` qui se trouve dans le répertoire  `fr` qui se trouve lui-même dans le répertoire `fichiers`.  [Ajouter une illustration]. 

Dans le protocole HTTP, si le chemin est un répertoire (et pas un fichier), le fichier par défaut index.html présent dans ce répertoire est envoyé par le serveur. 



### HTTP
HTTP (*HyperText Transfer Protocol) est le protocole qui régit la manière dont un client web (par exemple le navigateur web de Alice) et un serveur web (par exemple le site www.champignons.ch) vont interagir l'un avec l'autre. 

Par exemple 

[Ajouter quelque chose sur l'erreur 404]


### HTML



