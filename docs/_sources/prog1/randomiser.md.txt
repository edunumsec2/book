(prog1.randomiser)=
# Randomiser - `random`

Dans ce chapitre, nous verrons comment un programme peut introduire un élément aléatoire dans un calcul ou dans un raisonnement. Ceci est très important pour programmer certains jeux. Nous allons voir que :

- la fonction `random()` renvoie une valeur aléatoire dans l'intervalle [0, 1],
- la fonction `randint(a, b)` renvoie un entier aléatoire dans l'intervalle [a, b],
- la fonction `shuffle(liste)` fait une permutation aléatoire des éléments d'une liste.

```{question}
En Python, `random` est

{v}`un module`  
{f}`une condition`  
{f}`une variable aléatoire`  
{f}`un mot-clé`
```

## Le contenu du module

Le module `random` permet de créer des nombres pseudoaléatoires. Il met à disposition 13 fonctions.

```{codeplay}
:file: random1.py
import random
print(dir(random))
```

## Nombre aléatoire

La fonction `random()` retourne un nombre aléatoire dans l'intervalle [0, 1].

```{codeplay}
:file: random2.py
from random import random
    
for i in range(3):
    print(random())
```

Nous pouvons visualiser ceci dans un graphique.

```{codeplay}
:file: random3.py
from turtle import *
from random import *
up()

n = 15
for i in range(n):
    x = (i/n - 0.5) * 500
    goto(x, -150)
    down()
    write(i)
    y = round(random(), 2)
    sety((y - 0.5) * 300)
    dot()
    write(y)
    sety(-150)
```

## Entier aléatoire

La fonction `randint(a, b)` retourne un entier aléatoire dans l'intervalle [a, b].

```{codeplay}
:file: random4.py
from random import randint
    
print('randint - random integer')
for i in range(15):
    print(randint(0, 9), end=' ')
```

Nous pouvons visualiser ceci dans un graphique.

```{codeplay}
:file: random5.py
from turtle import *
from random import *

n = 20
for i in range(n):
    setx((i/n - 0.5) * 600)
    write(i)
    y = randint(-200, 200)
    sety(y)
    dot()
    write(y)
    sety(0)
```

## Sous la belle étoile

Les étoiles dans le ciel apparaissent à des positions plus au moins aléatoires.
Nous calculons `x` et `y` comme des entiers aléatoires, choisis dans l'intervalle de la largeur et de la hauteur de la fenêtre.

Nous choisissons la taille `d` avec une distribution normale (de Gauss) avec une moyenne de 3 et un sigma de 2.

```{codeplay}
:file: random6.py
from turtle import *
from random import *
getscreen().bgcolor('black')
speed(0)
up()

for i in range(200):
    x = randint(-300, 300)
    y = randint(-200, 300)
    d = abs(gauss(3, 2))
    goto(x, y)
    dot(d, 'white')
```

## La voie lactée

Pour arranger les étoiles plus dans une bande horizontale, comme dans la voie lactée, nous utilisons pour la variable `y` une distribution normale (de Gauss) avec une moyenne de 0 et un sigma de 50.

```{codeplay}
:file: random7.py
from turtle import *
from random import *
getscreen().bgcolor('black')
speed(0)
up()

for i in range(500):
    x = randint(-300, 300)
    y = gauss(0, 50)
    d = abs(gauss(2, 2))
    goto(x, y)
    dot(d, 'white')
```

## Fleurs dans un champ

Dans l'exemple suivant, nous plaçons des fleurs à des positions aléatoires dans un champ.

```{codeplay}
:file: random8.py
from turtle import *
from random import *
getscreen().bgcolor('green')
speed(0)
up()

def fleur(x, y, d):
    for i in range(5):
        dot(d, 'lightyellow')
        forward(d*0.8)
        left(72)
    left(60)
    forward(d*0.7)
    dot(d*0.7, 'gold')

for i in range(10):
    x = randint(-300, 300)
    y = randint(-200, 200)
    d = gauss(30, 10)
    seth(0)
    goto(x, y)
    fleur(x, y, d)
```

## Choisir dans une liste

La fonction `choice(liste)` retourne un élément aléatoire d'une liste.
Dans l'exemple suivant, nous choisissons parmi 5 couleurs.

```{codeplay}
:file: random9.py
from turtle import *
from random import *
getscreen().bgcolor('black')

colors = ['red', 'lime', 'pink', 'yellow', 'cyan']
up()
n = 60
for y in range(200-n, -200, -n):
    for x in range(-300+n, 300, n):
        setpos(x, y)
        dot(n, choice(colors))
```

Nous pouvons aussi choisir aléatoirement dans une liste numérique, avec différentes tailles de points, par exemple.

```{codeplay}
:file: random10.py
from turtle import *
from random import *
getscreen().bgcolor('black')

colors = ['red', 'lime', 'pink', 'yellow', 'cyan']
size = [20, 30, 40, 50, 60]
up()
n = 60
for y in range(200-n, -200, -n):
    for x in range(-300+n, 300, n):
        setpos(x, y)
        dot(choice(size), choice(colors))
```

