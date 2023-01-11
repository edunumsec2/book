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
:showonly: adder
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
:showonly: in.nibble out.nibble-display decoder-7seg out.7seg
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

## Addition et soustraction

Ajoutez un circuit qui calcule a+b-c et affiche le résultat.
Par exemple pour a=7, b=5, c=3, le résultat affiché devrait être 9.

```{logic}
:ref: mux
:height: 500
:showonly: alu in out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [60, 80], "id": [11, 12, 13, 14], "val": [1, 1, 1, 0], "name": "a"},
    {"type": "nibble", "pos": [60, 180], "id": [79, 80, 81, 82], "val": [1, 0, 1, 0], "name": "b"},
    {"type": "nibble", "pos": [60, 280], "id": [105, 106, 107, 108], "val": [1, 1, 0, 0], "name": "c"}
  ],
  "out": [
    {"type": "nibble-display", "pos": [110, 80], "id": [67, 68, 69, 70]},
    {"type": "nibble-display", "pos": [110, 180], "id": [83, 84, 85, 86]},
    {"type": "nibble-display", "pos": [110, 280], "id": [114, 115, 116, 117]}
  ],
  "wires": [[11, 67], [12, 68], [13, 69], [14, 70], [79, 83], [80, 84], [81, 85], [82, 86], [105, 114], [106, 115], [107, 116], [108, 117]]
}
```

## Addition signée

Interprétez les nombres binaires comme des nombres signés. Vous pouvez le configurer avec le menu contextuel. Complétez l'additionneur 4-bit et montrez que l'addition de -2 et -3 donne bien -5.

```{logic}
:ref: addsigned
:height: 500
:showonly: alu in in.nibble out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [60, 80], "id": [0, 1, 2, 3], "val": [0, 1, 1, 1]}
  ],
  "out": [
    {"type": "nibble-display", "pos": [110, 80], "id": [4, 5, 6, 7], "radix": -10}
  ],
  "components": [
    {"type": "alu", "pos": [230, 130], "in": [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "out": [19, 20, 21, 22, 23, 24, 25]}
  ],
  "wires": [[0, 4], [1, 5], [2, 6], [3, 7], [0, 8], [1, 9], [2, 10], [3, 11]]
}
```

## Addition 8-bits

Pour additionner un nombre à 8-bits, il faut combiner deux ALU 4-bits.
Complétez le circuit pour afficher l'addition de deux nombres binaires 8-bits.
Ajoutez une option pour soustraire deux nombres.

```{logic}
:ref: add8
:height: 500
:showonly: alu in in.byte out.byte-display
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [40, 110], "id": [24, 25, 26, 27, 28, 29, 30, 31], "val": "00001010"},
    {"type": "byte", "pos": [40, 320], "id": [74, 75, 76, 77, 78, 79, 80, 81], "val": "00000100"}
  ],
  "out": [
    {"type": "byte-display", "pos": [100, 110], "id": [32, 33, 34, 35, 36, 37, 38, 39]},
    {"type": "byte-display", "pos": [400, 170], "id": [66, 67, 68, 69, 70, 71, 72, 73]}
  ],
  "components": [
    {"type": "alu", "pos": [220, 130], "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "out": [11, 12, 13, 14, 15, 16, 17]},
    {"type": "alu", "pos": [220, 360], "in": [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], "out": [59, 60, 61, 62, 63, 64, 65]}
  ],
  "wires": [[24, 32], [25, 33], [26, 34], [27, 35], [28, 36], [29, 37], [30, 38], [31, 39], [17, 58], [24, 0], [25, 1], [26, 2], [27, 3], [28, 48], [29, 49], [30, 50], [31, 51], [11, 66], [12, 67], [13, 68], [14, 69], [74, 4], [75, 5], [76, 6]]
}
```


## Multiplexeur

Un multiplexeur permet de choisir entre deux signaux d'entrée et d'en transmettre un à sa sortie.

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

## Compteur avec bascule D

Une bascule D avec une rétroaction de la sorte Q_inv vers son entrée D divise la fréquence de l'horloge en 2. Nous avons effectivement un compteur.

- Ajoute 2 bascules D pour compter jusqu'à 15
- Modifie le circuit pour compter vers le haut (0 à 15)

```{logic}
:ref: shift
:height: 500
:showonly: in out out.nibble clock flipflop-d
{
  "v": 3,
  "opts": {"propagationDelay": 10},
  "in": [{"type": "clock", "pos": [40, 90], "id": 7, "period": 2000}],
  "components": [{"type": "flipflop-d", "pos": [180, 150], "in": [8, 9, 10, 11], "out": [12, 13], "state": 1}],
  "out": [{"type": "nibble", "pos": [250, 40], "orient": "n", "id": [29, 30, 31, 32]}],
  "wires": [[13, 11], [12, 30], [7, 29], [7, 8]]
}
```

