# TP Additionneur

Dans cette section, nous allons explorer d'abord la porte OU-X, l'additionneur qui sert de base pour

- addtion
- soustraction
- incrémentation
- décrémentation
## La porte ou exclusif

Le circuit ci-dessous représente une porte OU exclusive (XOR).
La sortie est 1 seulement si l'une ou l'autre des entrées est à 1.
Vérifiez le comportement avec les 4 entrées 00, 01, 10, 11.

Créez une deuxième façon pour obtenir une porte OU exclusive en utilisant :

- 2 portes NON
- 2 portes ET
- 1 porte OU

```{logic}
:ref: add
:height: 400
:showonly: in out not and or
{
  "v": 4,
  "in": [
    {"pos": [40, 30], "id": 0, "val": 0},
    {"pos": [40, 110], "id": 47, "val": 0}
  ],
  "out": [
    {"pos": [430, 50], "id": 59}
  ],
  "gates": [
    {"type": "OR", "pos": [170, 40], "in": [48, 49], "out": 50},
    {"type": "AND", "pos": [170, 100], "in": [51, 52], "out": 53},
    {"type": "NOT", "pos": [250, 100], "in": 54, "out": 55},
    {"type": "AND", "pos": [360, 50], "in": [56, 57], "out": 58}
  ],
  "wires": [[0, 48], [47, 49], [0, 51], [47, 52], [53, 54], [50, 56], [55, 57], [58, 59]]
}
```

## Porte OU-X

Une porte OU-X (ou exclusif) donne une sortie 1 si **exactement une** des entrées est à 1.

- Montrez la table de vérité pour la porte OU-X. 
- Ajoutez 3 portes OU-X et mettez les entrées à 01, 10, et 11
- Créez une porte OU-X avec 3 entrées et observez son comportement

```{logic}
:ref: or
:height: 400
:showonly: in out xor
{
  "v": 4,
  "in": [
    {"pos": [40, 60], "id": 7, "val": 0},
    {"pos": [40, 80], "id": 8, "val": 0},
    {"pos": [270, 50], "id": 16, "val": 0},
    {"pos": [270, 90], "id": 17, "val": 0},
    {"pos": [270, 130], "id": 18, "val": 0}
  ],
  "out": [
    {"pos": [180, 70], "id": 9},
    {"pos": [510, 90], "id": 19}
  ],
  "gates": [
    {"type": "XOR", "pos": [110, 70], "in": [4, 5], "out": 6}
  ],
  "labels": [
    {"pos": [110, 20], "text": "table de vérité"},
    {"pos": [390, 20], "text": "porte OU-X avec 3 entrées"}
  ],
  "wires": [[7, 4], [8, 5], [6, 9]]
}
```

## Détecteur de parité

Une porte ou exclusif est un détecteur de parité (pair/impair). La sortie d'une porte ou exclusif est 1 si le nombre des entrées actives est impair.

Ajoutez encore 6 portes XOR et complétez la table de vérité pour les 8 combinaisons possibles:

- pair : 000, 011, 101, 110
- impair : 001, 010, 100, 111

```{logic}
:ref: xor3
:height: 400
:showonly: in out xor3
{
  "v": 4,
  "in": [
    {"pos": [50, 60], "id": 23, "val": 0},
    {"pos": [50, 80], "id": 24, "val": 0},
    {"pos": [50, 100], "id": 25, "val": 0},
    {"pos": [310, 60], "id": 33, "val": 1},
    {"pos": [310, 80], "id": 34, "val": 0},
    {"pos": [310, 100], "id": 35, "val": 0}
  ],
  "out": [
    {"pos": [210, 80], "id": 28},
    {"pos": [470, 80], "id": 36}
  ],
  "gates": [
    {"type": "XOR3", "pos": [130, 80], "in": [19, 20, 21], "out": 22},
    {"type": "NOR3", "pos": [390, 80], "in": [29, 30, 31], "out": 32}
  ],
  "labels": [
    {"pos": [110, 20], "text": "entrée pair"},
    {"pos": [390, 20], "text": "entrée impair"}
  ],
  "wires": [[23, 19], [24, 20], [25, 21], [22, 28], [33, 29], [34, 30], [35, 31], [32, 36]]
}
```

Pour détecter si un nombre d'entrées est pair, il suffit d'ajouter un NON à la sortie du OU-X. On appelle ce circuit un NON-OU-X.

## Multiples commutateurs

La porte X-OU permet d'allumer et éteindre une lampe avec des commutateurs multiples.

