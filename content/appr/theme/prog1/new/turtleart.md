# TurtleArt

Ce chapitre vous donne des idées artistiques, inspirées du travail de Artemis Papert, présenté sur le site [TurtleArt](https://turtleart.org).

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
width(5)
left(90)

circle(-50, 180)
circle(50, 180)
circle(100)
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
color('fuchsia')
up()

n = 60
for i in range(20):
    x = randrange(-300+n, 300, n)
    y = randrange(-200+n, 200, n)
    goto(x, y)
    dot(n) 
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

**Exercice** : Définissez une fonction `coeur()` et dessinez pleins de coeurs.

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```


