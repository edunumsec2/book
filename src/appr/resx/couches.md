# Interopérabilité

Si Internet a connu un développement aussi remarquable, c'est aussi
grâce à certains choix techniques et de gouvernance qui ont permis de le
rendre accessible relativement facilement. Des personnes, organisations et
entreprises pouvaient ainsi participer à sa construction et son développement.

Certains de ces choix sont décrits ci-dessous.

## Un modèle en couches

La communication sur Internet se fait selon une pile de protocoles qui s'ajoutent les
uns aux autres tout en étant indépendant les uns par rapport aux autres selon un
*modèle en couches*. Ainsi, le protocole HTTP est responsable de l'échange de pages web,
mais toute la partie s'assurant du bon transfert et de la bonne réception des paquets est
gérée par le protocole TCP.
Mais ce protocole repose sur le protocole IP pour l'envoi des paquets indidivduels qui
lui-même repose sur différents protocoles selon que les paquets circulent par le wifi, un câble
sous-marin, la 4G ou de la fibre optique. Ainsi les niveaux supérieurs peuvent s'abstraire
des niveaux inférieurs, et vice-versa. Si un nouveau support physique de communication est
inventé (par exemple la téléportation quantique), il suffit de développer un protocole de
communication propre à ce support et on pourra utiliser le protocole IP pour la transmission
de paquets, ce qui permettra à ce nouveau support de s'intégrer sans difficulté à Internet.

On a ainsi défini le modèle de la {numref}`figcouches` en 4 "couches" de protocoles: la première couche "liaison réseau"
définit comment les données sont transmises entre deux appareils directement connectés ou du même réseau local. Le protocole
en question dépend donc du type de connexion entre les deux appareils
(wifi, câble électrique, fibre optique, etc.). La deuxième couche, "Internet", définit comment les données
sont transmises entre deux machines du réseau, c'est le protocole IP vu précédemment. La troisième couche "transport" définit comment les données sont segmentées (c'est-à-dire découpée et morceaux) et envoyées par l'émetteur
et reconstituées et quittancées par le récepteur, c'est le protocole TCP également vu précédemment. La quatrième couche est la couche applicative qui définit comment deux applications (ou programmes) communiquent entre elles, par exemple le protocole HTTP qui détermine la communication entre un navigateur web et un serveur web. D'autres exemples figurant dans cette couche pourraient inclure la manière dont l'application TikTok
d'un smartphone communique avec le serveur de TikTok.


