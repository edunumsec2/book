# ALU

Dans cette section, nous continuons notre exploration de comment les portes logiques, selon leur assemblage, fournissent les fonctionnalités de base des ordinateurs. En particulier, nous nous intéressons à comment faire effectuer plusieurs opérations à un ordinateur via ce qui s'appelle une **unité arithmétique et logique**, ou simplement une ALU.

Dans la section précédente, nous avons vu comment créer, via un assemblage de portes logiques, un circuit qui réalise l'addition de deux nombres de 4 bits. Ce circuit était fixe : avec les deux nombres d'entrées, il réalisait toujours une addition et ne servait ainsi qu'à ça.

Les ordinateurs ont la propriété d'être programmables : ils savent effectuer plusieurs opérations, et c'est la manière dont ils sont programmés qui va déterminer l'opération qu'ils effectuent. C'est aussi vrai pour des machines plus simples ; une calculatrice de poche, par exemple, pourra effectuer au moins les quatre opérations de base : addition, soustraction, multiplication et division.

Le composant qui nous permettra de sélectionner une opération ou une autre s'appelle « unité arithmétique et logique », communément appelé simplement « ALU » (de l'anglais _arithmetic logic unit_). Avant d'inspecter une ALU, nous avons besoin de comprendre comment on peut sélectionner une opération ou une autre avec des circuits logiques.

## Sélection de l'opération

Comment créer un circuit qui permet de sélectionner une opération à faire, et comment indiquer l'opération à sélectionner ? Essayons d'abord de créer un circuit à deux entrées qui va calculer soit le **OU** soit le **ET** de ces deux entrées.

Nous savons faire un circuit simple qui calcule le **OU** de deux entrées $X$ et $Y$, avec {logicref}`two_signal_tryout1.or|une seule porte logique` :

```{logic}
:height: 140
:mode: tryout
:ref: two_signal_tryout1

{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 0, "name": "X", "val": 0},
    {"pos": [50, 110], "id": 1, "name": "Y", "val": 0}
  ],
  "gates": [{"type": "OR", "pos": [180, 40], "ref": "or", "in": [6, 7], "out": 8}],
  "out": [{"pos": [250, 40], "id": 2, "name": "X OU Y"}],
  "wires": [[0, 6], [1, 7], [8, 2]]
}
```

Nous pouvons sans autre y ajouter {logicref}`two_signal_tryout2.and|une porte **ET**` pour calculer une autre sortie en parallèle, à partir des {logicref}`two_signal_tryout2.{x,y}|mêmes entrées` $X$ et $Y$ :

```{logic}
:height: 140
:mode: tryout
:ref: two_signal_tryout2

{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 0, "name": "X", "ref": "x", "val": 0},
    {"pos": [50, 110], "id": 1, "name": "Y", "ref": "y", "val": 0}
  ],
  "gates": [
    {"type": "OR", "pos": [180, 40], "in": [6, 7], "out": 8},
    {"type": "AND", "pos": [180, 100], "ref": "and", "in": [3, 4], "out": 5}
  ],
  "out": [
    {"pos": [250, 40], "id": 2, "name": "X OU Y"},
    {"pos": [250, 100], "id": 9, "name": "X ET Y"}
  ],
  "wires": [[0, 6], [1, 7], [8, 2], [0, 3], [1, 4], [5, 9]]
}
```

L'idée est maintenant de combiner ces sorties intermédiaires pour n'en avoir plus qu'une, qui sera soit le **OU**, soit le **ET**. Mais comment faire pour indiquer si l'on désire le **OU** ou le **ET** ? Nous pouvons rajouter une entrée pour choisir cette opération. Appelons-la $Op$, pour « opération ». Choisissons une convention : lorsque $Op$ vaut 0, nous souhaitons effectuer l'opération **OU**, et lorsque $Op$ vaut 1, nous souhaitons effectuer l'opération **ET**.

Ce que nous cherchons à créer est conceptuellement ce que fait {logicref}`mux_tryout.mux|ce composant tout prêt` ci-dessous. Il s’appelle _multiplexeur_ et connecte à {logicref}`mux_tryout.muxout|sa sortie` soit {logicref}`mux_tryout.muxin1|le signal du haut`, soit {logicref}`mux_tryout.muxin2|le signal du bas`, en fonction de la valeur de $Op$. Essayez de changer $Op$ :

