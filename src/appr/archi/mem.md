# Mémoire

Les {glo}`transistor|transistors`, les {glo}`portelogique|portes logiques` et leur représentation en {glo}`tableverite|tables de vérités`, permettent de manipuler des 0 et des 1 au niveau physique.. Tant qu'un courant électrique se déplace dans les {glo}`circuit|circuits`, on est capable de le transformer, de le laisser passer ou de l'arrêter, dans le but d'exprimer des portes « ouvertes » ou des portes « fermées » et donc des nombres binaires. L'ALU, explorée au chapitre précédent, va une étape plus loin et permet de choisir une opération à effectuer en fonction de bits de contrôle supplémentaire, et livre le résultat de l'opération arithmétique ou logique choisie.

Mais comment faire pour {glo}`stockage|stocker` cette information ? Comment faire pour que l'on se rappelle le résultat d'une addition effectuée par une ALU afin de pouvoir réutiliser cette valeur plus tard ? C'est là que nous avons besoin de _mémoire_.

Dans les ordinateurs, il y a en fait plusieurs types de {glo}`stockage|mémoires`, qu'on peut classer en deux grandes catégories. La {glo}`memvolatile|mémoire volatile`, et la mémoire non volatile. La mémoire volatile s'efface quand la machine et éteinte. C'est le cas de la RAM (_random-access memory_), par exemple. La {glo}`memnonvolatile|mémoire non volatile`, elle, persiste. C'est le cas d'un disque dur ou d'un SSD (_solid-state drive_). Si un smartphone s'éteint inopinément alors qu'on est en train de retoucher une photo sans avoir validé les modifications, ces retouches disparaissent. Elles étaient stockées sur la mémoire volatile. Par contre, au moment où ces retouches sont sauvegardées, elles s'inscrivent dans la mémoire non volatile.

On peut se demander pourquoi on n'utiliserait pas que de la mémoire non volatile, vu les « risques » posés par la mémoire volatile. La réponse est que la mémoire non volatile va probablement être entre 100 et 100 000 fois moins rapide que la mémoire volatile. On privilégie donc la mémoire volatile comme mémoire de travail rapide d'un ordinateur.

Dans les sections qui suivent, on propose de s'intéresser au cas le plus simple: la construction d'une cellule de mémoire volatile qui sera à même de stocker un bit. Par la suite, nous discuterons de la manière dont ce genre de mémoire est utilisée au cœur des microprocesseurs.


## Le verrou SR

L'idée principale derrière la conception d'un circuit logique qui est capable de stocker un signal est que l'on va utiliser la ou les sorties du circuit en les reconnectant à certaines de ses entrées. Essayons par exemple ce circuit simple avec une seule porte **OU** :

```{logic}
:height: 100
:mode: tryout
:ref: latch_build1

{
  "v": 3,
  "in": [{"pos": [50, 30], "id": 4, "name": "X", "val": 0}],
  "gates": [{"type": "OR", "pos": [140, 40], "in": [5, 6], "out": 7}],
  "out": [{"pos": [240, 40], "id": 0, "name": "Z"}],
  "wires": [[4, 5], [7, 6, {"via": [[170, 80, "w"], [110, 80, "w"]]}], [7, 0]]
}
```

