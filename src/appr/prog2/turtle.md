# Cloner - `Turtle`

Dans **Programmation I** nous avons fait connaissance avec un style de programmation que nous appelons **programmation procédurale**. Dans cette deuxième partie, nous allons découvrir un nouveau style de programmation qui s'appelle **programmation orientée objet**.

Le premier changement que nous allons voir est que nous pouvons créer des tortues à volonté. Jusqu'à maintenant nous avons travaillé avec une seule tortue. Dès maintenant nous allons créer autant de tortues que nous voulons. Les tortues sont des objets dérivés de la classe `Turtle`. Nous allons voir que :

- la classe `Turtle` permet de produire multiples tortues,
- la ligne de code `bob = Turtle()` crée une nouvelle tortue appelée `bob`,
- la méthode `bob.clone()` crée un clone de la tortue `bob`.

```{question}
L'expression `ana = bob.clone()` crée

{f}`un clone d’ana`  
{v}`une copie identique de bob`  
{f}`une nouvelle tortue avec les valeurs par défaut`  
{f}`une référence vers l'objet bob`
```

## Reproduire des tortues

Jusqu'à maintenant, nous avons utilisé une seule tortue. Mais nous pouvons en créer autant que nous voulons. Chaque tortue possède sa couleur, sa position, son orientation, sa vitesse, sa forme, etc.  Dans le programme suivant nous créons une tortue `ana`, une tortue `bob` et une tortue `mia`.

```{exercise}
Créez encore une autre tortue, choisissez sa couleur et faites la bouger quelque part.
```

```{codeplay}
:file: turtle1.py
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

## La course des tortues

Dans le programme ci-dessous deux tortues, Ana et Bob, font la course.

On crée d'abord la tortue `ana` qui est la tortue par défaut `getturtle()` et on configure

- sa forme
- sa vitesse
- sa couleur
- son épaisseur de trait

Ensuite nous faisons une copie identique avec `ana.clone()`.

Pour les faire bouger, vous devez appuyer sur les touches

- `a` pour faire avancer `ana` (rouge).
- `b` pour faire avancer `bob` (bleu).

```{codeplay}
from turtle import *
s = getscreen()

ana = getturtle()
ana.shape('turtle')
ana.speed(0)
ana.color('red')
ana.width(5)

bob = ana.clone()
bob.color('blue')
bob.sety(20)
bob.clear()

def a():
    ana.forward(1)

def b():
    bob.forward(1)
    
s.onkey(a, 'a')
s.onkey(b, 'b')
s.listen()
```

## Méthodes Turtle

La fonction `dir()` permet d'afficher toutes les méthodes que possède la classe `Turtle`. Il y en a environ 72 et vous en connaissez déjà une grande partie.

Dans la liste de compréhension, nous excluons les méthodes spéciales qui commencent avec un tiret bas `_` et affichons toutes les méthodes pour un objet `Turtle`.

```{codeplay}
:file: turtle2.py
from turtle import *

methodes = [x for x in dir(Turtle) if not x.startswith('_')]
print(methodes)
print(len(methodes))
```

Les 4 méthodes de mouvement et leurs raccourcis

- `forward`, `fd` - avancer
- `backward`, `back`, `bk` - reculer
- `left`, `lt` - tourner à gauche
- `right`, `rt` - tourner à droite

Les méthodes pour colorier

- `begin_fill`, `end_fill` - pour entourer la forme à remplir
- `color` - les 2 couleurs (ligne et remplissage)
- `colormode` - le mode (1 ou 255)
- `pencolor` - couleur de ligne
- `fillcolor` - couleur de remplissage

Les méthodes de dessin

- `dot` - dessiner un point
- `circle` - dessiner un cercle
- `stamp` - dessiner un tampon de la tortue
- `write` - écrire un texte

Les méthodes d'initialisation

- `clear` - effacer les traces
- `home` - retourner à l'origine
- `reset` - réinitialiser la tortue

Les méthodes de la tortue

- `shape` - choisir la forme
- `speed` - choisir la vitesse
- `width`, `pensize` - épaisseur du trait
- `hideturtle`, `ht` - masquer la tortue
- `showturtle`, `st` - afficher la tortue
- `down`, `pendown`, `pd` - baisser le stylo
- `up`, `penup`, `pu` - lever le stylo
- `isdown`, `isvisible`, `fill` - info sur l'état (True/False)
- `clone` - créer une copie de la tortue

Les méthodes de position et leurs raccourcis

- `position`, `pos` - lire la position
- `setposition`, `setpos`, `goto` - changer la position
- `xcor`, `ycor` - lire une coordonnée
- `setx`, `sety` - changer une coordonnée
- `towards`, `heading` - lire l'orientation
- `setheading`, `seth` - changer l'orientation
- `distance` - distance vers une tortue
- `degrees`, `radians` - choisir l'unité

Les méthodes pour trouver la référence aux objets

- `getpen`, `getturtle` - objet tortue
- `getscreen` - objet écran

Les méthodes pour la taille de la fenêtre

- `window_height`
- `window_width`

Les méthodes pour définir les fonctions de rappel

- `onclick` - cliquer la tortue
- `ondrag` - tirer la tortue
- `onrelease` - relâcher la tortue

La méthode pour entrer dans la boucle principale

- `done`, `mainloop`

Les méthodes pour contrôler l'animation de la tortue

