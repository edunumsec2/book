# TP Portes logiques

Dans ce chapitre, nous allons explorer les portes logiques NON, OU et ET.

- Créez chaque circuit comme demandé
- Quand le circuit est terminé, cliquez sur **Screenshot** (dans le menu à droite)
- La capture d'écran contient le code pour réouvrir le circuit dans l'éditeur [Logic](https://logic.modulo-info.ch/)
- Déposez vos captures de circuit sur Moodle

## Transmission d'un signal

Dans ce premier exemple se trouvent une entrée (in) et une sortie (out). Les deux sont liées par un fil de transmission qui transmet un signal binaire identifié par une couleur:

- 0 (noir)
- 1 (jaune)

Avec le menu contextuel (clic droit sur le fil), vous pouvez changer la couleur du fil ainsi que son délai de propagation.

- Ajoutez un deuxième fil avec un délai de propagation de 100 ms (rapide)
- Ajoutez un troisième fil avec un délai de propagation de 10 ms (instantané)
- Ajoutez un point intermédiaire au milieu du fil et déplacez-le un peu
- Mettez la couleur du fil en rouge

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

Vous pouvez ajouter des noms aux entrées sorties.

- Ajoutez une entrée *lumière*, configurez en commutateur, et reliez-la à une sortie *lampe*
- Ajoutez une entrée *sonnerie*, configurez en poussoir, et reliez-la à une sortie *alarme*

```{logic}
:ref: poussoir
:height: 240
:showonly: in out
{
  "v": 3,
  "in": [{"pos": [140, 30], "id": 0, "name": "commutateur", "val": 0}, {"pos": [140, 80], "id": 6, "name": "poussoir", "val": 0}],
  "out": [{"pos": [460, 30], "id": 1}],
  "wires": [[0, 1, {"propagationDelay": 1000}]]
}
```

## Feu de circulation

- Cliquez sur l'entrée pour basculer l'état entre 0 et 1
- Ajoutez deux autres segments carrés pour compléter un feu de circulation.
- Changez l'affichage en grand carré
- Changez les couleurs en jaune et vert
- Ajoutez les noms *rouge, jaune, vert*.

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

L'entrée horloge (clock) produit un signal qui alterne entre 0 et 1.

- Ajoutez une deuxième horloge
- Ajoutez une deuxième lampe (grand segment carré)
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

Les affichages à 7 segments permettent d'afficher des chiffres à l'aide de 7 diodes lumineuses (LED).

![LED](https://electronics-fun.com/wp-content/uploads/2020/11/Seven-segment-display.png)

- Ajoutez les entrées et les lampes qui manquent pour compléter cet affichage à 7 segments.
- Tournez la barre avec *Affichage > Barre verticale*
- Ajoutez les étiquettes a-g
- Ajoutez 7 entrées et ajoutez les étiquettes a-g
- Affichez un nombre entre 0 et 9

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

Les affichages à 16 segments permettent d'afficher aussi les lettres de l'alphabet, ainsi que des symboles de ponctuation.

- Configurez l'affichage pour afficher la lettre Y
- Ajoutez un deuxième affichage à 16 segments
- Ajoutez deux entrées 8-bits et connectez-les.
- Affichez la première lettre de votre nom

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
Montrez sa table de vérité.

- Mettez la première entrée à 0 et ajoutez une sortie
- Ajoutez une deuxième porte NON avec l'entrée à 1

Montrez l'effet de multiples portes NON.

- Mettez deux portes NON en série, ajoutez une entrée et une sortie
- Mettez trois portes NON en série, ajoutez une entrée et une sortie

```{logic}
:ref: not_
:height: 400
:showonly: in out not
{
  "v": 4,
  "in": [
    {"pos": [70, 70], "id": 0, "val": 1}
  ],
  "gates": [
    {"type": "NOT", "pos": [140, 70], "in": 1, "out": 2}
  ],
  "labels": [
    {"pos": [120, 30], "text": "table de vérité"},
    {"pos": [130, 210], "text": "multiples portes NON"}
  ],
  "wires": [[0, 1]]
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

- Montrez la table de vérité pour la porte OU.
- Ajoutez 3 portes OU et mettez les entrées à 01, 10, et 11
- Créez une porte OU avec 3 entrées

```{logic}
:ref: or
:height: 400
:showonly: in out or
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
    {"type": "OR", "pos": [110, 70], "in": [4, 5], "out": 6}
  ],
  "labels": [
    {"pos": [110, 20], "text": "table de vérité"},
    {"pos": [390, 20], "text": "porte OU avec 3 entrées"}
  ],
  "wires": [[7, 4], [8, 5], [6, 9]]
}
```

## Décodeur de clavier

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

Complétez le circuit pour un décodeur qui a le comportement suivant :

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

- Montrez la table de vérité pour la porte ET.
- Ajoutez 3 portes ET et mettez les entrées à 01, 10, et 11
- Créez une porte ET avec 3 entrées

```{logic}
:ref: and
:height: 400
:showonly: in out and
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
    {"type": "AND", "pos": [110, 70], "in": [4, 5], "out": 6}
  ],
  "labels": [
    {"pos": [110, 20], "text": "table de vérité"},
    {"pos": [390, 20], "text": "porte ET avec 3 entrées"}
  ],
  "wires": [[7, 4], [8, 5], [6, 9]]
}
```

## Décodeur binaire

Complétez le circuit pour créer un décodeur binaire. Chaque combinaison des deux entrées binaires allume une et une seule des 4 lampes.

- 00 allume seulement lampe 0
- 01 allume seulement lampe 1
- 10 allume seulement lampe 2
- 11 allume seulement lampe 3

```{logic}
:ref: 2bit-decoder
:height: 450
:showonly: in not and out.bar
{
  "v": 4,
  "in": [
    {"pos": [70, 60], "id": 0, "name": "b0", "val": 0},
    {"pos": [70, 110], "id": 1, "name": "b1", "val": 0}
  ],
  "out": [
    {"type": "bar", "pos": [460, 70], "id": 10, "display": "PX", "name": "0"},
    {"type": "bar", "pos": [460, 270], "id": 11, "display": "PX", "name": "2"},
    {"type": "bar", "pos": [460, 170], "id": 12, "display": "PX", "name": "1"},
    {"type": "bar", "pos": [460, 370], "id": 13, "display": "PX", "name": "3"}
  ],
  "gates": [
    {"type": "NOT", "pos": [140, 60], "in": 2, "out": 3},
    {"type": "NOT", "pos": [140, 110], "in": 4, "out": 5},
    {"type": "AND", "pos": [350, 70], "in": [6, 7], "out": 8}
  ],
  "wires": [[0, 2], [1, 4], [8, 10], [3, 6], [5, 7]]
}
```

## Décodeur de dé

Un dé de jeu peut afficher les nombres 1 à 6 à l'aide de 7 lampes.  
Plusieurs lampes s'allument par paire. Voici la table de vérité.

| b2 | b1 | b0 |valeur| a,g | b,f | c,e | d |
|----|----|:--:|:----:|:---:|:---:|:---:|---|
| 0  | 0  | 0  |      |  0  |  0  |  0  | 0 |
| 0  | 0  | 1  | 1    |  0  |  0  |  0  | 1 |
| 0  | 1  | 0  | 2    |  1  |  0  |  0  | 0 |
| 0  | 1  | 1  | 3    |  1  |  0  |  0  | 1 |
| 1  | 0  | 0  | 4    |  1  |  0  |  1  | 0 |
| 1  | 0  | 1  | 5    |  1  |  0  |  1  | 1 |
| 1  | 1  | 0  | 6    |  1  |  1  |  1  | 0 |
| 1  | 1  | 1  |      |  1  |  1  |  1  | 1 |

Utilisez des portes logiques OU et ET pour créer le circuit de décodage pour afficher les lampes qui correspondent aux nombres 1 à 6.

Le nombre binaire $b_2 b_1 b_0$ doit allumer les lampes a-g pour afficher ce nombre dans la façon d'un dé à jeu standard.

```{logic}
:ref: dice
:height: 300
:showonly: in and or out.bar
{
  "v": 4,
  "opts": {"propagationDelay": 10},
  "in": [
    {"pos": [60, 40], "id": 7, "name": "b0", "val": 1},
    {"pos": [60, 80], "id": 8, "name": "b1", "val": 0},
    {"pos": [60, 120], "id": 26, "name": "b2", "val": 1}
  ],
  "out": [
    {"type": "bar", "pos": [380, 30], "id": 0, "display": "px", "name": "a"},
    {"type": "bar", "pos": [380, 70], "id": 1, "display": "px", "name": "b"},
    {"type": "bar", "pos": [430, 70], "orient": "s", "id": 2, "display": "px", "name": "d"},
    {"type": "bar", "pos": [380, 120], "id": 3, "display": "px", "name": "c"},
    {"type": "bar", "pos": [480, 70], "id": 4, "display": "px", "name": "f"},
    {"type": "bar", "pos": [480, 30], "id": 5, "display": "px", "name": "e"},
    {"type": "bar", "pos": [480, 120], "id": 6, "display": "px", "name": "g"}
  ]
}
```

## Décoder 0 à 3

Le tableau ci-dessous montre les segments à allumer pour afficher les nombres 0 à 3 d'un affichage à 7 segments.

| dec | b1 | b0 | a | b | c | d | e | f | g |
|-----|----|----|---|---|---|---|---|---|---|
| 0   | 0  | 0  | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 1   | 0  | 1  | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 2   | 1  | 0  | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| 3   | 1  | 1  | 1 | 1 | 1 | 1 | 0 | 0 | 1 |

Ajoutez des portes NON, OR, et AND pour compléter le circuit

**Astuce** - Essayez de trouver le circuit logique pour chaque colonne.
C'est-à-dire il faut trouver le circuit pour allumer le segment.
Par exemple pour le segment a vous avez la table de vérité suivante.

| b1 | b0 | a |
|----|----|---|
| 0  | 0  | 1 |
| 0  | 1  | 0 |
| 1  | 0  | 1 |
| 1  | 1  | 1 |

Certaines colonnes sont identiques.  
Donc vous pouvez utiliser le même signal.

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

Pour ce dernier circuit, faites une capture d'écran pour chacune des 4 conditions.
