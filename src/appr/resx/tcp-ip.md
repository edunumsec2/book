# Paquets et protocoles

Dans la commutation par paquets les données à transmettre sont découpées en petits morceaux appelés paquets. Ces paquets sont composés d'un en-tête et d'une charge utile.  
L'en-tête est utilisé par le réseau pour diriger le paquet vers sa destination. La charge utile transporte l'information à transmettre.
Le contenu des entêtes ainsi que son interprétation font partie du protocole de transmission.
## Les paquets

Dès leur origine, les systèmes de communication se sont développés selon deux modes distincts selon les supports utilisés. Soit on maintient un "canal de communication" ouvert par exemple avec le téléphone ou la communication radio (le talkie-walkie). Dans ce cas, le récepteur et l'émetteur entrent en communication et l'information est envoyée de manière continue de l'émetteur au récepteur. Le récepteur ne peut pas être en communication avec plusieurs émetteurs à la fois.
Dans le second cas de figure, par exemple le courrier postal ou le télégramme, les informations sont envoyées "en bloc", typiquement par messages acheminés en une fois. Dans ce cas, le récepteur peut recevoir des messages de différentes personnes de manière presque simultanée, et le fait d'envoyer un message à quelqu'un ne va pas empêcher quelqu'un d'autre d'entrer en communication et nous envoyer des messages.

Afin d'éviter de bloquer les lignes de communication, Internet s'est développé selon ce second mode, et c'est pourquoi il était justifié d'évoquer ci-dessus
des *messages* qui étaient envoyés et circulaient dans le réseau. En effet, toute information envoyée par Internet est découpée en petits *paquets* qui sont envoyés indépendamment les uns des autres. Ainsi, lorsque le serveur hébergeant le
site www.champignons.ch va envoyer
une image de champignon à Alice, cette image sera découpée en petits paquets qui seront chacun envoyés séparément à
Alice. Cela a l'avantage qui si, pour une raison ou une autre, une partie de l'image se perd en route, il n'y a pas besoin de renvoyer toute l'image, mais uniquement les parties qui se sont perdues. Cela permet aussi à une machine de maintenir plusieurs canaux de communications ouverts simultanément. C'est ce qu'on appelle la *commutation par paquets* parce que ce sont les paquets qui sont adressés individuellement à leur destinataire. À l'inverse, dans le cas du téléphone traditionnel, lorsqu'on appelle quelqu'un, un circuit électrique est établi entre les deux téléphones pour leur permettre de communiquer (à l'exclusion des autres téléphones), c'est ce qu'on appelle la *commutation de circuits*.

```{figure} media/packets.svg
---
width: 500
align: center
---
Les données envoyées de Alice à champignons.ch sont découpées en petits paquets (représentés par des carrés orange). Cela permet de partager les lignes avec d'autres utilisateurs et utilisatrices tels que Anna et Tom qui communiquent
également en s'envoyant des paquets (représentés par des triangles jaunes). On peut noter que ces paquets ne prennent pas tous forcément le même chemin pour arriver à destination.
```

Les protocoles IP (Internet Protocol) et TCP (Transmission Control Protocol) décrivent le format ainsi que la gestion
possible de ces paquets.

## Le protocole IP

L'envoi d'un paquet par la poste suit certaines règles, telles que la position et le format de l'adresse de destination, la position et le format de l'adresse d'expédition, la position du timbre et son montant en fonction du poids et de la destination. Sans ces règles, l'acheminement du paquet ne peut pas être assuré. De manière analogue l'envoi d'un paquet sur Internet doit suivre certaines règles pour être acheminé. C'est le protocole IP qui définit ces règles.

Selon ce protocole un paquet est constitué d'une suite de 0 et de 1 que l'on peut séparer en deux parties.

1. L'entête qui donne des informations sur le paquet (son émetteur, sa destination, sa taille, etc.)
1. Les données qui forment le contenu du paquet, c'est-à-dire les informations que l'on veut transmettre.

```{image} media/IPpacket.svg
:width: 500
:align: center
```

L'entête joue le rôle de l'étiquette sur un paquet envoyé par la poste. On y indique l'adresse de destination, l'adresse de
l'expéditeur (appelée aussi l'adresse source), mais aussi d'autres informations telles que la version d'IP utilisée (4 ou 6),
la longueur totale du paquet, ainsi que sa "durée de vie". Sa durée de vie indique au bout de combien de temps le paquet peut
être abandonné pour éviter d'avoir des paquets qui circulent indéfiniment sans trouver leur destinataire. Dans la version IPv4,
l'entête fait au maximum 24 octets, remplis comme dans l'image ci-dessous.

```{figure} media/IPv4header.png
:width: 700
```

On remarque que les 4 premiers bits indiquent la version d'IP utilisée (donc 0100 si c'est la version 4), les quatre suivants
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

```{image} media/IPTCPpacket.svg
:width: 500
:align: center
```

L'en-tête TCP est constitué aussi de 24 octets contenant les informations suivantes:

```{image} media/TCPheader.png
:width: 700
:align: center
```

Comme le montre la figure ci-dessus, les quatre premiers octets
contiennent les ports source et de destination. Un port est un peu comme une
boîte aux lettres à l'intérieur d'un ordinateur. Les ports sont numérotés sur 16
bits, donc de 0 à $2^{16}-1$. Un ordinateur qui est en connexion simultanée avec
plusieurs ordinateurs pourra par exemple assigner un port différent à chaque
connexion, ce qui lui permettra de ne pas mélanger les messages reçus de ses
divers interlocuteurs. Dans ce contexte et contrairement à un port USB, un port
n'a pas de réalité matérielle, il est réalisé de manière logicielle par le
système d'exploitation.

Les quatre octets suivants contiennent le numéro de séquence qui va permettre
au programme qui reçoit les paquets de les remettre dans l'ordre selon ce
numéro. Le numéro d'acquittement permet au destinataire de renvoyer un paquet
pour indiquer quels sont les
paquets qui ont été reçus, permettant ainsi à la machine émettrice de quels
paquets se sont perdus en chemin et doivent être envoyés à nouveau. Les quatre
octets suivants contiennent divers éléments permettant aux deux machines en
communication de se synchroniser, notamment divers fanions indiquant si on veut
initier, ou terminer la connexion, ainsi que "Fenêtre" par lesquels le récepteur
indique à l'émetteur combien de place il lui reste dans la pile des paquets à
trier et traiter. Ceci permet à l'émetteur d'adapter le rythme auquel il
envoie les paquets pour ne pas déborder le récepteur. Enfin la "Somme de
contrôle" est un code correcteur d'erreur qui permet de vérifier si l'en-tête
n'a pas été altéré en chemin.

```{exercise}
Un paquet a été intercepté sur Internet avec le contenu initial suivant
indiqué en hexadécimal:
{itodo}`XXXXX`


1. Déterminer quelle partie de cet en-tête correspond à l'en-tête IP,
et laquelle correspond à l'en-tête TCP.
1. Indiquer l'adresse IP et le port de l'émetteur de ce paquet.
1. Indiquer l'adresse IP et le port du destinataire de ce paquet.
1. Combien d'octets du paquet ne sont pas représentés ci-dessus?

```

### Déroulement

Le protocole TCP applique une structure {glo}`clientserveur|client-serveur` à
communication entre deux machines. Cela signifie qu'une des machines, appelées
le serveur, va se mettre en mode d'écoute, et attendre que d'autres machines la
contactent. C'est la machine cliente qui va prendre l'initiative d'initier la
communication en envoyant un message TCP (juste l'entête, sans les données)
à la machine serveur. Le protocole TCP spécifie les messages qui doivent être
envoyés de part et d'autre pour initier la connexion, comment ensuite
envoyer et quittancer les données échangées, et comment mettre fin et terminer
la connexion une fois que tout a été envoyé et quittancé.

La figure ci-dessous indique comment les fanions SYN, FIN de l'entête TCP sont utilisés pour
indiquer que l'on veut respectivement initier et terminer une connexion, et comment
le fanion ACK est utilisé pour confirmer la bonne réception de la demande ou
des données, avec les numéros des séquences (#seq) et et d'acquittement (#ack).

```{image} media/TCPprot.svg
:width: 800
:align: center
```

```{exercise}
Un serveur reçoit un packet TCP avec le contenu suivant dans l'entête. Que cela signifie-t-il,
et comment le serveur est-il censé réagir? 

1. FIN = 1, no de séquence = 257
2. SYN = 1, no de séquence = 745
3. ACK = 1, no de séquence = 343, no d'acquittement = 746, 
````

## Le protocole UDP

TCP n'est pas l'unique moyen de transmettre des messages par internet. Par exemple, si l'important est que les
données soient transmises rapidement, même si certaines sont perdues en route, on peut utiliser le protocole UDP.
Avec ce protocole, l'émetteur envoie des paquets au destinataire sans vérifier que ce dernier les reçoit, ou même
qu'il est présent à l'adresse de destination. L'entête UDP ne contient que quatre champs de 2 octets chacun, déjà
présent dans l'entête TCP.

| 2 octets    |2 octets          |2 octets        |2 octets           |
|:------------|------------------|----------------|-------------------|
| port source | port destination | longueur totale | somme de contrôle|

Il n'y a donc pas de numérotations des séquences, ni de système d'acquittement, ce qui fait que si un paquet
est perdu ou s'arrive en retard par rapport aux autres paquets, on l'expéditeur et le destinataire n'ont aucun
moyen de le savoir. Par contre, cela permet d'aller plus vite, donc ce protocole est surtout utilisé dans les
applications en temps réel.

```{exercise}
Indiquer pour les applications suivantes, si le protocole TCP ou UDP était plus adapté, et indiquer pourquoi. 

1. La lecture d'une page web
2. Une application de téléphonie par Internet
3. Le streaming d'une vidéo
4. Une application bancaire en ligne
5. Un jeu vidéo en ligne
````