```{logic}
:height: 240
:mode: tryout
:ref: mux_tryout

{
  "v": 3,
  "opts": {"showDisconnectedPins": true},
  "in": [
    {"pos": [50, 110], "id": 0, "name": "X", "val": 0},
    {"pos": [50, 190], "id": 1, "name": "Y", "val": 0},
    {"pos": [290, 50], "orient": "s", "id": 2, "name": "Op", "val": 0}
  ],
  "out": [{"pos": [390, 150], "id": 20, "name": "Z"}],
  "gates": [
    {"type": "AND", "pos": [180, 180], "in": [3, 4], "out": 5},
    {"type": "OR", "pos": [180, 120], "in": [6, 7], "out": 8}
  ],
  "components": [{"type": "mux-2to1", "pos": [290, 150], "ref": "mux", "in": [9, 10, 11], "out": 12}],
  "wires": [[0, 3], [1, 4], [0, 6], [1, 7], [12, 20, {"ref": "muxout"}], [8, 9, {"ref": "muxin1"}], [5, 10, {"ref": "muxin2"}], [2, 11]]
}
```

Mais comment construire ce multiplexeur avec les portes logiques que nous connaissons ? Sans le multiplexeur, voici ce que nous devons compléter :

```{logic}
:height: 270
:mode: tryout

{
  "v": 3,
  "opts": {"showDisconnectedPins": true},
  "labels": [
    {"type": "rect", "pos": [310, 170], "w": 140, "h": 140, "color": "grey", "strokeWidth": 2, "caption": "???", "captionPos": "c"}
  ],
  "in": [
    {"pos": [50, 140], "id": 0, "name": "X", "val": 0},
    {"pos": [50, 220], "id": 1, "name": "Y", "val": 0},
    {"pos": [310, 50], "orient": "s", "id": 2, "name": "Op", "val": 0}
  ],
  "out": [{"pos": [430, 180], "id": 20, "name": "Z"}],
  "gates": [{"type": "AND", "pos": [180, 210], "in": [3, 4], "out": 5}, {"type": "OR", "pos": [180, 150], "in": [6, 7], "out": 8}],
  "wires": [[0, 3], [1, 4], [0, 6], [1, 7]]
}
```

Pour savoir quelles portes utiliser pour recréer le multiplexeur, nous avons besoin de nous rappeler ceci. Lorsqu'un signal, disons $A$, passe à travers {logicref}`and0_tryout.{and0,link0}|une porte logique **ET** dont la seconde entrée vaut 0` (ici affichée sans qu'on puisse la changer en cliquant dessus), la sortie de cette porte-là sera toujours identique à 0. Cela nous permet ainsi d'_annuler_ le signal $A$ — de le mettre à zéro. De manière similaire, si {logicref}`and0_tryout.link1|cette seconde entrée vaut 1`, le signal $A$ passera tel quel. On peut ainsi voir la porte **ET** comme un annulateur de signal. Vérifiez ceci ici :

```{logic}
:height: 190
:mode: tryout
:ref: and0_tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 40], "id": 0, "name": "A", "val": 0},
    {"pos": [50, 130], "id": 1, "name": "A'", "val": 0},
    {"pos": [130, 150], "id": 2, "val": 1, "ref": "inconst1", "isConstant": true},
    {"pos": [130, 60], "id": 7, "val": 0, "ref": "inconst0", "isConstant": true}
  ],
  "out": [
    {"pos": [270, 50], "id": 8, "name": "A annulé, toujours 0"},
    {"pos": [270, 140], "id": 12, "name": "A' tel quel"}
  ],
  "gates": [
    {"type": "AND", "pos": [200, 50], "ref": "and0", "in": [4, 5], "out": 6},
    {"type": "AND", "pos": [200, 140], "in": [9, 10], "out": 11}
  ],
  "wires": [[0, 4], [7, 5, {"ref": "link0"}], [6, 8], [1, 9], [2, 10, {"ref": "link1"}], [11, 12]]
}
```

Ensuite, lorsqu'un signal, disons $B$ cette fois, passe à travers {logicref}`or0_tryout.{or0,link0}|une porte logique **OU** dont la seconde entrée est annulée et vaut 0`, la sortie de cette porte sera toujours identique à $B$. Vérifiez ceci ici :

```{logic}
:height: 80
:mode: tryout
:ref: or0_tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 1, "name": "B", "val": 0},
    {"pos": [130, 50], "id": 2, "val": 0, "isConstant": true}
  ],
  "out": [{"pos": [270, 40], "id": 12, "name": "B tel quel"}],
  "gates": [{"type": "OR", "pos": [200, 40], "ref": "or0", "in": [9, 10], "out": 11}],
  "wires": [[1, 9], [2, 10, {"ref": "link0"}], [11, 12]]
}
```

