(prog1.parametrer)=
# Paramétrer - `f(x)`

Dans ce chapitre, nous allons voir de plus près le concept de la fonction, concept que nous avons vu dès le deuxième chapitre comme façon de donner un nom à une séquence d'instructions. Ici nous allons voir comment nous pouvons ajouter un ou plusieurs paramètres à une fonction. Nous allons voir que :

- l'expression `def f(x):` permet de définir une fonction,
- un paramètre `f(x)` est une variable (`x`) dans la définition de fonction,
- un argument `f(2)` est une valeur (`2`) dans l'appel de fonction.

```{question}
En Python, `def` est un raccourci pour

{f}`défoncé`  
{f}`défilé`  
{v}`définition`  
{f}`défavorisé`
```

## Paramétrer la fonction

Jusqu'à maintenant, notre rectangle était d'une taille fixe.
Il serait très utile que notre nouvelle commande `rectangle(a, b)` puisse dessiner des rectangles de largeur et hauteur variable.
C'est possible en spécifiant des **paramètres** pour la fonction.
Un paramètre de fonction est une variable locale qui peut être utilisée dans sa définition.

Lors de l'appel de la fonction, nous donnons des valeurs à la fonction.
Ces valeurs sont les **arguments** de la fonction.

```{codeplay}
from turtle import *

def rectangle(a, b):    # paramètres (a, b)
    for x in (a, b, a, b):
        forward(x)
        left(90)
        
rectangle(50, 100)      # arguments (50, 100)
rectangle(200, 80)
rectangle(70, 70)
```

La fonction `losange(a, angle)` a comme paramètre la longueur et le premier angle. Le deuxième anlge du losange est calculé.

```{codeplay}
from turtle import *

def losange(a, angle):      # paramètres (a, angle)
    for i in range(2):
        forward(a)
        left(angle)
        forward(a)
        left(180-angle)

losange(100, 60)            # arguments (100, 60)
losange(120, 120)
losange(150, 70)
```

La fonction `polygone(a, n)` a comme paramètre la longueur du côté et le nombre de sommets.

```{codeplay}
from turtle import *

def polygone(a, n):     # paramètres (a, n)
    for i in range(n):
        forward(a)
        left(360/n)

polygone(100, 3)        # arguments (100, 3)
polygone(100, 4)
polygone(100, 5)
polygone(30, 20)
```

## Dessiner une maison

Nous revenons à notre fonction pour dessiner une maison.

```{codeplay}
from turtle import *

def maison(a):
    forward (1.41 * a)
    for angle in (90, 45, 90, 45):
        left(angle)
        forward(a)
    left(90)

backward(200)        
maison(50)
forward(100)
maison(70)
```

## Couleur de la maison

Maintenant nous modifions la fonction pour inclure non seulement la position, la taille, mais également la couleur de la maison comme paramètres.

```{codeplay}
from turtle import *
getscreen().bgcolor('lightgreen')
up()

def maison(a, couleur):
    down()
    fillcolor(couleur)
    begin_fill()
    forward (1.4 * a)
    for angle in (90, 45, 90, 45):
        left(angle)
        forward(a)
    left(90)
    end_fill()
    up()

maison(70, 'lightblue')
goto(120, 30)
maison(50, 'yellow')
goto(-180, -80)
maison(100, 'pink')
```

## Maison avec porte

Maintenant nous modifions la fonction pour inclure non seulement la position, la taille, la couleur de la maison comme paramètres, mais nous y ajoutons aussi une porte.

```{codeplay}
:file: def8.py
from turtle import *
getscreen().bgcolor('lightgreen')
up()

def porte(d):
    for x in (1, 1.6, 1, 1.6):
        forward(d * x)
        left(90)

def mur(d):
    forward (1.4 * d)
    for a in (90, 45, 90, 45):
        left(a)
        forward(d)
    left(90)

def maison(p, d, col1, col2):
    goto(p)
    down()
    fillcolor(col1)
    begin_fill()
    mur(d)
    end_fill()

    forward(d/3)
    fillcolor(col2)
    begin_fill()
    porte(d/3)
    end_fill()
    up()

maison((-20, -80), 70, 'lightblue', 'red')
maison((-200, 20), 50, 'yellow', 'blue')
maison((120, 40), 40, 'pink', 'violet')
```