Ainsi, lorsque le navigateur web d'Alice demande une page au serveur web, ces deux applications (le navigateur et le serveur)
sont en communication en utilisant le protocole HTTP. Pour transmettre la requête HTTP d'Alice, une connexion entre Alice
et le serveur web sera établie en utilisant le procole TCP. Au besoin, ce protocole découpera la requête ou la page web en
petits morceaux et ajoutera les entêtes TCP à chaque morceau, qui sera envoyé individuellement en utilisant le protocole IP (en ajoutant y donc l'entête IP). Selon le type de connexion, (4G, wifi, cable), les paquets IP seront transmis selon différents protocoles à des routeurs qui les achemineront jusqu'au destinataire qui réassemblera les paquets selon le protocole TCP et fournira la requête HTTP d'Alice au serveur web ou la page web demandés au navigateur d'Alice. 

```{figure} media/couches_tcpip.svg
---
name: figcouches
width: 600
align: center
---
Gauche: le modèle en 4 couches de la communication par Internet. Droite: Exemple de l'application de ce modèle à la communication
entre le navigateur web d'Alice et un serveur web. Lorsque les applications veulent s'échanger de l'information, cet échange se fait
selon un protocle de la couche "Application" par exemple HTTP. La requête ou la page web ainsi formées (représentés par le rectangle
vert) sont ensuite traitées par le protcole TCP de la couche "Transport" qui va découper ces données en petits paquets, y ajouter une
entête TCP numérotée (en bleu ciel) et
envoyés à leur destinataire par le protocole IP de la couche "Internet". Avec ce protocole, une seconde entête (représentées en bleu
foncé) est ajoutée à chaque paquet qui est envoyé sur le réseau par un protocole propre au type de réseau utilisé (en y ajoutant
encore une entête mauve). L'information ne passera d'habitude pas directement d' Alice au serveur web, mais par des routeurs qui
achemineront les paquets IP jusqu'à leur destination, en utilisant les différents protocoles de la couche d'accès réseau selon les
besoins. 

```


Ce modèle en 4 couches a été ensuite développé en un modèle en 7 couches appelé OSI (pour *Open System Interconnection*).
Dans ce modèle, la couche d'accès réseau est séparée en
deux couches, la couche physique qui décrit comment le signal est codé dans un médium donné (fibre optique, onde électromagnétique, etc.)
et la couche de liaison qui indique comment un groupe de bits (appelé une trame) est envoyé au sein un réseau local (par exemple le wifi,
ou un réseau ethernet). Ce modèle ajoute deux couches à la couche "Application", la couche de présentation qui spécifique comment
les données sont encodées (par exemple avec la table ASCII) et potentiellement encryptées, et la couche "Session" qui gère les questions
d'authentification et d'autorisation, par exemple lorsque vous vous connectez à un service payant sur le web. 

```{figure} media/couches_osi.svg
---
width: 200
align: center
---
Le modèle (TCP-IP) en quatre couches et, à sa droite, le modèle OSI en sept couches. La couche "Application" a été séparée en
trois couches, et la couches "Accès réseau" a été séparée en deux couches. 

```

Le modèle OSI indique la manière dont les choses devraient se passer pour garantir à la fois la sécurité et la modularité des
communications, mais il n'est dans la pratique pas toujours entièrement respecté, en particulier pour les couches supérieures. 



## Des protocoles ouverts

Les protocoles décrits ci-dessus ont été établis sur proposition de différentes personnes travaillant
principalement dans les universités ou les entreprises de télécommunication et adoptés par consensus après
beaucoup de discussion. L'idée principale étant qu'Internet n'appartient à personne et qu'il s'agit d'une
œuvre collective à laquelle toute personne dotée des compétences nécessaires peut contribuer. Ces protocoles
sont *ouverts* dans le sens que chacun peut y avoir accès et les implémenter à sa manière. Par exemple,
quelqu'un qui souhaiterait développer un routeur peut avoir accès à toutes les informations nécessaires
pour le faire.

La collaboration autour de la définition des protocoles d'Internet est structurée autour l'Internet Society,
une association à but non lucratif dont le but est le développement d'Internet. L'Internet
Engineering Task Force et un groupe de personnes qui discutent des aspects techniques d'Internet. Ce groupe
est (théoriquement) ouvert à toute personne qui souhaite s'y impliquer. Les discussions s'articulent autour
de "Requests For Comments" (RFC) qui sont des documents publics qui proposent des idées qui sont discutées,
et, pour certaines d'entre elles, adoptées par consensus.
Le premier RFC, RFC1 a été formulé en 1969 pour proposer
un protocole de communication sur ARPANET, le projet de recherche militaire américain qui a donné naissance à
Internet. Toutes les technologies d'Internet décrites ci-dessus ont été proposées par le biais de RFC, par exemple IPv4, RIP, HTML, etc.  

```{micro} 
Chercher et lire le RFC 8962, en particulier l'abstract et les parties 7 et 8, ainsi que la date. De quoi s'agit-il?
````

## La neutralité d'Internet

Un des principes fondateurs d'internet est sa *neutralité*. Cela signifie que les paquets IP sont acheminés vers leur
destination sans discrimination de source, de destination ou de contenu. Contrairement à la poste suisse, où certains courriers
(par exemple le courrier A) sont prioritaires par rapport à d'autres, les paquets IP sont tous logés à la même enseigne sur Internet.
Cela permet d'éviter que certains services (par exemple un site web) puissent payer plus cher pour que ses paquets arrivent plus rapidement
chez leurs destinataires et offrir ainsi un service plus rapide au détriment d'autres services. Certains acteurs, tels que les fournisseurs
d'accès à Internet se sont opposés à la neutralité du net, car cela leur aurait permis de mettre leurs clients en concurrence sur les débits
fournis et ainsi augmenter leurs tarifs et donc leurs bénéfices. Ou alors, il leur serait possible de privilégier l'acheminement des
paquets liés à leurs propres services (par exemple Swisscom, pourrait privilégier l'acheminement des paquets liés à son service de télévision
au détriment d'autres chaînes.)

Le respect de la neutralité d'Internet est différent de pays en pays, certains, comme la Suisse l'ayant inscrite dans la loi.

```{micro}
Lire [ l'article 12e](https://www.fedlex.admin.ch/eli/cc/1997/2187_2187_2187/fr#art_12_e) de la loi fédérale sur les télécommunications qui concerne la neutralité d'Internet. Quel alinéa garantit la neutralité du réseau? Cette garantie est-elle absolue? 
````

## L'universalité d'Internet en question

Avec la montée en puissance des entreprises privées, une partie de l'ouverture qui caractérisait les débuts
d'Internet est remise en question. Ainsi, les entreprises qui ont développé les réseaux sociaux l'ont fait
en utilisant des protocoles fermés (ou privés). Par exemple, le protocole par lequel
l'application Whatsapp communique avec le serveur est gardé secret. Ceci permet d'empêcher que d'autres
personnes ne développent des applications compatibles avec Whatsapp et y fassent ainsi concurrence. Pour
illustrer la différence avec un protocole ouvert (ou public), on peut comparer Whatsapp (protocole fermé) avec
l'email qui repose sur un protocole ouvert (SMTP). Le fait que le protocole de l'email soit public permet à
toute personne qui en a les capacités d'offrir un service d'email. (Certaines personnes installent ainsi
leur propre serveur email hébergé sur leur ordinateur.) Tous ces services d'email différents, qui peuvent être
commerciaux, privés, ou artisanaux, sont compatibles les uns avec les autres, car ils suivent le même protocole
SMTP. Ceci est très différent de Whatsapp qui ne peut être utilisé qu'avec l'application Whatsapp et donc tous
les messages Whatsapp sont centralisés chez une seule entreprise. On observe certaines tentatives de créer des
réseaux sociaux sur des protocoles ouverts, par exemple Mastodon pour le microblogging, PeerTube pour la vidéo,
ou diaspora, mais leur succès reste limité, notamment car elles n'ont pas les ressources financières qui leur
permettraient de rivaliser avec leurs concurrentes à visée lucrative.

Une autre tendance qui remet en question la décentralité d'Internet est le développement du cloud. Avec les services
de cloud, les documents, les données et les sites web se concentrent dans les serveurs des entreprises offrant ces services.
Ainsi, si une panne affecte un de ces services offerts par Google ou Microsoft, ou si la sécurité d'un tel service est
compromise, les répercussions seront globales.

Enfin, si Internet donnait à ses débuts une impression d'universalité, on s'est rendu compte que l'utilisation des
caractères ASCII, la syntaxe de HTML et de l'URL étaient peu propices aux alphabets non latins, et qui ne
s'écrivent pas de gauche à droite. Tout choix "technique" est ancré dans un contexte social et culturel duquel il
est difficile de faire abstraction. Des inititatives pour rendre Internet plus universel ont été prises, comme le fait
de pouvoir entrer des URL en caractères chinois. Il n'en reste pas moins que les structures qui gèrent Internet restent
des entités de droit américain, et que l'occident garde une place prépondérante dans le façonnage d'Internet. Certains
états plus autoritaires, tels que la Chine ou la Russie, souhaitent avoir un contrôle plus strict de ce que leur population
font sur Internet et tentent de filtrer certains contenus. A terme, il n'est pas exclu que se développent plusieur réseaux
en parallèle avec des politiques d'ouverture très différentes. 
