Microprocesseur
===============

Dans ce chapitre, nous allons explorer le fonctionnement de base d'un processeur. Nous avons précédemment vu le fonctionnement des systèmes logiques à partir desquels nous pouvons construire un processeur. Nous avons également exposé l'architecture de von Neumann qui décrit la façon dont le processeur s'insère dans son environnement qui constitue un ordinateur. Ici, nous allons détailler les différents éléments qui constituent le processeur et qui en assurent le bon fonctionnement. 

````{panels}

:img-top: media/Gordon_Moore.jpeg

Gordon Moore
^^^^^
* **Naissance** 3 janvier 1929 / San Francisco 🇺🇸 
```{dropdown} Bio
:animate: fade-in-slide-down
Gordon Earle Moore est le cofondateur d'Intel en 1968. Intel est le premier fabricant mondial de microprocesseurs. Gordon Moore est célèbre pour avoir formulé en 1965 une loi empirique portant son nom: **loi de Moore**. Cette lois prédit un doublement de la complexité, et donc du nombre de transistors présents dans les microprocesseurs tous les deux ans. Bien que nous ayons atteint certaines limites physique au niveau atomique et des effets de bruits parasites liés aux effets quantique et à la désintégration alpha, la loi est toujours vérifiée aujourd'hui malgré un ralentissement de la progression pour certaines caractéristiques. Ces limites sont aujourd'hui compensées par des puces intégrant de plus en plus de composants de plus en plus complexes.
```

````

```{admonition} (micro)-processeur
:class: attention
Le processeur est l'unité de traitement centrale de l'ordinateur. Il est construit avec des circuits regroupés en systèmes qui produisent des fonctions logiques et arithmétiques en suivant un programme et en utilisant des éléments de mémoire appelés registres.
Un microprocesseur est un processeur construit avec un circuit intégré, c'est à dire une dispositif qui tient sur quelques cm<sup>2</sup>. Il n'y a donc que le taille qui fasse la différence.

```


## L'horloge
Un processeur est un dispositif synchrone, ce qui signifie que les opérations à l'intérieur du processeur se déroulent de manière synchrone à un temps donné. Pour assurer cette simultanéité, il faut comme pour un orchestre, donner le tempo. Cette fonction de métronome est assurée par une horloge, ou un signal d'horloge. Cette horloge est constituée d'un simple signal carré dont la fréquence atteint aujourd'hui plusieurs giga Herz, c'est-à-dire plusieurs milliards de cycles par seconde.

```{admonition} La notion de *synchrone*
:class: attention
<span commented>La notion de synchronicité est fondamentale</span><!-- REVIEW/JPP: à mon avis, ils n'en comprennent rien -->. Sans entrer dans les détails ici, il faut relever que dans un système synchrone il est possible d'assurer une coordination et une cohérence des opérations, ce qui est impossible autrement. Cet aspect devient crucial dans les systèmes distribués qui ne disposent plus de la garantie de synchronicité.
```

## L'accès à la mémoire

```{admonition} Rappel
:class: danger
Comme on l'a vu dans l'architecture de vonNeumman, la mémoire contient le programme et les données du programme. Un programme peut donc se <span commented>modifier lui-même</span><!-- REVIEW/JPP: en pratique, toutes les architectures modernes l'interdisent --> en se modifiant dans la mémoire (c'est rarement un effet souhaité).
```

L'Unité Centrale de Traitement (UCT ou CPU en anglais pour Central Processing Unit) doit accéder à la mémoire. On parle de mémoire RAM pour Random Access Memory. Le processeur peut accéder à la mémoire en lecture ou en écriture. Les deux mécanismes sont très similaires, mais avant de regarder plus en détail comment cela fonctionne, il faut d'abord définir comment la mémoire est structurée. La mémoire RAM permet, comme son nom l'indique, d'accéder à tout moment à n'importe quel emplacement.

TODO: illustration

