# Idées

Les programmes de ce chapitres sont des idées sous construction, à développer et à placer à leur endroit approprié.


## Arbre

```{codeplay}
from turtle import *

getscreen().bgcolor('lightblue')
color('brown')

def branche():
    width(1)
    forward(30)
    back(30)

def branche2():
    width(2)
    forward(40)
    left(50)
    branche()
    right(50+50)
    branche()
    left(50)
    back(40)
    
def branche4():
    width(4)
    forward(50)
    left(40)
    branche2()
    right(40+40)
    branche2()
    left(40)
    back(50)
    
def branche8():
    width(8)
    forward(50)
    left(50)
    branche4()
    right(50+50)
    branche4()
    left(50)
    back(50)

left(90)
back(50)
branche8()
```

## Etat de la tortue

Plusieurs fonctions nous renseignent sur l'état de la tortue :

- couleur
- tortue
- position
- fenêtre

```{codeplay}
from turtle import *

color('red', 'lime')
forward(50)
left(45)

print('Couleur:')
print('color =', color())
print('pen =', pencolor())
print('fill =', fillcolor())
print('mode =', colormode())

print('\nPosition:')
print('h =', heading())
print('x =', xcor())
print('y =', ycor())
print('pos =', pos())

print('\nFenêtre:')
print('h =', window_height())
print('w =', window_width())
```

## Les méthodes `Turtle`

Affiche tous les méthodes et attributs de `Turtle`.

```{codeplay}
from turtle import *

print(dir(Turtle))
```

## Les méthodes `Screen`

Affiche tous les méthodes et attributs de `Screen`.

```{codeplay}
from turtle import *

print(dir(Screen))
```

```{codeplay}
from turtle import *

print('Tortue:')
print('shapes =', getscreen().getshapes())
print('shape =', shape())
print('down =', isdown())
print('visible =', isvisible())
print('fill =', fill())
print('speed =', speed())
print('delay =', delay())
```

## Key events

```{codeplay}
from turtle import *
speed(0)

def left():
    setheading(0)
    forward(50)
    
def up():
    setheading(90)
    forward(50)

def right():
    setheading(180)
    forward(50)

def down():
    setheading(270)
    forward(50)

getscreen().onkey(up, 'w')
getscreen().onkey(right, 'a')
getscreen().onkey(down, 's')
getscreen().onkey(left, 'd')
getscreen().listen()

print("Cliquez dans la fenêtre pour l'activer.")
print("Utilisez les touches WASD pour bouger la tortue.")
```

## Key events `lambda`

```{codeplay}
from turtle import *
speed(0)

getscreen().onkey(home, 'h')
getscreen().onkey(clear, 'c')
getscreen().onkey(reset, 'r')

getscreen().onkey(up, 'u')
getscreen().onkey(down, 'd')

getscreen().onkey(lambda : forward(50), 'space')
getscreen().onkey(lambda : seth(0), 'right')
getscreen().onkey(lambda : seth(90), 'up')
getscreen().onkey(lambda : seth(180), 'left')
getscreen().onkey(lambda : seth(-90), 'down')
getscreen().listen()

print("Cliquez dans la fenêtre pour l'activer.")
print("Utilisez les touches de direction pour orienter la tortue.")
print("Utilisez espace pour avancer.")
print("Utilisez U/D pour up/down.")
print("Utilisez H/C/R pour home/clear/reset.")
```

## Animer un point

Animation en utilisant la fonction `undo()` pour effacer la dernière position.

```{codeplay}
from turtle import *
from time import *

getscreen().bgcolor('azure')
setundobuffer(1)
hideturtle()
speed(0)
up()
color('red')

d = 40
x0 = 300 - d//2

for x in range(-x0, x0+1, 20):
    undo()
    setx(x)
    dot(d)
    sleep(0.2)
```

Animation en utilisant la couleur `white` pour effacer la dernière position.


```{codeplay}
from turtle import *
from time import *

hideturtle()
speed(0)
up()

d = 40
x0 = 300 - d//2

for x in range(-x0, x0+1, 20):
    color('white')
    dot(d)
    
    setx(x)
    color('red')
    dot(d)
    
    sleep(0.2)
```

## Narration

```{codeplay}
from time import sleep

histoire = """
Une histoire d'aventure
-----------------------
A: comment vas-tu ?
B: très bien !
A: veux-tu faire un voyage ?
B: oui, vers où ?
A: à Rio de Janeiro.
B: choutte, on part quand ?
A: il y a un vol ce soir.
"""

for line in histoire.split('\n'):
    for c in line:
        print(c, end='')
        sleep(0.1)
    sleep(1)
    print()
```

## Events

La tortue a trois événements qui y sont associés : 

- cliquer
- tirer
- relâcher

```{codeplay}
from turtle import *

shape('turtle')
forward(100)

def click(x, y):
    print('click', x, y)
    
def drag(x, y):
    print('drag', x, y)
    
def release(x, y):
    print('release', x, y)
    
getturtle().onclick(click)
getturtle().ondrag(drag)
getturtle().onrelease(release)
getscreen().listen()
```

## Le Zen de Python

Le Zen de Python est un ensemble de 19 principes qui influencent la conception du langage de programmation Python, et sont utiles pour comprendre et utiliser le langage.

Il est aussi inclus comme "Easter egg" dans Python, et apparait quand on tape la commande `import this`.

```{codeplay}
import this
```

## Mot-clés de Python

Ce module contient la liste de tous les mot-clés de Python.

```{codeplay}
import keyword
a = keyword.kwlist
print(a)
print(len(a)) 
```

## Expression réguliers

```{codeplay}
import re
print(dir(re))
```

## Mitsubishi

Le nom Mitsubishi (三菱) signifie *trois losanges* ou *trois diamants* ce qui est réfléchi dans son logo.

```{codeplay}
from turtle import *
color('red')
hideturtle()

def losange():
    for i in range(2):
        forward(100)
        left(60)
        forward(100)
        left(120)

left(60)
for i in range(3):
    begin_fill()
    losange()
    end_fill()
    left(120)
```

## ontimer

```{codeplay}
from turtle import *

up()
goto(0, 150)
hideturtle()
n = 0

def f():
    global n
    dot(10)
    forward(15)
    right(6)
    n += 1
    if n < 60:
        getscreen().ontimer(f, 1000)
        
f()
```

## Echéquier

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

x0, dx, nx = -160, 40, 10
y0, dy, ny = -160, 40, 8
x1 = x0 + nx * dx
y1 = y0 + ny * dy

for i in range(ny + 1):
    y = y0 + i * dy
    goto(x0, y)
    down()
    goto(x0 + nx * dx, y)
    up()
    
for i in range(nx + 1):
    x = x0 + i * dx
    goto(x, y0)
    down()
    goto(x, y0 + ny * dy)
    up()

def f(x, y):
    if x0 < x < x1:
        i = (x - x0) // dx
    if y0 < y < y1:
        j = (y - y0) // dy

    x = x0 + i * dx + dx/2
    y = y0 + j * dy + dy/2
    
    goto(x, y)
    dot(dx)
    
getscreen().onclick(f)
getscreen().listen()
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