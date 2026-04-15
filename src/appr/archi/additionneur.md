
# Additionneur

On s'intéresse à une des opérations arithmétiques les plus simples : l'**addition**. Notre but est donc de réaliser un circuit logique capable d'additionner deux nombres entiers. 


## Demi-additionneur

On commence par additionner deux nombres à 1 bit, $A$ et $B$ et leur somme $S$. 
La table de vérité d'une telle addition est la suivante. 

| $A$ | $B$ | $S=A+B$ |
| :-: | :-: | :-: |
| 0   | 0   | 00  |
| 1   | 0   | 01  |
| 0   | 1   | 01  |
| 1   | 1   | 10  |

On note que la somme de deux bits peut faire $2$, c'est à dire $10$ en binaire.
La sortie $S$ doit donc être codée sur deux bits, qu'on appelle $S_0$
(bit des unité, de droite), et $S_1$ (bit de la valeur décimale 2, à gauche).
On peut donc ré-écrire la table de vérité ci-dessus ainsi: 

| $A$ | $B$ |$S_1$|$S_0$|
| :-: | :-: | :-: | :-: |
| 0   | 0   | 0   | 0   |
| 1   | 0   | 0   | 1   |
| 0   | 1   | 0   | 1   |
| 1   | 1   | 1   | 0   |

En comparant cette table de vérité avec celles des portes logiques, on se rend compte que $S_0$ n'est autre qu'un **OU-X** (OU exclusif) de $A$ et $B$, tandis quie celle de $S_1$ est un **ET**. 
On peut dessiner l'additionneur de deux bits (appelé *demi-additionneur*) ainsi :

```{logic}
:height: 140
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 0, "val": 0, "name": "A"},
    {"pos": [50, 110], "id": 1, "val": 0, "name": "B"}
  ],
  "out": [
    {"pos": [250, 40], "id": 8, "name": "S0"},
    {"pos": [250, 100], "id": 9, "name": "S1"}
  ],
  "gates": [
    {"type": "XOR", "pos": [180, 40], "in": [2, 3], "out": 4},
    {"type": "AND", "pos": [180, 100], "in": [5, 6], "out": 7}
  ],
  "wires": [[0, 2], [1, 3], [0, 5], [1, 6], [4, 8], [7, 9]]
}
```

```{exercise} 

Vérifiez que ce circuit livre bien les bonnes valeurs de sortie qui correspondent aux tables de vérité ci-dessous. Combien de combinaisons différentes devrez-vous tester ?
```
```{solution}
Le circuit fonctionne correctement. Il faut tester les quatre combinaisons qui apparaissent dans les tables de vérité.
```

## Additionneur complet

Le circuit précédent est particulièrement intéressant, car il montre qu'il est possible d'utiliser des opérateurs logiques pour réaliser l'opération arithmétique de l'addition. L'additionneur est limité: en fait, on l'appelle un _demi-additionneur_. Il n'est capable d'additionner que deux bits — c'est très limité. En fait, il serait intéressant d'avoir un additionneur de _trois_ bits. Pourquoi ? À cause de la manière dont on pose les additions en colonnes.

Lorsqu'on additionne deux nombres à plusieurs chiffres, que ce soit en base 10 ou en base 2, on commence par la colonne de droite, les unités. On connait le concept de _retenue_: en base 10, si l'addition des unités dépasse 9, on retient 1 dans la colonne des dizaines. En base 2, de façon similaire, si l'addition des unités dépasse… 1, on retient 1 dans la colonne suivante à gauche. C'est ce qu'on a fait avec le demi-additionneur: on peut considérer que la sortie $S_0$ représente la colonne des unités dans la somme, et la sortie $S_1$ représente la retenue à prendre en compte dans la colonne suivante.

C'est ici que ça se complique : pour additionner les chiffres de la deuxième colonne, on doit potentiellement additionner _trois_ chiffres, et plus seulement deux. On a donc, en entrée, les deux bits $A$ et $B$ qui viennent des nombres à additionner, et aussi potentiellement cette retenue qui vient de la colonne des unités, qu'on appellera $C_{in}$ (pour _carry_, «retenue» en anglais). Ceci est vrai en base 2 comme en base 10. Il faut donc un additionneur plus puissant, à trois entrées, pour prendre en compte cette retenue. Il s'appelle _additionneur complet_ et livrera deux sorties : le bit de somme, appelé simplement $S$, et la retenue à reporter pour la colonne suivante, appelée $C_{out}$.

