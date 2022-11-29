# TP Circuits

Dans ce chapitre nous allons explorer les circuits logiques.

- Créez chaque circuit comme demandé
- Quand le circuit est terminé, cliquez sur **Screenshot** (dans le menu à droite)
- La capture d'écran contient le code pour réouvrir le circuit dans l'éditeur [Logic](https://logic.modulo-info.ch/)
- Déposez vos captures de circuits sur Moodle

## Transmission d'un signal

Dans ce premier exemple se trouvent une entrée (in) et une sortie (out). Les deux sont lié par un fil de transmission qui transmet un signal binaire identifié avec une couleur:

- 0 (noir)
- 1 (jaune)

Avec le menu contextuel, vous pouvez changer la couleur du fil ainsi que son délai de propagation.

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

Changez la deuxième entrée en mode **poussoir** et augmentez le délai de propagation du fil à 1000 ms. Vous verrez alors des paquets d'informations se propager le long du fil.

```{logic}
:ref: poussoir
:height: 240
:showonly: in out
{
  "v": 3,
  "in": [{"pos": [110, 30], "id": 0, "name": "comm.", "val": 0}, {"pos": [110, 80], "id": 6, "name": "poussoir", "val": 0}],
  "out": [{"pos": [460, 30], "id": 1}],
  "wires": [[0, 1, {"propagationDelay": 1000}]]
}
```

## Feu de circulation

- Cliquez sur l'entrée pour basculer l'état entre 0 et 1
- Ajoutez deux autres segments carrés pour compléter un feu de circulation.
- Changez l'affichage en grand carré
- Changez les couleurs en jaune et rouge

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
- Configurez l'horloge pour une période de 1 seconde

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
- Ajoutez les étiquettes a à g

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
- Ajoutez une entrée octet
- Connectez les deux automatiquement en alignant les broches
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

- Ajoutez un deuxième segment rouge carré qui s'allume quand la lampe verte est éteinte

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

- Ajoutez les connexions pour afficher 0 ou 1 selon le signal sur l'entrée **b0**.

```{logic}
:ref: 7seg_01
:height: 300
:showonly: in not out.7seg
{
  "v": 3,
  "in": [{"pos": [70, 150], "id": 10, "name": "high", "val": 1, "isConstant": true}, {"pos": [70, 40], "id": 8, "name": "b0", "val": 0}],
  "out": [{"type": "7seg", "pos": [470, 180], "id": [0, 1, 2, 3, 4, 5, 6, 7]}],
  "gates": [{"type": "NOT", "pos": [180, 40], "in": 12, "out": 13}],
  "wires": [[10, 1], [8, 12], [13, 0]]
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
  "in": [{"type": "clock", "pos": [110, 130], "id": 0, "period": 2000}, {"pos": [110, 40], "id": 11, "name": "high", "val": 1, "isConstant": true}],
  "out": [{"type": "7seg", "pos": [360, 90], "id": [1, 2, 3, 4, 5, 6, 7, 8]}],
  "gates": [{"type": "NOT", "pos": [180, 130], "in": 9, "out": 10}],
  "wires": [[0, 9], [11, 2], [10, 1]]
}
```

## Porte OU

Une porte OU donne une sortie 1 si **au moins une** des entrées est à 1.

Complétez le circuit pour un décodeur qui a le comportement suivant :

- bouton 1 appuyé produit la sortie binaire 01
- bouton 2 appuyé produit la sortie binaire 10
- bouton 3 appuyé produit la sortie binaire 11

```{logic}
:ref: or
:height: 400
:showonly: in out or
{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 0, "name": "1", "val": 0, "isPushButton": true},
    {"pos": [50, 80], "id": 1, "name": "2", "val": 0, "isPushButton": true},
    {"pos": [50, 130], "id": 2, "name": "3", "val": 0, "isPushButton": true}
  ],
  "gates": [{"type": "OR", "pos": [220, 40], "in": [6, 7], "out": 8}],
  "out": [{"pos": [300, 150], "orient": "s", "id": 10}, {"pos": [350, 150], "orient": "s", "id": 11}],
  "wires": [[0, 6], [2, 7], [8, 11]]
}
```

## Clavier numérique

Quand on appuie sur une touche d'une calculette électronique, en interne l'action d’appuyer le bouton est transformée en une représentation binaire de la touche appuyée.

Complétez le circuit pour une décodeur qui à le comportement suivant :

- bouton 1 appuyé produit la sortie binaire 001
- bouton 2 appuyé produit la sortie binaire 010
- bouton 3 appuyé produit la sortie binaire 011
- bouton 4 appuyé produit la sortie binaire 100
- bouton 5 appuyé produit la sortie binaire 101
- bouton 6 appuyé produit la sortie binaire 110
- bouton 7 appuyé produit la sortie binaire 111

```{logic}
:ref: or3
:height: 400
:showonly: in out or4
{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 0, "name": "1", "val": 0, "isPushButton": true},
    {"pos": [50, 70], "id": 1, "name": "2", "val": 0, "isPushButton": true},
    {"pos": [50, 110], "id": 2, "name": "3", "val": 0, "isPushButton": true},
    {"pos": [50, 150], "id": 13, "name": "4", "val": 0, "isPushButton": true},
    {"pos": [50, 190], "id": 14, "name": "5", "val": 0, "isPushButton": true},
    {"pos": [50, 230], "id": 15, "name": "6", "val": 0, "isPushButton": true},
    {"pos": [50, 270], "id": 16, "name": "7", "val": 0, "isPushButton": true}
  ],
  "out": [{"pos": [390, 290], "orient": "s", "id": 10}, {"pos": [440, 290], "orient": "s", "id": 11}, {"pos": [490, 290], "orient": "s", "id": 12}],
  "gates": [{"type": "OR4", "pos": [260, 70], "in": [21, 22, 23, 24], "out": 25}],
  "wires": [[0, 21], [2, 22], [14, 23], [16, 24], [25, 12]]
}
```

## Porte ET

Une porte ET donne une sortie 1 seulement si **toutes** les entrées sont à 1.

Complétez le circuit pour obtenir le comportement suivant :

- 00 tous les lampes éteintes
- 01 seulement la lampe rouge allumée
- 10 seulement la lampe jaune allumée
- 11 seulement la lampe verte allumée

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

Le tableau ci-dessous montre les segments à allumer pour afficher les nombres 0 à 3

| dec | b1 | b0 | a | b | c | d | e | f | g |
|-----|----|----|---|---|---|---|---|---|---|
| 0   | 0  | 0  | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 1   | 0  | 1  | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 2   | 1  | 0  | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| 3   | 1  | 1  | 1 | 1 | 1 | 1 | 0 | 0 | 1 |

- Ajoutez des portes NON et AND pour compléter le circuit

```{logic}
:ref: 7seg_0123
:height: 400
:showonly: in not or and out.7seg
{
  "v": 3,
  "in": [
    {"pos": [70, 40], "id": 8, "name": "b0", "val": 0},
    {"pos": [70, 90], "id": 9, "name": "b1", "val": 0},
    {"pos": [70, 150], "id": 10, "name": "high", "val": 1, "isConstant": true}
  ],
  "out": [{"type": "7seg", "pos": [470, 180], "id": [0, 1, 2, 3, 4, 5, 6, 7]}],
  "gates": [
    {"type": "NOT", "pos": [180, 40], "in": 12, "out": 13},
    {"type": "AND", "pos": [250, 230], "in": [14, 15], "out": 16},
    {"type": "OR", "pos": [310, 50], "in": [17, 18], "out": 19}
  ],
  "wires": [[9, 6], [10, 1], [8, 12], [13, 4], [13, 17], [9, 18], [19, 0]]
}
```

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

- Créez la porte OU et X-XOU avec seulment des portes NON-ET

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

La porte X-OU (exclusive-ou) donne 1 si un **nombre impair** d'entrées est à 1.

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
