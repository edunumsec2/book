# Introduction

```{admonition} Attention
:class: note
Ce document doit être retravaillé ...
```

Dans ce chapitre, nous aborderons la question de l'architecture des ordinateurs, c'est-à-dire les multiples couches physiques qui rendent possibles des opérations numériques aussi complexes que celles qu'effectuent à chaque instant nos smartphones. 

Comme vous avez pu le voir dans le chapitre lié à la représentation de l'information, tout ce qui apparaît sur votre écran est représenté par l'ordinateur par suite de 0 et de 1. Pour comprendre comment ces {glo}`codebinaire|0 et 1` sont traités par l'ordinateur, il faut avoir en tête que les ordinateurs sont construits à partir d'une couche et de multiples niveaux, comme un mille-feuille, dont chacun possède ses propres règles. 


```{figure} media/abstractionlight.png
---
height: 400px
width: 250px
align: left
---
Les différents niveaux d'abstraction de l'informatique, en partant des électrons, jusqu'aux «programmes» 
```

<!---
```{image} media/abstractionlight.png
:width: 500
:height: 550
```
Les différents niveaux d'abstraction de l'informatique, en partant des électrons, jusqu'aux «programmes»
-->

<br>


Dans ce chapitre, nous nous concentrerons sur les couches de bas niveau, et tenterons de remonter progressivement jusqu'aux couches logicielles. 


## De quoi sont faits les nombres binaires? 

Les ordinateurs ne comprennent que les nombres binaires. La lettre «A», par exemple, est pour ces derniers une suite de 0 et de 1. Même chose pour une image, une vidéo, une chanson et ainsi de suite. Mais alors comment ces 0 et ces 1 sont-ils {glo}`stockage|stockés` et manipulés physiquement par les ordinateurs ? De quelle matière sont-ils faits ? Un indice : que mettez-vous dans votre smartphone pour le faire fonctionner : de l'essence ? Du gaz ? De l'énergie solaire ?

De l'électricité  !


```{figure} media/iphonecpu.jpeg
---
height: 350px
width: 500px
align: left
---
Vos photos, vos vidéos, vos messages, tout ce que vous consultez sur votre téléphone portable, sont traitées par un processeur similaire au modèle A9 de Apple, commercialisé dans les iPhone SE. 
```

<!---
```{image} media/iphonecpu.jpeg
:width: 600
:height: 500
```
Photos, vidéos, messages, tout ce qui est consulté sur un téléphone portable, est traité par un processeur similaire au modèle A9 de Apple, commercialisé dans les iPhone SE

-->

<br> <br>


```{figure} media/datacenter.jpeg
---
height: 350px
width: 500px
align: left
---
Vos likes, vos partages, vos vidéos transmises via des applications telles que WhatsApp, Instagram, TikTok, Snapchat, YouTube, sont stockées dans des centres de données aux quatre coins de la planète. 
```

<!---

```{image} media/datacenter.jpeg
:width: 600
:height: 500
```
Likes, partages, vidéos transmises via des applications telles que WhatsApp, Instagram, TikTok, Snapchat, YouTube, etc. : tout est stocké dans des centres de données (Data Center) aux quatre coins de la planète

-->

## Électricité et nombres binaires

Les nombres binaires, au niveau le plus élémentaire, sont matérialisés par des <span commented>courants électriques</span><!-- REVIEW/JPP: discussion courant vs tension? -->, qui traversent les circuits des ordinateurs. Mais pourquoi avoir choisi des 0 et des 1 comme alphabet ? Quel rapport avec l'électricité ?

En informatique, si nous avons choisi d'utiliser un code binaire, ça n'est pas par hasard. Ce sont les deux signaux les plus élémentaires que l'on puisse transmettre avec l'électricité. Soit le courant passe, soit il ne passe pas. Ouvert ou fermé ; allumé ou éteint ; 1 ou 0. 

```{didyouknow}

On aurait pu choisir un code possédant plus de deux signaux différents. Par exemple, avec trois signaux, on pourrait coder trois valeurs avec un courant faible, un courant moyen, un courant fort, ou encore mieux : une tension négative, une tension nulle et une tension positive. On appelle cette dernière proposition le ternaire balancé. En fait, cela s'est déjà fait: les soviétiques ont développé en 1958 un ordinateur nommé [Setun](https://en.wikipedia.org/wiki/Setun) basé sur ce principe, réputé très fiable et extrêmement peformant dans le développement d'applications dans certains domaines.  Mais ce projet, pour des raisons politiques, n'a pas reçu le soutient qu'il aurait mérité. D'autre part, il est plus simple de concevoir des circuits électroniques qui ne doivent traiter que deux valeurs.
```

La grande idée derrière la conception des ordinateurs et de leurs circuits électroniques repose sur l'utilisation de sortes d'« interrupteurs automatiques ». Ce composant fonctionne donc comme un interrupteur (en laissant ou non passer le courant sur un fil donné), mais de façon automatique: ce n'est pas un humain qui doit venir commuter l'interrupteur, mais l'interrupteur commute automatiquement en fonction de si oui ou non du courant passe sur un _autre_ fil du système. Historiquement, on a réalisé que si l'on disposait d'un tel composant, on pouvait en assembler plusieurs (en fait, plusieurs milliers) et ainsi construire des systèmes à même de manipuler des données représentées par des 0 et des 1. Nous allons voir comment dans les prochaines sections.