```{exercise} Table de vérité de l'additionneur 
 * Déterminez combien de combinaisons différentes sont possibles pour trois signaux d'entrée $A$, $B$ et $C_{in}$ qui chacun peuvent valoir soit 1 soit 0.
 * Listez toutes ces combinaisons.
 * Pour chaque combinaison, déterminez la valeur binaire qui est la somme des trois signaux d'entrée.
 * Finalement, avec les informations ainsi obtenues, complétez la table de vérité d'un additionneur complet qui a deux sorties $S_0$ et $C_{out}$ (qui correspond à $S_{1}$). 
```
```{solution}
 Il y a $2 \cdot 2 \cdot 2 = 2^3 = 8$ combinaisons différentes. Avec la notation $A + B + C =$ valeur en décimal $=$ valeur en binaire, les voici :
  * $0 + 0 + 0 = 0_{(10)} = 00_{(2)}$
  * $0 + 0 + 1 = 1_{(10)} = 01_{(2)}$
  * $0 + 1 + 0 = 1_{(10)} = 01_{(2)}$
  * $0 + 1 + 1 = 2_{(10)} = 10_{(2)}$
  * $1 + 0 + 0 = 1_{(10)} = 01_{(2)}$
  * $1 + 0 + 1 = 2_{(10)} = 10_{(2)}$
  * $1 + 1 + 0 = 2_{(10)} = 10_{(2)}$
  * $1 + 1 + 1 = 3_{(10)} = 11_{(2)}$

La table de vérité est ainsi:

| $A$ | $B$ |$C_{in}$|$C_{out}$| $S_0$ |
| :-: | :-: | :-:    | :-:     | :-: |
| 0   | 0   | 0      | 0       | 0   |
| 0   | 0   | 1      | 0       | 1   |
| 0   | 1   | 0      | 0       | 1   |
| 0   | 1   | 1      | 1       | 0   |
| 1   | 0   | 0      | 0       | 1   |
| 1   | 0   | 1      | 1       | 0   |
| 1   | 1   | 0      | 1       | 0   |
| 1   | 1   | 1      | 1       | 1   |

```

```{exercise} Circuit de l'additionneur
Déterminer les fonctions logiques correspondant aux sorties $S$ et $C_{out}$
de la table de vérité de l'additionneur de l'exercice ci-dessus. En déduire son
circuit logique
```
```{solution}
On remarque que $S_0$ vaut B **OU-X** $C_{in}$ si A=0 et **NON** (B **OU-X** $C_{in}$) si A=1.

Autrement dit $S_0$ = (**NON** A) **ET** (B **OU-X** $C_{in}$) **OU** (A **ET** **NON** (B **OU-X** $C_{in}$)). 

Cela peut se simpifier en $S_0$ = A **OU-X** (B **OU-X** $C_{in}$) 

Pour $C_{out}$, on remarque qu'il vaut 1, s'il y a au moins deux 1 parmi les trois entrées. Donc si A est 0 on est obligé d'avoir B et $C_{in}$ à 1 pour que $C_{out}$ soit à 1. Si A est 1, alors il suffit que B ou C vale 1 pour que $C_{out}$ soit à 1.

Autrement dit $C_{out}$ = (A **ET** (B **OU** $C_{in}$)) **OU** (B **ET** $C_{in}$)

Le circuit correspondant est donc le suivant: 


```{logic}
:id: YWKujr
:height: 260
:mode: tryout

{ // JSON5
  v: 8,
  opts: {origin: [1, 2]},
  components: {
    in0: {type: 'in', pos: [55, 30], id: 0, name: 'A'},
    in1: {type: 'in', pos: [60, 130], id: 1, name: 'B'},
    in2: {type: 'in', pos: [60, 230], id: 2, name: 'Cin'},
    xor0: {type: 'xor', pos: [265, 65], in: [3, 4], out: 5},
    xor1: {type: 'xor', pos: [470, 40], in: [6, 7], out: 8},
    and0: {type: 'and', pos: [265, 220], in: [9, 10], out: 11},
    and2: {type: 'and', pos: [350, 130], in: [23, 24], out: 25},
    or1: {type: 'or', pos: [465, 165], in: [26, 27], out: 28},
    or0: {type: 'or', pos: [265, 140], in: [29, 30], out: 31},
    out0: {type: 'out', pos: [540, 40], id: 17, name: 'S0'},
    out1: {type: 'out', pos: [535, 165], id: 18, name: 'Cout'},
  },
  wires: [[2, 4], [1, 3], [0, 6], [5, 7], [1, 9], [2, 10], [1, 29], [2, 30], [0, 23], [31, 24], [25, 26], [8, 17], [28, 18], [11, 27]]
}
```


````{micro}
Vérifier que le circuit donné dans la solution de l'exercice ci-dessus donne bien en sortie la somme des
trois entrée. 
````

On peut représenter ce circuit comme un nouveau composant à trois entrées et deux sorties, que l'on dessine simplement ainsi :

```{logic}
:height: 120
:mode: static

