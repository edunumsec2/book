# TP mémoire

Les circuits que nous avons vus jusqu'à maintenant s'appellent circuits combinatoires.
La famille de circuits que nous allons découvrir s'appelle circuit séquentiel.
Ces circuits permettent de mémoriser un état.

Mais tout d'abord, nous commençons avec une petite révision des portes logiques.


## Loi de Morgan

La **loi de Morgan** dit qu'une porte ET peut être fabriquée avec une porte OU et des inverseurs.

Créez une porte ET en utilisant des portes OU et NON.

```{logic}
:ref: morgan
:height: 300
:showonly: in out not or
{

}
```

Créez une porte OU en utilisant des portes ET et NON.

```{logic}
:ref: morgan
:height: 300
:showonly: in out not and
{

}
```

## La porte NAND

Avec la porte NON-ET (NAND) on peut en principe créer toutes les autres portes logiques de base (NON, ET, OU, X-OU).

- Créez la porte OU et X-XOU avec seulement des portes NON-ET

```{logic}
:ref: nand
:height: 500
:showonly: in out nand
{
  "v": 3,
  "gates": [
    {"type": "NAND", "pos": [160, 50], "in": [20, 21], "out": 22},
    {"type": "NAND", "pos": [160, 140], "in": [27, 28], "out": 29},
    {"type": "NAND", "pos": [270, 140], "in": [30, 31], "out": 32}
  ],
  "in": [{"pos": [60, 50], "id": 23, "val": 0}, {"pos": [60, 120], "id": 25, "val": 0}, {"pos": [60, 160], "id": 26, "val": 0}],
  "out": [{"pos": [230, 50], "id": 24, "name": "NON"}, {"pos": [340, 140], "id": 33, "name": "ET"}],
  "wires": [[23, 20], [23, 21], [22, 24], [25, 27], [26, 28], [29, 30], [29, 31], [32, 33]]
}
```

## La porte X-OU

La porte X-OU (exclusive ou) donne 1 si un **nombre impair** d'entrées est à 1.

Dans le schéma ci-dessous, on peut allumer la lumière d'une chambre à partir de la porte d'entrée et de la cuisine.

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


