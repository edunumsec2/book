# 7. Modules

Lorsqu'on crée de multiples programmes dans des domaines similaires, il est fort probable que des parties de code puissent être réutilisées très fréquemment. Il serait donc plus efficace de placer ce code d'utilité générale dans un endroit spécifique.

Un **module** est un ou plusieurs fichiers en Python que l'on peut importer au début d'un programme.
Ce sont des scripts, contenant un ensemble de définitions — typiquement des fonctions, mais aussi des variables ou constantes (comme *pi* du module `math`).

Python est accompagné d'une bibliothèque de modules standards, tels que :

- `math`,
- `random`,
- `time`,
- `turtle`.

Pour d'autres modules, on peut consulter l'[index des modules Python](https://docs.python.org/3/py-modindex.html).

## Importer un module

Le mot-clé `import` permet d'importer un module. La fonction `dir` permet de voir le contenu du module.
Normalement tous les modules sont importés au début d'un programme.

```{codeplay}
import math

print(dir(math))
````

**Exercice :** importez le module `random` et affichez son contenu avec `dir`.

Pour utiliser une fonction du module importé, il faut faire précéder le nom de la fonction par le nom du module, séparé d'un point.

```{codeplay}
import math


print('e =', math.e)
print('pi =', math.pi)
print('fact(7) =', math.factorial(7))
````

**Exercice :** utilisez la fonction `pow` (puissance) et affichez le résultat.

## Module `math`

On retrouve dans le module `math` des fonctions ainsi que des constantes :

- arithmétiques,
- logarithmiques et exponentielles,
- trigonométriques.

Voici quelques utilisations du module `math` avec des fonctions trigonométriques.

![trigonometry](trigo.gif)

```{codeplay}
from math import asin, acos, atan, degrees

opp = 3
adj = 4
hyp = 5

print(degrees(asin(opp/hyp)))
print(degrees(acos(adj/hyp)))
print(degrees(atan(opp/adj)))
```

Dans cet exemple, on importe les fonctions `asin`, `acos`, `atan` et `degrees` du module `math`. Les trois premières renvoient un angle en radian et la dernière permet de convertir radian en degré.

## Constantes

Voici toutes les objets importé par le module `math`:

```{codeplay}
import math
print(dir(math))
```

Parmi ces objets il y en a 5 qui sont des constantes:

- `math.e  ` base des logarithmes naturels (nombre d'Euler)
- `math.inf` symbole pour infinité
- `math.nan` symbole pour *not a number*
- `math.pi ` rapport de la circonférence d'un cercle à son diamètre
- `math.tau` rapport de la circonférence d'un cercle à son rayon


```{codeplay}
import math

print('Constantes:')
print('e   =', math.e)
print('inf =', math.inf)
print('nan =', math.nan)
print('pi  =', math.pi)
print('tau =', math.tau)
```

## Fonctions trigonométriques

Voici les fonctions trigonométriques:

- `math.sin/cos` fonction sinus/cosinus
- `math.sinh/cosh` fonctions sinus/cosinus hyperbolique
- `math.tan/tan2` fonction tangente avec 1 ou 2 arguments
- `math.tanh` fonction tangente hyperbolique

Et leurs fonctions inverses (arc):

- `math.asin/asinh`
- `math.acos/acosh`
- `math.atan/atanh`

Affichons donc les fonctions `math.sin()` et `math.cos()` avec deux couleurs différentes.

```{codeplay}
import math
from turtle import *

color('red')
for x in range(-300, 300, 10):
    y = 100 * math.sin(x/50)
    setpos(x, y)
    dot()
    
color('blue')
for x in range(-300, 300, 10):
    y = 100 * math.cos(x/50)
    setpos(x, y)
    dot()
```

Dessinons aussi des axes :

```{codeplay}
import math
from turtle import *

for x in range(-6, 7, 1):
    setx(x * 50)
    dot()
    write(' ' + str(x))
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


## Module `random`

Le module `random` permet de créer des nombres pseudo-aléatoires. Il met à disposition 13 fonctions:

- `choice`
- `expovariage`
- `gauss`
- ...

```{codeplay}
import random
print(dir(random))
```

La fonction `random.random()` retourne une valeur aléatoire dans la plage [0, 1].

```{codeplay}
from turtle import *
import random

n = 20
for i in range(n):
    setx((i/n - 0.5) * 600)
    write(i)
    y = random.random()
    sety((y - 0.5) * 400)
    dot()
    write(y)
    sety(0)
```

La fonction `random.randint(a, b)` retourne une valeur aléatoire dans la plage [a, b].

```{codeplay}
from turtle import *
import random

n = 20
for i in range(n):
    setx((i/n - 0.5) * 600)
    write(i)
    y = random.randint(-200, 200)
    sety(y)
    dot()
    write(y)
    sety(0)
```

La fonction `choice(liste)` retourne un élément aléatoire de la liste.
Parmis les 5 couleurs nous choisissons 1.

```{codeplay}
from random import *
from turtle import *

up()
n = 50
for y in range(200-n//2, -200, -n):
    for x in range(-300+n//2, 300, n):
        setpos(x, y)
        color(choice(['red', 'lime', 'blue', 'yellow', 'cyan']))
        dot(n)
```

La fonction `random()` retourne un nombre aléatoire dans l'intervalle [0, 1].

```{codeplay}
from random import random
    
for i in range(3):
    print(random())
```

La fonction `randint(a, b)` retourne un entier aléatoire dans l'intervalle [a, b].

```{codeplay}
from random import randint
    
print('randint - random integer')
for i in range(15):
    print(randint(0, 9), end=' ')
```

La fonction `choice(liste)` retourne un élément aléatoire de la liste.

```{codeplay}
from random import choice

for i in range(5):
    c = choice(['gagné', 'perdu', 'match nul'])
    print(c)
```

## Module `turtle`

Le module `turtle` permet de déplacer une tortue virtuelle sur un écran en lui donnant des commandes pour se déplacer.
En se déplaçant elle dessine une trace :

- la fonction `forward(200)` fait avancer la tortue de 200 pixels,
- la fonction `left(90)` fait tourner la tortue de 90 degrés vers la gauche.

```{codeplay}
from turtle import *

forward(200)
left(90)
forward(100)
```

La tortue connait aussi les commandes :

- `backward()` pour faire reculer la tortue,
- `right()` pour la faire tourner vers la droite.

Ceci dessine un pentagone.

```{codeplay}
from turtle import *

n = 5
for i in range(n):
    forward(100)
    left(360/n) 
```

**Exercice :** dessinez un hexagone, changez la taille.

```{codeplay}
from turtle import *
from math import atan2, degrees, sqrt

a = 200
b = 100
c = sqrt(a*a + b*b)
alpha = degrees(atan2(a, b))

forward(a)
left(90)
forward(b)
left(180 - alpha)
forward(c)
```

**Exercice :** modifiez a et b. Affichez a, b et c avec la fonction `write()` au milieu du segment.

Il est possible de personnaliser le pinceau et l'apparence du curseur ou de choisir si le pinceau est en train d'écrire ou s'il est relevé.
Plus d'infos sous [Python - Tortue graphique](https://docs.python.org/fr/3/library/turtle.html#module-turtle).


## Goto

La fonction `goto(x, y)` permet d'aller directement vers la position `(x, y)`,
sans changer l'orientation de la tortue.

```{codeplay}
from turtle import *
shape('turtle')
color('red', 'lime')
speed(3)

goto(40, 0)
goto(40, 40)
goto(60, 40)
goto(60, 0)
goto(100, 0)
goto(100, 100)
goto(50, 150)
goto(0, 100)
goto(0, 0)
```

## Compter en binaire

```{codeplay}
from turtle import *

def finger(x):
    forward(x)
    circle(-20, 180)
    forward(x)
    left(180)

def binaire(code):
    left(90)
    for c in code :
        write(c, font=('Arial', 24))
        if c == '1':
            finger(120)
        else :
            finger(30)
              
binaire('00110')
```

## Polygone

Un polygone régulier est une forme ou toutes les côtes ont la même longueur est toute les angles sont identiques.

```{codeplay}
from turtle import *

def polygon(n, a):
    for i in range(n):
        forward(a)
        dot(8)
        left(360/n)
        
polygon(3, 100)
polygon(4, 100)
polygon(5, 100)
polygon(6, 100)
```

Pour dessiner des formes qui ne sont pas connecté par une ligne, nous utilisons les deux fonctions:

- `up()` pour lever le stylo
- `down()` pour baisser le stylo

```{codeplay}
from turtle import *

def polygon(n, a):
    for i in range(n):
        forward(a)
        dot(8)
        left(360/n)

up()
back(200)

for i in range(3, 7):
    down()
    polygon(i, 60)
    up()
    forward(120)
```

##  Cercles

La fonction `circle(r)` dessine un cercle de rayon `r`.
Le cercle est dessiné

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

Cette fonction peut avoir un deuxième paramètre sous la forme `circle(r, angle)` 
ou `angle` représente l'angle du cercle dessiné.
Par défaut c'est 360°, donc un cercle entier.

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

Nous pouvons combiner deux segments de cercle et deux segments droits pour dessiner un coeur.

```{codeplay}
from turtle import *
r = 40
fillcolor('red')

begin_fill()
forward(2 * r)
circle(r, 180)
right(90)
circle(r, 180)
forward(2 * r)
end_fill()
```

Dessinons des cercle dans une boucle, et tournons à chaque fois.

```{codeplay}
from turtle import *

n = 6
for i in range(n):
    circle(50)
    left(360/n)
```

Il est également possible de faire varier le rayon dans une boucle `for` avec une expression `range()`.

```{codeplay}
from turtle import *

for r in range(20, 100, 20):
    circle(r)
```

## Objets
Quelle sont toutes les fonctions que nous importons avec le module `turtle` ?
La fonction `dir()` retourne une liste avec toutes les noms de fonctions et classes qui appartiennent au module.

```{codeplay}
import turtle
print(dir(turtle))
```


```{codeplay}

```