{
  "v": 3,
  "opts": {"showDisconnectedPins": true},
  "components": [{"type": "adder", "pos": [60, 60], "in": [0, 1, 2], "out": [3, 4]}]
}
```

## Chaînage d'additionneurs

La flexibilité de ce composant fait qu'on peut maintenant facilement l'utiliser pour construire un circuit qui additionne deux nombres $A$ et $B$ à 2 bits chacun (donc de $0 + 0 = 0$ à $3 + 3 = 6$).

Si $A$ est formé de deux bits $A_0$ et $A_1$ et que $B$ est formé des deux bits $B_0$ et $B_1$ et avec une sortie $S$ sur trois bits $S_0$, $S_1$ et $S_2$, on a :

```{logic}
:ref: fulladder_2bits
:height: 280
:mode: tryout

{
  "v": 3,
  "opts": {"showDisconnectedPins": true},
  "in": [
    {"pos": [190, 100], "orient": "s", "id": 10, "ref": "b0", "name": "B0", "val": 0},
    {"pos": [90,  100], "orient": "s", "id": 11, "ref": "b1", "name": "B1", "val": 0},
    {"pos": [230, 40], "orient": "s", "id": 12, "ref": "a0", "name": "A0", "val": 0},
    {"pos": [130, 40], "orient": "s", "id": 13, "ref": "a1", "name": "A1", "val": 0}
  ],
  "out": [
    {"pos": [210, 240], "orient": "s", "id": 14, "ref": "s0", "name": "S0"},
    {"pos": [110, 240], "orient": "s", "id": 15, "ref": "s1", "name": "S1"},
    {"pos": [30, 240], "orient": "s", "id": 16, "ref": "s2", "name": "S2"}
  ],
  "components": [
    {"type": "adder", "pos": [210, 170], "ref": "adder0", "in": [0, 1, 2], "out": [3, 4]},
    {"type": "adder", "pos": [110, 170], "ref": "adder1", "in": [5, 6, 7], "out": [8, 9]}
  ],
  "wires": [[4, 7, {"ref": "cout1"}], [10, 0], [11, 5], [13, 6], [12, 1], [3, 14], [8, 15], [9, 16, {"ref": "cout2"}]]
}
```

L'{logicref}`fulladder_2bits.adder0|additionneur de droite`, comme précédemment, additionne {logicref}`fulladder_2bits.{a0,b0}|les deux bits des unités` : $A_0$ et $B_0$. Son entrée $C_{in}$, qui représente l'éventuel troisième chiffre à additionner issu d'une retenue, n'est pas connectée et est toujours 0, vu qu'il n'y a aucune colonne précédente dans l'addition qui aurait pu en livrer une. Il livre comme {logicref}`fulladder_2bits.s0|première sortie` $S_0$, le chiffre des unités, et sa {logicref}`fulladder_2bits.cout1|seconde sortie` $C_{out}$ est la retenue à utiliser pour l'addition des chiffres suivants. C'est pourquoi elle est connectée à l'entrée de la retenue du {logicref}`fulladder_2bits.adder1|second additionneur` $C_{in}$, qui va lui ajouter également {logicref}`fulladder_2bits.{a1,b1}|les deux bits de la colonne suivante`, $A_1$ et $B_1$. Les sorties du second additionneur livrent {logicref}`fulladder_2bits.s1|le deuxième bit` $S_1$ de la valeur de sortie, ainsi que {logicref}`fulladder_2bits.cout2|la retenue pour la troisième colonne`. Comme il n'y a plus de bits d'entrée pour la troisième colonne, cette retenue peut directement être considérée comme {logicref}`fulladder_2bits.s2|le troisième bit de sortie` $S_2$.

````{exercise} Limite de cet additionneur à 2 bits
Avec l'additionneur ci-dessus, est-il possible d'obtenir des 1 sur toutes les sorties, donc d'avoir $S_2 = S_1 = S_0 = 1$ ?

<!-- ```{dropdown} Indice -->
<!-- Déterminez quel est le nombre décimal qui serait représenté par $S_2 = S_1 = S_0 = 1$: $111_{(2)} =\;???_{(10)}$  Ensuite, déterminez les nombres les plus grands représentables sur les deux fois 2 bits d'entrée et tirez-en une conclusion. -->
````

