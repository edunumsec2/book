# Architecture générale



Il est commun d’entendre parler du microprocesseur comme du « cœur de l’ordinateur ». On se propose de dégager les caractéristiques essentielles de ce qui constitue cette machine « intelligente » appelée ordinateur, tout en explicitant les composants informatiques spécifiques (le matériel ou « hardware »).

Si l’on suit l'évolution de l'ordinateur, depuis les années 50 jusqu’à aujourd’hui, on peut distinguer les éléments caractéristiques illustrés sur la figure suivante.


```{figure} media/Bus_ROM_RAM_CPU.png
---
height: 350px
width: 500px
align: left
---
Schéma simplifié d'un ordinateur
```
<br> <br>

D'un point de vue matériel, on distingue :

- l'alimentation,
- la carte mère,
- le processeur,
- la mémoire vive RAM,
- le disque dur / SSD / eMMC,
- le lecteur-graveur,
- la carte graphique.

On peut également citer les cartes sons, réseau, sorties USB etc. Ce type de matériel n'étant pas indispensable au bon fonctionnement du PC et souvent directement intégré à la carte mère, on ne s'y intéressera pas ici.
On distingue ce matériel, partie intégrante de la machine, avec les périphériques externes qui lui sont reliés par des câbles ou des moyens de communication sans fil.
<br> <br>

## La mémoire

**ROM** (Read-Only Memory) : ce que l’on nomme ROM constitue une mémoire « fixe », statique de la machine, dont la taille est définie à la conception. On parle de mémoire morte, ou mémoire en lecture seule. Ce qu’elle stocke ne « part pas » lors de la mise hors tension de la machine. 
      
Cette mémoire fixe va intégrer tous les éléments nécessaires en particulier au démarrage de la machine, au lancement du système d’exploitation ; il en est de même en ce qui concerne les facteurs de conversion, tables de constantes, instructions propres de la machine. On distingue différents types de ROM :

- ROM standard,

- EPROM : ce type de mémoire rend programmation et effacement accessibles à l’utilisateur,

- PROM : une programmation unique est possible sur ce type de mémoire,

- EEPROM : c’est une mémoire programmable dont les données peuvent être effacées électriquement (succède à l’UVPROM dont les données pouvaient être supprimées dans une « chambre à UV »).

Il s’agit d’une mémoire à long terme.

```{figure} media/ROM.png
---
height: 350px
width: 500px
align: left
---
Barrettes ROM
```

<br> 





**RAM** (Random Access Memory) : cette mémoire est une mémoire volatile, c’est à dire que son contenu va «disparaître» lorsque l’ordinateur est hors tension. On parle aussi de mémoire tampon. L’information étant stockée sous forme électrique dans les transistors, elle disparaît quand l’alimentation est coupée. 
    
```{figure} media/barrettes_RAM.png
---
width: 600
height: 300
align: left
---
Barettes RAM
```


<br>     
    
    
    
Cette mémoire stocke temporairement et aléatoirement les fichiers sur lequel on travaille : on parle de mémoire vive en français. Elle est accessible en lecture / écriture. Ce type de composants se présente sous la forme de «barrettes» amovibles faciles à remplacer. Les temps d’accès sont très courts (de l’ordre de la nanoseconde), et la capacité de stockage élevée en comparaison avec celle de la ROM. Elle est la plus coûteuse des deux. On distingue deux types de RAM : 

- la RAM statique nécessite un flux constant d’énergie pour conserver les données qu’elle contient,

- la RAM dynamique (DRAM, SDRAM) : elle doit être actualisée pour conserver les données qu’elle contient ; elle est plus lente et moins chère que la RAM statique.


Les composants de mémoire RAM existent en général en «barrettes» allant de 1 à 8 Go par unité (les configurations les plus courantes actuellement proposent 4 à 8 Go de RAM), elles sont à choisir en fonction du processeur et de l'utilisation que l'on fait du PC d'une part et des possibilités de la carte mère (capacité totale, nombre d'emplacements disponibles...) d'autre part.

<br> 

```{figure} media/RAM-Vs-ROM.jpeg
---
width: 600
height: 250
align: left
---
RAM versus ROM
```

