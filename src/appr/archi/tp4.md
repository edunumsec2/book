# TP Mémoire

Les circuits que nous avons vus jusqu'à maintenant s'appellent **circuits combinatoires**. Leur sortie est le seul résultat de leurs entrées. Une même entrée produit toujours la même sortie. Le circuit n'a pas de mémoire.

La famille de circuits que nous allons découvrir s'appelle **circuit séquentiel**.
Ces circuits permettent de mémoriser un état.

## Cellule de mémoire

Une cellule de mémoire élémentaire peut être créée avec une porte OU, ou la sortie est connectée avec une de ses entrées.

Circuit 1

- Connectez la sortie de la porte OU via la porte OUI avec une de ses entrées
- Montrez que vous avez une cellule de mémoire qui peut mémoriser une seule fois (fusible)

Circuit 2

- Connectez la sortie de la porte OU via la porte ET avec une de ses entrées
- Montrez que vous avez une cellule de mémoire qui peut mémoriser S (set) et qui peut être remis avec R (reset)

Circuit 3

- Connectez la sortie de la porte OU via la porte ET avec une de ses entrées
- Contrôlez la porte ET via une porte NON
- Mettez l'entrée R en poussoir

**Attention** : Pour éviter des effets d'oscillation, vous devez appuyer sur le bouton pressoir plus longtemps que 200 ms ou diminuer fortement le temps de propagation dans la boucle.

```{logic}
:ref: sr
:height: 500
:showonly: in out not or and
{
  "v": 4,
  "in": [
    {"pos": [50, 340], "id": 17, "name": "S", "val": 0},
    {"pos": [50, 160], "id": 29, "name": "S", "val": 0},
    {"pos": [50, 260], "id": 30, "name": "R", "val": 0},
    {"pos": [50, 40], "id": 46, "name": "S", "val": 0},
    {"pos": [50, 450], "id": 51, "name": "R", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [230, 350], "id": 5, "name": "Q"},
    {"pos": [220, 50], "id": 47, "name": "Q"},
    {"pos": [220, 170], "id": 48, "name": "Q"}
  ],
  "gates": [
    {"type": "OR", "pos": [120, 350], "in": [6, 7], "out": 8},
    {"type": "AND", "pos": [120, 220], "orient": "w", "in": [23, 24], "out": 25},
    {"type": "OR", "pos": [120, 170], "in": [26, 27], "out": 28},
    {"type": "AND", "pos": [120, 400], "orient": "w", "in": [38, 39], "out": 40},
    {"type": "BUF", "pos": [120, 90], "orient": "w", "in": 41, "out": 42},
    {"type": "OR", "pos": [120, 50], "in": [43, 44], "out": 45},
    {"type": "NOT", "pos": [120, 450], "in": 49, "out": 50}
  ],
  "wires": [[8, 5], [17, 6], [29, 26], [46, 43], [45, 47], [28, 48], [51, 49]]
}
```

## Verrou SR

Un verrou SR (set-reset) permet de "verrouiller" (mémoriser) une information.

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

La bascule D (data) recopie la donnée sur l'entrée **D** vers sa sortie **Q** à chaque front montant de l'horloge **clock**.

- ajoutez les 6 entrées/sorties à la bascule D,
- lisez et comprenez les étiquettes,
- observez et comprenez son comportement.

```{logic}
:ref: d
:height: 300
:showonly: in out
{
  "v": 4,
  "components": [
    {"type": "flipflop-d", "pos": [250, 130], "in": [0, 1, 2, 3], "out": [4, 5], "state": 0}
  ]
}
```

## Registre 4 bits

Le **registre** est un circuit qui peut mémoriser multiples bits sur un coup d'horloge. À partir de 4 bascules D, nous pouvons construire un registre pour mémoriser 4 bits.

Ajoutez les connexions qui manquent :

- Connectez chacun des 4 bits d'entrée vers une entrée **D** de la bascule.
- Connectez chacun des 4 bits de sortie **Q** vers son bit de sortie correspondante.
- Ajoutez une sortie 4 bits et un affichage 4 bits
- Connectez les 4 entrées **preset**,  **clock** et **clear**

