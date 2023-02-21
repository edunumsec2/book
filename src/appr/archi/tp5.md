# TP CPU

Le processeur, aussi appelé CPU (Central processing Unit) ou unité de traitement central, lit des instructions dans la mémoire programme et les exécute.

Tout ce que le processeur fait peut être décrit en 3 lignes:

- chercher une instruction dans la mémoire de programme (Fetch)
- exécuter cette instruction (Execute)
- incrémenter le pointeur vers la prochaine instruction (Increment)

Dans cette section nous allons étudier comment encoder des instructions en code binaire, et comment ensuite exécuter ce code dans le CPU. Nous allons nous inspirer du premier microprocesseur, la puce Intel 4004, sortie en 1971.

![boitier](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Intel_C4004.jpg/640px-Intel_C4004.jpg)

## Intel 4004

Le premier CPU sur un seul circuit intégré fut le 4004 commercialisé par Intel en 1971. Il contenait les éléments suivants:

- une ALU (unité arithmétique et logique)
- 16 registres de travail
- un accumulateur (accumulator)
- un bus de données (data bus)
- un bus d'adresses (adress bus)
- des fanions (flags)
- un registre d'instruction (instruction register)
- un compteur de programme (program counter)
- un pointeur de pile (stack pointer)
- une pile (stack)
- une unité de contrôle (control unit)

Voici le schéma de l'architecture du 4004.

![4004](https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/4004_arch.svg/1016px-4004_arch.svg.png)

## Langage assembleur

Nous allons commencer tout de suite avec un exemple de programme pour le 4004, en langage assembleur. Voici un bout de programme qui additionne deux nombres 4 bits.

```text
ADD2
; add two 4bit numbers on the Intel 4004
;
    FIM P0, $A2 ; initialize: R0=2 R1=A
    LDR R0      ; load R0 into accumulator
    ADD R1      ; add R1 into accumulator
    XCH R1      ; and store in R1
```

Le point-virgule (`;`) sert comme symbole de commentaire.  C'est l'équivalent du `#` en Python.
Un programme en assembleur est typiquement structuré en 4 colonnes :

1. Une étiquette pour désigner une adresse de programme (`ADD2`)
1. Une mnémonique de l'opération (`FIM`, `LDR`, `ADD`, `XCH`)
1. Des données (P0, $A2, R0, R1)
1. Des commentaires en fin de ligne

## Le langage machine

Le langage machine, ou code machine, est la suite de bits qui est interprétée par le processeur d'un ordinateur exécutant un programme informatique. C'est le langage natif d'un processeur, c'est-à-dire le seul qu'il puisse traiter. Il est composé d'instructions et de données à traiter codées en binaire.

- `1000RRRR` additionne (ADD) le registre `RRRR` à l'accumulateur
- `1001RRRR` soustrait (SUB) le registre `RRRR` de l'accumulateur
- `1101DDDD` charge (LDM = load) le nombre `DDDD` vers l'accumulateur

Le code machine est composée de :

- la partie instruction ou **opcode**, tel que `1000=ADD`, `1001=SUB`
- la partie donnée ou **data**, qui indique un registre `RRRR` où un nombre `DDDD`

Par exemple l'instruction en assembleur `ADD R3` se traduit en code machine comme `10000011`.

Trouvez les deux autres codes machine.

```{logic}
:ref: opcode
:height: 300
:showonly: in.byte
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [60, 50], "orient": "s", "id": [0, 1, 2, 3, 4, 5, 6, 7], "val": "10000011", "name": "ADD R3"},
    {"type": "byte", "pos": [60, 130], "orient": "s", "id": [8, 9, 10, 11, 12, 13, 14, 15], "name": "SUB R15"},
    {"type": "byte", "pos": [60, 210], "orient": "s", "id": [16, 17, 18, 19, 20, 21, 22, 23], "name": "LDM 13"}
  ]
}
```

## Mémoire de programme

Le CPU 4004 traite des données de 4 bits. Les données que ce processeur peut traiter avec une seule instruction sont limitées à une plage de 0 à 15 (de `0000` à `1111`). On dit que c'est un processeur 4 bits ou une **architecture 4 bits**.

Chaque instruction par contre est encodée sur 8 bits. Ce processeur pourrait donc avoir au maximum 256 instructions différentes. En réalité il a 46 instructions.

