# Cercler - `circle`

Dans ce chapitre nous explorons les cercles et les arcs de cercle. Nous allons voir que

- la fonction `circle(r)` dessine un cercle de rayon `r`, 
- la fonction `circle(r, a)` dessine un arc de cercle d'angle `a`.

## Du polygone au cercle

Plus que le polygone régulier a de sommets, plus il ressemble à un cercle.
Avec 36 sommets, il ressemble déjà raisonnablement à un cercle.

```{codeplay}
from turtle import *

def polygon(n, a):
    for i in range(n):
        forward(a)
        left(360/n)

polygon(36, 10)
```

## Périmètre et rayon

Quel est le rayon `r` du cercle approximé par par le polygone ?
Nous pouvons le trouver à partir du périmètre avec la relation suivante :

$$ p = 2r \pi $$

```{codeplay}
from turtle import *

def polygone(n, a):
    for i in range(n):
        forward(a)
        left(360/n)

n = 36
a = 10
p = n * a
r = p / (2 * 3.14)

print('périmètre =', p)
print('diamètre =', r)
polygone(n, a)
circle(r)
```

## La fonction `circle(r)`

La fonction `circle(r)` dessine un cercle de rayon `r`.
Le cercle est dessiné :

- vers la gauche si r est positif,
- vers la droite si r est négatif.

```{codeplay}
from turtle import *

forward(50)
circle(40)
forward(100)
circle(-30)
forward(100)
```

## Fleur

Dessinons des cercles dans une boucle, et tournons à chaque fois.

```{codeplay}
from turtle import *

n = 6
for i in range(n):
    circle(50)
    left(360/n)
```

**Exercice** : Inversez le signe du rayon.

## Cercle dans in cercle
Il est également possible d'imbriquer des cercles en faisant varier le rayon dans une boucle `for` avec une expression `range()`.

```{codeplay}
from turtle import *

for r in range(20, 100, 20):
    circle(r)
```

**Exercice** : Dessinez les cercles empilés les uns sur les autres.

Cette fonction peut avoir un deuxième paramètre sous la forme `circle(r, angle)`
ou `angle` représente l'angle de l'arc de cercle dessiné.
Par défaut l'angle est de 360°, donc un cercle entier.

Voici un exemple qui utilise deux demi-cercles de 180°.

```{codeplay}
from turtle import *

forward(100)
circle(40, 180)
forward(50)
circle(-30)
forward(50)
circle(40, 180)
```

**Exercice** : Dessinez un bonhomme de neige et utilisez `dot()` pour les yeux.

## Coeur

```{codeplay}
from turtle import *
width(10)

left(90)
circle(50, 225)
forward(120)
left(90)
forward(120)
circle(50, 225)
```

## Infini - ∞

Le mot **infini** (du latin in-, préfixe négatif, et finitus, *limité*) est un adjectif servant à qualifier quelque chose qui n'a pas de limite en nombre ou en taille. L'infini est représenté par le symbole ∞.

```{codeplay}
from turtle import *
width(10)

right(45)
forward(100)
circle(100, 270)
forward(200)
circle(-100, 270)
forward(100)
```

## Pretzel - ⌘

Le pictogramme ⌘ (Unicode 2318), parfois appelé *Gordon loop* ou *pretzel*, a été dessiné par Susan Kare lors de la création du premier Macintosh pour sa touche de commande. Elle sert de préfixe à d'autres touches pour construire des raccourcis tel que :

- cmd+X pour couper
- cmd+C pour Copier
- cmd+V pour Coller

```{codeplay}
from turtle import *
width(10)

for i in range(4):
    circle(50, 270)
    forward(150)
```

## Lettres

```{codeplay}
from turtle import *
width(10)

def espace():
    up()
    forward(30)
    down()

def n():
    left(90)
    forward(80)
    back(40)
    circle(-40, 180)
    forward(40)
    left(90)
    espace()

def o():
    espace()
    circle(40)
    espace()
    espace()

n()
o()
n()
```

## Pétales

```{codeplay}
from turtle import *

def petale():
    for i in range(2):
        circle(100, 120)
        left(60)

for i in range(6):
    petale()
    left(60)
````
