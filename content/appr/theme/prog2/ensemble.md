# Ensemble - `set`

Dans ce chapitre nous découvrons les ensembles. Comme la liste, l'ensemble est une collection d'objets. Mais ses éléments sont uniques et il n'y a pas le concept d'ordre. Nous allons voir que

- `set()` est l'ensemble vide,
- l'ensemble `{1, 3, 2}` comporte 3 éléments,
- `union()`, `intersection()` et `difference()` sont des opérations sur des ensembles.

## Un ensemble

Un **ensemble** est une collection d'objets ayant une propriété commune.

Dans l'exemple suivant nous dessinons d'abord un cercle de rayon `r`.
Ensuite nous définissons une liste de 10 points à l'aide d'une compréhension de liste.
Chaque points est désigné par son indice qui va de 0 à 9.

Nous définissons comme ensemble `A` les points qui se trouvent à l'intérieur du cercle et nous les affichons en rouge.
Les points qui ne font pas partie de l'ensemble `A` sont affichés en bleu.
Nous commençons avec un ensemble vide `A = set()` et nous ajoutons des éléments avec l'instruction `A.add(i)`.

```{codeplay}
from turtle import *
from random import *
getscreen().bgcolor('azure')

r = 160
dot(2 * r, (1, 0, 0, 0.3))
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

**Exercice** : Doublez le nombre des points.

## Diagramme de Venn

Un **diagramme de Venn** montre graphiquement la relation entre différents ensembles.

Dans l'exemple suivant nous montrons les 3 situations :

- les deux ensembles A et B sont disjoints,
- les deux ensembles A et B ont une intersection non vide,
- l'ensemble B est totalement inclus dans l'ensemble A.

```{codeplay}
from turtle import *
getscreen().bgcolor('azure')
up()

def ensemble(x, texte, d=80):
    goto(x, 0)
    dot(d, (1, 0, 0, 0.5))
    write(texte, font=(None, 14), align='center')
    
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
ensemble(200, 'A')
ensemble(220, 'B', 40)
hideturtle()
```

**Exercice** : Changez la couleur des diagrammes en vert.

## Des éléments uniques

Les éléments d'un ensemble sont uniques. Chaque élément apparait seulement une fois.
Le comportement est différent de celui d'une liste, ou des éléments peuvent apparaitre multiple fois.

```{codeplay}
liste = [1, 2, 4, 2, 1, 3, 1]
ensemble = {1, 2, 4, 2, 1, 3, 1}

print('liste =', liste)
print('ensemble =', ensemble)
```

**Exercice** : Affichez la longueur de la liste et de l'ensemble.

## Les méthodes `set`

Voici toutes les méthodes définis pour le type `set`.

```{codeplay}
print(dir(set()))
```

A l'aide d'une liste de compréhension nous allons afficher seulement les méthodes qui ne commencent pas avec un tiret bas.

```{codeplay}
print('set :')
print([x for x in dir(set()) if not x.startswith('_')])

print('\nlist :')
print([x for x in dir(list()) if not x.startswith('_')])
```

**Exercice** : Affichez aussi les méthodes pour le type `dict`.

## L'union

L'union de deux ensemble est l'ensemble des éléments qui fait partie des deux.

```{codeplay}
A = {1, 2, 3, 4}
B = {3, 4, 5}

print('union =', A.union(B))
```

Avec un diagramme de Venn nous représentons l'union des deux ensembles A et B avec la région rose.

```{codeplay}
from turtle import *
up()
d = 200

goto(-70, 0)
dot(d, (1, 0, 0, 0.5))
write('A', font=(None, 24), align='center')

goto(70, 0)
dot(d, (1, 0, 0, 0.5))
write('B', font=(None, 24), align='center')

hideturtle()
```

**Exercice** : Ajoutez un ensemble `C` qui a une intersection non-vide avec `A` et `B`.

## L'intersection

L'ensemble des éléments qui sont à la fois dans `A` et dans `B` constituent l'**intersection** de `A` et `B`.

```{codeplay}
from turtle import *

r = 120
fillcolor(1, 0, 0, 0.5)

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

Ensuite nous créons des points aléatoires dans toutes la surface du canevas.
Avec `A.inside(x, y) and B.inside(x, y)` nous sélectionnons la réunion.

```{codeplay}
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
        dot(self.r * 2, (1, 0, 0, 0.3))
        write(self.label, font=(None, 24))
        
A = Ensemble(-100, 0, 150, 'A')
B = Ensemble(100, 0, 150, 'B')

i = 0
while i < 50:
    x = randint(-300, 300)
    y = randint(-200, 200)
    if A.inside(x, y) and B.inside(x, y):      
        goto(x, y)
        dot(10, (1, 0, 0, 0.5))
        i += 1
```

**Exercice** : Placez les points dans la réunion de A et B.

## La différence

La différence entre deux ensembles `A` et `B` sont tous les éléments de `A` sans ceux de `B`. En Python, la différence d'ensemble peut être exprimé par la méthode `difference()` ou bien par l'opérateur `-` comme montré dans l'exemple suivant.

```{codeplay}
A = {0, 1, 2, 3}
B = {2, 3, 4, 5}

print('A =', A)
print('B =', B)
print()

print('A - B =', A.difference(B))
print('A - B =', A - B)
print('B - A =', B - A)
```

Il existe aussi une différence symétrique.

```{codeplay}
A = {0, 1, 2, 3}
B = {2, 3, 4, 5}

print('A =', A)
print('B =', B)
print('différence symétrique =', A.symmetric_difference(B))
```

## Un sous-ensemble

Un ensemble A est inclus dans un ensemble B si tous les éléments de A sont aussi éléments de B. On dit dans ce cas que A est un **sous-ensemble** ou une partie de B, ou encore que B est **sur-ensemble** de A.

```{codeplay}
A = {0, 1}
B = {0, 1, 2, 3}

print('A =', A)
print('B =', B)
print()

print('A est sous-ensemble de B =', A.issubset(B))
print('A est  sur-ensemble de B =', A.issuperset(B))
```

## Les opérateurs

En Python, les méthodes pour les ensembles ont des opérateurs plus court :

- union (`|`)
- intersection (`&`)
- différence symétrique (`^`)

```{codeplay}
A = {0, 1, 2}
B = {1, 2, 3}

print('A =', A)
print('B =', B)
print()

print('A | B (union) =', A | B)
print('A & B (intersection) =', A & B)
print('A - B (différence) =', A - B)
print('B - A (différence) =', B - A)
print('A ^ B (difference symétrique) =', A ^ B)
```

**Exercice** : Modifiez les ensemble A et B et re-évaluez.

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```
