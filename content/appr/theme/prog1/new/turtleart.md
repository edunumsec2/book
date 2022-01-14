# Créer - `turtle`

Dans ce chapitre nous présentons toute une série d'idées artistiques, inspirées du travail d'Artemis Papert que vous trouvez sur le site [TurtleArt](https://turtleart.org).

Explorez, modifiez, créez !

## Etoile

Une **étoile** est un point lumineux dans le ciel nocturne, et par extension, une figure géométrique représentant des rayons partant du centre.

```{codeplay}
from turtle import *

getscreen().bgcolor('midnightblue')
color('white')
width(1)

n = 10
for i in range(n):
    forward(150)
    back(150)
    left(360/n)
```

## Diaphragme

Un **diaphragme** est un élément mécanique sur le trajet lumineux d'un appareil photo pour régler la quantité de lumière.

```{codeplay}
from turtle import *

getscreen().bgcolor('beige')
color('brown')
width(3)

n = 10
for i in range(n):
    forward(150)
    back(130)
    left(360/n)
```

## Fleur

Les **fleurs** ont souvent inspiré les artistes, peintres, poètes, sculpteurs et décorateurs.

```{codeplay}
from turtle import *

getscreen().bgcolor('pink')
color('crimson')
width(3)

def square(a):
    for i in range(4):
        forward(a)
        left(90)
    
n = 10
for i in range(n):
    square(100)
    left(360/n)
```

## Laser

Le **laser** est un système photonique qui produit un rayonnement lumineux spatialement et temporellement cohérent.

```{codeplay}
from turtle import *

getscreen().bgcolor('yellow')
color('red')
width(1)
up()

def dashes(n, a):
    for i in range(n):
        forward(a/2)
        down()
        forward(a)
        up()
          
n = 10
for i in range(n):
    goto(0, 0)
    dashes(4, 30)
    left(360/n)
```

## Yin Yang

Dans la philosophie chinoise, le **yin** et le **yang** sont deux catégories complémentaires qui sont utilisées dans l'analyse de tous les phénomènes de la vie et du cosmos.

```{codeplay}
from turtle import *

getscreen().bgcolor('skyblue')
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
from turtle import *

getscreen().bgcolor('orange')
color('yellow')
width(3)

def wave(n, r):
    down()
    for i in range(n):
        circle(r, 120)
        circle(-r, 120)
    up()
          
n = 10
for i in range(n):
    goto(0, 0)
    wave(2, 20)
    left(360/n)
```

## Carrés

Un **carré** est un quadrilatère isométrique avec quatre angles droits.

```{codeplay}
from turtle import *

getscreen().bgcolor('honeydew')
color('teal')
width(3)

def square(a):
    for i in range(4):
        forward(a)
        left(90)
    
for x in range(20, 160, 20):
    square(x)
```

## Spirale

Une **spirale** est une courbe qui commence en un point central puis s'en éloigne de plus en plus, en même temps qu'elle tourne autour.

```{codeplay}
from turtle import *

getscreen().bgcolor('teal')
color('yellow')
width(2)
    
for x in range(10, 300, 10):
    forward(x)
    right(91)
```

## Moulin à vent

Un **moulin à vent** est un jouet composé d'une roue munie de pales en papier dont la forme lui permet de tourner quand on souffle dessus.

```{codeplay}
from turtle import *

getscreen().bgcolor('azure')
color('red', 'pink')
width(3)

def triangle(a):
    begin_fill()
    for i in range(3):
        forward(a)
        right(120)
    end_fill()

n = 10
for i in range(n):
    forward(90)
    triangle(90)
    back(90)
    right(360/n)    
```

## Disques

Un **disque** est un objet plat circulaire.

```{codeplay}
from turtle import *
from random import *

getscreen().bgcolor('lavender')
up()

n = 60
for i in range(20):
    x = randrange(-300+n, 300, n)
    y = randrange(-200+n, 200, n)
    goto(x, y)
    dot(n, 'fuchsia') 
```

## Oeillet

L'**oeillet** rouge est un des symboles du mouvement ouvrier. En France tout particulièrement, on porte un oeillet rouge à la boutonnière pour la fête du Travail.

```{codeplay}
from turtle import *

getscreen().bgcolor('aliceblue')
width(2)

def petale(a):
    begin_fill()
    for i in range(2):
        circle(a, 90)
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

## Coeur

Le **coeur** est un organe musculaire qui assure la circulation du sang dans le corps à travers des contractions rythmiques.

```{codeplay}
from turtle import *
getscreen().bgcolor('pink')

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

## Bulle comics

Un **phylactère**, également appelé bulle ou ballon, est un élément graphique permettant de placer le texte d'un dialogue dans une bande dessinée.

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

## Arbre récursif

La **récursivité** est une démarche dont la description mène à la répétition d'une même règle.

```{codeplay}
from turtle import *

getscreen().bgcolor('lightgreen')
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
    back(d)

left(90)
back(70)
branche(70, 6, 60)
```

## Bulles de savon

Les bulles de savons sont des cercles colorés, qui utilisent une transparence de 70%, ce qui permet de voir à travers.

```{codeplay}
from turtle import *
from random import *
up()

for i in range(100):
    x = randint(-300, 300)
    y = randint(-200, 200)
    s = randint(20, 100)
    goto(x, y)
    color((random(), random(), random(), 0.7))
    dot(s)
```

## Modulo

Le nom Modulo fait référence à l'opérateur **modulo** en mathématique `%` et à la structure **modulaire** du cour.

```{codeplay}
from turtle import *

up()
d = 60
color('rebeccapurple')
for c in 'modulo':
    write(c, font=(None, d, 'bold'), move=True)
    
goto(-2*d, d)
dot(0.8*d)
goto(-d, 0)
dot(0.8*d, 'turquoise')
goto(-2*d, 0)
dot(d/2, 'lightgray')
goto(-d, d)
dot(d/2, 'lightgray')
```

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```