Au début, les deux entrées de la porte valent 0, comme sa sortie. Si l'on essaie de faire passer l'entrée $X$ à 1, on voit que la sortie $Z$ passera à 1 elle aussi, comme il s'agit d'une porte **OU**. Mais comme $Z$ est aussi relié à l'autre entrée de la porte, on a maintenant un circuit dont on ne peut plus modifier la sortie : même si $X$ passe de nouveau à 0, l'autre entrée reste à 1 et suffit donc pour que $Z$ vaille maintenant 1 indéfiniment. On est obligé de remettre le circuit complètement à zéro (l'équivalent de débrancher la prise de courant et de la rebrancher) pour obtenir à nouveau un 0 sur la sortie $Z$.

Assurément, ce circuit n'est pas très intéressant : il se bloque dans un état sans retour possible. Il faudrait pouvoir faire repasser la valeur de sortie à 0. Pour ce faire, une idée est d'ajouter {logicref}`latch_build2.and|une porte **ET**` avant de faire repasser la sortie de {logicref}`latch_build2.or|la porte **OU**` dans sa propre entrée. Cela nous permet d’annuler le signal de retour si la seconde entrée du **ET** (appelons-la $Y$) vaut 0.

Essayez ce circuit : quand $Y$ vaut 1, il se comporte comme le circuit précédent, mais se remettra à 0 dès qu'$Y$ passera à 0.

```{logic}
:height: 180
:mode: tryout
:ref: latch_build2

{
  "v": 3,
  "in": [
    {"pos": [50, 40], "id": 4, "name": "X", "val": 0},
    {"pos": [50, 140], "id": 8, "name": "Y", "val": 1}
  ],
  "out": [{"pos": [290, 50], "id": 3, "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [170, 50], "ref": "or", "in": [0, 1], "out": 2},
    {"type": "AND", "pos": [170, 100], "orient": "w", "ref": "and", "in": [5, 6], "out": 7}
  ],
  "wires": [[2, 3], [4, 0], [7, 1, {"style": "bezier"}], [2, 6, {"style": "bezier"}], [8, 5, {"via": [[210, 140]], "style": "bezier"}]]
}
```

Le circuit est plus facile à utiliser lorsqu'on inverse l'entrée $Y$, comme dans le circuit suivant :

```{logic}
:height: 190
:mode: tryout
:ref: latch_build3

{
  "v": 3,
  "in": [
    {"pos": [50, 40], "id": 4, "name": "X", "val": 0},
    {"pos": [50, 150], "id": 8, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [290, 50], "id": 3, "name": "Z"}],
  "gates": [
    {"type": "OR", "pos": [170, 50], "in": [0, 1], "out": 2},
    {"type": "AND", "pos": [170, 100], "orient": "w", "in": [5, 6], "out": 7},
    {"type": "NOT", "pos": [170, 150], "in": 9, "out": 10}
  ],
  "wires": [[2, 3], [4, 0], [7, 1, {"style": "bezier"}], [2, 6, {"style": "bezier"}], [8, 9], [10, 5, {"style": "bezier"}]]
}
```

Dans ce circuit-ci, on peut considérer que :

 * Tant que $Y$ est inactif (donc vaut 0), le passage de $X$ de 0 à 1 fait passer la sortie $Z$ à 1. Ceci fait donc en sorte que la sortie « verrouille » sur la valeur 1, car elle garde sa valeur même si $X$ repasse à 0.
 * Tant que $X$ est inactif, le passage de $Y$ de 0 à 1 fait passer la sortie $Z$ à 0, et la sortie se « verrouille » ainsi à 0 même si $Y$ repasse à 0.

On appelle effectivement ce genre de circuits des {glo}`verrou|verrous`. Nous avons ici construit un des plus simples. D'habitude, son entrée $X$ est appelée $S$, pour _set_ en anglais, qui dénote le stockage d'un 1, et son entrée $Y$ est appelée $R$, pour _reset_ en anglais, qui dénote sa remise à zéro. C'est le verrou dit  « SR », pour _set/reset_. Un tel verrou est donc une minicellule mémoire ! La sortie de ces cellules mémoires est fréquemment appelée $Q$ plutôt que $Z$, nous allons donc faire pareil dans la suite du texte.

Voici une représentation équivalente du même circuit[^demorgan], donc du même verrou SR :

[^demorgan]: On peut montrer l'équivalence de ce circuit et du précédent à l'aide des [lois de De Morgan](https://fr.wikipedia.org/wiki/Lois_de_De_Morgan), qui ne sont volontairement pas abordées dans ce chapitre.

```{logic}
:height: 220
:mode: tryout

{
  "v": 3,
  "opts": {"propagationDelay": 10},
  "in": [
    {"pos": [50, 180], "id": 8, "name": "R", "val": 0},
    {"pos": [50, 40], "id": 9, "name": "S", "val": 0}
  ],
  "out": [
    {"pos": [340, 50], "id": 10, "name": "Q"},
    {"pos": [340, 170], "id": 11, "name": "Q̅"}
  ],
  "gates": [
    {"type": "OR", "pos": [240, 170], "in": [0, 1], "out": 2},
    {"type": "OR", "pos": [240, 50], "in": [4, 5], "out": 6},
    {"type": "NOT", "pos": [120, 70], "in": 3, "out": {"id": 7, "initialValue": 0}},
    {"type": "NOT", "pos": [120, 150], "in": 12, "out": 13}
  ],
  "wires": [[9, 4], [7, 5], [8, 1], [13, 0], [2, 3, {"via": [[90, 100, "w"]]}], [6, 12, {"via": [[90, 120, "w"]]}], [6, 10], [2, 11]]
}
```

Ce circuit stocke ainsi un bit de donnée — un 0 ou un 1 — qu'on va pouvoir lire via la sortie $Q$ et modifier avec les deux entrées $R$ et $S$. (La seconde sortie $\bar{Q}$ est ici toujours l'inverse de $Q$.)

Testez le circuit ci-dessus et observez l'effet de $R$ et $S$ pour vérifier qu'il correspond bien à notre circuit précédent.

On essaie en général d'éviter d'avoir un 1 sur $R$ et sur $S$ en même temps, car cela place le verrou dans un état où $\bar{Q}$ n'est plus l'inverse de $Q$. Pour cette raison, nous allons plutôt créer le circuit comme dans le schéma suivant. Les connexions sont exactement les mêmes, mais les entrées $S$ et $R$ ne restent pas à 1 lorsqu'on clique dessus, elles retombent à 0 dès que le clic se termine — elles se comportent comme des boutons poussoirs.

```{logic}
:height: 220
:mode: tryout

{
  "v": 3,
  "opts": {"propagationDelay": 0},
  "in": [
    {"pos": [50, 180], "id": 8, "name": "R", "val": 0, "isPushButton": true},
    {"pos": [50, 40], "id": 9, "name": "S", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [340, 50], "id": 10, "name": "Q"},
    {"pos": [340, 170], "id": 11, "name": "Q̅"}
  ],
  "gates": [
    {"type": "OR", "pos": [240, 170], "in": [0, 1], "out": 2},
    {"type": "OR", "pos": [240, 50], "in": [4, 5], "out": 6},
    {"type": "NOT", "pos": [120, 70], "in": 3, "out": {"id": 7, "initialValue": 0}},
    {"type": "NOT", "pos": [120, 150], "in": 12, "out": 13}
  ],
  "wires": [[9, 4], [7, 5], [8, 1], [13, 0], [2, 3, {"via": [[90, 100, "w"]]}], [6, 12, {"via": [[90, 120, "w"]]}], [6, 10], [2, 11]]
}
```

Ces verrous sont communs, et pour le reste du chapitre, on simplifiera la notation pour les représenter ainsi, sans changement de fonctionnalité, mais en faisant abstraction des détails internes :

```{logic}
:height: 100
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 70], "id": 10, "name": "R", "val": 0, "isPushButton": true},
    {"pos": [50, 30], "id": 11, "name": "S", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [210, 30], "id": 12, "name": "Q"},
    {"pos": [210, 70], "id": 13, "name": "Q̅"}
  ],
  "components": [
    {"type": "latch-sr", "pos": [130, 50], "in": [6, 7], "out": [8, 9], "state": 0}
  ],
  "wires": [[10, 7], [11, 6], [8, 12], [9, 13]]
}
```

````{dropdown} Pour aller plus loin
Voici une vidéo qui illustre ce principe de verrou SR.

```{youtube} KM0DdEaY5sY
:start: 4:58
```
````


## La bascule D

Un souci avec le verrou SR est qu'on a rarement un signal d'entrée qui soit facilement exploitable pour être « converti » en cette logique _set/reset_. La plupart du temps, on a simplement un signal donné, disons $D$, pour « donnée » (ou _data_ en anglais), et c'est ce signal-ci qu'on aimerait stocker. Avec ce système, il serait impossible de connecter $D$ à ce verrou ; on ne peut le brancher directement ni à l'entrée $S$, ni à l'entrée $R$.

On va utiliser pour cela un circuit similaire, mais qui fonctionne un peu différemment, qui s'appelle une **bascule D**[^flipflop] :

[^flipflop]: Il y a une différence conceptuelle fondamentale entre les verrous et les bascules : les verrous sont des composants dits _asynchrones_, dont l'état peut changer dès qu'une des entrées change, alors que les bascules sont des composants dits _synchrones_, qui ont une entrée appelée Horloge, et dont l'état ne changera qu'au moment où le signal d'horloge effectuera une transition (dans notre cas, passera de 0 à 1). Une discussion plus poussée de ces différences dépasse le cadre de ce cours.

```{logic}
:height: 120
:mode: tryout

{
  "v": 3,
  "opts": {"showDisconnectedPins": true},
  "in": [
    {"pos": [90, 40], "id": 0, "name": "D", "val": 0},
    {"pos": [90, 80], "id": 1, "name": "Horloge", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [250, 40], "id": 9, "name": "Q"},
    {"pos": [250, 80], "id": 10, "name": "Q̅"}
  ],
  "components": [
    {
      "type": "flipflop-d",
      "pos": [170, 60],
      "in": [3, 4, 5, 2],
      "out": [6, 7],
      "state": 0
    }
  ],
  "wires": [[0, 2], [1, 3], [6, 9], [7, 10]]
}
```

Cette bascule va stocker son entrée $D$ et la propager sur sa sortie $Q$ uniquement lorsque l'entrée spéciale $Horloge$ passe de 0 à 1. Le reste du temps, $Q$ et $\overline{Q}$ garderont leur valeur précédente. Notez que cette bascule a aussi deux entrées $Pre$ et $Clr$, ici déconnectées, qui servent à forcer l'état interne à valoir 1 ou 0, respectivement, indépendamment du signal $D$ et de l'horloge.

Testez cette bascule. Réglez l'entrée de données $D$ à 1 ou 0 et observez comme la bascule ne réagit pas : sa sortie $Q$ reste telle quelle. Donnez ensuite une impulsion en cliquant sur l'entrée $Horloge$ et voyez comme la valeur de $D$ est maintenant stockée sur la bascule.

````{togofurther} 

Pour aller plus loin, une vidéo de résumé qui parle aussi des bascules et des registres :

```{youtube} I0-izyq6q5s
```
````


`````{exercise} Stocker deux bits

Créez un circuit qui calcule, d'une part, le **OU** de deux entrées $X$ et $Y$, et, d'autre part, le **ET** de ces deux mêmes entrées. À l'aide de bascules D, complétez le circuit de manière à ce qu'il stocke ces deux valeurs calculées lors d'un coup d'horloge et les sorte sur les sorties $P$ et $Q$, respectivement. Faites finalement en sorte que le signal $Reset$, si activé, réinitialise les bascules à 0. Vérifiez qu'une fois les valeurs stockées par les bascules, des changements sur les entrées $X$ et $Y$ n'aient pas d'effet direct sur $P$ et $Q$.

```{logic}
:height: 400
:showonly: AND OR NOT XOR Flipflop-D

{
  "v": 3,
  "in": [
    {"pos": [100, 50], "id": 24, "name": "X", "val": 1},
    {"pos": [100, 130], "id": 25, "name": "Y", "val": 1},
    {"pos": [100, 200], "id": 26, "name": "Horloge", "val": 0, "isPushButton": true},
    {"pos": [100, 270], "id": 29, "name": "Reset", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [500, 50], "id": 27, "name": "P"},
    {"pos": [500, 160], "id": 28, "name": "Q"}
  ]
}
```

````{dropdown} Corrigé
```{logic}
:height: 320
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [100, 50], "id": 24, "name": "X", "val": 1},
    {"pos": [100, 130], "id": 25, "name": "Y", "val": 1},
    {"pos": [100, 200], "id": 26, "name": "Horloge", "val": 0, "isPushButton": true},
    {"pos": [100, 270], "id": 29, "name": "Reset", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [500, 50], "id": 27, "name": "P"},
    {"pos": [500, 160], "id": 28, "name": "Q"}
  ],
  "gates": [
    {"type": "OR", "pos": [210, 60], "in": [0, 1], "out": 2},
    {"type": "AND", "pos": [210, 120], "in": [3, 4], "out": 5}
  ],
  "components": [
    {
      "type": "flipflop-d",
      "pos": [390, 70],
      "in": [7, 8, 9, 6],
      "out": [10, 11],
      "state": 0
    },
    {
      "type": "flipflop-d",
      "pos": [390, 180],
      "in": [13, 14, 15, 12],
      "out": [16, 17],
      "state": 0
    }
  ],
  "wires": [
    [24, 0],
    [25, 1],
    [24, 3],
    [25, 4],
    [10, 27],
    [16, 28],
    [2, 6],
    [5, 12],
    [26, 7],
    [26, 13],
    [29, 15, {"via": [[340, 240]]}],
    [29, 9, {"via": [[340, 130]]}]
  ]
}
```
````
`````


