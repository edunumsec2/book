# TP ALU

L'unité arithmétique et logique (ALU) permet de choisir parmi un certain nombre d'opérations. Nous allons voir comment une ALU peut choisir entre différentes opérations (ET, OU, addition, soustraction) à l'aide d'un **multiplexeur**.

Nous allons découvrir comment des décalages et additions successives peuvent constituer une **multiplication** ou une **division**.

Finalement, un **registre** permet de mémoriser les opérandes du calcul. Un registre particulier appelé **accumulateur** permet de faire des additions successives et *accumuler* une somme courante.

## Sélectionneur

L'entrée **sel** du sélectionneur permet de choisir entre deux signaux d'entrée :

- entrée 0 : signal lent (période de 2 s)
- entrée 1 : signal rapide (période de 250 ms)

Recréez un tel sélecteur avec des portes NON, ET, OU.

```{logic}
:ref: mux
:height: 500
:showonly: in out clock not and or
{
  "v": 4,
  "in": [
    {"type": "clock", "pos": [100, 120], "id": 73, "name": "entrée 1", "period": 250},
    {"type": "clock", "pos": [100, 30], "id": 81, "name": "entrée 0", "period": 2000},
    {"pos": [200, 130], "orient": "n", "id": 82, "name": "sel", "val": 1},
    {"pos": [110, 400], "orient": "n", "id": 91, "name": "sel", "val": 1}
  ],
  "out": [
    {"pos": [450, 70], "id": 74, "name": "sortie"},
    {"pos": [450, 260], "id": 92, "name": "sortie"}
  ],
  "gates": [
    {"type": "AND", "pos": [250, 230], "in": [83, 84], "out": 85},
    {"type": "AND", "pos": [250, 300], "in": [86, 87], "out": 88},
    {"type": "NOT", "pos": [170, 310], "in": 89, "out": 90}
  ],
  "components": [
    {"type": "mux-2to1", "pos": [200, 70], "in": [51, 52, 53], "out": 54}
  ],
  "wires": [[73, 52], [54, 74, {"propagationDelay": 1000}], [81, 51], [82, 53], [90, 87], [91, 89]]
}
```

## Multiplexeur

Le multiplexeur (MUX) permet de choisir entre deux signaux 4-bits nommés a et b.
Ajoutez les éléments qui manquent.

- Ajoutez une deuxième entrée 4-bits avec un affichage.
- Ajoutez un décodeur et affichage à 7 segments.

```{logic}
:ref: mux
:height: 450
:showonly: in in.nibble out.nibble out.nibble-display decoder-7seg out.7seg
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [50, 100], "id": [33, 34, 35, 36], "val": [1, 0, 1, 0], "name": "a"}
  ],
  "out": [
    {"type": "nibble-display", "pos": [120, 100], "id": [37, 38, 39, 40]}
  ],
  "components": [
    {"type": "mux-8to4", "pos": [220, 150], "in": [20, 21, 22, 23, 24, 25, 26, 27, 28], "out": [29, 30, 31, 32]}
  ],
  "wires": [[33, 20], [34, 21], [35, 22], [36, 23], [33, 37], [34, 38], [35, 39], [36, 40]]
}
```

## Sélection d'opérations

Complétez le circuit qui permet de sélectionner entre les deux opérations `a ET b` et `a OU b`.

- Connectez a et b aux entrées des 4 portes OU,
- Ajoutez une sorie 4-bits pour afficher le résultat des opérations logiques
- Ajoutez une entrée de sélection pour le multiplexeur.

