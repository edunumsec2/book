# Reproduire - `Turtle`

Dans la première partie nous avons fait connaissance avec un style de programmation que nous appelons **programmation procédurale**. Dans la deuxième partie, nous allons découvrir un nouveau style de programmation qui s'appelle **programmation orientée objet**.

Le premier changement que nous allons voir est que nous pouvons créer des objets à volonté. Jusqu'à maintenant nous avons travaillé avec une seule tortue.
Mais les tortues sont des objets dérivés de la classe `Turtle`. Vous allez voir que

- la classe `Turtle` permet de produire plein de tortues,
- la fonction `dir()` permet d'afficher ses méthodes,
- la forme `bob = Turtle()` crée une nouvelle tortue.

## Créer des tortues

Dans la première partie, nous avons utilisé une seule tortue. Mais nous pouvons en créer autant que nous voulons. Chaque tortue garde sa couleur, sa position, et son orientation personnelle. Dans le programme suivant nous créons une tortue `ana` et une tortue `bob`.

```{codeplay}
from turtle import *

ana = Turtle()
ana.shape('turtle')
ana.color('red')
ana.speed(2)
ana.forward(100)
ana.right(120)
ana.forward(100)

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.left(60)
bob.speed(1)
bob.forward(100)
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

## Afficher un score

Nous pouvons aussi créer une tortue juste pour afficher du texte. Elle restera alors toujours au même endroit.

Nous créons une tortue `score` et nous la positionnons ne haut à gauche. Elle va afficher le texte **score = n**. 

Ici, à chaque fois que nous bougons la tortue, le score augmente. Avant d'écrire le nouveau score, nous devons effacer l'ancien score. Une écriture se présente donc comme :

- effacer l'ancien score avec `score.clear()`
- afficher le nouveau score avec `score.write()`

```{codeplay}
from turtle import *
s = getscreen()

ana = getturtle()
ana.shape('turtle')
ana.speed(0)
ana.color('red')

n = 0
score = Turtle()
score.up()
score.speed(0)
score.hideturtle()
score.goto(-280, 160)
score.write(f'score = {n}', font=(None, 18))

def bouger(tortue, dir):
    global n
    tortue.seth(dir)
    tortue.forward(20)
    n += 1
    score.clear()
    score.write(f'score = {n}', font=(None, 18))
    
s.onkey(lambda : bouger(ana, 0), 'right')
s.onkey(lambda : bouger(ana, 90), 'up')
s.onkey(lambda : bouger(ana, 180), 'left')
s.onkey(lambda : bouger(ana, 270), 'down')
s.listen()
```

## Trouver de la nourriture

Dans cet exemple nous créons 3 tortues :

- `player` sous forme de tortue bleue
- `food` sous forme de cercle rouge (pomme)
- `score` sans tortue et immobile pour afficher le score

La pomme rouge apparait a une position aléatoire.
Quand la tortue attrape la pomme, le score augmente et la pomme réapparait à une nouvelle position aléatoire.

```{codeplay}
from turtle import *
from random import *
s = getscreen()

player = getturtle()
player.shape('turtle')
player.speed(0)
player.color('blue')

food = Turtle()
food.shape('circle')
food.color('red')
food.speed(0)
food.up()
food.goto(randint(-300, 300), randint(-200, 200))

n = 0
score = Turtle()
score.up()
score.speed(0)
score.hideturtle()
score.goto(-280, 160)
score.write(f'score = {n}', font=(None, 18))

def bouger(tortue, dir):
    global n
    tortue.seth(dir)
    tortue.forward(20)
    if player.distance(food) < 20:
        n += 1
        score.clear()
        score.write(f'score = {n}', font=(None, 18))
        food.goto(randint(-300, 300), randint(-200, 200))
    
s.onkey(lambda : bouger(player, 0), 'right')
s.onkey(lambda : bouger(player, 90), 'up')
s.onkey(lambda : bouger(player, 180), 'left')
s.onkey(lambda : bouger(player, 270), 'down')
s.listen()
```

## Créer beaucoup de tortues

Dans l'exemple suivant nous créons toute une liste de tortues.

```{codeplay}
from turtle import *
from random import *

s = getscreen()
s.bgcolor('beige')
tortues = []
n = 10

for i in range(n):
    x = randint(-300, 300)
    y = randint(-200, 200)
    dir = randint(0, 360)
    col = (random(), random(), random())
    t = Turtle()
    t.color(col)
    t.speed(10)
    t.shape('turtle')
    t.up()
    t.goto(x, y)
    t.seth(dir)
    down()
    tortues.append(t)

def move():
    for t in tortues:
        t.forward(5)
    s.ontimer(move, 100)
        
move()
```