<br> <br>
*Une analogie intéressante pour comprendre les particularités et missions respectives de la ROM et de la RAM est celle du commerçant et de la gestion quotidienne de sa caisse. Dans sa journée de travail, le commerçant encaisse, rend de la monnaie, gère donc des flux monétaires fluides et dimensionnés : dans le cas d’une boulangerie par exemple, les flux moyens vont être de l’ordre de quelques francs. En fin de journée, le commerçant compte sa caisse et part déposer la recette du jour à la banque : cela peut représenter alors plusieurs milliers de francs.* 
*La caisse représente en quelque sorte la RAM, accessible facilement et rapidement, avec des flux modérés et relativement réguliers ; en revanche sa taille est limitée. Elle est vide le matin, se charge et décharge dans la journée, puis se vide en fin de journée à la clôture.*
*La banque représente la ROM : le stockage de l’argent prend plus de temps, mais l’espace de stockage est beaucoup plus vaste et est sécurisé.*

<br>

### Mémoire externe ou mémoire de masse
 Ce terme désigne les supports externes à la machine permettant du stockage supplémentaire et donc venant en complément du stockage initial fixe de la machine (ROM). Par exemple : disque dur interne ou externe, bande magnétique, SSD, disque optique, clé usb, carte SD, … Cette mémoire permet de stocker une grande quantité d’informations, mais à une vitesse limitée. C’est un peu l’intermédiaire entre la RAM et la ROM.

Sur le disque dur peuvent être enregistrées les données à conserver : les fichiers du système d'exploitation, les logiciels et surtout les données personnelles (photo, vidéo, musique, emails etc...). 

Le disque dur se présente sous la forme d'un boîtier rectangulaire, vissé au boiter du PC, qui intègre toute la mécanique (plateau, bras, tête de lecture...). Plus la vitesse de rotation des plateaux est importante, plus les performances sont élevées : on trouve actuellement des disques durs tournant à 5400, 7200, 10000 ou 15000 RPM (Round Per Minute: tours par minute), les vitesses de 7200 et 10000 RPM étant les plus répandues. 

Il est relié à la carte mère grâce à une nappe (câble plat) de type IDE ou grâce aux interfaces SATA (Serial ATA) ou SCSI. Un cavalier à positionner à l'arrière du boîtier permet généralement de le désigner comme disque «Maître», le disque dur principal (Master) ou comme «Esclave», un disque auxiliaire (Slave). 

Les disques durs aujourd'hui peuvent contenir des centaines de gigaoctets, voire plusieurs téraoctets de données.

```{figure} media/second_disquedur_23.png
---
width: 700
height: 400
align: left
---
Disque dur mécanique
```

Les ordinateurs récents sont de plus en plus équipés de SSD (Solid-State Drive) qui permettent de stocker des données tout comme les disques durs, mais leur conception est purement électronique et non plus mécanique. Ils sont donc plus résistant aux chocs et plus légers - et donc particulièrement adaptés aux ordinateurs portables - et beaucoup plus rapides. Ils ont une taille de plus en plus réduite et des gains de performance importants : temps d'accès réduits, meilleure bande passante que les disques durs traditionnels.

La fiabilité et les capacités des disques durs classiques pérennisent cependant leur utilisation.


```{figure} media/Ssd.png
---
width: 500
height: 200
align: left
---
Disque dur SSD
```

Sur certains ordinateurs portables d'entrée de gamme, le disque dur ou le SSD sont parfois remplacés par un stockage sous forme d'eMMC, solution peu coûteuse comme les cartes SD ou Multimedia Card.

 L'avantage, en plus du coût, réside au niveau de l'encombrement et du poids, et convient donc aux ordinateurs portables de petite taille. Compte-tenu des performances, à prix et configuration équivalents, on privilégiera le SSD, puis l'eMMC et enfin le disque dur.


**Le lecteur/graveur CD/DVD**
Un ordinateur peut encore aujourd'hui être équipé d'un graveur, vissé au boîtier, glissé dans un emplacement ouvert sur l'avant du PC, permettant ainsi l'ouverture du tiroir qui recevra le disque optique que l'on appelle plus communément CD (Compact Disc) ou DVD (Digital Versatile Disc). Il est connecté à la carte mère par un câble plat (nappe) IDE ou SATA. 

