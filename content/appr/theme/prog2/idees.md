# Idées

## Bulle comics

```{codeplay}
from turtle import *

getscreen().bgcolor('skyblue')
fillcolor('white')

begin_fill()
left(50)
forward(50)
right(50)
forward(170)
circle(40, 180)
forward(200)
circle(40, 180)
goto(0, 0)
end_fill()

up()
goto(30, 60)
color('black')
write('hello', font=('Courier', 32))
```

## Fenêtre

```{codeplay}
from turtle import *

def cote():
    forward(100)
    left(90)
    
def cote2():
    cote()
    cote()

def carre():
    cote2()
    cote2()

def carre2():
    carre()
    left(90)
    carre()
    left(90)
    
def fenetre():
    carre2()
    carre2()
    
fenetre()
````

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
````

## Arbre recursif

```{codeplay}
from turtle import *

getscreen().bgcolor('lightgreen')
color('brown')

def branche(d):
    if d == 1:
        width(1)
        forward(30)
        back(30)
    else:
        width(d)
        forward(50)
        left(55)
        branche(d//2)
        right(55+55)
        branche(d//2)
        left(55)
        back(50)

left(90)
back(50)
branche(8)
````

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

print('\nCouleur:')
print(p'color =', color())
print('pen =', pencolor())
print('fill =', fillcolor())
print('mode =', colormode())
print('fill =', fill())

print('\nTortue:')
print('shape =', shape())
print('down =', isdown())
print('visible =', isvisible())
print('speed =', speed())
print('delay =', delay())

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

print('shapes =', Screen.getshapes()))
print('shape =', shape())
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
````

## Key events `lamdda`

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
````

## Animer un point

Animation en utilisant la fonction `undo()` pour effacer la dernière position.

```{codeplay}
from turtle import *
from time import *

getscreen().bgcolor('azure')
setundobuffer(1)
hideturtle()
up()
color('red')

d = 40
x0 = 300 - d//2

for x in range(-x0, x0+1, 20):
    undo()
    setx(x)
    dot(d)
    sleep(0.2)
````

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
````

## Fonction `onclick`

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

def f(x, y):
    print('click at', x, y)
    goto(x, y)
    dot()
    
getscreen().onclick(f)
getscreen().listen()
````

## Dessiner une forme

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

def ligne(x, y):
    goto(x, y)
    down()
    dot()
    
getscreen().onkey(up, 'u')
getscreen().onkey(clear, 'c')
    
getscreen().onclick(ligne)
getscreen().listen()
````
## Système binaire

```{codeplay}
for i in range(16):
    print(i, '=', bin(i))
````

```{codeplay}
for i in range(16):
    print(f'{i:2} = {i:4b}')
````

```{codeplay}
for i in range(100, 105):
    print(f'{i:2} = b{i:08b} = x{i:2x}')
````

```{codeplay}
from random import *

n = 10
score = 0

for i in range(10):
    num = randint(2, 15)
    x = input(f'{num:4b} = ')
    if int(x) == num:
        score += 1
    else:
        print('Faux. Réponse correcte =', num)

print('score =', score, '/', n)
````


