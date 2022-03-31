
# 3. ALU et mémoire

Dans cette section, nous continuons notre exploration de comment les portes logiques, selon leur assemblage, fournissent les fonctionnalités de base des ordinateurs. En particulier, nous nous intéressons à comment faire effectuer plusieurs opérations à un ordinateur via ce qui s'appelle une unité arithmétique et logique, puis nous voyons comment l'ordinateur se rappelle les résultats des calculs intermédiaires via des bascules.


## 3.1. Unité arithmétique et logique

Dans la section précédente, nous avons vu comment créer, via un assemblage de portes logiques, un circuit qui réalise l'addition de deux nombres de 4 bits. Ce circuit était fixe : avec les deux nombres d'entrées, il réalisait toujours une addition et ne servait ainsi qu'à ça.

Les ordinateurs ont la propriété d'être programmables : ils savent effectuer plusieurs opérations, et c'est la manière dont ils sont programmés qui va déterminer l'opération qu'ils effectuent. C'est aussi vrai pour des machines plus simples ; une calculatrice de poche, par exemple, pourra effectuer au moins les quatre opérations de base : addition, soustraction, multiplication et division.

Le composant qui nous permettra de sélectionner une opération ou une autre s'appelle « unité arithmétique et logique », communément appelé simplement « ALU » (de l'anglais _arithmetic logic unit_). Avant d'inspecter une ALU, nous avons besoin de comprendre comment on peut sélectionner une opération ou une autre avec des circuits logiques.


### Sélection de l'opération

Comment créer un circuit qui permet de sélectionner une opération à faire, et comment indiquer l'opération à sélectionner ? Essayons d'abord de créer un circuit à deux entrées qui va calculer soit le **OU** soit le **ET** de ces deux entrées.

Nous savons faire un circuit simple qui calcule le **OU** de deux entrées $X$ et $Y$, avec une seule porte logique :

```{logic}
:height: 140
:mode: tryout

{
  "v": 1,
  "in": [
    {"pos": [50, 30], "id": 0, "name": "X", "val": 0},
    {"pos": [50, 110], "id": 1, "name": "Y", "val": 0}
  ],
  "gates": [{"type": "OR", "pos": [180, 40], "in": [6, 7], "out": 8}],
  "out": [{"pos": [250, 40], "id": 2, "name": "X OU Y"}],
  "wires": [[0, 6], [1, 7], [8, 2]]
}
```

Nous pouvons sans autre y ajouter une porte **ET** pour calculer une autre sortie en parallèle, à partir des mêmes entrées $X$ et $Y$ :

```{logic}
:height: 140
:mode: tryout

{
  "v": 1,
  "in": [
    {"pos": [50, 30], "id": 0, "name": "X", "val": 0},
    {"pos": [50, 110], "id": 1, "name": "Y", "val": 0}
  ],
  "gates": [
    {"type": "OR", "pos": [180, 40], "in": [6, 7], "out": 8},
    {"type": "AND", "pos": [180, 100], "in": [3, 4], "out": 5}
  ],
  "out": [
    {"pos": [250, 40], "id": 2, "name": "X OU Y"},
    {"pos": [250, 100], "id": 9, "name": "X ET Y"}
  ],
  "wires": [[0, 6], [1, 7], [8, 2], [0, 3], [1, 4], [5, 9]]
}
```

L'idée est maintenant de combiner ces sorties intermédiaires pour n'en avoir plus qu'une, qui sera soit le **OU**, soit le **ET**. Mais comment faire pour indiquer si l'on désire le **OU** ou le **ET** ? Nous pouvons rajouter une entrée pour choisir cette opération. Appelons-la $Op$, pour « opération ». Choisissons une convention : lorsque $Op$ vaut 0, nous souhaitons effectuer l'opération **OU**, et lorsque $Op$ vaut 1, nous souhaitons effectuer l'opération **ET**. Conceptuellement, il nous faut donc compléter ce schéma pour calculer notre sortie finale $Z$ en fonction de $Op$ :

```{logic}
:height: 300
:mode: tryout

{
  "v": 1,
  "opts": {"showDisconnectedPins": true},
  "in": [
    {"pos": [50, 170], "id": 0, "name": "X", "val": 0},
    {"pos": [50, 250], "id": 1, "name": "Y", "val": 0},
    {"pos": [260, 50], "orient": "s", "id": 2, "name": "Op", "val": 0}
  ],
  "out": [
    {"pos": [440, 200], "id": 20, "name": "Z"},
    {"pos": [250, 240], "id": 21, "name": "X ET Y"},
    {"pos": [250, 180], "id": 23, "name": "X OU Y"}
  ],
  "gates": [
    {"type": "AND", "pos": [180, 240], "in": [3, 4], "out": 5},
    {"type": "OR", "pos": [180, 180], "in": [6, 7], "out": 8}
  ],
  "wires": [[0, 3], [1, 4], [0, 6], [1, 7], [5, 21], [8, 23]]
}
```

Pour la suite, nous avons besoin de nous rappeler ceci. Lorsqu'un signal, disons $A$, passe à travers une porte logique **ET** dont la seconde entrée vaut 0, la sortie de cette porte-là sera toujours identique à 0. Cela nous permet ainsi d'annuler le signal $A$. De manière similaire, si cette seconde entrée vaut 1, le signal $A$ passera tel quel. On peut ainsi voir la porte **ET** comme un annulateur de signal. Vérifiez ceci ici :

<!-- TODO the aux inputs constant once we can in the simulator and remove their names -->

```{logic}
:height: 190
:mode: tryout

{
  "v": 1,
  "in": [
    {"pos": [50, 40], "id": 0, "name": "A", "val": 0},
    {"pos": [50, 130], "id": 1, "name": "A'", "val": 0},
    {"pos": [130, 150], "id": 2, "name": "1", "val": 1},
    {"pos": [130, 60], "id": 7, "name": "0", "val": 0}
  ],
  "out": [
    {"pos": [270, 50], "id": 8, "name": "A annulé"},
    {"pos": [270, 140], "id": 12, "name": "A' tel quel"}
  ],
  "gates": [
    {"type": "AND", "pos": [200, 50], "in": [4, 5], "out": 6},
    {"type": "AND", "pos": [200, 140], "in": [9, 10], "out": 11}
  ],
  "wires": [[0, 4], [7, 5], [6, 8], [1, 9], [2, 10], [11, 12]]
}
```

