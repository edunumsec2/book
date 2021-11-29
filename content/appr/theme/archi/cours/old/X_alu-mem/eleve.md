# X. De la logique à la mémoire

Dans cette section, nous continuons notre exploration de comment les portes logiques, selon leur assemblages, fournissent les fonctionnalités de base des ordinateurs. En particulier, nous nous intéressons à comment faire effectuer plusieurs opérations à un ordinateur via ce qui s'appelle une unité arithmétique et logique, puis nous voyons comment l'ordinateur se rappelle les résultats des calculs intermédiaires via des bascules.


## ALU

Dans la section précédente, nous avons vu comment créer, via un assemblage de portes logiques, un circuit qui réalise l'addition de deux nombres de 4 bits. Ce circuit était fixe : avec les deux nombres d'entrées, il réalistait toujours une addition et ne servait ainsi qu'à ça.

Les ordinateurs ont la propriété d'être programmables : ils savent effectuer plusieurs opérations, et c'est la manière dont ils sont programmés qui va déterminer l'opération qu'ils effectuent. C'est aussi vrai pour des machines plus simples; une calculatrice de poche, par exemple, pourra effectuer au moins les quatre opérations de base : addition, soustraction, multiplication et division.

Le composant qui nous permettra de sélectionner une opération ou une autre s'appelle « unité arithmétique et logique », communément appelé simplement « ALU » (de l'anglais _arithmetic logic unit_). Avant d'inspecter une ALU, nous avons besoin de comprendre comment on peut sélectionner une opération ou une autre avec des circuits logiques.


### Sélection de l'opération

Comment créer un circuit qui permet de sélectionner une opération à faire, et comment indiquer l'opération à sélectionner ? Essayons d'abord de créer un circuit à deux entrées qui va calculer soit le **OU** soit le **ET** de ces deux entrées.

Nous savons faire un circuit simple qui calcule le **OU** de deux entrées $X$ et $Y$, avec une seule porte logique :

```{logic}
:height: 140
:mode: tryout

{
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

 * Lorsque $Op = 0$, on va sélectionner $A$ et annuler $B$. On va donc faire passer $A$ à travers une porte **ET** à laquelle on donne 1 à l'autre entrée, et faire passer $B$ à travers une porte **ET** à laquelle on donne 0 à la secondre entrée.
 * Lorsque $Op = 1$, on va faire exactement l'inverse: sélectionner $B$ et annuler $A$. On donnera donc un 0 à la porte **ET** qui filtre $A$, et $1$ à la porte **ET** qui filtre $B$.

En relisant ces lignes, on voit que ce qu'on donne à la seconde entrée de la porte qui filtre $B$ est toujours la même chose que $Op$, et que ce qu'on donne à la seconde entrée de la porte qui filtre $A$ est toujours l'inverse de $Op$. On peut donc construire ce circuit avec un inverseur en plus :

```{logic}
:height: 290
:mode: tryout

