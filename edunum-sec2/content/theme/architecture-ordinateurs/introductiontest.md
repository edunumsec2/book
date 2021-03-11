# Introduction

Dans ce chapitre, nous aborderons la question de l'**architecture des ordinateurs**, c'est à dire les multiples couches physiques qui rendent possibles des opérations numériques aussi complexes que celles qu'effectuent à chaque instant nos smartphones. 

Comme vous avez pu le voir dans le chapitre lié à la **représentation de l'information** tout ce qui apparaît sur votre écran n'est qu'une suite de 0 et de 1. Pour comprendre comment ces **nombres binaires** sont traités par l'ordinateur, il faut avoir en tête que les ordinateurs sont construits en plusieurs **couches** successives, comme un mille feuille, dont chacune possède ses propres règles. 

```{figure} media/abstractionlight.png
---
height: 400px
width: 250px
---
Les différents niveaux d'abstraction de l'informatique, en partant des électrons, jusqu'aux "programmes", que l'on appelle aussi aujourd'hui "applications". 
```
Dans ce chapitre nous nous concentrerons sur les couches de **bas niveau**, et tenterons de remonter progressivement jusqu'aux **couches logicielles**. 


## De quoi sont faits les nombres binaires ? 

Les ordinateurs ne comprennent que les nombres binaires. La lettre "A", par exemple, est pour ces derniers une suite de 0 et de 1. Même chose pour une image, une vidéo, une chanson, et ainsi de suite. Mais alors comment ces 0 et ces 1 sont-ils stockés et manipulés physiquement ? De quelle matière sont-ils faits ? Un indice : que mettez-vous dans votre smartphone pour le faire fonctionner ? De l'essence ? Du gaz ? De l'énergie solaire ? 

De l'électricité.

```{figure} media/iphonecpu.jpeg
---
height: 350px
width: 500px
---
Vos photos, vos vidéos, vos messages, tout ce que vous consultez sur votre téléphone portable, sont traitées par un processeur similaire au modèle A9 de Apple, commercialisé dans les iPhone SE. 
```

```{figure} media/datacenter.jpeg
---
height: 350px
width: 500px
---
Vos likes, vos partages, vos vidéos transmises via des applications telles que Whatsapp, Instagram, Tik Tok, Snapchat, Youtube, sont stockées dans des centres de données aux quatre coins de la planète. 
```

## Comment sont-ils stockés ? 

Les nombres binaires, au niveau le plus élémentaire, sont donc de l'électricité. Mais pourquoi avoir choisi des 0 et des 1 comme alphabet ? Quel rapport avec l'électricité ? 

En informatique, si nous avons choisi d'utiliser un code binaire ça n'est pas par hasard. Ce sont les deux signaux les plus élémentaires que l'on puisse transmettre avec l'électricité. Soit le courant passe, soit il ne passe pas. Ouvert ou fermé, allumé ou éteint, 1 ou 0. 

```{panels}
:column: col-lg
Pourquoi pas un code ternaire ? 
^^^
On aurait pu choisir un code possédant plus que deux signaux différents. Si on choisissait, par exemple, trois signaux, on pourrait les coder par l'électricité en mesurant : un courant faible, un courant moyen, un courant fort. Le problème est qu'on augmente ainsi les possibilités de se tromper dans la mesure, et d'interpréter un courant moyen pour un courant fort, ou inversément. Puisque l'électricité permet une vitesse de transmission par signal très grande, il était plus optimal de garder deux positions clairement distinctes que l'on pouvait transmettre très vite, plutôt que trois positions avec un risque de confusion plus élevé. 
```

## Le transistor

Le transistor est la brique de base de construction des systèmes informatiques. Développé dans les années 1940 dans les [laboratoires Bell](https://fr.wikipedia.org/wiki/Laboratoires_Bell), aux Etats-Unis, ce composant électronique est à l'origine d'une révolution dans la taille, la fiabilité, et les performances générales des ordinateurs de l'époque. 

```{figure} media/transistor.jpeg
---
height: 350px
width: 500px
---
Différents modèles de transistor. On les reconnaît à leurs trois "pattes" aussi appelées : émetteur, base, collecteur. 
```

Le transistor fonctionne comme un robinet d'eau qui peut être ouvert ou fermé. Si on l'ouvre le courant passe, si on le ferme il ne passe pas. 

```{figure} media/transistorgif.gif
---
height: 350px
width: 500px
---
En appliquant un courant sur la **base** du transistor, on permet au courant de circuler entre le collecteur et l'émetteur (appelés ainsi parce que l'émetteur *émet* des électrons, et le collecteur les *collecte*). Envoyer du courant dans la **base** c'est donc "ouvrir" le transistor. 
```

De par sa capacité à être ouvert ou fermé, le transistor fonctionne comme une brique fondamentale dans la construction de systèmes informatiques permettant de transmettre, stocker et manipuler des suites de 0 et de 1. 


```{panels}
:column: col-lg
Des transistors presque invisibles
^^^
Donner une idée de la taille des transistors utilisés dans les microprocesseurs actuels n'a même plus d'intérêt tellement ils sont petits. À titre d'exemple, disons simplement que le microprocesseur Apple A9 de la figure 35 en possède six milliards. 
```

## Des transistors aux portes logiques

Un transistor seul ne peut représenter qu'un bit d'information. Oui ou non, ouvert ou fermé, 1 ou 0. Mais si l'on rassemble plusieurs transistors, on peut construire des systèmes logiques qui nous permettent d'exprimer des relations logiques plus avancées, comme la conjonction, la disjonction, la négation. C'est ce qu'on appelle des **portes logiques**. 

```{figure} media/andgate.svg
---
height: 100px
width: 200px
---
Ceci est une porte logique "ET", qui exprime la conjonction. C'est à dire que les deux transistors qui la composent (A & B) doivent être "ouvert" pour que le courant passe. 
```
En connectant entre eux les transistors de diverses manières, on est capable de faire que le courant se déplace dans un circuit de façon maîtrisée. Ce qui nous permet, à terme, de construire des programmes qui génèrent certaines "sorties" quand on leur donne certaines "entrées". 

```{figure} media/andgatetransistor.png
---
height: 300px
width: 200px
---
Voilà le schéma de construction d'une porte logique "ET", à partir de deux transistors. Si les deux transistors sont "ouverts", le courant passe. 
```



