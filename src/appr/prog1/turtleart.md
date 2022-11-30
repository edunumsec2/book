(prog1.turtleart)=
# TurtleArt

Dans ce chapitre, nous présentons toute une série d'idées artistiques, inspirées du travail d'Artemis Papert que vous trouvez sur le site [TurtleArt](https://turtleart.org).

*La créativité, c'est l'intelligence qui s'amuse.*  
– Albert Einstein

```{question}
Quand vous programmez, vous pouvez

{v}`créer`  
{v}`inventer`  
{v}`explorer`  
{v}`comprendre`
```

## Étoile

Une **étoile** est un point lumineux dans le ciel nocturne, et par extension, une figure géométrique représentant des rayons partant du centre.

```{codeplay}
:file: art1.py
from turtle import *

dot(1000, 'midnightblue')
color('white')
width(1)

n = 10
for i in range(n):
    forward(150)
    backward(150)
    left(360/n)
```

## Diaphragme

Un **diaphragme** est un élément mécanique sur le trajet lumineux d'un appareil photo pour régler la quantité de lumière.

```{codeplay}
:file: art2.py
from turtle import *

dot(1000, 'beige')
color('brown')
width(3)

n = 10
for i in range(n):
    forward(150)
    backward(130)
    left(360/n)
```

## Fleur

Les **fleurs** ont souvent inspiré les artistes, peintres, poètes, sculpteurs et décorateurs.

```{codeplay}
:file: art3.py
from turtle import *

dot(1000, 'pink')
color('crimson')
width(3)

def square(d):
    for i in range(4):
        forward(d)
        left(90)
    
n = 10
for i in range(n):
    square(100)
    left(360/n)
```

## Laser

Le **laser** est un système photonique qui produit un rayonnement lumineux spatialement et temporellement cohérent.

```{codeplay}
:file: art4.py
from turtle import *

dot(1000, 'yellow')
color('red')
width(1)
up()

def dashes(d, n):
    for i in range(n):
        forward(d/2)
        down()
        forward(d)
        up()
          
n = 10
for i in range(n):
    goto(0, 0)
    dashes(30, 4)
    left(360/n)
```

## Yin et yang

Dans la philosophie chinoise, le **yin** et le **yang** sont deux catégories complémentaires qui sont utilisées dans l'analyse de tous les phénomènes de la vie et du cosmos.

```{codeplay}
:file: art5.py
from turtle import *

dot(1000, 'skyblue')
color('navy')
width(2)
left(90)

begin_fill()
circle(-50, 180)
circle(50, 180)
circle(100, 180)
end_fill()
circle(100, 180)

up()
left(90)
forward(50)
dot(30, 'skyblue')
forward(100)
dot(30, 'navy')
```

## Soleil

Le **Soleil** est l’étoile de notre système solaire.

```{codeplay}
:file: art6.py
from turtle import *

dot(1000, 'orange')
color('yellow')
width(3)

def wave(r, n):
    down()
    for i in range(n):
        circle(r, 120)
        circle(-r, 120)
    up()
          
n = 10
for i in range(n):
    goto(0, 0)
    wave(20, 2)
    left(360/n)
```

## Carrés

Un **carré** est un quadrilatère isométrique avec quatre angles droits.

```{codeplay}
:file: art7.py
from turtle import *

dot(1000, 'honeydew')
color('teal')
width(3)

def square(d):
    for i in range(4):
        forward(d)
        left(90)
    
for d in range(20, 160, 20):
    square(d)
```

## Spirale

Une **spirale** est une courbe qui commence en un point central puis s'en éloigne de plus en plus, en même temps qu'elle tourne autour.

```{codeplay}
:file: art8.py
from turtle import *

dot(1000, 'teal')
color('yellow')
width(2)
    
for d in range(10, 300, 10):
    forward(d)
    right(91)
```

## Moulin

Un **moulin à vent** est un jouet composé d'une roue munie de pales en papier dont la forme lui permet de tourner quand on souffle dessus.

```{codeplay}
:file: art9.py
from turtle import *

dot(1000, 'azure')
color('red', 'pink')
width(3)

def triangle(d):
    begin_fill()
    for i in range(3):
        forward(d)
        right(120)
    end_fill()

n = 10
for i in range(n):
    forward(90)
    triangle(90)
    backward(90)
    right(360/n)    
```

## Disques

Un **disque** est un objet plat circulaire.

```{codeplay}
:file: art10.py
from turtle import *
from random import *

dot(1000, 'lavender')
up()

n = 60
for i in range(20):
    x = randrange(-300+n, 300, n)
    y = randrange(-200+n, 200, n)
    goto(x, y)
    dot(n, 'fuchsia') 
```

## Œillet

L'**œillet** rouge est un des symboles du mouvement ouvrier. En France tout particulièrement, on porte un œillet rouge à la boutonnière pour la fête du Travail.

```{codeplay}
:file: art11.py
from turtle import *

dot(1000, 'aliceblue')
width(2)

def petale(r):
    begin_fill()
    for i in range(2):
        circle(r, 90)
        left(90)
    end_fill()

color('green', 'lime')
petale(40)
left(90)
forward(30)
petale(40)
forward(90)
color('fuchsia', 'pink')
n = 5
for i in range(n):
    petale(30)
    left(360/n)
```

## Cœur

Le **cœur** est un organe musculaire qui assure la circulation du sang dans le corps à travers des contractions rythmiques.

```{codeplay}
:file: art12.py
from turtle import *
dot(1000, 'pink')

r = 40
left(45)
fillcolor('red')

begin_fill()
forward(2 * r)
circle(r, 180)
right(90)
circle(r, 180)
forward(2 * r)
end_fill()
```

## Comics

Un **phylactère**, également appelé bulle ou ballon, est un élément graphique permettant de placer le texte d'un dialogue dans une bande dessinée.

```{codeplay}
:file: art13.py
from turtle import *

dot(1000, 'skyblue')
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

## Arbre

La **récursivité** est une démarche dont la description mène à la répétition d'une même règle.

```{codeplay}
:file: art14.py
from turtle import *

dot(1000, 'lightgreen')
color('brown')

def branche(d, n, angle=50):
    width(n)
    forward(d)
    if n > 1:
        left(angle)
        branche(d-10, n-1)
        right(2 * angle)
        branche(d-10, n-1)
        left(angle)
    backward(d)

left(90)
backward(70)
branche(70, 6, 60)
```

## Bulles

Les bulles de savon sont des cercles multicolores.

```{codeplay}
:file: art15.py
from turtle import *
from random import *
up()

for i in range(100):
    x = randint(-300, 300)
    y = randint(-200, 200)
    s = randint(20, 100)
    goto(x, y)
    color(random(), random(), random())
    dot(s)
```

## Mitsubishi

Le nom Mitsubishi (三菱) signifie *trois losanges* ou *trois diamants* ce qui est représenté dans son logo.

```{codeplay}
:file: art16.py
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

## Modulo

Le nom Modulo fait référence à l'opérateur **modulo** en mathématique `%` et à la structure **modulaire** du cours.

```{codeplay}
:file: art17.py
from turtle import *

up()
d = 60
color('indigo')
for c in 'modulo':
    write(c, font=('Arial', d, 'bold'), move=True)
    
goto(-2*d, d)
dot(0.8*d)
goto(-d, 0)
dot(0.8*d, 'turquoise')
goto(-2*d, 0)
dot(d/2, 'lightgray')
goto(-d, d)
dot(d/2, 'lightgray')
```