La porte **OU** peut ainsi servir à combiner deux signaux, pour autant que l'un soit annulé.

Avec tout ceci, on peut ainsi construire un multiplexeur (un sélecteur de signal). Supposons qu'on ait les deux signaux $A$ et $B$ : nous pouvons construire un circuit qui combine soit $A$ tel quel et $B$ annulé, soit $A$ annulé et $B$ tel quel. Cela nous aidera pour notre projet initial ! Il faut cependant s'assurer que $A$ soit chaque fois annulé quand $B$ passe tel quel, et inversement. Ceci peut se faire en réutilisant l'idée d'une entrée de contrôle $Op$ ainsi. Nous avons ainsi deux cas :

* Lorsque $Op = 0$, on va sélectionner $A$ et annuler $B$. On va donc faire passer $A$ à travers une porte **ET** à laquelle on donne 1 à l'autre entrée, et faire passer $B$ à travers une porte **ET** à laquelle on donne 0 à la seconde entrée.
* Lorsque $Op = 1$, on va faire exactement l'inverse : sélectionner $B$ et annuler $A$. On donnera donc un 0 à la porte **ET** qui filtre $A$, et 1 à la porte **ET** qui filtre $B$.

En relisant ces lignes, on voit que ce qu'on donne à la seconde entrée de la porte qui filtre $B$ est toujours la même chose que $Op$, et que ce qu'on donne à la seconde entrée de la porte qui filtre $A$ est toujours l'inverse de $Op$. On peut donc construire ce circuit avec {logicref}`filter0_tryout.inv|un inverseur` en plus :

```{logic}
:height: 290
:mode: tryout
:ref: filter0_tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 180], "id": 0, "name": "A", "val": 0},
    {"pos": [50, 240], "id": 1, "name": "B", "val": 0},
    {"pos": [130, 50], "orient": "s", "id": 2, "name": "Op", "val": 0}
  ],
  "gates": [
    {"type": "NOT", "pos": [170, 120], "orient": "s", "ref": "inv", "in": 9, "out": 10},
    {"type": "AND", "pos": [230, 170], "in": [11, 12], "out": 13},
    {"type": "AND", "pos": [230, 230], "in": [14, 15], "out": 16}
  ],
  "out": [
    {"pos": [300, 170], "id": 3, "name": "A filtré"},
    {"pos": [300, 230], "id": 4, "name": "B filtré"}
  ],
  "wires": [
    [2, 9],
    [13, 3],
    [16, 4],
    [0, 12],
    [1, 15],
    [10, 11],
    [2, 14, {"via": [[130, 220]]}]
  ]
}
```

Essayez ce circuit. Quand $Op=0$, $B$ filtré sera toujours 0 mais $A$ passera, et inversement.

Pour recombiner ces sorties filtrées, il ne nous reste plus qu'à les connecter par {logicref}`filter1_tryout.or|une porte **OU**` :

```{logic}
:height: 290
:mode: tryout
:ref: filter1_tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 180], "id": 0, "name": "A", "val": 0},
    {"pos": [50, 240], "id": 1, "name": "B", "val": 0},
    {"pos": [130, 50], "orient": "s", "id": 2, "name": "Op", "val": 0}
  ],
  "gates": [
    {"type": "NOT", "pos": [170, 120], "orient": "s", "in": 9, "out": 10},
    {"type": "AND", "pos": [230, 170], "in": [11, 12], "out": 13},
    {"type": "AND", "pos": [230, 230], "in": [14, 15], "out": 16},
    {"type": "OR", "pos": [360, 200], "ref": "or", "in": [5, 6], "out": 7}
  ],
  "out": [{"pos": [430, 200], "id": 8, "name": "Z"}],
  "wires": [
    [2, 9],
    [0, 12],
    [1, 15],
    [10, 11],
    [2, 14, {"via": [[130, 220]]}],
    [13, 5],
    [16, 6],
    [7, 8]
  ]
}
```

Essayez ce circuit pour confirmer qu'il agit comme un sélecteur : lorsque $Op=0$, on aura sur la sortie $Z=A$, et lorsque $Op=1$, on aura $Z=B$. Comparez-le avec le multiplexeur tout seul ci-dessous : est-ce que notre circuit fait bien la même chose ?