```{Solution}
La configuration $S_2 = S_1 = S_0 = 1$ représente le nombre décimal 7. Ce serait le résultat de l'addition. Il faudrait ainsi chercher une configuration des bits d'entrées qui, une fois additionnés, donnent 7. Mais ceci n'est pas possible, car sur chacune des entrées $(A_1, A_0)$ et $(B_1, B_0)$, la plus grande valeur représentable est $11_{(2)}$, autrement dit $3_{(10)}$ — et c'est impossible d'atteindre 7 en évaluant au maximum $3+3$.
```

````{exercise} Additionneur de demi-octets

En connectant des additionneurs complets, réalisez un circuit qui additionne deux nombres $A$ et $B$ de quatre bits, numérotés $A_0$ à $A_3$ et $B_0$ à $B_3$, respectivement. Combien de bits de sortie doit-il y avoir pour traiter toutes les valeurs possibles ?

Les entrées sont déjà disposées. Glissez autant d'additionneurs et de bits de sortie que nécessaire et connectez les composants du circuit.

```{logic}
:height: 500
:showonly: out adder

{
  "v": 3,
  "in": [
    {"pos": [90,  90], "orient": "s", "id": 3, "name": "B3", "val": 0},
    {"pos": [190, 90], "orient": "s", "id": 0, "name": "B2", "val": 0},
    {"pos": [290, 90], "orient": "s", "id": 1, "name": "B1", "val": 0},
    {"pos": [390, 90], "orient": "s", "id": 2, "name": "B0", "val": 0},
    {"pos": [130, 40], "orient": "s", "id": 15, "name": "A3", "val": 0},
    {"pos": [230, 40], "orient": "s", "id": 14, "name": "A2", "val": 0},
    {"pos": [330, 40], "orient": "s", "id": 13, "name": "A1", "val": 0},
    {"pos": [430, 40], "orient": "s", "id": 12, "name": "A0", "val": 0}
  ]
}
```
````
````{solution}
On a besoin de cinq bits de sortie. Le schéma, représenté horizontalement et de droite à gauche pour être proche de la représentation selon laquelle les additions se résolvent en colonne, est :

```{logic}
:height: 300
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [90,  90], "orient": "s", "id": 3,  "name": "B3", "val": 0},
    {"pos": [190, 90], "orient": "s", "id": 0,  "name": "B2", "val": 0},
    {"pos": [290, 90], "orient": "s", "id": 1,  "name": "B1", "val": 0},
    {"pos": [390, 90], "orient": "s", "id": 2,  "name": "B0", "val": 0},
    {"pos": [130, 40], "orient": "s", "id": 15, "name": "A3", "val": 0},
    {"pos": [230, 40], "orient": "s", "id": 14, "name": "A2", "val": 0},
    {"pos": [330, 40], "orient": "s", "id": 13, "name": "A1", "val": 0},
    {"pos": [430, 40], "orient": "s", "id": 12, "name": "A0", "val": 0}
  ],
  "out": [
    {"pos": [30, 260], "orient": "s", "id": 37, "name": "S4"},
    {"pos": [110, 260], "orient": "s", "id": 36, "name": "S3"},
    {"pos": [210, 260], "orient": "s", "id": 38, "name": "S2"},
    {"pos": [310, 260], "orient": "s", "id": 39, "name": "S1"},
    {"pos": [410, 260], "orient": "s", "id": 40, "name": "S0"}
  ],
  "components": [
    {"type": "adder", "pos": [410, 190], "in": [16, 17, 18], "out": [19, 20]},
    {"type": "adder", "pos": [310, 190], "in": [21, 22, 23], "out": [24, 25]},
    {"type": "adder", "pos": [210, 190], "in": [26, 27, 28], "out": [29, 30]},
    {"type": "adder", "pos": [110, 190], "in": [31, 32, 33], "out": [34, 35]}
  ],
  "wires": [
    [20, 23],
    [25, 28],
    [30, 33],
    [2, 16],
    [12, 17],
    [1, 21],
    [13, 22],
    [0, 26],
    [14, 27],
    [3, 31],
    [15, 32],
    [35, 37],
    [34, 36],
    [29, 38],
    [24, 39],
    [19, 40]
  ]
}
```
````