```{logic}
:ref: mux
:height: 450
:showonly: in out.nibble-display out.nibble quad-gate
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [50, 70], "id": [24, 25, 26, 27], "val": [0, 1, 0, 0], "name": "a"},
    {"type": "nibble", "pos": [50, 170], "id": [28, 29, 30, 31], "val": [0, 0, 0, 0], "name": "b"}
  ],
  "out": [
    {"type": "nibble", "pos": [410, 170], "id": [57, 58, 59, 60], "name": "a ET/OU b"}
  ],
  "components": [
    {"type": "quad-gate", "subtype": "AND", "pos": [200, 120], "in": [3, 4, 5, 6, 7, 8, 9, 10], "out": [11, 12, 13, 14]},
    {"type": "quad-gate", "subtype": "OR", "pos": [200, 330], "in": [32, 33, 34, 35, 36, 37, 38, 39], "out": [40, 41, 42, 43]},
    {"type": "mux-8to4", "pos": [320, 170], "in": [44, 45, 46, 47, 48, 49, 50, 51, 52], "out": [53, 54, 55, 56]}
  ],
  "wires": [[24, 3], [25, 4], [26, 5], [27, 6], [28, 7], [29, 8], [30, 9], [31, 10], [11, 44], [12, 45], [13, 46], [14, 47], [53, 57], [54, 58], [55, 59], [56, 60]]
}
```

Un clic droit sur la porte quadruple permet de choisir son type (AND, OR, XOR, NAND, NOR, XNOR).

## ALU

L'unité arithmétique et logique, ALU (arithmetic and logic unit), est la partie de l'ordinateur qui effectue les différents calculs arithmétiques et logiques.

Ci-dessous vous pouvez voir les circuits logiques d'une ALU 4-bits très utilisée dans les années 60 et 70, le modèle 74181.

