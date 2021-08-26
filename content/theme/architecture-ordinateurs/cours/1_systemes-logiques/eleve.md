# Systèmes logiques

En informatique, les {glo}`syslogique|systèmes logiques` décrivent comment sont connectés les {glo}`circuitelectronique|circuits électroniques` des ordinateurs afin de leur permettre, d'une part, de faire des calculs et de traiter des données; et, d'autre part, d'utiliser leur mémoire de travail, où sont stockées les données qu'ils traitent.

Même si on a l'impression que les ordinateurs peuvent faire toutes sortes de choses, il y a un ensemble limité d'opérations de base que l'électronique d'une machine peut faire. Parmi ces quelques opérations de base, on trouve l'addition, la soustraction, la multiplication ou la division de nombres. La vaste majorité de ce que fait l'ordinateur repose sur ces quelques opérations (ainsi que sur quelques opérations dites _logiques_, que nous allons découvrir).

C'est assez fascinant de se dire que des tâches a priori non mathématiques, comme corriger l'orthographe ou la grammaire d'un texte automatiquement, sont réalisées avec ces opérations de base. 

En parallèle à ce qui leur permet de faire des calculs, les ordinateurs disposent d'une mémoire de travail, appelée aussi RAM (_random-access memory_). L'étude des systèmes logiques permet de comprendre les principes derrière la gestion de cette mémoire et de voir comment les ordinateurs peuvent y lire et écrire des données entre deux calculs.


## Exemple suivi: addition de deux nombres

Intéressons-nous à une des opérations arithmétiques les plus simples: l'**addition**. Comment l'ordinateur additionne-t-il deux nombres? Nous allons définir le cadre de travail et nous intéresser aux {glo}`circuitelectronique|circuits électroniques` qui vont être à même de réaliser une addition.

Imaginons donc que nous devons additionner deux nombres entiers. Nous allons utiliser leur représentation binaire (avec uniquement des 1 et des 0). Pour faire simple, nous allons chercher à additionner simplement deux bits, disons $A$ et $B$, où chacun peut valoir soit 0 soit 1. Posons que la somme $S = A + B$. En énumérant tous les cas figure, on a:

| $A$ | $B$ | $S$ |
| :-: | :-: | --: |
| 0   | 0   | 0   |
| 1   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 1   | 10  |

La dernière ligne est intéressante: nous savons que $1+1=2$, mais en {glo}`codebinaire|binaire`, nous savons aussi que nous n'avons droit qu'à des 0 et des 1, et 2 s'écrit ainsi $10$ (voir le chapitre {ref}`représentation de l'information <representationinformation>`). Cela veut dire que, pour traiter tous les cas d'une addition de 2 {glo}`bit|bits`, nous avons besoin aussi de 2 {glo}`bit|bits` de sortie, et qu'un seul ne suffit pas. En explicitant chaque fois le deuxième {glo}`bit|bit` de sortie, notre tableau devient:

| $A$ | $B$ | $S$ |
| :-: | :-: | :-: |
| 0   | 0   | 00  |
| 1   | 0   | 01  |
| 0   | 1   | 01  |
| 1   | 1   | 10  |

La question est de déterminer comment faire calculer les deux {glo}`bit|bits` de la somme $S$ à partir de $A$ et $B$ à un {glo}`circuitelectronique|circuit électronique`. Pour cela, avons besoin du concept de {glo}`portelogique|portes logiques`. Ces portes logiques sont elles-mêmes constituées de _transistors_, dont nous avons parlé en début de chapitre.

Dans un premier temps, nous parlons des portes logiques et de comment réaliser des circuits logiques.

Ensuite, nous regardons comment, fort de notre connaissance des portes logiques, nous pouvons concevoir un circuit qui effectuera l'addition qui nous intéresse.

Finalement, nous verrons comment un ordinateur est capable, avec un circuit logique, de stocker le résultat d'un tel calcul afin qu'il soit réutisable pllus tard.

Cette section est ainsi composée des sous-sections suivantes:

```{tableofcontents}
```

Les opérations arithmétiques et logiques et l'accès à la mémoire ne suffisent pas à consistuer un ordinateur complet. C'est dans le chapitre suivant que nous continueront à voir comment ces sous-systèmes sont agencés pour constituer une machine capable d'exécuter une suite d'instructions: un programme.