Dans le schéma ci-dessous, on peut allumer la lumière dans une pièce à partir de la porte d'entrée et de la cuisine.

Ajoutez un circuit pour qu'on puisse également l'allumer depuis la chambre.

```{logic}
:ref: xor
:height: 500
:showonly: in out not and or xor
{
  "v": 3,
  "labels": [{"type": "rect", "pos": [290, 120], "w": 300, "h": 200, "color": "yellow", "strokeWidth": 2}],
  "in": [
    {"pos": [100, 150], "id": 9, "name": "entrée", "val": 0},
    {"pos": [290, 250], "orient": "n", "id": 14, "name": "chambre", "val": 0},
    {"pos": [470, 120], "orient": "w", "id": 15, "name": "cuisine", "val": 0}
  ],
  "out": [{"type": "bar", "pos": [300, 40], "id": 10, "display": "px", "color": "yellow"}],
  "gates": [{"type": "XOR", "pos": [220, 90], "orient": "n", "in": [11, 12], "out": 13}],
  "wires": [[13, 10], [9, 11], [15, 12]]
}
```

## Addition binaire

Nous avons maintenant toutes les éléments pour construire un additionneur binaire. Rappelons-nous que l'addition binaire est très simple.

| a | b | a+b |
|---|---|-----|
| 0 | 0 | 00  |
| 0 | 1 | 01  |
| 1 | 0 | 01  |
| 1 | 1 | 10  |

Nous remarquons que nous avons besoin de deux bits pour représenter le résultat. Si vous regardez les deux colonnes du résultat, vous constatez que

- la colonne du gauche représente la fonction ET (retenue ou *carry* en anglais)
- la colonne de droite représente la fonction OU-X (somme)

Vous trouvez le circuit ci-dessous à droite. Vérifiez sa fonction en cliquant sur ses entrées.

Ajoutez encore 3 demi-additionneurs et montrez la table de vérité pour les 4 conditions d'entrée : 00, 01, 10, 11

```{logic}
:ref: add
:height: 450
:showonly: in out and xor halfadder
{
  "v": 4,
  "in": [
    {"pos": [370, 270], "id": 0, "name": "a", "val": 0},
    {"pos": [370, 320], "id": 1, "name": "b", "val": 0},
    {"pos": [50, 60], "id": 18, "name": "A", "val": 0},
    {"pos": [50, 100], "id": 19, "name": "B", "val": 0}
  ],
  "out": [
    {"pos": [550, 280], "id": 8, "name": "s"},
    {"pos": [550, 340], "ref": "c", "id": 9, "name": "c"},
    {"pos": [190, 60], "id": 20, "name": "S (somme)"},
    {"pos": [190, 100], "id": 21, "name": "C (retenue)"}
  ],
  "gates": [
    {"type": "XOR", "pos": [480, 280], "in": [2, 3], "out": 4},
    {"type": "AND", "pos": [480, 340], "in": [5, 6], "out": 7}
  ],
  "components": [
    {"type": "halfadder", "pos": [120, 80], "in": [10, 11], "out": [12, 13]}
  ],
  "labels": [
    {"pos": [100, 20], "text": "table de vérité"}
  ],
  "wires": [[0, 2], [0, 5], [1, 3], [1, 6], [4, 8], [7, 9], [18, 10], [19, 11], [12, 20], [13, 21]]
}
```

## Additionneur complet

L'additionneur de 2 bits est très limité. Pour le cas général, nous avons besoin d'un additionneur qui additionne 3 bits. Il faut tenir compte de la retenue de la colonne à droite, qu'il faut inclure dans l'addition. Voici donc la table de vérité pour un additionneur complet.

| a | b | c_in | c_out | s |
|:-:|:-:|:-:|:-----:|:-:|
| 0 | 0 | 0 |   0   | 0 |
| 0 | 0 | 1 |   0   | 1 |
| 0 | 1 | 0 |   0   | 1 |
| 0 | 1 | 1 |   1   | 0 |
| 1 | 0 | 0 |   0   | 1 |
| 1 | 0 | 1 |   1   | 0 |
| 1 | 1 | 0 |   1   | 0 |
| 1 | 1 | 1 |   1   | 1 |

Regardez les colonnes et essayez de comprendre avec quelles portes on pourrait le construire.
Vous constatez que la colonne s représente la parité. On pourra donc la construire avec des portes OU-X.