Ensuite, lorsqu'un signal, disons $B$ cette fois, passe à travers une porte logique **OU** dont la seconde entrée est annulée et vaut 0, la sortie de cette porte sera toujours identique à $B$. Vérifiez ceci ici :

```{logic}
:height: 80
:mode: tryout

{
  "v": 1,
  "in": [
    {"pos": [50, 30], "id": 1, "name": "B", "val": 0},
    {"pos": [130, 50], "id": 2, "name": "0", "val": 0}
  ],
  "out": [{"pos": [270, 40], "id": 12, "name": "B tel quel"}],
  "gates": [{"type": "OR", "pos": [200, 40], "in": [9, 10], "out": 11}],
  "wires": [[1, 9], [2, 10], [11, 12]]
}
```

La porte **OU** peut ainsi servir à combiner deux signaux, pour autant que l'un soit annulé.

Avec tout ceci, on peut ainsi construire un sélecteur de signal. Supposons qu'on ait les deux signaux $A$ et $B$ : nous pouvons construire un circuit qui combine soit $A$ tel quel et $B$ annulé, soit $A$ annulé et $B$ tel quel. Cela nous aidera pour notre projet initial ! Il faut cependant s'assurer que $A$ soit chaque fois annulé quand $B$ passe tel quel, et inversement. Ceci peut se faire en réutilisant l'idée d'une entrée de contrôle $Op$ ainsi. Nous avons ainsi deux cas :

 * Lorsque $Op = 0$, on va sélectionner $A$ et annuler $B$. On va donc faire passer $A$ à travers une porte **ET** à laquelle on donne 1 à l'autre entrée, et faire passer $B$ à travers une porte **ET** à laquelle on donne 0 à la seconde entrée.
 * Lorsque $Op = 1$, on va faire exactement l'inverse: sélectionner $B$ et annuler $A$. On donnera donc un 0 à la porte **ET** qui filtre $A$, et $1$ à la porte **ET** qui filtre $B$.

En relisant ces lignes, on voit que ce qu'on donne à la seconde entrée de la porte qui filtre $B$ est toujours la même chose que $Op$, et que ce qu'on donne à la seconde entrée de la porte qui filtre $A$ est toujours l'inverse de $Op$. On peut donc construire ce circuit avec un inverseur en plus :

```{logic}
:height: 290
:mode: tryout

{
  "v": 1,
  "in": [
    {"pos": [50, 180], "id": 0, "name": "A", "val": 0},
    {"pos": [50, 240], "id": 1, "name": "B", "val": 0},
    {"pos": [130, 50], "orient": "s", "id": 2, "name": "Op", "val": 0}
  ],
  "gates": [
    {"type": "NOT", "pos": [170, 120], "orient": "s", "in": 9, "out": 10},
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
    [2, 14, {"waypoints": [[130, 220]]}]
  ]
}
```

Essayez ce circuit. Quand $Op=0$, $B$ filtré sera toujours 0 mais $A$ passera, et inversement.

Pour recombiner ces sorties filtrées, il ne nous reste plus qu'à les connecter par une porte **OU** :

```{logic}
:height: 290
:mode: tryout

{
  "v": 1,
  "in": [
    {"pos": [50, 180], "id": 0, "name": "A", "val": 0},
    {"pos": [50, 240], "id": 1, "name": "B", "val": 0},
    {"pos": [130, 50], "orient": "s", "id": 2, "name": "Op", "val": 0}
  ],
  "gates": [
    {"type": "NOT", "pos": [170, 120], "orient": "s", "in": 9, "out": 10},
    {"type": "AND", "pos": [230, 170], "in": [11, 12], "out": 13},
    {"type": "AND", "pos": [230, 230], "in": [14, 15], "out": 16},
    {"type": "OR", "pos": [360, 200], "in": [5, 6], "out": 7}
  ],
  "out": [{"pos": [430, 200], "id": 8, "name": "Z"}],
  "wires": [
    [2, 9],
    [0, 12],
    [1, 15],
    [10, 11],
    [2, 14, {"waypoints": [[130, 220]]}],
    [13, 5],
    [16, 6],
    [7, 8]
  ]
}
```

Essayez ce circuit pour confirmer qu'il agit comme un sélecteur : lorsque $Op=0$, on aura sur la sortie $Z=A$, et lorsque $Op=1$, on aura $Z=B$.

Ceci nous permet de compléter le circuit lacunaire de début de chapitre pour sélectionner avec le même mécanisme soit le **OU** soit le **ET** de nos deux entrées $X$ et $Y$. On ajoute notre sélecteur en connectant à l'entrée $A$ le signal représentant $X$ **OU** $Y$, et à l'entrée $B$ le signal représentant $X$ **ET** $Y$ :

```{logic}
:height: 300
:mode: tryout

{
  "v": 1,
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
    {"type": "OR", "pos": [170, 180], "in": [0, 1], "out": 3},
    {"type": "AND", "pos": [170, 240], "in": [4, 17], "out": 18}
  ],
  "wires": [
    [2, 9],
    [10, 11],
    [2, 14, {"waypoints": [[230, 220]]}],
    [13, 5],
    [16, 6],
    [7, 8],
    [3, 12],
    [18, 15],
    [19, 0],
    [19, 4],
    [20, 17],
    [20, 1]
  ]
}
```