`````{exercise} Signal alternatif

À l'aide d'une bascule, créez un circuit avec une sortie $Q$ qui s'inverse à chaque coup d'horloge.

```{logic}
:height: 300
:showonly: AND OR NOT XOR Flipflop-D

{
  "v": 3,
  "in": [
    {"pos": [100, 90], "id": 6, "name": "Horloge", "val": 0, "isPushButton": true}
  ],
  "out": [{"pos": [380, 90], "id": 7, "name": "Q"}]
}
```

````{dropdown} Corrigé
```{logic}
:height: 190
:mode: tryout

{
  "v": 3,
  "components": [
    {
      "type": "flipflop-d",
      "pos": [230, 100],
      "in": [1, 2, 3, 0],
      "out": [4, 5],
      "state": 0
    }
  ],
  "in": [
    {"pos": [100, 90], "id": 6, "name": "Horloge", "val": 0, "isPushButton": true}
  ],
  "out": [{"pos": [380, 90], "id": 7, "name": "Q"}],
  "wires": [
    [4, 7],
    [6, 1],
    [5, 0, {"via": [[290, 120, "n"], [290, 40, "n"], [190, 40, "w"]]}]
  ]
}
```
````
`````


`````{exercise} Jeu de fréquences

Observez le circuit ci-dessous. L'horloge principale $A$ fonctionne ici toute seule et produit un coup d'horloge par seconde (elle a donc une fréquence d'un hertz — 1 Hz). Que pouvez-vous dire des signaux $B$ et $C$ par rapport au signal $A$ ? Comment expliquer cela avec ce que vous savez des bascules ? (Pour simplifier, le délai de propagation est ici presque nul.)

Vous pouvez mettre l'animation en pause et exécuter chaque transition pas à pas pour mieux comprendre ce qui se passe.

```{logic}
:height: 280
:mode: tryout

