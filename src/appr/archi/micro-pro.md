# CPU

Le processeur, en anglais central processing unit (CPU), est un composant qui exécute les instructions machine des programmes informatiques.

On a précédemment détaillé les différents composants et systèmes logiques à partir desquels on peut construire un processeur. On va à présent évoquer l'architecture de von Neumann qui décrit la façon dont le processeur s'insère dans son environnement. Les différents éléments qui constituent le processeur et qui en assurent le bon fonctionnement seront ensuite détaillés.

:::::{grid} 2

::::{grid-item}
:::{card}
:img-top: media/Gordon_Moore.jpeg

Gordon Moore
^^^^^
* **Naissance** 1929 / San Francisco 🇺🇸 
```{dropdown} Bio
:animate: fade-in-slide-down
Gordon Earle Moore est le cofondateur d'Intel en 1968. Intel est le premier fabricant mondial de microprocesseurs. Gordon Moore est célèbre pour avoir formulé en 1965 une loi empirique portant son nom : **loi de Moore**. Cette loi prédit un doublement de la complexité, et donc du nombre de transistors présents dans les microprocesseurs tous les deux ans. Bien que nous ayons atteint certaines limites physiques au niveau atomique et des effets de bruits parasites liés aux effets quantiques et à la désintégration alpha, la loi est toujours vérifiée aujourd'hui malgré un ralentissement de la progression pour certaines caractéristiques. Ces limites sont aujourd'hui compensées par des puces intégrant de plus en plus de composants de plus en plus complexes.
```
:::
::::
:::::

```{admonition} (micro)-processeur
:class: attention
Le processeur est l'unité de traitement central de l'ordinateur. Il est construit avec des circuits regroupés en systèmes qui produisent des fonctions logiques et arithmétiques en suivant un programme et en utilisant des éléments de mémoire appelés registres.
Un microprocesseur est un processeur construit avec un circuit intégré, c'est-à-dire un dispositif qui tient sur quelques cm<sup>2</sup>. Il n'y a donc que la taille qui fasse la différence.

```

## Horloge et accès mémoire

Un processeur est un dispositif synchrone, ce qui signifie que les opérations à l'intérieur du processeur se déroulent de manière synchrone à un temps donné. Pour assurer cette simultanéité, il faut comme pour un orchestre, donner le tempo. Cette fonction de métronome est assurée par une horloge, ou un signal d'horloge. Cette horloge est constituée d'un simple signal carré <!-- TODO: ajouter image --> dont la fréquence atteint aujourd'hui plusieurs gigahertz, c'est-à-dire plusieurs milliards de cycles par seconde.

```{admonition} La notion de *synchronisation*
:class: attention
La notion de synchronisation est centrale. 
Les systèmes numériques synchrones sont ceux dont les opérations (instructions, calculs, logique, etc.) sont coordonnées par un ou plusieurs signaux d'horloge centralisés, par opposition, aux systèmes asynchrones qui n'ont pas d'horloge globale. 
Les systèmes asynchrones ne dépendent pas d'heures d'arrivée strictes des signaux ou des messages pour un fonctionnement fiable. La coordination est obtenue via des tests sur l'arrivée des évènements.

Sans entrer dans les détails ici, on notera que dans un système synchrone, il est possible d'assurer une coordination et une cohérence des opérations, ce qui est impossible autrement. Cet aspect devient crucial dans les systèmes distribués qui ne disposent plus de la garantie de synchronisation.

Les circuits asynchrones ont été envisagés comme une alternative possible aux circuits synchrones, plus répandus, particulièrement pour diminuer la consommation d'énergie, augmenter la vitesse, faciliter la conception et augmenter la fiabilité. Il semblerait qu'après avoir été un peu délaissée par le monde de la recherche et du développement depuis les années 1990 et 2000, la thématique des circuits asynchrones suscite à nouveau un regain d'intérêt, en particulier relativement aux impératifs de faible consommation énergétique en relation avec le changement climatique.


```

### L'accès à la mémoire

