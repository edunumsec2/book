# Editer - `onclick()`

La souris est l'outil principal pour interagir dans un programme graphique. Dans un éditeur graphique, le
clic de souris sert à :

- faire des choix dans un menu,
- ajouter des points,
- dessiner des lignes,
- créer des rectangles et cercles.

## Hello mouse

Ce programme interactif dessine une ligne qui commence au centre et va vers l'endroit du clic de la souris.

```{codeplay}
from turtle import *
s = getscreen()

hideturtle()
speed(0)
width(10)
forward(200)

def f(x, y):
    home()
    clear()
    goto(x, y)

s.onclick(f)
```

## Astérisque

Ce programme interactif dessine un astérisque avec des lignes qui commencent toutes au centre et vont vers le clic de la souris.

```{codeplay}
from turtle import *
s = getscreen()
s.bgcolor('orange')

hideturtle()
speed(0)
color('white')
width(10)
forward(200)

def f(x, y):
    home()
    goto(x, y)

s.onclick(f)
```

## Palette de couleur

Dans un programme de dessin, la couleur actuelle peut souvent être choisi en cliquant dans une palette.

Le tuple `couleurs` contient une liste de couleurs. Il est est utilisé pour

- dessiner une palette (menu) coloriée
- déterminer l'index de la couleur lors de'un clique.

```{exercise}
Cliquez sur la palette de couleurs pour choisir une couleur.  
Cliquez dans le canevas, pour ajouter un point dans cette couleur.
```

```{codeplay}
from turtle import *
s = getscreen()
speed(0)
up()

couleurs = ('black', 'gray', 'brown', 'red', 'orange',  
            'lime', 'green', 'cyan', 'blue', 'magenta')
p0 = (-280, 150)
d = 30

goto(p0[0]+d/2, p0[1]+d/2)
for c in couleurs:
    dot(d, c)
    forward(d)

def f(x, y):
    if p0[0] < x < p0[0] + d*len(couleurs): 
        if p0[1] < y < p0[1] + d:
            i = (x-p0[0]) // d
            color(couleurs[i])
            return
    goto(x, y)
    down()
    dot(d/2)

s.onclick(f)
s.listen()
```

## Palette de taille

Dans un programme de dessin, la couleur actuelle peut souvent être choisi en cliquant dans une palette.

```{exercise}
Cliquez sur la palette de taille pour choisir une taille.  
Cliquez dans le canevas pour ajouter un point de cette taille.
```

```{codeplay}
from turtle import *
s = getscreen()
speed(0)
up()

tailles = (10, 20, 30, 40, 50)
taille = 10
p0 = (-280, 150)
d = 30

goto(p0[0]+d/2,  p0[1]+d/2)
for i in tailles:
    dot(d, 'lightgray')
    write(i, align='center')
    forward(d)

def f(x, y):
    global taille
    if p0[0] < x < p0[0] + d*len(tailles): 
        if p0[1] < y < p0[1]+d:
            i = (x-p0[0]) // d
            taille = tailles[i]
            return
    goto(x, y)
    down()
    dot(taille)

s.onclick(f)
s.listen()
```

## Palette d'épaisseur

Dans un programme de dessin, la taille actuelle peut souvent être choisi en cliquant dans une palette.

```{exercise}
Cliquez sur la palette d'épaisseur pour choisir une épaisseur.  
Cliquez dans le canevas pour ajouter une ligne de cette épaisseur.
```

```{codeplay}
from turtle import *
s = getscreen()
speed(0)
up()

epaisseurs = (1, 2, 3, 5, 10)
p0 = (-280, 150)
d = 30

goto(p0[0]+d/2,  p0[1]+d/2)
for i in epaisseurs:
    dot(d, 'lightgray')
    write(i, align='center')
    forward(d)

def f(x, y):
    if p0[0] < x < p0[0] + d*len(epaisseurs): 
        if p0[1] < y < p0[1]+d:
            i = (x-p0[0]) // d
            width(epaisseurs[i])
            return
    goto(x, y)
    down()
    dot()

s.onclick(f)
s.listen()
```

## Dessiner une ligne

Dans un programme de dessin, l'élément de base est une ligne.
Deux clics définissent une ligne. Nous allons utiliser une variable booléenne `start` pour mémoriser si un clique est le début ou la fin. Si `start` est vrai, nous leveons le stylo pour juste aller vers le premier point.

Nous utilisons l'opérateur logique `not` pour inverser l'état logique de la variable `start`

```{codeplay}
from turtle import *
s = getscreen()
hideturtle()
speed(0)
start = True            # point initial

def f(x, y):
    global start        # déclarer la variable globale
    if start:
        up()
    else:
        down()
    start = not start   # inverser l'était logique
    goto(x, y)
    dot()

s.onclick(f)
s.listen()
```

