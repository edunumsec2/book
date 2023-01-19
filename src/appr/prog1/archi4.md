# TP Mémoire

Les circuits que nous avons vus jusqu'à maintenant s'appellent circuits combinatoires.
La famille de circuits que nous allons découvrir s'appelle circuit séquentiel.
Ces circuits permettent de mémoriser un état.

## Verrou SR

Un verrou SR (set-reset) permet de mémoriser une information.

- Jouez avec le verrou SR pour comprendre son fonctionnement
- Recréez le verrou SR avec les composants NOT et OR

```{logic}
:ref: sr
:height: 500
:showonly: in out not or
{
  "v": 4,
  "in": [
    {"pos": [90, 170], "id": 20, "name": "Set", "val": 0, "isPushButton": true},
    {"pos": [90, 370], "id": 21, "name": "Reset", "val": 0, "isPushButton": true},
    {"pos": [230, 30], "id": 37, "name": "S (Set, mise à 1)", "val": 0, "isPushButton": true},
    {"pos": [230, 70], "id": 38, "name": "R (Reset, mise à 0)", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [400, 200], "id": 22, "name": "Q"},
    {"pos": [400, 320], "id": 32, "name": "Q_"},
    {"pos": [370, 30], "id": 39, "name": "Q (sortie normale)"},
    {"pos": [370, 70], "id": 40, "name": "Q̅ (sortie inversée)"}
  ],
  "gates": [
    {"type": "OR", "pos": [280, 200], "in": [17, 18], "out": 19},
    {"type": "NOT", "pos": [200, 210], "in": 30, "out": 31}
  ],
  "components": [
    {"type": "latch-sr", "pos": [300, 50], "in": [33, 34], "out": [35, 36], "state": 0}
  ],
  "wires": [[20, 17], [19, 22], [31, 18], [37, 33], [38, 34], [35, 39], [36, 40]]
}
```

## Bascule D

- ajoutez les 6 entrées/sorties à la bascule D,
- lisez et comprenez les étiquettes,
- observez et comprenez son comportement.

```{logic}
:ref: d
:height: 500
:showonly: in out
{
  "v": 4,
  "components": [
    {"type": "flipflop-d", "pos": [250, 130], "in": [0, 1, 2, 3], "out": [4, 5], "state": 0}
  ]
}
```

## Signal alternatif

Avec uniquement la bascule D, créez un circuit avec une sortie Q qui s'inverse à chaque coup d'horloge.