```{logic}
:ref: d
:height: 500
:showonly: in out in.nibble out.nibble out.nibble-display flipflop-d
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [60, 190], "id": [0, 1, 2, 3], "val": [1, 0, 0, 1]},
    {"pos": [110, 420], "id": 37, "name": "clock", "val": 0, "isPushButton": true},
    {"pos": [110, 40], "id": 42, "name": "preset", "val": 0, "isPushButton": true},
    {"pos": [110, 460], "id": 43, "name": "clear", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"type": "nibble-display", "pos": [110, 190], "id": [4, 5, 6, 7]}
  ],
  "components": [
    {"type": "flipflop-d", "pos": [240, 100], "in": [8, 9, 10, 11], "out": [12, 13], "state": 0},
    {"type": "flipflop-d", "pos": [240, 200], "in": [14, 15, 16, 17], "out": [18, 19], "state": 0},
    {"type": "flipflop-d", "pos": [240, 300], "in": [20, 21, 22, 23], "out": [24, 25], "state": 0},
    {"type": "flipflop-d", "pos": [240, 400], "in": [26, 27, 28, 29], "out": [30, 31], "state": 0}
  ],
  "layout": [
    {"type": "pass-4", "pos": [350, 190], "in": [32, 33, 34, 35], "out": [36, 38, 39, 40]}
  ],
  "wires": [[0, 4], [1, 5], [2, 6], [3, 7], [1, 17], [37, 26], [18, 33]]
}
```

## Décodeur de touche

Quand on appuie sur une touche d'une calculatrice électronique, telle que la TI-30, la valeur de la touche est transformée en binaire 4 bits, enregistré dans un **registre 4 bits**, et affiché avec un affichage à 7 segments. Les étapes sont :

- une **touche** 0 - 9 est appuyé
- une conversion en **binaire** est faite
- une entrée **clock** est produite
- la valeur est mémorisée dans un **registre**
- la valeur est décodée vers les signaux a-g
- la valeur numérique est montrée sur l'**affichage** à 7 segments

Complétez le circuit pour traiter les touches 0 à 3

```{logic}
:ref: but
:height: 500
:showonly: in or or3 register decoder-7seg out.7seg
{
  "v": 4,
  "in": [
    {"pos": [50, 80], "id": 63, "name": "0", "val": 0, "isPushButton": true},
    {"pos": [50, 120], "id": 69, "name": "1", "val": 0, "isPushButton": true},
    {"pos": [50, 160], "id": 70, "name": "2", "val": 0, "isPushButton": true},
    {"pos": [50, 200], "id": 71, "name": "3", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"type": "7seg", "pos": [470, 150], "id": [12, 13, 14, 15, 16, 17, 18, 19]}
  ],
  "gates": [
    {"type": "OR", "pos": [150, 130], "in": [64, 65], "out": 66},
    {"type": "OR", "pos": [150, 190], "in": [77, 78], "out": 79},
    {"type": "OR3", "pos": [200, 300], "in": [80, 81, 82], "out": 83}
  ],
  "components": [
    {"type": "register", "pos": [310, 140], "in": [41, 42, 43, 44, 45, 46, 47], "out": [48, 49, 50, 51], "state": [1, 0, 0, 0]},
    {"type": "decoder-7seg", "pos": [390, 140], "in": [52, 53, 54, 55], "out": [56, 57, 58, 59, 60, 61, 62]}
  ],
  "labels": [
    {"pos": [50, 30], "text": "touche"},
    {"pos": [140, 30], "text": "vers binaire"},
    {"pos": [230, 30], "text": "clock"},
    {"pos": [300, 30], "text": "registre"},
    {"pos": [390, 30], "text": "décodeur"},
    {"pos": [480, 30], "text": "affichage"}
  ],
  "wires": [[48, 52], [49, 53], [50, 54], [51, 55], [56, 12], [57, 13], [58, 14], [59, 15], [60, 16], [61, 17], [62, 18], [69, 64], [71, 78], [83, 41]]
}
```

## Décodeur pour 8 touches

Complétez le circuit pour traiter les touches 0 à 7

