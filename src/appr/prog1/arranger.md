# Arranger

## Sudoku

```{codeplay}
from turtle import *
from turtle import *
speed(0)
up()

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()
    
def grid(p, d):
    x0, y0 = p
    x1 = x0 + 9*d
    y1 = y0 + 9*d

    for i in range(10):
        y = y0 + i*d
        width(3 if i%3 == 0 else 1)
        ligne((x0, y), (x1, y))

    for i in range(10):
        x = x0 + i*d
        width(3 if i%3 == 0 else 1)
        ligne((x, y0), (x, y1))
    
grid((50, 0), 20)
grid((-280, -180), 30)
```


```{codeplay}
from turtle import *

sudoku = ((5, 3, 0, 0, 7, 0, 0, 0, 0),
          (6, 0, 0, 1, 9, 5, 0, 0, 0),
          (0, 9, 8, 0, 0, 0, 0, 6, 0),
          (8, 0, 0, 0, 6, 0, 0, 0, 3),
          (4, 0, 0, 8, 0, 3, 0, 0, 1),
          (7, 0, 0, 0, 2, 0, 0, 0, 6),
          (0, 6, 0, 0, 0, 0, 2, 8, 0),
          (0, 0, 0, 4, 1, 9, 0, 0, 5),
          (0, 0, 0, 0, 8, 0, 0, 7, 9))

up()
speed(0)
p = (-100, 100)
d = 20

x, y = p
for line in sudoku:
    for i in line:
        goto(x, y)
        if i:
            write(i)
        x += d
    x = p[0]
    y -= d
```

## Scrabble

```{codeplay}
from turtle import *

scrabble = (' F     D  EGGS ',
            ' R B  BUZZ  O  ',
            'MUSIC  C E  ARM', 
            ' I C   K BOAT O',
            ' TOY S   R    N',
            '   C H   ARCADE',
            '   L E T   A  Y',
            '  TELEVISION   ',
            '     P G   DOG ',
            '    J  E BOY R ',
            '   WATER     AX',
            '    C      B P ',
            '  S K    A A E ',
            ' QUEEN  APPLES ',
            '  N T     E L  ')


up()
speed(0)
p = (-100, 100)
d = 20

x, y = p
for line in scrabble:
    for c in line:
        goto(x, y)
        write(c)
        x += d
    x = p[0]
    y -= d
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