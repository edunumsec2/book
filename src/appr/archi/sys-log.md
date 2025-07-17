# Circuits logiques

Les portes logiques peuvent être combinées entre elles pour former des circuits logiques qui réalisent des fonctions logiques ou binaires. Certains circuits logiques
réalisent des calculs sur des nombres binaires, d'autres peuvent servir de mémoire pour stocker des valeurs binaires. 


## Des valeurs logiques aux nombres binaires
Du fait de la correspondance entre les valeurs logiques, les valeurs binaires et l'état d'un circuits électronique, on peut interpréter les entrées et
les sorties d'un circuit logique comme un nombre donnée en binaire.


````{exercise}
On considère que les entrées du circuit ci-dessous forment un nombre $x$ s'écrivant $X_2X_1X_0$ en binaire et que les sorties forment également un nombre $y$ s'écrivant
$Y_2Y_1Y_0$ en binaire. Que vaut $y$ en fonction de $x$, ou autrement dit, quel calcul réalise ce circuit logique composé de trois portes NON? Les affichages rectangulaires
indiquant la valeur en décimal de $x$ et $y$ ont été ajoutés pour vous aidez, mais ne sont pas forcément nécessaires. 

```{logic}
:id: KeZJvf
:height: 278
:mode: tryout

{ // JSON5
  v: 6,
  components: {
    in0: {type: 'in', pos: [100, 55], orient: 's', id: 0, name: 'X2'},
    in1: {type: 'in', pos: [150, 55], orient: 's', id: 1, name: 'X1'},
    in2: {type: 'in', pos: [200, 55], orient: 's', id: 2, name: 'X0'},
    not0: {type: 'not', pos: [100, 135], orient: 's', in: 3, out: 4},
    out0: {type: 'out', pos: [100, 225], orient: 's', id: 5, name: 'Y2'},
    not1: {type: 'not', pos: [150, 135], orient: 's', in: 6, out: 7},
    not2: {type: 'not', pos: [200, 140], orient: 's', in: 8, out: 9},
    out1: {type: 'out', pos: [150, 225], orient: 's', id: 11, name: 'Y1'},
    out2: {type: 'out', pos: [200, 225], orient: 's', id: 12, name: 'Y0'},
    disp0: {type: 'display', pos: [300, 80], id: '13-16', name: 'x'},
    disp1: {type: 'display', pos: [300, 190], id: '17-20', name: 'y'},
  },
  wires: [[0, 3], [4, 5], [1, 6], [2, 8], [9, 12], [7, 11], [1, 14], [2, 13], [0, 15], [4, 19], [7, 18], [9, 17]]
}
```

````
```{solution}
Le circuit logique réalise le calcul suivant: $y = 7-x$. Autrement dit, ce circuit réalise la fonction $f(x)=7-x$ en binaire. 
```

## Analyse de circuits logiques

L'analyse d'un circuit logique consiste à établir sa table de vérité, c'est-à-dire déterminer ses sorties pour chaque combinaison
possible de ces entrées.

````{exercise}
Remplir la table de vérité du circuit de l'exercice ci-dessus.

|$X_2$ | $X_1$ |$X_0$ | $Y_2$ | $Y_1$ |$Y_0$|
|----- |------ |------|-------|-------|-----|
| 0    | 0     | 0    |       |       |     |
| 0    | 0     | 1    |       | | |
| 0    | 1     | 0 | | | |
| 0    | 1     | 1 | | | |
| 1    | 0     | 0 | | | |
| 1    | 0     | 1 | | | |
| 1    | 1     | 0 | | | |
| 1    | 1     | 1 | | | |

````

```{dropdown} Solution
|$X_2$ | $X_1$ |$X_0$ | $Y_2$ | $Y_1$ |$Y_0$|
|----- |------ |------|-------|-------|-----|
| 0    | 0     | 0    |   1   |  1    |  1  |
| 0    | 0     | 1    |   1   |  1    |  0  |
| 0    | 1     | 0    |   1   |  0    |  1  |
| 0    | 1     | 1    |   1   |  0    |  0  |
| 1    | 0     | 0    |   0   |  1    |  1  |
| 1    | 0     | 1 	  |   0   |  1    |  0  |
| 1    | 1     | 0 	  |   0   |  0    |  1  |
| 1    | 1     | 1 	  |   0   |  0    |  0  |
```


<!-- En informatique, les {glo}`syslogique|circuits logiques` décrivent comment sont connectés les circuits électroniques des ordinateurs afin de leur permettre, d'une part, d'effectuer des calculs et de traiter des données et, d'autre part, d'utiliser leur mémoire de travail, où sont stockées les données qu'ils traitent. -->

<!-- Même si on a l'impression que les ordinateurs peuvent faire toutes sortes de choses, il y a un ensemble limité d'opérations de base que l'électronique d'une machine peut faire. Parmi ces quelques opérations de base, on trouve l'addition, la soustraction, la multiplication ou la division de nombres. La plupart des tâches que l'ordinateur exécute reposent sur ces quelques opérations (ainsi que sur quelques opérations dites _logiques_, qui vont être explicitées). -->