```{logic}
:ref: but8
:height: 500
:showonly: in or or3 or4 register decoder-7seg out.7seg
{
  "v": 4,
  "in": [
    {"pos": [50, 80], "id": 63, "name": "0", "val": 0, "isPushButton": true},
    {"pos": [50, 120], "id": 69, "name": "1", "val": 0, "isPushButton": true},
    {"pos": [50, 160], "id": 70, "name": "2", "val": 0, "isPushButton": true},
    {"pos": [50, 200], "id": 71, "name": "3", "val": 0, "isPushButton": true},
    {"pos": [50, 240], "id": 89, "name": "4", "val": 0, "isPushButton": true},
    {"pos": [50, 280], "id": 90, "name": "5", "val": 0, "isPushButton": true},
    {"pos": [50, 320], "id": 91, "name": "6", "val": 0, "isPushButton": true},
    {"pos": [50, 360], "id": 92, "name": "7", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"type": "7seg", "pos": [470, 150], "id": [12, 13, 14, 15, 16, 17, 18, 19]}
  ],
  "components": [
    {"type": "register", "pos": [310, 140], "in": [41, 42, 43, 44, 45, 46, 47], "out": [48, 49, 50, 51], "state": [1, 0, 0, 0]},
    {"type": "decoder-7seg", "pos": [390, 140], "in": [52, 53, 54, 55], "out": [56, 57, 58, 59, 60, 61, 62]}
  ],
  "labels": [
    {"pos": [50, 30], "text": "touche"},
    {"pos": [140, 30], "text": "vers binaire"},
    {"pos": [230, 30], "text": "clock"},
    {"pos": [300, 30], "text": "registre"},
    {"pos": [390, 30], "text": "décodeur"},
    {"pos": [480, 30], "text": "affichage"}
  ],
  "wires": [[48, 52], [49, 53], [50, 54], [51, 55], [56, 12], [57, 13], [58, 14], [59, 15], [60, 16], [61, 17], [62, 18]]
}
```

## Compteur 4 bits

Une bascule D avec une rétroaction de la sortie inversée $\bar{Q}$ vers son entrée $D$ divise la fréquence de l'horloge par 2.  Nous avons effectivement un compteur 1 bit.

- Complétez le circuit pour construire un compteur 4 bits.
- Le circuit final doit compter de `0000` vers `1111`.
- Ajoutez un affichage 4 bits
- Connectez aussi les 4 signaux **clear** pour la remise du compteur

```{logic}
:ref: counter_
:height: 500
:showonly: in out out.nibble out.nibble-display clock flipflop-d
{
  "v": 4,
  "in": [
    {"pos": [80, 420], "id": 43, "name": "clear", "val": 0, "isPushButton": true},
    {"type": "clock", "pos": [50, 80], "id": 44, "period": 1000}
  ],
  "out": [
    {"type": "nibble", "pos": [420, 70], "id": [8, 9, 10, 11]}
  ],
  "components": [
    {"type": "flipflop-d", "pos": [210, 160], "in": [14, 15, 16, 17], "out": [18, 19], "state": 1},
    {"type": "flipflop-d", "pos": [210, 260], "in": [20, 21, 22, 23], "out": [24, 25], "state": 1},
    {"type": "flipflop-d", "pos": [210, 360], "in": [26, 27, 28, 29], "out": [30, 31], "state": 1},
    {"type": "flipflop-d", "pos": [210, 60], "in": [45, 46, 47, 48], "out": [49, 50], "state": 0}
  ],
  "layout": [
    {"type": "pass-4", "pos": [350, 70], "in": [0, 1, 2, 3], "out": [4, 5, 6, 7]}
  ],
  "wires": [[44, 45], [50, 48, {"via": [[210, 30, "w"]]}], [49, 0], [4, 8], [5, 9], [6, 10], [7, 11]]
}
```

## Compteur 8 bits

Le compteur 4 bits utilise un signal d'horloge et incrémenté à chaque coup d'horloge.
Un décodeur à 7 segments transforme les 4 signaux qui représentent un nombre binaire de 0 à 16 vers les sorties correspondant pour activer les bonnes lampes de l'affichage à 7 segments.

- Utilisez le signal de sortie V (overflow) pour faire fonctionner un deuxième compteur
- Ceci donnera un compteur 8 bit, permettant de compter de 00 à FF (255)
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
L'entrée Reset peut être utilisée pour remettre le compteur à zéro. Une porte ET détecte le nombre 6 et réinitialise le compteur.

- Ajoutez un deuxième compteur
- Configurez-le pour qu'il compte de 0 à 9
- Ajoutez le décodeur et un affichage à 7 segments
- Utilisez les deux compteurs pour faire un compteur qui affiche les nombres 00 à 59
- Diminuez la période à 1 seconde