```{figure} media/LecteurCD.png
---
width: 700
height: 400
align: left
---
Lecteur CD
```


<br> <br>


## Le CPU (Central Processing Unit)

Il s’agit du processeur de l’ordinateur. C’est le cœur de l’ordinateur, c’est à dire l’espace où va se dérouler l’ensemble des opérations et instructions de la machine. C’est un peu le «cerveau» de la machine. 
Le CPU va aller chercher les informations dans la ROM en passant par la RAM qui est donc essentielle pour le traitement du processeur. On parle d’Unité Centrale de Traitement en français. Le processeur sert à l’échange de données entre composants informatiques : disques durs – carte graphique – ROM – RAM. Il coordonne, interprète, calcule, exécute.

La puissance du CPU est caractérisée par son nombre de bits, 32 ou 64 bits aujourd’hui, et la fréquence de traitement de l’information qu’il assure caractérise la rapidité avec laquelle il traite les informations. Cette puissance de traitement des cycles CPU, qui est donc la puissance de l’ordinateur, représente la capacité d’un ordinateur à manipuler des données. La puissance de calcul et la rapidité de traitement se trouvent multipliées par le nombres de cœurs éventuellement présents sur la puce. Nombre de bits et fréquence de traitement sont donc deux paramètres essentiels, mais également le nombre de cœurs que le processeur comporte.


```{figure} media/PROCESSEURS.png
---
width: 600
height: 400
align: left
---
Différents types de microprocesseurs simple cœur et multicœurs
```

<br> <br>

Le cœur du processeur est en fait une unité de traitement qui permet de lire des instructions pour effectuer des actions spécifiques. Ainsi, quelle que soit l'action que l'on souhaite effectuer sur la machine, elle est exécutée par le cœur, et s'il y a plusieurs cœurs, qui sont en fait des unités de traitement, on peut effectuer toutes les actions rapidement et en même temps.

Les principaux acteurs du marché sont Intel et AMD.


### La carte mère
Une carte mère est le composant central de l'ordinateur. Elle est vissée au boîtier du PC, et possède les connecteurs (slots) pour accueillir des dizaines de composants et périphériques en plus des éléments indispensables décrits ici, et gérer les flux logiciels, chaque information envoyée ou reçue par le matériel ou un programme transitant par elle. 

