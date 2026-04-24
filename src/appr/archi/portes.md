# Portes logiques

Les portes logiques sont des composants électroniques (eux-mêmes constitués en général de transistors et résistances)
qui ont une ou plusieurs entrées binaires (c'est-à-dire 0 ou 1) et qui combinent ces entrées pour produire une sortie
donnée, également binaire. La manière dont la sortie est calculée dépend du type de la porte. Chaque type de porte
correspond à une opération logique spécifique. On se propose à présent
d'étudier les portes ET, OU, OU-X et NON. 

## Porte ET

La première porte est la porte **ET**. Elle a deux entrées, qu'on appellera $X$ et $Y$, et une sortie $Z$. $Z$ sera 1
si et seulement si aussi bien $X$ que $Y$ valent 1. D'où son nom: il faut que $X$ **_et_** $Y$ soient à 1 pour obtenir un 1 sur la sortie.

En énumérant les quatre possibilités pour les entrées, on peut écrire ce qu'on appelle {glo}`tableverite|table de vérité` pour la porte **ET** :

| $X$ | $Y$ | $Z$ |
| :-: | :-: | :-: |
| 0   | 0   | 0   |
| 1   | 0   | 0   |
| 0   | 1   | 0   |
| 1   | 1   | 1   |

On peut dessiner des diagrammes avec des portes logiques. Ce ne sont pas des diagrammes électroniques, ils cachent une
partie de la complexité réelle des circuits. Dans un tel diagramme logique, la porte **ET** est représentée ainsi :

```{logic}
:height: 60
:mode: static

{"v": 3, "opts": {"showDisconnectedPins": true}, "gates": [{"type": "AND", "pos": [50, 30], "in": [0, 1], "out": 2}]}
```

Sur ce schéma logique, les entrées sont à gauche, la sortie à droite et la porte est connectée au milieu. Les circuits sont représentés en noir
s'ils véhiculent un «0» et avec une couleur s'ils véhiculent un «1».

Cliquez sur {logicref}`tryout_and.x|l'entrée X` ou {logicref}`tryout_and.y|l'entrée Y` pour changer leurs valeurs et observez le comportement
de la {logicref}`tryout_and.z|sortie Z`. Est-ce que cela correspond à la table de vérité ci-dessus ?

```{logic}
:ref: tryout_and
:height: 100
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 3, "ref": "x", "name": "X", "val": 0},
    {"pos": [50, 70], "id": 4, "ref": "y", "name": "Y", "val": 0}
  ],
  "out": [{"pos": [220, 50], "id": 5, "ref": "z", "name": "Z"}],
  "gates": [{"type": "AND", "pos": [150, 50], "in": [0, 1], "out": 2}],
  "wires": [[3, 0], [4, 1], [2, 5]]
}
```

````{togofurther} l'intérieur d'une porte ET
Comment une porte **ET** est-elle elle-même construite ? Cela a déjà été mentionné : avec d'autres composants électroniques plus simples. En simplifiant un peu,
on peut considérer qu'une porte **ET** est constituée de deux transistors (avec quelques résistances en plus) :

```{figure} media/andgatetransistor.svg
---
width: 200px
---
```

Ici, les deux transistors sont les composants symbolisés par un cercle. Rappelons qu'ils laissent passer du courant de haut en bas lorsqu'ils détectent un
courant sur l'entrée qui vient de la gauche. Ici, comme on a en haut une tension de 5 volts, on aura une tension similaire sur la sortie $Z$ que si à la fois
les entrées $X$ et $Y$ sont «actives» — donc lorsque les deux transistors sont «ouverts». Sinon, on aura une tension de 0 volt sur la sortie $Z$.
````




## Porte OU

Pour que la sortie de la porte **OU** vaille 1, il suffit que l'une des deux entrées $X$ ou $Y$ vaille 1.

Voici sa table de vérité:

| $X$ | $Y$ | $Z$ |
| :-: | :-: | :-: |
| 0   | 0   | 0   |
| 1   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 1   | 1   |

On notera que le **OU** logique est un peu différent du «ou» que l'on utilise en général à l'oral : on voit à la dernière ligne de la
table de vérité que la sortie $Z$ vaut également 1 si les deux entrées $X$ et $Y$ valent 1. À l'oral, le «ou» est en général interprété
comme _exclusif_: si l'on propose à un ami un bonbon _ou_ une glace, on exclut la possibilité qu'il choisisse les deux. Ce n'est pas le
cas pour le **OU** logique.

Essayez la porte **OU** :

```{logic}
:height: 100
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 3, "name": "X", "val": 0},
    {"pos": [50, 70], "id": 4, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [220, 50], "id": 5, "name": "Z"}],
  "gates": [{"type": "OR", "pos": [150, 50], "in": [0, 1], "out": 2}],
  "wires": [[3, 0], [4, 1], [2, 5]]
}
```

````{togofurther} l'intérieur d'une porte OU
Voici comment une porte **OU** peut être construite avec deux transistors :

```{figure} media/orgatetransistor.svg
---
width: 200px
---
```
````


## Porte OU-X

Pour que la sortie de la porte **OU-X** (une écriture raccourcie de "ou exclusif")  vaille 1, il faut qu'une des deux entrées $X$ ou $Y$ vaille 1 et que l'autre vaille 0.

Voici sa table de vérité:

| $X$ | $Y$ | $Z$ |
| :-: | :-: | :-: |
| 0   | 0   | 0   |
| 1   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 1   | 0   |

On notera que le **OU-X** logique correspond mieux au «ou» que l'on utilise en général à l'oral : on voit à la dernière ligne de la
table de vérité que la sortie $Z$ vaut également 0 si les deux entrées $X$ et $Y$ valent 1. 

Essayez la porte **OU-X** :

```{logic}
:height: 100
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 3, "name": "X", "val": 0},
    {"pos": [50, 70], "id": 4, "name": "Y", "val": 0}
  ],
  "out": [{"pos": [220, 50], "id": 5, "name": "Z"}],
  "gates": [{"type": "XOR", "pos": [150, 50], "in": [0, 1], "out": 2}],
  "wires": [[3, 0], [4, 1], [2, 5]]
}
```

## Porte NON

Cette porte est plus simple : elle n'a qu'une entrée, et sa sortie se contente d'inverser la valeur en entrée. On l'appelle d'ailleurs aussi un _inverseur_.

Voici sa table de vérité :

| $X$ | $Z$ |
| :-: | :-: |
| 0   | 1   |
| 1   | 0   |

Essayez l'inverseur :

```{logic}
:height: 60
:mode: tryout

{
  "v": 3,
  "in": [{"pos": [50, 30], "id": 0, "name": "X", "val": 0}],
  "out": [{"pos": [220, 30], "id": 2, "name": "Z"}],
  "gates": [{"type": "NOT", "pos": [130, 30], "in": 1, "out": 3}],
  "wires": [[0, 1], [3, 2]]
}
```
````{togofurther} l'intérieur d'une porte NON



Voici comment un inverseur peut être construit avec un transistor :

```{figure} media/notgatetransistor.svg
---
width: 200px
---
```
````

Ensemble, les portes **ET**, **OU** et **NON** représentent les relations logiques de la {glo}`conjonction|conjonction`,
la {glo}`disjonction|disjonction` et la {glo}`negation|négation`. Même si on ne les appelle pas ainsi, on utilise tous
les jours des relations logiques de conjonction, de disjonction et de négation.

 * La **conjonction** est ainsi l'«intersection logique» de deux propositions. Si on dit «je vais à la piscine s'*il fait beau* **ET** *que mes amis m'accompagnent*», on utilise la conjonction.
 * Au contraire, si on dit «je vais à la piscine s'*il fait beau* **OU** *que mes amis m'accompagnent*», on utilise
 la **disjonction**, qui est comme une sorte de «somme logique» de deux propositions (même si, comme noté plus haut,
 le «ou», dans le langage courant, est généralement exclusif, contrairement au **OU** logique, qui est inclusif).
 * La **négation** est encore plus évidente, puisque la proposition «je ne vais pas à la piscine» est simplement la
 négation, ou l'inverse, de la proposition «je vais à la piscine». 

````{exercise}
Identifier les trois portes logiques suivantes en vérifiant la sortie en fonction des entrées:
```{logic}
:id: 1BPIU5
:height: 180
:mode: tryout

{ // JSON5
  v: 8,
  components: {
    in0: {type: 'in', pos: [80, 65], id: 0, name: 'A'},
    in1: {type: 'in', pos: [80, 115], id: 1, name: 'B'},
    or0: {type: 'or', pos: [245, 30], in: [2, 3], out: 4, showAsUnknown: true},
    xor0: {type: 'xor', pos: [245, 90], in: [8, 9], out: 10, showAsUnknown: true},
    and0: {type: 'and', pos: [245, 150], in: [11, 12], out: 13, showAsUnknown: true},
    out0: {type: 'out', pos: [355, 30], id: 14, name: 'X'},
    out1: {type: 'out', pos: [355, 90], id: 15, name: 'Y'},
    out2: {type: 'out', pos: [355, 150], id: 16, name: 'Z'},
  },
  wires: [[0, 2], [1, 9], [1, 12], [4, 14], [10, 15], [13, 16], [0, 8], [0, 11], [1, 3]]
}
```
````
```{solution}
Il s'agit, de haut en bas, de portes OU, OU-X, et ET. 
```

```{related}
Une application pour s'exercer à l'interprétation des conjonctions, disjonctions et négations logiques: [The Boolean Game](https://booleangame.com/)
```