## Compteur 4 bits

Le compteur 4 bits utilise un signal d'horloge et incrémenté à chaque coup d'horloge.
Un un décodeur à 7 segments transforme les 4 signaux qui représentent un nombre binaire de 0 à 16 vers les sorties correspondant pour activer les bonnes lampes de l'affichage à 7 segments.

- Utilisez le signal de sortie V (overflow) pour faire fonctionner un deuxième compteur
- Ceci donnera un compteur 8 bit, permettant de compter de 0 à FF (255)
- Diminuez la période de l'horloge à 250 ms

```{logic}
:ref: counter
:height: 500
:showonly: in clock counter out.7seg in decoder-7seg
{
  "v": 3,
  "components": [
    {"type": "counter", "pos": [130, 70], "in": [0, 1], "out": [2, 3, 4, 5, 6], "count": 13},
    {"type": "decoder-7seg", "pos": [260, 60], "in": [9, 10, 11, 12], "out": [13, 14, 15, 16, 17, 18, 19]}
  ],
  "in": [
    {"type": "clock", "pos": [60, 110], "id": 7, "period": 2000},
    {"pos": [130, 160], "orient": "n", "id": 8, "name": "C (Clear, mise à 0)", "val": 0, "isPushButton": true}
  ],
  "out": [{"type": "7seg", "pos": [370, 70], "id": [20, 21, 22, 23, 24, 25, 26, 27]}],
  "wires": [[7, 0], [8, 1], [2, 9], [3, 10], [4, 11], [5, 12], [13, 20], [14, 21], [15, 22], [16, 23], [17, 24], [18, 25], [19, 26]]
}
```

## Compteur avec remise

Pour créer une montre, un minuteur ou une alarme, nous devons compter à 60, 12 ou 24.
L'entrée Reset peut être utilisé pour remettre le compteur. Une porte ET détecte le nombre 6 et remet le compter

- Ajoutez un deuxième compteur
- Configurez-le pour qu'il compte de 0 à 9
- Ajoutez le décodeur et un affichage à 7 segments
- Utilisez les deux compteurs pour faire un compteur qui affiche les nombres 00 à 59
- Diminuez la période à 1 seconde

```{logic}
:ref: counter_6
:height: 500
:showonly: in clock counter out.7seg in decoder-7seg
{
  "v": 3,
  "components": [
    {"type": "counter", "pos": [130, 70], "in": [0, 1], "out": [2, 3, 4, 5, 6], "count": 1},
    {"type": "decoder-7seg", "pos": [380, 60], "in": [9, 10, 11, 12], "out": [13, 14, 15, 16, 17, 18, 19]}
  ],
  "in": [{"type": "clock", "pos": [60, 110], "id": 7, "period": 2000}],
  "out": [{"type": "7seg", "pos": [490, 70], "id": [20, 21, 22, 23, 24, 25, 26, 27]}],
  "gates": [{"type": "AND", "pos": [220, 150], "orient": "s", "in": [28, 29], "out": 30}],
  "wires": [
    [7, 0],
    [2, 9],
    [3, 10],
    [4, 11],
    [5, 12],
    [13, 20],
    [14, 21],
    [15, 22],
    [16, 23],
    [17, 24],
    [18, 25],
    [19, 26],
    [4, 29],
    [3, 28],
    [30, 1]
  ]
}
```

## Horloge avec secondes

Un compteur 4 bits avec un circuit de remise à 0 peut être configuré pour afficher les secondes de 00 à 59.

- Ajoutez un deuxième compteur, décodeur et affichage à 7 segments
- Configurez-le pour compter à 60

```{logic}
:ref: clock09
:height: 500
:showonly: clock in counter out.7seg decoder.7seg
{
  "v": 3,
  "opts": {"propagationDelay": 10},
  "components": [
    {"type": "counter", "pos": [120, 70], "in": [35, 36], "out": [37, 38, 39, 40, 41], "count": 9},
    {"type": "decoder-7seg", "pos": [250, 60], "in": [42, 43, 44, 45], "out": [46, 47, 48, 49, 50, 51, 52]}
  ],
  "gates": [{"type": "AND", "pos": [200, 170], "orient": "s", "in": [53, 54], "out": 55}],
  "out": [{"type": "7seg", "pos": [330, 70], "id": [56, 57, 58, 59, 60, 61, 62, 63]}],
  "in": [{"type": "clock", "pos": [50, 110], "id": 64, "period": 2000}],
  "wires": [
    [38, 53],
    [37, 42],
    [38, 43],
    [39, 44],
    [40, 45],
    [55, 36],
    [40, 54],
    [46, 56],
    [47, 57],
    [48, 58],
    [49, 59],
    [50, 60],
    [51, 61],
    [52, 62],
    [64, 35]
  ]
}
```

