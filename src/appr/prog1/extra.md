# Extra

### Hypnose

```{codeplay}
from turtle import *
tracer(0)
width(10)
color('blue')

def star(n=7, a=400):
    for i in range(n):
        forward(a)
        backward(a)
        left(360/n)

while True:
    clear()
    star(13)
    left(1)
    update()
```



### Spiral

```{codeplay}
from turtle import *
tracer(0)
width(5)

a = 0
b = 0

def spiral(n=10):
    goto(0, 0)
    for i in range(200):
        forward(i)
        left(360/n)

while True:
    clear()
    seth(a)
    a += 1
    color('red')
    spiral()
    
    seth(b)
    b += -1
    color('blue')
    spiral(-10)
    update()
```

## Le coronavirus

Le nom « coronavirus » vient du latin et signifie « virus à couronne ». Son apparence sous un microscope électronique montre une frange de grandes projections bulbeuses qui évoquent une couronne solaire.

Dans la fonction `corona()` les paramètres sont :

- la distance entre projections `a`
- la longueur de la projection `d`
- le nombre de projections `n`

```{codeplay}
:file: def10.py
from turtle import *
getscreen().bgcolor('azure')
up()

def corona(a=10, d=20, n=24):
    down()
    for i in range(n):
        left(90  - 180/n)
        forward(d)
        dot()
        backward(d)
        right(90 + 180/n)
        forward(a)
    up()

corona()
```

**Exercice** : Ajoutez 3 autres virus avec d'autres valeurs pour `a`, `d` et `n`.

## Squid Game logo

Squid Game, ou Le Jeu du calmar, est une série télévisée dramatique de survie sud-coréenne de 9 épisodes, diffusée dans le monde entier en 2021 sur Netflix.
La série raconte l'histoire d'un groupe de personnes, fortement endettées, voire ruinées, qui risquent leur vie dans un jeu de survie mystérieux avec comme récompense une somme énorme.

Nous définissons une fonction `polygone(a, n)` pour dessiner le cercle, le triangle et le carré du logo.

```{codeplay}
:file: def11.py
from turtle import *
getscreen().bgcolor('peru')
width(5)
up()

def polygone(a, n):
    down()
    for i in range(n):
        forward(a)
        left(360/n)
    up()
    
backward(150)
polygone(10, 36)
forward(100)
polygone(120, 3)
forward(170)
polygone(100, 4)
```

**Exercice** : Ajoutez votre nom et vos coordonnées à la carte de visite en utilisant la fonction `write()`.