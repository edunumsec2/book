# Tracer - `math`

Dans ce chapitre nous allons découvrir comment nous pouvons tracer des fonctions mathématiques pour les visualiser. Le module `math` met à disposition toute une série de constantes et de fonctions mathématiques. Nous allons explorer :

- les fonctions trigonométriques `sin()`, `cos()` et `tan()`,
- la fonction exponentielle `exp()`,
- la fonction logarithmique `log()`.

```{question}
Le module `math` met à disposition

{f}`des nouveaux opérateurs mathématiques`  
{v}`des constantes`  
{f}`des fonctions matricielles`  
{f}`des fonctions statistiques`
```

## Tracer une fonction

Pour donner une idée de ce que nous allons faire, voici tout de suite un exemple de comment tracer les deux fonctions trigonométriques `sin()` et `cos()`.

Au début du programme nous importons le module `math`. Par la suite nous pouvons accéder aux nouvelles fonctions importées `math.sin()` et `math.cos()`.

Dans l'intervalle [-300, 300] nous prenons une valeur tous les 10, ce qui nous fait 60 valeurs.

Pour adapter la fonction à l'échelle de la tortue nous changeons :

- `x` par un facteur de 50,
- `y` par un facteur de 100.

```{exercise}
Modifiez couleur, amplitude, fréquence ou nombre de points de la courbe.
```

```{codeplay}
:file: math1.py
from turtle import *
import math
up()

color('red')
for x in range(-300, 300, 10):
    y = 100 * math.sin(x/50)
    setpos(x, y)
    down()
    dot()
    
up()
color('blue')
for x in range(-300, 300, 10):
    y = 100 * math.cos(x/50)
    setpos(x, y)
    down()
    dot()
```

## Importer un module

Le mot-clé `import` permet d'importer un module. Normalement c'est dans la première ligne d'un programme qu'on importe un module. La fonction `dir()` permet de voir le contenu du module.

```{exercise}
Importez le module `random` et affichez son contenu avec `dir`.
```

```{codeplay}
:file: math2.py
import math
m = [x for x in dir(math) if not x.startswith('_')]
print(m)
print(len(m))
```

## Format `module.objet`

Pour utiliser un objet d'un module importé, il faut écrire de façon `module.objet`

- le nom du module
- le point `.` (dot)
- le nom de l'objet

Par exemple `math.pi` pour la constante $\pi$. Voici quelques exemples.

```{exercise}
Essayez la fonction `pow()` (puissance) et affichez le résultat.
```

```{codeplay}
:file: math3.py
import math

print('e =', math.e)
print('pi =', math.pi)
print('fact(7) =', math.factorial(7))
```

## Constantes

Avec l'expression `from module import obj1, obj2` nous pouvons explicitement importer des objets par nom.

Ceci nous permet de directement accéder à l'objet sans ajouter le nom du module. Nous pouvons donc écrire directement `pi` au lieu de `math.pi`.

Le module `math` contient 5 constantes:

- `e` base des logarithmes naturels (nombre d'Euler)
- `inf` symbole pour infinité
- `nan` symbole pour *not a number*
- `pi` rapport de la circonférence d'un cercle à son diamètre
- `tau` rapport de la circonférence d'un cercle à son rayon

```{exercise}
Vérifiez de façon numérique que $2\pi = \tau$.
```

```{codeplay}
:file: math4.py
from math import e, inf, nan, pi, tau

print('Constantes:')
print('e   =', e)
print('inf =', inf)
print('nan =', nan)
print('pi  =', pi)
print('tau =', tau)
```

## Fonction trigo

Voici les fonctions trigonométriques:

- `sin/cos` fonction sinus/cosinus
- `sinh/cosh` fonctions sinus/cosinus hyperboliques
- `tan/tan2` fonction tangente avec 1 ou 2 arguments
- `tanh` fonction tangente hyperbolique

Et leurs fonctions inverses (arc):

- `asin/asinh`
- `acos/acosh`
- `atan/atanh`

Dorénavant nous utilisons l'expression `from math import *` pour importer tous les objets du module `math`. Le symbole `*` représente tous les objets.

```{exercise}
Ajoutez et tracez une deuxième fonction trigonométrique dans une autre couleur.
```

```{codeplay}
:file: math5.py
from turtle import *
from math import *
up()

color('red')
for x in range(-300, 300, 10):
    y = 100 * sin(x/50)
    setpos(x, y)
    down()
    dot()
```

## Afficher les axes

Dessinons aussi des axes, nous allons utiliser la fonction `stamp` pour dessiner la flèche de l'axe.

```{codeplay}
:file: math6.py
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

Nous pouvons re-écrire le code de façon plus court et plus lisible en définissant une fonction `axe()`.

Cette fonction utilise deux paramètres `p` et `q` qui sont un tuple qui représente^ les coordonnées du point de départ et du point d'arrivée.

```{codeplay}
:file: math7.py
from turtle import *
up()

def axe(p, q):
    goto(p)
    down()
    seth(towards(q))
    goto(q)
    stamp()
    up()
    
axe((-280, 0), (280, 0))
axe((0, -180), (0, 180))
```

## Afficher une grille

Avec multiples lignes horizontales et verticales nous dessinons une grille.

```{codeplay}
:file: math8.py
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

En définissant la fonction `ligne()` nous pouvons rendre le programme plus lisible.

```{exercise}
Mettez la distance `d` à 20 et à 10 et réexécutez le programme.
```

```{codeplay}
:file: math9.py
from turtle import *
speed(0)
up()
d = 40

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

for x in range(-280, 280+1, d):
    ligne((x, -180), (x, 180))
    
for y in range(-180, 180+1, d):
    ligne((-280, y), (280, y))
```

## Echelle

```{codeplay}
:file: math10.py
import math
from turtle import *
up()

n = 60
plage = -3, 6
d = plage[1] - plage[0]

for i in range(n):
    x = -300 + i * 600/n
    x_ = plage[0] + i * d/n
    goto(x, 0)
    if i % 10 == 0:
        dot()
        write(f'{x_:.1}')
```

## Tracer des fonctions

```{codeplay}
:file: math11.py
from turtle import *
from math import *
up()
    
def tracer(f, couleur='red', nom='f'):
    color(couleur)
    for x in range(-300, 250, 10):
        y = 100 * f(x/50)
        goto(x, y)
        down()
        dot()
    up()
    write(' ' + nom, font=(None, 18))

tracer(sin, 'green', 'sin')
tracer(cos)
```

Voici du code à développer.

```{codeplay}
:file: math12.py
from turtle import *
from math import *
up()
color('red')
n = 60
plage = -3, 6
d = plage[1] - plage[0]

for i in range(n):
    x = -300 + i * 600/n
    x_ = plage[0] + i * d/n
    y_ = sin(x_)
    y = 200/2 * sin(x_)
    goto(x, y)
    down()
    if i % 5 == 0:
        dot()
        write(f'{x_:.2}, {y_:.2}')
```

## arc tangente

```{codeplay}
:file: math13.py
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

## Équation de 2e degré

```{codeplay}
:file: math14.py
from turtle import *

def axes():
    backward(280)
    forward(560)
    stamp()
    backward(280)
    left(90)
    backward(180)
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