{
  "v": 3,
  "opts": {"propagationDelay": 0},
  "in": [{"type": "clock", "pos": [40, 30], "id": 30, "period": 1000}],
  "out": [
    {"pos": [380, 30], "id": 7, "name": "A"},
    {"pos": [380, 80], "id": 10, "name": "B"},
    {"pos": [380, 130], "id": 11, "name": "C"}
  ],
  "components": [
    {
      "type": "flipflop-d",
      "pos": [180, 100],
      "in": [13, 14, 15, 12],
      "out": [16, 17],
      "state": 1
    },
    {
      "type": "flipflop-d",
      "pos": [180, 230],
      "in": [25, 26, 27, 24],
      "out": [28, 29],
      "state": 1
    }
  ],
  "wires": [
    [16, 25, {"via": [[250, 120, "s"], [120, 180, "s"]]}],
    [16, 10],
    [28, 11],
    [17, 12, {"via": [[230, 120], [230, 50], [140, 50]]}],
    [29, 24, {"via": [[230, 250], [230, 180], [140, 180]]}],
    [30, 13],
    [30, 7]
  ]
}
```

````{dropdown} Corrigé
Le signal $B$ a une fréquence deux fois plus petite que le signal $A$, et le signal $C$, de façon similaire, a une fréquence deux fois plus petite que le signal $B$. Ainsi, $B$ « bat » à 0.5 Hz et $C$ à 0.25 Hz.

TODO ajouter explication

Si ce petit circuit fonctionne à 1 Hz, les appareils que nous utilisons aujourd'hui ont des horloges qui fonctionnent à plusieurs gigahertz (GHz), c'est-à-dire plusieurs milliards de fois plus vite. On attend ainsi moins d'une nanoseconde entre deux coups d'horloge.
````
`````


