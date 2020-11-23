# Corrigé - Exercices avec des portes logiques

:::{admonition,error} Corrigé

Corrigés des exercices sur les portes logiques.

Les exercices dont les résultats sont évidents ne font pas l'objet d'un corrigé.

:::

::::{admonition,attention} Exercice 5 : lois de De Morgan

[Corrigé](media/Logidules/Ex5_DeMorgan/EquivalencesDeMorgan) pour le simulateur de Logidules

::::

::::{admonition,attention} Exercice 6 : demi-additionneur



::::

::::{admonition,attention} Exercice 7 : additionneur

1. Table de vérité complétée :

|  A  |  B  | $C_{in}$  | $S$             | $C_{out}$ |
|:---:|:---:|:---------:|:---------------:|:---------:|
|  0  |  0  |  0        |       0         |   0       |
|  0  |  0  |  1        |       1         |   0       |
|  0  |  1  |  0        |       1         |   0       |
|  0  |  1  |  1        |       0         |   1       |
|  1  |  0  |  0        |       1         |   0       |
|  1  |  0  |  1        |       0         |   1       |
|  1  |  1  |  0        |       0         |   1       |
|  1  |  1  |  1        |       1         |   1       |

2. Proposition de schémas pour un circuit logique :
:::{figure} retenue
<img src="media/Logidules/Ex8_Add/add1.jpg"  width="200px">

Additionneur avec retenue 1
:::

:::{figure} retenue
<img src="media/Logidules/Ex8_Add/add2.jpg"  width="200px">

Additionneur avec retenue 1
:::

Et le [corrigé](media/Logidules/Ex8_Add/Additionneur) pour le simulateur de logidules

::::
