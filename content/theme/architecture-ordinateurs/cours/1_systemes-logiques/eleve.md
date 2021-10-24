# 1. Systèmes logiques

En informatique, les {glo}`syslogique|systèmes logiques` décrivent comment sont connectés les {glo}`circuitelectronique|circuits électroniques` des ordinateurs afin de leur permettre, d'une part, d'effectuer des calculs et de traiter des données et, d'autre part, d'utiliser leur mémoire de travail, où sont stockées les données qu'ils traitent.

Même si on a l'impression que les ordinateurs peuvent faire toutes sortes de choses, il y a un ensemble limité d'opérations de base que l'électronique d'une machine peut faire. Parmi ces quelques opérations de base, on trouve l'addition, la soustraction, la multiplication ou la division de nombres. La plupart des tâches que l'ordinateur exécute repose sur ces quelques opérations (ainsi que sur quelques opérations dites _logiques_, qui vont être explicitées).

C'est assez fascinant de se dire que des tâches a priori non mathématiques, comme corriger l'orthographe ou la grammaire d'un texte automatiquement, sont réalisées avec ces opérations de base. 

En parallèle à ce qui leur permet de faire des calculs, les ordinateurs disposent et utilisent de la mémoire. Il y en a au cœur des microprocesseurs, les _registres_, ce qu'on appelle la _mémoire vive_ - appelée aussi RAM (_Random-Access Memory_). La mémoire servant au stockage de longue durée comme disques durs et autres SSD n'est pas discutée dans cette section. L'étude des systèmes logiques permet de comprendre les principes derrière la gestion de cette mémoire et de voir comment les ordinateurs peuvent y lire et écrire des données entre deux calculs.


## Exemple suivi : addition de deux nombres

On s'intéresse à une des opérations arithmétiques les plus simples : l'**addition**. Comment l'ordinateur additionne-t-il deux nombres ? On va définir le cadre de travail et s'intéresser aux {glo}`circuitelectronique|circuits électroniques` qui vont être à même de réaliser une addition.

Que se passe-t-il pour l'addition de deux nombres entiers ? On va utiliser leur représentation binaire (avec uniquement des 1 et des 0). Pour faire simple, on va chercher à additionner simplement deux bits, disons $A$ et $B$, où chacun peut valoir soit 0 soit 1. Posons que la somme $S = A + B$. En énumérant tous les cas de figure, on a :

| $A$ | $B$ | $S$ |
| :-: | :-: | --: |
| 0   | 0   | 0   |
| 1   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 1   | 10  |

La dernière ligne est intéressante : On sait que $1+1=2$, mais en {glo}`codebinaire|binaire`, on sait aussi que n'existent que des 0 et des 1, et 2 s'écrit ainsi $10$ (voir le chapitre {ref}`représentation de l'information <representationinformation>`). Cela veut dire que, pour traiter tous les cas d'une addition de deux {glo}`bit|bits`, on a besoin aussi de deux {glo}`bit|bits` de sortie, et qu'un seul ne suffit pas. En explicitant chaque fois le deuxième {glo}`bit|bit` de sortie, notre tableau devient:

| $A$ | $B$ | $S$ |
| :-: | :-: | :-: |
| 0   | 0   | 00  |
| 1   | 0   | 01  |
| 0   | 1   | 01  |
| 1   | 1   | 10  |

La question est de déterminer comment faire calculer les deux {glo}`bit|bits` de la somme $S$ à partir de $A$ et $B$ à un {glo}`circuitelectronique|circuit électronique`. Pour cela, on a besoin du concept de {glo}`portelogique|portes logiques`. Ces portes logiques sont elles-mêmes constituées de _transistors_, dont on a parlé en début de chapitre.

Dans un premier temps, on détaille les portes logiques et on s'intéresse à la réalisation des circuits logiques.

Ensuite, on regarde comment, fort de cette connaissance des portes logiques, il est possible de concevoir un circuit qui effectuera l'addition en question.

Finalement, on comprendra comment un ordinateur est capable, avec un circuit logique, de stocker le résultat d'un tel calcul afin qu'il soit réutilisable plus tard.

Ce chapitre est ainsi composée des sous-chapitres suivants :

```{tableofcontents}
```

Les opérations arithmétiques et logiques et l'accès à la mémoire ne suffisent pas à constituer un ordinateur complet. C'est dans le chapitre suivant que sera traité la problématique de l'agencement de ces sous-systèmes afin de constituer une machine capable d'exécuter une suite d'instructions, c'est à dire un programme.