```{admonition} Rappel
:class: danger
Comme on l'a vu dans l'architecture de von Neumman, la mémoire contient le programme et les données du programme. Un programme peut donc théoriquement se modifier lui-même en se modifiant dans la mémoire, même si, en pratique, toutes les architectures modernes l'interdisent (c'est rarement un effet souhaité !).
```

L'UCT doit accéder à la mémoire RAM en lecture ou en écriture. Les deux mécanismes sont très similaires, mais avant de regarder plus en détail comment cela fonctionne, il faut d'abord définir comment la mémoire est structurée. La mémoire RAM permet, comme on l'a vu au premier chapitre, d'accéder à tout moment à n'importe quel emplacement.

Pour y accéder, le processeur envoie d'abord l'adresse au module mémoire, puis lit ou écrit la valeur via le bus d'adressage.

```{admonition} Anecdote
:class: attention
Le processeur Intel 80286 (ancêtre des processeurs Pentium), sorti en 1982, présentait un bus de données de 16 bits et un bus d'adresses de 24 bits. De plus l'adressage par segments (relativement compliqué) réduisait l'adressage physique à un adressage sur 20 bits.
```

Il manque encore un élément : lorsque la mémoire voit une adresse apparaître elle doit pouvoir déterminer s'il s'agit d'une lecture ou d'une écriture. Pour cela deux connexions supplémentaires relient le processeur à la mémoire : une ligne *enable* et une ligne *set*. Lorsque la ligne *enable* est à 1, alors le processeur accède à la mémoire en lecture et sur le bus de données doit apparaître les données qui sont stockées dans la mémoire à l'adresse indiquée sur le bus d'adressage. Lorsque c'est la ligne *set* qui est à 1, alors la mémoire doit enregistrer les données à l'adresse indiquée.

```{admonition} Le contenu de la mémoire
:class: hint

**Les instructions** : 
la mémoire contient le programme sous forme de codes qui représentent des instructions à exécuter par le processeur. Ces codes correspondent à un jeu d'instructions propre à chaque modèle de processeur. On parle de langage machine. Pour écrire de tels programmes, on utilise un programme et un langage assembleur, proche de la machine : c'est une représentation exacte du langage machine, mais qui est une interface plus lisible dans la communication machine. C'est le langage de plus bas niveau qui représente le langage machine sous une forme lisible par un humain.


**Les données** : 
les données stockées dans la mémoire peuvent être des nombres, des lettres, des chaînes de caractères ainsi que des adresses d'autres emplacements en mémoire. On trouvera plus de détails à ce sujet dans le chapitre {ref}`représentation de l'information <repinfo>`.