````{admonition} Exercice 1 : test du sélecteur **OU**/**ET**
Testez le circuit ci-dessus. Établissez la table de vérité de $Z$ en fonction de $X$, $Y$ et $Op$. À l'aide de la table de vérité, montrez que, lorsque $Op=0$, $Z$ représente bien $X$ **OU** $Y$, et que, lorsque $Op=1$, $Z$ représente bien $X$ **ET** $Y$.
````

Nous avons ici construit un circuit qui, grâce à un bit de contrôle $Op$, sélectionne une opération ou une autre à appliquer à ses deux bits d'entrées $X$ et $Y$.


`````{admonition} Exercice 2 : construction d'un sélecteur
En réutilisant les principes appliqués ci-dessus, construisez un circuit à deux bits d'entrées $X$ et $Y$ et un bit de contrôle $Op$ qui donnera sur sa sortie $Z$ :

 * Le **OU** exclusif de $X$ et $Y$, lorsque $Op=0$ ;
 * L'inverse du bit $Y$, lorsque $Op=1$.

```{logic}
:height: 400
:showonly: AND OR NOT XOR

{
  "v": 1,
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
  "v": 1,
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
    [2, 14, {"waypoints": [[230, 220]]}],
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


`````{admonition} Exercice 3 : inverseur conditionnel
En réutilisant les principes appliqués ci-dessus, construisez un circuit à une entrée $X$ avec un bit de contrôle $Op$ qui donnera sur sa sortie $Z$ :

 * $X$ tel quel, lorsque $Op=0$ ;
 * $X$ inversé, lorsque $Op=1$.

Écrivez la table de vérité de ce circuit. Correspond-elle par hasard à une porte déjà connue? Serait-ce dès lors possible de simplifier votre circuit?

```{logic}
:height: 400
:showonly: AND OR NOT XOR

{
  "v": 1,
  "in": [
    {"pos": [230, 50], "orient": "s", "id": 2, "name": "Op", "val": 0},
    {"pos": [50, 170], "id": 19, "name": "X", "val": 0},
    {"pos": [50, 250], "id": 20, "name": "Y", "val": 0}
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
  "v": 1,
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
    [2, 14, {"waypoints": [[150, 220]]}],
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
  "v": 1,
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


### Une ALU à 4 bits

Une unité arithmétique et logique, ou ALU, est un circuit qui ressemble dans ses principes de base à ce que nous venons de faire. L'ALU réaliste plusieurs opérations et permet de sélectionner, via un ou plusieurs bits de contrôle, l'opération qui est réalisée. Les opérations proposées sont, comme le nom de l'ALU indique, des opérations arithmétiques (typiquement, l'addition et la soustraction) et des opérations logiques (par exemple, un **ET** et un **OU** logiques).

Nous présentons ici une ALU simple à 4 bits :

```{logic}
:height: 240
:mode: static

{
  "v": 1,
  "opts": {"showDisconnectedPins": true},
  "components": [
    {
      "type": "alu",
      "pos": [70, 120],
      "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      "out": [10, 11, 12, 13, 14, {"id": 15, "force": 0}],
      "showOp": false
    }
  ]
}
```

Cette ALU sait effectuer l'addition ou la soustraction de deux nombres entiers représentés sur 4 bits. Elle a ainsi 8 bits d'entrée pour les données et 4 bits de sorties, à gauche et à droite. En plus de l'addition et de la soustraction, elle sait aussi faire les opérations logiques **ET** et **OU** — en tout donc, quatre opérations. Pour sélectionner l'une des quatre opérations, on ne peut plus se contenter d'un seul bit de contrôle, mais nous allons en utiliser deux pour avoir quatre combinaisons possibles. Ce sont les deux entrées supérieures de l'ALU. La convention utilisée pour la sélection de l'opération est la suivante :

| $Op$ | Opération effectuée |
| :--: | :-----------------: | 
|  00  |       Addition      |
|  01  |     Soustraction    |
|  10  |        **OU**       |
|  11  |        **ET**       |


`````{admonition} Exercice 4 : test de l'ALU
Connectez cette ALU à 8 entrées et à 4 sorties de manière à lui faire effectuer l'opération $7 + 2 = 9$. Connectez les 4 bits des entrées et de la sortie à des afficheurs de demi-octet pour vérifier leur fonctionnement. Connectez ensuite une entrée pour le bit de contrôle qui permettra d'effectuer la soustraction avec les mêmes données d'entrée, donc $7 - 2 = 5$.

```{logic}
:height: 400
:showonly: in in.nibble out out.nibble

{
  "v": 1,
  "components": [
    {
      "type": "alu", "pos": [300, 200],
      "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "out": [10, 11, 12, 13, 14, 15]
    }
  ]
}
```

````{dropdown} Corrigé
```{logic}
:height: 400
:mode: tryout

{
  "v": 1,
  "components": [
    {
      "type": "alu",
      "pos": [300, 200],
      "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
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

L'ALU a deux sorties en plus, en bas du composant :

 * la sortie $V$ (pour _oVerflow_) vaut 1 lors d'un dépassement de capacité (si le résultat de l'opération arithmétique représenté sur la sortie n'est pas valable parce qu'il vaudrait davantage de bits pour le représenter ; par exemple, le résultat de $8 + 8 = 16$ n'est pas représentable sur 4 bits, qui suffisent à représenter les valeurs entières jusqu'à 15 seulement) ;
 * la sortie $Z$ (pour _Zero_) vaut 1 lorsque tous les bits de sortie valent 0.

`````{admonition} Exercice 5 : une ALU comme comparateur
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
:showonly: ALU in out NOT OR AND XOR

{
  "v": 1,
  "in": [
    {"pos": [50, 30], "id": 16, "val": 0},
    {"pos": [50, 60], "id": 17, "val": 0},
    {"pos": [50, 90], "id": 18, "val": 0},
    {"pos": [50, 120], "id": 19, "val": 0},
    {"pos": [50, 210], "id": 24, "val": 0},
    {"pos": [50, 240], "id": 25, "val": 0},
    {"pos": [50, 270], "id": 26, "val": 0},
    {"pos": [50, 300], "id": 27, "val": 0}
  ],
  "out": [{"pos": [410, 160], "id": 37, "name": "Z"}]
}
```

````{dropdown} Indice
Deux nombres $A$ et $B$ sont égaux si leur différence est nulle — donc si tous les bits de sortie de $A - B$ valent 0.
````

````{dropdown} Corrigé avec ALU — approche arithmétique
On connecte les 8 entrées, on règle l'opération de l'ALU sur soustraction et on utilise la sortie de l'ALU qui indique si tous les bits de sortie sont à zéro. En effet, cela ne se produit que lorsque la différence entre les deux nombres d'entrée est 0 — c'est-à-dire, s'ils sont égaux. On constate qu'on peut ignorer les 4 bits de sorties ici !

```{logic}
:mode: tryout
:height: 330

{
  "v": 1,
  "in": [
    {"pos": [50, 30], "id": 16, "val": 0},
    {"pos": [50, 60], "id": 17, "val": 0},
    {"pos": [50, 90], "id": 18, "val": 0},
    {"pos": [50, 120], "id": 19, "val": 0},
    {"pos": [50, 210], "id": 24, "val": 0},
    {"pos": [50, 240], "id": 25, "val": 0},
    {"pos": [50, 270], "id": 26, "val": 0},
    {"pos": [50, 300], "id": 27, "val": 0},
    {"pos": [230, 30], "orient": "s", "id": 54, "val": 1}
  ],
  "out": [{"pos": [410, 160], "id": 37, "name": "Z"}],
  "components": [
    {
      "type": "alu",
      "pos": [220, 150],
      "in": [38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
      "out": [48, 49, 50, 51, 52, 53]
    }
  ],
  "wires": [
    [16, 38],
    [17, 39],
    [18, 40],
    [19, 41],
    [24, 42],
    [25, 43],
    [26, 44],
    [27, 45],
    [54, 46],
    [53, 37]
  ]
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

{
  "v": 1,
  "in": [
    {"pos": [50, 30], "id": 16, "val": 0},
    {"pos": [50, 60], "id": 17, "val": 0},
    {"pos": [50, 90], "id": 18, "val": 0},
    {"pos": [50, 120], "id": 19, "val": 0},
    {"pos": [50, 210], "id": 24, "val": 0},
    {"pos": [50, 240], "id": 25, "val": 0},
    {"pos": [50, 270], "id": 26, "val": 0},
    {"pos": [50, 300], "id": 27, "val": 0}
  ],
  "out": [{"pos": [530, 160], "id": 37, "name": "Z"}],
  "gates": [
    {"type": "XOR", "pos": [190, 270], "in": [55, 56], "out": 57},
    {"type": "OR", "pos": [290, 210], "in": [58, 59], "out": 60},
    {"type": "OR", "pos": [290, 110], "in": [61, 62], "out": 63},
    {"type": "OR", "pos": [390, 160], "in": [64, 65], "out": 66},
    {"type": "XOR", "pos": [190, 200], "in": [67, 68], "out": 69},
    {"type": "XOR", "pos": [190, 120], "in": [70, 71], "out": 72},
    {"type": "XOR", "pos": [190, 50], "in": [73, 74], "out": 75},
    {"type": "NOT", "pos": [460, 160], "in": 76, "out": 77}
  ],
  "wires": [
    [16, 73],
    [24, 74],
    [17, 70],
    [25, 71],
    [18, 67],
    [26, 68],
    [19, 55],
    [27, 56],
    [75, 61],
    [72, 62],
    [63, 64],
    [60, 65],
    [69, 58],
    [57, 59],
    [66, 76],
    [77, 37]
  ]
}
```
````
`````


En résumé, nous avons appris ici ce qu'est une unité arithmétique et logique et avons examiné de plus près comment construire un circuit qui est à même de « choisir » parmi plusieurs signaux d'entrées. L'ALU est spécialement intéressante, car c'est le premier composant que nous rencontrons qui incarne une des propriétés de base d'un ordinateur, à savoir d'être programmable, en faisant en sorte que l'opération effectuée ne soit pas préprogrammée mais dépende d'un signal externe.


````{admonition} Pour aller plus loin
:class: attention

Notre petite ALU peut aussi faire des calculs en utilisant une représentation signée des nombres entiers. Sur 4 bits, une représentation en complément à deux peut représenter les nombres de $-8$ à $+7$. Il est possible d'utiliser les mêmes afficheurs de demi-octets en mode signé pour effectuer des opérations arithmétiques avec des valeurs négatives, par exemple, ici, $-2 - (-4) = 2$ :

```{logic}
:height: 400
:mode: tryout

{
  "v": 1,
  "in": [
    {"pos": [50, 70], "id": 16, "val": 0},
    {"pos": [50, 100], "id": 17, "val": 1},
    {"pos": [50, 130], "id": 18, "val": 1},
    {"pos": [50, 160], "id": 19, "val": 1},
    {"pos": [50, 250], "id": 24, "val": 0},
    {"pos": [50, 280], "id": 25, "val": 0},
    {"pos": [50, 310], "id": 26, "val": 1},
    {"pos": [50, 340], "id": 27, "val": 1},
    {"pos": [360, 60], "orient": "w", "id": 36, "name": "Add./Soustr.", "val": 1}
  ],
  "out": [
    {
      "type": "nibble",
      "pos": [220, 50],
      "id": [20, 21, 22, 23],
      "name": "A",
      "radix": -10
    },
    {
      "type": "nibble",
      "pos": [220, 350],
      "id": [28, 29, 30, 31],
      "name": "B",
      "radix": -10
    },
    {
      "type": "nibble",
      "pos": [400, 200],
      "id": [32, 33, 34, 35],
      "name": "S",
      "radix": -10
    }
  ],
  "components": [
    {
      "type": "alu",
      "pos": [300, 200],
      "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      "out": [10, 11, 12, 13, 14, 15]
    }
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

Notez que grâce à la représentation en complément à deux, la circuiterie interne de l'ALU peut se permettre de complètement ignorer si ses entrées sont signées ou pas et livrera le bon résultat tant que la convention d'entrée et de sortie reste la même.
````


## 3.3. Mémoire

Les {glo}`transistor|transistors`, les {glo}`portelogique|portes logiques` et leur représentation en {glo}`tableverite|tables de vérités`, permettent de manipuler des 0 et des 1 au niveau physique.. Tant qu'un courant électrique se déplace dans les {glo}`circuit|circuits`, on est capable de le transformer, de le laisser passer ou de l'arrêter, dans le but d'exprimer des portes « ouvertes » ou des portes « fermées » et donc des nombres binaires. L'ALU va une étape plus loin et permet de choisir une opération à effectuer en fonction de bits de contrôle supplémentaire, et livre le résultat de l'opération arithmétique ou logique choisie.

Mais comment faire pour {glo}`stockage|stocker` cette information ? Comment faire pour que l'on se rappelle le résultat d'une addition effectuée par une ALU afin de pouvoir réutiliser cette valeur plus tard ? C'est là que nous avons besoin de _mémoire_.

Dans les ordinateurs, il y a en fait plusieurs types de {glo}`stockage|mémoires`, qu'on peut classer en deux grandes catégories. La {glo}`memvolatile|mémoire volatile`, et la mémoire non volatile. La mémoire volatile s'efface quand la machine et éteinte. C'est le cas de la RAM (_random-access memory_), par exemple. La {glo}`memnonvolatile|mémoire non volatile`, elle, persiste. C'est le cas d'un disque dur ou d'un SSD (_solid-state drive_). Si un smartphone s'éteint inopinément alors qu'on est en train de retoucher une photo sans avoir validé les modifications, ces retouches disparaissent. Elles étaient stockées sur la mémoire volatile. Par contre, au moment où ces retouches sont sauvegardées, elles s'inscrivent dans la mémoire non volatile.

On peut se demander pourquoi on n'utiliserait pas que de la mémoire non volatile, vu les « risques » posés par la mémoire volatile. La réponse est que la mémoire non volatile va probablement être entre 100 et 100 000 fois moins rapide que la mémoire volatile. On privilégie donc la mémoire volatile comme mémoire de travail rapide d'un ordinateur.

Dans les sections qui suivent, on propose de s'intéresser au cas le plus simple: la construction d'une cellule de mémoire volatile qui sera à même de stocker un bit. Par la suite, nous discuterons de la manière dont ce genre de mémoire est utilisée au cœur des microprocesseurs.


### Le verrou SR

L'idée principale derrière la conception d'un circuit logique qui est capable de stocker un signal est que l'on va utiliser la ou les sorties du circuit en les reconnectant à certaines de ses entrées. Essayons par exemple ce circuit simple avec une seule porte **OU** :

```{logic}
:height: 100
:mode: tryout

{
  "v": 1,
  "in": [{"pos": [50, 30], "id": 4, "name": "X", "val": 0}],
  "gates": [{"type": "OR", "pos": [140, 40], "in": [5, 6], "out": 7}],
  "out": [{"pos": [240, 40], "id": 0, "name": "Z"}],
  "wires": [[4, 5], [7, 6, {"waypoints": [[170, 80, "w"], [110, 80, "w"]]}], [7, 0]]
}
```

Au début, les deux entrées de la porte valent 0, comme sa sortie. Si l'on essaie de faire passer l'entrée $X$ à 1, on voit que la sortie $Z$ passera à 1 elle aussi, comme il s'agit d'une porte **OU**. Mais comme $Z$ est aussi relié à l'autre entrée de la porte, on a maintenant un circuit dont on ne peut plus modifier la sortie : même si $X$ passe de nouveau à 0, l'autre entrée reste à 1 et suffit donc pour que $Z$ vale maintenant 1 indéfiniment. On est obligé de remettre le circuit complètement à zéro (l'équivalent de débrancher la prise de courant et de la rebrancher) pour obtenir à nouveau un 0 sur la sortie $Z$.

Assurément, ce circuit n'est pas très intéressant : il se bloque dans un état sans retour possible. Serait-ce possible de construire un circuit un peu plus élaboré qui permettrait de choisir la valeur de sa sortie et de la conserver ? Ces circuits existent en effet et sont à la base du stockage de l'information dans les microprocesseurs. On appelle ces circuits des {glo}`verrou|verrous`, vu qu'ils « verrouillent » une valeur donnée.

Examinons le circuit ci-dessous : c'est le verrou dit « SR », pour _set/reset_, en anglais. 

```{logic}
:height: 160
:mode: tryout

{
  "v": 1,
  "in": [
    {"pos": [50, 30], "id": 8, "name": "R", "val": 0},
    {"pos": [50, 130], "id": 9, "name": "S", "val": 0}
  ],
  "out": [
    {"pos": [290, 40], "id": 10, "name": "Q"},
    {"pos": [290, 120], "id": 11, "name": "Q'"}
  ],
  "gates": [
    {"type": "OR", "pos": [130, 40], "in": [0, 1], "out": 2},
    {"type": "OR", "pos": [130, 120], "in": [4, 5], "out": 6},
    {"type": "NOT", "pos": [200, 120], "in": 3, "out": 7},
    {"type": "NOT", "pos": [200, 40], "in": 12, "out": 13}
  ],
  "wires": [
    [8, 0],
    [9, 5],
    [6, 3],
    [7, 11],
    [2, 12],
    [13, 10],
    [7, 1, {"waypoints": [[80, 50]]}],
    [13, 4, {"waypoints": [[80, 110]]}]
  ]
}
```

Ce circuit stocke un bit de donnée un 0 ou un 1, qu'on va pouvoir lire via la sortie $Q$ et modifier avec les deux entrées $R$ et $S$. (La seconde sortie $\bar{Q}$ est ici toujours l'inverse de $Q$.)

Dans l'état normal de ce verrou, la sortie $Q$ vaut soit 1, soit 0, et les deux entrées $S$ et $R$ restent à 0. Testez le circuit ci-dessus et observez l'effet de $R$ et $S$. $S$, pour _set_, sert à changer l'état du verrou pour lui faire dorénavant stocker un 1. « Allumer » $S$ cause ainsi $Q$ à passer à 1. Ce qu'il y a d'intéressant, c'est qu'une fois que $Q$ est passé à 1, on peut sans autre « éteindre » le signal $S$ et le faire repasser à 0, et la sortie $Q$, elle, reste à 1 — alors que les deux entrées du circuit $S$ et $R$ sont maintenant à nouveau les mêmes qu'avant, lorsque la sortie $Q$ valait 0.

De manière similaire, l'entrée $R$, pour _reset_, sert à faire passer la valeur stockée par le du verrou à 0, et cet état reste 0 même lorsque $R$ est de nouveau « éteint ».

On essaie en général d'éviter d'avoir un 1 sur $R$ et sur $S$ en même temps, cela place le verrou dans un état où $\bar{Q}$ n'est plus l'inverse de $Q$. Pour cette raison, nous allons plutôt créer le circuit comme suit — les connexions sont exactement les mêmes, mais les entrées $S$ et $R$ ne restent pas à 1 lorsqu'on clique dessus, elles retombent à 0 dès que le clic se termine.

```{logic}
:height: 160
:mode: tryout

{
  "v": 1,
  "in": [
    {"pos": [50, 30], "id": 8, "name": "R", "val": 0, "isPushButton": true},
    {"pos": [50, 130], "id": 9, "name": "S", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [290, 40], "id": 10, "name": "Q"},
    {"pos": [290, 120], "id": 11, "name": "Q'"}
  ],
  "gates": [
    {"type": "OR", "pos": [130, 40], "in": [0, 1], "out": 2},
    {"type": "OR", "pos": [130, 120], "in": [4, 5], "out": 6},
    {"type": "NOT", "pos": [200, 120], "in": 3, "out": 7},
    {"type": "NOT", "pos": [200, 40], "in": 12, "out": 13}
  ],
  "wires": [
    [8, 0],
    [9, 5],
    [6, 3],
    [7, 11],
    [2, 12],
    [13, 10],
    [7, 1, {"waypoints": [[80, 50]]}],
    [13, 4, {"waypoints": [[80, 110]]}]
  ]
}
```

Ces verrous sont communs, et pour le reste du chapitre, on simplifiera la notation pour les représenter ainsi, sans changement de fonctionnalité, mais en faisant abstraction des détails internes :

```{logic}
:height: 100
:mode: tryout

{
  "v": 1,
  "in": [
    {"pos": [50, 30], "id": 10, "name": "R", "val": 0, "isPushButton": true},
    {"pos": [50, 70], "id": 11, "name": "S", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [210, 30], "id": 12, "name": "Q"},
    {"pos": [210, 70], "id": 13, "name": "Q'"}
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


### La bascule D

Un souci avec le verrou SR est qu'on a rarement un signal d'entrée qui soit facilement exploitable pour être « converti » en cette logique _set/reset_. La plupart du temps, on a simplement un signal donné, disons $D$, pour « donnée » (ou _data_ en anglais), et c'est ce signal-ci qu'on aimerait stocker. Avec ce système, il serait impossible de connecter $D$ à ce verrou ; on ne peut le brancher directement ni à l'entrée $S$, ni à l'entrée $R$.

On va utiliser pour cela un circuit similaire, mais qui fonctionne un peu différemment, qui s'appelle une **bascule D**[^flipflop] :

[^flipflop]: Il y a une différence conceptuelle fondamentale entre les verrous et les bascules : les verrous sont des composants dits _asynchrones_, dont l'état peut changer dès qu'une des entrées change, alors que les bascules sont des composants dits _synchrones_, qui ont une entrée appelée Horloge, et dont l'état ne changera qu'au moment où le signal d'horloge effectuera une transition (dans notre cas, passera de 0 à 1). Une discussion plus poussée de ces différences dépasse le cadre de ce cours.

```{logic}
:height: 120
:mode: tryout

{
  "v": 1,
  "in": [
    {"pos": [90, 40], "id": 0, "name": "D", "val": 0},
    {"pos": [90, 80], "id": 1, "name": "Horloge", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [250, 40], "id": 9, "name": "Q"},
    {"pos": [250, 80], "id": 10, "name": "Q'"}
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

Cette bascule va stocker son entrée $D$ et la propager sur sa sortie $Q$ uniquement lorsque l'entrée spéciale $Horloge$ passe de 0 à 1. Le reste du temps, $Q$ et $\overline{Q}$ garderont leur valeur précédente. Notez que cette bascule a aussi deux entrées $S$ et $R$, qui servent à forcer l'état interne à valoir 1 ou 0, respectivement, indépendamment du signal $D$ et de l'horloge.

Testez cette bascule. Réglez l'entrée de données $D$ à 1 ou 0 et observez comme la bascule ne réagit pas : sa sortie $Q$ reste telle quelle. Donnez ensuite une impulsion en cliquant sur l'entrée $Horloge$ et voyez comme la valeur de $D$ est maintenant stockée sur la bascule.

````{dropdown} Pour aller plus loin
Pour aller plus loin, une vidéo de résumé qui parle aussi des bascules et des registres :

```{youtube} I0-izyq6q5s
```
````


`````{admonition} Exercice 6 : stocker deux bits
Créez un circuit qui calcule, d'une part, le **OU** de deux entrées $X$ et $Y$, et, d'autre part, le **ET** de ces deux mêmes entrées. À l'aide de bascules D, complétez le circuit de manière à ce qu'il stocke ces deux valeurs calculées lors d'un coup d'horloge et les sorte sur les sorties $P$ et $Q$, respectivement. Faites finalement en sorte que le signal $Reset$, si activé, réinitialise les bascules à 0. Vérifiez qu'une fois les valeurs stockées par les bascules, des changements sur les entrées $X$ et $Y$ n'aient pas d'effet direct sur $P$ et $Q$.

```{logic}
:height: 400
:showonly: AND OR NOT XOR Flipflop-D

{
  "v": 1,
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
  "v": 1,
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
    [29, 15, {"waypoints": [[340, 240]]}],
    [29, 9, {"waypoints": [[340, 130]]}]
  ]
}
```
````
`````


`````{admonition} Exercice 7 : signal alternatif
À l'aide d'une bascule, créez un circuit avec une sortie $Q$ qui s'inverse à chaque coup d'horloge.

```{logic}
:height: 300
:showonly: AND OR NOT XOR Flipflop-D

{
  "v": 1,
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
  "v": 1,
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
    [5, 0, {"waypoints": [[290, 120, "n"], [290, 40, "n"], [190, 40, "w"]]}]
  ]
}
```
````
`````


`````{admonition} Exercice 8 : jeu de fréquences
Observez le circuit ci-dessous. L'horloge principale $A$ fonctionne ici toute seule et produit un coup d'horloge par seconde (elle a donc une fréquence d'un hertz — 1 Hz). Que pouvez-vous dire des signaux $B$ et $C$ par rapport au signal $A$ ? Comment expliquer cela avec ce que vous savez des bascules ? (Pour simplifier, le délai de propagation est ici presque nul.)

Vous pouvez mettre l'animation en pause et exécuter chaque transition pas à pas pour mieux comprendre ce qui se passe.

```{logic}
:height: 280
:mode: tryout

{
  "v": 1,
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
    [16, 25, {"waypoints": [[250, 120, "s"], [120, 180, "s"]]}],
    [16, 10],
    [28, 11],
    [17, 12, {"waypoints": [[230, 120], [230, 50], [140, 50]]}],
    [29, 24, {"waypoints": [[230, 250], [230, 180], [140, 180]]}],
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


### Addition en plusieurs étapes

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
  "v": 1,
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
      "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
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
    [40, 37, {"waypoints": [[340, 400]]}],
    [40, 31, {"waypoints": [[340, 300, "n"]]}],
    [40, 25, {"waypoints": [[340, 200, "n"]]}],
    [40, 19, {"waypoints": [[340, 100, "n"]]}],
    [45, 35, {"waypoints": [[280, 380]]}],
    [45, 29, {"waypoints": [[280, 280, "n"]]}],
    [45, 23, {"waypoints": [[280, 180, "n"]]}],
    [45, 17, {"waypoints": [[280, 80, "n"]]}],
    [20, 46, {"waypoints": [[480, 40]]}],
    [26, 47, {"waypoints": [[480, 140]]}],
    [32, 48, {"waypoints": [[480, 240]]}],
    [38, 49, {"waypoints": [[480, 340]]}]
  ]
}
```

Connectons maintenant les entrées de l'ALU. On se rappelle qu'à chaque étape, l'ALU calculera une addition de la forme « accumulateur + nombre à additionner = nouvel accumulateur ». L'entrée $A$ de l'ALU est la valeur de l'accumulateur, donc ce qui est stocké par nos bascules. On connecte donc la sortie $Q$ de chaque bascule vers le bit d'entrée $A$ correspondant de l'ALU.

L'entrée $B$ de l'ALU est le nouveau nombre à additionner. Pour cela, nous ajoutons simplement quatre entrées normales, ainsi qu'un afficheur décimal pour nous simplifier la lecture du nombre représenté par ces entrées :

```{logic}
:height: 550
:mode: tryout

{
  "v": 1,
  "opts": {"showDisconnectedPins": true},
  "in": [
    {
      "pos": [340, 490],
      "orient": "n",
      "id": 40,
      "name": "Reset",
      "val": 0,
      "isPushButton": true
    },
    {"pos": [40, 220], "id": 41, "val": 0},
    {"pos": [40, 250], "id": 42, "val": 0},
    {"pos": [40, 280], "id": 43, "val": 0},
    {"pos": [40, 310], "id": 44, "val": 0},
    {
      "pos": [280, 490],
      "orient": "n",
      "id": 45,
      "name": "Horloge",
      "val": 0,
      "isPushButton": true
    }
  ],
  "out": [
    {
      "type": "nibble",
      "pos": [100, 390],
      "orient": "s",
      "id": [50, 51, 52, 53],
      "name": "B"
    },
    {"type": "nibble", "pos": [550, 230], "id": [46, 47, 48, 49], "name": "Acc."}
  ],
  "components": [
    {
      "type": "alu",
      "pos": [180, 210],
      "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      "out": [10, 11, 12, 13, 14, 15]
    },
    {
      "type": "flipflop-d",
      "pos": [390, 100],
      "in": [17, 18, 19, 16],
      "out": [20, 21],
      "state": 0
    },
    {
      "type": "flipflop-d",
      "pos": [390, 200],
      "in": [23, 24, 25, 22],
      "out": [26, 27],
      "state": 0
    },
    {
      "type": "flipflop-d",
      "pos": [390, 300],
      "in": [29, 30, 31, 28],
      "out": [32, 33],
      "state": 0
    },
    {
      "type": "flipflop-d",
      "pos": [390, 400],
      "in": [35, 36, 37, 34],
      "out": [38, 39],
      "state": 0
    }
  ],
  "wires": [
    [40, 37, {"waypoints": [[340, 440]]}],
    [40, 31, {"waypoints": [[340, 340, "n"]]}],
    [40, 25, {"waypoints": [[340, 240, "n"]]}],
    [40, 19, {"waypoints": [[340, 140, "n"]]}],
    [20, 0, {"waypoints": [[430, 80], [430, 50], [130, 50], [130, 130]]}],
    [26, 1, {"waypoints": [[440, 180], [440, 40], [120, 40], [120, 150]]}],
    [32, 2, {"waypoints": [[450, 280], [450, 30], [110, 30], [110, 170]]}],
    [38, 3, {"waypoints": [[460, 380, "n"], [460, 20], [100, 20], [100, 190]]}],
    [41, 4],
    [42, 5],
    [43, 6],
    [44, 7],
    [45, 35, {"waypoints": [[280, 420]]}],
    [45, 29, {"waypoints": [[280, 320, "n"]]}],
    [45, 23, {"waypoints": [[280, 220, "n"]]}],
    [45, 17, {"waypoints": [[280, 120, "n"]]}],
    [41, 50],
    [42, 51],
    [43, 52],
    [44, 53],
    [20, 46, {"waypoints": [[480, 80]]}],
    [26, 47, {"waypoints": [[480, 180]]}],
    [32, 48, {"waypoints": [[480, 280]]}],
    [38, 49, {"waypoints": [[480, 380]]}]
  ]
}
```

Il reste à connecter la sortie $S$ de l'ALU. Cette sortie nous livre la prochaine valeur à stocker dans l'accumulateur, et nous pouvons ainsi la connecter aux quatre entrées $D$ des bascules.

Voici le circuit final :

```{logic}
:height: 550
:mode: tryout

{
  "v": 1,
  "in": [
    {
      "pos": [340, 490],
      "orient": "n",
      "id": 40,
      "name": "Reset",
      "val": 0,
      "isPushButton": true
    },
    {"pos": [40, 220], "id": 41, "val": 0},
    {"pos": [40, 250], "id": 42, "val": 0},
    {"pos": [40, 280], "id": 43, "val": 0},
    {"pos": [40, 310], "id": 44, "val": 0},
    {
      "pos": [280, 490],
      "orient": "n",
      "id": 45,
      "name": "Horloge",
      "val": 0,
      "isPushButton": true
    }
  ],
  "out": [
    {
      "type": "nibble",
      "pos": [100, 390],
      "orient": "s",
      "id": [50, 51, 52, 53],
      "name": "B"
    },
    {"type": "nibble", "pos": [550, 230], "id": [46, 47, 48, 49], "name": "Acc."}
  ],
  "components": [
    {
      "type": "alu",
      "pos": [180, 210],
      "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      "out": [10, 11, 12, 13, 14, 15]
    },
    {
      "type": "flipflop-d",
      "pos": [390, 100],
      "in": [17, 18, 19, 16],
      "out": [20, 21],
      "state": 0
    },
    {
      "type": "flipflop-d",
      "pos": [390, 200],
      "in": [23, 24, 25, 22],
      "out": [26, 27],
      "state": 0
    },
    {
      "type": "flipflop-d",
      "pos": [390, 300],
      "in": [29, 30, 31, 28],
      "out": [32, 33],
      "state": 0
    },
    {
      "type": "flipflop-d",
      "pos": [390, 400],
      "in": [35, 36, 37, 34],
      "out": [38, 39],
      "state": 0
    }
  ],
  "wires": [
    [10, 16, {"waypoints": [[260, 80]]}],
    [11, 22, {"waypoints": [[260, 180]]}],
    [12, 28, {"waypoints": [[260, 280]]}],
    [13, 34, {"waypoints": [[260, 380]]}],
    [40, 37, {"waypoints": [[340, 440]]}],
    [40, 31, {"waypoints": [[340, 340, "n"]]}],
    [40, 25, {"waypoints": [[340, 240, "n"]]}],
    [40, 19, {"waypoints": [[340, 140, "n"]]}],
    [20, 0, {"waypoints": [[430, 80], [430, 50], [130, 50], [130, 130]]}],
    [26, 1, {"waypoints": [[440, 180], [440, 40], [120, 40], [120, 150]]}],
    [32, 2, {"waypoints": [[450, 280], [450, 30], [110, 30], [110, 170]]}],
    [38, 3, {"waypoints": [[460, 380, "n"], [460, 20], [100, 20], [100, 190]]}],
    [41, 4],
    [42, 5],
    [43, 6],
    [44, 7],
    [45, 35, {"waypoints": [[280, 420]]}],
    [45, 29, {"waypoints": [[280, 320, "n"]]}],
    [45, 23, {"waypoints": [[280, 220, "n"]]}],
    [45, 17, {"waypoints": [[280, 120, "n"]]}],
    [41, 50],
    [42, 51],
    [43, 52],
    [44, 53],
    [20, 46, {"waypoints": [[480, 80]]}],
    [26, 47, {"waypoints": [[480, 180]]}],
    [32, 48, {"waypoints": [[480, 280]]}],
    [38, 49, {"waypoints": [[480, 380]]}]
  ]
}
```

Ce circuit fonctionne ainsi : au début du calcul, on réinitialise les bascules à zéro avec le signal $Reset$. Ensuite, on compose le prochain nombre à additionner sur l'entrée $B$. L'ALU va calculer immédiatement la somme $A + B$, mais ce n'est qu'au prochain coup d'horloge que cette somme sera stockée dans les bascules et apparaîtra ainsi à droite. Après avoir donné ce coup d'horloge, donc, on pourra à nouveau composer sur l'entrée $B$ le prochain nombre à additionner, et ainsi de suite.

On réalise ici l'importance du coup d'horloge : si les bascules stockaient immédiatement la valeur livrée par l'ALU sans attendre le coup d'horloge, on retrouverait presque sans délai cette valeur sur la sortie des bascules et donc… à l'entrée $A$ de l'ALU, qui recalculerait immédiatement la somme de cette valeur et de l'entrée $B$, livrerait le résultat sur la sortie vers les bascules, qui feraient à nouveau la propagation immédiate de ceci sur leurs sorties et sur l'entrée $A$ de l'ALU, etc. — le système s'emballerait. Le signal d'horloge veille à ce que l'opération de stockage et de propagation soit coordonnée et se passe au bon moment.

`````{admonition} Exercice 9 : additions avec bascules
Suivez la procédure décrite ci-dessus pour effectuer l'addition $1 + 4 + 5 + 3 = 13$.
`````


<!-- TODO avons-nous besoin de cet exercice?
`````{admonition} Exercice 10 : bit de dépassement
Un problème avec le circuit actuel est qu'en cas de dépassement de capacité, (décrire problème du carry, comment s'en souvenir? circuit à modifier)

ajouter circuit de départ, mêne qu'en haut mais modifiable

````{dropdown} Corrigé
La solution consiste à stocker aussi le bit de dépassement $V$ au sortir de l'ALU à chaque coup d'horloge. Pour cela, il nous faut ajouter une nouvelle bascule, dont l'entrée récupère la sortie $V$ de l'ALU et dont l'horloge et le _reset_ dont les mêmes signaux que pour les autres bascules.

montrer circuit corrigé
````
`````
-->

## 3.4. Récapitulatif

Au cours des trois chapitres précédents, nous avons vu comment les portes logiques sont utilisées comme composants de base des ordinateurs. Nous avons d'abord exploré des portes simples comme **OU** et **ET**, puis montré comment ces portes peuvent être combinées en systèmes logiques plus complexes.

Avec des portes, nous avons construit un additionneur de deux bits. Nous avons ensuite été à même, en enchaînant plusieurs additionneurs, de créer un système qui peut additionner non pas simplement deux bits, mais deux nombres entiers codés sur 4 bits chacun.

Nous avons ensuite découvert l'unité arithmétique et logique, capable de réaliser plusieurs opérations différentes avec ses entrées en fonction de bits supplémentaires qui permettent de sélectionner l'opération à effectuer.

Notre dernière étape d'exploration des systèmes logiques nous a menés aux verrous et aux bascules, des composants pensés pour stocker des bits de données et ainsi constituer des cellules de mémoire pour l'ordinateur. Nous avons enfin été capables, avec une ALU et une série de bascules, d'additionner à la chaîne plusieurs nombres, en nous rappelant les résultats des additions intermédiaires.

Il existe bien d'autres éléments qui composent les ordinateurs et nous n'avons pas l'occasion de tous les explorer en détail. Dans la section qui suit, faisons un saut conceptuel et parlons de l'architecture générale des ordinateurs et de la manière dont les grands composants sont interconnectés pour permettre à un ordinateur de remplir les fonctions que nous lui connaissons.


````{dropdown} Jeu pour aller plus loin
Dans le jeu en ligne « Nandgame » (<https://nandgame.com>), on construit petit à petit un ordinateur complet juste avec, à la base, des portes **NON-ET**. Elles sont la particularité (avec les portes **NON-OU**, d'ailleurs) de pouvoir simuler toutes les autres portes — y compris un inverseur.
````
