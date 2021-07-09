(architectureordinateurs)=
Architecture des ordinateurs
===========================

<!-- <iframe src='https://timeline.knightlab.com/examples/houston/index.html' width='600' height='600' frameborder='0'></iframe> -->


L'ENIAC, l'un des tout premiers ordinateurs opérationnels, conçu en 1945, à la fin de la IIème Guerre Mondiale, pour calculer des trajectoires de missiles, était constitué de 17'468 tubes électroniques de la taille d'une main, qui cassaient en moyenne une fois par semaine.  Il s'étendait sur 170 mètres carrés et pesait plus de 25 tonnes. Il était capable d'exécuter environ 5'000 opérations par seconde. 

L'iPhone X, pour un poids de 147 grammes, exécute environ 600 milliards d'opérations par seconde. 

En 1991, 1 GO de mémoire non volatile coutait environ 45'000 dollars. Aujourd'hui, un iPhone possède 256 GO d'espace libre, ce qui aurait coûté à l'époque 11.5 millions de dollars[^1]. 

Mais par quoi ont été remplacés les 17'468 tubes électroniques de l'ENIAC ? Et comment se fait-il qu'un objet qui tient dans la poche puisse contenir 256 fois plus d'espace disque qu'un ordinateur des années 1990 ? 

Dans ce chapitre, vous découvrirez comment sont construits les ordinateurs, comment sont organisés leurs différents composants pour leur permettre d'effectuer des milliards de calculs à la seconde alors qu'ils ne comprennent que la distinction entre 0 et 1, allumé ou éteint.

<!-- ![img](media/microprocessor.gif) -->

## Contenus du chapitre

```{tableofcontents}
```

## Objectifs du chapitre

{fa}`check, text-success mr-1`Découvrir les **éléments de base** qui composent l'ordinateur.

{fa}`check, text-success mr-1`Comprendre les notions de **système logique** et de **microprocesseur**.

{fa}`check, text-success mr-1`Appréhender l’importance de **l'architecture des ordinateurs** pour optimiser les performances et effectuer des tâches informatiques spécifiques.

## Personnages-clés

````{panels}

:img-top: media/lovelace.jpeg

Ada Lovelace
^^^^^
* **Naissance** 10 décembre 1815 / Londres 🇬🇧  
* **Déces** 27 novembre janvier 1852 / Marylebone 🇬🇧 
* **Pseudonyme** A. A. L

[**Ada Lovelace**](https://fr.wikipedia.org/wiki/Ada_Lovelace) est principalement connue pour avoir réalisé le premier véritable programme informatique, lors de son travail sur un ancêtre de l'ordinateur : la machine analytique de Charles Babbage. Dans ses notes, on trouve en effet le premier programme publié, destiné à être exécuté par une machine, ce qui fait considérer Ada Lovelace comme « le premier programmeur du monde ».

----
:img-top: media/babbage.jpeg

Charles Babbage
^^^^^
* **Naissance** 26 décembre 1791 / Londres 🇬🇧
* **Déces** 18 octobre 1871 / Marylebone 🇬🇧 

[**Charles Babbage**](https://fr.wikipedia.org/wiki/Charles_Babbage) fut le premier inventeur à énoncer le principe d'un ordinateur. C'est en 1834, pendant le développement d'une machine à calculer destinée au calcul et à l'impression de tables mathématiques (la machine à différences) qu'il eut l'idée d'y incorporer des cartes du métier Jacquard, dont la lecture séquentielle donnerait des instructions et des données à sa machine, et donc imagina l'ancêtre mécanique des ordinateurs d'aujourd'hui. 
````

[^1]:https://www.aei.org/technology-and-innovation/the-a12-chip-estimating-innovation-with-iphone-prices/