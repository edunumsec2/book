# Éditer - `onclick()`

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

Dans un programme de dessin, la couleur actuelle peut souvent être choisie en cliquant dans une palette.

Le tuple `couleurs` contient une liste de couleurs. Il est est utilisé pour

- dessiner une palette (menu) coloriée
- déterminer l'index de la couleur lors de'un clic.

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

Dans un programme de dessin, la couleur actuelle peut souvent être choisie en cliquant dans une palette.

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

Dans un programme de dessin, la taille actuelle peut souvent être choisie en cliquant dans une palette.

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
Deux clics définissent une ligne. Nous allons utiliser une variable booléenne `start` pour mémoriser si un clic est le début ou la fin. Si `start` est vrai, nous levons le stylo pour juste aller vers le premier point.

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
    setx(q[0])      # segment 1 (horizontal)
    goto(q)         # segment 2 (vertical)
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
Le premier clic désigne le centre, le deuxième clic le sommet du rectangle entourant cette ellipse.

L'ellipse est constituée de 36 points, dont les coordonnées (x, y) sont calculées à l'aide des fonctions trigonométriques `sin()` et `cos()` du module `math`.

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
Aucune position n’a été retenue en mémoire.
Pour pouvoir éditer des formes dessinées, nous devons alors garder les coordonnées en mémoire.

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

Jusqu'à maintenant, nous avons seulement dessiné. Aucune position n’a été retenue en mémoire.
Pour pouvoir éditer des formes dessinées, nous devons alors garder les coordonnées en mémoire.

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

Nous utilisons une liste `points` pour stocker les points d'une ligne polygonale.
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

## Afficher un polygone

Nous allons maintenant créer un éditeur de polygone. La première version permet de créer avec des clics de souris et d’afficher ce polygone, avec 6 options d'affichage:

- `d` afficher un point (dot)
- `l` afficher la ligne
- `f` afficher un remplissage (fill)
- `i` afficher l'indice du point
- `p` afficher la position du point
- `c` fermer le polygone (close)

Ces valeurs booléennes sont stockées dans un dictionnaire `settings`.  

``` python
settings = {}
settings['show_dots'] = True
```

La fonction `toggle(key)` permet de basculer `True` et `False` pour une clé et ensuite redessiner le polygone.

``` python
def toggle(key):
    settings[key] = not settings[key]
    draw()
```

La fonction `draw()` dessine tout et utilise les valeurs booléennes pour dessiner ou non les options choisies. Voici par exemple la partie qui décide s'il faut dessiner les points (dots) ou ajouter l'indice du point.

``` python
    if settings['show_dots']:
        dot()
    if settings['show_index']:
        write(i)
```

Voici le code en entier. Vous pouvez également le télécharger et exécuter avec un éditeur externe.

```{codeplay}
:file: polygon_editor1.py
===
from turtle import *
hideturtle()
tracer(0)
fillcolor('pink')

points = []
settings = {}
settings['show_dots'] = True
settings['show_fill'] = False
settings['show_line'] = True
settings['show_index'] = False
settings['show_pos'] = False
settings['close_poly'] = False

def draw():
    clear()
    up()
    _col = color()
    if points:
        goto(points[0])
        if settings['show_fill']:
            begin_fill()
        if settings['show_line']:
            down()
    for i, p in enumerate(points):
        goto(p)
        if settings['show_dots']:
            dot()
        if settings['show_index']:
            color('black')
            write(i)
        if settings['show_pos']:
            color('black')
            p = int(xcor()), int(ycor())
            write(p)
        color(*_col)
    if settings['close_poly']:
            goto(points[0])
    if settings['show_fill']:
        end_fill()
    up()
    update()

def toggle(key):
    settings[key] = not settings[key]
    draw()

def click(x, y):
    points.append((x, y))       # add the point
    draw()

screen = getscreen()
screen.onclick(click)
screen.onkey(lambda: toggle('close_poly'), 'c')
screen.onkey(lambda: toggle('show_dots'), 'd')
screen.onkey(lambda: toggle('show_fill'), 'f')
screen.onkey(lambda: toggle('show_index'), 'i')
screen.onkey(lambda: toggle('show_line'), 'l')
screen.onkey(lambda: toggle('show_pos'), 'p')
screen.listen()
===
if 'Pen' in globals():      # not running codeplay
    screen.setup(width=600, height=400, startx=0, starty=0)
    done()
```