## Dessiner un rectangle

Le rectangle est un élément graphique de base.

```{codeplay}
from turtle import *
s = getscreen()
speed(0)
up()
start = True        # point inital

def rectangle(p, q):
    goto(p)
    down()
    setx(q[0])      # segmant 1 (horizontal)
    goto(q)         # segmant 2 (vertical)
    setx(p[0])      # segment 3 (horizontal)
    goto(p)         # segment 4 (vertical)
    up()

def f(x, y):
    global start, p
    goto(x, y)
    dot()
    if start:
        p = x, y    # mémoriser point initial
    else:
        rectangle(p, (x, y))
    start = not start       # inverser

s.onclick(f)
```

## Dessiner une ellipse

Ce programme interactif dessine une ellipse avec deux clics de souris.
Le premier clic dessigne le centre, le deuxième clic le sommet du rectangle entourant cette ellipse.

L'ellipse est constituté de 36 points, dont les coordonnées (x, y) sont calculé à l'aide des fonctions trigonométriques `sin()` et `cos()` du module `math`. 

```{codeplay}
from turtle import *
from math import *
s = getscreen()
speed(0)
up()
start = True           # signifie le point intial (centre)

def ellipse(p, size):
    for i in range(37):
        x = p[0] + size[0] * sin(pi * i / 18)
        y = p[1] + size[1] * cos(pi * i / 18)
        goto(x, y)
        down()
    up()

def f(x, y):
    global start, p
    goto(x, y)
    dot()
    if start:
        p = x, y        # mémoriser le centre
    else:
        ellipse(p, (x - p[0], y - p[1]))
    start = not start

s.onclick(f)
```

## Effacer un point

Jusqu'à maintenant, nous avons seulement ajouté des points et des segments au dessin.
Aucune position à été retenu en mémoire.
Pour pouvor éditer des formes dessinés, nous devons alors garder les coordonnées en mémoire.

La liste `points` contient les coordonnées de la ligne polygonale. A chaque clic nous devons :

- vérifier si nous avons cliqué sur un point existant,
- ajouter le nouveau point dans la liste des points, le cas échéant.

Quand on clique sur un point existant, nous devons l'enlever de la liste et redessiner la ligne polygonale.

```{codeplay}
from turtle import *
s = getscreen()
tracer(0)
up()

points = []
d = 20

def draw():
    clear()
    up()
    for p in points:
        goto(p)
        down()
        dot(d)
    update()
        
def dist(p, q):
    d = (p[0]-q[0])**2 + (p[1]-q[1])**2 
    return d ** 0.5

def f(x, y):
    for p in points:
        if dist((x, y), p) < d:
            points.remove(p)    # enlever le point de la liste
            draw()              # redessiner le nouveau polygone
            return              # quitter cette fonction
    goto(x, y)
    down()
    dot(d)
    points.append((x, y))       # ajouter le nouveau point à la liste
    update()
    
s.onclick(f)
```

## Marquer un point

Jusqu'à maintenant, nous avons seulement dessiné. Aucune position à été retenu en mémoire.
Pour pouvor éditer des formes dessinés, nous devons alors garder les coordonnées en mémoire.

La liste `points` contient les coordonnées de la ligne polygonale.
Si nous cliquons sur un point existant, nous le sauvegardons avec la variable `q`.

```{codeplay}
from turtle import *
s = getscreen()
tracer(0)
up()

points = []
d = 20

def draw():
    clear()
    up()
    for p in points:
        goto(p)
        down()
        dot(d, 'red' if p==q else 'black')
    update()
        
def dist(p, q):
    d = (p[0]-q[0])**2 + (p[1]-q[1])**2 
    return d ** 0.5

def f(x, y):
    global q
    for p in points:
        if dist((x, y), p) < d:
            q = p       # mémoriser le point marqué
            draw()      # redessiner les points
            return      # quitter cette fonction
    goto(x, y)
    down()
    dot(d)
    points.append((x, y))
    update()
    
s.onclick(f)
```

## Enlever le dernier point

Nous utilisons une liste `points` pour stoquer les points d'une ligne polygonale.
La touche `Back` permet d'enlever le dernier point et de redessiner la ligne.

```{codeplay}
from turtle import *
s = getscreen()
hideturtle()
tracer(0)
up()
points = []
d = 20

def back():
    points.pop()        # enlever le dernier point de la liste
    clear()
    up()
    for p in points:
        goto(p)
        down()
        dot(d)
    update()

def f(x, y):
    goto(x, y)
    down()
    dot(d) 
    points.append((x, y))
    update()
    
s.onclick(f)
s.onkey(back, 'Back')
s.listen()
```


