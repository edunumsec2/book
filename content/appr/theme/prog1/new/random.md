# Randomiser - `random`

Dans ce chapitre nous verrons comment un programme peut introduire un élément aléatoire dans un calcul ou dans un raisonnement. Ceci est très important pour programmer certains jeux. Nous allons voir que

- la fonction `random()` retourne une valeur aléatoire dans l'intervalle [0, 1],
- la fonction `randint(a, b)` retourne un entier aléatoire dans l'intervalle [a, b],
- la fonction `shuffle(liste)` fait une permutation aléatoire des éléments d'une liste.

## Le contenu du module

Le module `random` permet de créer des nombres pseudo-aléatoires. Il met à disposition 13 fonctions.

```{codeplay}
import random
print(dir(random))
```

## Nombre aléatoire

La fonction `random()` retourne un nombre aléatoire dans l'intervalle [0, 1].

```{codeplay}
from random import random
    
for i in range(3):
    print(random())
```

Nous pouvons visualiser ceci dans un graphique.

```{codeplay}
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
from random import randint
    
print('randint - random integer')
for i in range(15):
    print(randint(0, 9), end=' ')
```

Nous pouvons visualiser ceci dans un graphique.

```{codeplay}
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

## Choisir dans une liste

La fonction `choice(liste)` retourne un élément aléatoire d'une liste.
Dans l'exemple suivant nous choisissons entre 5 couleurs.

```{codeplay}
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

Nous pouvons aussi choisir aléatoirement d'une liste numérique, avec la taille du points.

```{codeplay}
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

## Permuter

La fonction `shuffle()` permet de permuter les éléments d'une liste. Ceci est l'équivalent de ce qu'on fait avec des cartes de jeux, quand on les mélange.

```{codeplay}
from random import *

a = list(range(10))
print(a)

for i in range(3):
    shuffle(a)
    print(a)
```

## Distribution normale

Dans l'exemple suivant les variables x e y suivent une distribution normale avec mu=0 et sigma=50.

```{codeplay}
from turtle import *
from random import *

speed(0)
color(0, 0, 0, 0.5)
up()

for i in range(1000):
    x = gauss(0, 50)
    y = gauss(0, 50)
    goto(x, y)
    dot(10)
```

## Rouler un dé

```{codeplay}
from turtle import *
from random import *
from time import *

speed(5)
up()

a = 80
d = 50

for n in range(1, 7):
    print(n)
    if n % 2 == 1:
        dot(d)
    if n % 2 == 0:
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
    sleep(1)
```
