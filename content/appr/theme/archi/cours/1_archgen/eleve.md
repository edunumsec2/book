# 1. Architecture générale

<!--**TODO:** _Ici, on parlera de quelques composants informatiques en les examinant avec le vocabulaire acquis dans les sections précédentes... Lesquels ????!!! : cartes graphiques, réseau, son, mère, alimentation, éléments de stockage interne/externe, lecteurs ... ?_ -->



Il est commun d’entendre parler du microprocesseur comme du «coeur de l’ordinateur». On se propose de dégager les caractéristiques essentielles de ce qui constitue cette machine «intelligente» appelée ordinateur.

Si l’on suit son évolution, depuis les années 50 jusqu’à aujourd’hui, on peut distinguer les éléments caractéristiques illustrés sur la figure suivante.


```{image} media/Bus_ROM_RAM_CPU.png
:width: 600
:height: 300
```
Schéma simplifié d'un ordinateur
<br> <br>

## La mémoire

**ROM** (Read Only Memory) : ce que l’on nomme ROM constitue une mémoire «fixe», statique de la machine, dont la taille est définie à la conception. On parle de mémoire morte, ou mémoire en lecture seule. Ce qu’elle stocke ne « part pas» lors de la mise hors tension de la machine. 
      
Cette mémoire fixe va intégrer tous les éléments nécessaires en particulier au démarrage de la machine, au lancement du système d’exploitation ; il en est de même en ce qui concerne les facteurs de conversion, tables de constantes, instructions propres de la machine. On distingue différents types de ROM :

- ROM standard,

- EPROM : ce type de mémoire rend programmation et effacement accessibles à l’utilisateur,

- PROM : une programmation unique est possible sur ce type de mémoire,

- EEPROM : c’est une mémoire programmable dont les données peuvent être effacées électriquement (succède à l’UVPROM dont les données pouvaient être supprimées dans une «chambre à UV»).

Il s’agit d’une mémoire à long terme.

     
```{image} media/ROM.png
:width: 600
:height: 300
```
Barrettes ROM

<br> <br>

**RAM** (Random Access Memory) : cette mémoire est une mémoire volatile, c’est à dire que son contenu va «disparaître» lorsque l’ordinateur est hors tension. On parle aussi de mémoire tampon. L’information étant stockée sous forme électrique dans les transistors, elle disparaît quand l’alimentation est coupée. 
    
```{image} media/barrettes_RAM.png
:width: 600
:height: 300
```
Barrettes RAM

<br>     
    
    
    
Cette mémoire stocke temporairement et aléatoirement les fichiers sur lequel on travaille : on parle de mémoire vive en français. Elle est accessible en lecture / écriture. Ce type de composants se présente sous la forme de «barrettes» amovibles faciles à remplacer. Les temps d’accès sont très courts (de l’ordre de la nanoseconde), et la capacité de stockage élevée en comparaison avec celle de la ROM. Elle est la plus coûteuse des deux. On distingue deux types de RAM : 

- la RAM statique nécessite un flux constant d’énergie pour conserver les données qu’elle contient,

- la RAM dynamique (DRAM, SDRAM) : elle doit être actualisée pour conserver les données qu’elle contient ; elle est plus lente et moins chère que la RAM statique.

<br> 

```{image} media/RAM-Vs-ROM.jpeg
:width: 600
:height: 250
```

<br> <br>
*Une analogie intéressante pour comprendre les particularités et missions respectives de la ROM et de la RAM est celle du commerçant et de la gestion quotidienne de sa caisse. Dans sa journée de travail, le commerçant encaisse, rend de la monnaie, gère donc des flux monétaires fluides et dimensionnés : dans le cas d’une boulangerie par exemple, les flux moyens vont être de l’ordre de quelques francs. En fin de journée, le commerçant compte sa caisse et part déposer la recette du jour à la banque : cela peut représenter alors plusieurs milliers de francs.* 
*La caisse représente en quelque sorte la RAM, accessible facilement et rapidement, avec des flux modérés et relativement réguliers ; en revanche sa taille est limitée. Elle est vide le matin, se charge et décharge dans la journée, puis se vide en fin de journée à la clôture.*
*La banque représente la ROM : le stockage de l’argent prend plus de temps, mais l’espace de stockage est beaucoup plus vaste et est sécurisé.*

<br> <br>

