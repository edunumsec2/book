# Créer - `class`

La programmation orientée objet met au centre de la programmation la notion d'objet. Des objets individuels sont créés à partir d'un modèle qu'on appelle classe.

Un objet est caractérisé par ses attributs (variables) et méthodes (fonctions). La programmation orientée objet attache les attributs et méthodes à l'objet-même et permet de cette façon un code très structuré et facilement extensible.  Nous allons voir que :

- le mot-clé `class` permet de définir un modèle pour créer des objets,
- l'expression `point = Point()` crée un nouveau objet à partir d'une classe,
- un objet possède des  **attributs** et des **méthodes**.

```{question}
En programmation orientée objet une classe est

{f}`un objet`  
{v}`un modèle pour faire des objets`  
{f}`quelque chose de très chic`  
{f}`une classification`
```

## Définir une classe

Le mot-clé `class` permet de définir une classe, ici la classe `Point`.
C'est une convention en Python, que le nom de classe soit écrit avec une majuscule. Pour définir une classe nous écrivons :

1. le mot-clé `class`
1. le nom de la class (avec une majuscule)
1. des parenthèses optionnelles (classe parent)
1. un deux-points `:`
1. un bloc en indentation

```{codeplay}
class Point:
    "Definition d'un point géométrique"

print(Point)
print(Point.__name__)
```

**Exercice** : Créez une deuxième classe `Rectangle` et affichez son type.

## Créer des objets

A partir d'une class, nous pouvons créer autant d'objets que nous voulons. L'expression `Point()` crée un objet de type `Point`. On dit aussi qu'on crée une **instance** de la classe `Point`.

Pour créer une instance on utilise le nom de la classe suivi de parenthèses. Plus tard nous verrons qu'il peux y avoir des arguments entre ces parenthèses.

Une classe est comme un moule qui nous permet de créer des copies, à partir d'une définition de classe.

```{codeplay}
class Point():
    "Definition d'un point géométrique"

p0 = Point()
p1 = Point()

print(p0, p1)
```

**Exercice** : Créez encore d'autres instances de la classe `Point`,

## Définir des attributs

La notation doté permet de définir des attribut à un objet.
Par exemple le point peut avoir un attribut `x` et `y`.
Il pourrait avoir une couleur, une épaisseur, etc.

La fonction `dir()` affiche les attributs d'un objet.

```{codeplay}
class Point():
    pass

p = Point()
p.x = 20
p.y = 30

print(p.x)
print(p.y)
print(dir(p))
```

## La méthode `__init__()`

Chaque classe possède une méthode spéciale `__init__()` que nous appelons **constructeur**. Cette méthode est appelé lors de la création de l'objet. Son premier paramètres est toujours `self`, qui représente l'objet lui-même. Cette fonction est utilisé pour initialiser les attributs avec les valeurs intiales.

```{codeplay}
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p = Point(20, 30)

print(p.x, p.y)
print(p)
```

## Le méthode `__str__()`

Toutes les classes possède aussi une méthode spéciale `__str__()` qui retourne une chaîne de caractères. Cette chaîne est un descripteur de l'objet. Il est utilisé quand on affiche l'objet avec la fonction `print()`.

Souvent la représentation d'un objet sous forme de texte ressemble à son constructeur, et affiche le nom de la classe et quelques attributs essentiels.

```{codeplay}
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

p = Point()
p1 = Point(20, 30)
print(p)
print(p1)
```

## Définir une méthode

Dans la définition de classe, nous pouvons définir des méthodes supplémentaires. Le premier paramètres de toute méthode est `self`, la variable qui représente l'objet lui-même.

```{codeplay}
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def norme(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

p = Point(20, 30)

print('p.norme() =', p.norme())
print('p =', p)
```

## Définir la classe `Dot`

Essayons maintenant de créer une classe pour un objet graphique. Définissons la classe `Dot` avec les attributs:

- position
- diamètre
- couleur

et les méthodes

- `__init__()` du constructeur
- `__str__()` du descripteur
- `draw()` pour dessiner l'objet

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

class Dot(): 
    def __init__(self, pos=(0, 0), d=40, color='red'):
        self.pos = pos
        self.d = d
        self.color = color
        self.draw()
        
    def draw(self):
        color(self.color)
        goto(self.pos)
        dot(self.d)
        color('black')
        write(self.__str__())
       
    def __str__(self):
        return f'Dot({self.pos}, {self.d}, {self.color})'
        
p0 = Dot()
p1 = Dot((-100, 100))
p2 = Dot((-200, -100), 60, 'lime')
p3 = Dot((100, 100), 100, 'yellow')
```

## Objet cliquable

Nous ajoutons maintenant une fonction de rappel pour basculer la couleur du disque quand on y clique avec la souris.

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

class Dot(): 
    def __init__(self, pos, d=100):
        self.pos = pos
        self.d = d
        self.state = False
        self.color = 'red'
        self.draw()
        
    def draw(self):
        color(self.color)
        goto(self.pos)
        dot(self.d)
       
    def inside(self, x, y):
        dx = self.pos[0] - x
        dy = self.pos[1] -y
        r = self.d/2 
        return dx*dx + dy*dy < r*r
    
    def toggle(self):
        self.state = not self.state
        self.color = 'lime' if self.state else 'red'
        self.draw()
        
p0 = Dot((-100, 0))
p1 = Dot((100, 0))

def f(x, y):
    if p0.inside(x, y):
        p0.toggle()
        
    if p1.inside(x, y):
        p1.toggle()
          
getscreen().onclick(f)
getscreen().listen()
```

## Dot cliquable

Dans l'exemple suivant nous avons deux points `p0` et `p1` qui 

