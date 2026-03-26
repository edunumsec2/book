(prog.randomiser)=
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

Le module `random` permet de créer des nombres pseudoaléatoires. Pour afficher le contenu d'un module, nous pouvons utiliser la fonction `dir()` qui affiche les objets du module.

Le module met à disposition 13 fonctions.

```{codeplay}
:file: random1.py
import random

for f in dir(random):
    print(f)
```

## Entier aléatoire

La fonction `randint(a, b)` retourne un nombre aléatoire dans l'intervalle [a, b].
Avec `y = randint(-200, 200)` nous choisissons une valeur `y` aléatoire.

Pour éviter de dessiner une ligne depuis l'origine au premier point, nous levons le stylo au début, et nous le posons dès le premier point atteint avec `goto(x, y)`

```{codeplay}
from turtle import *
from random import *

d = 20
up()

for x in range(-300, 300, d):
    y = randint(-200, 200)
    goto(x, y)
    down()
    forward(d)
    dot()
    write(y)
```

## Position aléatoire

Nous pouvons également choisir les deux coordonnées `x` et `y` de façon aléatoire.

```{codeplay}
from turtle import *
from random import *

for i in range(10):
    x = randint(-300, 300)
    y = randint(-200, 200)
    p = (x, y)
    goto(p)
    dot()
    write(p)
```

## Angle aléatoire

La fonction `a = randint(-90, 90)` retourne un angle aléatoire dans l'intervalle [-90, 90].
Le programme produit un parcours aléatoire (**random walk**)

```{codeplay}
from turtle import *
from random import *
    
d = 20 

for i in range(100):
    a = randint(-90, 90)
    dot()
    write(a)
    left(a)
    forward(d)
```

## Taille aléatoire

La fonction `d = randint(1, 3)` retourne un diamètre aléatoire dans l'intervalle [1, 3]. Chaque taille a la même probabilité.

```{codeplay}
from turtle import *
from random import *
up()

for i in range(20):
    x = randint(-300, 300)
    y = randint(-200, 200)
    d = randint(1, 3)
    goto(x, y)
    dot(d*10, 'pink')
    write(d, align='center')
```

### Sous la belle étoile

Les étoiles dans le ciel apparaissent à des positions plus ou moins aléatoires.
Nous calculons `x` et `y` comme des entiers aléatoires, choisis dans l'intervalle de la largeur et de la hauteur de la fenêtre.

Nous choisissons la taille `d` avec une distribution normale (de Gauss).

L'expression `d = gauss(3, 2)` renvoie un diamètre avec une moyenne de 3 et un sigma de 2.
Comme cette valeur pourrait être négative, dans certains cas, nous en prenons la valeur absolue avec la fonction `abs())`.

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

Pour faire un dessin, il est utile de pouvoir spécifier la région des étoiles.
Nous choisissons ici des régions rectangulaires définies par une position `p` et une taille `size`.
Les étoiles seront placées dans cette région.

```{codeplay}
from turtle import *
from random import *
speed(0)
up()

def rectangle(p, size, c):
    color(c)
    begin_fill()
    goto(p)                 # la tortue va au point de départ
    for d in size * 2:      # équivalent à (w, h, w, h)
        forward(d)
        left(90) 
    end_fill()

def etoiles(p, size, n, c):
    for i in range(n):
        x = randint(p[0], p[0] + size[0])
        y = randint(p[1], p[1] + size[1])
        d = abs(gauss(3, 2))
        goto(x, y)
        dot(d, c)
    
rectangle((-300, -200), (600, 150), 'darkgreen')
rectangle((-300, -50), (600, 250), 'black')
etoiles((-300, -50), (600, 250), 100, 'white')
```

### La voie lactée

Pour arranger les étoiles plus dans une bande horizontale, comme dans la Voie lactée, nous utilisons pour la variable `y` une distribution normale (de Gauss) avec une moyenne de 0 et un sigma de 50.

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

## Couleur aléatoire

La fonction `choice()` retourne un élément aléatoire dans une séquence. 

```{codeplay}
from turtle import *
from random import *
up()

couleurs = ('pink', 'red', 'orange', 'lime', 'cyan', 
            'beige', 'yellow', 'silver', 'gold', 'skyblue')

for i in range(20):
    x = randint(-300, 300)
    y = randint(-200, 200)
    c = choice(couleurs)
    goto(x, y)
    dot(60, c)
    write(c, align='center')
```

