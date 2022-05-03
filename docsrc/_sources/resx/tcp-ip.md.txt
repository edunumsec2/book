# Paquets et protocoles
(ou comment envoyer de l'information)
## Les paquets
Dès leur origine, les systèmes de communication se sont développés selon deux modes distincts selon les supports utilisés. Soit on maintient un "canal de communication" ouvert par exemple avec le téléphone ou la communication radio (le talkie-walkie). Dans ce cas, le récepteur et l'émetteur entrent en communication et l'information est envoyées de manière continue de l'émetteur au récepteur. Le récepteur ne peut pas être en communication avec plusieurs émetteurs à la fois. 
Dans le second cas de figure, par exemple le courrier postal ou le télégramme, les informations sont envoyées "en bloc", typiquement par messages acheminés en une fois. Dans ce cas, le récepteur peut recevoir des messages de différentes personnes de manière presque simultanée, et le fait d'envoyer un message à quelqu'un ne va pas empêcher quelqu'un d'autre d'entrer en communication et nous envoyer des messages. 

Afin d'éviter de bloquer les lignes de communication, Internet s'est développé selon ce second mode, et c'est pourquoi il était justifié d'évoquer ci-dessus
des *messages* qui étaient envoyés et circulaient dans le réseau. En effet, toute information envoyée par internet est découpée en petits
*paquets* qui sont envoyés indépendamment les uns des autres. Ainsi, lorsque le serveur hébergeant le
site www.champignons.ch va envoyer
une image de champignon à Alice, cette image sera découpé en petits paquets qui seront chacuns envoyés séparément à
Alice. Cela a l'avantage qui si, pour une raison ou une autre, une partie de l'image se perd en route, il n'y a pas besoin de renvoyer toute l'image mais uniquement les parties qui se sont perdues. Cela permet aussi à une machine de maintenir plusieurs canaux de communications ouverts simultanément. C'est ce qu'on appelle la *commutation par paquets* parce que ce sont les paquets qui sont adressés individuellement à leur destinataire. A l'inverse, dans le cas du téléphone traditionnel, lorsqu'on appelle quelqu'un, un circuit électrique est établi entre les deux téléphones pour leur permettre de communiquer (à l'exclusion des autres téléphones), c'est ce qu'on appelle la *commutation de circuit*.

Les protocoles IP (Internet Protocol) et TCP (Transmission Control Protocol) décrivent le format ainsi que la gestion
possible de ces paquets. 



## Le protocole IP
L'envoi d'un paquet par la poste suit certaines règles, telles que la position et le format de l'adresse de destination, la position et le format de l'adresse d'expédition, la position du timbre et son montant en fonction du poids et de la destination. Sans ces règles, l'acheminement du paquet ne peut pas être assuré. De manière analogue l'envoi d'un paquet sur internet doit suivre certaines règles pour être acheminé. C'est le protocole IP qui définit ces règles.

Selon ce protocole un paquet est constitué d'une suite de 0 et de 1 que l'on peut séparer en deux parties. 
1. L'entête qui donne des informations sur le paquet (son émetteur, sa destination, sa taille, etc.)
1. Les données qui forment le contenu du paquet, c'est-à-dire les informations que l'on veut transmettre. 

[ indiquer la spécification de l'entête IP]


## Le protocole TCP
Contrairement à une lettre dans laquelle on peut écrire tant qu'on veut, un paquet IP a une taille maximale fixe, est donc on sera parfois obligé de
découper une information (par exemple une image ou une vidéo) en plusieurs paquets IP afin de l'envoyer. Le récepteur doit ensuite reconstruire l'information
à partir des paquets reçus et confirmer qu'il a bien tout reçu et que rien n'a été perdu en route (ce qui arrive parfois, comme avec la poste). Le protocle
TCP (Transmission Control Protocol) permet aux machines réceptrice et émettrice de s'assurer que l'information a bien été transmise et reconstituée. 

Pour ceci, l'information est découpées en morceaux de taille inférieure à la taille maximale des paquets IP, et chaque morceau est numéroté (avec des nombres consécutifs) et envoyé dans un paquet IP. La machine réceptrice sait ainsi comment reconstituer l'information et peut vérifier qu'il ne lui manque pas de
morceaux

De manière similaire au protocol IP, le protocole TCP est constitué d'un *en-tête* placé au début des données du paquet IP et qui contient des informations
sur les numéros de morceaux envoyés et reçus. En effet, la machine réceptrice va envoyer une quittance (*acknowledgement* en anglais) pour chaque paquet reçu,
de manière à ce que la machine émettrice puisse renvoyer un paquet qui n'aurait pas été acheminé à destination. 

[donner le détail du protocole et le format de l'en-tête]