![ALU](https://upload.wikimedia.org/wikipedia/commons/c/c0/74181aluschematic.png)

L'ALU dont nous disposons peut effectuer 4 opérations :

- addition (00)
- soustraction (01)
- OU logique (10)
- ET logique (11)

Avec l'ALU ci-dessous, ajoutez

- la deuxième entrée (B) avec un bloc d'affichage 4 bits
- un bloc d'affichage 4 bits pour la sortie (S)
- les 3 entrées (Cin, Op0, Op1)
- les 3 sorties (Cout, V, Z)

Ensuite, testez les 4 opérations. Montrez une soustraction.

```{logic}
:ref: alu
:height: 400
:showonly: in out in.nibble out.nibble out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [40, 150], "id": [72, 73, 74, 75], "val": [1, 0, 1, 0]}
  ],
  "out": [
    {"type": "nibble-display", "pos": [340, 200], "id": [68, 69, 70, 71]},
    {"type": "nibble-display", "pos": [130, 150], "id": [80, 81, 82, 83]}
  ],
  "components": [
    {"type": "alu", "pos": [230, 200], "in": [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], "out": [62, 63, 64, 65, 92, 67, 66]}
  ],
  "wires": [[62, 68], [63, 69], [64, 70], [65, 71], [72, 51], [73, 52], [74, 53], [75, 54], [72, 80], [73, 81], [74, 82], [75, 83]]
}
```

## Addition signée

Interprétez les nombres binaires comme des nombres signés. Vous pouvez configurer l'afficheur 4 bits avec son menu contextuel. Complétez l'additionneur 4-bit et montrez que l'addition de -2 et -3 donne bien -5.

```{logic}
:ref: addsigned
:height: 400
:showonly: alu in out in.nibble out.nibble-display
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

## Addition 8 bits

Pour additionner un nombre à 8-bits, il faut combiner deux ALU 4-bits. Dans ce cas il faut connecter Cout de la première ALU avec Cin de la deuxième.

- Complétez le circuit pour afficher l'addition de deux nombres binaires 8-bits.
- Ajoutez une entrée pour soustraire deux nombres.
- Montrez une soustraction correcte, dont le résultat est plus grand que 30

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

## Carry et Overflow (V)

L'ALU possède deux sorties pour indiquer un dépassement de plage de résultat. Le résultat affiché est alors décalé de 16.  Ce cas est signalé par l'ALU à l'aide de deux signaux de sortie spéciaux.

- C (carry) signale un dépassement pour des nombres non signés,
- V (overflow) signale un dépassement pour des nombres signés.

L'addition de deux nombres naturels (0 à 15) peut produire un résultat de 0 à 30.  
L'addition de deux nombres relatifs (-8 à 7) peut produire un résultat de -16 à 14.  
Dans certains cas on aura donc besoin de 5 bits pour représenter correctement le résultat.

```{figure} media/4bits_Integers.svg
:width: 100%
```

Pour les nombres non signés (première ALU)

- Choisissez des valeurs a et b qui produisent un dépassement (C = 1), et donc un affichage incorrect sur une sortie de 4 bits.
- Ajoutez en plus un affichage 8 bits et connectez-y les 4 bits de S et C comme 5e bit, pour afficher le résultat correct.

Pour les nombres signés (deuxième ALU)

- Ajoutez 2 entrées 4 bits et 1 sortie 4 bits.
- Ajoutez 3 affichages 4 bits configurés (via menu contextuel) en nombres signés.
- Choisissez des valeurs a et b négatives qui produisent un dépassement (V = 1).
- Ajoutez un affichage 8 bits configuré (via le menu contextuel) en nombres signés, et connectez-y les 4 bits de S et C comme 5e bit.

**Attention** : Dans ce cas vous devez connecter C également avec les 3 autres bits (b5-b7) pour faire une propagation du bit de signe et traiter correctement le cas des nombres négatifs.

```{logic}
:ref: overflow
:height: 600
:showonly: alu in out in.nibble out.nibble out.nibble-display out.byte-display
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [50, 90], "id": [18, 19, 20, 21], "val": [1, 0, 0, 0], "name": "a"},
    {"type": "nibble", "pos": [50, 190], "id": [26, 27, 28, 29], "val": [0, 1, 0, 0], "name": "b"}
  ],
  "out": [
    {"type": "nibble-display", "pos": [100, 90], "id": [22, 23, 24, 25]},
    {"type": "nibble-display", "pos": [100, 190], "id": [30, 31, 32, 33]},
    {"type": "nibble", "pos": [290, 140], "id": [35, 36, 37, 38]},
    {"type": "nibble-display", "pos": [370, 140], "id": [39, 40, 41, 42]},
    {"pos": [290, 250], "id": 43, "name": "Cout (retenue de sortie)"},
    {"pos": [240, 560], "id": 83, "name": "V (oVerflow)"}
  ],
  "components": [
    {"type": "alu", "pos": [180, 140], "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "out": [11, 12, 13, 14, 15, 16, 17]},
    {"type": "alu", "pos": [190, 420], "in": [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], "out": [55, 56, 57, 58, 59, 60, 61]}
  ],
  "labels": [
    {"pos": [130, 20], "text": "nombres non signés"},
    {"pos": [100, 290], "text": "nombres signés"}
  ],
  "wires": [[18, 0], [19, 1], [20, 2], [21, 3], [18, 22], [19, 23], [20, 24], [21, 25], [26, 4], [27, 5], [28, 6], [29, 7], [26, 30], [27, 31], [28, 32], [29, 33], [11, 35], [12, 36], [13, 37], [14, 38], [11, 39], [12, 40], [13, 41], [14, 42], [17, 43], [59, 83]]
}
```

## Multiplier 1x1 bit

Les règles de la multiplication 1-bit sont très simples. Voici la table de vérité.

| a | b | a x b |
|---|---|:-----:|
| 0 | 0 |   0   |
| 0 | 1 |   0   |
| 1 | 0 |   0   |
| 1 | 1 |   1   |

On voit tout de suite que ceci correspond à la porte ET.
Dans l'exemple si dessous vous voyez une porte ET pour multiplier a et b, les deux ayant juste 1 bit.

- Vérifiez le bon fonctionnement du multiplicateur 1-bit
- Ensuite, utilisez 4 portes ET pour créer un multiplicateur **a** (4-bits) fois **b** (1-bit).
- Basculez b entre 0 et 1 pour vérifier si votre circuit fonctionne correctement.

```{logic}
:ref: mul1
:height: 400
:showonly: in and in.nibble out.nibble-display
{
  "v": 4,
  "in": [
    {"pos": [70, 50], "id": 0, "name": "a", "val": 1},
    {"pos": [70, 70], "id": 4, "name": "b", "val": 0},
    {"type": "nibble", "pos": [70, 200], "id": [6, 7, 8, 9], "val": [0, 0, 1, 0], "name": "a"},
    {"pos": [70, 290], "id": 10, "name": "b", "val": 1}
  ],
  "out": [
    {"pos": [210, 60], "id": 5, "name": "a x b"},
    {"type": "nibble-display", "pos": [350, 200], "id": [11, 12, 13, 14], "name": "a x b"}
  ],
  "gates": [
    {"type": "AND", "pos": [140, 60], "in": [1, 2], "out": 3}
  ],
  "wires": [[0, 1], [4, 2], [3, 5]]
}
```

## Multiplier par 2, 4, 8

La multiplication par une puissance de 2 est facile. Il suffit de décaler les bits.
Le circuit ci-dessous calcule 2a en décalant d'un bit en direction du poids fort.

- Complétez le circuit pour calculer et afficher 4a et 8a.
- Vérifiez avec a=5. Votre affichage devrait montrer 10, 20 et 40.

```{logic}
:ref: mul2
:height: 400
:showonly: in.nibble out.nibble-display out.byte-display
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [40, 60], "id": [0, 1, 2, 3], "val": [1, 1, 0, 0], "name": "a"}
  ],
  "out": [
    {"type": "byte-display", "pos": [220, 60], "id": [4, 5, 6, 7, 8, 9, 10, 11], "name": "2a"},
    {"type": "nibble-display", "pos": [90, 60], "id": [12, 13, 14, 15]},
    {"type": "byte-display", "pos": [220, 160], "id": [16, 17, 18, 19, 20, 21, 22, 23], "name": "4a"},
    {"type": "byte-display", "pos": [220, 260], "id": [24, 25, 26, 27, 28, 29, 30, 31], "name": "8a"}
  ],
  "wires": [[0, 12], [1, 13], [2, 14], [3, 15], [0, 5], [1, 6], [2, 7], [3, 8]]
}
```

## Multiplier 1x4 bit

Le circuit ci-dessous utilise un multiplexeur 8x4 pour faire la multiplication d'un nombre **a** (4 bits) avec un nombre **b** (1 bit), au lieu des 4 portes ET utilisées précédemment.

Nous pouvons représenter un nombre binaire **b** par une séquence de 4 chiffres binaires : $b_3 b_2 b_1 b_0$.
Chaque bit $b_i$ contrôle la multiplication de son poids ($2^i$) avec $a$.

- $b_0 \cdot 2^0 a$
- $b_1 \cdot 2^1 a$
- $b_2 \cdot 2^2 a$
- $b_3 \cdot 2^3 a$

Pour compléter l'opération de multiplication 4x4 bits, la dernière étape sera d'additionner les 4 nombres.

Complétez le circuit avec :

- deux entrées que vous appelez **b2** et **b3**
- un affichage 8 bits qui affiche 4a sous contrôle de b2
- un affichage 8 bits qui affiche 8a sous contrôle de b3

Essayer de multiplier deux nombres, par exemple a=5 et b=5 (0101). Vous trouvez le résultat de la multiplication en additionnant les 4 nombres affichés.

```{logic}
:ref: mul3
:height: 450
:showonly: in in.nibble out.nibble-display out.byte-display mux-8to4
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [40, 230], "id": [0, 1, 2, 3], "val": [1, 0, 1, 0], "name": "a"},
    {"pos": [460, 50], "orient": "s", "id": 39, "name": "b0", "val": 1},
    {"pos": [350, 50], "orient": "s", "id": 108, "name": "b1", "val": 1}
  ],
  "out": [
    {"type": "nibble-display", "pos": [90, 230], "id": [49, 50, 51, 52]},
    {"type": "byte-display", "pos": [590, 360], "id": [4, 5, 6, 7, 8, 9, 10, 11]},
    {"type": "byte-display", "pos": [480, 360], "id": [12, 13, 14, 15, 16, 17, 18, 19]}
  ],
  "components": [
    {"type": "mux-8to4", "pos": [150, 180], "in": [22, 23, 24, 25, 26, 27, 28, 29, 30], "out": [31, 32, 33, 34]},
    {"type": "mux-8to4", "pos": [240, 180], "in": [53, 54, 55, 56, 57, 58, 59, 60, 61], "out": [62, 63, 64, 65]},
    {"type": "mux-8to4", "pos": [350, 180], "in": [75, 76, 77, 78, 79, 80, 81, 82, 83], "out": [84, 85, 86, 87]},
    {"type": "mux-8to4", "pos": [460, 180], "in": [95, 96, 97, 98, 99, 100, 101, 102, 103], "out": [104, 105, 106, 107]}
  ],
  "wires": [[0, 26], [1, 27], [2, 28], [3, 29], [0, 49], [1, 50], [2, 51], [3, 52], [0, 57], [1, 58], [2, 59], [3, 60], [0, 79], [1, 80], [2, 81], [3, 82], [0, 99], [1, 100], [2, 101], [3, 102], [39, 103], [108, 83], [104, 4], [105, 5], [106, 6], [107, 7], [84, 13], [85, 14], [86, 15], [87, 16]]
}
```

## Multiplier 4x4 bits

La multiplication 4 x 4 bits nécessite:

- 4 multiplexeurs  pour la multiplication 4 x 1 bit
- 3 additionneurs pour additionner les 4 opérandes décalés

Pour multiplier `0101` x `1001` = `00101101`  (5 x 9 = 45) nous écrivons en colonnes ceci :

```text
1     1001
0    0000
1   1001
0 +0000
----------
  00101101