<!-- C'est assez fascinant de se dire que des tâches a priori non mathématiques, comme corriger l'orthographe ou la grammaire d'un texte automatiquement, sont réalisées avec ces opérations de base.  -->

<!-- En parallèle à ce qui leur permet de faire des calculs, les ordinateurs disposent et utilisent de la mémoire. Il y en a au cœur des microprocesseurs, les _registres_, ce qu'on appelle la _mémoire vive_ — appelée aussi RAM (_Random-Access Memory_). La mémoire servant au stockage de longue durée comme disques durs et autres SSD n'est pas discutée dans cette section. L'étude des systèmes logiques permet de comprendre les principes derrière la gestion de cette mémoire et de voir comment les ordinateurs peuvent y lire et écrire des données entre deux calculs. -->


## Exemple suivi : addition de deux nombres

On s'intéresse à une des opérations arithmétiques les plus simples : l'**addition**. Comment l'ordinateur additionne-t-il deux nombres ? On va définir le cadre de travail et s'intéresser aux circuits électroniques qui vont être à même de réaliser une addition.

Que se passe-t-il pour l'addition de deux nombres entiers ? On va utiliser leur représentation binaire (avec uniquement des 1 et des 0). Pour faire simple, on va chercher à additionner simplement deux bits, disons $A$ et $B$, où chacun peut valoir soit 0 soit 1. Posons que la somme $S = A + B$. En énumérant tous les cas de figure, on a :

| $A$ | $B$ | $S$ |
| :-: | :-: | --: |
| 0   | 0   | 0   |
| 1   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 1   | 10  |

La dernière ligne est intéressante : on sait que $1+1=2$, mais en {glo}`codebinaire|binaire`, on sait aussi que n'existent que des 0 et des 1, et 2 s'écrit ainsi 10 (voir le chapitre {ref}`représentation de l'information <repinfo>`). Cela veut dire que, pour traiter tous les cas d'une addition de deux {glo}`bit|bits`, on a besoin aussi de deux bits de sortie, et qu'un seul ne suffit pas. En explicitant chaque fois le deuxième bit de sortie, notre tableau devient :

| $A$ | $B$ | $S$ |
| :-: | :-: | :-: |
| 0   | 0   | 00  |
| 1   | 0   | 01  |
| 0   | 1   | 01  |
| 1   | 1   | 10  |

La question est de déterminer comment faire calculer les deux bits de la somme $S$ à partir de $A$ et $B$ à un circuit électronique. Pour cela, on a besoin du concept de {glo}`portelogique|portes logiques`. Ces portes logiques sont elles-mêmes constituées de _transistors_, dont on a parlé en début de chapitre.

Dans un premier temps, on détaille les portes logiques et on s'intéresse à la réalisation des circuits logiques.

Ensuite, on regarde comment, fort de cette connaissance des portes logiques, il est possible de concevoir un circuit qui effectuera l'addition en question.

Finalement, on comprendra comment un ordinateur est capable, avec un circuit logique, de stocker le résultat d'un tel calcul afin qu'il soit réutilisable plus tard.

Les opérations arithmétiques et logiques et l'accès à la mémoire ne suffisent pas à constituer un ordinateur complet. C'est dans le chapitre suivant que sera traité la problématique de l'agencement de ces sous-systèmes afin de constituer une machine capable d'exécuter une suite d'instructions, c'est à dire un programme.

## Combinaisons de portes

Les portes peuvent être connectées les unes aux autres. Voici par exemple un diagramme logique réalisant la fonction appelée **OU-X**, qui est un «ou exclusif» et dont {logicref}`xor_circuit_tryout.z|la sortie $Z$` vaut 1 lorsque soit {logicref}`xor_circuit_tryout.x|$X$`, soit {logicref}`xor_circuit_tryout.y|$Y$` vaut 1, mais pas les deux en même temps :

```{logic}
:ref: xor_circuit_tryout
:height: 150
:mode: tryout

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 0, "ref": "x", "name": "X", "val": 0},
    {"pos": [50, 90], "id": 1, "ref": "y", "name": "Y", "val": 0}
  ],
  "out": [{"pos": [390, 50], "id": 2, "ref": "z", "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [190, 40], "in": [3, 4], "ref": "or", "out": 5},
    {"type": "AND", "pos": [330, 50], "in": [6, 7], "ref": "and2", "out": 8},
    {"type": "NOT", "pos": [230, 120], "in": 9, "ref": "inv", "out": 10},
    {"type": "AND", "pos": [160, 120], "in": [11, 12], "ref": "and1", "out": 13}
  ],
  "wires": [[0, 3], [0, 11], [1, 4], [1, 12], [13, 9], [10, 7], [5, 6], [8, 2]]
}
```


Ce circuit contient {logicref}`xor_circuit_tryout.or|une porte **OU**`, {logicref}`xor_circuit_tryout.{and1,and2}|deux portes **ET**` et {logicref}`xor_circuit_tryout.inv|un inverseur`, tous interconnectés.

