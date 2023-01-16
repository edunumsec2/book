# Paquets et protocoles

(ou comment envoyer de l'information)

## Les paquets

Dès leur origine, les systèmes de communication se sont développés selon deux modes distincts selon les supports utilisés. Soit on maintient un "canal de communication" ouvert par exemple avec le téléphone ou la communication radio (le talkie-walkie). Dans ce cas, le récepteur et l'émetteur entrent en communication et l'information est envoyée de manière continue de l'émetteur au récepteur. Le récepteur ne peut pas être en communication avec plusieurs émetteurs à la fois.
Dans le second cas de figure, par exemple le courrier postal ou le télégramme, les informations sont envoyées "en bloc", typiquement par messages acheminés en une fois. Dans ce cas, le récepteur peut recevoir des messages de différentes personnes de manière presque simultanée, et le fait d'envoyer un message à quelqu'un ne va pas empêcher quelqu'un d'autre d'entrer en communication et nous envoyer des messages.

Afin d'éviter de bloquer les lignes de communication, Internet s'est développé selon ce second mode, et c'est pourquoi il était justifié d'évoquer ci-dessus
des *messages* qui étaient envoyés et circulaient dans le réseau. En effet, toute information envoyée par Internet est découpée en petits.
*paquets* qui sont envoyés indépendamment les uns des autres. Ainsi, lorsque le serveur hébergeant le
site www.champignons.ch va envoyer
une image de champignon à Alice, cette image sera découpée en petits paquets qui seront chacun envoyés séparément à
Alice. Cela a l'avantage qui si, pour une raison ou une autre, une partie de l'image se perd en route, il n'y a pas besoin de renvoyer toute l'image, mais uniquement les parties qui se sont perdues. Cela permet aussi à une machine de maintenir plusieurs canaux de communications ouverts simultanément. C'est ce qu'on appelle la *commutation par paquets* parce que ce sont les paquets qui sont adressés individuellement à leur destinataire. À l'inverse, dans le cas du téléphone traditionnel, lorsqu'on appelle quelqu'un, un circuit électrique est établi entre les deux téléphones pour leur permettre de communiquer (à l'exclusion des autres téléphones), c'est ce qu'on appelle la *commutation de circuits*.

Les protocoles IP (Internet Protocol) et TCP (Transmission Control Protocol) décrivent le format ainsi que la gestion
possible de ces paquets.

{itodo}`[ajouter illustrations] `

## Le protocole IP

L'envoi d'un paquet par la poste suit certaines règles, telles que la position et le format de l'adresse de destination, la position et le format de l'adresse d'expédition, la position du timbre et son montant en fonction du poids et de la destination. Sans ces règles, l'acheminement du paquet ne peut pas être assuré. De manière analogue l'envoi d'un paquet sur Internet doit suivre certaines règles pour être acheminé. C'est le protocole IP qui définit ces règles.

Selon ce protocole un paquet est constitué d'une suite de 0 et de 1 que l'on peut séparer en deux parties.

1. L'entête qui donne des informations sur le paquet (son émetteur, sa destination, sa taille, etc.)
1. Les données qui forment le contenu du paquet, c'est-à-dire les informations que l'on veut transmettre.

```{figure} media/IPpacket.svg
:width: 500
```
L'entête joue le rôle de l'étiquette sur un paquet envoyé par la poste. On y indique l'adresse de destination, l'adresse de
l'expéditeur (appelée aussi l'adresse source), mais aussi d'autres information telles que la version d'IP utilisée (4 ou 6),
la longueur totale du paquet, ainsi que sa "durée de vie". Sa durée de vie indique au bout de combien de temps le paquer peut
être abandonné pour éviter d'avoir des paquets qui circulent indéfiniment sans trouver leur destinataire. Dans la version IPv4,
l'entête fait au maximum 24 octets, remplis comme dans l'image ci-dessous.

```{figure} media/IPv4header.png
:width: 700
```
On remarque que les 4 premiers bits indiquent la version de d'IP utilisée (donc 0100 si c'est la version 4), les quatre suivants
donnent la longueur de l'entête, etc. 


## Le protocole TCP

Contrairement à une lettre dans laquelle on peut écrire tant qu'on veut, un paquet IP a une taille maximale fixe, est donc on sera parfois obligé de
découper une information (par exemple une image ou une vidéo) en plusieurs paquets IP afin de l'envoyer. Le récepteur doit ensuite reconstruire l'information
à partir des paquets reçus et confirmer qu'il a bien tout reçu et que rien n'a été perdu en route (ce qui arrive parfois, comme avec la poste). Le protocole
TCP (Transmission Control Protocol) permet aux machines réceptrice et émettrice de s'assurer que l'information a bien été transmise et reconstituée.