- `delay` - délai entre les animations
- `tracer` - activer ou désactiver l'animation
- `update` - redessiner la scène

```{caution}
Si vous exécutez ce code directement en Python avec un éditeur externe comme Thonny, vous constatez un nombre bien plus élevé d'objets (plus que 130).

Ceci est dû au fait que dans ce site votre code est traduit en JavaScript et exécuté par [Skulpt](https://skulpt.org) directement dans votre navigateur.
Le module en JavaScript ne traduit pas tous les objets, mais les méthodes essentielles sont toutes présentes.
```

## Une tortue texte

Nous allons maintenant introduire une deuxième tortue qui sera responsable uniquement pour écrire du texte. L'expression `text = Turtle()` crée une nouvelle tortue appelée `text`. Pour appeler des méthodes sur cette nouvelle tortue nous devons utiliser la méthode dotée, donc précéder les instructions par `text.`

```{exercise}
Ajoutez une fonction de rappel pour faire tourner la tortue.
```

```{codeplay}
:file: onkey3.py
from turtle import *
text = Turtle()
text.up()
text.hideturtle()
text.goto(-290, 180)
text.write('a–avancer  h–home  c–clear', font=('Arial', 14))

shape('turtle')
color('red')

def avancer():
    forward(20)

s = getscreen()
s.onkey(avancer, 'a')
s.onkey(home, 'h')
s.onkey(clear, 'c')
s.listen()
```

## Bouger deux tortues

Nous pouvons utiliser des fonctions de rappel pour faire bouger les deux tortues à l'aide des touches du clavier.

La fonction `clone()` permet de cloner la tortue `ana`. La nouvelle tortue est un objet séparé qui sera initialisé avec les bonnes valeurs pour la forme et la vitesse. Pour `bob` il faudra juste changer sa couleur en bleu.

```{codeplay}
:file: turtle3.py
from turtle import *
s = getscreen()
d = 20

ana = getturtle()
ana.shape('turtle')
ana.speed(0)
ana.color('red')

bob = ana.clone()
bob.color('blue')
bob.goto(0, d)

def bouger(tortue, dir):
    tortue.seth(dir)
    tortue.forward(d)
    
s.onkey(lambda : bouger(ana, 0), 'Right')
s.onkey(lambda : bouger(ana, 90), 'Up')
s.onkey(lambda : bouger(ana, 180), 'Left')
s.onkey(lambda : bouger(ana, 270), 'Down')

s.onkey(lambda : bouger(bob, 0), 'd')
s.onkey(lambda : bouger(bob, 90), 'w')
s.onkey(lambda : bouger(bob, 180), 'a')
s.onkey(lambda : bouger(bob, 270), 's')
s.listen()
```

## Créer en boucle

Dans l'exemple suivant, nous allons créer 10 tortues à des positions aléatoires, avec des couleurs aléatoires.

Appuyer sur la touche espace fait les avancer de 10 pixels. La fonction `s.turtles()` renvoie une liste de toutes les tortues créées. Dans une boucle nous déplaçons chaque tortue de 10 pixels.

```{codeplay}
:file: turtle4.py
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

def move():
    for t in s.turtles():
        t.forward(10)

s.onkey(move, 'Space')
s.listen()
```

## Créer par un clic

Dans l'exemple suivant, nous créons des tortues en cliquant avec la souris.

La stratégie adopte est de crée une première tortue cachée au centre qui a les propriétés suivantes:

- forme de tortue
- vitesse maximale
- stylo levé

À chaque clic de souris, cette tortue invisible au centre est clonée. Il suffit alors de la colorier, placer, orienter et montrer.

Appuyer sur la touche espace fait les avancer de 10 pixels.

```{codeplay}
:file: turtle5.py
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

def move():
    for t in s.turtles():
        t.forward(10)

s.onclick(f)
s.onkey(move, 'Space')
s.listen()
```

## Une tortue parmi 10

Dans l'exemple suivant, nous allons créer 10 tortues à des endroits aléatoires.
Cliquer sur une des tortues, change sa couleur en rouge et la rend active. Son déplacement peut être contrôlé par les touches flèches.

```{codeplay}
:file: turtle7.py
from turtle import *
from random import *
s = getscreen()
d = 20

def f(x, y, tortue):
    global t
    t.color('black')
    t = tortue
    t.color('red')

for i in range(10):
    t = getturtle() if i == 0 else Turtle()
    t.speed(0)
    t.shape('turtle')
    
    x = randint(-300, 300)
    y = randint(-200, 200)
    t.goto(x, y)
    t.onclick(lambda x, y, tortue=t : f(x, y, tortue))

s.onkey(lambda : t.right(30), 'Right')
s.onkey(lambda : t.left(30), 'Left')
s.onkey(lambda : t.forward(d), 'Up')
s.onkey(lambda : t.backward(d), 'Down')
s.listen()
```

## Exercice

### La course

Dans la course des tortues :

- ajoutez une ligne de départ une ligne d'arrivé,
- affichez le nom du gagnant,
- affichez le temps utilisé,
- affichez les clics par seconde

```{codeplay}
:file: course.py
from turtle import *
s = getscreen()

ana = getturtle()
ana.shape('turtle')
ana.speed(0)
ana.color('red')
ana.width(5)

bob = ana.clone()
bob.color('blue')
bob.sety(20)
bob.clear()
```
