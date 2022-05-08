(soutracteur)=
Soustracteur
============

((TODO))

## Objectifs
((TODO))


## Fiche
````{panels}
Fiche
^^^^^
* Type d'activité : travaux pratique avec le simulateur logique
* Durée : 1 période
* Par groupe : possible/recommandé

---

Résumé
^^^^^
((TODO))

````

## Déroulement

### Première partie: 

((TODO))

```{logic}
:mode: design
:height: 450
:showonly: and,or,xor,not,nand,nor,adder,alu

{
  "v": 2,
  "in": [
    {"pos": [100, 50], "id": 4, "name": "X0", "val": 1},
    {"pos": [100, 90], "id": 5, "name": "X1", "val": 0},
    {"pos": [100, 130], "id": 6, "name": "X2", "val": 0},
    {"pos": [100, 170], "id": 7, "name": "X3", "val": 0}
  ],
  "out": [
    {"type": "nibble", "pos": [350, 80], "id": [8, 9, 10, 11], "name": "X"},
    {"type": "nibble", "pos": [350, 360], "id": [0, 1, 2, 3], "name": "Y = –X"}
  ],
  "wires": [[4, 8], [5, 9], [6, 10], [7, 11]]
}
```
