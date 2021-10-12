# Introduction

Dans ce chapitre, nous aborderons la question de l'architecture des ordinateurs, c'est à dire les multiples couches physiques qui rendent possibles des opérations numériques aussi complexes que celles qu'effectuent à chaque instant nos smartphones. 

Comme vous avez pu le voir dans le chapitre lié à la représentation de l'information, tout ce qui apparaît sur votre écran est représenté par l'ordinateur par suite de 0 et de 1. Pour comprendre comment ces <span commented>{glo}`codebinaire|nombres binaires`</span><!-- REVIEW/JPP: pas nombres --> sont traités par l'ordinateur, il faut avoir en tête que les ordinateurs sont <span commented>construits</span><!-- REVIEW/JPP: pour moi, ils ne sont pas construits comme ça. Il n'y a qu'une seule couche, à la base. Mais on y réfléchit selon plusieurs niveaux --> en plusieurs couches successives, comme un mille-feuille, dont chacune possède ses propres règles. 

```{figure} media/abstractionlight.png
---
height: 400px
width: 250px
---
Les différents niveaux d'abstraction de l'informatique, en partant des électrons, jusqu'aux «programmes», <span commented>que l'on appelle aussi aujourd'hui «applications»</span><!-- REVIEW/JPP: pas la même chose -->. 
```
Dans ce chapitre, nous nous concentrerons sur les couches de bas niveau, et tenterons de remonter progressivement jusqu'aux couches logicielles. 


## De quoi sont faits les nombres binaires? 

