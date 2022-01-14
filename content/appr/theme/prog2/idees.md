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
    for a in (60, 120, 60, 120):
        forward(100)
        left(a)

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

## Chercher un élément

La fonction cherche un élément dans une liste

```{codeplay}
from random import *
 
a = []
for i in range(100):
    x = randint(1, 999)
    a.append(x)

print(a)
a.sort()
print(a)
```

L'expression `x in liste` retourne une valeur booléene qui indique si x fait partie de la liste.

```{codeplay}
a = [121, 939, 19, 143, 471, 273, 480, 852, 672, 321, 885, 628, 648, 374, 376, 555, 156, 239, 741, 348, 139, 665, 600, 801, 500, 320, 216, 396, 81, 965, 568, 45, 494, 723, 392, 704, 413, 879, 529, 468, 683, 479, 720, 959, 57, 207, 302, 931, 878, 681, 145, 462, 180, 318, 417, 337, 159, 800, 237, 898, 964, 907, 295, 669, 570, 474, 30, 111, 159, 777, 615, 516, 429, 973, 696, 209, 872, 147, 180, 142, 905, 415, 573, 512, 816, 814, 329, 598, 216, 131, 830, 134, 478, 313, 832, 470, 244, 480, 662, 855]

print(855 in a)
print(856 in a)
```

```{codeplay}
a = [121, 939, 19, 143, 471, 273, 480, 852, 672, 321, 885, 628, 648, 374, 376, 555, 156, 239, 741, 348, 139, 665, 600, 801, 500, 320, 216, 396, 81, 965, 568, 45, 494, 723, 392, 704, 413, 879, 529, 468, 683, 479, 720, 959, 57, 207, 302, 931, 878, 681, 145, 462, 180, 318, 417, 337, 159, 800, 237, 898, 964, 907, 295, 669, 570, 474, 30, 111, 159, 777, 615, 516, 429, 973, 696, 209, 872, 147, 180, 142, 905, 415, 573, 512, 816, 814, 329, 598, 216, 131, 830, 134, 478, 313, 832, 470, 244, 480, 662, 855]
===
x = 855
print(x)
for val in a:
    if x == val:
        print(True)
        break

x = 856
print(x)
for val in a:
    if x == val:
        print('True')
        break
print(False)
from turtle import *
n = len(a)
speed(0)

x = -300
for y in a:
    goto(x, y/5)
    dot()
    x += 6
    
color('red')
a.sort()
x = -300
for y in a:
    goto(x, y/5)
    dot()
    x += 6         
```

## Une liste est-elle triée ?

```{codeplay}
a = [570, 562, 87, 609, 411, 833, 825, 852, 390, 892, 417, 55, 632, 496, 902, 893, 222, 796, 179, 766, 793, 354, 793, 186, 254, 72, 995, 45, 362, 762, 118, 650, 19, 429, 504, 763, 111, 474, 167, 754, 344, 299, 13, 404, 703, 684, 760, 621, 674, 327, 836, 930, 390, 821, 51, 990, 416, 297, 553, 183, 307, 221, 350, 841, 762, 728, 341, 548, 798, 432, 103, 759, 525, 972, 174, 844, 566, 199, 76, 164, 383, 929, 480, 49, 798, 23, 976, 991, 570, 833, 336, 117, 953, 345, 635, 798, 510, 69, 725, 171]
b = [13, 19, 23, 45, 49, 51, 55, 69, 72, 76, 87, 103, 111, 117, 118, 164, 167, 171, 174, 179, 183, 186, 199, 221, 222, 254, 297, 299, 307, 327, 336, 341, 344, 345, 350, 354, 362, 383, 390, 390, 404, 411, 416, 417, 429, 432, 474, 480, 496, 504, 510, 525, 548, 553, 562, 566, 570, 570, 609, 621, 632, 635, 650, 674, 684, 703, 725, 728, 754, 759, 760, 762, 762, 763, 766, 793, 793, 796, 798, 798, 798, 821, 825, 833, 833, 836, 841, 844, 852, 892, 893, 902, 929, 930, 953, 972, 976, 990, 991, 995]

def is_sorted(a):
    n = len(a)
    for i in range(1, n):
        if a[i-1] > a[i]:
            return False
    return True

print(is_sorted(a))
print(is_sorted(b))
```

## Recherche binaire

```{codeplay}
liste = [13, 19, 23, 45, 49, 51, 55, 69, 72, 76, 87, 103, 111, 117, 118, 164, 167, 171, 174, 179, 183, 186, 199, 221, 222, 254, 297, 299, 307, 327, 336, 341, 344, 345, 350, 354, 362, 383, 390, 390, 404, 411, 416, 417, 429, 432, 474, 480, 496, 504, 510, 525, 548, 553, 562, 566, 570, 570, 609, 621, 632, 635, 650, 674, 684, 703, 725, 728, 754, 759, 760, 762, 762, 763, 766, 793, 793, 796, 798, 798, 798, 821, 825, 833, 833, 836, 841, 844, 852, 892, 893, 902, 929, 930, 953, 972, 976, 990, 991, 995]

a = 0
b = len(liste)
x = 995

while b - a > 0:
    m = (a + b) // 2
    print(a, m, b, liste[m])
    
    if x == liste[m]:
        break
    elif x < liste[m]:
        b = m
    else:
        a = m + 1
    
print(liste[m] == x)
```

## Ordre du tri par séléction

Quel est la somme de 1 + 2 + 3 + ... n ?  
Graphiquement ceci nous donne la surface d'un triangle.
Si nous affichons

- `x` sur la première ligne
- `xx` sur la deuxième ligne
- n fois `x` sur la dernière ligne

la réponse à la formule est la somme des x.
Nous pouvons ajouter un triangle identique (cette fois dessiné avec des traits (`-`)), ce qui nous donne un rectangle de taille `(n) * (n+1)`.
La taille du triangle est donc  `(n) * (n+1) / 2`.

```{codeplay}
n = 10
for i in range(n+1):
    print('x' * i + '-' * (n-i))

print(n * (n+1) // 2)
```

## Tortues multiples

```{codeplay}
 from turtle import *

a = Turtle()
a.color('red')
a.shape('turtle')
a.forward(100)

b = Turtle()
b.color('blue')
b.shape('turtle')
b.left(90)
b.forward(100)

c = Turtle()
c.color('lime')
c.shape('turtle')
c.left(45)
c.forward(100)
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
