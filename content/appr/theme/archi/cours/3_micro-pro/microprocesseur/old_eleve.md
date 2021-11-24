# Fonctionnement du microprocesseur

On se propose à présent d'étudier le fonctionnement de base d'un processeur. On a précédemment étudié le fonctionnement des systèmes logiques à partir desquels on peut construire un processeur. L'architecture de von Neumann qui décrit la façon dont le processeur s'insère dans son environnement qui constitue un ordinateur a été abordée. Les différents éléments qui constituent le processeur et qui en assurent le bon fonctionnement vont à présent être détaillés. 

````{panels}

:img-top: media/Gordon_Moore.jpeg

Gordon Moore
^^^^^
* **Naissance** 3 janvier 1929 / San Francisco 🇺🇸 
```{dropdown} Bio
:animate: fade-in-slide-down
Gordon Earle Moore est le cofondateur d'Intel en 1968. Intel est le premier fabricant mondial de microprocesseurs. Gordon Moore est célèbre pour avoir formulé en 1965 une loi empirique portant son nom : **loi de Moore**. Cette loi prédit un doublement de la complexité, et donc du nombre de transistors présents dans les microprocesseurs tous les deux ans. Bien que nous ayons atteint certaines limites physiques au niveau atomique et des effets de bruits parasites liés aux effets quantiques et à la désintégration alpha, la loi est toujours vérifiée aujourd'hui malgré un ralentissement de la progression pour certaines caractéristiques. Ces limites sont aujourd'hui compensées par des puces intégrant de plus en plus de composants de plus en plus complexes.
```

````

```{admonition} (micro)-processeur
:class: attention
Le processeur est l'unité de traitement central de l'ordinateur. Il est construit avec des circuits regroupés en systèmes qui produisent des fonctions logiques et arithmétiques en suivant un programme et en utilisant des éléments de mémoire appelés registres.
Un microprocesseur est un processeur construit avec un circuit intégré, c'est-à-dire un dispositif qui tient sur quelques cm<sup>2</sup>. Il n'y a donc que la taille qui fasse la différence.

```


## L'horloge
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
Comme on l'a vu dans l'architecture de von Neumman, la mémoire contient le programme et les données du programme. Un programme peut donc théoriquement se modifier lui-même en se modifiant dans la mémoire, même si, en pratique, toutes les architectures modernes l'interdisent (c'est rarement un effet souhaité !).
```

L'Unité Centrale de Traitement (UCT ou CPU en anglais pour Central Processing Unit) doit accéder à la mémoire. On parle de mémoire RAM pour Random Access Memory. Le processeur peut accéder à la mémoire en lecture ou en écriture. Les deux mécanismes sont très similaires, mais avant de regarder plus en détail comment cela fonctionne, il faut d'abord définir comment la mémoire est structurée. La mémoire RAM permet, comme son nom l'indique, d'accéder à tout moment à n'importe quel emplacement.

Pour y accéder, le processeur envoie d'abord l'adresse au module mémoire, puis lit ou écrit la valeur. Pour cela le processeur dispose d'un **bus d'adressage**, appelé encore bus d'adresses. Il s'agit physiquement de câbles parallèles qui relient le processeur à la mémoire. La taille de ce bus ou sa largeur définissent le nombre de connexions parallèles et dépendent des caractéristiques du processeur et de la RAM. Chaque connexion transporte un bit, un bus de largeur 32 bits transporte 32 bits, ce qui permet de répertorier 2<sup>32</sup> adresses mémoire différentes (env. 4 Go). Le bus de données, lui, transporte les données entre le processeur et la mémoire (dans les deux sens). Ces deux bus, d'adressage et de données, ne sont pas forcément de largeur identique.


La principale différence entre le bus d’adressage et le bus de données est que le bus d’adressage permet de transférer des adresses de mémoire, tandis que le bus de données facilite l’envoi et la réception de données. Le bus d'adressage est utilisé pour spécifier une adresse physique dans la mémoire, tandis que le bus de données est utilisé pour transmettre des données entre des composants dans les deux sens. Par conséquent, le bus d'adressage est unidirectionnel tandis que le bus de données est bidirectionnel.

```{figure} media/Im58.gif
---
alt: bus de données
width: 750px
---
Bus de données et d'adresses - communication avec le CPU, les mémoires ROM et RAM et les entrées-sorties.
```



 ```{admonition} Anecdote
