# Interopérabilité

Si Internet a connu un développement aussi remarquable, c'est aussi
grâce à certains choix techniques et de gouvernance qui ont permis de le
rendre accessible relativement facilement. Des personnes, organisations et
entreprises pouvaient ainsi participer à sa construction et son développement.

Certains de ces choix sont décrits ci-dessous. 

## Un modèle en couches

La communication sur internet se fait selon un pile de protocoles qui s'ajoutent les
uns aux autres tout en étant indépendant les uns par rapport aux autres selon un
*modèle en couches*. Ainsi, le protocole HTTP est responsable de l'échange de pages web,
mais toute la partie s'assurant du bon transfert et de la bonne réception des paquets est
gérée par le protocole TCP.
Mais ce protocole repose sur le protocole IP pour l'envoi des paquets indidivduels qui
lui-même repose sur différents protocoles selon que les paquet circule par le wifi, un cable
sous-marin, de la 4G ou de la fibre optique. Ainsi les niveaux supérieurs peuvent s'abstraire
des niveaux inférieurs, et vice-versa. Si un nouveau support physique de communication est
inventé (par exemple la téléportation quantique), il suffit de développer un protocole de
communication propre à ce support et on pourra utiliser le protocole IP pour la transmission
de paquets, ce qui permettra à ce nouveau support de s'intégrer sans difficulté à Internet. 

On a ainsi définit le modèle suivant en 4 "couches" de protocoles: La première couche "data link"
définit comment les données sont transmises entre deux appareils directement connectés. Le protocole
en question dépends donc du type de connnexion entre les deux appareils
(wifi, cable électrique, fibre optique, etc.). La deuxième couche, "internet", définit comment les données
sont transmises entre deux machines du réseau, c'est le protocole IP vu précédemment. La troisiène couche "transport", définit comment les données sont segmentées (c'est-à-dire découpée et morceaux) et envoyées par l'émetteur
et reconstituées et quittancée par le recepteur, c'est le protocole TCP également vu précédemment. La quatrième couche est la couche applicative qui définit comment deux appplications (ou programmes) communiquent entre elles, par exemple le protocole HTTP qui détermine la communication entre un navigateur web et un serveur web. D'autres exemples figurant dans cette couche pourraient inclure la manière dont l'application TikTok
d'un smartphone communique avec le serveur de TikTok.

Ce modèle en 4 couches a été ensuite développé en un modèle en 7 couches dans lequel a été ajoutée au plus bas
niveau une "couche physique" qui décrit les caractéristiques physiques utilisée pour la connection
(voltage, fréquences, etc.). Juste en dessous de la couche applicative, deux couches de protocoles
on été insérée. La "couche de session" qui gère les sessions, par exemple lorsqu'on lance une application sur
son smartphone, celle-ci va ouvrir une session avec le serveur. Enfin la "couche de présentation" gère les
questions de compression et d'encryptage des données. Le modéle résultant, appelé OSI, est illustré ci-dessous.


[Ajouter une figure]

[Ajouter l'exemple complet d'Alice]


## Des protocoles ouverts et négociés
Les protocoles décrits ci-dessus ont été établis sur proposition de différentes personnes travaillant
principalement dans les universités ou les entreprises de télécommunication et adoptés par consensus après
beaucoup de discussion. L'idée principale étant qu'internet n'appartient à personne et qu'il s'agit d'une
oeuvre collective à laquelle toute personne dotée des compétences nécessaires peut contribuer. Ces protocoles
sont *ouverts* dans le sens que chacun peut y avoir accès et les implémenter à sa manière. Par exemple,
quelqu'un qui souhaiterait développer un routeur peut avoir accès à toutes les informations nécessaires
pour le faire.

La collaboration autour de la définition des protocoles d'internet est structurée autour l'Internet Society,
une association à but non lucratif dont le but est le développement d'Internet. L'Internet
Engineering Task Force et un groupe de personnes qui discutent des aspects techniques d'Internet. Ce groupe
est (théoriquement) ouvert à toute personne qui souhaite s'y impliquer. Les discussions s'articulent autour
de "Requests For Comments" (RFC) qui sont des documents publics qui proposent des idées qui sont discutées,
et, pour certaines d'entre elles, adoptées par consensus.
Le premier RFC, RFC1 a été formulé en 1969 pour proposer
un protocole de communication sur Arpanet, le projet de recherche militaire américain qui a donné naissance à
Internet. Toutes les technologies d'Internet décrites ci-dessus ont été proposée par le biais de RFC, par exemple IPv4, RIP, HTML, etc.  


Exercice: Chercher et lire le RFC 8962, en particulier l'abstract et les parties 7. et 8. De quoi s'agit-il?


## La neutralité d'Internet

## L'universalité et la décentralisation d'Internet en question

Avec la montée en puissance des entreprises privées, une partie de l'ouverture qui caractérisait les débuts
d'Internet est remise en question. Ainsi, les entreprises qui ont développé les réseaux sociaux l'ont fait
en utilisant des protocoles fermés (ou privés). Par exemple, le protocole par lequel
l'application Whatsapp communique avec le serveur est gardée secrète. Ceci permet d'empêcher que d'autres
personnes ne développent des application compatibles avec Whatsapp et y fassent ainsi concurrence. Pour
illustrer la différence avec un protocole ouvert (ou public), on peut comparer Whatsapp (protocole fermé) avec
l'email qui repose sur un protocole ouvert (SMTP). Le fait que le protocole de l'email soit public permet à
toute personne qui en a les capacités d'offrir un service d'email. (Certaines personnes installent ainsi
leur propre serveur email hébergé sur leur ordinateur.) Tous ces services d'email différents, qui peuvent être
commerciaux, privés, ou artisanaux, sont compatibles les uns avec les autres car ils suivent le même protocole
SMTP. Ceci est très différent de Whatsapp qui ne peut être utilisé qu'avec l'application Whatsapp et donc tous
les messages Whatsapp sont centralisés chez une seule entreprise. On observe certaines tentatives de créer des
réseaux sociaux sur des protocoles ouverts, par exemple Mastodon pour le micro-blogging, PeerTube pour la vidéo,
ou diaspora, mais leur succès reste limité, notamment car elles n'ont pas les ressources financières qui leur
permettraient de rivaliser avec leur concurrentes à visée lucrative.

Une autre tendance qui remet en question la décentralité du web est le développement du cloud. 


Enfin, si internet donnait à ses début une impression d'unversalité, on s'est rendu compte que l'utilisation des
caractères ASCII, la syntaxe d'HTML et de l'URL étaient peu propices aux alphabets non latin, et qui ne
s'écrivent pas de gauche à droite. Tout choix "technique" est ancré dans un contexte social et culturel...