## Valeurs par défaut

Nous pouvons spécifier des valeurs par défaut. Pour ceci nous ajoutons la valeur par défaut dans la liste de paramètres.

    def maison(p, d=50, col1='yellow', col2='blue'):

Il a maintenant différentes façons à appeler la fonction. Tous les paramètres qui ont une valeur par défaut sont optionnels. Au minimum nous devons spécifier les paramètres sans valeur par défaut.

    maison((-20, -80))

```{codeplay}
:file: def9.py
from turtle import *
getscreen().bgcolor('lightgreen')
up()

def porte(d):
    for x in (1, 1.6, 1, 1.6):
        forward(d * x)
        left(90)

def mur(d):
    forward (1.4 * d)
    for a in (90, 45, 90, 45):
        left(a)
        forward(d)
    left(90)

def maison(p, d=50, col1='yellow', col2='blue'):
    goto(p)
    down()
    fillcolor(col1)
    begin_fill()
    mur(d)
    end_fill()

    forward(d/3)
    fillcolor(col2)
    begin_fill()
    porte(d/3)
    end_fill()
    up()

maison((-20, -80))
maison((-200, 20), col1='lime')
maison((120, 40), col2='red')
maison((-170, -140), d=80)
```

## Formes avec cercles

```{codeplay}
from turtle import *

def coeur(r):
    circle(r, 225)
    forward(2.4 * r)
    left(90)
    forward(2.4 * r)
    circle(r, 225)
    left(180)

left(90)
coeur(70)
coeur(50)
```

```{codeplay}
from turtle import *

def infini(r):
    down()
    forward(r)
    circle(r, 270)
    forward(2*r)
    circle(-r, 270)
    forward(r)
    up()

infini(80)
infini(50)
````

## Rectangle

La fonction `rectangle(a, b, w=1, pen='black', fill=None)` dessine un rectangle a x b.
Elle possède les 3 paramètres optionnels (valeur par défaut en parenthèse):

- `w` -- épaisseur de ligne (`1`)
- `pen` -- couleur de ligne (`'black'`)
- `fill` -- couleur de remplissage (`'white'`)

Le rectangle est dessiné dans la direction actuelle de la tortue. Cette orientation peut être changée avec `seth()`. La tortue se positionne de l'autre côté du point de départ. Ceci permet d'enchainer à dessiner des rectangles.

```{codeplay}
from turtle import *

def rectangle(a, b, w=1, pen='black', fill='white'):
    down()
    width(w)
    pencolor(pen)
    fillcolor(fill)
    begin_fill()
    for x in (a, b, a, b):
        forward(x)
        left(90)
    end_fill()
    up()
    forward(a)

rectangle(40, 30, 3, 'blue', 'lime')
forward(10)
rectangle(40, 30, 1, 'orange', 'orange')
forward(10)
rectangle(30, 80, fill='yellow')
seth(45)
rectangle(40, 30, 5, 'magenta')
seth(0)
rectangle(80, 40, 1, 'red', 'pink')
```

## Pixelart

Nous pouvons utiliser la fonction `rectangle()` pour dessiner du Pixelart.
Pour ceci nous utilisons deux tuples:

- `palette` -- un tuple 1D contenant les couleurs (la palette des couleurs)
- `table` -- un tuple 2D avec les indices des couleurs, ligne par ligne

Les paramètres suivants sont passés à la fonction `rectangle()`:

- `a` -- la taille du pixel (`20`)
- `w` -- épaisseur de ligne (`1`)
- `pen` -- couleur de ligne (`'black'`)

```{codeplay}
from turtle import *
speed(0)

def rectangle(a, b, w=1, pen='black', fill=None):
    """Dessine un rectangle de taille a x b."""
    if pen:
        down()
        width(w)
        pencolor(pen)
    if fill:
        fillcolor(fill)
        begin_fill()
    for x in (a, b, a, b):
        forward(x)
        left(90)
    if fill:
        end_fill()
    up()
    forward(a)