Ce diagramme n'est pas forcément facile à lire — discutons d'abord comment l'interpréter avec papier et crayon pour vérifier s'il effectue bien un **OU-X**.


### Analyse d'un circuit

Pour analyser un circuit logique comme celui présenté ci-dessus, on cherchera à établir sa table de vérité. En l'occurrence, comme pour les portes précédentes, ce circuit a {logicref}`xor_circuit_tryout.{x,y}|deux entrées`: si chaque entrée peut valoir 1 ou 0, on a en tout, de nouveau, quatre configurations possibles à examiner dans le but de remplir la dernière colonne :

| $X$ | $Y$ | $Z$ |
| :-: | :-: | :-: |
| 0   | 0   | ?   |
| 1   | 0   | ?   |
| 0   | 1   | ?   |
| 1   | 1   | ?   |


 Pour remplir chaque ligne, on va changer les entrées selon les valeurs de $X$ et $Y$ et observer l'effet des portes et ainsi voir comment le circuit se comporte. Prenons $X=Y=0$: c'est le cas représenté par le diagramme fixe ci-dessous. Rappelons qu'un segment noir véhicule un «0», alors qu'un segment coloré véhicule un «1».

 ```{logic}
:ref: xor_circuit_00
:height: 150
:mode: static

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 0, "ref": "x", "name": "X", "val": 0},
    {"pos": [50, 90], "id": 1, "ref": "y", "name": "Y", "val": 0}
  ],
  "out": [{"pos": [390, 50], "id": 2, "ref": "z", "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [190, 40], "in": [3, 4], "ref": "or", "out": 5},
    {"type": "AND", "pos": [330, 50], "in": [6, 7], "ref": "and2", "out": 8},
    {"type": "NOT", "pos": [230, 120], "in": 9, "ref": "inv", "out": 10},
    {"type": "AND", "pos": [160, 120], "in": [11, 12], "ref": "and1", "out": 13}
  ],
  "wires": [[0, 3], [0, 11], [1, 4], [1, 12], [13, 9], [10, 7], [5, 6], [8, 2]]
}
```

Le résultat intermédiaire des {logicref}`xor_circuit_00.{or,and1}|deux portes de gauche` sera 0. L'{logicref}`xor_circuit_00.inv|inverseur` transforme en 1 la sortie de la porte **ET**, mais la {logicref}`xor_circuit_00.and2|porte finale`, qui est aussi une porte **ET**, n'obtient qu'un seul 1 en entrée et donc livre une {logicref}`xor_circuit_00.z|sortie de 0`.

Le cas est différent si l'une des deux entrées vaut 1. Voici deux diagrammes fixes, une fois pour $X=1, Y=0$ et une fois pour $Y=1, X=0$ :

```{logic}
:ref: xor_circuit_10
:height: 150
:mode: static

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 0, "ref": "x", "name": "X", "val": 1},
    {"pos": [50, 90], "id": 1, "ref": "y", "name": "Y", "val": 0}
  ],
  "out": [{"pos": [390, 50], "id": 2, "ref": "z", "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [190, 40], "in": [3, 4], "ref": "or", "out": 5},
    {"type": "AND", "pos": [330, 50], "in": [6, 7], "ref": "and2", "out": 8},
    {"type": "NOT", "pos": [230, 120], "in": 9, "ref": "inv", "out": 10},
    {"type": "AND", "pos": [160, 120], "in": [11, 12], "ref": "and1", "out": 13}
  ],
  "wires": [[0, 3], [0, 11], [1, 4], [1, 12], [13, 9], [10, 7], [5, 6], [8, 2]]
}
```

```{logic}
:ref: xor_circuit_01
:height: 150
:mode: static

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 0, "ref": "x", "name": "X", "val": 0},
    {"pos": [50, 90], "id": 1, "ref": "y", "name": "Y", "val": 1}
  ],
  "out": [{"pos": [390, 50], "id": 2, "ref": "z", "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [190, 40], "in": [3, 4], "ref": "or", "out": 5},
    {"type": "AND", "pos": [330, 50], "in": [6, 7], "ref": "and2", "out": 8},
    {"type": "NOT", "pos": [230, 120], "in": 9, "ref": "inv", "out": 10},
    {"type": "AND", "pos": [160, 120], "in": [11, 12], "ref": "and1", "out": 13}
  ],
  "wires": [[0, 3], [0, 11], [1, 4], [1, 12], [13, 9], [10, 7], [5, 6], [8, 2]]
}
```


Ici, dans les deux cas, {logicref}`{xor_circuit_01,xor_circuit_10}.or|la porte **OU**, en haut`, livrera un 1, dont a besoin {logicref}`{xor_circuit_01,xor_circuit_10}.and2|la porte **ET** finale de droite` pour donner {logicref}`{xor_circuit_01,xor_circuit_10}.z|une sortie de 1`. {logicref}`{xor_circuit_01,xor_circuit_10}.and1|La porte **ET** du bas`, elle, continue de livrer un 0.

