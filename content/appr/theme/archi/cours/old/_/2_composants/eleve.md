# 4. Composants d'un ordinateur

Par composant d'ordinateur on désigne le matériel à l'intérieur de l'ordinateur, contrairement aux périphériques externes qui sont reliés par des câbles ou des moyens de communication sans fil.
Il s'agit de :

- l'alimentation,
- la carte mère,
- le processeur,
- la mémoire vive RAM,
- le disque dur / SSD / eMMC,
- le lecteur-graveur,
- la carte graphique.

On peut également citer les cartes sons, réseau, sorties USB etc. Ce type de matériel n'étant pas indispensable au bon fonctionnement du PC et souvent directement intégré à la carte mère, on ne s'y intéressera pas ici.


## L'alimentation
L'alimentation branchée sur le secteur transforme et fournit l'énergie nécessaire à la carte mère, mais l'alimentation est aussi directement reliée à certains composants tel que le lecteur/graveur de DVD ou le disque dur par exemple. 

La transformation du courant cause une déperdition d'énergie thermique, un système de ventilation est donc installé dans le coffret de l'alimentation et expulse l'air via l'arrière du boîtier de l'ordinateur. 

Une puissance de 400 watts est généralement suffisante pour les ordinateurs en «configuration bureautique» même si certaines alimentations peuvent atteindre les 1000 watts pour des configurations gourmandes en énergie (gaming par exemple).

```{image} media/Alim.png
:width: 700
:height: 400
```

## La carte mère
Une carte mère est le composant central de l'ordinateur. Elle est vissée au boîtier du PC, et possède les connecteurs (slots) pour accueillir des dizaines de composants et périphériques en plus des éléments indispensables décrits ici, et gérer les flux logiciels, chaque information envoyée ou reçue par le matériel ou un programme transitant par elle. 

Elle intègre également la ROM sur laquelle est enregistrée le BIOS, petit programme gérant la configuration «de base» du matériel et se chargeant de faire le lien avec le système d'exploitation. Ces réglages sont conservés en mémoire même en l'absence de courant grâce au [CMOS](https://fr.wikipedia.org/wiki/Complementary_metal_oxide_semi-conductor), alimenté par la pile de carte mère.
```{image} media/CarteMere.png
:width: 700
:height: 400
```

## Le processeur
On parle de microprocesseur ou de CPU, de l'anglais Central Processing Unit. Son rôle est le traitement de l'information numérique et il ne communique qu'en binaire. Il fait ainsi les calculs nécessaires à l'exécution des programmes et instructions à une vitesse en partie déterminée par sa fréquence exprimée en GigaHertz (GHz). Il est étudié en détails lors du chapitre suivant.

Un ventilateur dissipe généralement la chaleur du microprocesseur provoquée par le traitement massif des opérations et le maintient à la température optimale de fonctionnement. 

```{image} media/Processeur.png
:width: 500
:height: 250
```


## La mémoire vive «RAM»
Comme nous l'avons vu au cours du chapitre précédent, la mémoire RAM est utilisée par le processeur qui y place les données le temps de leur traitement. L'un des avantages de la mémoire équipant les ordinateurs est justement sa rapidité d'accès. 

Une autre particularité de la mémoire RAM est d'être temporaire, une fois l'opération terminée, les données ne sont pas conservées et sont de toute façon définitivement perdues une fois l'ordinateur éteint. 

Plusieurs types de mémoire RAM existent. En «barrettes» allant de 1 à 8 Go par unité (les configurations les plus courantes actuellement proposent 4 à 8 Go de RAM), elles sont à choisir en fonction du processeur et de l'utilisation que l'on fait du PC d'une part et des possibilités de la carte mère (capacité totale, nombre d'emplacements disponibles...) d'autre part.

```{image} media/RAM_Slot.jpeg
:width: 700
:height: 400
```

## Le disque dur ou le SSD
C'est sur le disque dur que les données à conserver sont enregistrées : les fichiers du système d'exploitation, les logiciels et surtout les données personnelles (photo, vidéo, musique, emails etc...). 

Il se présente sous la forme d'un boîtier rectangulaire, vissé au boiter du PC, qui intègre toute la mécanique (plateau, bras, tête de lecture...). Plus la vitesse de rotation des plateaux est importante, plus les performances sont élevées : on trouve actuellement des disques durs tournant à 5400, 7200, 10000 ou 15000 RPM (Round Per Minute: tours par minute), les vitesses de 7200 et 10000 RPM étant les plus répandues. 

Il est relié à la carte mère grâce à une nappe (câble plat) de type IDE ou grâce aux interfaces SATA (Serial ATA) ou SCSI. Un cavalier à positionner à l'arrière du boîtier permet généralement de le désigner comme disque «Maître», le disque dur principal (Master) ou comme «Esclave», un disque auxiliaire (Slave). 

Les disques durs aujourd'hui peuvent contenir des centaines de giga-octets, voire plusieurs tera-octets de données.

```{image} media/second_disquedur_23.png
:width: 700
:height: 400
```

Les ordinateurs récents sont de plus en plus équipés de SSD (Solid-State Drive) qui permettent de stocker des données tout comme les disques durs, mais leur conception est purement électronique et non plus mécanique. Ils sont donc plus résistant aux chocs et plus légers - et donc particulièrement adaptés aux ordinateurs portables - et beaucoup plus rapides. Ils ont une taille de plus en plus réduite et des gains de performance importants : temps d'accès réduits, meilleure bande passante que les disques durs traditionnels.

La fiabilité et les capacités des disques durs classiques pérénisent cependant leur utilisation.


```{image} media/Ssd.png
:width: 500
:height: 200
```

Sur certains ordinateurs portables d'entrée de gamme, le disque dur ou le SSD sont parfois remplacés par un stockage sous forme d'eMMC, solution peu coûteuse comme les cartes SD ou Multimedia Card.

 L'avantage, en plus du coût, réside au niveau de l'encombrement et du poids, et convient donc aux ordinateurs portables de petite taille. Compte-tenu des performances, à prix et configuration équivalents, on privilégiera le SSD, puis l'eMMC et enfin le disque dur.


## Le lecteur/graveur CD/DVD
Un ordinateur peut encore aujourd'hui être équipé d'un graveur, vissé au boîtier, glissé dans un emplacement ouvert sur l'avant du PC, permettant ainsi l'ouverture du tiroir qui recevra le disque optique que l'on appelle plus communément CD (Compact Disc) ou DVD (Digital Versatile Disc). Il est connecté à la carte mère par un câble plat (nappe) IDE ou SATA. 

```{image} media/LecterCD.png
:width: 700
:height: 400
```


## La carte graphique
La carte graphique, bien que très importante pour certains usages, est placée en dernière position de cette liste car elle peut-être remplacée par un chipset intégré (jeu de circuit) directement à la carte mère. Toutefois, pour certaines applications et notamment les jeux, gros consommateurs de ressources graphiques, elle est indispensable. En prenant à sa charge la gestion de l'affichage, elle libère le processeur de cette fonction, traite elle-même les informations et utilise sa propre mémoire (voir accélération matérielle). 

La carte graphique s'insère dans un connecteur de la carte mère : le port AGP ou le port PCI Express pour les plus récentes. Une fois connectée, les entrées et sorties de la carte sont accessibles par l'arrière du boîtier afin de fournir une image au système de visualisation (écran, TV, projecteur).


```{image} media/CarteVidéo.png
:width: 700
:height: 400
```
