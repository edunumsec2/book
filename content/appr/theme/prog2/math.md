# Tracer - `math`

Le module `math` permet d'importer toute une série de constantes et fonctions mathématiques.

## Importer un module

Le mot-clé `import` permet d'importer un module. La fonction `dir()` permet de voir le contenu du module.
Normalement c'est dans la première ligne d'un programme qu'on importe un module.

```{codeplay}
import math
print(dir(math))
```

**Exercice :** importez le module `random` et affichez son contenu avec `dir`.

## Format `module.objet`

Pour utiliser un objet du module importé, il faut faire précéder le nom de l'objet par le nom du module, séparé d'un point, par exemple `math.pi` pour la constante $\pi$.

```{codeplay}
import math

print('e =', math.e)
print('pi =', math.pi)
print('fact(7) =', math.factorial(7))
```

**Exercice :** utilisez la fonction `pow()` (power = puissance) et affichez le résultat.

On retrouve dans le module `math` des fonctions :

- arithmétiques,
- logarithmiques et exponentielles,
- trigonométriques.

## Constantes

Nous pouvons explicitement importer des objets avec les mots-clés `from x import y`. 
Ceci nous permet de directement accéder au nom de l'objet sans ajouter le nom du module. Nous pouvons donc écrire directement `pi` au lieu de `math.pi`.

Parmi ces objets il y en a 5 qui sont des constantes:

- `e  ` base des logarithmes naturels (nombre d'Euler)
- `inf` symbole pour infinité
- `nan` symbole pour *not a number*
- `pi ` rapport de la circonférence d'un cercle à son diamètre
- `tau` rapport de la circonférence d'un cercle à son rayon

```{codeplay}
from math import e, inf, nan, pi, tau

print('Constantes:')
print('e   =', e)
print('inf =', inf)
print('nan =', nan)
print('pi  =', pi)
print('tau =', tau)
```

## Fonctions trigonométriques

Voici les fonctions trigonométriques:

- `sin/cos` fonction sinus/cosinus
- `sinh/cosh` fonctions sinus/cosinus hyperbolique
- `tan/tan2` fonction tangente avec 1 ou 2 arguments
- `tanh` fonction tangente hyperbolique

Et leurs fonctions inverses (arc):

- `asin/asinh`
- `acos/acosh`
- `atan/atanh`

Dorénavant nous utilisons l'expression `from math import *` pour importer tous les objets du module `math`. Le symbole `*` signifie tout.
Affichons donc les fonctions `sin()` et `cos()` avec deux couleurs différentes.

```{codeplay}
from turtle import *
from math import *
up()

color('red')
for x in range(-300, 300, 10):
    y = 100 * sin(x/50)
    setpos(x, y)
    down()
    dot()
    
up()
color('blue')
for x in range(-300, 300, 10):
    y = 100 * cos(x/50)
    setpos(x, y)
    down()
    dot()
```

## Afficher les axes

Dessinons aussi des axes :

```{codeplay}
from turtle import *
width(1)
up()

goto(-280, 0)
down()
goto(280, 0)
stamp()
up()

goto(0, -180)
left(90)
down()
goto(0, 180)
stamp()
up()
```

```{codeplay}
import math
from turtle import *

for x in range(-6, 7, 1):
    setx(x * 50)
    dot()
    write(' ' + str(x))
```

## Fonction exponentielle

```{codeplay}
from turtle import *
from math import *

for x in range(-5, 6):
    goto(x * 50, 0)
    dot()
    write(x)
    
up()

for x in range(-5, 6):
    y = exp(x)
    goto(x * 50, y * 50)
    down()
    dot()
```

## Afficher une grille

```{codeplay}
from turtle import *
width(1)
speed(0)
up()

d = 40
for x in range(-280, 280+1, d):
    goto(x, -180)
    down()
    goto(x, 180)
    up()
    
for y in range(-180, 180+1, d):
    goto(-280, y)
    down()
    goto(280, y)
    up()
```

## Grapher des fonctions

```{codeplay}
from turtle import *
from math import *
up()
    
def graph(f, col, name):
    color(col)
    for x in range(-300, 250, 10):
        y = 100 * f(x/50)
        goto(x, y)
        down()
        dot()
    up()
    write(' ' + name, font=(None, 18))

graph(sin, 'green', 'sin')
graph(cos, 'red', 'cos')
```

## arc tangente

```{codeplay}
from turtle import *
from math import *
up()
    
def graph(f, col, name):
    color(col)
    for x in range(-300, 250, 10):
        y = 100 * f(x/50)
        goto(x, y)
        down()
        dot()
    up()
    write(' ' + name, font=(None, 18))

graph(atan, 'red', 'atan')
graph(cos, 'blue', 'cos')
```

## Equation de 2e degré

```{codeplay}
from turtle import *

def axes():
    back(280)
    forward(560)
    stamp()
    back(280)
    left(90)
    back(180)
    forward(360)
    stamp()
    up()

def f(x): 
    return 3 * x ** 2 - 5 * x - 40

def tracer():
    color('red')    
    for x in range(-5, 6):
        goto(50 * x, 2 * f(x))
        down()
        dot()
        
axes()
tracer()
```

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```