Mais dans le cas $X = Y = 1$, représenté ici, la situation est différente :

```{logic}
:ref: xor_circuit_11
:height: 150
:mode: static

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 0, "ref": "x", "name": "X", "val": 1},
    {"pos": [50, 90], "id": 1, "ref": "y", "name": "Y", "val": 1}
  ],
  "out": [{"pos": [390, 50], "id": 2, "ref": "z", "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [190, 40], "in": [3, 4], "ref": "or", "out": 5},
    {"type": "AND", "pos": [330, 50], "in": [6, 7], "ref": "and2", "out": 8},
    {"type": "NOT", "pos": [230, 120], "in": 9, "ref": "inv", "out": 10},
    {"type": "AND", "pos": [160, 120], "in": [11, 12], "ref": "and1", "out": 13}
  ],
  "wires": [[0, 3], [0, 11], [1, 4], [1, 12], [13, 9], [10, 7], [5, 6], [8, 2]]
}
```

{logicref}`xor_circuit_11.and1|La porte **ET** du bas` livre un 1, qui est {logicref}`xor_circuit_11.inv|inversé en 0` avant d'atteindre {logicref}`xor_circuit_11.and2|la porte finale`, qui ne peut dès lors elle-même que {logicref}`xor_circuit_11.z|livrer un 0 comme sortie`.

La table de vérité complétée de ce circuit est ainsi :

| $X$ | $Y$ | $Z$ |
| :-: | :-: | :-: |
| 0   | 0   | 0   |
| 1   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 1   | 0   |

Cette fonction s'appelle «ou exclusif», car pour avoir un 1 de sortie, elle exclut le cas où les deux entrées sont 1 en même temps. Elle est souvent utilisée, au point qu'on la représente en fait dans les diagrammes simplement par {logicref}`xor_tryout.xor|le dessin de cette porte`, appelée **OU-X**, comme simplification du diagramme ci-dessus :

```{logic}
:ref: xor_tryout
:height: 100
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 3, "name": "X", "val": 0},
    {"pos": [50, 70], "id": 4, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [220, 50], "id": 5, "name": "Z"}],
  "gates": [{"type": "XOR", "pos": [150, 50], "in": [0, 1], "ref": "xor", "out": 2}],
  "wires": [[3, 0], [4, 1], [2, 5]]
}
```

```{exercise} Vérification d’une porte

Vérifiez que la porte **OU-X** se comporte bien comme le circuit ci-dessous réalisé avec des portes **ET**, **OU** et **NON**.
```


### Création d'un circuit

On s'intéresse à présent à la création de ce diagramme réalisant un **OU-X** avec les portes à disposition à partir de sa table de vérité. Plusieurs approches sont possibles, et on constatera que, suivant l'approche, on aurait très bien pu créer un circuit logique différent réalisant la même fonction.


**Approche ad hoc**

