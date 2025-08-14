# Théorie - Coloration de graphe

## Définitions
La *coloration d'un graphe* consiste à attribuer une couleur à chaque sommet de sorte que
deux sommets adjacents n’aient jamais la même couleur.
Le *nombre chromatique* est le nombre minimal de couleurs nécessaires pour y parvenir.

## Algorithme de Welsh-Powell

L'algorithme de Welsh-Powell permet d'obtenir une coloration de graphe. Pour appliquer cet
algorithme, on peut s'aider d'un tableau où chaque ligne correspond à un sommet du graphe
et indique son degré (c'est-à-dire le nombre de voisins) et la liste de ses voisins.
Les sommets sont ordonnés par degrés. L'agorithme de Welsh-Powell peut être résumé par le
logigramme ci-dessous: 

```{figure} media/logigramme.png
---
width: 300
align: center
---
```

## Exemple d'application

<!-- ```{figure} media/exemple.png -->
<!-- --- -->
<!-- width: 300 -->
<!-- align: left -->
<!-- --- -->
<!-- ``` -->

<!-- | Sommet | Degré |Voisins  | -->
<!-- |--------|-------|---------| -->
<!-- |        |       |         | -->
<!-- |        |       |         | -->
<!-- |        |       |         | -->
<!-- |        |       |         | -->
<!-- |        |       |         | -->
<!-- |        |       |         | -->
<!-- |        |       |         | -->
<!-- |        |       |         | -->

```{csv-table} Liste des sommets
:header: Sommet, Degré, Voisins
:align: left

,,
,,
,,
,,
,,
,,
,,
,,
```

```{figure} media/exemple.png
---
width: 300
align: right
---
```
