## Les portes logiques de base

### Représentations

````{question}
```{logic}
:height: 60
:mode: static

{"v": 3, "opts": {"showDisconnectedPins": true}, "gates": [{"type": "AND", "pos": [50, 30], "in": [0, 1], "out": 2}]}
```
De quelle porte logique s'agit-il ?
* {v}`AND (ET)`
* {f}`OR (OU)`
* {f}`NOT (NON)`
* {f}`XOR (OU X)`
````

````{question}
```{logic}
:height: 60
:mode: static

{"v": 3, "opts": {"showDisconnectedPins": true}, "gates": [{"type": "OR", "pos": [50, 30], "in": [0, 1], "out": 2}]}
```
De quelle porte logique s'agit-il ?
* {f}`AND (ET)`
* {v}`OR (OU)`
* {f}`NOT (NON)`
* {f}`XOR (OU X)`
````

````{question}
```{logic}
:height: 60
:mode: static

{"v": 3, "opts": {"showDisconnectedPins": true}, "gates": [{"type": "NOT", "pos": [50, 30], "in": 1, "out": 3}]}
```
De quelle porte logique s'agit-il ?
* {f}`AND (ET)`
* {f}`OR (OU)`
* {v}`NOT (NON)`
* {f}`XOR (OU X)`
````

````{question}
```{logic}
:height: 60
:mode: static

{"v": 3, "opts": {"showDisconnectedPins": true}, "gates": [{"type": "XOR", "pos": [50, 30], "in": [0, 1], "out": 2}]}
```
De quelle porte logique s'agit-il ?
* {f}`AND (ET)`
* {f}`OR (OU)`
* {f}`NOT (NON)`
* {v}`XOR (OU X)`
````
### Fonctionnement
Ici, nous cachons la représentation de la porte. Il faut donc trouver de quelle porte il s'agit en testant.

````{question}
```{logic}
:height: 160
:mode: tryout

{
  "v": 3,
  "in": [{"pos": [50, 40], "id": 0, "val": 0}, {"pos": [50, 80], "id": 1, "val": 0}],
  "out": [{"pos": [280, 60], "id": 7}],
  "gates": [{"type": "XOR", "pos": [180, 60], "in": [3, 4], "out": 6, "showAsUnknown": true}],
  "wires": [[0, 3], [1, 4], [6, 7]]
}
```
De quelle porte logique s'agit-il ?
* {f}`AND (ET)`
* {f}`OR (OU)`
* {f}`NOT (NON)`
* {v}`XOR (OU X)`
````

````{question}
```{logic}
:height: 160
:mode: tryout

{
  "v": 3,
  "in": [{"pos": [50, 40], "id": 0, "val": 0}, {"pos": [50, 80], "id": 1, "val": 0}],
  "out": [{"pos": [280, 60], "id": 7}],
  "gates": [{"type": "AND", "pos": [180, 60], "in": [3, 4], "out": 6, "showAsUnknown": true}],
  "wires": [[0, 3], [1, 4], [6, 7]]
}
```
De quelle porte logique s'agit-il ?
* {v}`AND (ET)`
* {f}`OR (OU)`
* {f}`NOT (NON)`
* {f}`XOR (OU X)`
````

````{question}
```{logic}
:height: 160
:mode: tryout

{
  "v": 3,
  "in": [{"pos": [50, 40], "id": 0, "val": 0}, {"pos": [50, 80], "id": 1, "val": 0}],
  "out": [{"pos": [280, 60], "id": 7}],
  "gates": [{"type": "OR", "pos": [180, 60], "in": [3, 4], "out": 6, "showAsUnknown": true}],
  "wires": [[0, 3], [1, 4], [6, 7]]
}
```
De quelle porte logique s'agit-il ?
* {f}`AND (ET)`
* {v}`OR (OU)`
* {f}`NOT (NON)`
* {f}`XOR (OU X)`
````

````{question}
```{logic}
:height: 160
:mode: tryout

{
  "v": 3,
  "in": [{"pos": [50, 40], "id": 0, "val": 0}],
  "out": [{"pos": [280, 60], "id": 7}],
  "gates": [{"type": "NOT", "pos": [180, 60], "in": 3, "out": 6, "showAsUnknown": true}],
  "wires": [[0, 3], [6, 7]]
}
```
De quelle porte logique s'agit-il ?
* {f}`AND (ET)`
* {f}`OR (OU)`
* {v}`NOT (NON)`
* {f}`XOR (OU X)`
````

### Tables de vérité
Dans cette série d'exercices, l'élève doit trouver de quelle porte logique il s'agit à partir de la table de vérité.

````{question}
| $X$ | $Y$ | $Z$ |
| :-: | :-: | :-: |
| 0   | 0   | 0   |
| 1   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 1   | 1   |

De quelle porte logique s'agit-il ?
* {f}`AND (ET)`
* {v}`OR (OU)`
* {f}`NOT (NON)`
* {f}`XOR (OU X)`
````

````{question}
| $X$ | $Y$ | $Z$ |
| :-: | :-: | :-: |
| 0   | 0   | 0   |
| 1   | 0   | 0   |
| 0   | 1   | 0   |
| 1   | 1   | 1   |

De quelle porte logique s'agit-il ?
* {v}`AND (ET)`
* {f}`OR (OU)`
* {f}`NOT (NON)`
* {f}`XOR (OU X)`
````

````{question}
| $X$ | $Z$ |
| :-: | :-: |
| 0   | 1   |
| 1   | 0   |

De quelle porte logique s'agit-il ?
* {f}`AND (ET)`
* {f}`OR (OU)`
* {v}`NOT (NON)`
* {f}`XOR (OU X)`
````

````{question}
| $X$ | $Y$ | $Z$ |
| :-: | :-: | :-: |
| 0   | 0   | 0   |
| 1   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 1   | 0   |

De quelle porte logique s'agit-il ?
* {f}`AND (ET)`
* {f}`OR (OU)`
* {f}`NOT (NON)`
* {v}`XOR (OU X)`
````