Pour y accéder, le processeur envoie d'abord l'adresse au module mémoire, puis lis ou écrit la valeur. Pour cela le processeur dispose d'un **bus d'adressage**. Il s'agit physiquement de câbles parallèles qui relient le processeur à la mémoire. La taille de ce bus ou sa largeur définit le nombre de connexions parallèles et dépend des caractéristiques du processeur et de la RAM. Chaque connexion transporte un bit, un bus de largeur 32 bit transporte 32 bits ce qui permet d'adresser 2<sup>32</sup> adresses mémoire (env. 4 Go). Le bus de données lui transporte les données entre le processeur et la mémoire (dans les deux sens). Ces deux bus, adresses et données, ne sont pas forcément de largeur identique.

 TODO: illustration

 ```{admonition} Anecdote
:class: attention
Le processeur Intel 80286 (ancêtre des processeurs Pentium),  sorti en 1982, présentait un bus de données de 16 bits et un bus d'adresses de 24 bits. De plus l'adressage par segments (relativement compliqué) réduisait l'adressage physique à un adressage sur 20 bits.
```

 Il nous manque encore un élément : lorsque la mémoire voit une adresse apparaître elle doit pouvoir déterminer s'il s'agit d'une lecture ou d'une écriture. Pour cela deux connexions supplémentaires relie le processeur à la mémoire: une ligne *enable* et une ligne *set*. Lorsque la ligne *enable* est à 1, alors le processeur accède à la mémoire en lecture et sur le bus de donnée doit apparaître les données qui sont stockées dans la mémoire à l'adresse indiquée sur le bus d'adressage. Lorsque c'est la ligne *set* qui est à 1, alors la mémoire doit enregistrer les données à l'adresse indiquée.

```{admonition} Le contenu de la mémoire
:class: hint

**Les instructions** : 
La mémoire contient le programme sous-forme de codes qui représentent des instructions à exécuter par le processeur. Ces codes correspondent à un jeu d'instruction propre à chaque modèle de proceseur. On parle de langage machine. Pour écrire de tels programme, on utilise un logiciel de type assembleur qui traduit les codes dans une représentation plus lisible.

**Les données** : 
Les données stockées dans la mémoire peuvent être des nombres, des lettres, des chaînes de caractères ainsi que des adresses d'autres emplacement en mémoire. On trouvera plus de détails à ce sujet dans le chapitre [Représentation de l'information](/content/theme/representation-information/accueil/eleve.html "Représentation de l'information").

```


 ### Exercice

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


## L'unité de contrôle
L'unité de contrôle reçoit les instructions en provenance de la RAM. Elle s'occupe d'activer les composants qui doivent l'être dans le microprocesseur.

## Les registres
Les registres permettent de stocker des valeurs, comme la RAM, mais directement à l'intérieur du processeur. Ils fonctionnent aussi en mode lecture ou écriture. C'est l'unité de contrôle qui détermine si un registre est utilisé en lecture ou en écriture avec deux fil de connexion : *enable* et *set*.
En principe ces registres stockent les informations en provenance de la mémoire ou le résultat d'un calcul.
Il existe trois registre plus spécifiques:

### Le registre d'état
Le registre d'état regroupe les drapeaux (en anglais flags). Ils servent à renseigner l'état d'exécution du processeur. Par exemple le drapeau *dépassement* s'il est mis à 1 signal qu'un dépassement de capacité et survenu, ou encore le drapeau *division par zéro* signal une division par zéro.

### Le compteur de programme
Le compteur de programme (registre **PC** pour *Program Counter*) contient l'adresse mémoire de la prochaine instruction devant être exécutée. En principe l'unité de contrôle l'incrémente de un après chaque instruction, mais certaines instructions qui permettent de se *brancher* ailleurs dans le programme modifient différemment ce registre.

### Le compteur de pile
Le compteur de pile (registre **SP** pour *Stack Pointer*) contient la position sur une pile. Cette dernière est une zone mémoire à laquelle on ne peut pas accéder aléatoirement, mais uniquement en empilant ou dépilant des éléments.