```

```{question} Question 1
Avec un bus d'adressage de 24 bits, quelle est la taille maximum de la mémoire ? 
* {f}`32ko`
* {v}`16Mo`
* {f}`16Go`
```

```{question} Question 2
Quelle est la taille maximale de la mémoire pour un processeur 80286, sachant que l'adressage physique est finalement réduit à 20 bits ? 
* {f}`32ko`
* {f}`16Mo`
* {v}`1Mo`
```

### L'unité de contrôle

L'unité de contrôle reçoit les instructions en provenance de la RAM. Elle s'occupe d'activer les composants qui doivent l'être dans le microprocesseur.

### Les registres

Les registres permettent de stocker des valeurs, comme la RAM, mais directement à l'intérieur du processeur. Ils fonctionnent aussi en mode lecture ou écriture. C'est l'unité de contrôle qui détermine si un registre est utilisé en lecture ou en écriture avec deux fils de connexion: *enable* et *set*.
En principe ces registres stockent les informations en provenance de la mémoire ou le résultat d'un calcul.
Il existe trois registres plus spécifiques :

#### Le registre d'état

Le registre d'état regroupe les drapeaux (en anglais *flags*). Ils servent à renseigner l'état d'exécution du processeur. Par exemple le drapeau *dépassement* s'il est mis à 1 signale qu'un dépassement de capacité est survenu, ou encore le drapeau *division par zéro* signale une division par zéro.

### Le compteur de programme

Le compteur de programme (registre **PC** pour *Program Counter*) contient l'adresse mémoire de la prochaine instruction devant être exécutée. En principe l'unité de contrôle l'incrémente de un après chaque instruction, mais certaines instructions qui permettent de se *brancher* ailleurs dans le programme modifient différemment ce registre.

### Le compteur de pile

Le compteur de pile (registre **SP** pour *Stack Pointer*) contient la position sur une pile. Cette dernière est une zone mémoire à laquelle on ne peut pas accéder aléatoirement, mais uniquement en empilant ou dépilant des éléments.

## L'unité arithmétique et logique

L'unité arithmétique et logique (UAL plus communément appelée ALU en abréviation anglaise) effectue tous les calculs arithmétiques et logiques. Quelques-uns de ces composants comme l'additionneur ont été abordés dans le chapitre *De la logique à l'arithmétique*.

### Exemple : le 6502

Le 6502, conçu en 1975, est le premier microprocesseur grand public avec un prix de 25$ (bien en-dessous des concurrents de cette époque). Une de ses premières utilisations pour le grand public fut la console de jeux vidéo Atari 2600. A partir de 1985, Nintendo équipe la NES d'une version modifiée du 6502. Il a équipé également le célèbre Apple II. Il a donné lieu à de nombreuses versions, jusqu'aux processeurs 16 bits actuels de dernière génération.

```{figure} media/6502_pad_annot_07.png
---
width: 600
height: 400
align: left
---
Ce schéma détaille l'ensemble des transistors du 6502. On voit également quelques-uns des éléments principaux (horloge, registres, etc)
```

```{admonition} Activité
:class: note