```{logic}
:height: 230
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 120], "id": 0, "name": "A", "val": 0},
    {"pos": [50, 180], "id": 1, "name": "B", "val": 0},
    {"pos": [160, 50], "orient": "s", "id": 2, "name": "Op", "val": 0}
  ],
  "out": [{"pos": [260, 150], "id": 8, "name": "Z"}],
  "components": [{"type": "mux-2to1", "pos": [160, 150], "in": [3, 4, 5], "out": 6}],
  "wires": [[0, 3], [1, 4], [2, 5], [6, 8]]
}
```

Ceci nous permet de compléter le circuit lacunaire de début de chapitre pour sélectionner avec le même mécanisme soit {logicref}`and_or_full.or|le **OU**` soit {logicref}`and_or_full.and|le **ET**` de nos deux entrées $X$ et $Y$. On ajoute {logicref}`and_or_full.{muxinv,muxand0,muxand1,muxor}|les portes de notre sélecteur` en connectant à l'entrée $A$ {logicref}`and_or_full.muxin0|le signal représentant $X$ **OU** $Y$`, et à l'entrée $B$ {logicref}`and_or_full.muxin1|le signal représentant $X$ **ET** $Y$` :

```{logic}
:height: 300
:mode: tryout
:ref: and_or_full

{
  "v": 3,
  "labels": [
    {"type": "rect", "pos": [360, 180], "w": 280, "h": 200, "color": "yellow", "strokeWidth": 2, "caption": "Sélecteur", "captionPos": "ne"}
  ],
  "in": [
    {"pos": [230, 40], "orient": "s", "id": 2, "name": "Op", "val": 0},
    {"pos": [50, 180], "id": 19, "name": "X", "val": 0},
    {"pos": [50, 260], "id": 20, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [530, 210], "id": 8, "name": "Z"}],
  "gates": [
    {"type": "NOT", "pos": [270, 130], "orient": "s", "ref": "muxinv", "in": 9, "out": 10},
    {"type": "AND", "pos": [330, 180], "ref": "muxand0", "in": [11, 12], "out": 13},
    {"type": "AND", "pos": [330, 240], "ref": "muxand1", "in": [14, 15], "out": 16},
    {"type": "OR", "pos": [460, 210], "ref": "muxor", "in": [5, 6], "out": 7},
    {"type": "OR", "pos": [170, 190], "ref": "or", "in": [0, 1], "out": 3},
    {"type": "AND", "pos": [170, 250], "ref": "and", "in": [4, 17], "out": 18}
  ],
  "wires": [
    [2, 9, {"via": [[230, 90]]}],
    [10, 11],
    [2, 14, {"via": [[230, 230]]}],
    [13, 5],
    [16, 6],
    [7, 8],
    [3, 12, {"ref": "muxin0"}],
    [18, 15, {"ref": "muxin1"}],
    [19, 0],
    [19, 4],
    [20, 17],
    [20, 1]
  ]
}
```