```

Cet algorithme peut être exprimé mathématiquement comme

$$ produit = \sum^4_{i=0} (b_i \cdot a) \cdot 2^i $$

Modifiez a et b dans le circuit multiplicateur 4 x 4 bits ci-dessus vérifiez que vous obtenez bien le produit de a et b. Faites une capture d'écran avec la plus grande valeur possible.

```{logic}
:ref: mul4
:height: 855
:showonly: in in.nibble out.nibble-display out.byte-display mux-8to4 alu

{ // JSON5
  v: 6,
  opts: {zoom: 90},
  components: {
    in0: {type: 'in', pos: [615, 45], orient: 's', id: '19-22', name: 'a', bits: 4, val: '1001'},
    in1: {type: 'in', pos: [110, 45], orient: 's', id: '23-26', name: 'b', bits: 4, val: '0101'},
    disp0: {type: 'display', pos: [450, 790], orient: 's', id: '115-122', bits: 8},
    disp1: {type: 'display', pos: [35, 95], orient: 'w', id: '141-144'},
    disp2: {type: 'display', pos: [695, 95], id: '145-148'},
    alu0: {type: 'alu', pos: [575, 385], orient: 's', in: '123-133', out: '134-140'},
    alu1: {type: 'alu', pos: [505, 515], orient: 's', in: '162-172', out: '173-179'},
    alu2: {type: 'alu', pos: [435, 650], orient: 's', in: '205-215', out: '216-222'},
    mux0: {type: 'mux', pos: [645, 200], orient: 's', in: '0-8', out: '9-12', from: 8, to: 4, bottom: true},
    mux1: {type: 'mux', pos: [500, 260], orient: 's', in: ['13-18', '27-29'], out: '30-33', from: 8, to: 4, bottom: true},
    mux2: {type: 'mux', pos: [355, 385], orient: 's', in: '34-42', out: '43-46', from: 8, to: 4, bottom: true},
    mux3: {type: 'mux', pos: [245, 510], orient: 's', in: '47-55', out: '56-59', from: 8, to: 4, bottom: true},
  },
  wires: [[19, 4], [20, 5], [21, 6], [22, 7], [19, 17, {via: [[645, 115, 'w'], [480, 115, 'w']]}], [20, 18, {via: [[625, 95, 'w'], [460, 95, 'w']]}], [21, 27, {via: [[605, 80, 'w'], [440, 80, 'w']]}], [22, 28, {via: [[420, 65, 'w']]}], [30, 127], [31, 128], [32, 129], [33, 130], [10, 123], [11, 124], [12, 125], [24, 29, {via: [[150, 260]]}], [9, 115, {via: [[685, 250, 's'], [685, 690, 's']]}], [134, 116, {via: [[630, 465, 's'], [630, 690, 's']]}], [23, 141], [24, 142], [25, 143], [26, 144], [19, 145], [20, 146], [21, 147], [22, 148], [19, 38, {via: [[645, 115, 'w'], [335, 115, 'w']]}], [20, 39, {via: [[625, 95, 'w'], [315, 95, 'w']]}], [21, 40, {via: [[605, 80, 'w'], [295, 80, 'w']]}], [22, 41, {via: [[275, 65, 'w']]}], [135, 162], [136, 163], [137, 164], [43, 166], [44, 167], [45, 168], [46, 169], [25, 42, {via: [[150, 385]]}], [173, 117, {via: [[555, 585, 's'], [555, 690, 's']]}], [140, 165, {via: [[465, 365, 's'], [465, 435, 's'], [525, 435, 's']]}], [174, 205], [175, 206], [176, 207], [56, 209], [57, 210], [58, 211], [59, 212], [19, 51, {via: [[645, 115, 'w'], [225, 115, 'w']]}], [20, 52, {via: [[625, 95, 'w'], [205, 95, 'w']]}], [21, 53, {via: [[605, 80, 'w'], [185, 80, 'w']]}], [22, 54, {via: [[165, 65, 's']]}], [179, 208, {via: [[395, 495, 's'], [395, 565, 's'], [455, 565, 's']]}], [216, 118], [217, 119], [218, 120], [219, 121], [222, 122, {via: [[325, 630, 's'], [325, 690, 's']]}], [26, 55, {via: [[150, 510]]}], [23, 8, {via: [[150, 200]]}]]
}
```

## Diviser par 2, 4 et 8

La division par une puissance de 2 est très simple. Il suffit de décaler le nombre binaire. Pour diviser par 2 nous décalons d'une unité, et nous obtenons :

- La division entière (`a // 2`)
- Le reste de la division, l'opération modulo (`a % 2`)