## Addition en plusieurs étapes

Dans cet exemple final, nous allons construire un circuit capable d'effectuer l'addition de plusieurs nombres ; par exemple, d'évaluer la somme $1 + 4 + 5 + 3$ pour trouver $13$.

Si ce calcul a l'air simple, il s'y cache une subtilité : nous n'avons aucun circuit auquel nous pourrions donner quatre nombres et qui en ferait la somme. Nous ne savons additionner que deux nombres à la fois. Mais nous pouvons additionner progressivement les nombres un à un à une sorte d'« accumulateur » qui stockerait les résultats intermédiaires. Au début, avant d'avoir additionné quoi que ce soit, cet accumulateur représenterait un 0. Ensuite, on y additionnerait, l'un après l'autre, chacun des nombres du calcul ainsi :

$$\begin{aligned}
0 + 1 &= 1 \\
1 + 4 &= 5 \\
5 + 5 &= 10 \\
10 + 3 &= 13
\end{aligned}$$

Chacune de ces lignes a la forme « accumulateur + nombre à additionner = nouvel accumulateur ».

L'avantage de procéder ainsi, en décomposant à l'extrême, est que chaque étape est une addition de précisément deux nombres — et nous savons faire de telles additions avec une ALU.

Commençons à créer un circuit capable de faire ceci. Notre ALU opérant sur des nombres de 4 bits, prenons le parti de représenter notre accumulateur via également 4 bits — 4 cellules mémoire, et donc 4 bascules. Pour remettre l'accumulateur à zéro, nous allons connecter un signal unique au _reset_ de chacune de ces bascules. Nous allons aussi, comme chaque fois, connecter un signal d'horloge aux bascules, pour leur indiquer leur moment où elles doivent stocker les valeurs qui sont sur leurs entrées respectives. Ajoutons aussi une ALU pour effectuer l'addition et un afficheur décimal pour les 4 bits stockés dans les bascules.