## Parcourir l'alphabet

Les affichages à 16 segments permettent d'afficher les chiffres, lettres et divers symboles.

- Changez pour afficher 15 minuscules

```{logic}
:ref: counter_16seg
:height: 500
:showonly: in in.nibble clock counter decoder-16seg out.16seg
{
  "v": 3,
  "components": [
    {"type": "counter", "pos": [110, 70], "in": [0, 1], "out": [2, 3, 4, 5, 6], "count": 7},
    {
      "type": "decoder-16seg",
      "pos": [330, 70],
      "in": [55, 56, 57, 58, 59, 60, 61],
      "out": [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]
    }
  ],
  "in": [
    {"type": "clock", "pos": [40, 110], "id": 7, "period": 2000},
    {"type": "nibble", "pos": [220, 150], "id": [87, 88, 89, 90], "val": [0, 0, 1, 0]},
    {"pos": [110, 160], "orient": "n", "id": 92, "name": "C (Clear, mise à 0)", "val": 0, "isPushButton": true}
  ],
  "out": [{"type": "16seg", "pos": [480, 70], "id": [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]}],
  "wires": [
    [7, 0],
    [62, 38],
    [63, 39],
    [64, 40],
    [65, 41],
    [66, 42],
    [67, 43],
    [68, 44],
    [69, 45],
    [70, 46],
    [71, 47],
    [72, 48],
    [73, 49],
    [74, 50],
    [75, 51],
    [76, 52],
    [77, 53],
    [78, 54],
    [2, 55],
    [3, 56],
    [4, 57],
    [5, 58],
    [87, 59],
    [88, 60],
    [89, 61],
    [92, 1]
  ]
}
```

## Rouler un dé

Un dé électronique utilise 7 LEDs pour afficher les points.
Une horloge rapide, liée par une porte ET vers l'entrée d'un compteur compte rapidement de 0 à 5.
À 6 le compteur est remis à 0 à l'aide d'une autre porte ET.

Voici la table de vérité pour les 7 LEDS.

| dice | bin | a | b | c | d | e | f | g |
|:----:|-----|---|---|---|---|---|---|---|
|   1  | 000 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
|   2  | 001 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
|   3  | 010 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
|   4  | 011 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
|   5  | 100 | 1 | 0 | 1 | 1 | 1 | 0 | 1 |
|   6  | 101 | 1 | 1 | 1 | 0 | 1 | 1 | 1 |

Ajoutez les portes logiques appropriées pour implémenter ce dé électronique.

```{logic}
:ref: dice
:height: 500
:showonly: in clock not and or out.bar
{
  "v": 3,
  "opts": {"propagationDelay": 10},
  "out": [
    {"type": "bar", "pos": [440, 290], "id": 0, "display": "px", "name": "a"},
    {"type": "bar", "pos": [440, 340], "id": 1, "display": "px", "name": "b"},
    {"type": "bar", "pos": [490, 340], "orient": "s", "id": 2, "display": "px", "name": "d"},
    {"type": "bar", "pos": [440, 390], "id": 3, "display": "px", "name": "c"},
    {"type": "bar", "pos": [540, 340], "id": 4, "display": "px", "name": "f"},
    {"type": "bar", "pos": [540, 290], "id": 5, "display": "px", "name": "e"},
    {"type": "bar", "pos": [540, 390], "id": 6, "display": "px", "name": "g"}
  ],
  "in": [{"type": "clock", "pos": [40, 30], "id": 9, "period": 100}, {"pos": [90, 150], "id": 23, "name": "rouler", "val": 0, "isPushButton": true}],
  "components": [{"type": "counter", "pos": [210, 80], "in": [10, 11], "out": [12, 13, 14, 15, 16], "count": 4}],
  "gates": [
    {"type": "AND", "pos": [290, 210], "orient": "s", "in": [17, 18], "out": 19},
    {"type": "AND", "pos": [120, 80], "in": [20, 21], "out": 22},
    {"type": "NOT", "pos": [330, 40], "in": 24, "out": 25}
  ],
  "wires": [
    [13, 17],
    [14, 18],
    [19, 11],
    [22, 10],
    [9, 20],
    [23, 21],
    [12, 24],
    [25, 2]
  ]
}
```