On se dit donc, selon la table de vérité, que la sortie de notre circuit «ou exclusif» doit être 1, donc l'une ou l'autre des entrées $X$ ou $Y$ est à 1, mais pas les deux. On peut ainsi commencer par {logicref}`xor_build_step1.or|insérer une porte **OU**` dans le diagramme, qui fait une partie du travail. Mais il faut modifier sa sortie, pour ne pas avoir la valeur 1 lorsque les deux entrées sont à 1 : cela contredirait la quatrième ligne de la table de vérité. Comment effectuer cela ? En connectant la sortie de {logicref}`xor_build_step1.or|cette porte **OU**` à {logicref}`xor_build_step1.and2|une nouvelle porte **ET** à droite` (dont on n'a pas encore déterminé la seconde entrée).

Pourquoi rajouter une porte **ET** ? On utilise ici le fait que connecter une porte **ET** à un signal peut _restreindre_ les conditions sous lesquelles la nouvelle sortie $Z$ sera 1 (alors qu'au contraire, on aurait pu _étendre_ ces conditions si on avait connecté une nouvelle porte **OU**). Comme si, pour être d'accord de finalement livrer 1 sur la sortie, {logicref}`xor_build_step1.and2|la porte **ET**` voulait la «confirmation» d'un autre signal avant de livrer 1...

À ce moment, on a ce diagramme partiel, qui peut être lu comme : «la sortie $Z$ sera 1 lorsque ces deux conditions sont vraies en même temps: (1) le **OU** de $X$ et $Y$ vaut 1, et (2) quelque chose qui reste ici à définir, qui sera connecté à la seconde entrée de la porte **ET**».

```{logic}
:ref: xor_build_step1
:height: 120
:mode: tryout

{
  "v": 3,
  "opts": {"showGateTypes": true, "showDisconnectedPins": true},
  "in": [
    {"pos": [50, 30], "id": 0, "name": "X", "val": 0},
    {"pos": [50, 90], "id": 1, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [390, 50], "id": 2, "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [190, 40], "ref": "or", "in": [3, 4], "out": 5},
    {"type": "AND", "pos": [330, 50], "ref": "and2", "in": [6, 7], "out": {"id": 8, "force": "?"}}
  ],
  "wires": [[0, 3], [1, 4], [5, 6], [8, 2]]
}
```


Ce qui reste à définir en complétant avant la porte **ET**, c'est l'exclusion du cas où $X$ et $Y$ valent les deux 1, de manière à ce que la condition (2) puisse être lue comme «$X$ et $Y$ ne sont pas en même temps les deux à 1». Avec {logicref}`xor_build_step2.and1|une porte **ET** connectée directement aux deux entrées $X$ et $Y$`, on obtient une partie de ceci en créant le signal «$X$ et $Y$ sont les deux à 1». Mais c'est en fait la condition inverse de celle que l'on cherche. Pour l'inverser, on insère {logicref}`xor_build_step2.inv|un inverseur` à la sortie de {logicref}`xor_build_step2.and1|cette nouvelle porte **ET**`, ce qui complète le circuit :

```{logic}
:ref: xor_build_step2
:height: 150
:mode: tryout

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 0, "name": "X", "val": 0},
    {"pos": [50, 90], "id": 1, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [390, 50], "id": 2, "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [190, 40], "in": [3, 4], "ref": "or", "out": 5},
    {"type": "AND", "pos": [330, 50], "in": [6, 7], "ref": "and2", "out": 8},
    {"type": "NOT", "pos": [230, 120], "in": 9, "ref": "inv", "out": 10},
    {"type": "AND", "pos": [160, 120], "in": [11, 12], "ref": "and1", "out": 13}
  ],
  "wires": [[0, 3], [0, 11], [1, 4], [1, 12], [13, 9], [10, 7], [5, 6], [8, 2]]
}
```

La lecture finale du circuit est donc «la sortie $Z$ sera 1 lorsque ces deux conditions sont vraies en même temps (selon {logicref}`xor_build_step2.and2|la porte **ET** de droite`) : (1) {logicref}`xor_build_step2.or|le **OU** de $X$ et $Y$ vaut 1`, et (2) {logicref}`xor_build_step2.{and1,inv}|$X$ et $Y$ ne sont pas les deux en même temps à 1`».

````{exercise} Analyse d'un circuit

Ceci est le même circuit que ci-dessus, mais sans la porte **ET** finale. À la place, on a inséré deux sorties intermédiaires, $I$ et $J$, qui sont les deux signaux qui allaient précédemment à la porte **ET** :

```{logic}
:height: 150
:mode: tryout

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 0, "name": "X", "val": 0},
    {"pos": [50, 90], "id": 1, "name": "Y", "val": 0}
  ],
  "out": [
    {"pos": [310, 40], "id": 15, "name": "I"},
    {"pos": [310, 120], "id": 14, "name": "J"}
  ],
  "gates": [
    {"type": "OR", "pos": [190, 40], "in": [3, 4], "out": 5},
    {"type": "NOT", "pos": [230, 120], "in": 9, "out": 10},
    {"type": "AND", "pos": [160, 120], "in": [11, 12], "out": 13}
  ],
  "wires": [[0, 3], [0, 11], [1, 4], [1, 12], [13, 9], [10, 14], [5, 15]]
}
```

 1. Combien de lignes a une table de vérité pour $I$ et $J$ en fonction des deux entrées $X$ et $Y$ ? Écrivez cette table de vérité.
 1. Quelle différence y a-t-il entre $J$ et ce qu'on obtient en connectant directement une porte **ET** aux entrées $X$ et $Y$ : quel élément du schéma réalise cette différence ?
 1. Dans votre table de vérité, ajoutez une colonne et remplissez-là : elle doit représenter une nouvelle sortie $K$, qui serait produite si on connectait une porte **OU** en lui donnant $I$ et $J$ comme entrées, comme montré ci-dessous. Le schéma représente ici le circuit dans un état indéterminé, mais les types des portes ont été ajoutés pour vous aider. La sortie $K$ est-elle ici toujours la même que la sortie $Z$ plus haut ? Quelles sont les éventuelles différences ? Finalement, la sortie $K$ a-t-elle un intérêt ?

```{logic}
:height: 150
:mode: static

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 0, "name": "X", "val": "?"},
    {"pos": [50, 90], "id": 1, "name": "Y", "val": "?"}
  ],
  "out": [{"pos": [390, 50], "id": 2, "name": "K"}],
  "gates": [
    {"type": "OR", "pos": [190, 40], "in": [3, 4], "out": 5},
    {"type": "OR", "pos": [330, 50], "in": [6, 7], "out": 8},
    {"type": "NOT", "pos": [230, 120], "in": 9, "out": 10},
    {"type": "AND", "pos": [160, 120], "in": [11, 12], "out": 13}
  ],
  "wires": [[0, 3], [0, 11], [1, 4], [1, 12], [13, 9], [10, 7], [5, 6], [8, 2]]
}
```
````


**Approche systématique**

Il est parfois difficile d'avoir l'«intuition» nécessaire pour suivre une telle approche ad hoc. Voici donc une autre technique, illustrée avec le même exemple.

La table de vérité montre qu'il y a deux lignes où la sortie doit valoir 1 : (a) la ligne où $X=1$ et $Y=0$, et (b) la ligne où $X=0$ et $Y=1$. Si l'on pouvait créer {logicref}`xor_build2_step1.sub1|un premier sous-circuit` qui livre un 1 lorsque qu'on se trouve dans la circonstance (a) et {logicref}`xor_build2_step1.sub2|un autre sous-circuit` qui livre un 1 lorsqu'on se trouve dans la circonstance (b), on pourrait ensuite les combiner avec {logicref}`xor_build2_step1.or|une porte **OU**` et ainsi construire notre sortie $Z$ ainsi :

```{logic}
:ref: xor_build2_step1
:height: 180
:mode: static

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 0, "name": "X", "val": "?"},
    {"pos": [50, 150], "id": 1, "name": "Y", "val": "?"}
  ],
  "out": [{"pos": [400, 90], "id": 2, "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [340, 90], "in": [6, 7], "ref": "or", "out": 8},
    {"type": "AND", "pos": [200, 60], "in": [3, 4], "out": 5, "ref": "sub1", "showAsUnknown": true},
    {"type": "AND", "pos": [200, 130], "in": [9, 10], "out": 11, "ref": "sub2", "showAsUnknown": true}
  ],
  "wires": [[8, 2], [0, 3], [1, 10], [5, 6], [11, 7], [0, 9], [1, 4]]
}
```

Ici, les deux sous-circuits notés avec «?» et encadrés donc encore à définir — potentiellement avec plus d'une seule porte. Essayons de les créer.

Disons que le sous-circuit du haut correspond à la deuxième ligne de la table de vérité, le cas de figure (a). Pour cette ligne, nous voulons un 1 de sortie lorsque $X=1$ et $Y=0$. En lisant littéralement cette dernière phrase, on y détecte un **ET** de deux conditions qui doivent être remplies: $X=1$ et $Y=0$. Mais ajouter une porte **ET** directement avec les signaux $X$ et $Y$ ne fera pas l'affaire, parce que cela livrerait un 1 lors que les _deux_ entrées $X$ et $Y$ sont à 1. La solution ici, c'est d'{logicref}`xor_build2_step2.inv1|inverser $Y$` avant l'entrée dans {logicref}`xor_build2_step2.and1|la porte **ET**` — ce qui donne bel et bien la condition (a).

On avance ainsi à ceci :

```{logic}
:ref: xor_build2_step2
:height: 180
:mode: static

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 0, "name": "X", "val": "?"},
    {"pos": [50, 150], "id": 1, "name": "Y", "val": "?"}
  ],
  "out": [{"pos": [400, 90], "id": 2, "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [340, 90], "in": [6, 7], "out": 8},
    {"type": "AND", "pos": [230, 50], "in": [3, 4], "ref": "and1", "out": 5},
    {"type": "AND", "pos": [200, 130], "in": [9, 10], "out": 11, "showAsUnknown": true},
    {"type": "NOT", "pos": [160, 60], "in": 12, "out": 13, "ref": "inv1"}
  ],
  "wires": [[8, 2], [13, 4], [0, 3], [1, 12], [1, 10], [5, 6], [11, 7], [0, 9]]
}
```

Pour la condition (b), qui correspond à la troisième ligne de la table de vérité, un raisonnement similaire s'applique. À la place d'inverser $Y$, on {logicref}`xor_build2_step3.inv2|inversera cette fois $X$` afin d'obtenir, à la sortie de {logicref}`xor_build2_step3.and2|la nouvelle porte **ET** du bas`, un signal qui vaut 1 lorsque $X=0$ et $Y=1$.

Voici le circuit final ainsi réalisé :

```{logic}
:ref: xor_build2_step3
:height: 180
:mode: static

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 0, "name": "X", "val": "?"},
    {"pos": [50, 150], "id": 1, "name": "Y", "val": "?"}
  ],
  "out": [{"pos": [400, 90], "id": 2, "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [340, 90], "in": [6, 7], "out": 8, "ref": "or"},
    {"type": "AND", "pos": [230, 50], "in": [3, 4], "out": 5, "ref": "and1"},
    {"type": "AND", "pos": [230, 130], "in": [9, 10], "out": 11, "ref": "and2"},
    {"type": "NOT", "pos": [160, 60], "in": 12, "out": 13, "ref": "inv1"},
    {"type": "NOT", "pos": [160, 120], "in": 14, "out": 15, "ref": "inv2"}
  ],
  "wires": [
    [8, 2], [13, 4], [15, 9], [0, 3], [0, 14], [1, 12], [1, 10],
    [5, 6], [11, 7]
  ]
}
```

(Ce schéma ne peut être simulé que dans l'indice de l'exercice suivant.)

Ce que cette approche systématique apprend, c'est qu'un circuit peut toujours être pensé comme {logicref}`xor_build2_step3.or|un **OU**` de toutes les conditions sous lesquelles la sortie doit être à 1. Ces conditions sont elles-mêmes réalisables avec les entrées du circuit avec {logicref}`xor_build2_step3.{and1,and2,inv1,inv2}|des portes **ET** et des inverseurs` directement connectés aux entrées.

On fait également les constats suivants :
 * plusieurs circuits logiques différents peuvent réaliser la même fonction de sortie,
 * l'approche systématique décrite ici ne livre pas forcément le circuit le plus compact: on a obtenu un circuit avec cinq portes pour réaliser un **OU-X** alors que l'approche ad hoc a conduit à la construction d'un circuit à quatre portes.


`````{exercise} Analyse d'un circuit

En annotant le schéma logique avec les quatre cas de figure possibles pour les entrées $X$ et $Y$, faites l'analyse du circuit **OU-X** ci-dessus construit avec l'approche systématique et montrez que la table de vérité ainsi reconstituée est la même que celle de la porte **OU-X**.

````{dropdown} Indice
```{logic}
:height: 180
:mode: tryout

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 0, "name": "X", "val": 0},
    {"pos": [50, 150], "id": 1, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [400, 90], "id": 2, "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [340, 90], "in": [6, 7], "out": 8},
    {"type": "AND", "pos": [230, 50], "in": [3, 4], "out": 5},
    {"type": "AND", "pos": [230, 130], "in": [9, 10], "out": 11},
    {"type": "NOT", "pos": [160, 60], "in": 12, "out": 13},
    {"type": "NOT", "pos": [160, 120], "in": 14, "out": 15}
  ],
  "wires": [
    [8, 2], [13, 4], [15, 9], [0, 3], [0, 14], [1, 12], [1, 10],
    [5, 6], [11, 7]
  ]
}
```
````
`````