- Ajoutez les deux fils qui manquent à l'entrée de la porte ET pour que le circuit se comporte comme un additionneur complet.
- Ajoutez des entrées et sorties au bloc de l'additionneur complet et vérifiez son fonctionnement.

```{logic}
:ref: adder
:height: 450
:showonly: in out and or adder
{
  "v": 4,
  "in": [
    {"pos": [70, 40], "id": 0, "name": "a", "val": 0},
    {"pos": [70, 90], "id": 1, "name": "b", "val": 0},
    {"pos": [70, 140], "id": 2, "name": "c_in", "val": 0}
  ],
  "out": [
    {"pos": [420, 60], "id": 7, "name": "s"},
    {"pos": [420, 130], "id": 26, "name": "c_out"}
  ],
  "gates": [
    {"type": "AND", "pos": [270, 120], "in": [8, 9], "out": 10},
    {"type": "AND", "pos": [220, 170], "in": [14, 15], "out": 16},
    {"type": "XOR", "pos": [170, 50], "in": [17, 18], "out": 19},
    {"type": "XOR", "pos": [290, 60], "in": [20, 21], "out": 22},
    {"type": "OR", "pos": [350, 130], "in": [23, 24], "out": 25}
  ],
  "components": [
    {"type": "adder", "pos": [140, 310], "orient": "n", "in": [27, 28, 29], "out": [30, 31]}
  ],
  "wires": [[0, 17], [1, 18], [19, 20], [2, 21], [22, 7], [19, 8], [10, 23], [16, 24], [25, 26], [2, 9]]
}
```

## Additionneur 4 bits

Pour additionner deux nombres 4-bits (quartets) nous avons besoins de 4 additionneurs complets.
Chaque sortie `C_out` est lié à la l'entrée `C_in` de l'additionneur suivant.

- Ajoutez les circuits manquants pour additionner deux nombres 4-bits.
- Montrez l'addition de 7+5 dont le résultat devrait être 12.

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

## Incrémenter (`i++`)

Additionner 1 à un nombre binaire est une opération très fréquente. Elle est utilisé pour incrémenter le compteur de programe `pc` (program counter), pour pointer à la prochaine instruction.

Completez le circuit pour incrementer la variable `i`. 
Dans beaucoup de langages de programmation une variable incrémenté est désigné par `i++`.

D'ailleur le nom du langauge de programmation C++ est une référence à cet opérateur d'incrémentation.

```{logic}
:ref: inc
:height: 400
:showonly: in out in.nibble out.nibble-display adder
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [50, 70], "id": [0, 1, 2, 3], "val": [0, 1, 1, 1]}
  ],
  "out": [
    {"type": "nibble-display", "pos": [440, 70], "id": [4, 5, 6, 7], "name": "i"},
    {"type": "nibble-display", "pos": [440, 300], "id": [56, 57, 58, 59], "name": "i++"}
  ],
  "components": [
    {"type": "adder", "pos": [390, 190], "in": [25, 26, 27], "out": [28, 29]},
    {"type": "adder", "pos": [190, 190], "in": [35, 36, 37], "out": [38, 39]},
    {"type": "adder", "pos": [90, 190], "in": [42, 43, 44], "out": [45, 46]},
    {"type": "adder", "pos": [290, 190], "in": [47, 48, 49], "out": [50, 51]}
  ],
  "wires": [[0, 4], [1, 5], [2, 6], [3, 7], [39, 44], [29, 49], [51, 37]]
}
```

## Décrémenter (`i--`)

Soustraire 1 à un nombre binaire est une opération très fréquente. Elle est utilisé pour décrémenter un compteur de boucle `i`, un pointeur de pile `sp` (stack pointer), ou un pointeur `p` vers les addresses de la mémoire.

Completez le circuit pour décrémenter la variable `i`. 
Dans beaucoup de langages de programmation une variable incrémenté est désigné par `i--`.

Astuce : pour décrémenter la valeur `i` il suffit d'additionner `1111` qui représente la valeur -1 en format signé.

```{logic}
:ref: inc
:height: 400
:showonly: in out in.nibble out.nibble-display adder
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [50, 70], "id": [0, 1, 2, 3], "val": [0, 1, 1, 1]}
  ],
  "out": [
    {"type": "nibble-display", "pos": [440, 70], "id": [4, 5, 6, 7], "name": "i"},
    {"type": "nibble-display", "pos": [440, 350], "id": [56, 57, 58, 59], "name": "i--"}
  ],
  "components": [
    {"type": "adder", "pos": [390, 240], "in": [25, 26, 27], "out": [28, 29]},
    {"type": "adder", "pos": [190, 240], "in": [35, 36, 37], "out": [38, 39]},
    {"type": "adder", "pos": [90, 240], "in": [42, 43, 44], "out": [45, 46]},
    {"type": "adder", "pos": [290, 240], "in": [47, 48, 49], "out": [50, 51]}
  ],
  "wires": [[0, 4], [1, 5], [2, 6], [3, 7], [39, 44], [29, 49], [51, 37]]
}
```