Cet exercice démontre l'opportunité de penser en termes modulaires, ce qui revient souvent en informatique. Ici, on a réalisé qu'un additionneur complet résout un sous-problème bien défini d'une addition générale d'un nombre à $n$ bits, et qu'une fois qu'on a créé un tel additionneur, il suffit d'en connecter plusieurs les uns derrière les autres de manière structurée pour additionner des nombres plus grands.


`````{htmlonly}

````{exercise} Dépassement de capacité

Le schéma ci-dessous montre le même additionneur de demi-octets de l'exercice précédent, mais, de plus, la valeur en base 10 de ses 4 bits d'entrée pour $A$ et pour $B$ est affichée avec {logicref}`fulladder_4bits_test.{displayA,displayB}|un module d'affichage spécial à droite`. {logicref}`fulladder_4bits_test.{displayS}|La même chose` est faite pour représenter la valeur $S = A + B$ (mais seulement sur les quatre premiers bits de $S$). Actuellement, le circuit effectue le calcul $0 + 0 = 0$.

Réglez les entrées du circuit de manière à lui faire effectuer les additions suivantes, et vérifiez le résultat. Dans quelles circonstances est-il correct et pourquoi est-il de temps en temps incorrect ? Comment, en regard de ceci, interpréter le bit de sortie $S_4$, qui est la retenue de l'additionneur de gauche ?
   1. $1 + 0$
   1. $3 + 1$
   1. $3 + 3$
   1. $10 + 5$
   1. $14 + 1$
   1. $14 + 2$
   1. $15 + 15$

```{logic}
:ref: fulladder_4bits_test
:height: 550
:mode: tryout

{ // JSON5
  v: 8,
  opts: {wireStyle: 'vh'},
  components: {
    in0: {type: 'in', pos: [100, 195], orient: 's', id: 3, name: 'B3'},
    in1: {type: 'in', pos: [200, 195], orient: 's', id: 0, name: 'B2'},
    in2: {type: 'in', pos: [300, 195], orient: 's', id: 1, name: 'B1'},
    in3: {type: 'in', pos: [400, 195], orient: 's', id: 2, name: 'B0'},
    in4: {type: 'in', pos: [140, 45], orient: 's', id: 15, name: 'A3'},
    in5: {type: 'in', pos: [240, 45], orient: 's', id: 14, name: 'A2'},
    in6: {type: 'in', pos: [340, 45], orient: 's', id: 13, name: 'A1'},
    in7: {type: 'in', pos: [440, 45], orient: 's', id: 12, name: 'A0'},
    out0: {type: 'out', pos: [30, 475], orient: 's', id: 37, name: 'S4'},
    out1: {type: 'out', pos: [120, 475], orient: 's', id: 36, name: 'S3'},
    out2: {type: 'out', pos: [220, 475], orient: 's', id: 38, name: 'S2'},
    out3: {type: 'out', pos: [320, 475], orient: 's', id: 39, name: 'S1'},
    out4: {type: 'out', pos: [420, 475], orient: 's', id: 40, name: 'S0'},
    displayA: {type: 'display', pos: [530, 255], id: '4-7', name: 'B'},
    displayB: {type: 'display', pos: [530, 105], id: '8-11', name: 'A'},
    displayS: {type: 'display', pos: [530, 415], id: '41-44', name: 'S'},
    adder0: {type: 'adder', pos: [420, 345], orient: 's', in: [17, 16, 18], out: [19, 20]},
    adder1: {type: 'adder', pos: [320, 345], orient: 's', in: [22, 21, 23], out: [24, 25]},
    adder2: {type: 'adder', pos: [220, 345], orient: 's', in: [27, 26, 28], out: [29, 30]},
    adder3: {type: 'adder', pos: [120, 345], orient: 's', in: [32, 31, 33], out: [34, 35]},
    label0: {type: 'label', pos: [530, 180], text: '+'},
    label1: {type: 'label', pos: [530, 335], text: '='},
  },
  wires: [[12, 8], [13, 9], [14, 10], [15, 11], [2, 4], [1, 5], [0, 6], [3, 7], [20, 23], [25, 28], [30, 33], [2, 16], [12, 17], [1, 21], [13, 22], [0, 26], [14, 27], [3, 31], [15, 32], [19, 41], [24, 42], [29, 43], [34, 44], [35, 37, {style: 'hv'}], [34, 36], [29, 38], [24, 39], [19, 40]]
}
```
````
```{solution}
Dès que la somme dépasse 15, elle n'est plus représentable sur les 4 bits qui sont affichés sur la sortie. La plupart des ordinateurs et smartphones actuels représentent les nombres non pas sur 4 bits, mais sur 64. Mais même avec 64 bits, il y a un nombre maximal que l'on peut représenter (en l'occurrence, $2^{64} - 1 = 18\,446\,744\,073\,709\,551\,615$.) La retenue du dernier additionneur indique si le résultat est valable : il vaut 1 lorsque le résultat de l'addition n'est pas correctement représenté avec les 4 (ou 64) bits de sortie. Dans les processeurs, il porte souvent simplement le nom de $C$ (pour _carry_, retenue). On utilisera dorénavant aussi ce nom.
```


