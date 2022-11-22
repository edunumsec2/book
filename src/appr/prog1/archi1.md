# TP Circuits

Dans ce chapitre nous allons explorer les circuits logiques.

- Créez chaque circuit comme demandé
- Quand le circuit est terminé, cliquez sur **Screenshot**
- La capteur d'écran contient le code pour réouvrir le circuit dans l'éditeur [Logic](https://logic.modulo-info.ch/)
- Déposez vos circuits sur Moodle

## Transmission d'un signal

Dans ce premier exemple se trouve une entrée (in) et une sortie (out). Les deux sont lié par un fil de transmission qui transmet un signal binaire identifié avec une couleur:

- 0 (noir)
- 1 (jaune)

Avec le menu contextuel vous pouvez changez la couleur du fil ainsi que son délai de propagation.

- Ajouter un deuxième fil avec un délai de propagation de 100 ms
- Ajoutez un troisième fil avec un délai de propagation de 10 ms

```{logic}
:ref: in_out
:height: 240
:showonly: in out
{
  "v": 3,
  "in": [
    {"pos": [100, 40], "id": 0, "name": "1000ms", "val": 0},
    {"pos": [100, 80], "id": 2, "name": "100ms", "val": 0},
    {"pos": [100, 120], "id": 3, "name": "10ms", "val": 1}
  ],
  "out": [{"pos": [500, 40], "id": 1}],
  "wires": [[0, 1, {"propagationDelay": 1000}]]
}
```

## Commutateur/poussoir

Les entrées ont deux modes que vous pouvez changer avec le menu contextuel:

- commutateur : bascule entre l'état 0 et 1
- poussoir : garde la valeur 1 seulement pendant qu'il est appuyé

Changez la deuxième entrée en mdoe **poussoir**

```{logic}
:ref: poussoir
:height: 240
:showonly: in out
{
  "v": 3,
  "in": [{"pos": [170, 40], "id": 0, "name": "commutateur", "val": 1}, {"pos": [170, 80], "id": 2, "name": "poussoir", "val": 1}],
  "out": [{"pos": [570, 40], "id": 1}],
  "wires": [[0, 1, {"propagationDelay": 1000}]]
}
```

## Feu de circulation

- Cliquez sur l'entrée pour basculer l'état entre 0 et 1
- Ajoutez deux autres segments carrés pour completer un feu de circulation.
- Changez l'affichage en grand carré
- Changez les coulers en jaune et rouge

```{logic}
:ref: feu
:height: 400
:showonly: in out.bar
{
  "v": 3,
  "in": [{"pos": [80, 80], "id": 0, "val": 0}],
  "out": [{"type": "bar", "pos": [280, 80], "id": 1, "display": "PX", "color": "red"}],
  "wires": [[0, 1]]
}
```

## Lampe clignotante

L'entrée horloge (clock) produit un signal qui alterne entre 0 et 1

- Ajoutez une deuxième horloge
- Ajoutez une deuxième lampe
- Configurez l'horloge pour une péridode de 1 seconde

Avec le bouton **Pause** vous pouvez arrêter l'horloge.

```{logic}
:ref: clock
:height: 400
:showonly: clock out.bar
{
  "v": 3,
  "in": [{"type": "clock", "pos": [70, 70], "id": 0, "period": 2000}],
  "out": [{"type": "bar", "pos": [220, 70], "id": 1, "display": "PX"}],
  "wires": [[0, 1]]
}
```


## Affichage à 7 segments

- Ajoutez les entrées et les lampes qui manquent pour compléter cet affichage à 7 segments.
- Ajoutez les étiquette a à g

```{logic}
:ref: 7seg
:height: 400
:showonly: in out.bar
{
  "v": 3,
  "in": [{"pos": [60, 50], "id": 0, "name": "a", "val": 1}, {"pos": [60, 90], "id": 3, "name": "b", "val": 0}],
  "out": [
    {"type": "bar", "pos": [210, 50], "id": 1, "display": "h", "name": "a"},
    {"type": "bar", "pos": [280, 120], "id": 2, "display": "v", "name": "b"},
    {"type": "bar", "pos": [280, 260], "id": 4, "display": "v", "name": "c"},
    {"type": "bar", "pos": [210, 190], "id": 5, "display": "h"}
  ],
  "wires": [[0, 1], [3, 2]]
}
```

## Affichage à 2 chiffres

Les 7 diodes lumineuses (LED) permettent d'afficher les chiffres de 0 à 9.
L'état des lampes (a-g) ainsi que du point décimal (p) est déterminé par 8 bits.

- Ajoutez un deuxième bloc affichage à 7 segments
- Ajoutez un entrée octet
- Connectez les deux autmatiquement en alignant les broches
- Configurez les entrées pour afficher le nombre 42

```{logic}
:ref: 7seg2
:height: 300
:showonly: in.byte out.7seg

{
  "v": 3,
  "out": [{"type": "7seg", "pos": [160, 70], "id": [0, 1, 2, 3, 4, 5, 6, 7]}],
  "in": [{"type": "byte", "pos": [60, 70], "id": [12, 13, 14, 15, 16, 17, 18, 19], "val": "00000110"}],
  "wires": [[12, 0], [13, 1], [14, 2], [15, 3], [16, 4], [17, 5], [18, 6], [19, 7]]
}
```

## Affichage à 16 segments

- Ajoutez une deuxième entrée à octet
- Configurez pour afficher la lettre X

```{logic}
:ref: 16seg
:height: 300
:showonly: in.byte out.16seg

{
  "v": 3,
  "out": [{"type": "16seg", "pos": [190, 70], "id": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}],
  "in": [{"type": "byte", "pos": [40, 70], "id": [17, 18, 19, 20, 21, 22, 23, 24], "val": "01100000"}],
  "wires": [[17, 0], [18, 2], [19, 4], [20, 6], [21, 8], [22, 10], [23, 12], [24, 14]]
}
```

## Porte NON

La porte NON inverse un signal.

- Ajoutez un deuxième segment rouge carré qui s'allume quand la lampe verte est étainte


```{logic}
:ref: not
:height: 400
:showonly: in not out.bar

{
  "v": 3,
  "in": [{"pos": [40, 70], "id": 0, "val": 0}],
  "gates": [{"type": "NOT", "pos": [150, 70], "in": 1, "out": 2}],
  "out": [{"type": "bar", "pos": [330, 70], "id": 3, "display": "PX"}],
  "wires": [[0, 1], [2, 3]]
}
```

## Afficher 0 et 1

La porte NON inverse un signal.

- Ajoutez les connection pour afficher 0 ou 1 selon le signal sur in

```{logic}
:ref: 7seg_01
:height: 300
:showonly: in not out.7seg
{
  "v": 3,
  "out": [{"type": "7seg", "pos": [400, 80], "id": [0, 1, 2, 3, 4, 5, 6, 7]}],
  "in": [{"pos": [80, 40], "id": 8, "name": "in", "val": 1}, {"pos": [80, 110], "id": 11, "name": "high", "val": 1}],
  "gates": [{"type": "NOT", "pos": [150, 40], "in": 9, "out": 10}],
  "wires": [[8, 9], [10, 0], [11, 1], [11, 2]]
}
```

## Alterner 0 et 1

Utilisez une horloge et une porte NON pour afficher les chiffres 0 et 1 en alternance.

```{logic}
:ref: clock_01
:height: 300
:showonly: in not out.7seg clock
{
  "v": 3,
  "in": [{"type": "clock", "pos": [110, 130], "id": 0, "period": 2000}, {"pos": [110, 40], "id": 11, "name": "high", "val": 1}],
  "out": [{"type": "7seg", "pos": [360, 90], "id": [1, 2, 3, 4, 5, 6, 7, 8]}],
  "gates": [{"type": "NOT", "pos": [180, 130], "in": 9, "out": 10}],
  "wires": [[0, 9], [11, 2], [10, 1]]
}
```

## Porte ET

Une porte ET donne une sorte 1 seulement si les deux entrées sont à 1.

```{logic}
:ref: feu_and
:height: 400
:showonly: in not and out.7seg
{
  "v": 3,
  "in": [{"pos": [60, 70], "id": 0, "name": "a", "val": 1}, {"pos": [60, 120], "id": 1, "name": "b", "val": 1}],
  "out": [
    {"type": "bar", "pos": [430, 70], "id": 2, "display": "PX", "color": "red"},
    {"type": "bar", "pos": [430, 190], "id": 3, "display": "PX", "color": "yellow"},
    {"type": "bar", "pos": [430, 310], "id": 4, "display": "PX"}
  ],
  "gates": [{"type": "AND", "pos": [280, 310], "in": [5, 6], "out": 7}, {"type": "NOT", "pos": [200, 70], "in": 8, "out": 9}],
  "wires": [[7, 4], [0, 5], [1, 6], [0, 8]]
}
```

## Décoder 0 à 3

Le tableau ci-dessous montre les segments à allumer pour afficher les nombre 0 à 3

| dec | b1 | b0 | a | b | c | d | e | f | g |
|-----|----|----|---|---|---|---|---|---|---|
| 0   | 0  | 0  | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 1   | 0  | 1  | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 2   | 1  | 0  | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| 3   | 1  | 1  | 1 | 1 | 1 | 1 | 0 | 0 | 1 |

- Ajoutez des porte NON et AND pour compléter le circuit

```{logic}
:ref: 7seg_0123
:height: 400
:showonly: in not or and out.7seg
{
  "v": 3,
  "out": [{"type": "7seg", "pos": [470, 180], "id": [0, 1, 2, 3, 4, 5, 6, 7]}],
  "in": [
    {"pos": [70, 40], "id": 8, "name": "b0", "val": 0},
    {"pos": [70, 90], "id": 9, "name": "b1", "val": 0},
    {"pos": [70, 150], "id": 10, "name": "high", "val": 1}
  ],
  "gates": [
    {"type": "NOT", "pos": [180, 40], "in": 12, "out": 13},
    {"type": "AND", "pos": [250, 230], "in": [14, 15], "out": 16},
    {"type": "OR", "pos": [310, 50], "in": [17, 18], "out": 19}
  ],
  "wires": [[9, 6], [10, 1], [8, 12], [13, 4], [13, 17], [9, 18], [19, 0]]
}
```

## Compteur 4 bits

Le compteur 4 bits utilise un signal d'horloge et incrémente à chaque coup d'horloge.
Un un décodeur à 7 segments transforme les 4 signaux qui représentent un nombre binaire de 0 à 16 vers les sorties correspondant pour activer les bonnes lampes de l'affichage à 7 segments.

- Utilisez le signal de sortie V (overflow) pour faire fonctionner un deuxième compteur


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

Pour créer une montre, un minuteur ou un alarme, nous devons compter à 60, 12 ou 24.
L'entrée Reset peut être utilisé pour remettre le compteur. Une porte ET detecte le nombre 6 et remet le compter

- Ajoutez un deuxième compteur
- Configurez-le pour qu'il compte de 0 à 9
- Ajoutez le décodeur et un affichage à 7 segments
- Utilisez les deux compteur pour faire un compteur qui affiche les nombres 00 à 59
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