:class: attention
Le processeur Intel 80286 (ancêtre des processeurs Pentium), sorti en 1982, présentait un bus de données de 16 bits et un bus d'adresses de 24 bits. De plus l'adressage par segments (relativement compliqué) réduisait l'adressage physique à un adressage sur 20 bits.
```

 Il manque encore un élément : lorsque la mémoire voit une adresse apparaître elle doit pouvoir déterminer s'il s'agit d'une lecture ou d'une écriture. Pour cela deux connexions supplémentaires relient le processeur à la mémoire : une ligne *enable* et une ligne *set*. Lorsque la ligne *enable* est à 1, alors le processeur accède à la mémoire en lecture et sur le bus de données doit apparaître les données qui sont stockées dans la mémoire à l'adresse indiquée sur le bus d'adressage. Lorsque c'est la ligne *set* qui est à 1, alors la mémoire doit enregistrer les données à l'adresse indiquée.

```{admonition} Le contenu de la mémoire
:class: hint

**Les instructions** : 
la mémoire contient le programme sous forme de codes qui représentent des instructions à exécuter par le processeur. Ces codes correspondent à un jeu d'instructions propre à chaque modèle de processeur. On parle de langage machine. Pour écrire de tels programmes, on utilise un programme et un langage assembleur, proche de la machine : c'est une représentation exacte du langage machine, mais qui est une interface plus lisible dans la communication machine. C'est le langage de plus bas niveau qui représente le langage machine sous une forme lisible par un humain.


**Les données** : 
les données stockées dans la mémoire peuvent être des nombres, des lettres, des chaînes de caractères ainsi que des adresses d'autres emplacements en mémoire. On trouvera plus de détails à ce sujet dans le chapitre [*Représentation de l'information*](/content/theme/representation-information/accueil/eleve.html "Représentation de l'information").

```


```{question} Question 1
Avec un bus d'adressage de 24 bits, quelle est la taille maximum de la mémoire ? 
* {f}`32ko`
* {v}`16Mo`
* {f}`16Go`
```

```{question} Question 2
Quelle est la taille maximale de la mémoire pour un processeur 80286, sachant que l'adressage physique est finalement réduit à 20 bits ? 
* {f}`32ko`
* {f}`16Mo`
* {v}`1Mo`
```


### L'unité de contrôle
L'unité de contrôle reçoit les instructions en provenance de la RAM. Elle s'occupe d'activer les composants qui doivent l'être dans le microprocesseur.

### Les registres
Les registres permettent de stocker des valeurs, comme la RAM, mais directement à l'intérieur du processeur. Ils fonctionnent aussi en mode lecture ou écriture. C'est l'unité de contrôle qui détermine si un registre est utilisé en lecture ou en écriture avec deux fils de connexion: *enable* et *set*.
En principe ces registres stockent les informations en provenance de la mémoire ou le résultat d'un calcul.
Il existe trois registres plus spécifiques :

#### <u> Le registre d'état </u>
Le registre d'état regroupe les drapeaux (en anglais *flags*). Ils servent à renseigner l'état d'exécution du processeur. Par exemple le drapeau *dépassement* s'il est mis à 1 signale qu'un dépassement de capacité est survenu, ou encore le drapeau *division par zéro* signale une division par zéro.

### Le compteur de programme
Le compteur de programme (registre **PC** pour *Program Counter*) contient l'adresse mémoire de la prochaine instruction devant être exécutée. En principe l'unité de contrôle l'incrémente de un après chaque instruction, mais certaines instructions qui permettent de se *brancher* ailleurs dans le programme modifient différemment ce registre.

### Le compteur de pile
Le compteur de pile (registre **SP** pour *Stack Pointer*) contient la position sur une pile. Cette dernière est une zone mémoire à laquelle on ne peut pas accéder aléatoirement, mais uniquement en empilant ou dépilant des éléments.

### L'unité arithmétique et logique
L'unité arithmétique et logique (UAL plus communément appelée ALU en abréviation anglaise) effectue tous les calculs arithmétiques et logiques. Quelques-uns de ces composants comme l'additionneur ont été abordés dans le chapitre *Systèmes logiques*.


#### <u> Exemple : le 6502 </u>

Le 6502, conçu en 1975, est le premier microprocesseur grand public avec un prix de 25$ (bien en-dessous des concurrents de cette époque). Une de ses premières utilisations pour le grand public fut la console de jeux vidéo Atari 2600. A partir de 1985, Nintendo équipe la NES d'une version modifiée du 6502. Il a équipé également le célèbre Apple II. Il a donné lieu à de nombreuses versions, jusqu'aux processeurs 16 bits actuels de dernière génération.

```{figure} media/6502_pad_annot_07.png
---
alt: schémas annoté du 6502
width: 750px
---
Ce schéma détaille l'ensemble des transistors du 6502. On voit également quelques-uns des éléments principaux (horloge, registres, etc).
```

```{admonition} Activité
:class: note