````{exercise} Circuit défectueux

L'additionneur de demi-octets ci-dessous a été endommagé et ne fonctionne plus correctement. Par exemple, lorsqu'on lui demande d'effectuer le calcul $11 + 1$, il livre comme réponse $8$.

Déterminez quel composant est défectueux dans ce circuit et comment il faudrait le réparer. Vous pouvez changer les entrées pour vérifier ce qui ne fonctionne pas.

```{logic}
:ref: fulladder_4bits_faulty
:height: 550
:mode: tryout

{ // JSON5
  v: 8,
  opts: {wireStyle: 'vh', origin: [-41, -26]},
  components: {
    in0: {type: 'in', pos: [100, 195], orient: 's', id: 3, name: 'B3'},
    in1: {type: 'in', pos: [200, 195], orient: 's', id: 0, name: 'B2'},
    in2: {type: 'in', pos: [300, 195], orient: 's', id: 1, name: 'B1'},
    in3: {type: 'in', pos: [400, 195], orient: 's', id: 2, name: 'B0', val: 1},
    in4: {type: 'in', pos: [140, 45], orient: 's', id: 15, name: 'A3', val: 1},
    in5: {type: 'in', pos: [240, 45], orient: 's', id: 14, name: 'A2'},
    in6: {type: 'in', pos: [340, 45], orient: 's', id: 13, name: 'A1', val: 1},
    in7: {type: 'in', pos: [440, 45], orient: 's', id: 12, name: 'A0', val: 1},
    out0: {type: 'out', pos: [30, 475], orient: 's', id: 37, name: 'S4'},
    out1: {type: 'out', pos: [120, 475], orient: 's', id: 36, name: 'S3'},
    out2: {type: 'out', pos: [220, 475], orient: 's', id: 38, name: 'S2'},
    out3: {type: 'out', pos: [320, 475], orient: 's', id: 39, name: 'S1'},
    out4: {type: 'out', pos: [420, 475], orient: 's', id: 40, name: 'S0'},
    displayA: {type: 'display', pos: [530, 255], id: '4-7', name: 'B'},
    displayB: {type: 'display', pos: [530, 105], id: '8-11', name: 'A'},
    displayS: {type: 'display', pos: [530, 415], id: '41-44', name: 'S'},
    adder0: {type: 'adder', pos: [420, 345], orient: 's', in: [17, 16, 18], out: [19, 20]},
    adder1: {type: 'adder', pos: [320, 345], orient: 's', in: [22, 21, 23], out: [24, {id: 25, force: 0}]},
    adder2: {type: 'adder', pos: [220, 345], orient: 's', in: [27, 26, 28], out: [29, 30]},
    adder3: {type: 'adder', pos: [120, 345], orient: 's', in: [32, 31, 33], out: [34, 35]},
    label0: {type: 'label', pos: [530, 180], text: '+'},
    label1: {type: 'label', pos: [530, 335], text: '='},
  },
  wires: [[12, 8], [13, 9], [14, 10], [15, 11], [2, 4], [1, 5], [0, 6], [3, 7], [20, 23], [25, 28, {ref: "cout2"}], [30, 33], [2, 16], [12, 17], [1, 21], [13, 22], [0, 26], [14, 27], [3, 31], [15, 32], [19, 41], [24, 42], [29, 43], [34, 44], [35, 37, {style: 'hv'}], [34, 36], [29, 38], [24, 39], [19, 40]]
}
```
````
```{solution}
La {logicref}`fulladder_4bits_faulty.cout2|retenue sortant du deuxième additionneur depuis la droite` est bloquée à 0 à la place de correctement changer de valeur suivant ses entrées.
```
`````
