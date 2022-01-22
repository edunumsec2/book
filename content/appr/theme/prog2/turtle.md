# Reproduire - `Turtle`

Dans **Programmation I** nous avons fait connaissance avec un style de programmation que nous appelons **programmation procédurale**. Dans cette deuxième partie nous allons découvrir un nouveau style de programmation qui s'appelle **programmation orientée objet**.

Le premier changement que nous allons voir est que nous pouvons créer des objets à volonté. Jusqu'à maintenant nous avons travaillé avec une seule tortue. Mais dès maintenant vous pouvez créer autant de tortues que vous voulez. Les tortues sont des objets dérivés de la classe `Turtle`. Vous allez voir que :

- la classe `Turtle` permet de produire plein de tortues,
- la fonction `dir()` permet d'afficher ses méthodes,
- la forme `bob = Turtle()` crée une nouvelle tortue.

```{question}
En programmation orientée objet une classe est

{f}`un objet`  
{v}`un prototype pour faire des objets`  
{f}`quelque chose de très chic`  
{f}`un niveau d'abstraction`
```

## Reproduire des tortues

Dans la première partie, nous avons utilisé une seule tortue. Mais nous pouvons en créer autant que nous voulons. Chaque tortue garde sa couleur, sa position, et son orientation personnelle. Dans le programme suivant nous créons une tortue `ana` et une tortue `bob`.

```{codeplay}
from turtle import *

ana = Turtle()
ana.shape('turtle')
ana.color('red')
ana.forward(100)

bob = Turtle()
bob.color('lime')
bob.shape('turtle')
bob.left(45)
bob.forward(100)

mia = Turtle()
mia.color('blue')
mia.shape('turtle')
mia.left(90)
mia.forward(100)
```

**Exercice** : Créez encore une autre tortue, choisissez sa couleur et faites la bouger quelque part.

## Les méthodes

La fonction `dir()` permet d'afficher toutes les méthodes que possède la classe `Turtle`. Il y en a environ 87 et vous en connaissez déjà une grande partie.

```{codeplay}
from turtle import *

methodes = dir(Turtle)
print(methodes)
print(len(methodes))
```

## Bouger deux tortues

Nous pouvons utiliser des fonctions de rappel pour faire bouger les deux tortues à l'aide des touches du clavier.

La fonction `clone()` permet de cloner la tortue `ana`. La nouvelle tortue est un objet séparé qui sera initialisé avec les bonnes valeurs pour forme et vitesse. Pour `bob` il faudra juste changer sa couleur en bleu.

```{codeplay}
from turtle import *
s = getscreen()

ana = getturtle()
ana.shape('turtle')
ana.speed(0)
ana.color('red')

bob = ana.clone()
bob.color('blue')

def bouger(tortue, dir):
    tortue.seth(dir)
    tortue.forward(50)
    
s.onkey(lambda : bouger(ana, 0), 'right')
s.onkey(lambda : bouger(ana, 90), 'up')
s.onkey(lambda : bouger(ana, 180), 'left')
s.onkey(lambda : bouger(ana, 270), 'down')

s.onkey(lambda : bouger(bob, 0), 'd')
s.onkey(lambda : bouger(bob, 90), 'w')
s.onkey(lambda : bouger(bob, 180), 'a')
s.onkey(lambda : bouger(bob, 270), 's')
s.listen()
```

## Créer en boucle

Dans l'exemple suivant nous allons créer 10 tortues à des positions aléatoires, avec des couleurs aléatoires.

```{codeplay}
from turtle import *
from random import *
s = getscreen()

for i in range(10):
    x = randint(-300, 300)
    y = randint(-200, 200)
    dir = randint(0, 360)
    col = (random(), random(), random())
    
    t = getturtle() if i == 0 else Turtle()
    t.up()
    t.color(col)
    t.speed(5)
    t.seth(t.towards(x, y))
    t.shape('turtle')
    t.goto(x, y)
    t.seth(dir)
```

## Créer par un clic

Dans l'exemple suivant nous créons des tortues en cliquant avec la souris.

La stratégie adopte est de crée une première tortue caché au centre qui a les propriété suivantes:

- forme de tortue
- vitesse maximale
- stylo levé

A chaque clique de souris cette tortue invisible au centre est cloné. Il suffit alors de la colorier, placer, orienter et montrer.

```{codeplay}
from turtle import *
from random import *
s = getscreen()
shape('turtle')
speed(0)
up()
hideturtle()

def f(x, y):
    dir = randint(0, 360)
    col = (random(), random(), random())
    t = clone()
    t.color(col)
    t.goto(x, y)
    t.seth(dir)
    t.showturtle()

s.onclick(f)
s.listen()
```

## Une tortue parmi 3

Cliquez sur une tortue pour la sélectionner, ensuite utiliser les touches flèches pour la déplacer.

```{codeplay}
from turtle import *
from random import *
s = getscreen()
d = 50

def f(tortue, x, y):
    global t
    t = tortue

ana = Turtle()
ana.shape('turtle')
ana.speed(0)

bob = ana.clone()
bob.color('lime')

lea = ana.clone()
lea.color('red')
t = ana

ana.onclick(lambda x, y:f(ana, x, y))
bob.onclick(lambda x, y:f(bob, x, y))
lea.onclick(lambda x, y:f(lea, x, y))

s.onkey(lambda : t.setx(t.xcor() + d), 'right')
s.onkey(lambda : t.setx(t.xcor() - d), 'left')
s.onkey(lambda : t.sety(t.ycor() + d), 'up')
s.onkey(lambda : t.sety(t.ycor() - d), 'down')
s.listen()
```

## Une tortue parmi 10

```{codeplay}
from turtle import *
from random import *
s = getscreen()
d = 50

def f(tortue, x, y):
    global t
    tortue.color('red')
    t = tortue

from turtle import *
from random import *
s = getscreen()

for i in range(10):
    x = randint(-300, 300)
    y = randint(-200, 200)
    dir = randint(0, 360)
    col = (random(), random(), random())
    
    t = getturtle() if i == 0 else Turtle()
    t.up()
    t.color(col)
    t.speed(0)
    t.seth(t.towards(x, y))
    t.shape('turtle')
    t.goto(x, y)
    t.seth(dir)
    t.down()
    t.onclick(lambda x, y : f(t, x, y))

s.onkey(lambda : t.setx(t.xcor() + d), 'right')
s.onkey(lambda : t.setx(t.xcor() - d), 'left')
s.onkey(lambda : t.sety(t.ycor() + d), 'up')
s.onkey(lambda : t.sety(t.ycor() - d), 'down')
s.listen()
````
