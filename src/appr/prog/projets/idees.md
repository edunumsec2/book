# Idées

Les programmes de ce chapitre sont des idées sous construction, à développer et à placer à leur endroit approprié.

## Processing

L'environnement [Processing](https://processing.org) est une plateforme de programmation conçue par des artistes pour la création graphique interactive. Le principe majeur de Processing est de simplifier au maximum la mise en œuvre des programmes. Il existe aussi une implémentation en

- JavaScript ([p5.js](https://p5js.org)),
- Python ([Processing.py](https://py.processing.org)).

Le programme suivant place des disques noirs quand on clique avec la souris.

```{codeplay}
from turtle import *
s = getscreen()
tracer(0)
up()

def f(x, y):
    goto(x, y)
    dot(50)
    update()

s.onclick(f)
s.listen()
```

## Hello world

Ceci est l'équivalent du *hello world* dans Processing - dessiner une ligne.

```{codeplay}
from turtle import *
dot(1000, (0.75, 0.25, 0))

color('white')
width(10)
forward(200)
```


## Niveau de gris

Dans le `colormode(255)` les niveaux de gris sont représentés par des entiers allant de 0 (noir) à 255 (blanc).

```{codeplay}
from turtle import *
colormode(255)
up()

backward(250)
for x in range(0, 255, 20):
    dot(40, (x, x, x))
    color('white' if x < 128 else 'black')
    write(x, font=(None, 10), align='center')
    forward(40)
```

## Formes

Le programme suivant définit 4 fonctions pour dessiner des formes géométriques de base :

- `point(p)` pour dessiner un point à la position `p`,
- `ligne(p, q)` pour dessiner une ligne entre deux points,
- `rectangle(p, taille)` pour dessiner un rectangle à la position `p`,
- `ellipse(p, taille)` pour dessiner une ellipse.

```{codeplay}
from turtle import *
from math import *

s = getscreen()
s.bgcolor('teal')
color('white')
width(5)
up()

def point(p, d=10):
    goto(p)
    dot(d)

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

def rectangle(p, taille):
    goto(p)
    down()
    for x in taille * 2:
        forward(x)
        left(90)
    up()

def ellipse(p, taille):
    for i in range(37):
        x = p[0] + taille[0]/2 * sin(pi * i / 18)
        y = p[1] + taille[1]/2 * cos(pi * i / 18)
        goto(x, y)
        down()
    up()

point((-200, 0))
ligne((-100, -100), (-100, 100))
rectangle((0, 0), (80, 120))
ellipse((200, 0), (80, 120))
```

À ajouter :

- Position mode `rectangle(p, size)`
- Center mode `rectangle(c, size)`
- Corner mode `rectangle(p0, p1)`

## Dessine ligne

Ce programme interactif dessine une ligne avec deux clics de souris.

```{codeplay}
from turtle import *
s = getscreen()
speed(0)
up()
state = False

def f(x, y):
    global state
    goto(x, y)
    if state:
       up()
    else:
        down()
    state = not state

s.onclick(f)
s.listen()
```

## Dessine rectangle

Ce programme interactif dessine un rectangle avec deux clics de souris.

```{codeplay}
from turtle import *
s = getscreen()
speed(0)
up()
state = True

def rectangle(p, size):
    goto(p)
    down()
    for x in size * 2:
        forward(x)
        left(90)
    up()

def f(x, y):
    global state, p
    goto(x, y)
    if state:
        p = x, y
    else:
        rectangle(p, (x - p[0], y - p[1]))
    state = not state

s.onclick(f)
s.listen()
```


## Faire défiler un texte

Ce programme fait défiler un texte.

```{codeplay}
from turtle import *
from time import *
speed(0)
tracer(0)

t = 'ceci est une phrase très longue'

for x in range(300, -3100, -10):
    goto(x, 0)
    clear()
    write(t, font=(None, 150))
    update()
```

## Texte qui vibre

Ce programme déplace chaque lettre aléatoirement dans la direction verticale.

```{codeplay}
from turtle import *
from random import *
speed(0)
up()

texte = 'cette phrase vibre'

while True:
    clear()
    goto(-200, 0)
    for c in texte:
        y = randint(-3, 3)
        sety(y)
        write(c, font=(None, 24), move=True)
        update()
```

## module `string`

Le module `string` met à disposition des ensembles de caractères, ainsi que quelque méthodes de transformation typographique.

- lettres
- chiffres
- ponctuation

```{codeplay}
import string

a = dir(string)
print(a)
print(len(a))
```

Le module `string` met à disposition des ensembles de caractères tel que :

- lettres
- chiffres
- ponctuation

```{codeplay}
from string import *

print('lowercase =', lowercase)
print('uppercase =', uppercase)
print('letters =', letters)

print('digits =', digits)
print('hexdigits =', hexdigits)
print('octdigits =', octdigits)

print('punctuation =', punctuation)
print('whitespace =', whitespace, len(whitespace))
```

Le module dispose aussi de fonctions pour mettre en majuscules la première lettre :

- d'une phrase (`capitalize()`),
- de tous les mots d'une phrase (`capwords()`).

```{codeplay}
from string import *

s = 'heLLo YoU'
print('s =', s)
print('capitalize(s) =', capitalize(s))
print('capwords(s) =', capwords(s))
print('s.upper() =', s.upper())
print('s.lower() =', s.lower())
```

## `split()` et `join()`

La méthode `split()` permet de découper une `phrase` en mots, basé sur les espaces, et de renvoyer une liste de mots.

La méthode `join()` fait l'opposé. Elle permet de joindre des mots d'une `liste` en utilisant un ou plusieurs caractères de jonction (`##`).

```{codeplay}
phrase = 'hello how are you'

liste = phrase.split()
phrase2 = '##'.join(liste)

print(phrase)
print(liste)
print(phrase2)
```

## Glissière

La glissière (slider en anglais) est un élément de l'interface utilisateur (UI = user interface) qui permet de choisir une valeur numérique à l'aide d'un mouvement de souris.

```{codeplay}
from turtle import *

width(5)
speed(0)
shape('square')
forward(255)
tracer(0)

def f(x, y):
    x = max(0, min(x, 255))
    clear()
    goto(0, 0)
    forward(255)
    write(x, font=(None, 18))
    goto(x, 0)
    update()
    
ondrag(f)
```

Voici la version améliorée qui permet de cliquer également dans la région de la glissière, pour faire sauter directement à l'endroit du click.

```{codeplay}
from turtle import *
s = getscreen()

width(5)
speed(0)
shape('square')
forward(255)
tracer(0)

def f(x, y):
    if -20 < x < 275 and -20 < y < 20:
        x = max(0, x)
        x = min(x, 255)
        clear()
        goto(0, 0)
        forward(255)
        write(x, font=(None, 18))
        goto(x, 0)
        update()
    
ondrag(f)
s.onclick(f)
#s.listen()
```