````{exercise} Test du sélecteur **OU**/**ET**

Testez le circuit ci-dessus. Établissez la table de vérité de $Z$ en fonction de $X$, $Y$ et $Op$. À l'aide de la table de vérité, montrez que, lorsque $Op=0$, $Z$ représente bien $X$ **OU** $Y$, et que, lorsque $Op=1$, $Z$ représente bien $X$ **ET** $Y$.
````

Nous avons ici construit un circuit qui, grâce à un bit de contrôle $Op$, sélectionne une opération ou une autre à appliquer à ses deux bits d'entrées $X$ et $Y$.

`````{exercise} Construction d'un sélecteur

En réutilisant les principes appliqués ci-dessus, construisez un circuit à deux bits d'entrées $X$ et $Y$ et un bit de contrôle $Op$ qui donnera sur sa sortie $Z$ :

 * Le **OU** exclusif de $X$ et $Y$, lorsque $Op=0$ ;
 * L'inverse du bit $Y$, lorsque $Op=1$.

```{logic}
:height: 400
:showonly: AND OR NOT XOR

{
  "v": 3,
  "in": [
    {"pos": [230, 50], "orient": "s", "id": 2, "name": "Op", "val": 0},
    {"pos": [50, 170], "id": 19, "name": "X", "val": 0},
    {"pos": [50, 250], "id": 20, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [530, 200], "id": 8, "name": "Z"}]
}
```

````{dropdown} Corrigé
Voici un circuit qui réutilise le sélecteur de signal et qui fournit à ce sélecteur les deux nouvelles entrées décrites, à savoir, en haut, le **OU** exclusif de $X$ et $Y$ tel que fourni par une porte **OU-X**, et en bas, $Y$ une fois inversé par une porte **NON** :

```{logic}
:height: 300
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [230, 50], "orient": "s", "id": 2, "name": "Op", "val": 0},
    {"pos": [50, 170], "id": 19, "name": "X", "val": 0},
    {"pos": [50, 250], "id": 20, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [530, 200], "id": 8, "name": "Z"}],
  "gates": [
    {"type": "NOT", "pos": [270, 120], "orient": "s", "in": 9, "out": 10},
    {"type": "AND", "pos": [330, 170], "in": [11, 12], "out": 13},
    {"type": "AND", "pos": [330, 230], "in": [14, 15], "out": 16},
    {"type": "OR", "pos": [460, 200], "in": [5, 6], "out": 7},
    {"type": "XOR", "pos": [170, 180], "in": [0, 1], "out": 3},
    {"type": "NOT", "pos": [170, 250], "in": 21, "out": 22}
  ],
  "wires": [
    [2, 9],
    [10, 11],
    [2, 14, {"via": [[230, 220]]}],
    [13, 5],
    [16, 6],
    [7, 8],
    [3, 12],
    [19, 0],
    [20, 1],
    [20, 21],
    [22, 15]
  ]
}
```
````
`````

`````{exercise} Inverseur conditionnel

En réutilisant les principes appliqués ci-dessus, construisez un circuit à une entrée $X$ avec un bit de contrôle $Op$ qui donnera sur sa sortie $Z$ :

 * $X$ tel quel, lorsque $Op=0$ ;
 * $X$ inversé, lorsque $Op=1$.

Écrivez la table de vérité de ce circuit. Correspond-elle par hasard à une porte déjà connue? Serait-ce dès lors possible de simplifier votre circuit?

```{logic}
:height: 400
:showonly: AND OR NOT XOR

{
  "v": 3,
  "in": [
    {"pos": [230, 50], "orient": "s", "id": 2, "name": "Op", "val": 0},
    {"pos": [50, 170], "id": 19, "name": "X", "val": 0}
  ],
  "out": [{"pos": [530, 200], "id": 8, "name": "Z"}]
}
```


````{dropdown} Corrigé

Voici une proposition qui réutilise le sélecteur de signal et qui fournit à ce sélecteur $X$ en haut et $X$ inversé en bas :

```{logic}
:height: 290
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [150, 50], "orient": "s", "id": 2, "name": "Op", "val": 0},
    {"pos": [50, 180], "id": 19, "name": "X", "val": 0}
  ],
  "out": [{"pos": [450, 200], "id": 8, "name": "Z"}],
  "gates": [
    {"type": "NOT", "pos": [190, 120], "orient": "s", "in": 9, "out": 10},
    {"type": "AND", "pos": [250, 170], "in": [11, 12], "out": 13},
    {"type": "AND", "pos": [250, 230], "in": [14, 15], "out": 16},
    {"type": "OR", "pos": [380, 200], "in": [5, 6], "out": 7},
    {"type": "NOT", "pos": [120, 240], "in": 23, "out": 24}
  ],
  "wires": [
    [2, 9],
    [10, 11],
    [2, 14, {"via": [[150, 220]]}],
    [13, 5],
    [16, 6],
    [7, 8],
    [19, 12],
    [19, 23],
    [24, 15]
  ]
}
```

La table de vérité est identique à celle d'une porte **OU-X**. On peut donc simplement remplacer tout le circuit par cette unique porte :

```{logic}
:height: 180
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [100, 50], "orient": "s", "id": 2, "name": "Op", "val": 0},
    {"pos": [50, 130], "id": 19, "name": "X", "val": 0}
  ],
  "out": [{"pos": [210, 120], "id": 8, "name": "Z"}],
  "gates": [{"type": "XOR", "pos": [140, 120], "in": [25, 26], "out": 27}],
  "wires": [[19, 26], [2, 25], [27, 8]]
}
```
````
`````

## Une ALU à 4 bits

Une unité arithmétique et logique, ou ALU, est un circuit qui ressemble dans ses principes de base à ce que nous venons de faire. L'ALU réalise plusieurs opérations et permet de sélectionner, via un ou plusieurs bits de contrôle, l'opération qui est réalisée. Les opérations proposées sont, comme le nom de l'ALU indique, des opérations arithmétiques (typiquement, l'addition et la soustraction) et des opérations logiques (par exemple, un **ET** et un **OU** logiques).

Nous présentons ici une ALU simple à 4 bits :

```{logic}
:height: 240
:mode: static

{
  "v": 3,
  "opts": {"showDisconnectedPins": true},
  "components": [
    {
      "type": "alu",
      "pos": [70, 120],
      "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 16],
      "out": [10, 11, 12, 13, 14, {"id": 15, "force": 0}],
      "showOp": false
    }
  ]
}
```

Cette ALU sait effectuer l'addition ou la soustraction de deux nombres entiers représentés sur 4 bits. Elle a ainsi 8 bits d'entrée pour les données et 4 bits de sorties, à gauche et à droite. En plus de l'addition et de la soustraction, elle sait aussi faire les opérations logiques **ET** et **OU** — en tout donc, quatre opérations. Pour sélectionner l'une des quatre opérations, on ne peut plus se contenter d'un seul bit de contrôle, mais nous allons en utiliser deux pour avoir quatre combinaisons possibles. Ce sont les deux entrées supérieures gauches de l'ALU (on ignore ici l'entrée $C_{in}$).

La convention utilisée pour la sélection de l'opération est la suivante :

| $Op$ | Opération effectuée |
| :--: | :-----------------: |
|  00  |       Addition      |
|  01  |     Soustraction    |
|  10  |        **OU**       |
|  11  |        **ET**       |

`````{exercise} Test de l'ALU

Connectez cette ALU à 8 entrées et à 4 sorties de manière à lui faire effectuer l'opération $7 + 2 = 9$. Connectez les 4 bits des entrées et de la sortie à des afficheurs de demi-octet pour vérifier leur fonctionnement. Connectez ensuite une entrée pour le bit de contrôle qui permettra d'effectuer la soustraction avec les mêmes données d'entrée, donc $7 - 2 = 5$.

```{logic}
:height: 400
:showonly: in in.nibble out out.nibble display

{
  "v": 3,
  "components": [
    {
      "type": "alu", "pos": [300, 200],
      "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 16], "out": [10, 11, 12, 13, 14, 15]
    }
  ]
}
```

````{dropdown} Corrigé
```{logic}
:height: 400
:mode: tryout

{
  "v": 3,
  "components": [
    {
      "type": "alu",
      "pos": [300, 200],
      "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 37],
      "out": [10, 11, 12, 13, 14, 15]
    }
  ],
  "in": [
    {"pos": [50, 70], "id": 16, "val": 1},
    {"pos": [50, 100], "id": 17, "val": 1},
    {"pos": [50, 130], "id": 18, "val": 1},
    {"pos": [50, 160], "id": 19, "val": 0},
    {"pos": [50, 250], "id": 24, "val": 0},
    {"pos": [50, 280], "id": 25, "val": 1},
    {"pos": [50, 310], "id": 26, "val": 0},
    {"pos": [50, 340], "id": 27, "val": 0},
    {"pos": [360, 60], "orient": "w", "id": 36, "name": "Add./Soustr.", "val": 0}
  ],
  "out": [
    {"type": "nibble", "pos": [220, 50], "id": [20, 21, 22, 23], "name": "A"},
    {"type": "nibble", "pos": [220, 350], "id": [28, 29, 30, 31], "name": "B"},
    {"type": "nibble", "pos": [400, 200], "id": [32, 33, 34, 35], "name": "S"}
  ],
  "wires": [
    [16, 20],
    [17, 21],
    [18, 22],
    [19, 23],
    [16, 0],
    [17, 1],
    [18, 2],
    [19, 3],
    [24, 4],
    [25, 5],
    [26, 6],
    [27, 7],
    [24, 28],
    [25, 29],
    [26, 30],
    [27, 31],
    [10, 32],
    [11, 33],
    [12, 34],
    [13, 35],
    [36, 8]
  ]
}
```
````
`````

L'ALU a trois sorties en plus, en bas du composant :

 * la sortie $C_{out}$ (pour _carry out_) vaut 1 lors d'un dépassement de capacité (si le résultat de l'opération arithmétique représenté sur la sortie n'est pas valable parce qu'il vaudrait davantage de bits pour le représenter ; par exemple, le résultat de $8 + 8 = 16$ n'est pas représentable sur 4 bits, qui suffisent à représenter les valeurs entières jusqu'à 15 seulement) ;
 * la sortie $V$ (pour _oVerflow_) vaut 1 lors d'un dépassement de capacité si on considère les entrées et les sorties comme des nombres signés. Nous ne faisons pas cela ici et ignorons cette sortie ;
 * finalement, la sortie $Z$ (pour _Zero_) vaut 1 lorsque tous les bits de sortie valent 0.


`````{exercise} Une ALU comme comparateur

En programmation, c'est fréquent de tester, par exemple dans une condition avec un `if`, si deux valeurs sont égales. Par exemple, ce fragment de code affichera « Ces valeurs sont égales! » uniquement si les deux nombres entiers donnés lors de l'exécution du code sont les mêmes:

```{codeplay}
A = int(input("Quel est le premier nombre? "))
B = int(input("Quel est le second nombre? "))
if A == B:
    print("Ces valeurs sont égales!")
```

Ce qui nous intéresse spécialement, c'est la comparaison à la ligne 3. Cette comparaison peut être réalisée avec une ALU. Pour cet exercice, créez un circuit avec une ALU qui compare deux nombres de quatre bits et indique sur la sortie $Z$ un 1 si les deux nombres sont égaux et un 0 s'ils sont différents.

```{logic}
:height: 330
:showonly: ALU in in.nibble out out.nibble NOT OR OR4 AND XOR

{
  "v": 5,
  "in": [
    {"bits": 4, "pos": [60, 90], "id": "0-3"},
    {"bits": 4, "pos": [60, 240], "id": "4-7"}
  ],
  "out": [
    {"pos": [410, 160], "id": 37, "name": "Z"}
  ]
}
```

````{dropdown} Indice
Deux nombres $A$ et $B$ sont égaux si leur différence est nulle — donc si tous les bits de sortie de la soustraction $A - B$ valent 0.
````

````{dropdown} Corrigé avec ALU — approche arithmétique
On connecte les 8 entrées, on règle l'opération de l'ALU sur soustraction et on utilise la sortie de l'ALU qui indique si tous les bits de sortie sont à zéro. En effet, cela ne se produit que lorsque la différence entre les deux nombres d'entrée est 0 — c'est-à-dire, s'ils sont égaux. On constate qu'on peut ignorer les 4 bits de sorties ici !

```{logic}
:mode: tryout
:height: 330
:ref: 4bit_diff_alu

{
  "v": 5,
  "in": [
    {"bits": 4, "pos": [60, 90], "id": "0-3"},
    {"bits": 4, "pos": [60, 240], "id": "4-7"},
    {"pos": [230, 30], "orient": "s", "id": 26, "val": 1}
  ],
  "out": [
    {"pos": [410, 160], "id": 37, "name": "Z"}
  ],
  "ic": [
    {"type": "alu", "pos": [210, 160], "in": "8-18", "out": "19-25"}
  ],
  "wires": [[0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15], [24, 37], [26, 16]]
}
```
````

Plus difficile : essayez de réaliser un circuit qui calcule la même valeur de sortie, mais sans utiliser d'ALU.

````{dropdown} Indice
Une porte **OU-X** peut être vue comme un comparateur de deux bits : sa sortie vaudra 1 si et seulement si ses deux entrées sont différentes.
````

````{dropdown} Corrigé sans ALU — approche logique
Cette solution utilise des portes **OU-X** comme comparateurs. On voit ici que 4 portes **OU-X** comparent deux à deux les 8 bits d'entrée. Leurs sorties sont ensuite combinées avec des portes **OU**, afin d'obtenir un signal qui vaudra 1 si au moins une différence est détectée, donc si les deux nombres d'entrées ne sont pas égaux. Il ne reste plus qu'à inverser ce signal pour obtenir la sortie demandée qui, selon la donnée, doit valoir 1 lorsque les nombres sont égaux.

```{logic}
:height: 330
:mode: tryout
:ref: 4bit_diff_logic0

{
  "v": 5,
  "in": [
    {"bits": 4, "pos": [60, 90], "id": "0-3"},
    {"bits": 4, "pos": [60, 240], "id": "4-7"}
  ],
  "out": [
    {"pos": [515, 160], "id": 37, "name": "Z"}
  ],
  "gates": [
    {"type": "XOR", "pos": [185, 70], "in": [27, 28], "out": 29},
    {"type": "XOR", "pos": [185, 130], "in": [30, 31], "out": 32},
    {"type": "XOR", "pos": [185, 195], "in": [33, 34], "out": 35},
    {"type": "XOR", "pos": [180, 260], "in": [36, 38], "out": 39},
    {"type": "OR", "pos": [280, 120], "ref": "or1", "in": [40, 41], "out": 42},
    {"type": "OR", "pos": [280, 205], "ref": "or2", "in": [43, 44], "out": 45},
    {"type": "OR", "pos": [380, 160], "ref": "or3", "in": [46, 47], "out": 48},
    {"type": "NOT", "pos": [445, 160], "in": 49, "out": 50}
  ],
  "wires": [[0, 27], [4, 28], [3, 36], [7, 38], [6, 34], [2, 33], [5, 31], [1, 30], [29, 40], [32, 41], [35, 43], [39, 44], [42, 46], [45, 47], [48, 49], [50, 37]]
}
```

Alernativement, à la place d'utiliser {logicref}`4bit_diff_logic0.{or1,or2,or3}|trois portes **OU**` dans le schéma ci-dessus, on aurait pu utiliser {logicref}`4bit_diff_logic1.{bigor}|une grande porte **OU** à quatre entrées` :

```{logic}
:height: 330
:mode: tryout
:ref: 4bit_diff_logic1

{
  "v": 5,
  "in": [
    {"bits": 4, "pos": [60, 90], "id": "0-3"},
    {"bits": 4, "pos": [60, 240], "id": "4-7"}
  ],
  "out": [
    {"pos": [485, 160], "id": 37, "name": "Z"}
  ],
  "gates": [
    {"type": "XOR", "pos": [185, 70], "in": [27, 28], "out": 29},
    {"type": "XOR", "pos": [185, 130], "in": [30, 31], "out": 32},
    {"type": "XOR", "pos": [185, 195], "in": [33, 34], "out": 35},
    {"type": "XOR", "pos": [180, 260], "in": [36, 38], "out": 39},
    {"type": "NOT", "pos": [415, 160], "in": 49, "out": 50},
    {"type": "OR", "bits": 4, "pos": [320, 160], "ref": "bigor", "in": "54-57", "out": 58}
  ],
  "wires": [[0, 27], [4, 28], [3, 36], [7, 38], [6, 34], [2, 33], [5, 31], [1, 30], [50, 37], [29, 54], [32, 55], [35, 56], [39, 57], [58, 49]]
}
```

````
`````

En résumé, nous avons appris ici ce qu'est une unité arithmétique et logique et avons examiné de plus près comment construire un multiplexeur, un circuit qui est à même de « choisir » parmi plusieurs signaux d'entrées lequel il va propager sur sa sortie. L'ALU est spécialement intéressante, car c'est le premier composant que nous rencontrons qui incarne une des propriétés de base d'un ordinateur, à savoir d'être programmable, en faisant en sorte que l'opération qu'elle effectue dépende d'un signal externe.

````{togofurther}

Notre petite ALU peut aussi faire des calculs en utilisant une représentation signée des nombres entiers. Sur 4 bits, une représentation en complément à deux peut représenter les nombres de $-8$ à $+7$. Il est possible d'utiliser les mêmes afficheurs de demi-octets en mode signé pour effectuer des opérations arithmétiques avec des valeurs négatives, par exemple, ici, $-2 - (-4) = 2$ :

```{logic}
:height: 400
:mode: tryout

{
  "v": 5,
  "in": [
    {"pos": [370, 60], "orient": "w", "id": 36, "name": {"0": "Addition", "1": "Soustraction"}, "val": 1},
    {"bits": 4, "pos": [60, 130], "id": "40-43", "val": "1110"},
    {"bits": 4, "pos": [60, 280], "id": "48-51", "val": "1100"}
  ],
  "out": [
    {"type": "display", "pos": [220, 50], "id": "20-23", "name": "A", "radix": -10},
    {"type": "display", "pos": [220, 350], "id": "28-31", "name": "B", "radix": -10},
    {"type": "display", "pos": [400, 200], "id": "32-35", "name": "S", "radix": -10},
    {"pos": [370, 350], "id": 39, "name": {"0": "0 – Résultat correct", "1": "1 – Dépassement"}}
  ],
  "ic": [
    {"type": "alu", "pos": [300, 200], "in": ["0-9", 37], "out": ["10-13", 38, 15, 14]}
  ],
  "wires": [[10, 32], [40, 20], [41, 21], [42, 22], [43, 23], [40, 0], [41, 1], [42, 2], [43, 3], [48, 4], [49, 5], [50, 6], [51, 7], [48, 28], [49, 29], [50, 30], [51, 31], [36, 8], [38, 39], [11, 33], [12, 34], [13, 35]]
}
```

Notez que grâce à la représentation en complément à deux, la circuiterie interne de l'ALU peut se permettre de complètement ignorer si ses entrées sont signées ou pas et livrera le bon résultat tant que la convention d'entrée et de sortie reste la même.

Attention, lorsqu'on interprète les entrées et la sortie comme des nombres signés, ce n'est plus la sortie $C_{out}$ de l'ALU qui indique un dépassement de capacité, mais la sortie $V$, qui est calculée différemment.

Essayez de régler les entrées pour que cette ALU calcule le résultat de $-8 - 4$. Vérifiez qu'un dépassement de capacité est signalé et expliquez pourquoi.
````