Ajoutez deux affichages 8 bits pour la division par 4 et 8
Ajoutez deux affichages 4 bits pour le modulo 4 et 8
Ajoutez les étiquettes (`a % 4`, `a // 4`, etc.)

Par exemple pour `43 // 8` vous devriez obtenir 5,  
et pour `43 % 8` vous devriez obtenir 3.

```{logic}
:ref: div
:height: 400
:showonly: in out, in.byte out.nibble-display out.byte-display
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [40, 160], "id": [0, 1, 2, 3, 4, 5, 6, 7], "val": "00101011", "name": "a"}
  ],
  "out": [
    {"type": "byte-display", "pos": [130, 160], "id": [8, 9, 10, 11, 12, 13, 14, 15]},
    {"type": "nibble-display", "pos": [220, 60], "id": [20, 21, 22, 23], "name": "a%2"},
    {"type": "byte-display", "pos": [230, 170], "id": [24, 25, 26, 27, 28, 29, 30, 31], "name": "a//2"}
  ],
  "wires": [[0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15], [0, 20], [1, 24], [2, 25], [3, 26], [4, 27], [5, 28], [6, 29], [7, 30]]
}
```

## Registre

Le registre que nous allons voir plus en détail dans le prochain chapitre permet de mémoriser une donnée.
Avec un coup d'horloge (clock), les 4-bits de données sont mémorisés.

