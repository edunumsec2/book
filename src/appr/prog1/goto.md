
# Aller - `goto(x, y)`

La fonction `goto(x, y)` permet d'aller à une position `(x, y)`.

## Dessiner un polygone

Nous définissons un tuple de points, et dessinons le polygone.

```{codeplay}
from turtle import *

poly = ((0, 0), (200, 0), (200, 100), (100, 150), (0, 100), (0, 0))

for p in poly:
    goto(p)
    write(p)
```

## Numéroter les sommets

```{codeplay}
from turtle import *

poly = ((0, 0), (200, 0), (200, 100), (100, 150), (0, 100), (0, 8))

i = 0
for p in poly:
    goto(p)
    write(i)
    i = i + 1
```

## Déplacer un polygone

```{codeplay}
from turtle import *

poly = ((0, 0), (200, 0), (200, 100), (100, 150), (0, 100), (0, 0))

for p in poly:
    goto(p)
    write(p)
    
color('red')
for p in poly:
    q = p[0] - 150, p[1] - 50
    goto(q)
    write(q)
```

## Changer l'échelle

```{codeplay}
from turtle import *

poly = ((0, 0), (200, 0), (200, 100), (100, 150), (0, 100), (0, 0))

for p in poly:
    goto(p)
    write(p)
    
color('red')
for p in poly:
    q = 0.7 * p[0] - 200, 0.7 * p[1] - 100
    goto(q)
    write(q)
```

## Titre

```{codeplay}


```

## Titre

```{codeplay}


```