Pour ceci, l'information est découpée en morceaux de taille inférieure à la taille maximale des paquets IP, et chaque morceau est numéroté (avec des nombres consécutifs) et envoyé dans un paquet IP. La machine réceptrice sait ainsi comment reconstituer l'information et peut vérifier qu'il ne lui manque pas de
morceaux.

### En-tête

De manière similaire au protocole IP, le protocole TCP est constitué d'un *en-tête* placé au début des données du paquet IP et qui contient des informations
sur les numéros de morceaux envoyés et reçus. En effet, la machine réceptrice va envoyer une quittance (*acknowledgement* en anglais) pour chaque paquet reçu,
de manière à ce que la machine émettrice puisse renvoyer un paquet qui n'aurait pas été acheminé à destination. 


```{figure} media/IPTCPpacket.svg
:width: 500
```

L'en-tête TCP est constitué aussi de 24 octets contenant les informations suivantes:

```{figure} media/TCPheader.png
:width: 700
```

Comme le montre la figure ci-dessus, les quatre premiers octets
contiennent les ports source et de destination. Un port est un peu comme une
boîte aux lettres à l'intérieur d'un ordinateur. Le ports sont numérotés sur 16
bits, donc de 0 à $2^16-1$. Un ordinateur qui est en connexion simultanée avec
plusieurs ordinateurs pourra par exemple assigner un port différent à chaque
connnexion, ce qui lui permettra de ne pas mélanger les messages reçus de ses
divers interlocuteurs. Dans ce contexte et contrairement à un port USB, un port
n'a pas de réalité matérielle, il est réalisé de manière logicielle par le
système d'exploitation.

Les quatre octets suivants contiennent le numéro de séquence qui va permettre
au programme qui recoit les paquets de les remettre dans l'ordre selon ce
numéro. La numéro d'aquittement permet au destinataire de renvoyer un paquet
pour indiquer quel sont les
paquets qui ont été reçus, permettant ainsi à la machine émetrice de quels
paquets se sont perdus en chemin et doivent être envoyés à nouveau. Les quatres
octets suivants contiennent divers éléments permettant aux deux machines en
communication de se synchroniser, notamment divers fanions indiquant si on veut
initier, ou terminer la connexion, ainsi que "Fenêtre" par quoi le récepteur
indique à l'émetteur combien de place il lui reste dans la pile des paquets à
trier et traiter. Ceci permet à l'émetteur d'adapter la rythme auquel il
envoie les paquets pour ne pas déborder le récepteur. Enfin la "Somme de
contrôle" est un code correcteur d'erreur qui permet de vérifier si l'en-tête
n'a pas été altérée en chemin.

```{exercise}
Un paquet a été intercepté sur Internet avec le contenu initial suivant
indiqué en hexadécimal:



1. Déterminer quelle partie de cette en-tête correspond à l'en-tête IP,
et laquelle correspond à l'en-tête TCP.
1. Indiquer l'adresse IP et le port de l'émetteur de ce paquet.
1. Indiquer l'adresse IP et le port du destinataire de ce paquet.
1. Combien d'octets du paquet ne sont pas représentés ci-dessus?

```




### Déroulement

Le protocole TCP applique une structure {glo}`clientserveur|client-serveur` à
communication entre deux machines. Cela signifie qu'une des machines, appelée
le serveur, va se mettre en mode d'écoute, et attendre que d'autres machines la
contactent. C'est la machine cliente qui va prendre l'initiative d'initier la
communication en envoyant un message TCP (juste l'entête, sans les données)
à la machine serveur. Le protocole TCP spécifie les messages qui doivent être
envoyés de part et d'autre pour initier la connection, comment ensuite
envoyer et quittancer les données échangées, et comment mettre fin et terminer
la connexion une fois que tout a été envoyé et quittancé.

La figure ci-dessous indique comment les fanion SYN, FIN sont utilisés pour
indiquer que l'on veut respectivement initier et terminer une connexion, et comment
le fanion ACK est utiliser pour confirmer la bonne réception de la demande ou des
données, avec les numéros des séquences (#seq) et et d'acquittement (#ack). 


```{figure} media/TCPprot.svg
:width: 800
```