Cela nous donne ce début de circuit, qui pour l'instant n'est pas fonctionnel :

```{logic}
:height: 510
:mode: tryout

{
  "v": 3,
  "opts": {"showDisconnectedPins": true},
  "in": [
    {
      "pos": [340, 450],
      "orient": "n",
      "id": 40,
      "name": "Reset",
      "val": 0,
      "isPushButton": true
    },
    {
      "pos": [280, 450],
      "orient": "n",
      "id": 45,
      "name": "Horloge",
      "val": 0,
      "isPushButton": true
    }
  ],
  "components": [
    {
      "type": "alu",
      "pos": [180, 170],
      "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 50],
      "out": [10, 11, 12, 13, 14, 15]
    },
    {
      "type": "flipflop-d",
      "pos": [390, 60],
      "in": [17, 18, 19, 16],
      "out": [20, 21],
      "state": 0
    },
    {
      "type": "flipflop-d",
      "pos": [390, 160],
      "in": [23, 24, 25, 22],
      "out": [26, 27],
      "state": 0
    },
    {
      "type": "flipflop-d",
      "pos": [390, 260],
      "in": [29, 30, 31, 28],
      "out": [32, 33],
      "state": 0
    },
    {
      "type": "flipflop-d",
      "pos": [390, 360],
      "in": [35, 36, 37, 34],
      "out": [38, 39],
      "state": 0
    }
  ],
  "out": [
    {"type": "nibble", "pos": [550, 190], "id": [46, 47, 48, 49], "name": "Acc."}
  ],
  "wires": [
    [40, 37, {"via": [[340, 400]]}],
    [40, 31, {"via": [[340, 300, "n"]]}],
    [40, 25, {"via": [[340, 200, "n"]]}],
    [40, 19, {"via": [[340, 100, "n"]]}],
    [45, 35, {"via": [[280, 380]]}],
    [45, 29, {"via": [[280, 280, "n"]]}],
    [45, 23, {"via": [[280, 180, "n"]]}],
    [45, 17, {"via": [[280, 80, "n"]]}],
    [20, 46, {"via": [[480, 40]]}],
    [26, 47, {"via": [[480, 140]]}],
    [32, 48, {"via": [[480, 240]]}],
    [38, 49, {"via": [[480, 340]]}]
  ]
}
```

Connectons maintenant les entrées de l'ALU. On se rappelle qu'à chaque étape, l'ALU calculera une addition de la forme « accumulateur + nombre à additionner = nouvel accumulateur ». L'entrée $A$ de l'ALU est la valeur de l'accumulateur, donc ce qui est stocké par nos bascules. On connecte donc la sortie $Q$ de chaque bascule vers le bit d'entrée $A$ correspondant de l'ALU.

L'entrée $B$ de l'ALU est le nouveau nombre à additionner. Pour cela, nous ajoutons simplement quatre entrées normales, ainsi qu'un afficheur décimal pour nous simplifier la lecture du nombre représenté par ces entrées :

