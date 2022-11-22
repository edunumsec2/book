# TP ALU

Dans cette section, nous allons explorer d'abord l'additionneur et ensuite une **unité arithmétique et logique**, ou simplement une ALU.

## Demi-additionneur

Le demi-additionneur peut additionner deux bits A et B.

- Trouvez la table de vérité du demi-additionneur
- Reconstruisez-le avec des portes ET, OU et X-OU

```{logic}
:ref: add
:height: 500
:showonly: in out not and or xor
{
  "v": 3,
  "components": [{"type": "halfadder", "pos": [130, 50], "in": [51, 52], "out": [53, 54]}],
  "in": [{"pos": [60, 30], "id": 55, "name": "A", "val": 0}, {"pos": [60, 70], "id": 56, "name": "B", "val": 0}],
  "out": [{"pos": [200, 30], "id": 57, "name": "S (somme)"}, {"pos": [200, 70], "id": 58, "name": "C (retenue)"}],
  "wires": [[55, 51], [56, 52], [53, 57], [54, 58]]
}
```

## Additionneur

L'additionneur ci-dessous additionne 1 et 2 et affiche 3.

- Ajoutez les circuits manquants pour additionner deux nombres 4-bits.

```{logic}
:ref: add2
:height: 500
:showonly: fulladder
{
  "v": 3,
  "components": [
    {"type": "adder", "pos": [300, 170], "orient": "n", "in": [25, 26, 27], "out": [28, 29]},
    {"type": "adder", "pos": [300, 70], "orient": "n", "in": [30, 31, 32], "out": [33, 34]}
  ],
  "in": [
    {"type": "nibble", "pos": [30, 160], "id": [37, 38, 39, 40], "val": [1, 0, 0, 0]},
    {"type": "nibble", "pos": [30, 290], "id": [74, 75, 76, 77], "val": [0, 1, 0, 0]}
  ],
  "out": [
    {"type": "nibble", "pos": [410, 180], "id": [41, 42, 43, 44]},
    {"type": "nibble", "pos": [150, 160], "id": [53, 54, 55, 56]},
    {"type": "nibble", "pos": [150, 290], "id": [78, 79, 80, 81]}
  ],
  "wires": [
    [34, 27],
    [37, 31],
    [38, 26],
    [33, 41],
    [28, 42],
    [37, 53],
    [38, 54],
    [39, 55],
    [40, 56],
    [74, 78],
    [75, 79],
    [76, 80],
    [77, 81],
    [74, 30],
    [75, 25]
  ]
}
```

## ALU

L'ALU que nous avons peut effectuer 4 opérations

- addition (00)
- soustraction (01)
- OU logique (10)
- ET logique (11)

Ajoutez la deuxième entrée, un bloc de visualisation, un décodeur 7 segments et un affichage à 7 segments.

```{logic}
:ref: add2
:height: 500
:showonly: in.nibble out.nibble decoder-7seg out.7seg
{
  "v": 3,
  "components": [{"type": "alu", "pos": [230, 200], "in": [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], "out": [62, 63, 64, 65, 66, 67]}],
  "out": [
    {"type": "nibble", "pos": [340, 200], "id": [68, 69, 70, 71]},
    {"type": "nibble", "pos": [130, 150], "id": [80, 81, 82, 83]},
    {"pos": [300, 340], "id": 88, "name": "Z (Zero)"},
    {"pos": [200, 370], "orient": "s", "id": 89, "name": "V (oVerflow)"}
  ],
  "in": [
    {"type": "nibble", "pos": [40, 150], "id": [72, 73, 74, 75], "val": [1, 0, 1, 0]},
    {"pos": [190, 50], "orient": "s", "id": 90, "name": "Op1", "val": 0},
    {"pos": [230, 70], "orient": "s", "id": 91, "name": "Op0", "val": 0}
  ],
  "wires": [
    [62, 68],
    [63, 69],
    [64, 70],
    [65, 71],
    [72, 51],
    [73, 52],
    [74, 53],
    [75, 54],
    [72, 80],
    [73, 81],
    [74, 82],
    [75, 83],
    [67, 88],
    [66, 89],
    [90, 60],
    [91, 59]
  ]
}
```

## Multiplexeur

Un multiplexeur permet de choisir entre deux signaux d'entrées et d'en transmettre un à sa sortie.

- Créez un multiplexeur à partir des portes NON, ET et OU

```{logic}
:ref: mux
:height: 500
:showonly: not and or
{
  "v": 3,
  "in": [
    {"type": "clock", "pos": [70, 40], "id": 59, "period": 2000},
    {"type": "clock", "pos": [70, 120], "id": 61, "period": 500},
    {"pos": [190, 150], "orient": "n", "id": 66, "name": "S0", "val": 1},
    {"type": "clock", "pos": [70, 270], "id": 67, "period": 1000},
    {"type": "clock", "pos": [70, 350], "id": 68, "period": 250}
  ],
  "out": [
    {"type": "bar", "pos": [400, 90], "id": 60, "display": "PX"},
    {"type": "bar", "pos": [400, 310], "id": 69, "display": "PX", "color": "red"}
  ],
  "components": [{"type": "mux-2to1", "pos": [190, 90], "in": [62, 63, 64], "out": 65}],
  "wires": [[59, 62], [61, 63], [65, 60], [66, 64]]
}
```

## Égalité

Souvent il est nécessaire de comparer deux valeurs numériques.

- Créez un comparateur qui a comme résultat **Egal** à 1 si les deux nombres a et b sont égaux.

```{logic}
:ref: mux
:height: 500
:showonly: in alu
{
  "v": 3,
  "in": [
    {"type": "nibble", "pos": [40, 130], "id": [4, 5, 6, 7], "val": [1, 0, 1, 0], "name": "a"},
    {"type": "nibble", "pos": [40, 230], "id": [8, 9, 10, 11], "val": [1, 1, 1, 0], "name": "b"},
    {"pos": [160, 50], "orient": "s", "id": 29, "name": "Op0", "val": 1}
  ],
  "components": [{"type": "alu", "pos": [160, 180], "in": [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], "out": [23, 24, 25, 26, 27, 28]}],
  "out": [{"pos": [380, 170], "id": 30, "name": "Egal"}],
  "wires": [[4, 12], [5, 13], [6, 14], [7, 15], [8, 16], [9, 17], [10, 18], [11, 19], [29, 20], [28, 30]]
}
```