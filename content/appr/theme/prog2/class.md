# Mouler - `class`

La programmation orientée objet (POO) considère les éléments d'un programme comme des objets qui sont *moulés* d'après une référence qu'on appelle class. Nous allons voir que

- le mot-clé `class Point` permet de définir une nouvelle class d'objets,
- les classes se distinguent des objets d'une majuscule,
- l'expression `point = Point(1, 2)` crée une nouvelle instance et initialise avec des valeurs.

## Définir une classe

Le mot-clé `class` permet de définir une classe.
Le nom des classe est écrit avec une majuscule.

```{codeplay}
class Point():
    pass

p = Point()

print(p)
print(type(p))
```

**Exercice** : Créez une deuxième classe `Rectangle` et affichez son type.

## Définir des objets

A partir d'une class, nous pouvons créer autant d'objets que nous voulons.
Une classe est comme un moule qui nous permet de créer des copies, ou clones à partir d'une définition de classe.

On appelle ces objets des **instances** de la classe, et l'action de créer des objets est appelé **instancier**.

```{codeplay}
class Point():
    pass

p0 = Point()
p1 = Point()
p2 = Point()

print(p0, p1, p2)
```

**Exercice** : Instanciez des autres objets de la classe `Point`,

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

## Le constructeur `__init__()`

```{codeplay}
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p = Point()
p1 = Point(20, 30)

print(p1.x)
print(p1.y)
print(p1)
```

## Le descripteur `__str__()`

```{codeplay}
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

p = Point()
p1 = Point(20, 30)

print(p1.x)
print(p1.y)
print(p)
print(p1)
```

## Définir une méthode

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

print(p.x)
print(p.y)
print(p.norme())
print(p)
```

## Définir une classe `Dot()`

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

class Dot(): 
    def __init__(self, x=0, y=0, d=40, color='red'):
        self.x = x
        self.y = y
        self.d = d
        self.color = color
        self.draw()
        
    def draw(self):
        color(self.color)
        goto(self.x, self.y)
        dot(self.d)
        color('black')
        write(self.__str__())
       
    def __str__(self):
        return f'Dot({self.x}, {self.y}, {self.d}, {self.color})'
        
p0 = Dot()
p1 = Dot(-100, 100)
p2 = Dot(-200, -100, 60, 'lime')
p3 = Dot(100, 100, 100, 'yellow')

print(p0)
print(p1)
print(p2)
```

## Dot cliquable

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

class Dot(): 
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.state = False
        self.color = 'red'
        self.draw()
        
    def draw(self):
        color(self.color)
        goto(self.x, self.y)
        dot(self.d)
       
    def inside(self, x, y):
        dx = self.x - x
        dy = self.y -y
        r = self.d/2 
        return dx*dx + dy*dy < r*r
    
    def toggle(self):
        if self.state:
            self.color = 'green'
        else:
            self.color = 'red'
        self.state = not self.state
        self.draw()
    
        
p0 = Dot(-100, 100, 50)
p1 = Dot(-100, -100, 50)

def f(x, y):
    if p0.inside(x, y):
        p0.toggle()
        
    if p1.inside(x, y):
        p1.toggle()
          
getscreen().onclick(f)
getscreen().listen()
```

## Dot cliqable

```{codeplay}
from turtle import *

hideturtle()
speed(0)
up()

class Dot(): 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = False
        self.draw()
        
    def draw(self):
        color('yellow' if self.state else 'lightgray')
        goto(self.x, self.y)
        dot(40)
        color('black')
        sety(self.y - 10)
        write(int(self.state), font=(None, 18), align='center')
       
    def inside(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2 < (20 ** 2)
    
    def set(self, state):
        self.state = state
        self.draw()
    
    def toggle(self):
        self.set(not self.state)    
        
p0 = Dot(-100, 100)
p1 = Dot(-100, -100)
p2 = Dot(100, 0)

def f(x, y):
    if p0.inside(x, y):
        p0.toggle()
        
    if p1.inside(x, y):
        p1.toggle()
        
    p2.set(p0.state and p1.state)
            
getscreen().onclick(f)
getscreen().listen()
```

## Texte cliquable

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

class Bin4(): 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.n = 3
        self.draw()
        
    def draw(self):
        goto(self.x, self.y)
        down()
        color('black', 'white')
        begin_fill()
        for i in range(2):
            forward(100)
            left(90)
            forward(50)
            left(90)
        end_fill()
        up()
        
        goto(self.x+10, self.y+10)
        color('black')
        write(f'{self.n:04b}', font=('Courier', 24))
       
    def __str__(self):
        return f'Bin4({self.x}, {self.y})'
        
p0 = Bin4()
p1 = Bin4(-200, -100)
p2 = Bin4(100, -100)

print(p0)
print(p1)
print(p2)
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
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.n = 0
        self.draw()
        
    def draw(self):
        goto(self.x, self.y)
        color('linen')
        dot(60)
        color('black')
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
        
b0 = Bin4(-100, 100)
b1 = Bin4(100, 100)
b2 = Bin4(0, -100)

def f(x, y):
    b0.click(x, y)    
    b1.click(x, y)
    b2.set(b0.n + b1.n)
            
getscreen().onclick(f)
getscreen().listen()
```

## Dessiner le symbole ALU

L'unité arithmétique et logique (UAL, en anglais arithmetic–logic unit, ALU), est l'organe de l'ordinateur chargé d'effectuer les calculs.

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
        color('lightgray')
        dot(60)
        color('black')
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

## Classe Rect

```{codeplay}
from turtle import *
up()

class Rect:
    def __init__(self, x=0, y=0, w=100, h=50, col='yellow'):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col = col
        self.draw()
        
    def draw(self):
        goto(self.x, self.y)
        down()
        seth(0)
        fillcolor(self.col)
        begin_fill()
        for i in range(2):
            forward(self.w)
            left(90)
            forward(self.h)
            left(90)
        end_fill()
        up()
    
Rect()
Rect(100, -100, col='lime')
```

## Classe Card

```{codeplay}
from turtle import *
up()

class Card:
    couleur = '♥️♦️'

    def __init__(self, pos=(0, 0), size=(50, 100), r=10, fill='white'):
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
        write('♥️', font=(None, 40))
        
Card()
Card((50, 20), fill='pink')
Card((100, -120), (100, 50), r=20, fill='lime')
```

## N-uplet - `tuple`

Un **n-uplet** (tuple) est une séquence d'objets. Ce sont :

- multiple valeurs séparé par une virgule,
- une seule valeur terminé par une virgule,
- des parenthèses vides pour le tuple vide.

```{codeplay}
x = 1, 2
y = 1,
z = ()

print(x)
print(y)
print(z)
print(type(x))
```

Un tuple est le forme idéale pour représenter les deux coordonnées `(x, y)` d'une position, ou longueur et hauteur `(w, h)` d'une taille.

```{codeplay}
from turtle import *
up()

pos = 100, -20
size = 100, 70

print('pos =', pos)
print('x =', pos[0])
print('y =', pos[1])

print('size =', size)
print('w =', size[0])
print('h =', size[1])
print('size * 2 =', size * 2)

goto(pos)
down()
for d in size * 2:
    forward(d)
    left(90)
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