Dans les premiers ordinateurs entre les années 1950 et 1960, ce sont les [tubes à vide](https://fr.wikipedia.org/wiki/Tube_électronique) qui ont rempli cette fonction. Mais les tubes à vides étaient gros, consommaient beaucoup d'électricité, et avaient une durée de vie limitée : il fallait souvent les changer, un peu comme de vieilles ampoules à incandescence. En utilisant des tubes à vide, on pouvait certes construire des ordinateurs, mais certainement pas ceux que l'on connaît aujourd'hui.


```{figure} media/vaccum_tubes.jpeg
---
height: 350px
align: left
---
Différents modèles de tubes à vide. Photographie de Stefan Riepl, 2008, CC BY-SA.
```


<!---
```{image} media/vaccum_tubes.jpeg
:width: 500
:height: 300
```
Différents modèles de tubes à vide. Photographie de Stefan Riepl, 2008, CC BY-SA
-->

<br>


Il a fallu attendre une invention majeure pour permettre aux ordinateurs de se miniaturiser, de consommer moins, d'être plus efficaces et fiables, pour finalement arriver à ce qu'on a appelé dès la fin des années 1970 des **PC** : des _personal computers_, des ordinateurs personnels. L'invention qui a permis cette évolution est le **transistor**.

## Le transistor

Le {glo}`transistor|transistor` est aujourd'hui la brique de base de construction des systèmes informatiques. Il a été développé dans les années 1940 dans les [laboratoires Bell](https://fr.wikipedia.org/wiki/Laboratoires_Bell), aux Etats-Unis. Ce n'est que vers la fin des années 1950 que l'on commence à construire des ordinateurs commerciaux qui utilisent des transistors plutôt que des tubes à vide. Le transistor est à l'origine d'une révolution dans la taille, la fiabilité, et les performances générales des ordinateurs de l'époque. 


```{figure} media/transistor.jpeg
---
height: 350px
width: 500px
align: left
---
Différents modèles de transistor. On les reconnaît à leurs trois «pattes» aussi appelées: émetteur, base, collecteur. 
```

<br> <br>


<span commented>Le transistor, comme le tube à vide qu'il remplace, fonctionne comme un interrupteur automatique. Il laissera ou non passer du courant entre deux de ses pattes en fonction de ce qui se passe sur sa troisième. On peut aussi le comparer à un robinet d'eau qui peut être ouvert ou fermé, et qu'on peut ouvrir ou fermer automatiquement sans devoir l'activer manuellement. 


```{figure} media/transistorgif.gif
---
height: 350px
width: 500px
align: left
---
En appliquant un courant qui va de la base à l'émetteur (en rose pâle), on permet au courant de circuler entre le collecteur et l'émetteur (appelés ainsi parce que l'émetteur *émet* des électrons, et le collecteur les *collecte*). Envoyer du courant dans la base, c'est donc *ouvrir* le transistor; ne plus en envoyer a, inversement, l'effet de *fermer* le transistor. 
```

En appliquant un courant qui va de la base à l'émetteur (en rose pâle), on permet au courant de circuler entre le collecteur et l'émetteur (appelés ainsi parce que l'émetteur *émet* des électrons, et le collecteur les *collecte*). Envoyer du courant dans la base, c'est donc *ouvrir* le transistor ; ne plus en envoyer a, inversement, l'effet de *fermer* le transistor

<br>


De par sa capacité à être ouvert ou fermé, le transistor fonctionne comme une brique fondamentale dans la construction de systèmes informatiques permettant de {glo}`transmission|transmettre`, stocker et {glo}`traitement|traiter` des nombres binaires. 


````{dropdown} Pour aller plus loin
Les transistors sont faits avec des matériaux dit « semi-conducteurs ». Voici une vidéo qui explique en détail ce qui se passe dans ces semi-conducteurs et qui permet de faire fonctionner un transistor.
```{youtube} 33vbFFFn04k
```
````


:::{card}
Des transistors presque invisibles
^^^
Chercher à se représenter la taille des transistors utilisés dans les microprocesseurs actuels n'a pas d'intérêt tellement ils sont petits. À titre d'exemple, disons simplement que le microprocesseur Apple A9 en possède six milliards.
````{dropdown} Zoom sur un transistor
```{youtube} Fxv3JoS1uY8
```
````
:::

## Des transistors aux systèmes logiques

Il reste difficile de concevoir des circuits d'ordinateurs en réfléchissant en termes de transistors. Un transistor seul ne peut représenter ou traiter qu'un bit d'information. Oui ou non, ouvert ou fermé, 1 ou 0.

Dans le chapitre suivant, où nous commençons à voir comment sont conçus les circuits électroniques des ordinateurs, nous parlerons tout d'abord de **{glo}`portelogique|portes logiques`**. Ce sont des composants qui sont eux-mêmes constitués de plusieurs transistors. Réfléchir en termes de portes logiques permet de véritablement concevoir les circuits des ordinateurs qui vont manipuler les bits d'informations formant nos données.