**Mémoire externe ou mémoire de masse** : ce terme désigne les supports externes à la machine permettant du stockage supplémentaire et donc venant en complément du stockage initial fixe de la machine (ROM). Par exemple : disque dur interne ou externe, bande magnétique, SSD, disque optique, clé usb, carte SD, … Cette mémoire permet de stocker une grande quantité d’informations, mais à une vitesse limitée. C’est un peu l’intermédiaire entre la RAM et la ROM.

<br>


## Le CPU (Central Processing Unit)

Il s’agit du processeur de l’ordinateur. C’est le coeur de l’ordinateur, c’est à dire l’espace où va se dérouler l’ensemble des opérations et instructions de la machine. C’est un peu le «cerveau» de la machine. 
Le CPU va aller chercher les informations dans la ROM en passant par la RAM qui est donc essentielle pour le traitement du processeur. On parle d’Unité Centrale de Traitement en français. Le processeur sert à l’échange de données entre composants informatiques : disques durs – carte graphique – ROM – RAM. Il coordonne, interprète, calcule, exécute.

La puissance du CPU est caractérisée par son nombre de bits, 32 ou 64 bits aujourd’hui, et la fréquence de traitement de l’information qu’il assure caractérise la rapidité avec laquelle il traite les informations. Cette puissance de traitement des cycles CPU, qui est donc la puissance de l’ordinateur, représente la capacité d’un ordinateur à manipuler des données. La puissance de calcul et la rapidité de traitement se trouvent multipliées par le nombres de coeurs éventuellement présents sur la puce. Nombre de bits et fréquence de traitement sont donc deux paramètres essentiels, mais également le nombre de coeurs que le processeur comporte.


```{image} media/PROCESSEURS.png
:width: 600
:height: 400
```
Différents types de microprocesseurs simple cœur et multicœurs
<br> <br>

Le cœur du processeur est en fait une unité de traitement qui permet de lire des instructions pour effectuer des actions spécifiques. Ainsi, quelle que soit l'action que l'on souhaite effectuer sur la machine, elle est exécutée par le cœur, et s'il y a plusieurs cœurs, qui sont en fait des unités de traitement, on peut effectuer toutes les actions rapidement et en même temps.

Les principaux acteurs du marché sont Intel et AMD.

### Processeur à noyau unique
Un processeur à noyau unique ou CPU utilise un seul noyau à l'intérieur du processeur. 

Avantages :

Un processeur à un seul cœur consomme moins d'énergie que les processeurs à plusieurs cœurs. Ceci est surtout problématique pour les appareils mobiles, oû le problème de l'autonomie de la batterie est essentiel. 
Comme les processeurs à cœur unique consomment moins d'énergie, l'ensemble du système qu'ils font fonctionner chauffe moins.
Un processeur à un seul cœur est toujours adapté pour la plupart des applications : vérification du courrier, navigation sur Internet, téléchargement de données, etc. peuvent toujours être traitées par un processeur à noyau unique. 

Inconvénients :

C'est un processeur relativement lent. Il n'a pas une grande puissance de calcul pour traiter de grandes opérations complexes, ou plusieurs opérations à la fois.
Comme les applications modernes nécessitent une grande puissance de traitement, un processeur monocœur qui les fait fonctionner peut se bloquer, paralysant ainsi l'ensemble du système alors «planté».

### Processeurs à double cœur
Un processeur à double cœur possède deux cœurs pour exécuter les opérations, intégrés dans un circuit unique pour se comporter comme une seule unité - un seul processeur -, à la différence d'un système multiprocesseur ; toutefois, ces cœurs possèdent leurs propres contrôleurs et caches, ce qui leur permet de travailler plus rapidement que les processeurs à cœur unique.


```{image} media/2coeurs.png
:width: 600
:height: 400
```
Microprocesseur bicœur
<br> <br>


Avantages :

Un processeur double cœur exécute l'ensemble des tâches beaucoup plus rapidement. Si un processeur à noyau unique est chargé de deux tâches différentes, il ne peut pas les effectuer simultanément. Il passe à toutes les tâches une par une, en série, alors qu'un processeur à double cœur peut effectuer les deux opérations en même temps, en parallèle.
Un processeur double cœur «équivaut» à deux ordinateurs en un... mais à un tarif moindre.

Inconvénients :