===
def pixelart(table, palette, a=20, w=1, pen='black'):
    for line in table:
        for i in line:
            rectangle(a, a, w=w, pen=pen, fill=palette[i])
        backward(len(line)*a)
        sety(ycor()-a)

palette = (None, 'black', 'yellow', 'white', 'red', )
pikachu = ((1, 2, 2, 1),
            (3, 4, 2, 3),
            (2, 2, 2, 2),
            (2, 2, 2, 3))

dot(1000, 'whitesmoke')
up()
pixelart(pikachu, palette)
goto(-180, 0)
pixelart(pikachu, palette, a=30, w=0, pen=None)
goto(100, 0)
pixelart(pikachu, (None, 'green', 'lime', 'cyan', 'pink'), 25, 3, 'red')
```

## Polygone

La fonction `polygone()` dessine un polygone régulier avec n sommets. Les arguments de la fonction sont :

- `a` -- longueur du segment
- `n` -- nombre de segments
- `m` -- paramètre pour polygone étoilé (>1)

La fonction `polygone()` permet également de dessiner un polygone étoilé, en choisissant un paramètre `m` >1.

```{codeplay}
from turtle import *

def polygon(a, n, m=1, w=1, pen='black', fill='white'):
    down()
    pencolor(pen)
    width(w)
    fillcolor(fill)
    begin_fill()
    for i in range(n):
        forward(a)
        left(m*360/n)
    end_fill()
    forward(a)
    up()  

up()
goto(-280, 0)
for n in range(3, 9):
    polygon(40, n)
    forward(60)
    
goto(-250, -160)
for m in range(2, 6):
    polygon(80, 11, m, fill='yellow')
    forward(60)
```

## Ligne polygonale

La fonction `polyline(poly, pos=(0, 0), size=(1, 1), w=1, pen='black', fill='white')` dessine une ligne polygonale définie par un tuple de points. Les arguments sont:

- `poly` -- tuple de positions (x, y)
- `pos` -- position de déplacement
- `size` -- facteur d'échelle

```{codeplay}
from turtle import *

def polyline(poly, pos=(0, 0), size=(1, 1), w=1, pen='black', fill='white'):
    width(w)
    pencolor(pen)
    fillcolor(fill)
    goto(pos)
    begin_fill()
    for p in poly:
        goto(pos[0]+p[0]*size[0], pos[1]+p[1]*size[1], )
        down()
    end_fill()
    up()

house = ((0, 0), (10, 0), (10, 15), (20, 15), (20, 0),
            (50, 0), (50, 25), (25, 50), (0, 25), (0, 0))

up()
polyline(house)
polyline(house, pos=(-150, -50), fill='pink')
polyline(house, (90, -60), size=(2, 2), w=3)
polyline(house, (90, -80), size=(2, -1.5))
```

## Exercices

### Pingpong

La fonction `pingpong()` reprend le dessin du chapitre 1 et ajoute trois paramètres

```{codeplay}
:file: pingpong.py
from turtle import *

def pingpong(a, col1, col2):
    down()
    color(col1)
    width(0.15*a)
    forward(0.6*a)
    color(col2)
    width(0.6*a)
    forward(0.1*a)
    up()

seth(90)
pingpong(200, 'brown', 'red')
goto(100, 0)
pingpong(100, 'brown', 'blue')
```

### Stickman

```{codeplay}
from turtle import *
up()


def leg(angle, a):
    left(angle)
    forward(a)
    backward(a)
    right(angle)

def stickman(a, bras=(30, -45), jambes=(10, -30)):
    seth(0)
    down()
    circle(a/2)       # tête
    right(90)
    forward(a/2)    # cou
    
    leg(bras[0], a)
    leg(bras[1], a)
    forward(a)
    
    leg(jambes[0], a)
    leg(jambes[1], a)
    up()

goto(-200, 0)      
stickman(20)

goto(-100, 0)      
stickman(20, (90, -110))

goto(0, 0)      
stickman(30, (90, -110), (110, -24))
hideturtle()
```