```{logic}
:height: 550
:mode: tryout

{
  "v": 5,
  "opts": {"showDisconnectedPins": true},
  "in": [
    {"pos": [340, 490], "orient": "n", "id": 40, "name": "Reset", "isPushButton": true},
    {"pos": [280, 490], "orient": "n", "id": 45, "name": "Horloge", "isPushButton": true},
    {"bits": 4, "pos": [35, 260], "id": [54, "57-59"]}
  ],
  "out": [
    {"type": "display", "pos": [100, 390], "orient": "s", "id": "50-53", "name": "B"},
    {"type": "display", "pos": [550, 230], "id": "46-49", "name": "Acc."}
  ],
  "ic": [
    {"type": "alu", "pos": [180, 210], "in": ["0-9", 55], "out": ["10-13", 56, 15, 14]},
    {"type": "flipflop-d", "pos": [390, 100], "in": ["17-19", 16], "out": [20, 21]},
    {"type": "flipflop-d", "pos": [390, 200], "in": ["23-25", 22], "out": [26, 27]},
    {"type": "flipflop-d", "pos": [390, 300], "in": ["29-31", 28], "out": [32, 33]},
    {"type": "flipflop-d", "pos": [390, 400], "in": ["35-37", 34], "out": [38, 39]}
  ],
  "wires": [[40, 37, {"via": [[340, 440]]}], [40, 31, {"via": [[340, 340, "n"]]}], [40, 25, {"via": [[340, 240, "n"]]}], [40, 19, {"via": [[340, 140, "n"]]}], [20, 0, {"via": [[430, 80], [430, 50], [130, 50], [130, 130]]}], [26, 1, {"via": [[440, 180], [440, 40], [120, 40], [120, 150]]}], [32, 2, {"via": [[450, 280], [450, 30], [110, 30], [110, 170]]}], [38, 3, {"via": [[460, 380, "n"], [460, 20], [100, 20], [100, 190]]}], [45, 35, {"via": [[280, 420]]}], [45, 29, {"via": [[280, 320, "n"]]}], [45, 23, {"via": [[280, 220, "n"]]}], [45, 17, {"via": [[280, 120, "n"]]}], [20, 46, {"via": [[480, 80]]}], [26, 47, {"via": [[480, 180]]}], [32, 48, {"via": [[480, 280]]}], [38, 49, {"via": [[480, 380]]}], [54, 4], [57, 5], [58, 6], [59, 7], [54, 50], [57, 51], [58, 52], [59, 53]]
}
```

Il reste à connecter la sortie $S$ de l'ALU. Cette sortie nous livre la prochaine valeur à stocker dans l'accumulateur, et nous pouvons ainsi la connecter aux quatre entrées $D$ des bascules.

Voici le circuit final :

```{logic}
:height: 550
:mode: tryout

{
  "v": 5,
  "opts": {"showDisconnectedPins": true},
  "in": [
    {"pos": [340, 490], "orient": "n", "id": 40, "name": "Reset", "isPushButton": true},
    {"pos": [280, 490], "orient": "n", "id": 45, "name": "Horloge", "isPushButton": true},
    {"bits": 4, "pos": [35, 260], "id": [54, "57-59"]}
  ],
  "out": [
    {"type": "display", "pos": [100, 390], "orient": "s", "id": "50-53", "name": "B"},
    {"type": "display", "pos": [550, 230], "id": "46-49", "name": "Acc."}
  ],
  "ic": [
    {"type": "alu", "pos": [180, 210], "in": ["0-9", 55], "out": ["10-13", 56, 15, 14]},
    {"type": "flipflop-d", "pos": [390, 100], "in": ["17-19", 16], "out": [20, 21]},
    {"type": "flipflop-d", "pos": [390, 200], "in": ["23-25", 22], "out": [26, 27]},
    {"type": "flipflop-d", "pos": [390, 300], "in": ["29-31", 28], "out": [32, 33]},
    {"type": "flipflop-d", "pos": [390, 400], "in": ["35-37", 34], "out": [38, 39]}
  ],
  "wires": [[40, 37, {"via": [[340, 440]]}], [40, 31, {"via": [[340, 340, "n"]]}], [40, 25, {"via": [[340, 240, "n"]]}], [40, 19, {"via": [[340, 140, "n"]]}], [20, 0, {"via": [[430, 80], [430, 50], [130, 50], [130, 130]]}], [26, 1, {"via": [[440, 180], [440, 40], [120, 40], [120, 150]]}], [32, 2, {"via": [[450, 280], [450, 30], [110, 30], [110, 170]]}], [38, 3, {"via": [[460, 380, "n"], [460, 20], [100, 20], [100, 190]]}], [45, 35, {"via": [[280, 420]]}], [45, 29, {"via": [[280, 320, "n"]]}], [45, 23, {"via": [[280, 220, "n"]]}], [45, 17, {"via": [[280, 120, "n"]]}], [20, 46, {"via": [[480, 80]]}], [26, 47, {"via": [[480, 180]]}], [32, 48, {"via": [[480, 280]]}], [38, 49, {"via": [[480, 380]]}], [54, 4], [57, 5], [58, 6], [59, 7], [54, 50], [57, 51], [58, 52], [59, 53], [10, 16, {"via": [[275, 80]]}], [11, 22, {"via": [[260, 180]]}], [12, 28, {"via": [[260, 280]]}], [13, 34, {"via": [[260, 380]]}]]
}
```