Le vrai CPU 4004 peut adresser un espace mémoire de programme avec une adresse 12 bits. Ceci lui permet d'adresser un maximum de $2^{12}$ instructions différentes dans sa mémoire programme.
Ici nous simplifions beaucoup et utilisons des adresses de 4 bits. Notre mémoire programme a une taille de 16 x 8 bits. Notre programme peut avoir un maximum de 16 instructions.

Beaucoup d'instructions sont composées d'une partie

- instruction (4 bits), appelée **opcode**
- données (4 bits), appelé **data**

Dans le circuit ci-dessous, ajoutez :

- une broche 4 bits
- une sortie 4 bits
- un affichage 4 bits (en hexadécimal)
- une étiquette **opcode**
- Mettez les instructions `ADD R3`, `SUB R15` et `LDM 13` dans les 3 premiers octets de la mémoire programme.

```{logic}
:ref: progmem
:height: 300
:showonly: layout.pass-4 out.nibble out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [180, 40], "orient": "s", "id": [23, 24, 25, 26], "val": [0, 0, 1, 0], "name": "adresse"},
    {"type": "byte", "pos": [60, 140], "id": [27, 28, 29, 30, 31, 32, 33, 34], "val": "11000001", "name": "inst"},
    {"pos": [80, 200], "id": 51, "name": "clock", "val": 0, "isPushButton": true},
    {"pos": [160, 250], "orient": "n", "id": 52, "val": 1},
    {"pos": [200, 250], "orient": "n", "id": 93, "val": 0, "isPushButton": true}
  ],
  "out": [
    {"type": "nibble", "pos": [350, 70], "id": [35, 36, 37, 38]},
    {"type": "nibble-display", "pos": [420, 70], "id": [39, 40, 41, 42], "name": "data", "radix": 16}
  ],
  "components": [
    {"type": "ram-16x8", "pos": [180, 140], "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "out": [15, 16, 17, 18, 19, 20, 21, 22]}
  ],
  "layout": [
    {"type": "pass-4", "pos": [320, 70], "in": [43, 44, 45, 46], "out": [47, 48, 49, 50]}
  ],
  "wires": [[23, 11], [24, 12], [25, 13], [26, 14], [27, 3], [28, 4], [29, 5], [30, 6], [31, 7], [32, 8], [33, 9], [34, 10], [15, 43], [16, 44], [17, 45], [18, 46], [47, 35], [48, 36], [49, 37], [50, 38], [47, 39], [48, 40], [49, 41], [50, 42], [51, 0], [52, 1], [93, 2]]
}
```

## Le jeu d'instructions

On appelle **jeu d'instruction** (instruction set) la totalité des instructions qu'un processeur peut exécuter. Ces instructions sont représentées par une abréviation à 3 lettres (mnémonique). Les premières 14 instructions sont composées d'une partie:

- instruction (4 bits), appelée **opcode**, de `0000` à `1101`
- données (4 bits), appelé **data**

La partie `data' peu représenter 3 types de données :

- `AAAA` une adresse dans la mémoire programme
- `RRRR` un registre dans la banque des registres
- `DDDD` une donnée immédiate (un nombre de 0 à 15)

```text
NOP 00000000  No Operation
JCN 0001AAAA  Jump Conditional
FIM 0010RRR0  DDDDDDDD  Fetch Immediate
FIN 0011RRR0  Fetch Indirect
JUN 0100AAAA  Jump Unconditional
JMS 0101AAAA  Jump to Subroutine
INC 0110RRRR  Increment
ISZ 0111RRRR  AAAAAAAA  Increment and Skip