## L'unité arithmétique et logique
L'unité arithmétique et logique (UAL plus communément appelée ALU en abréviation anglaise) effectue tous les calculs arithmétiques et logiques. Nous avons vu quelques un de ces composants comme l'additionneur dans la partie sur les systèmes logiques.



## Exemple: le 6502

Le 6502, conçu en 1975, est le premier microprocesseur grand public avec un prix de 25$ (bien en-dessous des concurrents de cette époque). Une de ses première utilisation pour le *grand public* fut la console de jeux vidéo Atari 2600. A partir de 1985, Nintendo équipe la NES d'une version modifiée du 6502. Il <span commented>équipe</span><!-- REVIEW/JPP: temps du verbe --> aussi le célèbre Apple II. Il est encore fabriqué et commercialisé en <span commented>2014</span><!-- REVIEW/JPP: et maintenant? -->.

```{figure} media/6502_pad_annot_07.png
---
alt: schémas annoté du 6502
width: 200px
---
Ce schémas détaille l'ensemble des transistors du 6502. On voit également quelques-uns des éléments principaux (horloge, registres, etc).
```

```{admonition} Activité
:class: note

[Simulateur visuel du 6502](http://visual6502.org/JSSim/index.html)

Ce simulateur reproduit le fonctionnement complet du 6502 jusque dans l'activité de chaque transistor le composant. On peut clairement visualiser la façon dont la complexité du fonctionnement de ce que l'on appelle communément le *cerveau* de l'ordinateur émerge de la quantité de dispositifs triviaux pris individuellement.

1. Observer le déroulement du programme proposé et tenter d'en déduire le fonctionnement. On pourra s'aider du désassembleur proposé sur la même page.
:::{question} Question
Que fait le programme en exemple sur le site visual6502 ?
* {f}`Il parcourt la mémoire et recopie la valeur 40 à des adresses successives`
* {v}`Il effectue une boucle et incrémente une valeur en mémoire à l'adresse FF`
* {f}`Il additionne deux registres et stocke le résultat dans un autre registre`
:::

2. Modifier ou écrire un nouveau programme en allant sur la page *Avanced*.

```


## Pour aller plus loin
Les microprocesseurs modernes ajoutent quelques éléments de complexité que nous n'avons pas exposés ici. Il s'agit notamment des éléments suivants.
### Les multi-coeurs
Alors que dans le processeur que nous avons présenté, il n'y avait qu'une seule unité arithmétique et logique, ce qui limitait notre processeur à une opération par cycle d'horloge, l'industrie fournit aujourd'hui des microprocesseurs qui sont capables d'effectuer plusieurs opérations simultanément. Pour cela, ces derniers sont dotés de plusieurs coeurs capable d'effectuer chacun une opération. Mais cette mise en parallèle des opérations ne se fait pas sans difficultés. De la même manière qu'il serait extrêmement difficile pour plusieurs personnes d'écrire un texte en tenant le même stylo, il est compliqué de partager un calcul entre plusieurs unités de traitement.
### Le pipeline
Comme nous l'avons vu, l'exécution d'une instruction par le microprocesseur implique plusieurs opérations : accès à la mémoire en lecture et en écriture, accès aux registres en lecture et en écriture, opération logique. Pour optimiser la vitesse d'exécution, les processeurs modernes effectue en série ces opérations. Ainsi alors que les opérations logiques d'une instruction sont effectuées, l'instruction précédente est déjà chargée en mémoire. La difficulté de ce type d'optimisation réside dans le fait que des branchements conditionnels provoquent l'annulation des instructions déjà chargées. Pour optimiser encore ce genre de procédé, les processeur font de la prédiction dans l'exécution. Ces optimisations sont extrêmement compliquées à gérer.
 ```{admonition} Anecdote
:class: attention
La vulnérabilité Spectre (ainsi que d'autres vulnérabilités similaires) exploite justement cette fonction de prédiction dans l'exécution de branchement conditionnels pour accéder à des emplacements mémoire auxquels le programme ne devrait en principe pas accéder.
```
