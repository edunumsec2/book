# Vecteurs

Un vecteur est défini par :

- une direction
- une distance
- une oriention

```{codeplay}
from turtle import *

dot()
write('A', font=('Arial', 12))
left(30)
forward(200)
stamp()
dot()
write('B', font=('Arial', 12))
```

## Balle rebondissante

Voici une balle rebondissante sur les 4 murs. Dans une première approche nous utilisons deux variables pour la position, et deux variables pour la vitesse.

```{codeplay}
from turtle import *

tracer(0)
d = 40
x = 0
y = 0
dx = 5
dy = 3

def draw():
    global x, y, dx, dy
    x += dx
    y += dy 

    if not -300 < x < 300:
        dx = -dx
    if not -200 < y < 200:
        dy = -dy

    goto(x, y)
    dot(d)

while True:
    clear()
    draw()
    update()
```

## Avec des vecteurs

```{codeplay}
from turtle import *
from time import *

tracer(0)
d = 40
p = [0, 0]
v = [5, 3]

def draw():
    global p, v, d
    p[0] += v[0]
    p[1] += v[1]

    if not -300 < p[0] < 300:
        v[0] = -v[0]
    if not -200 < p[1] < 200:
        v[1] = -v[1]

    goto(p)
    dot(d)

while True:
    clear()
    draw()
    sleep(0.02)
    update()
```

## Définir un vecteur

```{codeplay}
class Vec2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vec2d(self.x+other.x, self.y+other.y)
    
    def __str__(self):
        return f'Vec2d({self.x}, {self.y})'
    
a = Vec2d(30, 40)
b = Vec2d(50, 10)
print('a =', a)
print('b =', b)
print('a + b =', a + b)
```


```{codeplay}
from turtle import *
from time import *

class Vec2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vec2d(self.x+other.x, self.y+other.y)
    
    def __str__(self):
        return f'Vec2d({self.x}, {self.y})'

Screen().bgcolor('pink')
tracer(0)
d = 40
p = Vec2d()
v = Vec2d(5, 3)

def draw():
    global p, v, d
    p = p + v

    if not -300 < p.x < 300:
        v.x = -v.x
    if not -200 < p.y < 200:
        v.y = -v.y

    goto(p.x, p.y)
    dot(d)

while True:
    clear()
    draw()
    sleep(0.02)
    update()
```

## Accélération

```{codeplay}
from turtle import *
from time import *

class Vec2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vec2d(self.x+other.x, self.y+other.y)
    
    def __str__(self):
        return f'Vec2d({self.x}, {self.y})'

Screen().bgcolor('pink')
hideturtle()
tracer(0)
d = 40
p = Vec2d(100, 100)
v = Vec2d(5, 4)
acc = Vec2d(0, -0.1)

def draw():
    global p, v, d
    v += acc
    p += v

    if not -300 < p.x < 300:
        v.x = -v.x
    if not -200 < p.y < 200:
        v.y = -v.y

    goto(p.x, p.y)
    dot(d, 'white')

while True:
    clear()
    draw()
    sleep(0.02)
    update()
```