```{logic}
:ref: counter_6
:height: 500
:showonly: in not and or clock counter out.7seg in decoder-7seg
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

## Rouler un dé

Un dé électronique utilise 7 LEDs pour afficher les points.
Une horloge rapide, liée par une porte ET vers l'entrée d'un compteur compte rapidement de 0 à 5.
À 6 le compteur est remis à 0 à l'aide d'une autre porte ET.

Voici la table de vérité pour les 7 LEDS.

| dice | bin | a,g | b,f | c,e | d |
|:----:|-----|:---:|:---:|:---:|---|
|   1  | 000 | 0   | 0   | 0   | 1 |
|   2  | 001 | 1   | 0   | 0   | 0 |
|   3  | 010 | 1   | 0   | 0   | 1 |
|   4  | 011 | 1   | 0   | 1   | 0 |
|   5  | 100 | 1   | 0   | 1   | 1 |
|   6  | 101 | 1   | 1   | 1   | 0 |

Ajoutez les portes logiques appropriées pour implémenter ce dé électronique.  
Par exemple, le signal pour lampe a,g correspond à 

`b0 or b1 or b2`

Trouvez les autres circuits et construsez ce dé électronique.

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

## Registre à décalage

Un registre de décalage propage une information d'un registre vers l'autre.

- Placez tous les entrées P (preset) et C (clear)
- Connectez la sortie Q avec l'entrée D suivante
- Connectez tous les entrées clock
- Testez le circuit à décalage

Si ça fonctionne, connectez la sortie du registre à décalage avec son entrée et connectez une entrée horloge à 1 second à l'entrée clock. Vous avez un **registre à décalage circulaire**.

```{logic}
:ref: shift
:height: 500
:showonly: in out clock flipflop-d
{
  "v": 4,
  "in": [
    {"pos": [100, 40], "orient": "s", "id": 12, "name": "P", "val": 0, "isPushButton": true},
    {"pos": [100, 180], "orient": "n", "id": 14, "name": "C", "val": 0, "isPushButton": true},
    {"pos": [70, 260], "id": 16, "name": "clock", "val": 0, "isPushButton": true}
  ],
  "components": [
    {"type": "flipflop-d", "pos": [100, 110], "in": [0, 1, 2, 3], "out": [4, 5], "state": 0},
    {"type": "flipflop-d", "pos": [220, 110], "in": [6, 7, 8, 9], "out": [10, 11], "state": 0},
    {"type": "flipflop-d", "pos": [340, 110], "in": [17, 18, 19, 20], "out": [21, 22], "state": 0},
    {"type": "flipflop-d", "pos": [460, 110], "in": [23, 24, 25, 26], "out": [27, 28], "state": 0}
  ],
  "wires": [[12, 1], [14, 2], [16, 0], [21, 26]]
}
```

## RAM (mémoire vive)

La RAM (Random Access Memory) de 16 x 4 bits permet de stocker 16 mots de 4 bits.
Les quatre bits de l'adresse **Addr** déterminent l'endroit où seront écrites les données **D**.

- **Addr** détermine l'endroit des données
- **D** signifie les données à écrire
- **Q** représente les 4 bits des données lus
- **WE** (Write Enable) permet d'écrire si 1
- **clock** transmet les données sur D en mémoire
- **Clr** (clear) remet toute la mémoire à zéro

À l'adresse `0001` (1) se trouvent déjà les données `1001`.  Ceci ressemble à des yeux.
Ajoutez d’autres valeurs pour en faire un smiley.

```{logic}
:ref: d
:height: 500
:showonly: in out.nibble-display
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

## RAM avec bits aléatoires

Le circuit suivant utilise un compteur pour créer les 16 adresses et écrire un bit aléatoire dans la RAM.

Complétez le circuit pour écrié 16 x 4 bits aléatoires dans la mémoire.

```{logic}
:ref: ram_random
:height: 500
:showonly: in.random in out  out.nibble-display ram-16x4 counter
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
:showonly: clock in out  out.nibble-display ram-16x4 counter

{
  "v": 4,
  "components": [
    {"type": "ram-16x4", "pos": [320, 110], "in": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "out": [12, 13, 14, 15], "content": ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010"]}
  ]
}

```

## RAM avec image

La mémoire peut contenir des images. Chaque bit représente un pixel.
Un des premiers jeux vidéo, **Space Invaders**,  utilise des images monocolores pour présenter des envahisseurs extraterrestres.

![invader](media/space_invader.jpg)