[Simulateur visuel du 6502](http://visual6502.org/JSSim/index.html)

Ce simulateur reproduit le fonctionnement complet du 6502 jusque dans l'activité de chaque transistor. On peut clairement visualiser la façon dont la complexité du fonctionnement de ce qu'on appelle communément le *cerveau* de l'ordinateur émerge de la quantité de dispositifs triviaux pris individuellement.

1. Observer le déroulement du programme proposé et tenter d'en déduire le fonctionnement. On pourra s'aider du désassembleur proposé sur la même page.
    :::{question} Question
    Que fait le programme en exemple sur le site visual6502 ?
    {f}`Il parcourt la mémoire et recopie la valeur 40 à des adresses successives.`
    {v}`Il effectue une boucle et incrémente une valeur en mémoire à l'adresse FF.`
    {f}`Il additionne deux registres et stocke le résultat dans un autre registre.`
    :::
<br> 2. Modifier ou écrire un nouveau programme en allant sur la page *Avanced*.

<!-- REVIEW/Olivier: Alors là, sérieusement, c'est super-difficile à voir ce qui se passe... Un peu en effet ! Mais bon.../CD -->

```
## Pour aller plus loin

Les microprocesseurs modernes ajoutent quelques éléments de complexité qui n'ont pas été exposés ici. Il s'agit notamment des éléments suivants.

### Les processeurs multi-cœurs

Alors que dans les processeurs jusqu'ici évoqués, il n'y avait qu'une seule unité arithmétique et logique, ce qui limitait le processeur à une opération par cycle d'horloge, l'industrie fournit aujourd'hui des microprocesseurs qui sont capables d'effectuer plusieurs opérations simultanément. Pour cela, ces derniers sont dotés de plusieurs cœurs capables d'effectuer chacun une opération. Si cette mise en parallèle des opérations ne se fait pas sans difficultés, elle offre toutefois la possibilité de palier en particulier aux problèmes d'élévation de température dues à l'augmentation de la fréquence, pour des sollicitations importantes de processeurs monocœurs (c'est à dire des calculs lourds), en réduisant sensiblement la consommation énergétique, paramètre particulièrement d'importance aujourd'hui.



### Le pipeline

On l'a vu, l'exécution d'une instruction par le microprocesseur implique plusieurs opérations : accès à la mémoire en lecture et en écriture, accès aux registres en lecture et en écriture, opération logique. Pour optimiser la vitesse d'exécution, les processeurs modernes effectuent en série ces opérations. Ainsi, alors que les opérations logiques d'une instruction sont effectuées, l'instruction précédente est déjà chargée en mémoire. La difficulté de ce type d'optimisation réside dans le fait que des branchements conditionnels provoquent l'annulation des instructions déjà chargées. Pour optimiser encore ce genre de procédé, les processeurs font de la prédiction dans l'exécution. Ces optimisations sont extrêmement compliquées à gérer.

 ```{admonition} Anecdote
:class: attention
La vulnérabilité Spectre (ainsi que d'autres vulnérabilités similaires) exploite justement cette fonction de prédiction dans l'exécution de branchements conditionnels pour accéder à des emplacements mémoire auxquels le programme ne devrait en principe pas accéder.
```