## Inverser (`-i`)

Les nombres signés sont représenté avec le format *complément à deux*.

L'opération pour trouver le nombre négatif est d'inverser toutes les bits et d'additionner 1.

Completez le circuit pour inverser le signe de la variable `i` et obtenir son négatif `-i`

```{logic}
:ref: inc
:height: 500
:showonly: in out not in.nibble out.nibble-display adder
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [50, 70], "id": [0, 1, 2, 3], "val": [0, 1, 1, 1]}
  ],
  "out": [
    {"type": "nibble-display", "pos": [440, 70], "id": [4, 5, 6, 7], "name": "i", "radix": -10},
    {"type": "nibble-display", "pos": [460, 370], "id": [56, 57, 58, 59], "name": "-i", "radix": -10}
  ],
  "gates": [
    {"type": "NOT", "pos": [90, 180], "orient": "s", "in": 61, "out": 62}
  ],
  "components": [
    {"type": "adder", "pos": [410, 260], "in": [25, 26, 27], "out": [28, 29]},
    {"type": "adder", "pos": [210, 260], "in": [35, 36, 37], "out": [38, 39]},
    {"type": "adder", "pos": [110, 260], "in": [42, 43, 44], "out": [45, 46]},
    {"type": "adder", "pos": [310, 260], "in": [47, 48, 49], "out": [50, 51]}
  ],
  "wires": [[0, 4], [1, 5], [2, 6], [3, 7], [39, 44], [29, 49], [51, 37], [62, 42], [3, 61], [45, 59]]
}
```

## Soustraction (`a-b`)

Pour soustraire deux nombres `a-b` il suffit d'additionner le nombre négatif du deuxième (`-b`).

Complétez le circuit pour soustraire `a-b`. Le resultat de 10-3 devrait être 7.

```{logic}
:ref: inc
:height: 500
:showonly: in out not in.nibble out.nibble-display adder
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [40, 100], "id": [0, 1, 2, 3], "val": [0, 1, 0, 1]},
    {"type": "nibble", "pos": [40, 210], "id": [63, 64, 65, 66], "val": [1, 1, 0, 0]}
  ],
  "out": [
    {"type": "nibble-display", "pos": [110, 100], "id": [4, 5, 6, 7], "name": "a"},
    {"type": "nibble-display", "pos": [440, 140], "id": [56, 57, 58, 59], "name": "a-b"},
    {"type": "nibble-display", "pos": [110, 210], "id": [76, 77, 78, 79], "name": "b"}
  ],
  "gates": [
    {"type": "NOT", "pos": [250, 90], "in": 86, "out": 87}
  ],
  "components": [
    {"type": "adder", "pos": [330, 110], "orient": "n", "in": [25, 26, 27], "out": [28, 29]},
    {"type": "adder", "pos": [330, 300], "orient": "n", "in": [35, 36, 37], "out": [38, 39]},
    {"type": "adder", "pos": [330, 400], "orient": "n", "in": [42, 43, 44], "out": [45, 46]},
    {"type": "adder", "pos": [330, 210], "orient": "n", "in": [47, 48, 49], "out": [50, 51]}
  ],
  "wires": [[0, 4], [1, 5], [2, 6], [3, 7], [39, 44], [29, 49], [51, 37], [28, 56], [0, 25], [63, 76], [64, 77], [65, 78], [66, 79], [87, 26], [63, 86]]
}
```

## Inversion commutée (~a)

L'inverseur commuté permet d'inverser toutes les 4 bites d'un nombre.

Ajoutez un inverseur commuté pour ouvoir obtenir `~a` ou `a` selon l'état du sélecteur.

```{logic}
:ref: inc
:height: 400
:showonly: in out in.nibble switched-inverter
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [40, 70], "id": [0, 1, 2, 3], "val": [1, 0, 0, 0]}
  ],
  "out": [
    {"type": "nibble-display", "pos": [300, 70], "id": [4, 5, 6, 7], "name": "a"},
    {"type": "nibble-display", "pos": [300, 180], "id": [22, 23, 24, 25], "name": "~a"}
  ],
  "wires": [[0, 4], [1, 5], [2, 6], [3, 7]]
}
```