Remplissez la mémoire avec l'image d'un *space invader* 8x8 bits.
L'image sera alors visible dans la partie visualisation du bloc RAM 16x8 bits.

```{logic}
:ref: invader
:height: 400
:showonly: clock in out out.byte-display ram-16x8
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [170, 160], "id": [38, 39, 40, 41, 42, 43, 44, 45], "val": "01000010", "name": "data"},
    {"type": "nibble", "pos": [260, 40], "orient": "s", "id": [51, 52, 53, 54], "val": [0, 0, 0, 0], "name": "addr"}
  ],
  "out": [
    {"type": "byte-display", "pos": [390, 160], "id": [64, 65, 66, 67, 68, 69, 70, 71], "radix": 16}
  ],
  "components": [
    {"type": "ram-16x8", "pos": [260, 160], "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "out": [15, 16, 17, 18, 19, 20, 21, 22]}
  ],
  "wires": [[38, 3], [39, 4], [40, 5], [41, 6], [42, 7], [43, 8], [44, 9], [45, 10], [51, 11], [52, 12], [53, 13], [54, 14], [15, 64], [16, 65], [17, 66], [18, 67], [19, 68], [20, 69], [21, 70], [22, 71]]
}
```

## RAM avec ASCII

La mémoire peut contenir du code ASCII. Voici les codes ASCII des 6 lettres du mot `ON AIR`, exprimées en binaire et en hexadécimal.

```
O = 0b01001111 0x4f
N = 0b01001110 0x4e
  = 0b00100000 0x20
A = 0b01000001 0x41
I = 0b01001001 0x49
R = 0b01010010 0x52
```

Le circuit ci-dessous contient le mot `HELLO` en mémoire RAM. Un compteur avec une horloge 1 Hz affiche le contenu de la mémoire en boucle vers un affichage à 16 segments.

Remplacez le contenu de la mémoire pour afficher le mot `ON AIR`.

```{logic}
:ref: ascii
:height: 500
:showonly: clock in out  out.byte-display ram-16x8 counter
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [180, 320], "id": [38, 39, 40, 41, 42, 43, 44, 45], "val": "01001111", "name": "data"},
    {"pos": [150, 460], "orient": "n", "id": 114, "name": "WE (Write Enable)", "val": 1},
    {"pos": [200, 380], "id": 115, "name": "Clock (horloge)", "val": 0, "isPushButton": true},
    {"type": "clock", "pos": [90, 110], "id": 132, "period": 1000},
    {"pos": [320, 430], "orient": "n", "id": 138, "name": "C (Clear, mise à 0)", "val": 0, "isPushButton": true},
    {"pos": [200, 180], "id": 141, "name": "C (Clear, mise à 0)", "val": 0, "isPushButton": true},
    {"pos": [80, 60], "id": 146, "name": "clock", "val": 1},
    {"pos": [150, 40], "orient": "s", "id": 147, "name": "sel", "val": 1}
  ],
  "out": [
    {"type": "16seg", "pos": [560, 310], "id": [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]}
  ],
  "components": [
    {"type": "ram-16x8", "pos": [300, 320], "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "out": [15, 16, 17, 18, 19, 20, 21, 22], "content": ["01001000", "01000101", "01001100", "01001100", "01001111"]},
    {"type": "decoder-16seg", "pos": [430, 310], "in": [90, 91, 92, 93, 94, 95, 96], "out": [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]},
    {"type": "counter", "pos": [290, 180], "orient": "s", "in": [116, 117], "out": [118, 119, 120, 121, 122], "count": 1},
    {"type": "mux-2to1", "pos": [150, 100], "in": [142, 143, 144], "out": 145}
  ],
  "wires": [[38, 3], [39, 4], [40, 5], [41, 6], [42, 7], [43, 8], [44, 9], [45, 10], [97, 73], [98, 74], [99, 75], [100, 76], [101, 77], [102, 78], [103, 79], [104, 80], [105, 81], [106, 82], [107, 83], [108, 84], [109, 85], [110, 86], [111, 87], [112, 88], [113, 89], [15, 90], [16, 91], [17, 92], [18, 93], [19, 94], [20, 95], [21, 96], [114, 1], [115, 0], [118, 11], [119, 12], [120, 13], [121, 14], [138, 2], [141, 117], [132, 143], [146, 142], [147, 144], [145, 116]]
}
```