```{logic}
:ref: d
:height: 500
:showonly: flipflop-d
{
  "v": 4,
  "in": [
    {"pos": [190, 80], "id": 0, "name": "Clock (horloge)", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [410, 40], "id": 7, "name": "Q (sortie normale)"}
  ]
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
Un décodeur à 7 segments transforme les 4 signaux qui représentent un nombre binaire de 0 à 16 vers les sorties correspondant pour activer les bonnes lampes de l'affichage à 7 segments.

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
L'entrée Reset peut être utilisée pour remettre le compteur. Une porte ET détecte le nombre 6 et remet le compter

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

## Guirlande lumineuse

Un registre de décalage propage une information d'un registre vers l'autre.

- Ajoutez encore des bascules D
- Créez une guirlande lumineuse
- Utilisez une horloge comme entrée

```{logic}
:ref: shift
:height: 500
:showonly: in clock out.bar flipflop-d
{
  "v": 3,
  "in": [
    {"pos": [160, 70], "id": 8, "name": "D (Données)", "val": 1},
    {"pos": [200, 180], "id": 33, "name": "Clock (horloge)", "val": 0, "isPushButton": true}
  ],
  "components": [
    {"type": "flipflop-d", "pos": [250, 90], "in": [18, 19, 20, 21], "out": [22, 23], "state": 1},
    {"type": "flipflop-d", "pos": [360, 90], "in": [34, 35, 36, 37], "out": [38, 39], "state": 1},
    {"type": "flipflop-d", "pos": [470, 90], "in": [40, 41, 42, 43], "out": [44, 45], "state": 0}
  ],
  "out": [{"type": "bar", "pos": [250, 20], "id": 46, "display": "h"}],
  "wires": [[8, 21], [33, 18], [22, 37], [33, 34], [33, 40], [38, 43], [8, 46]]
}
```

## Registre à décalage

Le registre à décalage accepte une entrée D à chaque coup d'horloge.
Ici nous utilisons une entrée aléatoire (symbole du dé).

Nous utilisons un compteur pour faire une remise à chaque fois quand le compteur atteint 4.
Modifiez le circuit pour que la remise ait lieu quand le compteur atteint 8.

```{logic}
:ref: shift
:height: 500
:showonly: in clock out.shiftbuffer counter
{
  "v": 4,
  "in": [
    {"type": "clock", "pos": [30, 110], "id": 0, "period": 2000},
    {"type": "random", "pos": [160, 40], "in": 8, "out": 9}
  ],
  "out": [
    {"type": "shiftbuffer", "pos": [370, 80], "id": [10, 11, 12], "state": "000"}
  ],
  "components": [
    {"type": "counter", "pos": [150, 170], "in": [1, 2], "out": [3, 4, 5, 6, 7], "count": 3}
  ],
  "wires": [[0, 1], [9, 12], [0, 8], [0, 10], [5, 11, {"propagationDelay": 1}], [5, 2, {"propagationDelay": 1}]]
}
```

## RAM (mémoire vive)

La RAM (Random Access Memory) de 16 x 4 bits permet de stocker 16 mots de 4 bits.
Les quatre bits de l'adresse **Addr** déterminent l'endroit où seront écrites les données **D**.

À l'adresse '0001' (1) se trouvent déjà les données '1001'.  Ceci ressemble à des yeux.
Ajoutez d’autres valeurs pour en faire un smiley.

```{logic}
:ref: d
:height: 500
:showonly: in
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [130, 160], "id": [15, 16, 17, 18], "val": [1, 0, 0, 1]},
    {"type": "nibble", "pos": [280, 30], "orient": "s", "id": [23, 24, 25, 26], "val": [1, 0, 0, 0]},
    {"pos": [180, 220], "id": 27, "name": "Clock (horloge)", "val": 0, "isPushButton": true},
    {"pos": [150, 290], "orient": "n", "id": 28, "name": "WE (Write Enable)", "val": 1},
    {"pos": [340, 290], "orient": "n", "id": 29, "name": "C (Clear, mise à 0)", "val": 0, "isPushButton": true}
  ],
  "components": [
    {"type": "ram-16x4", "pos": [280, 160], "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "out": [11, 12, 13, 14], "content": ["0000", "1001"]}
  ],
  "wires": [[15, 3], [16, 4], [17, 5], [18, 6], [23, 7], [24, 8], [25, 9], [26, 10], [27, 0], [28, 1], [29, 2]]
}
```

## RAM à contenu aléatoire

Le circuit suivant utilise un compteur pour créer les 16 adresses et écrire un bit aléatoire dans la RAM.

Complétez le circuit pour écrié 16 x 4 bits aléatoires dans la mémoire.

```{logic}
:ref: ram_random
:height: 500
:showonly: in.random in out ram-4x16 counter
{
  "v": 4,
  "in": [
    {"type": "clock", "pos": [50, 60], "id": 29, "period": 2000},
    {"type": "random", "pos": [240, 120], "in": 30, "out": 31},
    {"pos": [360, 330], "orient": "n", "id": 32, "name": "WE (Write Enable)", "val": 1}
  ],
  "components": [
    {"type": "ram-16x4", "pos": [380, 220], "in": [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], "out": [18, 19, 20, 21], "content": ["0000", "0010", "0011", "0011", "0011", "0001", "0010", "0000", "0001", "0011", "0001", "0000", "0000", "0000", "0011"]},
    {"type": "counter", "pos": [370, 80], "orient": "s", "in": [22, 23], "out": [24, 25, 26, 27, 28], "count": 14}
  ],
  "wires": [[24, 14], [25, 15], [26, 16], [27, 17], [29, 22], [31, 10], [29, 30], [32, 8], [29, 7]]
}
```

## RAM avec binaire

Utilisez un compteur 4-bit pour remplir automatiquement la RAM avec les valeurs de 0 à 15.
Voici le contenu à écrire dans la RAM.

    0000
    0001
    0010
    ...
    1111

Utilisez la sortie overflow (V) du compteur pour faire une mise à zéro de la RAM, à chaque fois quand elle est pleine.
Dans l'image ci-dessous, la RAM est déjà remplie jusqu'à `1010` (10).

```{logic}
:ref: ram_counter
:height: 500
:showonly: clock in out ram-4x16 counter

{
  "v": 4,
  "components": [
    {"type": "ram-16x4", "pos": [320, 110], "in": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "out": [12, 13, 14, 15], "content": ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010"]}
  ]
}

```