Elle intègre également la ROM sur laquelle est enregistrée le BIOS, petit programme gérant la configuration «de base» du matériel et se chargeant de faire le lien avec le système d'exploitation. Ces réglages sont conservés en mémoire même en l'absence de courant grâce au [CMOS](https://fr.wikipedia.org/wiki/Complementary_metal_oxide_semi-conductor), alimenté par la pile de carte mère.

```{figure} media/CarteMere.png
---
width: 700
height: 400
align: left
---
Carte mère
```

<br> <br>

## Les entrées-sorties
Un ordinateur traite de l'information au niveau de sa mémoire et de son processeur. Il récupère donc cette information via des ports d'entrée et redistribue une information après traitement via des ports de sortie. L'ensemble de cet environnement d'entrées-sorties constitue ce que l'on nomme les périphériques : clavier, écran, enceintes audio ou casque, imprimante, souris ou pad, disques externes, microphone, réseau ethernet ou wifi, etc.
Certains périphériques sont par nature destinés uniquement à l'entrée de données (claviers et souris, microphones), tandis que d'autres s'occupent avant tout de la sortie (imprimantes, écrans non-tactiles) ; d'autres encore permettent à la fois l'entrée et la sortie de données (disques durs, disquettes, CD-ROM inscriptibles, clés usb).

```{figure} media/peripheriques1.png
---
width: 650
height: 500
align: left
---
Unité centrale et périphériques
```

<br> <br>

### Interfaçage
Dans une description idéale, le processeur se connecte au bus et envoie sur le bus adresses, données et commandes au périphérique. Ensuite, le processeur va devoir attendre et rester connecté au bus tant que le périphérique n'a pas traité sa demande intégralement en lecture ou en écriture. Mais les périphériques sont lents et le processeur attend le périphérique...
Pour résoudre ce problème, on intercale des registres d'interfaçage entre le processeur et les entrées-sorties. Une fois que le processeur a écrit les informations à transmettre dans ces registres, il peut faire autre chose, le registre se chargeant de maintenir et mémoriser les informations à transmettre. Les registres d’interfaçage sont surveillés régulièrement par le processeur pour voir si un périphérique lui a envoyé une information, mais le processeur peut utiliser quelques cycles pour faire son travail en attendant que le périphérique traite intégralement sa commande. Ces registres peuvent contenir des données ou des commandes, des valeurs numériques auxquelles le périphérique répond en effectuant un ensemble d'actions préprogrammées.

Les commandes sont traitées par un contrôleur de périphérique, qui va lire les commandes envoyées par le processeur, les interpréter, et piloter le périphérique de façon à faire ce qui est demandé. Le contrôleur de périphérique génère des signaux de commande qui déclencheront une action effectuée par le périphérique. Certains contrôleurs de périphérique peuvent permettre au processeur de communiquer avec plusieurs périphériques en même temps. C'est notamment le cas pour tout ce qui est des contrôleurs PCI, USB et autres. Certains périphériques, comme les disques IDE intègrent en leur sein ce contrôleur. Certains de ces contrôleurs intègrent un registre d'état, lisible par le processeur, qui contient des informations sur l'état du périphérique. Ils servent à signaler des erreurs de configuration ou des pannes touchant un périphérique.

Le système d'exploitation d'un ordinateur ne connait pas toujours le fonctionnement d'un périphérique ou de son contrôleur : il faut alors installer un programme qui va permettre la communication avec le périphérique, et qui va gérer transfert des données, adressage du périphérique, etc. Ce petit programme est appelé un *driver* ou pilote de périphérique. 

<br> <br>

## Les bus
Un bus informatique est un dispositif de transmission de données partagé entre plusieurs composants d'un système informatique. Le bus informatique est la réunion des parties matérielles et immatérielles qui permet la transmission de données entre les composants de la machine.
On distingue deux types de bus : le FSB (Front Side Bus), ou *bus système*, et le bus d'extension. Le premier permet au processeur de communiquer avec la mémoire vive, le second est une voie de liaison entre le processeur et les cartes d'extension. Des connecteurs d'extension présents sur la carte mère permettent d'y ajouter de nouveaux composants : cartes d'extension tels que carte son, carte d'acquisition vidéo, carte réseau, etc.
Il existe différents types de bus d'extension : [ISA, EISA, PCI, PCMCIA, VESA.](http://www.dicofr.com/cgi-bin/n.pl/dicofr/definition/20010101000612)
On se propose ici de décrire exclusivement les différents types de bus système : bus de données, d'adressage et de commande.


```{figure} media/Schéma_ordi.png
---
width: 600
height: 400
align: left
---
Schéma général d'un ordinateur
```

<br> <br>



### Bus de données (Data Bus)
Le bus de données interconnecte le processeur, la mémoire centrale et les contrôleurs de périphériques et véhicule les données entre ces composants. Il est bidirectionnel (contrairement au bus d'adressage) puisque le processeur l'utilise pour lire et pour écrire en mémoire ou dans les entrées-sorties.

Le bus de données est commandé par le CPU, les autres composants y sont connectés à tour de rôle pour répondre aux commandes de lecture ou d'écriture du processeur.

Le débit des données véhiculées par ce bus dépend d'une part des vitesses de transmission ou plus exactement de la capacité des composants à saisir rapidement les signaux des bus et à y répondre aussi vite. La cadence de ces signaux est liée à fréquence de la carte mère.

La largeur du bus est le second critère qui va influencer le débit des transmissions des données. Plus le bus est large et plus important sera le nombre de données qui pourront être véhiculées simultanément. La largeur du bus de donnée peut être comparée au nombre de voies de circulation d'une autoroute. Elle dépend directement de la puissance du processeur.

*NB: Les premiers microprocesseurs qui ne pouvaient traiter que 8 bits simultanément avaient un bus de données de 8 bits. Actuellement, les microprocesseurs traitent en général les données par mots de 32 bits mais le bus de donnée est plus large encore (64 bits) ce qui lui permet de véhiculer plus de données en parallèle.*

### Le bus d'adressage (Address Bus) 
Le bus d'adressage (ou bus d'adresse, ou bus mémoire) reçoit du processeur les adresses des cellules mémoire et des entrées/sorties auxquelles il veut accéder.
Chacun des conducteurs du bus d'adressage peut prendre deux états, 0 ou 1. L'adresse est donc le nombre binaire qui est véhiculé par ces lignes. La quantité d'adresses qui peuvent ainsi être formées est égale à deux exposant le nombre de bits d'adresse.
Ce bus est physiquement constitué de câbles parallèles qui relient le processeur à la mémoire. La taille de ce bus ou sa largeur définissent le nombre de connexions parallèles et dépendent des caractéristiques du processeur et de la RAM. Chaque connexion transporte un bit, un bus de largeur 32 bits transporte 32 bits, ce qui permet de répertorier 2<sup>32</sup> adresses mémoire différentes (env. 4 Go). 
Les deux bus, d'adressage et de données, ne sont pas forcément de largeur identique.

*NB: Le processeur 8088 qui équipait des premiers PC n'avait que 20 lignes d'adresse. Il pouvait donc accéder à 2 exposant 20 adresses différentes, soit 1 Mo. C'est pour cette raison que le système d'exploitation DOS qui date de cette époque ne peut pas adresser la totalité de la mémoire des systèmes actuels. Le nombre de lignes du bus d'adresse a ensuite évolué avec les différentes générations de processeurs.*

### Le bus de commande (Control Bus) 
Le bus de commande ou bus de contrôle transporte les ordres et les signaux de synchronisation en provenance du CPU et à destination de l'ensemble des composants matériels via un ensemble de connexions physiques telles que des câbles ou des circuits imprimés. Il s'agit d'un bus bidirectionnel qui transmet également les signaux de réponse des éléments matériels.
Le CPU utilise un des signaux pour indiquer le sens des transferts sur le bus de données (lecture ou écriture).
Le bus de contrôle est constitué de lignes de contrôle qui envoient chacune un signal spécifique, tel que lecture, écriture et interruption. La plupart des microprocesseurs incluent des lignes d'horloge système, des lignes d'état et des lignes d'activation d'octets.

<br> <br>

## Autres composants matériels

### L'alimentation
L'alimentation branchée sur le secteur transforme et fournit l'énergie nécessaire à la carte mère, mais l'alimentation est aussi directement reliée à certains composants tel que le lecteur/graveur de DVD ou le disque dur par exemple. 

La transformation du courant cause une déperdition d'énergie thermique, un système de ventilation est donc installé dans le coffret de l'alimentation et expulse l'air via l'arrière du boîtier de l'ordinateur. 

Une puissance de 400 watts est généralement suffisante pour les ordinateurs en «configuration bureautique» même si certaines alimentations peuvent atteindre les 1000 watts pour des configurations gourmandes en énergie (gaming par exemple).

```{figure} media/Alim.png
---
width: 700
height: 400
align: left
---
Alimentation
```


### La carte graphique
La carte graphique, bien que très importante pour certains usages, est placée en dernière position de cette liste car elle peut-être remplacée par un chipset intégré (jeu de circuit) directement à la carte mère. Toutefois, pour certaines applications et notamment les jeux, gros consommateurs de ressources graphiques, elle est indispensable. En prenant à sa charge la gestion de l'affichage, elle libère le processeur de cette fonction, traite elle-même les informations et utilise sa propre mémoire (voir accélération matérielle). 

La carte graphique s'insère dans un connecteur de la carte mère : le port AGP ou le port PCI Express pour les plus récentes. Une fois connectée, les entrées et sorties de la carte sont accessibles par l'arrière du boîtier afin de fournir une image au système de visualisation (écran, TV, projecteur).


```{figure} media/CarteVidéo.png
---
width: 700
height: 400
align: left
---
Carte graphique
```
