# Exercices

## Exercice 1:

### A: du réseau à la table de routage

On donne le réseau de routeurs suivants où les routeurs sont numérotés de 1 à 8, et les interfaces de A à C.

```{figure} media/res1.svg
---
width: 60%
```

Compléter les tables de routage suivantes pour les routeurs 1, 3 et 5. 

Routeur 1:

| Destination | Interface | Distance |
|-------------|-----------|----------|
|        2    |           |         |
|        3    |           |         |
|        4    |           |         |
|        5    |           |         |
|        6    |           |         |
|        7    |           |         |
|        8    |           |         |

Routeur 3:

| Destination | Interface | Distance |
|-------------|-----------|----------|
|       1     |           |          |
|       2     |           |          |
|       4     |           |          |
|       5     |           |          |
|       6     |           |          |
|       7     |           |          |
|       8     |           |          |

Routeur 5:

| Destination | Interface | Distance|
|-------------|-----------|---------|
|        1    |           |         |
|        2    |           |         |
|        3    |           |         |
|        4    |           |         |
|        6    |           |         |
|        7    |           |         |
|        8    |           |         |


### B: des tables de routage au réseau

On considère un réseau de routeurs, dont on donne les tables de routages. Pour chaque cas, proposer un réseau cohérent avec ces tables de routage. 

Routeur 1:

| Destination | Interface | Distance |
|-------------|-----------|----------|
|        2    |     B     |   1      |
|        3    |     C     |   1      |
|        4    |     A     |   1      |
|        5    |     A     |   2      |


Routeur 2:

| Destination | Interface | Distance |
|-------------|-----------|----------|
|        1    |    B      |   1      |
|        3    |    A      |   1      |
|        4    |    B      |   2      |
|        5    |    A      |   2      |

Routeur 3:

| Destination | Interface | Distance |
|-------------|-----------|----------|
|       1     |    A      |   1      |
|       2     |    B      |   1      |
|       4     |    A      |   2      |
|       5     |    C      |   1      |

Routeur 4:

| Destination | Interface | Distance |
|-------------|-----------|----------|
|       1     |    B      |   1      |
|       2     |    B      |   2      |
|       3     |    A      |   2      |
|       5     |    A      |   1      |


Routeur 5:

| Destination | Interface | Distance|
|-------------|-----------|---------|
|        1    |     A     |    2    |
|        2    |     A     |    2    |
|        3    |     A     |    1    |
|        4    |     B     |    1    |





### C: routage
On donne les tables de routage suivantes d'un réseau de routeurs. Indiquer par quels routeurs passe un message pour aller atteindre sa destination depuis son point de départ. 


Routeur 1:

| Destination | Interface | Distance |
|-------------|-----------|----------|
|        2    |     A     |   2      |
|        3    |     A     |   1      |
|        4    |     A     |   3      |
|        5    |     A     |   3      |
|        6    |     A     |   2      |

Routeur 2:

| Destination | Interface | Distance |
|-------------|-----------|----------|
|        1    |    C      |   2      |
|        3    |    C      |   1      |
|        4    |    A      |   1      |
|        5    |    B      |   1      |
|        6    |    C      |   2      |

Routeur 3:

| Destination | Interface | Distance |
|-------------|-----------|----------|
|       1     |    C      |   1      |
|       2     |    A      |   1      |
|       4     |    A      |   2      |
|       5     |    A      |   2      |
|       6     |    B      |   1      |

Routeur 4:

| Destination | Interface | Distance |
|-------------|-----------|----------|
|       1     |    A      |   3      |
|       2     |    A      |   1      |
|       3     |    A      |   2      |
|       5     |    A      |   2      |
|       6     |    A      |   3      |


Routeur 5:

| Destination | Interface | Distance |
|-------------|-----------|----------|
|       1     |    A      |   3      |
|       2     |    A      |   1      |
|       3     |    A      |   2      |
|       4     |    A      |   2      |
|       6     |    A      |   3      |



| Départ | Destination| Chemin  |
|--------|------------|---------|
|  4     |    1       |         |
|  3     |    5       |         |
|  1     |    6       |         |
|  6     |    1       |         |
|  4     |    3       |         |
