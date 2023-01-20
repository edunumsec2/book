# TP CPU

Dans cette section nous mettons l'ALU, les registres, et la mémoire ensemble avec des circuits de contrôle, pour simuler un CPU (central processing unit).

## Intel 4004

Le premier CPU sur un circuit intégré fut le 4004 produit par Intel en 1971. Il contenait les éléments suivants:

- un bus 4 bits
- une ALU pour faire des additions et soustractions
- un registre accumulateur
- 16 registres de travail 4-bit
- un registre d'instruction 8-bit (IR)
- un pointeur de programme 12 bit (PC)

Voici le schéma de l'architecture du 4004.

![4004](https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/4004_arch.svg/1016px-4004_arch.svg.png)

Le circuit était embarqué dans un boitier en céramique avec seulement 16 broches.

![boitier](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Intel_C4004.jpg/640px-Intel_C4004.jpg)

## Code opération (opcode

Le code opération est l'instruction en code machine qui dit au CPU quelle opération à exécuter. Le opcode inclut souvent les registres sur lesquelles il faut agir.

- `1000RRRR` ADD additionner registre `RRRR` à l'accumulateur
- `1001RRRR` SUB soustraire registre `RRRR` de l'accumulateur
- `1101DDDD` LDM charger les données `MMMM` vers l'accumulateur

## Instruction registre (IR)

Le CPU 4004 possède des instructions qui ont 8 bits. À chaque pas de l'exécution d'un programme, une instruction est chargée dans le registre d'instruction (IR) et décodée.

- Découpez les 8 bits du registre d'instruction en deux fois 4 bits
- Ajoutez les noms **opcode** et **data** aux affichages 4-bits
- Affichez **opcode** en forme hexadécimale
- Décodez l'instruction `10000011` (additionner le contenu du registre 3 à l'accumulateur)

```{logic}
:ref: LDM
:height: 300
:showonly: in out
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [110, 60], "orient": "s", "id": [0, 1, 2, 3, 4, 5, 6, 7], "name": "instruction"}
  ],
  "out": [
    {"type": "nibble-display", "pos": [170, 190], "orient": "s", "id": [12, 13, 14, 15]},
    {"type": "nibble-display", "pos": [80, 190], "orient": "s", "id": [43, 44, 45, 46]}
  ]
}
```

## Bus 4 bits

Une ALU doit acheminer différents signaux sur un même ligne de transfert des données. On appelle un tel chemin un bus de données. Pour y connecter plusieurs sources, nous devons utiliser un multiplexeur.

- Ajoutez une deuxième entrée 4 bits
- Liez le multiplexeur et le démultiplexeur
- Ajoutez les 2 entrées de sélection
- Ajoutez 4 affichages 4 bits pour montrer tous les signaux

```{logic}
:ref: LDM
:height: 500
:showonly: in out in.nibble out.nibble-display mux-8to2 demux-4to8
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

La partie `1101` est l'opcode (LDM) et la partie `DDDD` représente les 4 bits des données à charger dans l'accumulateur.

- Liez les bits b0-b3 avec l'accumulateur
- Placez une entrée horloge (clock) vers l'accumulateur
- Placez un affichage à la sorte de l'accumulateur et à la sortie de l'ALU
- Mettez une valeur dans les bits b0-b3 et transférez-la vers l'accumulateur

```{logic}
:ref: LDM
:height: 400
:showonly: in out out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [60, 50], "orient": "s", "id": [21, 22, 23, 24, 25, 26, 27, 28], "val": "11010001", "name": "instruction"}
  ],
  "components": [
    {"type": "alu", "pos": [370, 270], "in": [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "out": [40, 41, 42, 43, 44, 45, 46]},
    {"type": "register", "pos": [200, 220], "in": [186, 187, 188, 189, 190, 191, 192], "out": [193, 194, 195, 196], "state": [1, 0, 0, 0]}
  ],
  "wires": [[193, 29], [194, 30], [195, 31], [196, 32]]
}
```

## Charger depuis reg (LD)

L'instruction `LD` (load) charge l'accumulateur avec le contenu d'un des 16 registres.

`1010RRRR``

La parte `1010` est l'opcode (LD) et la parte `RRRR` représente un des 16 registres

- Liez les bits b0-b3 avec l'entrée adressée des registres
- Placez une entrée WE et **clock** vers les registres
- Placez une entrée horloge (clock) vers l'accumulateur
- Placez un affichage à la sorte de l'accumulateur et à la sortie de l'ALU
- Mettez une valeur dans le registre et transférez-la vers l'accumulateur

```{logic}
:ref: LD
:height: 500
:showonly: in out out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [60, 50], "orient": "s", "id": [21, 22, 23, 24, 25, 26, 27, 28], "val": "11010001", "name": "instruction"},
    {"type": "nibble", "pos": [40, 260], "id": [9, 10, 11, 12], "val": [1, 1, 0, 1]}
  ],
  "components": [
    {"type": "alu", "pos": [430, 310], "in": [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "out": [40, 41, 42, 43, 44, 45, 46]},
    {"type": "ram-16x4", "pos": [130, 260], "in": [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], "out": [58, 59, 60, 61], "content": ["0000", "1011"]},
    {"type": "register", "pos": [260, 260], "in": [126, 127, 128, 129, 130, 131, 132], "out": [133, 134, 135, 136], "state": [1, 1, 0, 1]}
  ],
  "wires": [[133, 29], [134, 30], [135, 31], [136, 32], [58, 129], [59, 130], [60, 131], [61, 132], [9, 50], [10, 51], [11, 52], [12, 53]]
}
```

