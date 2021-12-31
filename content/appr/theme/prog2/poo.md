# Objet - `class`

La programmation orientée objet (POO) considère les éléments d'un programme comme des objets. Ces objets peuvent appartenir à différents catégories ou classes.

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

On appelle ces objets des **instances** de la classe, et l'action de créer des objets est appelé **instantier**.

```{codeplay}
class Point():
    pass

p0 = Point()
p1 = Point()
p2 = Point()

print(p0, p1, p2)
```

**Exercice** : Instantie des autres objets de la classe `Point`,

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


## Dot clickable

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


## Dot clickable

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