[Simulateur visuel du 6502](http://visual6502.org/JSSim/index.html)

Ce simulateur reproduit le fonctionnement complet du 6502 jusque dans l'activité de chaque transistor. On peut clairement visualiser la façon dont la complexité du fonctionnement de ce qu'on appelle communément le *cerveau* de l'ordinateur émerge de la quantité de dispositifs triviaux pris individuellement.

1. Observer le déroulement du programme proposé et tenter d'en déduire le fonctionnement. On pourra s'aider du désassembleur proposé sur la même page.
    :::{question} Question
    Que fait le programme en exemple sur le site visual6502 ?
    {f}`Il parcourt la mémoire et recopie la valeur 40 à des adresses successives.`
    {v}`Il effectue une boucle et incrémente une valeur en mémoire à l'adresse FF.`
    {f}`Il additionne deux registres et stocke le résultat dans un autre registre.`
    :::
<br> 2. Modifier ou écrire un nouveau programme en allant sur la page *Avanced*.

<!-- REVIEW/Olivier: Alors là, sérieusement, c'est super-difficile à voir ce qui se passe... Un peu en effet ! Mais bon.../CD -->

```

<br> <br>

````{admonition} Aller plus loin
:class: note

La partie qui suit présente de manière plus approfondie certaines spécificités des processeurs modernes.
````

## Processeur à noyau unique

C'est le processeur standard : un processeur à noyau unique ou CPU utilise un seul noyau à l'intérieur du processeur.

Avantages :

Un processeur à un seul cœur consomme moins d'énergie que les processeurs à plusieurs cœurs. Ceci est surtout problématique pour les appareils mobiles, oû le problème de l'autonomie de la batterie est essentiel.
Comme les processeurs à cœur unique consomment moins d'énergie, l'ensemble du système qu'ils font fonctionner chauffe moins.
Un processeur à un seul cœur est toujours adapté pour la plupart des applications : vérification du courrier, navigation sur Internet, téléchargement de données, etc. peuvent toujours être traitées par un processeur à noyau unique.

Inconvénients :

C'est un processeur relativement lent. Il n'a pas une grande puissance de calcul pour traiter de grandes opérations complexes, ou plusieurs opérations à la fois.
Comme les applications modernes nécessitent une grande puissance de traitement, un processeur monocœur qui les fait fonctionner peut se bloquer, paralysant ainsi l'ensemble du système alors « planté ».

## Processeur à double cœur

Un processeur à double cœur possède deux cœurs pour exécuter les opérations, intégrés dans un circuit unique pour se comporter comme une seule unité - un seul processeur -, à la différence d'un système multiprocesseur ; toutefois, ces cœurs possèdent leurs propres contrôleurs et caches, ce qui leur permet de travailler plus rapidement que les processeurs à cœur unique.

```{figure} media/2coeurs.png
---
width: 600
height: 400
align: left
---
Microprocesseur bicœur
```

<br> <br>

Avantages :

Un processeur double cœur exécute l'ensemble des tâches beaucoup plus rapidement. Si un processeur à noyau unique est chargé de deux tâches différentes, il ne peut pas les effectuer simultanément. Il passe à toutes les tâches une par une, en série, alors qu'un processeur à double cœur peut effectuer les deux opérations en même temps, en parallèle.
Un processeur double cœur « équivaut » à deux ordinateurs en un... mais à un tarif moindre.

Inconvénients :

Peu d'opérations nécessitent réellement la puissance des processeurs double cœur. Une grande partie de la puissance est ainsi gaspillée et vide rapidement la batterie. Un appareil mobile utilisé à des fins informatiques générales, telles que la vérification du courrier électronique, la navigation sur Internet, la saisie de documents et le partage de données, ne nécessite pas réellement la puissance d'un processeur double cœur.
Pour ces raisons, de nombreux développeurs d'applications mobiles ne programment pas leurs applications pour qu'elles fonctionnent avec des processeurs à multiple cœur, les rendant ainsi incompatibles avec les mobiles qui fonctionnent toujours avec des processeurs à double ou multiple cœur.

## Les processeurs quadricœur et autres processeurs à cœurs multiples

En termes simples, un processeur quadricœur possède quatre cœurs et il en va de même pour un processeur hexacœur (six cœurs), octocœur (huit cœurs), etc.. Ces cœurs peuvent être soit sur le même circuit intégré, soit sur le même boîtier de puce.

```{figure} media/4coeurs.png
---
width: 600
height: 400
align: left
---
Microprocesseur quadricœur
```

<br>

```{figure} media/8coeurs.png
---
width: 600
height: 400
align: left
---
Microprocesseur octocœur
```

<br> <br>

Avantages :

Le multitâche est le principal avantage des processeurs quadri ou octocœurs. Un plus grand nombre de cœurs offre évidemment une plus grande capacité à effectuer plusieurs tâches en parallèle.
Ces processeurs sont utiles pour exécuter des applications qui sont plutôt intensives et nécessitent beaucoup de ressources. Ces applications comprennent les éditeurs vidéo, les antivirus, les programmes graphiques, etc.
Les nouveaux processeurs quadricœurs consomment moins d'énergie, dégagent moins de chaleur, et sont donc très efficaces.
Ces processeurs sont en fait très en avance sur la technologie actuelle de développement d'applications mobiles, car tous les développeurs ne sont pas capables de programmer des applications fonctionnant sur ces processeurs multiples. De nombreux programmes sont encore écrits pour des processeurs à double ou simple cœur.

Inconvénients :

... encore et toujours la consommation énergétique, vidant très rapidement la batterie.

Le nombre de cœurs de processeur est important dans certaines activités comme le *gaming* : il est de plus en plus courant de trouver des processeurs hexa-cœurs, ou octo-cœurs ; [les dernières générations de multiprocesseurs possèdent jusqu'à 12 ou 16 cœurs](https://www.futura-sciences.com/tech/comparatifs/meilleur-processeur-comparatif) !

On doit également mentionner les cœurs logiques, c’est-à-dire les *threads*, comme on les appelle plus communément (tâches en français). La performance d'un monoprocesseur est jugée sur sa capacité à gérer plusieurs « fils » d'instructions. Du point de vue de l'utilisateur, ces exécutions semblent se dérouler en parallèle. Toutefois, là où chaque processus possède sa propre mémoire virtuelle, les threads d'un même processus se partagent sa mémoire virtuelle. Par contre, tous les threads possèdent leur propre pile d'exécution.

Les technologies d’hyperthreading d’Intel et de multithreading d’AMD permettent à un seul cœur physique de gérer deux tâches simultanément, fonctionnant ainsi comme deux cœurs logiques distincts. Cette technologie est aujourd'hui très performante.
La plupart de la gamme Ryzen d’AMD propose le multithreading, y compris les modèles de milieu et de haut de gamme, tandis que l’hyperthreading est pour l’instant réservé aux processeurs i7 et i9 haut de gamme d’Intel.

## Le pipeline

On l'a vu, l'exécution d'une instruction par le microprocesseur implique plusieurs opérations : accès à la mémoire en lecture et en écriture, accès aux registres en lecture et en écriture, opération logique. Pour optimiser la vitesse d'exécution, les processeurs modernes effectuent en série ces opérations. Ainsi, alors que les opérations logiques d'une instruction sont effectuées, l'instruction précédente est déjà chargée en mémoire. La difficulté de ce type d'optimisation réside dans le fait que des branchements conditionnels provoquent l'annulation des instructions déjà chargées. Pour optimiser encore ce genre de procédé, les processeurs font de la prédiction dans l'exécution. Ces optimisations sont extrêmement compliquées à gérer.

 ```{admonition} Anecdote
:class: attention
La vulnérabilité Spectre (ainsi que d'autres vulnérabilités similaires) exploite justement cette fonction de prédiction dans l'exécution de branchements conditionnels pour accéder à des emplacements mémoire auxquels le programme ne devrait en principe pas accéder.
```

<br>

````{admonition} Matière à réfléchir. Vite... très vite
:class: hint

Nous avons démontré que finalement nos ordinateurs ont un cerveau très simple dans le fonctionnement de ses éléments de base: des portes logiques qui traitent des **0** ou des **1**. Il est cependant très difficile de se représenter à quel point ces traitements vont vite.
Imaginons pour cela que le processeur écrive toutes les opérations qu'il effectue sur un ruban de papier et calculons la vitesse de défilement de ce papier. 

Pour cela, nous faisons les hypothèses suivantes:
* Les processeurs actuels ont une cadence d'horloge de 3 GHz, c'est à dire $3\cdot 10^9~[s^{-1}]$. Pour simplifier, nous allons supposer qu'ils effectuent une opération par cycle[^f1].
* Nous transcrivons un mot de 64 bits (taille standard pour les processeurs actuels) sur une longueur de 15 cm, ce qui correspond à $15 \cdot 10^{-2}~[m]$.

Le calcul devient alors:

$$
    3 \cdot 10^9~[s^{-1}] \times 15 \cdot 10^{-2}~[m] \\
    45 \cdot 10^7~[m/s]
$$

Que nous convertissons en km:

$$
    45 \cdot 10^5~[km/s]~\textrm{ou encore:}~450'000~[km/s]
$$

Rappelons que la vitesse de la lumière est :

$$
    c \cong 300'000~[km/s]
$$

Ce qui veut dire que si un microprocesseur, tel que ceux que l'on trouve dans notre ordinateur ou notre smartphone, écrivait sur un ruban de papier tout ce qu'il fait, ce ruban de papier devrait se déplacer à une fois et demi la vitesse de la lumière. Ou encore, ce ruban ferait chaque seconde plus de 11 fois le tour de la terre.

Si les éléments de base sont simples, la complexité et la richesse des expériences numériques comme l'immersion dans un jeu vidéo proviennent de la quantité extraordinaire d'opérations effectuées.

[^f1]: En fait le opérations d'un processeur prennent plus d'un cycle pour être réalisées, mais comme les processeurs ont plusieurs cœurs et un pipeline dont nous n'abordons pas ici le fonctionnement, la simplification proposée n'est pas aberrante.
````