## Choix de source (LD/LDM)

Avec les deux opcode différents, le circuit de décodage du CPU choisit un registre ou une donnée immédiate comme valeur à charger dans l'accumulateur.

- Liez les bits b0-b3 avec l'entrée adressée des registres, mais aussi avec l'entrée du multiplexeur
- Placez une entrée WE et **clock** vers les registres
- Placez une entrée horloge (clock) vers l'accumulateur
- Placez un affichage à la sortie de l'accumulateur et à la sortie de l'ALU
- Mettez une valeur dans le registre et transférez-la vers l'accumulateur
- Configurez le multiplexeur et chargez une valeur immédiate dans l'accumulateur

```{logic}
:ref: LD2
:height: 500
:showonly: in out out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [80, 40], "orient": "s", "id": [21, 22, 23, 24, 25, 26, 27, 28], "val": "10100011", "name": "instruction"},
    {"type": "nibble", "pos": [60, 310], "id": [9, 10, 11, 12], "val": [1, 0, 0, 0]}
  ],
  "components": [
    {"type": "alu", "pos": [530, 310], "in": [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "out": [40, 41, 42, 43, 44, 45, 46]},
    {"type": "ram-16x4", "pos": [150, 310], "in": [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], "out": [58, 59, 60, 61], "content": ["0000", "1011", "0000", "0001"]},
    {"type": "register", "pos": [360, 260], "in": [126, 127, 128, 129, 130, 131, 132], "out": [133, 134, 135, 136], "state": [1, 1, 0, 0]},
    {"type": "mux-8to4", "pos": [280, 260], "in": [138, 139, 140, 141, 142, 143, 144, 145, 146], "out": [147, 148, 149, 150]}
  ],
  "wires": [[133, 29], [134, 30], [135, 31], [136, 32], [9, 50], [10, 51], [11, 52], [12, 53], [147, 129], [148, 130], [149, 131], [150, 132], [58, 142], [59, 143], [60, 144], [61, 145]]
}
```

## Addition (ADD)

L'addition et la soustraction se distinguent dans l'opcode d'un seul bit.

- `1000RRRR` ADD additionner registre `RRRR` à l'accumulateur
- `1001RRRR` SUB soustraire registre `RRRR` de l'accumulateur

Créez le circuit pour décoder et exécuter ces deux instructions.

- Liez les bits b0-b3 du IR avec l'entrée adressée des registres
- Liez le bit b4 du IR avec l'entrée Op de l'ALU
- Liez la sortie de l'ALU avec l'entrée de l'accumulateur
- Placez un affichage à la sortie de l'accumulateur, des registres et  de l'ALU
- Mettez une instruction ADD/SUB valide dans le IR
- Exécuté l'instruction

```{logic}
:ref: LD2
:height: 500
:showonly: in out out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [80, 40], "orient": "s", "id": [21, 22, 23, 24, 25, 26, 27, 28], "val": "10010001", "name": "instruction"},
    {"type": "nibble", "pos": [60, 310], "id": [9, 10, 11, 12], "val": [0, 1, 0, 0]},
    {"pos": [270, 240], "id": 151, "val": 0, "isPushButton": true},
    {"pos": [50, 370], "id": 152, "val": 0, "isPushButton": true},
    {"pos": [130, 420], "orient": "n", "id": 153, "name": "WE", "val": 1},
    {"pos": [350, 410], "orient": "n", "id": 0, "val": 0, "isPushButton": true}
  ],
  "components": [
    {"type": "alu", "pos": [480, 260], "in": [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39], "out": [40, 41, 42, 43, 44, 45, 46]},
    {"type": "ram-16x4", "pos": [150, 310], "in": [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], "out": [58, 59, 60, 61], "content": ["0000", "1011", "0000", "0010"]},
    {"type": "register", "pos": [350, 180], "in": [126, 127, 128, 129, 130, 131, 132], "out": [133, 134, 135, 136], "state": [1, 1, 1, 0]}
  ],
  "wires": [[133, 29], [134, 30], [135, 31], [136, 32], [9, 50], [10, 51], [11, 52], [12, 53], [151, 126], [152, 47], [153, 48], [0, 128], [61, 36], [60, 35], [59, 34], [58, 33]]
}
```

## Program counter (PC)

Le pointeur de programme, PC (program counter), pointe toujours à la prochaine instruction dans la mémoire de programme. Le contenu à l'adresse pointé par le PC est celui qui est chargé dans le registre d'instruction (IR) et exécuté au prochain pas.

- Liez la sortie du PC avec l'entrée A du l'ALU pour incrémenter de 1 à chaque pas
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