`````{exercise} Porte cachée

Quelle est la porte cachée de ce circuit ?
````{logic}
:height: 100
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 3, "name": "X", "val": 0},
    {"pos": [50, 70], "id": 4, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [220, 50], "id": 5, "name": "Z"}],
  "gates": [{"type": "OR", "pos": [150, 50], "in": [0, 1], "out": 2, "showAsUnknown": true}],
  "wires": [[3, 0], [4, 1], [2, 5]]
}
````
```{dropdown} Corrigé
C'est une porte **OU**.
```
`````

`````{exercise} Circuit défectueux

Analysez ce circuit. De quel type de portes est-il constitué ? Fonctionne-t-il correctement ? Déterminez ce qui pose problème. Dites ce que fait ce circuit une fois corrigé et écrivez sa table de vérité.

````{logic}
:ref: faulty_and
:height: 140
:mode: tryout

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 3, "name": "X", "val": 0},
    {"pos": [50, 70], "id": 4, "name": "Y", "val": 0},
    {"pos": [50, 110], "id": 6, "name": "W", "val": 0}
  ],
  "out": [{"pos": [320, 70], "id": 5, "name": "Z"}],
  "gates": [
    {"type": "AND", "pos": [150, 50], "in": [0, 1], "out": 2, "ref": "ok"},
    {"type": "OR", "pos": [260, 70], "in": [7, 8], "out": 9, "poseAs": "AND", "ref": "faulty"}
  ],
  "wires": [[3, 0], [4, 1], [6, 8], [2, 7], [9, 5]]
}
````

````{dropdown} Indice
Voici le circuit corrigé (il a la même apparence que le circuit de la question, mais toutes les portes fonctionnent ici correctement).
```{logic}
:height: 140
:mode: tryout

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 30], "id": 3, "name": "X", "val": 0},
    {"pos": [50, 70], "id": 4, "name": "Y", "val": 0},
    {"pos": [50, 110], "id": 6, "name": "W", "val": 0}
  ],
  "out": [{"pos": [320, 70], "id": 5, "name": "Z"}],
  "gates": [
    {"type": "AND", "pos": [150, 50], "in": [0, 1], "out": 2},
    {"type": "AND", "pos": [260, 70], "in": [7, 8], "out": 9}
  ],
  "wires": [[3, 0], [4, 1], [6, 8], [2, 7], [9, 5]]
}
```
````

````{dropdown} Corrigé
Ce circuit est constitué de {logicref}`faulty_and.{ok,faulty}|deux portes **ET**`. Mais {logicref}`faulty_and.faulty|la porte **ET** de droite` semble poser problème, parce qu'elle se comporte comme une porte **OU** ! Le circuit montré dans l'indice se comporte correctement.

Ce circuit, une fois corrigé, implémente en fait un **ET** à trois entrées $X$, $Y$ et $W$, où la sortie $Z$ ne vaut 1 que si les trois entrées valent 1. Sa table de vérité, à huit lignes dues aux trois entrées, est ainsi la suivante :

| $X$ | $Y$ | $W$ | $Z$ |
| :-: | :-: | :-: | :-: |
| 0   | 0   | 0   | 0   |
| 0   | 0   | 1   | 0   |
| 0   | 1   | 0   | 0   |
| 0   | 1   | 1   | 0   |
| 1   | 0   | 0   | 0   |
| 1   | 0   | 1   | 0   |
| 1   | 1   | 0   | 0   |
| 1   | 1   | 1   | 1   |
````
`````