Ajoutez un deuxième registre, décodeur et affichage à 7 segments, pour permettre d'afficher un nombre décimal de 00 à 99 ou un nombre hexadécimal de 00 à FF.

```{logic}
:ref: reg
:height: 500
:showonly: in in.nibble register decoder-7seg out.7seg
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [50, 130], "id": [11, 12, 13, 14], "val": [1, 0, 0, 0]},
    {"pos": [100, 310], "id": 15, "name": "clock", "val": 0, "isPushButton": true},
    {"type": "nibble", "pos": [50, 230], "id": [35, 36, 37, 38], "val": [0, 0, 0, 0]}
  ],
  "out": [
    {"type": "7seg", "pos": [410, 140], "id": [27, 28, 29, 30, 31, 32, 33, 34]}
  ],
  "components": [
    {"type": "register", "pos": [220, 130], "in": [0, 1, 2, 3, 4, 5, 6], "out": [7, 8, 9, 10], "state": [0, 0, 0, 0]},
    {"type": "decoder-7seg", "pos": [330, 130], "in": [16, 17, 18, 19], "out": [20, 21, 22, 23, 24, 25, 26]}
  ],
  "wires": [[11, 3], [12, 4], [13, 5], [14, 6], [15, 0], [7, 16], [8, 17], [9, 18], [10, 19], [20, 27], [21, 28], [22, 29], [23, 30], [24, 31], [25, 32], [26, 33]]
}
```

