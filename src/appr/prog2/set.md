# Appartenir - `set`

La [théorie des ensembles](https://fr.wikipedia.org/wiki/Théorie_des_ensembles) est une théorie de l'appartenance. Un élément d'un ensemble est dit **appartenir** à cet ensemble. En Python, l'ensemble est une collection d'objets. Mais contrairement à une liste, ses éléments sont uniques et il n'y a pas le concept d'ordre. Nous allons voir que :

- l'expression `set()` est l'ensemble vide,
- l'ensemble `{1, 3, 2}` comporte 3 éléments,
- `union()`, `intersection()` et `difference()` sont des opérations sur des ensembles.

```{question}
L'expression `set('belle')` contient

{f}`1 élément`  
{f}`2 éléments`  
{v}`3 éléments`  
{f}`5 éléments`
```

## Un ensemble

Un **ensemble** est une collection d'objets ayant une propriété commune.

Dans l'exemple suivant, nous dessinons d'abord un cercle de rayon `r`.
Ensuite nous définissons une liste de 10 points à l'aide d'une compréhension de liste.
Chaque point est désigné par son indice qui va de 0 à 9.

Nous définissons comme ensemble `A` les points qui se trouvent à l'intérieur du cercle et nous les affichons en rouge.
Les points qui ne font pas partie de l'ensemble `A` sont affichés en bleu.
Nous commençons avec un ensemble vide `A = set()` et nous ajoutons des éléments avec l'instruction `A.add(i)`.

```{exercise}
Doublez le nombre des points.
```

```{codeplay}
:file: set1.py
from turtle import *
from random import *
getscreen().bgcolor('azure')

r = 160
dot(2 * r, 'pink')
write('A', font=(None, 24), align='center')

points = [(randint(-300, 280), randint(-200, 180)) for i in range(10)]

A = set()
i = 0

up()
for point in points:
    goto(point)
    if point[0]**2 + point[1]**2 < r**2:
        color('red')
        A.add(i)
    else:
        color('blue')
    dot(10)
    write(f'   {i}', font=(None, 12))
    i += 1
hideturtle()

print('A =', A)
```

## Diagramme de Venn

Un **diagramme de Venn** montre graphiquement la relation entre différents ensembles.

Dans l'exemple suivant, nous montrons les 3 situations :

- les deux ensembles A et B sont disjoints,
- les deux ensembles A et B ont une intersection non vide,
- l'ensemble B est totalement inclus dans l'ensemble A.

```{exercise}
Ajoutez un ensemble C.
```

```{codeplay}
:file: set2.py
from turtle import *
up()

def ensemble(x, texte, d=80):
    goto(x, 0)
    write(texte, font=(None, 12), align='center')
    forward(d/2)
    left(90)
    down()
    circle(d/2)
    up()
    
def etiquette(x, texte):
    goto(x, 100)
    write(texte, font=(None, 14), align='center')

etiquette(-175, 'ensembles disjoints')
ensemble(-220, 'A')
ensemble(-130, 'B')

etiquette(25, 'intersection')
ensemble(0, 'A')
ensemble(50, 'B')

etiquette(200, 'inclusion')
ensemble(200, 'A', 100)
ensemble(230, 'B', 30)
hideturtle()
```

## Des éléments uniques

Les éléments d'un ensemble sont uniques. Chaque élément apparait seulement une fois.
Le comportement est différent de celui d'une liste, ou des éléments peuvent apparaitre multiple fois.

```{exercise}
Affichez la longueur de la liste et de l'ensemble.
```

```{codeplay}
:file: set3.py
liste = [1, 2, 4, 2, 1, 3, 1]
ensemble = {1, 2, 4, 2, 1, 3, 1}

print('liste =', liste)
print('ensemble =', ensemble)
```

## Les méthodes `set`

Voici toutes les méthodes définies pour le type `set`.

```{codeplay}
print(dir(set()))
```

À l'aide d'une liste de compréhension, nous allons afficher seulement les méthodes qui ne commencent pas avec un tiret bas.

```{exercise}
Affichez aussi les méthodes pour le type `dict`.
```

```{codeplay}
:file: set3.py
print('set :')
print([x for x in dir(set()) if not x.startswith('_')])

print('\nlist :')
print([x for x in dir(list()) if not x.startswith('_')])
```

## L'union

L'union de deux ensembles est l'ensemble des éléments qui font partie des deux.

```{codeplay}
:file: set4.py
A = {1, 2, 3, 4}
B = {3, 4, 5}

print('union =', A.union(B))
```

Avec un diagramme de Venn nous représentons l'union des deux ensembles A et B avec la région rose.

```{exercise}
Ajoutez un ensemble `C` qui a une intersection non vide avec `A` et `B`.
```

```{codeplay}
:file: set5.py
from turtle import *
fillcolor('pink')
r = 120

up()
goto(0, 0.8 * r)
down()

begin_fill()
left(150)
circle(r, 240)
right(60)
circle(r, 240)
end_fill()

circle(r, 120)
left(60)
circle(r, 120)
```

## L'intersection

L'ensemble des éléments qui sont à la fois dans `A` et dans `B` constituent l'**intersection** de `A` et `B`.

```{codeplay}
:file: set6.py
from turtle import *
fillcolor('pink')
r = 120

up()
goto(0, 0.8 * r)
down()

left(150)
circle(r, 240)
right(60)
circle(r, 240)

begin_fill()
circle(r, 120)
left(60)
circle(r, 120)
end_fill()
```

Dans l'exemple suivant, nous créons une classe `Ensemble` qui permet de dessiner un diagramme de Venn avec :

- position x, y
- rayon r
- étiquette

La méthode `inside(x, y)` permet de déterminer si un point `(x, y)` fait partie de l'ensemble.

Ensuite nous créons des points aléatoires dans toute la surface du canevas.
Avec `A.inside(x, y) and B.inside(x, y)` nous sélectionnons la réunion.

```{exercise}
Placez les points dans la réunion de A et B.
```

```{codeplay}
:file: set7.py
from turtle import *
from random import *

hideturtle()
speed(0)
up()

class Ensemble:
    def __init__(self, x, y, r, label):
        self.x = x
        self.y = y
        self.r = r
        self.label = label
        self.draw()
    
    def inside(self, x, y):
        return (x-self.x)**2 + (y-self.y)**2 < self.r**2
    
    def draw(self):
        goto(self.x, self.y)
        dot(self.r * 2, 'pink')
        write(self.label, font=(None, 24))
        
A = Ensemble(-100, 0, 150, 'A')
B = Ensemble(100, 0, 150, 'B')

i = 0
while i < 200:
    x = randint(-300, 300)
    y = randint(-200, 200)
    if A.inside(x, y) and B.inside(x, y):      
        goto(x, y)
        dot(10, 'red')
        i += 1
```

## La différence

La différence entre deux ensembles `A` et `B` sont tous les éléments de `A` sans ceux de `B`. En Python, la différence d'ensemble peut être exprimée par la méthode `difference()` ou bien par l'opérateur `-` comme montré dans l'exemple suivant.

```{codeplay}
:file: set8.py
A = {0, 1, 2, 3}
B = {2, 3, 4, 5}

print('A =', A)
print('B =', B)
print()

print('A - B =', A.différence(B))
print('A - B =', A - B)
print('B - A =', B - A)
```

Il existe aussi une différence symétrique.

```{codeplay}
:file: set9.py
A = {0, 1, 2, 3}
B = {2, 3, 4, 5}

print('A =', A)
print('B =', B)
print('différence symétrique =', A.symmetric_difference(B))
```

## Un sous-ensemble

Un ensemble A est inclus dans un ensemble B si tous les éléments de A sont aussi éléments de B. On dit dans ce cas que A est un **sous-ensemble** ou une partie de B, ou encore que B est **sur-ensemble** de A.

```{codeplay}
:file: set10.py
A = {0, 1}
B = {0, 1, 2, 3}

print('A =', A)
print('B =', B)
print()

print('A est sous-ensemble de B =', A.issubset(B))
print('A est  sur-ensemble de B =', A.issuperset(B))
```

## Les opérateurs

En Python, les méthodes pour les ensembles ont des opérateurs plus courts :

- union (`|`)
- intersection (`&`)
- différence symétrique (`^`)

```{exercise}
Modifiez les ensembles A et B et reévaluez.
```

```{codeplay}
:file: set11.py
A = {0, 1, 2}
B = {1, 2, 3}

print('A =', A)
print('B =', B)
print()

print('A | B (union) =', A | B)
print('A & B (intersection) =', A & B)
print('A - B (différence) =', A - B)
print('B - A (différence) =', B - A)
print('A ^ B (différence symétrique) =', A ^ B)
```