{
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

Ceci nous permet de compléter le circuit lacunaire de début de chapitre pour sélectionner avec le même mécanime soit le **OU** soit le **ET** de nos deux entrées $X$ et $Y$. On ajoute notre sélecteur en connectant à l'entrée $A$ le signal représentant $X$ **OU** $Y$, et à l'entrée $B$ le signal représentant $X$ **ET** $Y$ :

```{logic}
:height: 300
:mode: tryout

{
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

````{admonition} Exercice XX : Test du sélecteur **OU**/**ET**
Testez le circuit ci-dessus. Établissez la table de vérité de $Z$ en fonction de $X$, $Y$ et $Op$. À l'aide de la table de vérité, montrez que, lorsque $Op=0$, $Z$ représente bien $X$ **OU** $Y$, et que, lorsque $Op=1$, $Z$ représente bien $X$ **ET** $Y$.
````

Nous avons ici construit un circuit qui, grâce à un bit de contrôle $Op$, sélectionne une opération ou une autre à appliquer à ses deux bits d'entrées $X$ et $Y$.


`````{admonition} Exercice XX : construction d'un sélecteur
En réutilisant les principes appliqués ci-dessus, construisez un circuit à deux bits d'entrées $X$ et $Y$ et un bit de contôle $Op$ qui donnera sur sa sortie $Z$ :

 * Le **OU** exclusif de $X$ et $Y$ lorsque $Op=0$;
 * L'inverse du bit $Y$ lorsque $Op=1$.

TODO éditeur

````{dropdown} Corrigé
```{logic}
:height: 300
:mode: tryout

{
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


`````{admonition} Exercice XX : inverser conditionnel
En réutilisant les principes appliqués ci-dessus, contruisez un circuit à une entrée $X$ avec un bit de contrôle $Op$ qui donnera sur sa sortie $Z$  :

 * $X$ tel quel lorsque $Op=0$;
 * $X$ inversé lorsque $Op=1$.

Écrivez la table de vérité de ce circuit. Correspond-elle par hasard à une porte déjà connue? Serait-ce dès lors possible de simplifier votre circuit?

TODO éditeur

````{dropdown} Corrigé

Voici A TODO:

```{logic}
:height: 290
:mode: tryout

{
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

On peut blabla TODO:
```{logic}
:height: 180
:mode: tryout

{
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

TODO



## Mémoire




**TODO:** _Du contenu supplémentaire sera rajouté ici pour parler de la mémoire._

<u> La construction de la mémoire </u>

Les {glo}`transistor|transistors`, les {glo}`portelogique|portes logiques` et leur représentation en {glo}`tableverite|tables de vérités`, permettent de manipuler des 0 et des 1 au niveau physique. Tant qu'un courant électrique se déplace dans les {glo}`circuit|circuits`, on est capable de le transformer, de le laisser passer ou de l'arrêter, dans le but d'exprimer des portes «ouvertes» ou des portes «fermées» et donc des nombres binaires.  

Mais comment faire pour {glo}`stockage|stocker` cette information ?

Pour comprendre comment la {glo}`stockage|mémoire` des ordinateurs fonctionne, il faut commencer par la classer en deux grandes catégories. La {glo}`memvolatile|mémoire volatile`, et la {glo}`memnonvolatile|mémoire non volatile`. La {glo}`memvolatile|mémoire volatile` s'efface quand la machine et éteinte. La {glo}`memnonvolatile|mémoire non volatile`, elle, persiste. Si un smartphone s'éteint alors que qu'on est en train de retoucher une photo, ces retouches disparaissent. Elles étaient stockées sur la {glo}`memvolatile|mémoire volatile`. Par contre, au moment où ces retouches sont sauvegardées, elles s'inscrivent dans la {glo}`memnonvolatile|mémoire non volatile`. 

### Les verrous informatiques

Pour stocker de l'information avec un circuit logique, il faut utiliser une autre technique que ce qui a été fait jusqu'à présent, où toutes les sorties dépendaient exclusivement et immédiatement des entrées. Regardons ce qui se passe avec ce circuit, par exemple : c'est une simple porte **OU**, dont l'une des entrées est en fait sa propre sortie.

```{logic}
:height: 100
:mode: tryout

{
  "in": [{"pos": [50, 30], "id": 4, "name": "X", "val": 0}],
  "gates": [{"type": "OR", "pos": [140, 40], "in": [5, 6], "out": 7}],
  "out": [{"pos": [240, 40], "id": 0, "name": "Z"}],
  "wires": [[4, 5], [7, 6, {"waypoints": [[170, 80, "w"], [110, 80, "w"]]}], [7, 0]]
}
```

Au début, les deux entrées de la porte valent 0, comme sa sortie. Si l'on essaie de faire passer l'entrée $X$ à 1, on voit que la sortie $Z$ passera à 1 elle aussi, comme il s'agit d'une porte **OU**. Mais comme $Z$ est aussi relié à l'autre entrée de la porte, on a maintenant un circuit dont on ne peux plus modifier la sortie : même si $X$ passe de nouveau à 0, l'autre entrée reste à 1 et suffit donc pour que $Z$ vale maintenant 1 indéfiniment. On est obligé de remettre le circuit complètement à zéro (l'équivalent de débrancher la prise de courant et de la rebrancher) pour obtenir à nouveau un 0 sur la sortie $Z$.

Assurément, ce circuit n'est pas très intéressant : il se bloque dans un état sans retour possible. Serait-ce possible de construire un circuit un peu plus élaboré qui permettrait de choisir la valeur de sa sortie et de la conserver ? Ces circuits existent en effet et sont à la base du stockage de l'information dans les microprocesseurs. On appelle ces circuits des {glo}`verrou|verrous`. Examinons le circuit ci-dessous : c'est le verrou dit «S-R», pour _set/reset_, en anglais. 

```{logic}
:height: 160

{
  "in": [
    {"pos": [50, 30], "id": 8, "name": "R", "val": 1},
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

Dans l'exemple ci-dessus, à partir du moment où on a «ouvert» la porte S (donc qu'on a «set», c'est à dire «établi» l'état initial), la sortie Q est 1. Si on avait une ampoule à cet endroit, elle serait allumée. Maintenant, même si on «ferme» la porte S, Q reste bloqué sur 1. On a donc créé une forme de mémoire. La seule façon «d'éteindre» la sortie Q est d'ouvrir R (donc de «reset», c'est à dire réinitialiser le système). 

Voici une vidéo qui illustre ce principe de verrou S-R.

```{youtube} KM0DdEaY5sY
:start: 4:58
```

Pour aller plus loin, une vidéo de résumé qui parle aussi des bascules et des registres :

```{youtube} I0-izyq6q5s
```

````{admonition} Pour aller plus loin
:class: attention

Dans le jeu en ligne «Nandgame» (<https://nandgame.com>), on construit petit à petit un ordinateur complet juste avec, à la base, des portes **NON-ET**. Elles sont la particularité, avec la porte **NON-OU**, de pouvoir simuler toutes les autres portes (y compris un inverseur).
````
