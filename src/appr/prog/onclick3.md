
# Caser - `onclick()`

Dans ce chapitre nous allons traiter les jeu de bords. 

## Tableau

```{codeplay}
from turtle import *
s = getscreen()
hideturtle()
tracer(0)
up()

p = -160, -160
dim = 8, 8
d = 40

def line(p, q):
    goto(p)
    down()
    goto(q)
    up()
    
def square(c):
    width(3)
    down()
    for i in range(4):
        forward(d)
        left(90)
    up()

def grid():
    width(1)
    x0, y0 = p
    x1, y1 = x0 + dim[1] * d, y0 + dim[0] * d
    for i in range(dim[0] + 1):
        line((x0, y0 + i * d), (x1, y0 + i * d))
    for i in range(dim[1] + 1):
        line((x0 + i * d, y0), (x0 + i * d, y1))
    update()
    
def draw():
    clear()
    grid()
    
def index(x, y):
    x0, y0 = p
    x1, y1 = x0 + dim[1] * d, y0 + dim[0] * d
    if x0 < x < x1 and y0 < y < y1:
        i = (y - y0) // d
        j = (x - x0) // d
        goto(x0 + j*d, y0 + i*d)
        return i, j

def f(x, y):
    ij = index(x, y)
    if ij:
        square('pink')
    update()

grid()
s.onclick(f)
s.onkey(draw, 'd')
s.listen()
```


## Grille

Nous utilisons une liste `points` pour stoquer les points d'une ligne polygonale.
La touche `Back` permet d'enlever le dernier point et de redessiner la ligne.

```{codeplay}
from turtle import *
s = getscreen()
hideturtle()
tracer(0)
up()

p = -100, -100
q = 100, 0
d = 30

def line(p, q):
    goto(p)
    down()
    goto(q)
    up()

def grid(p, dim, d):
    x0, y0 = p
    x1, y1 = x0 + dim[1] * d, y0 + dim[0] * d
    for i in range(dim[0] + 1):
        line((x0, y0 + i * d), (x1, y0 + i * d))
    for i in range(dim[1] + 1):
        line((x0 + i * d, y0), (x0 + i * d, y1))
    update()

def index(x, y, p, dim, d):
    x0, y0 = p
    x1, y1 = x0 + dim[1] * d, y0 + dim[0] * d
    if x0 < x < x1 and y0 < y < y1:
        i = (y - y0) // d
        j = (x - x0) // d
        goto(x0 + j*d, y0 + i*d)
        return i, j

grid(p, (8, 4), d)
grid(q, (2, 5), d)

def f(x, y):
    goto(x, y)
    ij = index(x, y, p, (8, 4), d)
    if ij:
        dot()
        write(ij)
    ij = index(x, y, q, (2, 5), d)
    if ij:
        dot()
        write(ij)
    update()

s.onclick(f)
```

## Echec

```{codeplay}
from turtle import *

game = """
♜♞
♟♟♟♟♟♟♟♟
"""

```

## Number puzzle

```{codeplay}
from turtle import *

game = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]]
```