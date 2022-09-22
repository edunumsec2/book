(soutracteur)=
Soustracteur
============

((TODO))

## Objectifs
((TODO))


## Fiche
````{panels}
Fiche
^^^^^
* Type d'activité : travaux pratique avec le simulateur logique
* Durée : 1 période
* Par groupe : possible/recommandé

---

Résumé
^^^^^
((TODO))

````

## Déroulement

### Première partie: 

((TODO — à compléter!))

```{logic}
:mode: design
:height: 450
:showonly: and,or,xor,not,adder,alu,in,out

{
  "v": 3,
  "in": [
    {"pos": [100, 50], "id": 4, "name": "X0", "val": 1},
    {"pos": [100, 90], "id": 5, "name": "X1", "val": 0},
    {"pos": [100, 130], "id": 6, "name": "X2", "val": 1},
    {"pos": [100, 170], "id": 7, "name": "X3", "val": 0}
  ],
  "out": [
    {"type": "nibble", "pos": [350, 80], "id": [8, 9, 10, 11], "name": "X", "radix": -10},
    {"type": "nibble", "pos": [350, 360], "id": [0, 1, 2, 3], "name": "Y = –X", "radix": -10}
  ],
  "wires": [[4, 8], [5, 9], [6, 10], [7, 11]]
}
```

#### Solution

Avec ALU:

```{logic}
:height: 480
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [100, 50], "id": 4, "name": "X0", "val": 1},
    {"pos": [100, 90], "id": 5, "name": "X1", "val": 0},
    {"pos": [100, 130], "id": 6, "name": "X2", "val": 1},
    {"pos": [100, 170], "id": 7, "name": "X3", "val": 0},
    {"pos": [240, 240], "orient": "s", "id": 28, "name": "Op", "val": 1}
  ],
  "out": [
    {"type": "nibble", "pos": [350, 80], "id": [8, 9, 10, 11], "name": "X", "radix": -10},
    {"type": "nibble", "pos": [350, 360], "id": [0, 1, 2, 3], "name": "Y = –X", "radix": -10}
  ],
  "components": [{"type": "alu", "pos": [230, 360], "in": [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 29], "out": [22, 23, 24, 25, 26, 27]}],
  "wires": [[4, 8], [5, 9], [6, 10], [7, 11], [28, 20], [4, 16], [5, 17], [6, 18], [7, 19], [22, 0], [23, 1], [24, 2], [25, 3]]
}
```

… Mais ce n'est pas le but! Donc sans ALU:

```{logic}
:height: 570
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [100, 50], "id": 4, "name": "X0", "val": 1},
    {"pos": [100, 90], "id": 5, "name": "X1", "val": 0},
    {"pos": [100, 130], "id": 6, "name": "X2", "val": 1},
    {"pos": [100, 170], "id": 7, "name": "X3", "val": 0},
    {"pos": [280, 150], "id": 26, "val": 1}
  ],
  "out": [
    {"type": "nibble", "pos": [350, 80], "id": [8, 9, 10, 11], "name": "X", "radix": -10},
    {"type": "nibble", "pos": [480, 330], "id": [0, 1, 2, 3], "name": "Y = –X", "radix": -10}
  ],
  "gates": [
    {"type": "NOT", "pos": [220, 220], "in": 12, "out": 13},
    {"type": "NOT", "pos": [220, 320], "in": 14, "out": 15},
    {"type": "NOT", "pos": [220, 420], "in": 16, "out": 17},
    {"type": "NOT", "pos": [220, 520], "in": 18, "out": 19}
  ],
  "components": [
    {"type": "adder", "pos": [330, 200], "orient": "n", "in": [20, 21, 22], "out": [23, 24]},
    {"type": "adder", "pos": [330, 300], "orient": "n", "in": [31, 32, 33], "out": [34, 35]},
    {"type": "adder", "pos": [330, 400], "orient": "n", "in": [36, 37, 38], "out": [39, 40]},
    {"type": "adder", "pos": [330, 500], "orient": "n", "in": [41, 42, 43], "out": [44, 45]}
  ],
  "wires": [
    [4, 8],
    [5, 9],
    [6, 10],
    [7, 11],
    [13, 20],
    [26, 22],
    [4, 12],
    [5, 14],
    [6, 16],
    [7, 18],
    [24, 33],
    [35, 38],
    [40, 43],
    [15, 31],
    [17, 36],
    [19, 41],
    [23, 0],
    [34, 1],
    [39, 2],
    [44, 3]
  ]
}
```