Ce circuit fonctionne ainsi : au début du calcul, on réinitialise les bascules à zéro avec le signal $Reset$. Ensuite, on compose le prochain nombre à additionner sur l'entrée $B$. L'ALU va calculer immédiatement la somme $A + B$, mais ce n'est qu'au prochain coup d'horloge que cette somme sera stockée dans les bascules et apparaîtra ainsi à droite. Après avoir donné ce coup d'horloge, donc, on pourra à nouveau composer sur l'entrée $B$ le prochain nombre à additionner, et ainsi de suite.

On réalise ici l'importance du coup d'horloge : si les bascules stockaient immédiatement la valeur livrée par l'ALU sans attendre le coup d'horloge, on retrouverait presque sans délai cette valeur sur la sortie des bascules et donc… à l'entrée $A$ de l'ALU, qui recalculerait immédiatement la somme de cette valeur et de l'entrée $B$, livrerait le résultat sur la sortie vers les bascules, qui feraient à nouveau la propagation immédiate de ceci sur leurs sorties et sur l'entrée $A$ de l'ALU, etc. — le système s'emballerait. Le signal d'horloge veille à ce que l'opération de stockage et de propagation soit coordonnée et se passe au bon moment.

`````{exercise} Additions avec bascules

Suivez la procédure décrite ci-dessus pour effectuer l'addition $1 + 4 + 5 + 3 = 13$.
`````

## Récapitulatif

Au cours des quatre chapitres précédents, nous avons vu comment les portes logiques sont utilisées comme composants de base des ordinateurs. Nous avons d'abord exploré des portes simples comme **OU** et **ET**, puis montré comment ces portes peuvent être combinées en systèmes logiques plus complexes.

Avec des portes, nous avons construit un additionneur de deux bits. Nous avons ensuite été à même, en enchaînant plusieurs additionneurs, de créer un système qui peut additionner non pas simplement deux bits, mais deux nombres entiers codés sur 4 bits chacun.

Nous avons ensuite découvert l'unité arithmétique et logique, capable de réaliser plusieurs opérations différentes avec ses entrées en fonction de bits supplémentaires qui permettent de sélectionner l'opération à effectuer.

Notre dernière étape d'exploration des systèmes logiques nous a menés aux verrous et aux bascules, des composants pensés pour stocker des bits de données et ainsi constituer des cellules de mémoire pour l'ordinateur. Nous avons enfin été capables, avec une ALU et une série de bascules, d'additionner à la chaîne plusieurs nombres, en nous rappelant les résultats des additions intermédiaires.

Il existe bien d'autres éléments qui composent les ordinateurs et nous n'avons pas l'occasion de tous les explorer en détail. Dans la section qui suit, faisons un saut conceptuel et parlons de l'architecture générale des ordinateurs et de la manière dont les grands composants sont interconnectés pour permettre à un ordinateur de remplir les fonctions que nous lui connaissons.


````{dropdown} Jeu pour aller plus loin
Dans le jeu en ligne « Nandgame » (<https://nandgame.com>), on construit petit à petit un ordinateur complet juste avec, à la base, des portes **NON-ET**. Elles ont la particularité (avec les portes **NON-OU**, d'ailleurs) de pouvoir simuler toutes les autres portes — y compris un inverseur.
````