## Éditer les points

Dans la suite nous ajoutons la possibilité pour éditer les points du polygone. Un click de souris sélectionner un point du polygone, il devient rouge.

Une fois sélectionné on peut

- déplacer ce point
- marquer un autre point

Trois touches ajoutent des fonctions supplémentaires

- sélectionner un point
- `Tab` pour déplacer le point marqué
- `BackSpace` pour effacer le point marqué
- `Escape` pour désélectionner le point marqué

Dans le code ci-dessous, nous n'affichons plus le code précédent. Mais il est toujours présent et exécuté. Si vous téléchargez le code, vous aurez le code complet.

```{codeplay}
:file: polygon_editor2.py
from turtle import *
hideturtle()
tracer(0)
fillcolor('pink')
screen = getscreen()

points = []
settings = {}
settings['show_dots'] = True
settings['show_fill'] = False
settings['show_line'] = True
settings['show_index'] = False
settings['show_pos'] = False
settings['close_poly'] = False

def draw():
    clear()
    up()
    _col = color()
    if points:
        goto(points[0])
        if settings['show_fill']:
            begin_fill()
        if settings['show_line']:
            down()
    for i, p in enumerate(points):
        goto(p)
        if settings['show_dots']:
            dot()
        if settings['show_index']:
            color('black')
            write(i)
        if settings['show_pos']:
            color('black')
            p = int(xcor()), int(ycor())
            write(p)
        color(*_col)
    if settings['close_poly']:
            goto(points[0])
    if settings['show_fill']:
        end_fill()
    up()
    if p_index >=0:
        goto(points[p_index])
        dot(d, 'red')
    update()

def toggle(key):
    settings[key] = not settings[key]
    draw()
===
def click(x, y):
    if select_point(x, y):          # sélectionner un point
        ...
    elif p_index >= 0:
        points[p_index] = x, y      # repositionner le point
    else:
        points.append((x, y))       # ajouter le point
    draw()

def distance(p, q):
    d = (p[0]-q[0])**2 + (p[1]-q[1])**2
    return d ** 0.5

p_index = -1
d = 10

def select_point(x, y):
    global p_index
    for i, p in enumerate(points):
        if distance(p, (x, y)) < d:
            p_index = i
            return True         # on a cliqué sur un point
        
def unselect_dot():
    global p_index
    p_index = -1
    draw()

def next_dot():
    global p_index
    p_index = (p_index + 1) % len(points)
    draw()

def remove_dot():
    global p_index
    if points:
        points.pop(p_index)
    p_index = min(len(points)-1, p_index)
    draw()

screen.onkey(unselect_dot, 'Escape')
screen.onkey(next_dot, 'Tab')
screen.onkey(remove_dot, 'BackSpace')
===
screen.onclick(click)
screen.onkey(lambda: toggle('close_poly'), 'c')
screen.onkey(lambda: toggle('show_dots'), 'd')
screen.onkey(lambda: toggle('show_fill'), 'f')
screen.onkey(lambda: toggle('show_index'), 'i')
screen.onkey(lambda: toggle('show_line'), 'l')
screen.onkey(lambda: toggle('show_pos'), 'p')
screen.listen()

if 'Pen' in globals():      # it's not codeplay
    screen.setup(width=600, height=400, startx=0, starty=0)
    done()
```

## Éditeur complet

Téléchargez le code source {download}`polygon_editor.py <code/polygon_editor.py>`

![editor](media/polygon_editor.png)

### Déplacement (Move)

La touche `Space` permets de sélectionner le polygone entier. Il est marqué par une boite de sélection rouge, avec 9 points de références. Avec un clic de souris, on peut choisir un des 9 points de référence.