Peu d'opérations nécessitent réellement la puissance des processeurs double cœur. Une grande partie de la puissance est ainsi gaspillée et vide rapidement la batterie. Un appareil mobile utilisé à des fins informatiques générales, telles que la vérification du courrier électronique, la navigation sur Internet, la saisie de documents et le partage de données, ne nécessite pas réellement la puissance d'un processeur double cœur.
Pour ces raisons, de nombreux développeurs d'applications mobiles ne programment pas leurs applications pour qu'elles fonctionnent avec des processeurs à multiple cœur, les rendant ainsi incompatibles avec les mobiles qui fonctionnent toujours avec des processeurs à double ou multiple cœur.


### Les processeurs quadricœur et autres processeurs à cœurs multiples
En termes simples, un processeur quadricœur possède quatre cœurs et il en va de même pour un processeur hexacœur (six cœurs), octocœur (huit cœurs), etc.. Ces cœurs peuvent être soit sur le même circuit intégré, soit sur le même boîtier de puce.

```{image} media/4coeurs.png
:width: 600
:height: 400
```
Microprocesseur quadricoeur
<br> 

```{image} media/8coeurs.png
:width: 600
:height: 400
```
Microprocesseur octocoeur
<br> <br>


Avantages :

Le multitâche est le principal avantage des processeurs quadri ou octocœurs. Un plus grand nombre de cœurs offre évidemment une plus grande capacité à effectuer plusieurs tâches en parallèle.
Ces processeurs sont utiles pour exécuter des applications qui sont plutôt intensives et nécessitent beaucoup de ressources. Ces applications comprennent les éditeurs vidéo, les antivirus, les programmes graphiques, etc.
Les nouveaux processeurs quadricœurs consomment moins d'énergie, dégagent moins de chaleur, et sont donc très efficaces.
Ces processeurs sont en fait très en avance sur la technologie actuelle de développement d'applications mobiles, car tous les développeurs ne sont pas capables de programmer des applications fonctionnant sur ces processeurs multiples. De nombreux programmes sont encore écrits pour des processeurs à double ou simple cœur.

Inconvénients :

... encore et toujours la consommation énergétique, vidant très rapidement la batterie.