Les ordinateurs ne comprennent que les {glo}`codebinaire|nombres binaires`. La lettre «A», par exemple, est pour ces derniers une suite de 0 et de 1. Même chose pour une image, une vidéo, une chanson et ainsi de suite. Mais alors comment ces 0 et ces 1 sont-ils {glo}`stockage|stockés` et manipulés physiquement par les ordinateurs? De quelle matière sont-ils faits? Un indice: que mettez-vous dans votre smartphone pour le faire fonctionner? De l'essence? Du gaz? De l'énergie solaire? 

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
Vos likes, vos partages, vos vidéos transmises via des applications telles que WhatsApp, Instagram, TikTok, Snapchat, YouTube, sont stockées dans des centres de données aux quatre coins de la planète. 
```

## Électricité et nombres binaires

Les {glo}`codebinaire|nombres binaires`, au niveau le plus élémentaire, sont matérialisés par des <span commented>courants électriques</span><!-- REVIEW/JPP: discussion courant vs tension? -->, qui traversent les circuits des ordinateurs. Mais pourquoi avoir choisi des 0 et des 1 comme alphabet? Quel rapport avec l'électricité? 

En informatique, si nous avons choisi d'utiliser un {glo}`codebinaire|code binaire`, ça n'est pas par hasard. Ce sont les deux signaux les plus élémentaires que l'on puisse transmettre avec l'électricité. Soit le courant passe, soit il ne passe pas. Ouvert ou fermé; allumé ou éteint; 1 ou 0. 

```{admonition} Le saviez-vous?
:class: hint
On aurait pu choisir un code possédant plus de deux signaux différents. Si on choisissait, par exemple, trois signaux, on pourrait les coder par l'électricité en mesurant un courant faible, un courant moyen, un courant fort. En fait, cela s'est fait: les Soviétiques ont développé en 1958 un ordinateur nommé [Setun](https://en.wikipedia.org/wiki/Setun) basé sur ce principe. Mais le problème est qu'on augmenterait ainsi les possibilités de se tromper dans la mesure, et d'interpréter un courant moyen pour un courant fort, ou inversément. Puisque l'électricité permet une vitesse de transmission par signal très grande, il est plus performant de garder deux positions clairement distinctes que l'on peut transmettre très vite, plutôt que trois positions avec un risque de confusion plus élevé. D'autre part, c'est plus simple de concevoir des circuits électroniques qui ne doivent traiter que deux valeurs.
```

La grande idée derrière la conception des ordinateurs et de leur circuits électroniques repose sur l'utilisation de sortes d'«interrupteurs automatiques». Ce composant fonctionne donc comme un interrupteur (en laissant ou non passer le courant sur un fil donné), mais de façon automatique: ce n'est pas un humain qui doit venir commuter l'interrupteur, mais l'interrupteur commute automatiquement en fonction de si oui ou non du courant passe sur un _autre_ fil du système. Historiquement, on a réalisé que si l'on disposait d'un tel composant, on pouvait en assembler plusieurs (en fait, plusieurs milliers) et ainsi construire des systèmes à même de manipuler des données représentées par des 0 et de 1. Nous allons voir comment dans les prochaines sections.

Dans les premiers ordinateurs entre les années 1950 et 1960, ce sont les [tubes à vide](https://fr.wikipedia.org/wiki/Tube_électronique) qui ont rempli cette fonction. Mais les tubes à vides étaient gros, consommaient beaucoup d'électricité, et avaient une durée de vie limitée: il fallait souvent les changer, un peu comme de vieilles ampoules à incandescence. En utilisant des tubes à vide, on pouvait certes construire des ordinateurs, mais certainement pas ceux que l'on connaît aujourd'hui.


```{figure} media/vaccum_tubes.jpeg
---
height: 350px
---
Différents modèles de tubes à vide. Photographie de Stefan Riepl, 2008, CC BY-SA.
```


Il a fallu attendre une invention majeure pour permettre aux ordinateurs de se miniaturiser, de consommer moins, d'être plus efficaces et fiables, pour finalement arriver à ce qu'on a appelé dès la fin des années 1970 des **PC**: des _personal computers_, des ordinateurs personnels. L'invention qui a permis cette évolution est le **transistor**.

## Le transistor

Le {glo}`transistor|transistor` est aujourd'hui la brique de base de construction des systèmes informatiques. Il a été développé dans les années 1940 dans les [laboratoires Bell](https://fr.wikipedia.org/wiki/Laboratoires_Bell), aux Etats-Unis. Ce n'est que vers la fin des années 1950 que l'on commence à construire des ordinateurs commerciaux qui utilisent des transistors plutôt que des tubes à vide. Le transistor est à l'origine d'une révolution dans la taille, la fiabilité, et les performances générales des ordinateurs de l'époque. 

```{figure} media/transistor.jpeg
---
height: 350px
width: 500px
---
Différents modèles de transistor. On les reconnaît à leurs trois «pattes» aussi appelées: émetteur, base, collecteur. 
```

<span commented>Le {glo}`transistor|transistor`, comme le tube à vide qu'il remplace, fonctionne comme un interupteur automatique. Il laissera ou non passer du courant entre deux de ses pattes en fonction de ce qui se passe sur sa troisième patte. On peut aussi le comparer à un robinet d'eau qui peut être ouvert ou fermé, et qu'on peut ouvrir ou fermer automatiquement sans devoir l'activer manuellement. 

```{figure} media/transistorgif.gif
---
height: 350px
width: 500px
---
En appliquant un courant qui va de la base à l'émetteur (en rose pâle), on permet au courant de circuler entre le collecteur et l'émetteur (appelés ainsi parce que l'émetteur *émet* des électrons, et le collecteur les *collecte*). Envoyer du courant dans la base, c'est donc *ouvrir* le transistor; ne plus en envoyer a, inversement, l'effet de *fermer* le transistor. 
```

De par sa capacité à être ouvert ou fermé, le {glo}`transistor|transistor` fonctionne comme une brique fondamentale dans la construction de systèmes informatiques permettant de {glo}`transmission|transmettre`, {glo}`stockage|stocker` et {glo}`traitement|traiter` des nombres binaires. 


````{dropdown} Pour aller plus loin
Les transistors sont faits avec des matériaux dit «semi-conducteurs». Voici une vidéo facultative qui explique en détail ce qui se passe dans ces semi-conducteurs et qui permet de faire fonctionner un transistor.
```{youtube} 33vbFFFn04k
```
````


`````{panels}
:column: col-lg
Des transistors presque invisibles
^^^
Chercher à se représenter la taille des transistors utilisés dans les microprocesseurs actuels n'a pas d'intérêt tellement ils sont petits. À titre d'exemple, disons simplement que le microprocesseur Apple A9 (igure 35) en possède six milliards.
````{dropdown} Zoom sur un transistor
```{youtube} Fxv3JoS1uY8
```
````
`````

## Des transistors aux systèmes logiques

Cela reste difficile de concevoir des circuits d'ordinateurs en réfléchissant en termes de {glo}`transistor|transistors`. Un {glo}`transistor|transistor` seul ne peut représenter ou traiter qu'un bit d'information. Oui ou non, ouvert ou fermé, 1 ou 0.

Dans la section suivante, où nous commençons à voir comment concevoir sont conçus les circuits électroniques des ordinateurs, nous commençons par parler de **{glo}`portelogique|portes logiques`**. Ce sont des composants qui sont eux-mêmes composés de plusieurs transistors. Réfléchir en termes de portes logiques permet de véritablement concevoir les circruits des ordinateurs qui vont manipuler les bits d'informations qui constituent nos données.