Avec un clic de souris, on peut alors déplacer le polygone partout dans le canevas.

La fonction `move()` permet de déplacer chaque point d'un vecteur de déplacement `dx, dy`.

``` python
def move(points, dx, dy):
    for i, p in enumerate(points):
        points[i] = p[0] + dx, p[1] + dy
```

### Échelle (Scale)

Dans le mode transformation, marqué par la boite rouge, on peut alors déformer le polygone à l'aide des touches de direction.

- `Up/Down` effectue une déformation verticale
- `Left/Right` effectue une déformation horizontale

La fonction `scale()` permets de changer chaque point d'un facteur d'échelle `dx, dy`, par rapport à un point de référence `p0`.

``` python
def scale(points, p0, dx, dy):
    x0, y0 = p0
    for i, (x, y) in enumerate(points):
        points[i] = x0 + (x - x0) * dx, y0 + (y - y0) * dy
    draw()
```

### Cisaillement (Shear)

Dans le mode transformation, marqué par la boite rouge, on peut alors cisailler le polygone à l'aide des touches de direction.

- `Up/Down` effectue un cisaillement vertical
- `Left/Right` effectue un cisaillement horizontal

La fonction `shear()` permet de déformer par un facteur `dx, dy`, par rapport à un point de référence `p0`.

``` python
def shear(points, p0, dx, dy):
    for i, p in enumerate(points):
        x = p[0] - p0[0]
        y = p[1] - p0[1]
        points[i] = p0[0] + x + dx*y, p0[1] + y + dy * x
```

### Rotation

Dans le mode transformation, marqué par la boite rouge, on peut alors faire tourner et changer l'échelle du polygone à l'aide des touches de direction.

- `Left/Right` effectue une rotation autour du point de référence
- `Up/Down` effectue un changement d'échelle (zoom)

La fonction `rotate()` permet de tourner par un angle `angle`, par rapport à un point de référence `p0`.
Nous avons besoins des fonctions trigonométriques `sin()` et `cos()`.

``` python
def rotate(points, p0, angle):
    x0, y0 = p0
    for i, (x, y) in enumerate(points):
        x1 = x0 + cos(angle) * (x - x0) - sin(angle) * (y - y0)
        y1 = y0 + sin(angle) * (x - x0) + cos(angle) * (y - y0)
        points[i] = x1, y1
```

Créez d'abord un polygone avec des clics de souris. Ensuite utilisez les touches de direction pour changer l'échelle et tourner le polygone.

```{codeplay}
:file: polygone_transform.py
from turtle import *
from math import sin, cos, radians
hideturtle()
tracer(0)
screen = getscreen()

points = []
p0 = (0, 0)

def draw():
    clear()
    up()
    for p in points:
        goto(p)
        down()
        dot()
    up()
    goto(p0)
    dot(10, 'red')
    update()

def click(x, y):
    points.append((x, y))       # ajouter le point
    draw()
===
def scale(points, p0, dx, dy):
    x0, y0 = p0
    for i, (x, y) in enumerate(points):
        points[i] = x0 + (x - x0) * dx, y0 + (y - y0) * dy
    draw()

def rotate(points, p0, angle):
    x0, y0 = p0
    for i, (x, y) in enumerate(points):
        x1 = x0 + cos(angle) * (x - x0) - sin(angle) * (y - y0)
        y1 = y0 + sin(angle) * (x - x0) + cos(angle) * (y - y0)
        points[i] = x1, y1
    draw()

screen.onkey(lambda : scale(points, p0, 1.2, 1.2), 'Up')
screen.onkey(lambda : scale(points, p0, 0.8, 0.8), 'Down')
screen.onkey(lambda : rotate(points, p0, radians(30)), 'Left')
screen.onkey(lambda : rotate(points, p0, radians(-30)), 'Right')
===
screen.onclick(click)
screen.listen()

if 'Pen' in globals():      # it's not codeplay
    screen.setup(width=600, height=400, startx=0, starty=0)
    done()
```