## Accumulateur

Un accumulateur est un registre spécial qui *accumule* une somme. La sortie de l'accumulateur est reliée avec l'entrée A de l'ALU. À chaque coup d'horloge du registre, le calcul `acc + b` est effectué et affiché.

Par exemple dans le circuit ci-dessous, l'accumulateur contient 3. Au prochain coup d'horloge, l'entrée b qui est 2 y sera additionnée. Ceci permet de calculer une somme courante.

Voici un exemple typique, calculer la somme 1+3+7.
En Python ceci correspondrait à :

``` Python
acc = 0     # clear
acc += 1    # add
acc += 3    # add
acc += 7    # add
print(acc)
```

Avec le circuit ci-dessous ceci correspond à 4 étapes:

1. **clear**
1. b=1 et **add**
1. b=3 et **add**
1. b=7 et **add**

Connectez les entrées **clear** et **add** au bon endroit et calculez 1+3+7.

**Attention:** tenez le bouton suffisamment longtemps pour laisser propager les signaux jusqu'au bout.

```{logic}
:ref: acc
:height: 500
:showonly: in in.nibble register alu out.nibble-display

{ // JSON5
  v: 6,
  components: {
    in0: {type: 'in', pos: [40, 220], id: '0-3', name: 'b', bits: 4, val: '0010'},
    in1: {type: 'in', pos: [380, 320], orient: 'n', id: 37, name: 'clear', isPushButton: true},
    in2: {type: 'in', pos: [200, 320], id: 38, name: 'add', isPushButton: true},
    disp0: {type: 'display', pos: [90, 220], id: '47-50'},
    disp1: {type: 'display', pos: [520, 170], id: '51-54'},
    disp2: {type: 'display', pos: [290, 170], id: '33-36'},
    alu0: {type: 'alu', pos: [200, 170], in: '4-14', out: '15-21'},
    acc: {type: 'reg', pos: [380, 170], in: '22-28', out: '29-32', content: '3'},
    label0: {type: 'label', pos: [380, 70], text: 'accumulateur'},
  },
  wires: [[15, 25], [16, 26], [17, 27], [18, 28], [0, 47], [1, 48], [2, 49], [3, 50], [29, 51], [30, 52], [31, 53], [32, 54], [0, 8], [1, 9], [2, 10], [3, 11], [29, 4, {via: [[440, 140, 'w'], [440, 50, 'w'], [155, 50, 'w']]}], [30, 5, {via: [[450, 160, 'n'], [450, 40, 'w'], [145, 40, 'w'], [145, 110, 'w']]}], [31, 6, {via: [[460, 180, 'w'], [460, 30, 'w'], [135, 30, 'w'], [135, 130, 'w']]}], [32, 7, {via: [[470, 200, 'w'], [470, 20, 'w'], [125, 20, 'w'], [125, 150, 'w']]}], [15, 33], [16, 34], [17, 35], [18, 36]]
}
```

## Incrémenter/décrémenter

Certains appareils électroniques ont très peu de touches et on doit utiliser juste deux boutons.
C'est le cas pour régler la température ou le volume.

Compléter le circuit pour les boutons

- **up** pour incrémenter la valeur (clock)
- **down** pour décrémenter la valeur (clock + soustraction)
- **clear** pour mettre la valeur à zéro

Attention au délai de transmission par défaut de 100 ms. Il faut soit appuyer plus longtemps sur les boutons, ou diminuer ce délai.