- basculent d'état quand on y clique.
- montrent leur état 0 ou 1,
- changent de couleur entre gris et jaune.

Le troisième point `p2` tient son état à partir de la relation logique 
`p0 and p1`.

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

class Dot(): 
    def __init__(self, pos):
        self.pos = pos
        self.state = False
        self.draw()
        
    def draw(self):
        goto(self.pos)
        dot(40, 'yellow' if self.state else 'lightgray')
        sety(self.pos[1] - 10)
        write(int(self.state), font=(None, 18), align='center')
       
    def inside(self, x, y):
        return (x - self.pos[0]) ** 2 + (y - self.pos[1]) ** 2 < (20 ** 2)
    
    def set(self, state):
        self.state = state
        self.draw()
    
    def toggle(self):
        self.set(not self.state)    
        
p0 = Dot((-100, 100))
p1 = Dot((-100, -100))
p2 = Dot((100, 0))

def f(x, y):
    if p0.inside(x, y):
        p0.toggle()   
    if p1.inside(x, y):
        p1.toggle()
    p2.set(p0.state and p1.state)
            
getscreen().onclick(f)
getscreen().listen()
```

## Nombre binaire 4-bits

Le programme suivant définit une classe `Bin4`. Elle:

- dessine un nombre à 4 digits binaires
- à la position (x, y)
- vérifie si un click est dedans
- incrémente le nombre

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

class Bin4(): 
    def __init__(self, pos=(0, 0)):
        self.pos = pos
        self.n = 0
        self.draw()
        
    def draw(self):
        goto(self.pos)
        dot(60, 'linen')
        sety(self.pos[1]-8)
        write(f'{self.n:04b}', font=('Courier', 16), align='center')
    
    def inside(self, x, y):
        return (-30 < x-self.pos[0] < 30) and (-30 < y-self.pos[1] < 30)
    
    def inc(self):
        self.n = (self.n + 1) % 16
        self.draw()
        
    def set(self, n):
        self.n = n % 16
        self.draw()
        
    def click(self, x, y):
        if self.inside(x, y):
            self.inc()
        
b0 = Bin4((-100, 100))
b1 = Bin4((100, 100))
b2 = Bin4((0, -100))

def f(x, y):
    b0.click(x, y)    
    b1.click(x, y)
    b2.set(b0.n + b1.n)
            
getscreen().onclick(f)
getscreen().listen()
```

## Dessiner une ALU

L'unité arithmétique et logique (en anglais arithmetic–logic unit, ALU), est la partie de l'ordinateur chargé d'effectuer les calculs.

```{codeplay}
from turtle import *

def alu():
    a = 60
    left(a)
    forward(50)
    right(a)
    forward(150)
    right(180-a)
    forward(150)
    right(a)
    forward(200)
    right(a)
    forward(150)
    right(180-a)
    forward(150)
    right(a)
    forward(50)
    up()

def line(x, y):
    goto(x, y)
    seth(-90)
    down()
    goto(x, y-50)
    stamp()
    up()

alu()
line(-100, 100)
line(100, 100)
line(0, -90) 
```

## Une ALU interactive

Dans cette ALU (en anglais arithmetic–logic unit, ALU), nous allons simuler une addition de deux opérandes de 4 bits. En cliquant avec la souris sur une des opérandes d'entrée, la valeur est incrémenté de 1. Les valeurs peuvent aller de 0 à 15.

```{codeplay}
from turtle import *

def alu():
    a = 60
    left(a)
    forward(50)
    right(a)
    forward(150)
    right(180-a)
    forward(150)
    right(a)
    forward(200)
    right(a)
    forward(150)
    right(180-a)
    forward(150)
    right(a)
    forward(50)
    up()

def line(x, y):
    goto(x, y)
    seth(-90)
    down()
    goto(x, y-50)
    stamp()
    up()

class Bin4(): 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.n = 0
        self.draw()
        
    def draw(self):
        goto(self.x, self.y)
        dot(60, 'lightgray')
        goto(self.x, self.y-8)
        write(f'{self.n:04b}', font=('Courier', 16), align='center')
    
    def inside(self, x, y):
        return (-30 < x-self.x < 30) and (-30 < y-self.y < 30)
    
    def inc(self):
        self.n = (self.n + 1) % 16
        self.draw()
        
    def set(self, n):
        self.n = n % 16
        self.draw()
        
    def click(self, x, y):
        if self.inside(x, y):
            self.inc()
===
alu()
line(-100, 100)
line(100, 100)
line(0, -90) 
    
b0 = Bin4(-100, 120)
b1 = Bin4(100, 120)
b2 = Bin4(0, -170)

hideturtle()
speed(0)

def f(x, y):
    b0.click(x, y)    
    b1.click(x, y)
    b2.set(b0.n + b1.n)
            
getscreen().onclick(f)
getscreen().listen()
```

## Classe Card

Les cartes de jeux sont représentées avec un rectangle arrondi et un des 4 symboles (coeur, piq, carreau, trèfle).

```{codeplay}
from turtle import *
up()

class Card:
    couleur = '♥♦'

    def __init__(self, pos=(0, 0), size=(50, 80), r=10, fill='white'):
        self.pos = pos
        self.size = size
        self.r = r
        self.fill = fill
        self.show()
        
    def outline(self):
        down()
        for d in self.size * 2:
            forward(d)
            circle(self.r, 90)
        up()
        
    def show(self):
        goto(self.pos)
        fillcolor(self.fill)
        begin_fill()
        self.outline()
        end_fill()
        color('red')
        sety(self.pos[1]+5)
        write('♥', font=(None, 30))
        
Card()
Card((50, 20), fill='pink')
Card((100, -120), fill='azure')
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

```{codeplay}

```

```{codeplay}

```
