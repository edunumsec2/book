(archi)=

# Architecture des ordinateurs

```{toctree}
:maxdepth: 2
:hidden:
:numbered: 2
intro
sys-log
additionneur
alu
mem
micro-pro
archi-gen

tp1
tp2
tp3
tp4
tp5
```

<!-- <iframe src='https://timeline.knightlab.com/examples/houston/index.html' width='600' height='600' frameborder='0'></iframe> -->

L'ENIAC, l'un des tout premiers ordinateurs opérationnels, conçu en 1945, à la fin de la Seconde Guerre mondiale, pour calculer des trajectoires de missiles, était constitué de 17 468 tubes électroniques de la taille d'une main, qui cassaient en moyenne une fois par semaine.  Il s'étendait sur 170 mètres carrés et pesait plus de 25 tonnes. Il était capable d'exécuter environ 5000 opérations par seconde.

Pour comparaison, les microprocesseurs des smartphones modernes exécutent de l'ordre de plusieurs centaines de _milliards_ d'opérations par seconde.

En 1991, 1 Go (un milliard d'octets) de mémoire non volatile coûtait environ 45 000 dollars. Aujourd'hui, un smartphone moderne dispose de l'ordre de 256 Go d'espace de stockage, ce qui aurait coûté à l'époque 11.5 millions de dollars[^1].

À quoi servaient précisément 17 468 tubes électroniques de l'ENIAC dans le rôle que l'ordinateur avait ? Et par quoi ont-ils été remplacés dans nos machines modernes ? Et comment se fait-il qu'un objet qui tient dans la poche puisse contenir 256 fois plus d'espace disque qu'un ordinateur des années 1990 ?

Dans ce chapitre, vous découvrirez comment sont construits les ordinateurs, comment sont organisés leurs différents composants pour leur permettre d'effectuer des milliards de calculs à la seconde alors qu'ils ne comprennent que la distinction entre 0 et 1, allumé ou éteint.



## Objectifs

* Découvrir les **éléments de base** qui composent l'ordinateur.

* Comprendre les notions de **système logique** et de **microprocesseur**.

* Appréhender l’importance de **l'architecture des ordinateurs** pour optimiser les performances et effectuer des tâches informatiques spécifiques.

## Personnages-clés

:::::{grid} 1 2 2 2
:gutter: 2

::::{grid-item}
:::{card}
:img-top: media/anitaborg.jpg

Anita Borg 🇺🇸 
^^^^^
***1949-2003***

[**Anita Borg**](https://fr.wikipedia.org/wiki/Anita_Borg) est une informaticienne américaine. Elle a notamment travaillé pour Digital Equipment Corporation où elle a développé une méthode permettant de concevoir des systèmes mémoriels à haute vitesse. 
:::
::::

::::{grid-item}
:::{card}
:img-top: media/babbage.jpeg

Charles Babbage 🇬🇧 
^^^^^
***1791-1871***

[**Charles Babbage**](https://fr.wikipedia.org/wiki/Charles_Babbage) fut le premier inventeur à énoncer le principe d'un ordinateur. C'est en 1834, pendant le développement d'une machine à calculer destinée au calcul et à l'impression de tables mathématiques, qu'il eut l'idée d'y incorporer des cartes du métier Jacquard, dont la lecture séquentielle donnerait des instructions et des données à sa machine. 
:::
::::
:::::

[^1]:https://www.aei.org/technology-and-innovation/the-a12-chip-estimating-innovation-with-iphone-prices/