```{logic}
:ref: incdec
:height: 500
:showonly: in or or3 or4 register decoder-7seg out.7seg

{ // JSON5
  v: 6,
  components: {
    in0: {type: 'in', pos: [80, 400], id: 75, name: 'clear', isPushButton: true},
    in1: {type: 'in', pos: [80, 360], id: 78, name: 'down', isPushButton: true},
    in2: {type: 'in', pos: [80, 320], id: 82, name: 'up', isPushButton: true},
    '7seg0': {type: '7seg', pos: [510, 180], id: '27-34'},
    or0: {type: 'or', pos: [210, 350], in: [79, 80], out: 81},
    reg0: {type: 'reg', pos: [300, 170], in: '0-6', out: '7-10', content: '4'},
    dec0: {type: 'dec-7seg', pos: [430, 170], in: '16-19', out: '20-26'},
    alu0: {type: 'alu', pos: [165, 170], in: '57-67', out: '68-74'},
  },
  wires: [[7, 16], [8, 17], [9, 18], [10, 19], [20, 27], [21, 28], [22, 29], [23, 30], [24, 31], [25, 32], [26, 33], [7, 57, {via: [[350, 55, 'w'], [120, 55, 'w']]}], [8, 58, {via: [[360, 160, 'w'], [360, 45, 'n'], [110, 45, 'w'], [110, 110, 'w']]}], [9, 59, {via: [[370, 180, 'w'], [370, 35, 'w'], [100, 35, 'w'], [100, 130, 'w']]}], [10, 60, {via: [[380, 200, 'n'], [380, 25, 'w'], [90, 25, 'w'], [90, 150, 's']]}], [68, 3], [69, 4], [70, 5], [71, 6]]
}
```

## Comparer

En Python nous disposons de 6 comparateurs pour comparer deux nombres a et b :

- `>` plus grand
- `>=` plus grand ou égal
- `==` égal
- `!=` non égal
- `<=` plus petit ou égal
- `<` plus petit

Nous pouvons créer ces 6 comparaisons en utilisant une ALU qui soustrait deux nombres a et b et quelques portes logiques.
Voici quelques astuces :

- quand a-b est zéro alors `Z=1`, donc **a égal b**
- quand a-b est négatif, alors `C=1`, donc **a plus petit que b**
- quand vous combinez les deux `Z=1` ou `C=1`, vous trouvez **a plus petit ou égal à b**

Utilisez les portes ET, OU et NON pour décoder les 6 types de comparaisons.

```{logic}
:ref: compare
:height: 600
:showonly: in out alu not or and 
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [50, 120], "id": [18, 19, 20, 21], "val": [0, 1, 0, 0], "name": "a"},
    {"type": "nibble", "pos": [50, 220], "id": [26, 27, 28, 29], "val": [1, 1, 0, 0], "name": "b"},
    {"pos": [200, 40], "orient": "s", "id": 94, "name": "Op0", "val": 1}
  ],
  "out": [
    {"type": "nibble-display", "pos": [100, 120], "id": [22, 23, 24, 25], "radix": -10},
    {"type": "nibble-display", "pos": [100, 220], "id": [30, 31, 32, 33], "radix": -10},
    {"type": "nibble-display", "pos": [270, 170], "id": [39, 40, 41, 42], "name": "a-b", "radix": -10},
    {"pos": [340, 310], "id": 83, "name": "plus grand ou égal (>=)"},
    {"pos": [340, 260], "id": 93, "name": "plus grand (>)"},
    {"pos": [340, 360], "id": 95, "name": "égal (==)"},
    {"pos": [340, 410], "id": 96, "name": "non égal (!=)"},
    {"pos": [340, 460], "id": 97, "name": "plus petit (<)"},
    {"pos": [340, 510], "id": 98, "name": "plus petit ou égal (<=)"}
  ],
  "components": [
    {"type": "alu", "pos": [180, 170], "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "out": [11, 12, 13, 14, 15, 16, 17]}
  ],
  "wires": [[18, 0], [19, 1], [20, 2], [21, 3], [18, 22], [19, 23], [20, 24], [21, 25], [26, 4], [27, 5], [28, 6], [29, 7], [26, 30], [27, 31], [28, 32], [29, 33], [11, 39], [12, 40], [13, 41], [14, 42], [94, 8], [16, 95]]
}
```
