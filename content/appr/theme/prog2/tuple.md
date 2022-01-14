# Grouper - `tuple`

Dans ce chapitre nous allons voir une structure très similaire à une liste - le tuple.
Contrairement à la liste, le tuple est immuable, c'est à dire on peux accéder à ces éléments via un indice, mais on ne peux pas le changer.

## Une séquence d'objets

Des le premier chapitre nous avons vu qu'un programme est une séquence d'instructions.
Un tuple est une séquence d'objets

```{codeplay}
a = 1, 2, 3
print(a)
print()

sequence = 1, 1.2, 'hello'

for x in sequence:
    print(x, type(x), sep='\t')
```

**Exercice** : Ajoutez un élément de type `bool`.

## Un tuple dans un tuple

Un tuple peut être imbriqué dans un autre tuple.

```{codeplay}
x = 1, 2
print(x)

y = 3, 4
print(y)

a = x, y
print(a)
```

Nous pouvons utiliser un tuple pour une séquence de coordonnées qui représente une forme.

```{codeplay}
from turtle import *

maison = (0, 0), (200,0), (200, 100), (100, 150), (0, 100), (0, 0)

for p in maison:
    goto(p)
```

Nous pouvons utiliser un tuple pour une séquence de couleurs.

```{codeplay}
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
maison = (0, 0), (200,0), (200, 100), (100, 150), (0, 100), (0, 0)

print('simple index:', maison[2])
print('double index:', maison[2][0])
print('tranche:', maison[-3:])
```

## Les méthodes

```{codeplay}
print(dir(tuple()))
```

En Python, des noms de méthodes qui commencent et terminent par `__` (2 tirets bas) sont des méthodes spéciales. Ce sont ces méthodes qui font fonctionner les opérateurs tel que `+` ou `*`:

Ces opérations 'surchargent' les opérateurs standards. Les opérateurs standard (`+`, `*`) vont acquérir une nouvelle signification pour des objets de cette classe.

- `__add__  +`
- `__mul__   *`
- `__len__   len`

```{codeplay}
a = (1, 2, 1)
b = (3, 4)

print('a + b =', a.__add__(b))
print('a * 2 =', a.__mul__(2))
print('2 in a =', a.__contains__(2))
```

Et nous retrouvons ces 3 méthodes-ci qui existent aussi pour les listes.

```{codeplay}
a = (1, 2, 1)

print('a =', a)
print('len(a) =', a.__len__())
print('a.count(1) =', a.count(1))
print('a.index(2) =', a.index(2))
```

## classe Vec2D

La classe `Vec2D` définit des vecteurs 2D. Elle définit les opérations

- addition
- soustraction
- multiplication

```{codeplay}
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

```{codeplay}

```