Le nombre de cœurs de processeur est important dans certaines activités comme le *gaming* : il est de plus en plus courant de trouver des processeurs hexa-cœurs, ou octo-cœurs ; [les dernières générations de multiprocesseurs possèdent jusqu'à 12 ou 16 cœurs](https://www.futura-sciences.com/tech/comparatifs/meilleur-processeur-comparatif) !

On doit également mentionner les cœurs logiques, c’est-à-dire les *threads*, comme on les appelle plus communément (tâches en français). La performance d'un monoprocesseur est jugée sur sa capacité à gérer plusieurs «fils» d'instructions. Du point de vue de l'utilisateur, ces exécutions semblent se dérouler en parallèle. Toutefois, là où chaque processus possède sa propre mémoire virtuelle, les threads d'un même processus se partagent sa mémoire virtuelle. Par contre, tous les threads possèdent leur propre pile d'exécution.

Les technologies d’hyperthreading d’Intel et de multithreading d’AMD permettent à un seul cœur physique de gérer deux tâches simultanément, fonctionnant ainsi comme deux cœurs logiques distincts. Cette technologie est aujourd'hui très performante. 
La plupart de la gamme Ryzen d’AMD propose le multithreading, y compris les modèles de milieu et de haut de gamme, tandis que l’hyperthreading est pour l’instant réservé aux processeurs i7 et i9 haut de gamme d’Intel.

## Les entrées-sorties
Un ordinateur traite de l'information au niveau de sa mémoire et de son processeur. Il récupère donc cette information via des ports d'entrée et redistribue une information après traitement via des ports de sortie. L'ensemble de cet environnement d'entrées-sorties constitue ce que l'on nomme les périphériques : clavier, écran, enceintes audio ou casque, imprimante, souris ou pad, disques externes, microphone, réseau ethernet ou wifi, etc.
Certains périphériques sont par nature destinés uniquement à l'entrée de données (claviers et souris, microphones), tandis que d'autres s'occupent avant tout de la sortie (imprimantes, écrans non-tactiles) ; d'autres encore permettent à la fois l'entrée et la sortie de données (disques durs, disquettes, CD-ROM inscriptibles, clés usb).

```{image} media/peripheriques1.png
:width: 650
:height: 500
```
Unité centrale et périphériques
<br> <br>

### Interfaçage
Dans une description idéale, le processeur se connecte au bus et envoie sur le bus adresses, données et commandes au périphérique. Ensuite, le processeur va devoir attendre et rester connecté au bus tant que le périphérique n'a pas traité sa demande intégralement en lecture ou en écriture. Mais les périphériques sont lents et le processeur attend le périphérique...
Pour résoudre ce problème, on intercale des registres d'interfaçage entre le processeur et les entrées-sorties. Une fois que le processeur a écrit les informations à transmettre dans ces registres, il peut faire autre chose, le registre se chargeant de maintenir et mémoriser les informations à transmettre. Les registres d’interfaçage sont surveillés régulièrement par le processeur pour voir si un périphérique lui a envoyé une information, mais le processeur peut utiliser quelques cycles pour faire son travail en attendant que le périphérique traite intégralement sa commande. Ces registres peuvent contenir des données ou des commandes, des valeurs numériques auxquelles le périphérique répond en effectuant un ensemble d'actions préprogrammées.

Les commandes sont traitées par un contrôleur de périphérique, qui va lire les commandes envoyées par le processeur, les interpréter, et piloter le périphérique de façon à faire ce qui est demandé. Le contrôleur de périphérique génère des signaux de commande qui déclencheront une action effectuée par le périphérique. Certains contrôleurs de périphérique peuvent permettre au processeur de communiquer avec plusieurs périphériques en même temps. C'est notamment le cas pour tout ce qui est des contrôleurs PCI, USB et autres. Certains périphériques, comme les disques IDE intègrent en leur sein ce contrôleur. Certains de ces contrôleurs intègrent un registre d'état, lisible par le processeur, qui contient des informations sur l'état du périphérique. Ils servent à signaler des erreurs de configuration ou des pannes touchant un périphérique.

Le système d'exploitation d'un ordinateur ne connait pas toujours le fonctionnement d'un périphérique ou de son contrôleur : il faut alors installer un programme qui va permettre la communication avec le périphérique, et qui va gérer transfert des données, adressage du périphérique, etc. Ce petit programme est appelé un *driver* ou pilote de périphérique. 

## Les bus
Un bus informatique est un dispositif de transmission de données partagé entre plusieurs composants d'un système informatique. Le bus informatique est la réunion des parties matérielles et immatérielles qui permet la transmission de données entre les composants de la machine.
On distingue deux types de bus : le FSB (Front Side Bus), ou *bus système*, et le bus d'extension. Le premier permet au processeur de communiquer avec la mémoire vive, le second est une voie de liaison entre le processeur et les cartes d'extension. Des connecteurs d'extension présents sur la carte mère permettent d'y ajouter de nouveaux composants : cartes d'extension tels que carte son, carte d'acquisition vidéo, carte réseau, etc.
Il existe différents types de bus d'extension : [ISA, EISA, PCI, PCMCIA, VESA.](http://www.dicofr.com/cgi-bin/n.pl/dicofr/definition/20010101000612)
On se propose ici de décrire exclusivement les différents types de bus système : bus de données, d'adressage et de commande.


```{image} media/Schéma_ordi.png
:width: 600
:height: 400
```
Schéma général d'un ordinateur
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

*NB: Le processeur 8088 qui équipait des premiers PC n'avait que 20 lignes d'adresse. Il pouvait donc accéder à 2 exposant 20 adresses différentes, soit 1 Mo. C'est pour cette raison que le système d'exploitation DOS qui date de cette époque ne peut pas adresser la totalité de la mémoire des systèmes actuels. Le nombre de lignes du bus d'adresse a ensuite évolué avec les différentes générations de processeurs.*

### Le bus de commande (Control Bus) 
Le bus de commande ou bus de contrôle transporte les ordres et les signaux de synchronisation en provenance du CPU et à destination de l'ensemble des composants matériels via un ensemble de connexions physiques telles que des câbles ou des circuits imprimés. Il s'agit d'un bus bidirectionnel qui transmet également les signaux de réponse des éléments matériels.
Le CPU utilise un des signaux pour indiquer le sens des transferts sur le bus de données (lecture ou écriture).
Le bus de contrôle est constitué de lignes de contrôle qui envoient chacune un signal spécifique, tel que lecture, écriture et interruption. La plupart des microprocesseurs incluent des lignes d'horloge système, des lignes d'état et des lignes d'activation d'octets.