## Cube de Rubik

Depuis une liste avec les 6 couleurs du cube de Rubik nous en choisissons une aléatoirement, pour dessiner un cube dans son état défait.

```{codeplay}
from turtle import *
from random import *
speed(8)
couleurs = 'red', 'green', 'blue', 'yellow', 'orange', 'white'

def losange():
    fillcolor(choice(couleurs))
    begin_fill()
    for a in (120, 60, 120, 60):
        forward(50)
        left(a)
    end_fill()

def surface():
    for j in range(3):
        for i in range(3):
            losange()
            forward(50)
        backward(150)
        left(120)
        forward(50)
        right(120)
    left(120)
    backward(150)
    
for i in range(3):
    surface()
```

## Distribution normale

Dans l'exemple suivant les variables x e y suivent une distribution normale avec une moyenne de 0 et un sigma de 50.

```{codeplay}
:file: random11.py
from turtle import *
from random import *

speed(0)
up()

for i in range(1000):
    x = gauss(0, 50)
    y = gauss(0, 50)
    goto(x, y)
    dot(10)
```

## Zoo

Pour simuler la perspective, nous dessinons les animaux proches plus grands.

```{codeplay}
:file: random12.py
from turtle import *
from random import *
getscreen().bgcolor('lightgreen')
up()

animals = list('🐑🦧🐫🐆🦓')

for i in range(30):
    x = randint(-300, 300)
    y = randint(-200, 200)
    d = gauss(30, 5) * (250-y)/400
    goto(x, y)
    animal = choice(animals)
    write(animal, font=(None, int(d)))
hideturtle()
```

## Champs de fleurs

Pour simuler la perspective, nous dessinons les fleurs proches plus grandes.

```{codeplay}
:file: random13.py
from turtle import *
from random import *
getscreen().bgcolor('lightgreen')
up()

fleurs = list('🌸🌺🌷🌻🌼')

for i in range(30):
    x = randint(-300, 300)
    y = randint(-200, 200)
    d = gauss(40, 5) * (250-y)/400
    goto(x, y)
    fleur = choice(fleurs)
    write(fleur, font=(None, int(d)))
hideturtle()
```

## Aquarium

Nous ajoutons des feuillages en bas de l'aquarium et intercalons les poissons avec les plantes.

```{codeplay}
:file: random14.py
from turtle import *
from random import *
getscreen().bgcolor('lightblue')
up()

poissons = list('🐠🐟🐡🦀🐠')
print(poissons)
plantes = list('🌿🌱')
print(plantes)

for i in range(10):
    x = randint(-300, 260)
    y = randint(-200, 160)
    d = gauss(40, 5)
    goto(x, y)
    poisson = choice(poissons)
    write(poisson, font=(None, int(d)))
    
    plante = choice(plantes)
    goto(randint(-300, 250), -180)
    write(plante, font=(None, int(gauss(50, 20))))
    
hideturtle()
```

## Rouler un dé

```{codeplay}
:file: random15.py
from turtle import *
from random import *
from time import *

speed(5)
up()

a = 80
d = 50

for n in range(1, 7):
    if n % 2 == 1:
        home()
        dot(d)
    if n >= 2:
        goto(-a, a)
        dot(d)
        goto(a, -a)
        dot(d)
    if n >= 4:
        goto(-a, -a)
        dot(d)
        goto(a, a)
        dot(d)
    if n == 6: 
        goto(-a, 0)
        dot(d)
        goto(a, 0)
        dot(d)
        
    sleep(1)
    clear()
```

**Exercice** : Modifiez le code pour afficher le dé avec un nombre aléatoire entre 1 et 6.

## Permuter

La fonction `shuffle()` permet de permuter les éléments d'une liste. Ceci est l'équivalent de ce qu'on fait avec des cartes de jeux, quand on les mélange.

```{codeplay}
:file: random16.py
from random import *

a = list(range(10))
print(a)

for i in range(3):
    shuffle(a)
    print(a)
```

## Mélanger des cartes

La fonction `shuffle()` permet de mélanger ou permuter aléatoirement une liste. Nous l'utilisons pour mélanger nos cartes de jeu.

```{codeplay}
:file: random17.py
from turtle import *
from random import *
getscreen().bgcolor('green')
up()
speed(0)
w = 20
width(w)

def card(c):
    down()
    color('white')
    for d in (w, 1.6 * w) * 2:
        forward(d)
        left(90)
    color('red')
    write(c, font=(None, w))
    up()
    forward(2 * w + 5)

cartes = list('A23456789JQK')
print(cartes)
goto(-260, 100)
for c in cartes:
    card(c)

shuffle(cartes)
print(cartes)
goto(-260, 0)
for c in cartes:
    card(c)
```
