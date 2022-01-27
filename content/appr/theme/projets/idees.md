## Idées

Les programmes de ce chapitre sont des idées sous construction, à développer et à placer à leur endroit approprié.

## `processing.py`

```{codeplay}
from turtle import *
s = getscreen()
tracer(0)
up()

def f(x, y):
    goto(x, y)
    dot(50)
    update()

s.onclick(f)
s.listen()
```

## Hello world

```{codeplay}
from turtle import *
dot(1000, (0.75, 0.25, 0))

color('white')
width(10)
forward(200)
```

## Hello mouse

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

## Shapes

Add 

- Position mode `rectangle(p, size)`
- Center mode `rectangle(c, size)`
- Corner mode `rectangle(p0, p1)`

```{codeplay}
from turtle import *
from math import *

s = getscreen()
s.bgcolor('teal')
color('white')
width(5)
up()

def point(p, d=10):
    goto(p)
    dot(d)

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

def rectangle(p, size):
    goto(p)
    down()
    for x in size * 2:
        forward(x)
        left(90)
    up()

def ellipse(p, size):
    for i in range(37):
        x = p[0] + size[0]/2 * sin(pi * i / 18)
        y = p[1] + size[1]/2 * cos(pi * i / 18)
        goto(x, y)
        down()
    up()

point((-200, 0))
ligne((-100, -100), (-100, 100))
rectangle((0, 0), (80, 120))
ellipse((200, 0), (80, 120))
```

## Dessine ligne

```{codeplay}
from turtle import *
s = getscreen()
speed(0)
up()
state = False

def f(x, y):
    global state
    goto(x, y)
    if state:
       up()
    else:
        down()
    state = not state

s.onclick(f)
s.listen()
```

## Dessine rectangle

```{codeplay}
from turtle import *
s = getscreen()
speed(0)
up()
state = True

def rectangle(p, size):
    goto(p)
    down()
    for x in size * 2:
        forward(x)
        left(90)
    up()

def f(x, y):
    global state, p
    goto(x, y)
    if state:
        p = x, y
    else:
        rectangle(p, (x - p[0], y - p[1]))
    state = not state

s.onclick(f)
s.listen()
```

## Dessine ellipse

```{codeplay}
from turtle import *
s = getscreen()
speed(0)
up()
state = True

def ellipse(p, size):
    for i in range(37):
        x = p[0] + size[0]/2 * sin(pi * i / 18)
        y = p[1] + size[1]/2 * cos(pi * i / 18)
        goto(x, y)
        down()
    up()

def f(x, y):
    global state, p
    goto(x, y)
    if state:
        p = x, y
    else:
        ellipse(p, (2 * (x - p[0]), 2 * (y - p[1])))
    state = not state

s.onclick(f)
s.listen()
```

## Colors

```{codeplay}
from turtle import *
colormode(255)
up()

back(250)
for x in range(0, 255, 20):
    dot(40, (x, x, x))
    color('white' if x < 128 else 'black')
    write(x, font=(None, 10), align='center')
    forward(40)
```

## onkey - lettres

```{codeplay}
from turtle import *
s = getscreen()
speed(0)

def f(x):
    write(x, font=(None, 24), move=True)

for c in 'abcdefghijklmnopqrstuvwxyz':
    s.onkey(lambda x=c: f(x), c)
    
s.listen()
done()
```

## onkey - nombres

```{codeplay}
from turtle import *
s = getscreen()
speed(0)

def f(x):
    write(x, font=(None, 24), move=True)

for c in '0123456789':
    s.onkey(lambda x=c: f(x), c)
    
s.listen()
done()
```

## module `string`

```{codeplay}
import string

a = dir(string)
print(a)
print(len(a))
```


```{codeplay}
from string import *

print('lowercase =', lowercase)
print('uppercase =', uppercase)
print('letters =', letters)

print('digits =', digits)
print('hexdigits =', hexdigits)
print('octdigits =', octdigits)

print('punctuation =', punctuation)
print('whitespace =', whitespace, len(whitespace))
```

```{codeplay}
from string import *

s = 'heLLo YoU'
print('s =', s)
print('capitalize =', capitalize(s))
print('capwords =', capwords(s))
print('capitalize =', capitalize(s))
print('capwords =', capwords(s))
```

## `split()` et `join()`

```{codeplay}
phrase = 'hello how are you'

liste = phrase.split()
phrase2 = '##'.join(liste)

print(phrase)
print(liste)
print(phrase2)
```

## Glissière

```{codeplay}
from turtle import *

width(5)
speed(0)
shape('square')
forward(255)
tracer(0)

def f(x, y):
    x = max(0, min(x, 255))
    clear()
    goto(0, 0)
    forward(255)
    write(x, font=(None, 18))
    goto(x, 0)
    update()
    
ondrag(f)
```
