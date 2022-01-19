# Idées

Les programmes de ce chapitre sont des idées sous construction, à développer et à placer à leur endroit approprié.

## Arbre

Cet exemple montre la construction hiérarchique d'un arbre, a partir d'une simple branche.

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
    right(100)
    branche()
    left(50)
    back(40)
    
def branche4():
    width(4)
    forward(50)
    left(50)
    branche2()
    right(100)
    branche2()
    left(50)
    back(50)
    
def branche8():
    width(8)
    forward(50)
    left(50)
    branche4()
    right(100)
    branche4()
    left(50)
    back(50)

left(90)
back(50)
branche8()
```

## Les méthodes `Turtle`

Affiche tous les méthodes et attributs de `Turtle`.

```{codeplay}
from turtle import *

print(dir(Turtle))
```

Les 6 comparaisons

```{codeplay}
from turtle import *

print('__eq__ =', Turtle.__eq__)
print('__ge__ =', Turtle.__ge__)
print('__gt__ =', Turtle.__gt__)
print('__le__ =', Turtle.__le__)
print('__lt__ =', Turtle.__lt__)
print('__ne__ =', Turtle.__ne__)
```

Les 9 autres méthodes privées.

```{codeplay}
from turtle import *

print('__format__ =', Turtle.__format__)
print('__getattribute__ =', Turtle.__getattribute__)
print('__hash__ =', Turtle.__hash__)
print('__init__ =', Turtle.__init__)
print('__module__ =', Turtle.__module__)
print('__new__ =', Turtle.__new__)
print('__repr__ =', Turtle.__repr__)
print('__setattr__ =', Turtle.__setattr__)
print('__str__ =', Turtle.__str__)
```

## Les méthodes `Screen`

Affiche tous les méthodes et attributs de `Screen`. Nous constatons les mêmes 15 méthodes spéciales que pour `Turtle`.

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

## La fonction `shape()`

```{codeplay}
from turtle import *

shapes = getscreen().getshapes()
print('shapes =', shapes)

left(90)
up()
back(180)

for s in shapes:
    forward(50)
    write(s + '   ', align='right', font=(None, 18))
    shape(s)
    stamp()
```

La taille des 3 formes géométriques `square`,  `triangle` et `circle` est de 20 pixels. Ces formes peuvent être utilisés dans des animations ou des jeux vidéos.

```{codeplay}
from turtle import *
up()

shape('square')
for i in range(10):
    stamp()
    forward(22)
    
goto(0, 30)
shape('circle')
for i in range(10):
    stamp()
    forward(22) 

goto(0, 60)
shape('triangle')
for i in range(10):
    stamp()
    forward(22)
    
hideturtle()
```

## La fonction `delay()`

```{codeplay}
from turtle import *

print('delay =', delay()) # 33 milisecondes = 60 fps
delay(500)

left(50)    # delai tous les 5 degrees 
forward(50) # delai tous les 5 pixels
```

## La fonction `tracer()`

La fonction `tracer(0/1)` (traceur) active ou désactive les animations des tortues.
Lorsque le traceur est désactivé vous devez utiliser la fonction `update()` pour mettre à jour le dessin sur l'écran.

```{codeplay}
from turtle import *

def etoile(n, m):
    for i in range(n):
        forward(100)
        left(360/n*m)

back(200)
print('tracer =', tracer())
etoile(7, 3)

forward(150)
tracer(0)
print('tracer =', tracer())
etoile(7, 3)
update()

forward(150)
etoile(9, 4)
update()
```

La fonction `tracer(n)` contrôle la fréquence des mises à jour du dessin. Seulement les n-ièmes mises à jours régulières de l'écran seront vraiment effectuées. Cette fonction peut être utilisé pour accélérer le dessin de graphiques complexes. Lorsqu'appelé sans arguments, elle renvoie la valeur actuelle de n.

```{codeplay}
from turtle import *
delay(200)

tracer(2)
print('tracer() =', tracer())
write('tracer(2)', align='right', font=(None, 16))
forward(200)

up()
goto(0, 50)
down()

tracer(5)
print('tracer() =', tracer())
write('tracer(5)', align='right', font=(None, 16))
forward(200)
```

## La fonction `speed()`

La vitesse de la tortue peut varier entre 1 et 1000.
Une vitesse de 0 représente la vitesse maximum. La vitesse par défaut est 3.

```{codeplay}
from turtle import *

print('speed =', speed())

for s in range(2, 10):
    reset()
    speed(s)
    write(f'speed({s})  ', font=(None, 18), align='right')
    for i in range(4):
        forward(100)
        left(90)
```

## Animer un point

Animation en utilisant la fonction `tracer(0)` et `update()`.

```{codeplay}
from turtle import *
hideturtle()
tracer(0)
up()

for x in range(-300, 300, 10):
    clear()
    setx(x)
    dot(40, 'red')
    update()
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

## Fonction `ontimer`

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

L'expression `x in liste` retourne une valeur booléenne qui indique si x fait partie de la liste.

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

## Ordre du tri par sélection

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

## Chronométrer

```{codeplay}
from turtle import *
from time import *
import time

print(dir(time))
print('clock =', clock())
print('ctime =', ctime())
print('time =', time.time())
```

```{codeplay}
from turtle import *
from time import *
from random import *

# speed(3) : 80 seconds
# speed(0) : 20 secondes
# tracer(0) : 0.04 secondes

up()
speed(0)
tracer(0)

t0 = time()
d = 20
x0 = 300 - d//2
y0 = 200 - d//2

for y in range(y0, -y0-d, -d):
    for x in range(-x0, x0+d, d):
        goto(x, y)
        r = random()
        dot(d, (r, r, r))
update()
t1 = time()
print(t1-t0)
```

## Snow Crash

```{codeplay}
from turtle import *
from random import *
up()
tracer(0)

d = 20
x0 = 300 - d//2
y0 = 200 - d//2

while True:
    for y in range(y0, -y0-d, -d):
        for x in range(-x0, x0+d, d):
            goto(x, y)
            r = random()
            dot(d, (r, r, r))
    update()
```

```{codeplay}
from turtle import *
from random import *
up()
tracer(0)

d = 20
x0 = 300 - d//2
y0 = 200 - d//2

while True:
    for y in range(y0, -y0-d, -d):
        for x in range(-x0, x0+d, d):
            goto(x, y)
            r = random()
            g = random()
            b = random()
            dot(d, (r, g, b))
    update()
```

## Une tortue par pixel

```{codeplay}
from turtle import *
from time import *
from random import *

tracer(0)
t0 = time()
d = 20
x0 = 300 - d//2
y0 = 200 - d//2
tortues = []

for y in range(y0, -y0-d, -d):
    for x in range(-x0, x0+d, d):
        t = Turtle()
        t.up()
        t.hideturtle()
        t.goto(x, y)
        r = random()
        t.dot(d, (r, r, r))
        tortues.append(t)

update()
t1 = time()
print('time =', t1-t0)
print('obejcts =', len(tortues))
```

## Heading

```{codeplay}
from turtle import *

for i in range(12):
    down()
    forward(100)
    stamp()
    up()
    forward(10)
    write(heading(), align='center')
    backward(110)
    left(30)

hideturtle()
```