ADD 1000RRRR  Add register
SUB 1001RRRR  Subtract register
LDR 1010RRRR  Load register
XCH 1011RRRR  Exchange register
BBL 1100DDDD  Branch Back and Load
LDM 1101DDDD  Load Immediate data
```

## Décoder une instruction

Pour décoder les 14 instructions, nous pouvons utiliser un démultiplexeur.
Pour compléter le circuit de décodage d'instruction :

- Ajoutez un deuxième démultiplexeur
- Ajoutez les 11 sorties manquantes
- Ajoutez les étiquettes (`FIN` à `LDM`)
- Remplissez la mémoire programme avec les 14 instructions (`NOP` à `LDM`)
- Vérifiez que chaque instruction est décodée correctement

Par exemple à l'adresse `0100` (4) se trouve l'instruction `00010001` (`JCN 1`) et le décodeur active correctement la sortie `JCN`.

```{logic}
:ref: decode
:height: 700
:showonly: out not demux-1to8
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [180, 40], "orient": "s", "id": [23, 24, 25, 26], "val": [0, 0, 1, 0], "name": "adresse"},
    {"type": "byte", "pos": [60, 140], "id": [27, 28, 29, 30, 31, 32, 33, 34], "val": "00010001", "name": "inst"},
    {"pos": [80, 200], "id": 51, "name": "clock", "val": 0, "isPushButton": true},
    {"pos": [160, 250], "orient": "n", "id": 52, "val": 1},
    {"pos": [200, 250], "orient": "n", "id": 93, "val": 0, "isPushButton": true}
  ],
  "out": [
    {"type": "nibble", "pos": [350, 70], "id": [35, 36, 37, 38]},
    {"type": "nibble-display", "pos": [420, 70], "id": [39, 40, 41, 42], "name": "data", "radix": 16},
    {"type": "nibble", "pos": [350, 170], "id": [102, 103, 104, 105]},
    {"type": "nibble-display", "pos": [420, 170], "id": [106, 107, 108, 109], "name": "opcode", "radix": 16},
    {"pos": [380, 300], "id": 122, "name": "NOP"},
    {"pos": [380, 320], "id": 123, "name": "JCN"},
    {"pos": [380, 340], "id": 127, "name": "FIM"}
  ],
  "gates": [
    {"type": "NOT", "pos": [210, 370], "in": 125, "out": 126}
  ],
  "components": [
    {"type": "ram-16x8", "pos": [180, 140], "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "out": [15, 16, 17, 18, 19, 20, 21, 22], "content": ["00000000", "00000000", "00000000", "00000000", "00010001"]},
    {"type": "demux-1to8", "pos": [300, 370], "in": [110, 111, 112, 113], "out": [114, 115, 116, 117, 118, 119, 120, 121]}
  ],
  "layout": [
    {"type": "pass-4", "pos": [320, 70], "in": [43, 44, 45, 46], "out": [47, 48, 49, 50]},
    {"type": "pass-4", "pos": [320, 170], "in": [94, 95, 96, 97], "out": [98, 99, 100, 101]}
  ],
  "wires": [[23, 11], [24, 12], [25, 13], [26, 14], [27, 3], [28, 4], [29, 5], [30, 6], [31, 7], [32, 8], [33, 9], [34, 10], [15, 43], [16, 44], [17, 45], [18, 46], [47, 35], [48, 36], [49, 37], [50, 38], [47, 39], [48, 40], [49, 41], [50, 42], [51, 0], [52, 1], [93, 2], [19, 94], [20, 95], [21, 96], [22, 97], [98, 102], [99, 103], [100, 104], [101, 105], [98, 106], [99, 107], [100, 108], [101, 109], [19, 111], [20, 112], [21, 113], [114, 122], [115, 123], [126, 110], [22, 125], [116, 127]]
}
```

## Bus 4 bits

Une ALU doit acheminer différents signaux sur une même ligne de transfert des données. On appelle un tel chemin un bus de données. Pour y connecter plusieurs sources, nous devons utiliser un multiplexeur.

- Ajoutez une deuxième entrée 4 bits
- Liez le multiplexeur et le démultiplexeur à travers une broche 4 bits
- Ajoutez les 2 entrées de sélection
- Ajoutez 4 affichages 4 bits pour montrer tous les signaux

```{logic}
:ref: LDM
:height: 500
:showonly: in out layout.pass-4 in.nibble out.nibble-display mux-8to2 demux-4to8
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [30, 120], "id": [0, 1, 2, 3], "val": [0, 0, 0, 0]}
  ],
  "components": [
    {"type": "mux-8to4", "pos": [180, 170], "in": [45, 46, 47, 48, 49, 50, 51, 52, 53], "out": [54, 55, 56, 57]},
    {"type": "demux-4to8", "pos": [500, 320], "in": [58, 59, 60, 61, 62], "out": [63, 64, 65, 66, 67, 68, 69, 70]}
  ],
  "labels": [
    {"pos": [280, 290], "text": "bus 4 bits"}
  ],
  "wires": [[0, 45], [1, 46], [2, 47], [3, 48]]
}
```

## Charger imméd. (LDM)

La commande `LDM` (Load immediate) va charger une valeur directe (0-15), contenue dans le code de l'instruction, dans l'accumulateur.

`1101DDDD`

La partie `1101` est l'opcode (`LDM`) et la partie `DDDD` représente les 4 bits des données à charger dans l'accumulateur.

- Liez les bits b0-b3 avec l'accumulateur
- Utilisez la porte ET pour charger cette valeur dans l'accumulateur seulement si le signal **execute** est activé ET l'instruction `LDM` est décodée
- Placez un affichage à la sorte de l'accumulateur et à la sortie de l'ALU
- Mettez une valeur dans les bits b0-b3 et exécutez l'instruction avec **execute**

```{logic}
:ref: LDM_
:height: 500
:showonly: in out out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [60, 50], "orient": "s", "id": [85, 86, 87, 88, 89, 90, 91, 92], "val": "11011001", "name": "instruction"},
    {"pos": [130, 350], "id": 101, "name": "execute", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [160, 150], "id": 122, "name": "ADD"},
    {"pos": [160, 170], "id": 123, "name": "SUB"},
    {"pos": [160, 190], "id": 127, "name": "LDR"},
    {"pos": [160, 210], "id": 53, "name": "XCH"},
    {"pos": [160, 230], "id": 54, "name": "BBL"},
    {"pos": [160, 250], "id": 55, "name": "LDM"}
  ],
  "gates": [
    {"type": "AND", "pos": [280, 340], "in": [102, 103], "out": 104}
  ],
  "components": [
    {"type": "demux-1to8", "pos": [80, 220], "in": [110, 111, 112, 113], "out": [114, 115, 116, 117, 118, 119, 120, 121]},
    {"type": "register", "pos": [370, 280], "in": [56, 57, 58, 59, 60, 61, 62], "out": [63, 64, 65, 66], "state": [1, 0, 0, 1]},
    {"type": "alu", "pos": [510, 330], "in": [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], "out": [78, 79, 80, 81, 82, 83, 84]}
  ],
  "layout": [
    {"type": "pass-4", "pos": [190, 60], "in": [93, 94, 95, 96], "out": [97, 98, 99, 100]}
  ],
  "wires": [[114, 122], [115, 123], [116, 127], [117, 53], [118, 54], [119, 55], [63, 67], [64, 68], [65, 69], [66, 70], [92, 110], [91, 113], [90, 112], [89, 111], [85, 93], [86, 94], [87, 95], [88, 96], [104, 56]]
}
```

## Charger depuis reg (LDR)

L'instruction `LDR` (load from register) charge l'accumulateur avec le contenu d'un des 16 registres.

`1010RRRR`

La parte `1010` est l'opcode (LD) et la parte `RRRR` représente un des 16 registres

- Ajoutez la RAM avec les 16 registres
- Créez le circuit de décodage pour charger registre `RRRR` dans l'accumulateur
- Placez un affichage à la sortie de l'accumulateur et à la sortie de l'ALU
- Mettez une valeur dans `R5`
- Mettez l'instruction `LDR R5` et exécutez l'instruction avec **execute**

```{logic}
:ref: LDM_
:height: 600
:showonly: in in.nibble out not and ram-16x4 out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [60, 50], "orient": "s", "id": [85, 86, 87, 88, 89, 90, 91, 92], "val": "11011001", "name": "instruction"},
    {"pos": [130, 350], "id": 101, "name": "execute", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [160, 150], "id": 122, "name": "ADD"},
    {"pos": [160, 170], "id": 123, "name": "SUB"},
    {"pos": [160, 190], "id": 127, "name": "LDR"},
    {"pos": [160, 210], "id": 53, "name": "XCH"},
    {"pos": [160, 230], "id": 54, "name": "BBL"},
    {"pos": [160, 250], "id": 55, "name": "LDM"}
  ],
  "gates": [
    {"type": "AND", "pos": [280, 340], "in": [102, 103], "out": 104}
  ],
  "components": [
    {"type": "demux-1to8", "pos": [80, 220], "in": [110, 111, 112, 113], "out": [114, 115, 116, 117, 118, 119, 120, 121]},
    {"type": "register", "pos": [370, 280], "in": [56, 57, 58, 59, 60, 61, 62], "out": [63, 64, 65, 66], "state": [1, 0, 0, 1]},
    {"type": "alu", "pos": [510, 330], "in": [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], "out": [78, 79, 80, 81, 82, 83, 84]}
  ],
  "layout": [
    {"type": "pass-4", "pos": [190, 60], "in": [93, 94, 95, 96], "out": [97, 98, 99, 100]}
  ],
  "wires": [[114, 122], [115, 123], [116, 127], [117, 53], [118, 54], [119, 55], [63, 67], [64, 68], [65, 69], [66, 70], [92, 110], [91, 113], [90, 112], [89, 111], [85, 93], [86, 94], [87, 95], [88, 96], [104, 56]]
}
```

## Choix entre LDR/LDM

Avec les deux opcode différents, le circuit de décodage du CPU choisit un registre ou une donnée immédiate comme valeur à charger dans l'accumulateur.

- Ajoutez la RAM avec les 16 registres
- Ajoutez un multiplexeur 8x4
- Créez le circuit de décodage pour choisir entre un registre `RRRR` ou une donnée immédiate `DDDD`
- Placez un affichage à la sortie de l'accumulateur et à la sortie de l'ALU
- Mettez une valeur dans `R5`
- Mettez l'instruction `LDR R5` et exécutez l'instruction avec **execute**
- Mettez l'instruction `LDM 13` et exécutez l'instruction avec **execute**

```{logic}
:ref: LDM_
:height: 600
:showonly: in in.nibble out out.nibble not and ram-16x4 mux-8to4 out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [60, 50], "orient": "s", "id": [85, 86, 87, 88, 89, 90, 91, 92], "val": "11011001", "name": "instruction"},
    {"pos": [130, 350], "id": 101, "name": "execute", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [160, 150], "id": 122, "name": "ADD"},
    {"pos": [160, 170], "id": 123, "name": "SUB"},
    {"pos": [160, 190], "id": 127, "name": "LDR"},
    {"pos": [160, 210], "id": 53, "name": "XCH"},
    {"pos": [160, 230], "id": 54, "name": "BBL"},
    {"pos": [160, 250], "id": 55, "name": "LDM"}
  ],
  "gates": [
    {"type": "AND", "pos": [280, 340], "in": [102, 103], "out": 104}
  ],
  "components": [
    {"type": "demux-1to8", "pos": [80, 220], "in": [110, 111, 112, 113], "out": [114, 115, 116, 117, 118, 119, 120, 121]},
    {"type": "register", "pos": [370, 280], "in": [56, 57, 58, 59, 60, 61, 62], "out": [63, 64, 65, 66], "state": [1, 0, 0, 1]},
    {"type": "alu", "pos": [510, 330], "in": [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], "out": [78, 79, 80, 81, 82, 83, 84]}
  ],
  "layout": [
    {"type": "pass-4", "pos": [190, 60], "in": [93, 94, 95, 96], "out": [97, 98, 99, 100]}
  ],
  "wires": [[114, 122], [115, 123], [116, 127], [117, 53], [118, 54], [119, 55], [63, 67], [64, 68], [65, 69], [66, 70], [92, 110], [91, 113], [90, 112], [89, 111], [85, 93], [86, 94], [87, 95], [88, 96], [104, 56]]
}
```

## Choix entre ADD/SUB

L'addition et la soustraction se distinguent dans l'opcode d'un seul bit.

- `1000RRRR` ADD additionner registre `RRRR` à l'accumulateur
- `1001RRRR` SUB soustraire registre `RRRR` de l'accumulateur

Créez le circuit pour décoder et exécuter ces deux instructions.

- Ajoutez la RAM avec les 16 registres
- Créez le circuit de décodage pour choisir entre `ADD` et `SUB`
- Placez un affichage à la sortie de l'accumulateur et nommez le **acc** (y mettre 9)
- Placez un affichage à la sortie de la RAM et nommez le **reg**
- Placez un affichage à la sortie de l'ALU et nommez le **result**
- Mettez la valeur 3 dans `R5`
- Mettez l'instruction `ADD R5` et vous devriez avoir **result = 12** (9 + 3)
- Mettez l'instruction `SUB R5` et vous devriez avoir **result = 6** (9 - 3)

```{logic}
:ref: LDM_
:height: 600
:showonly: in in.nibble out out.nibble not and ram-16x4 mux-8to4 out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [60, 50], "orient": "s", "id": [85, 86, 87, 88, 89, 90, 91, 92], "val": "11011001", "name": "instruction"},
    {"pos": [130, 350], "id": 101, "name": "execute", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"pos": [160, 150], "id": 122, "name": "ADD"},
    {"pos": [160, 170], "id": 123, "name": "SUB"},
    {"pos": [160, 190], "id": 127, "name": "LDR"},
    {"pos": [160, 210], "id": 53, "name": "XCH"},
    {"pos": [160, 230], "id": 54, "name": "BBL"},
    {"pos": [160, 250], "id": 55, "name": "LDM"}
  ],
  "gates": [
    {"type": "AND", "pos": [280, 340], "in": [102, 103], "out": 104}
  ],
  "components": [
    {"type": "demux-1to8", "pos": [80, 220], "in": [110, 111, 112, 113], "out": [114, 115, 116, 117, 118, 119, 120, 121]},
    {"type": "register", "pos": [370, 280], "in": [56, 57, 58, 59, 60, 61, 62], "out": [63, 64, 65, 66], "state": [1, 0, 0, 1]},
    {"type": "alu", "pos": [510, 330], "in": [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], "out": [78, 79, 80, 81, 82, 83, 84]}
  ],
  "layout": [
    {"type": "pass-4", "pos": [190, 60], "in": [93, 94, 95, 96], "out": [97, 98, 99, 100]}
  ],
  "wires": [[114, 122], [115, 123], [116, 127], [117, 53], [118, 54], [119, 55], [63, 67], [64, 68], [65, 69], [66, 70], [92, 110], [91, 113], [90, 112], [89, 111], [85, 93], [86, 94], [87, 95], [88, 96], [104, 56]]
}
```

## Program counter (PC)

Le pointeur de programme, PC (program counter), pointe toujours à la prochaine instruction dans la mémoire de programme. Le contenu à l'adresse pointé par le PC est celui qui est chargé dans le registre d'instruction (IR) et exécuté au prochain pas.

- Liez la sortie du PC avec l'entrée A du l'ALU pour incrémenter de 1 à chaque pas
- Placez un affichage à la sortie du registre et nommez le **PC**
- Liez le PC avec l'entrée adresse de la mémoire de programme
- Liez l'entrée **clock** avec l'horloge de l'ALU et l'horloge des deux registres IR
- Faites avancer le PC et chargez des instructions successives dans le registre IR

```{logic}
:ref: PC
:height: 600
:showonly: in out out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [170, 420], "id": [23, 24, 25, 26, 27, 28, 29, 30], "val": "10001011"},
    {"pos": [160, 480], "id": 53, "val": 0, "isPushButton": true},
    {"pos": [240, 530], "orient": "n", "id": 54, "val": 1},
    {"pos": [60, 40], "orient": "s", "id": 93, "name": "Cin", "val": 1},
    {"pos": [90, 320], "id": 94, "name": "clock", "val": 0, "isPushButton": true},
    {"pos": [190, 280], "orient": "n", "id": 96, "val": 0, "isPushButton": true}
  ],
  "out": [
    {"type": "nibble-display", "pos": [490, 280], "id": [56, 57, 58, 59], "name": "data"},
    {"type": "nibble-display", "pos": [490, 470], "id": [60, 61, 62, 63], "name": "opcode"}
  ],
  "components": [
    {"type": "ram-16x8", "pos": [260, 420], "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "out": [15, 16, 17, 18, 19, 20, 21, 22], "content": ["01001001", "01011011", "10001011", "00000000", "00000000", "00000000", "10001011"]},
    {"type": "register", "pos": [410, 280], "in": [31, 32, 33, 34, 35, 36, 37], "out": [38, 39, 40, 41], "state": [0, 0, 0, 0]},
    {"type": "register", "pos": [410, 470], "in": [42, 43, 44, 45, 46, 47, 48], "out": [49, 50, 51, 52], "state": [0, 0, 0, 0]},
    {"type": "alu", "pos": [80, 170], "in": [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], "out": [75, 76, 77, 78, 79, 80, 81]},
    {"type": "register", "pos": [190, 170], "in": [82, 83, 84, 85, 86, 87, 88], "out": [89, 90, 91, 92], "state": [0, 0, 0, 0]}
  ],
  "labels": [
    {"pos": [220, 60], "text": "program counter (PC)"},
    {"pos": [410, 180], "text": "instruction register (IR)"},
    {"pos": [240, 570], "text": "program memory"}
  ],
  "wires": [[23, 3], [24, 4], [25, 5], [26, 6], [27, 7], [28, 8], [29, 9], [30, 10], [15, 34], [16, 35], [17, 36], [18, 37], [19, 45], [20, 46], [21, 47], [53, 0], [54, 1], [22, 48], [38, 56], [39, 57], [40, 58], [41, 59], [49, 60], [50, 61], [51, 62], [52, 63], [75, 85], [76, 86], [77, 87], [78, 88], [93, 74], [96, 84]]
}
```

## Le saut (jump)

Le saut est une instruction qui permet de changer l'avancement linéaire du compteur de programme.
L'instruction de saut a la forme :

`Jump Uncoditional JUN 0100AAAA`

Pour l'exécuter, le CPU doit d'abord détecter l'opcode `0100`. Ceci peut être fait avec une porte ET à 4 entrées et des inverseurs.

Ensuite la valeur actuelle du compteur de programme doit être remplacée par la nouvelle adresse de destination du saut `AAAA`. Pour ceci nous utilisons un multiplexeur 8 vers 4.

Utilisez des portes NON et ET pour décoder l'opcode `0100` et l'utiliser pour sélectionner entre incrémentation normale et destination de saut.

A l'adresse 14 se trouve l'instruction `01000011` (`JUN 3`). Si le décodeur fonctionne correctement le programme va faire une boucle entre les addresses 3 et 14.

```{logic}
:ref: PC
:height: 600
:showonly: in out not and4 out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [200, 360], "id": [27, 28, 29, 30, 31, 32, 33, 34], "val": "01000011"},
    {"pos": [350, 470], "orient": "n", "id": 43, "name": "WE (Write Enable)", "val": 1},
    {"pos": [270, 420], "id": 44, "name": "Clock (horloge)", "val": 0, "isPushButton": true},
    {"pos": [50, 150], "id": 87, "name": "B0", "val": 1},
    {"type": "clock", "pos": [50, 330], "id": 88, "period": 2000}
  ],
  "out": [
    {"type": "byte-display", "pos": [260, 360], "id": [35, 36, 37, 38, 39, 40, 41, 42]},
    {"type": "nibble-display", "pos": [520, 280], "id": [98, 99, 100, 101], "name": "data"},
    {"type": "nibble-display", "pos": [520, 370], "id": [115, 116, 117, 118], "name": "opcode"}
  ],
  "components": [
    {"type": "ram-16x8", "pos": [370, 360], "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "out": [15, 16, 17, 18, 19, 20, 21, 22], "content": ["00110011", "00000000", "00000000", "01000011", "00000000", "01000011", "01000011", "00000000", "00000000", "00000000", "00000000", "00110010", "00100000", "00000000", "01000011"]},
    {"type": "alu", "pos": [120, 130], "in": [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], "out": [56, 57, 58, 59, 60, 61, 62]},
    {"type": "register", "pos": [270, 180], "in": [63, 64, 65, 66, 67, 68, 69], "out": [70, 71, 72, 73], "state": [0, 1, 1, 0]},
    {"type": "mux-8to4", "pos": [190, 180], "in": [74, 75, 76, 77, 78, 79, 80, 81, 82], "out": [83, 84, 85, 86]}
  ],
  "wires": [[27, 3], [28, 4], [29, 5], [30, 6], [31, 7], [32, 8], [33, 9], [34, 10], [27, 35], [28, 36], [29, 37], [30, 38], [31, 39], [32, 40], [33, 41], [34, 42], [43, 1], [44, 0], [83, 66], [84, 67], [85, 68], [86, 69], [56, 74], [57, 75], [58, 76], [59, 77], [87, 49], [70, 45], [71, 46], [72, 47], [73, 48], [88, 63], [73, 14], [72, 13], [71, 12], [70, 11], [15, 98], [16, 99], [17, 100], [18, 101], [15, 78], [16, 79], [17, 80], [19, 115], [20, 116], [21, 117], [22, 118]]
}
```

## La pile (stack)

La pile est un espace de sauvegarde temporaire. Elle est utilisée pour sauvegarder les adresses de retour lors d'un saut vers une sous-routine.

Ici nous créons une pile de 16 mots à 4 bits. D'habitude on commence la pile en bas de l'espace mémoire (adresse 15) et on *empile* les valeurs.

Le pointeur de pile (stack pointer) est un registre 4 bit, qui utilise une ALU pour être incrémenté ou décrémenté.
Si l'entrée `Op = 0` il incrémente. Si l'entrée `Op = 1` il décrémente.

Ajoutez les circuits de contrôle.

- Le signal **clear** efface la pile et met le pointeur de pile à `1111` (tout en bas)
- Le signal **push** choisit la décrémentation (sp--) et envoie un coup d'horloge vers le registre du pointeur et la pile
- Le signal **pop** choisit l'incrémentation (sp++) et envoie un coup d'horloge vers le registre du pointeur et la pile

Mettez dans la pile `3141592` (les 7 premiers chiffres du nombre pi) avec l'instruction **push**.  
Ensuite, lisez ces chiffres dans l'ordre inverse avec l'instruction **pop**

```{logic}
:ref: stack
:height: 600
:showonly: in out out.nibble-display
{
  "v": 4,
  "in": [
    {"pos": [50, 150], "id": 37, "name": "B0", "val": 1},
    {"type": "nibble", "pos": [290, 320], "id": [53, 54, 55, 56], "val": [0, 1, 1, 1], "name": "push"},
    {"pos": [70, 360], "id": 70, "name": "push", "val": 0, "isPushButton": true},
    {"pos": [70, 420], "id": 74, "name": "pop", "val": 0, "isPushButton": true},
    {"pos": [70, 480], "id": 75, "name": "clear", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"type": "nibble-display", "pos": [350, 130], "id": [29, 30, 31, 32], "name": "stack pointer"},
    {"type": "nibble-display", "pos": [340, 320], "id": [58, 59, 60, 61]},
    {"type": "nibble", "pos": [540, 320], "id": [62, 63, 64, 65]},
    {"type": "nibble-display", "pos": [590, 320], "id": [66, 67, 68, 69], "name": "pop"}
  ],
  "gates": [
    {"type": "OR", "pos": [160, 410], "in": [71, 72], "out": 73}
  ],
  "components": [
    {"type": "alu", "pos": [120, 130], "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "out": [11, 12, 13, 14, 15, 16, 17]},
    {"type": "register", "pos": [210, 130], "in": [18, 19, 20, 21, 22, 23, 24], "out": [25, 26, 27, 28], "state": [0, 0, 0, 1]},
    {"type": "ram-16x4", "pos": [450, 320], "in": [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], "out": [49, 50, 51, 52], "content": ["0000", "0000", "0000", "0000", "0000", "0000", "1110", "1110", "1110", "1001", "1001", "1001", "1001", "1111", "1001", "1001"]}
  ],
  "wires": [[13, 23], [14, 24], [25, 29], [26, 30], [27, 31], [28, 32], [11, 21], [12, 22], [25, 0], [26, 1], [27, 2], [28, 3], [37, 4], [25, 45], [26, 46], [27, 47], [28, 48], [53, 41], [54, 42], [55, 43], [56, 44], [53, 58], [54, 59], [55, 60], [56, 61], [49, 62], [50, 63], [51, 64], [52, 65], [49, 66], [50, 67], [51, 68], [52, 69]]
}
```

## Projet final

Ouvrez l'[éditer logique](https://logic.modulo-info.ch/) dans une page entière du navigateur et choisissez un des projets suivants:

1. Complétez l'architecture du CPU 4004 pour en faire un processeur fonctionnel.  
Voici le [jeu d'instructions](http://e4004.szyc.org/iset.html) complet.

1. Créez une calculatrice avec les touches 0 à 10, les opérations + et -, et un affichage à 7 segments avec 4 chiffres ou plus. Le point décimal est optionnel.

1. Créez une horloge avec un affichage à 7 segments du style `HH:MM:SS`, avec des boutons **up/down** pour mettre le temps.

1. Créez un minuteur avec un affichage à 7 segments du style `MM:SS` qui décompte, avec des boutons **up/down** pour mettre le temps, et des boutons **start/stop/clear**.

1. Créez un chronomètre avec un affichage à 7 segments du style `MM:SS.S` qui affiche des dixièmes de seconde. Ajoutez des boutons **start/stop/clear**.

## Nand Game

Dans le jeu [Nand Game](https://nandgame.com/) vous allez construire un ordinateur à partir de composants de base.

Le jeu se compose d'une série de niveaux. Dans chaque niveau, vous êtes chargé de construire un composant qui se comporte selon une spécification. Ce composant peut ensuite être utilisé comme bloc de construction dans le niveau suivant.

Le jeu ne nécessite aucune connaissance préalable de l'architecture informatique ou des logiciels, et ne nécessite aucune compétence en mathématiques au-delà de l'addition et de la soustraction. (Cela demande un peu de patience - certaines tâches peuvent prendre un certain temps à résoudre !)

Votre première tâche est de créer un composant nand (Non-Et).

Bonne chance!