### Cube de Rubik

Depuis une liste avec les 6 couleurs du cube de Rubik, nous en choisissons une aléatoirement, pour dessiner un cube dans son état défait.

```{codeplay}
from turtle import *
from random import *
speed(0)
couleurs = 'red', 'green', 'blue', 'yellow', 'orange', 'white'

def losange(d, c):
    fillcolor(c)
    begin_fill()
    for a in (120, 60, 120, 60):
        forward(d)
        left(a)
    end_fill()

def surface():
    for j in range(3):
        for i in range(3):
            c = choice(couleurs)
            losange(50, c)
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

## Text aléatoire

La fonction 'choice()' permet aussi de choisir parmi un tuple de mots. Ici nous affichons les noms des chapitres à des positions aléatoires. 
Parfois les positions sont superposées. Nous allons voir plus tard, comment nous pouvons résoudre ce problème.

```{codeplay}
from turtle import *
from random import *
up()

mots = ('dessiner', 'définir', 'colorier', 'répéter', 'cercler', 'paramétrer', 
        'parcourir', 'positionner', 'typographier', 'itérer', 'randomiser')

for i in range(20):
    x = randint(-300, 300)
    y = randint(-200, 200)
    mot = choice(mots)
    goto(x, y)
    write(mot, font=('Courier', 18))
```

## Emoji aléatoire


```{codeplay}
from turtle import *
from random import *
up()
d = 40
emojis = list('🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯🦁🐮🐷🐸🐵')

for i in range(20):
    x = randint(-300, 300-d)
    y = randint(-200, 200-d)
    emoji = choice(emojis)
    goto(x, y)
    write(emoji, font=('Courier', d))
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

def fleur(d):
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
    fleur(d)
```



## Distribution gaussienne

La distribution normale, ou **distribution gaussienne**, est la distribution qui apparait souvent dans la nature. La taille d'une population, le poids d'une population, suit souvent une distribution gaussienne.

La distribution normale `gauss(mu, sigma)` est décrite par deux paramètres :

- son espérance `mu`
- son écart-type `sigma`

La fonction `gauss(0, 5)' avec un sigma de 5 va distribuer ses valeurs autour de 0, de sorte placer 67% des points dans l'intervalle [-5, 5]. Le programme suivant montre un histogramme visuel de classification de 400 points.

```{codeplay}
from turtle import *
from random import *
speed(0)
up()

sigma = 5
d = 10
y = [-180] * 60

for x in range(-300, 300, 50):
    goto(x, -200)
    write(x//d)
for i in range(400):
    j = int(gauss(0, sigma))
    goto(j*d, y[j+30])
    dot(d)
    y[j+30] += d
```

La distribution des tailles des animaux, ou des humains, est également gaussienne. Ci-dessous nous montrons une distribution avec un sigma de 2 et ensuite avec un sigma de 10.

```{codeplay}
from turtle import *
from random import *
d = 100
up()

for (y, sigma) in ((50, 2), (-150, 10)):
    goto(-280, y)
    write(sigma)
    for x in range(-300, 300-d, d//2):
        goto(x, y)
        d = int(gauss(100, sigma))
        write('🧍‍', font=(None, d))
```

## Champs de fleurs

Pour simuler la perspective, nous dessinons les fleurs proches plus grandes.
Il est de nouveau utile de définir une fonction de répartition, qui permet de distribuer des listes d'objets dans une région rectangulaire.

```{codeplay}
from turtle import *
from random import *
getscreen().bgcolor('lightgreen')
up()

def repartition(p, size, n, emojis):
    for i in range(n):
        x = randint(p[0], p[0] + size[0])
        y = randint(p[1], p[1] + size[1])
        d = gauss(40, 5) * (p[1]+size[1]-y)/size[1]
        goto(x, y)
        c = choice(emojis)
        write(c, font=(None, int(d)))
        
repartition((-300, -200), (250, 400), 20, '🌸🌺🌷🌻🌼')
repartition((0, -200), (300, 400), 20, '🍏🍎🍐🍊🍋🍉🍇🍓🫐🍒🍑🥝')      
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
