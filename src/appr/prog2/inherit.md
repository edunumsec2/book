# Hériter - `E(P)`

Dans ce chapitre nous découvrons comment une classe `E` peut hériter les attributs et les méthodes d'une classe parents `P`. Ceci permet de hiérarchiser notre code, et de facilement réutiliser des méthodes et des attributs, tout en laissant la liberté de les changer ou d'en ajouter des autres. Nous allons voir que :

- l'expression `class E(P):` désigne un héritage depuis la classe `P`,
- la fonction `super()` renvoie la classe parente,
- une méthode enfant avec le nom d'une méthode parent, remplace celle-ci.

```{question}
La la classe `P` dans `E(P)` est appelé

{v}`la classe parent`  
{f}`la classe enfant`  
{f}`la classe primaire`  
{f}`la classe principale`
```

## Une séquence d'objets

Des le tout premier chapitre nous avons vu qu'un programme est une séquence d'instructions. Un tuple est une séquence d'objets.

```{exercise}
Ajoutez un élément de type `bool`.
```

```{codeplay}
:file: ep1.py
a = 1, 2, 3
print(a)
print()

sequence = 1, 1.2, 'hello'

for x in sequence:
    print(x, type(x), sep='\t')
```

## Un tuple dans un tuple

Un tuple peut être imbriqué dans un autre tuple.

```{codeplay}
:file: ep2.py
x = 1, 2
print(x)

y = 3, 4
print(y)

a = x, y
print(a)
```

Nous pouvons utiliser un tuple pour une séquence de coordonnées qui représente une forme.

```{codeplay}
:file: ep3.py
from turtle import *

maison = (0, 0), (200,0), (200, 100), (100, 150), (0, 100), (0, 0)

for p in maison:
    goto(p)
```

Nous pouvons utiliser un tuple pour une séquence de couleurs.

```{codeplay}
:file: ep4.py
from turtle import *
up()

colors = 'red', 'pink', 'violet', 'blue'

d = 50
for x in colors:
    dot(d, x)
    forward(d)
```

## Indexer un tuple

Un index `[i]` permet d'extraire un élément.
L'opérateur de tranche `[i:j]` permet d'extraire un sous-tuple.

```{codeplay}
:file: ep5.py
maison = (0, 0), (200,0), (200, 100), (100, 150), (0, 100), (0, 0)

print('simple index:', maison[2])
print('double index:', maison[2][0])
print('tranche:', maison[-3:])
```

## Les méthodes

```{codeplay}
print(dir(tuple()))
```

En Python, des noms de méthodes qui commencent et terminent par `__` (2 tirets bas) sont des méthodes spéciales. Ce sont ces méthodes qui font fonctionner les opérateurs tels que `+` ou `*`:

Ces opérations 'surchargent' les opérateurs standards. Les opérateurs standard (`+`, `*`) vont acquérir une nouvelle signification pour des objets de cette classe.

- `__add__  +`
- `__mul__   *`
- `__len__   len`

```{codeplay}
:file: ep6.py
a = (1, 2, 1)
b = (3, 4)

print('a + b =', a.__add__(b))
print('a * 2 =', a.__mul__(2))
print('2 in a =', a.__contains__(2))
```

Et nous retrouvons ces 3 méthodes-ci qui existent aussi pour les listes.

```{codeplay}
:file: ep7.py
a = (1, 2, 1)

print('a =', a)
print('len(a) =', a.__len__())
print('a.count(1) =', a.count(1))
print('a.index(2) =', a.index(2))
```

## classe Vec2D

La classe `Vec2D` définit des vecteurs 2D. Elle définit les opérations :

- addition
- soustraction
- multiplication

```{codeplay}
:file: ep8.py
class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __ne__(self, other):
        return not self.__eq__(other)

a = Vec2D(2, 3)
b = Vec2D(3, 4)

print('a =', a)
print('b =', b)
print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a == b =', a == b)
print('abs(a) =', abs(a))
print('abs(b) =', abs(b))
```

## Visualiser Vect2D

```{codeplay}
:file: ep9.py
from turtle import *
up()

class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def show(self, col='black'):
        color(col)
        goto(0, 0)
        seth(towards(self.x, self.y))
        down()
        goto(self.x, self.y)
        stamp()
        up()

a = Vec2D(100, 50)
b = Vec2D(150, -50)
c = a + b

a.show()
b.show()
c.show('red')
```

## Classe Dot, Rect, Text

Dans l'exemple suivant, nous définissons une classe parente `Object`. Elle possède les méthodes.

- `draw_box()` pour dessiner un contour rectangulaire
- `fill_box()` pour dessiner un rectangle rempli
- `inside(x, y)` pour tester si le point `(x, y)` se trouve dans le rectangle

Les trois fonctions `Dot`, `Rect` et `Text` héritent tous les méthodes de la classe parent `Object`.

```{exercise}
Cliquez dans tous les objets et observez les infos affichées dans la console.
```

```{codeplay}
:file: ep10.py
from turtle import *
up()
speed(0)
hideturtle()
getscreen().bgcolor('lightgray')

class Object:
        
    def draw_box(self):
        goto(self.pos)
        down()
        for d in self.size * 2:
            forward(d)
            left(90)
        up()
        
    def fill_box(self):
        goto(self.pos)
        color(*self.col)
        width(self.width)
        begin_fill()
        self.draw_box()
        end_fill()
        width(1)

    def inside(self, x, y):
        x0, y0 = self.pos
        x1 = x0 + self.size[0]
        y1 = y0 + self.size[1]
        return x0 < x < x1 and y0 < y < y1
        
    def __str__(self):
        return f'{self.__class__.__name__}({self.pos}, {self.size})'

class Dot(Object):
    def __init__(self, pos, d=20, col='red'):
        self.pos = pos
        self.size = d, d
        self.col = col
        self.draw()
        
    def draw(self):
        r = self.size[0] / 2
        goto(self.pos[0]+r, self.pos[1]+r)
        pencolor(self.col)
        dot(self.size[0])
        self.draw_box()
    
class Rect(Object):
    def __init__(self, pos, size, width=1, col=('black', 'white')):
        self.pos = pos
        self.size = size
        self.width = width
        self.col = col
        self.draw()
        
    def draw(self):
        self.fill_box()        
             
class Text(Object):
    def __init__(self, pos, text, col='red', font=(None, 12, 'normal'), align='left'):
        super()
        self.text = text
        self.pos = pos
        self.col = col
        self.font = font
        self.align = align
        self.draw()
        
    def draw(self):
        goto(self.pos)
        color(self.col)
        x0 = xcor()
        write(self.text, font=self.font, align=self.align, move=True)
        self.size = xcor() - x0, self.font[1]
        self.draw_box()
        
d0 = Dot((0, 0))
d1 = Dot((100, 20), 50, 'lime')

t0 = Text((0, 50), 'origin', font=(None, 18, 'bold'))
t1 = Text((0, 100), 'pad', font=(None, 80), col='blue')
t2 = Text((-100, 100), '夢', font=(None, 60), col='blue')
t3 = Text((-200, 100), '📺', font=(None, 60), col='blue')

r0 = Rect((-100, 0), (50, 80))
r1 = Rect((-150, -20), (60, 80), width=5, col=('black', 'pink'))

def f(x, y):
    for obj in (d0, d1, t0, t1, t2, t3, r0, r1):
        if obj.inside(x, y):
            print('clicked in', obj)
    
getscreen().onclick(f)
getscreen().listen()
```