## Négation commutée (`-a`)

Complétez le circuit pour pouvoir obtenir `-a` ou `a` selon l'état du sélecteur **neg**.

```{logic}
:ref: neg2
:height: 450
:showonly: in out in.nibble switched-inverter
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [40, 70], "id": [0, 1, 2, 3], "val": [0, 1, 0, 0]},
    {"pos": [70, 270], "id": 31, "name": "neg", "val": 1}
  ],
  "out": [
    {"type": "nibble-display", "pos": [160, 70], "id": [4, 5, 6, 7], "name": "a", "radix": -10},
    {"type": "nibble-display", "pos": [440, 110], "id": [56, 57, 58, 59], "name": "-a", "radix": -10}
  ],
  "components": [
    {"type": "adder", "pos": [330, 80], "orient": "n", "in": [25, 26, 27], "out": [28, 29]},
    {"type": "adder", "pos": [330, 270], "orient": "n", "in": [35, 36, 37], "out": [38, 39]},
    {"type": "adder", "pos": [330, 370], "orient": "n", "in": [42, 43, 44], "out": [45, 46]},
    {"type": "adder", "pos": [330, 180], "orient": "n", "in": [47, 48, 49], "out": [50, 51]},
    {"type": "switched-inverter", "pos": [160, 190], "in": [17, 18, 19, 20, 21], "out": [22, 23, 24, 30]}
  ],
  "wires": [[0, 4], [1, 5], [2, 6], [3, 7], [39, 44], [29, 49], [51, 37], [45, 59], [28, 56], [50, 57], [38, 58], [31, 21]]
}
```

## Soustraction commutée

Complétez le circuit pour pouvoir obtenir `a+b` ou `a-b` selon l'état du sélecteur **sub**.

```{logic}
:ref: neg2
:height: 450
:showonly: in out in.nibble switched-inverter
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [40, 60], "id": [0, 1, 2, 3], "val": [0, 1, 0, 0]},
    {"pos": [80, 340], "id": 31, "name": "sub", "val": 0},
    {"type": "nibble", "pos": [40, 170], "id": [32, 33, 34, 40], "val": [0, 0, 0, 0]}
  ],
  "out": [
    {"type": "nibble-display", "pos": [120, 60], "id": [4, 5, 6, 7], "name": "a", "radix": -10},
    {"type": "nibble-display", "pos": [440, 210], "id": [56, 57, 58, 59], "name": "a+/-b"},
    {"type": "nibble-display", "pos": [120, 170], "id": [41, 52, 53, 54], "name": "b"}
  ],
  "components": [
    {"type": "adder", "pos": [330, 70], "orient": "n", "in": [25, 26, 27], "out": [28, 29]},
    {"type": "adder", "pos": [330, 260], "orient": "n", "in": [35, 36, 37], "out": [38, 39]},
    {"type": "adder", "pos": [330, 360], "orient": "n", "in": [42, 43, 44], "out": [45, 46]},
    {"type": "adder", "pos": [330, 170], "orient": "n", "in": [47, 48, 49], "out": [50, 51]},
    {"type": "switched-inverter", "pos": [160, 270], "in": [17, 18, 19, 20, 21], "out": [22, 23, 24, 30]}
  ],
  "wires": [[0, 4], [1, 5], [2, 6], [3, 7], [39, 44], [29, 49], [51, 37], [45, 59], [28, 56], [50, 57], [38, 58], [31, 21], [32, 41], [33, 52], [34, 53], [40, 54], [32, 17], [33, 18], [34, 19], [40, 20]]
}
```

## Les fanions (flags)

Les fanions (flag) sont des signaux qui caractérisent un nombre.

- N pour indiquer que le nombre est négatif
- Z pour indiquer que le nombre est zéro

Complétez le circuit pour correctement afficher les fanions N et Z.

```{logic}
:ref: flag
:height: 400
:showonly: in out in.nibble nor4
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [40, 70], "id": [0, 1, 2, 3], "val": [1, 0, 1, 1], "name": "a"}
  ],
  "out": [
    {"type": "nibble-display", "pos": [320, 70], "id": [4, 5, 6, 7], "radix": -10},
    {"pos": [320, 190], "id": 13, "name": "Z"},
    {"pos": [320, 150], "id": 14, "name": "N"}
  ],
  "wires": [[0, 4], [1, 5], [2, 6], [3, 7]]
}
```