`````{exercise} Conception d'un circuit

Écrivez la table de vérité de ce circuit, dont une partie est masquée :

```{logic}
:height: 100
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 3, "name": "X", "val": 0},
    {"pos": [50, 70], "id": 4, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [220, 50], "id": 5, "name": "Z"}],
  "gates": [{"type": "RIMPLY", "pos": [150, 50], "in": [0, 1], "out": 2, "showAsUnknown": true}],
  "wires": [[3, 0], [4, 1], [2, 5]]
}
```

```{dropdown} Corrigé
| $X$ | $Y$ | $Z$ |
| :-: | :-: | :-: |
| 0   | 0   | 1   |
| 0   | 1   | 0   |
| 1   | 0   | 1   |
| 1   | 1   | 1   |
```


Réalisez ensuite un circuit logique avec les mêmes deux entrées $X$ et $Y$ et la même sortie $Z$ qui implémente cette table de vérité. On peut utiliser des portes **ET** et **OU** et des inverseurs. Glissez les portes depuis la gauche pour en ajouter, et glissez entre les connecteurs rond pour les connecter.

```{logic}
:height: 350
:showonly: AND OR NOT

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 40], "id": 3, "name": "X", "val": 0},
    {"pos": [50, 160], "id": 4, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [380, 100], "id": 5, "name": "Z"}]
}
```

````{dropdown} Indice 1
On peut lire cette fonction comme «$Z$ vaut 1 lorsque $X$ et $Y$ sont les deux à 0 (la première ligne de la table de vérité) ou lorsque $X$ est à 1 (les deux dernières lignes)».
````

````{dropdown} Indice 2
$Z$ est donc le **OU** de $X$ et du **ET** de l'inverse de $X$ et de $Y$.
````

````{dropdown} Corrigé
Il y plusieurs solutions possibles. Celle qui correspond aux indices est la suivante:

```{logic}
:height: 200
:mode: tryout

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 40], "id": 3, "name": "X", "val": 0},
    {"pos": [50, 160], "id": 4, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [380, 100], "id": 5, "name": "Z"}],
  "gates": [
    {"type": "AND", "pos": [230, 110], "in": [0, 1], "out": 2},
    {"type": "OR", "pos": [320, 100], "in": [6, 7], "out": 8},
    {"type": "NOT", "pos": [130, 100], "in": 9, "out": 10},
    {"type": "NOT", "pos": [130, 160], "in": 11, "out": 12}
  ],
  "wires": [[3, 6], [8, 5], [2, 7], [3, 9], [10, 0], [4, 11], [12, 1]]
}
```

Une autre solution est la suivante, où on se dit qu'on construit d'abord une {logicref}`imply_exercise_key2.{inv1,and}|partie du circuit` qui identifie le cas où $X=0$ et $Y=1$, et on l'{logicref}`imply_exercise_key2.inv2|inverse` pour correspondre à la table de vérité.
```{logic}
:ref: imply_exercise_key2
:height: 130
:mode: tryout

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 40], "id": 3, "name": "X", "val": 0},
    {"pos": [50, 90], "id": 4, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [410, 80], "id": 5, "name": "Z"}],
  "gates": [
    {"type": "NOT", "pos": [320, 80], "ref": "inv2", "in": 17, "out": 18},
    {"type": "AND", "pos": [230, 80], "ref": "and", "in": [19, 20], "out": 21},
    {"type": "NOT", "pos": [130, 40], "ref": "inv1", "in": 22, "out": 23}
  ],
  "wires": [[18, 5], [21, 17], [4, 20], [23, 19], [3, 22]]
}
```

Voici un circuit plus simple, qui fait la même chose mais qui est plus difficile à concevoir d'emblée :
```{logic}
:height: 120
:mode: tryout

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [
    {"pos": [50, 40], "id": 3, "name": "X", "val": 0},
    {"pos": [50, 80], "id": 4, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [290, 60], "id": 5, "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [230, 60], "in": [6, 7], "out": 8},
    {"type": "NOT", "pos": [120, 80], "in": 11, "out": 12}
  ],
  "wires": [[3, 6], [8, 5], [4, 11], [12, 7]]
}
```

En fait, il existe même une porte spéciale qui réalise exactement la fonction correspondant à la table de vérité, la porte **IMPLIQUE** :
```{logic}
:height: 120
:mode: tryout

{
  "v": 3,
  "opts": {"showGateTypes": true},
  "in": [{
    "pos": [50, 40], "id": 3, "name": "X", "val": 0},
    {"pos": [50, 80], "id": 4, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [230, 60], "id": 5, "name": "Z"}],
  "gates": [{"type": "RIMPLY", "pos": [160, 60], "in": [0, 1], "out": 2}],
  "wires": [[3, 0], [4, 1], [2, 5]]
}
```

````

`````
