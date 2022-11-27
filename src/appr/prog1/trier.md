(prog1.trier)=

# Trier - `sort()`

Dans ce chapitre, nous allons découvrir quelques algorithmes de tri.
Pouvoir trier les éléments d'une liste est une fonctionnalité fondamentale dans l'informatique. Le succès énorme de Google est basé sur un tri efficace de l'information, car dans une liste triée on peut trouver un élément **beaucoup** plus vite. Nous allons voir que :

- la fonction `min(liste)` retourne le minimum,
- la fonction `max(liste)` retourne le maximum,
- la méthode `liste.sort()` trie une liste.

Lorsque vous jouez aux cartes, vous triez vos cartes par valeur et dans ce cas, vous utilisez sans le savoir un algorithme de tri.

```{image} media/cartes.webp
:width: 300px
```

## Fonction `min` et `max`

Les fonctions `min()` et `max()` retournent le minimum et le maximum d'une liste à l'aide d'un algorithme.  
Mais comment fonctionne cet algorithme ?

```{exercise}
Modifiez la liste avec de nouvelles valeurs et essayez de nouveau.
```

```{codeplay}
:file: sort1.py
liste = [3, 4, 1, 2, 6, 5]

print(min(liste))
print(max(liste))
```

## Trouver le minimum

Pour trouver le minimum dans une liste il faut :

- prendre la première valeur comme minimum courant,
- parcourir le reste de la liste,
- garder la valeur comme nouveau minimum si elle est plus petite.

```{exercise}
Modifiez l'algorithme pour trouver le minimum ET le maximum.
```

```{codeplay}
:file: sort2.py
liste = [3, 4, 1, 2, 6, 5]

min = liste[0]
for val in liste[1:]:
    if val < min:
        min = val
        
print(min)
```

## Créer une liste

Pour visualiser les algorithmes que nous allons rencontrer dans ce chapitre,
nous allons créer des listes avec des nombres aléatoires.

Avec une compréhension nous allons créer :

- une liste `x` avec des valeurs équidistantes dans l'intervalle [-300, 300]
- une liste `y` avec des valeurs aléatoires dans l'intervalle [-200, 200]

```{exercise}
Modifiez `n` à 14.
```

```{codeplay}
:file: sort3.py
from random import *

n = 10
d = 600//n
x0 = 300 - d//2
y0 = 200 - d//2
x = [-x0 + i * d for i in range(n)]
y = [randint(-y0, y0) for i in range(n)]

print('x =', x)
print('y =', y)
```

## Visualiser une liste

Nous utilisons les listes `x` et `y` pour afficher des points et visualiser la liste `y`.

```{exercise}
Modifiez le nombre d'éléments.
```

```{codeplay}
:file: sort4.py
from turtle import *
from random import *

color('blue')
speed(0)
up()

def create(size, bg='skyblue'):
    global n, d, x, y
    getscreen().bgcolor(bg)
    n = size
    d = 600/n
    x0 = 300 - d//2
    y0 = 200 - d//2
    x = [-x0 + i * d for i in range(n)]
    y = [randint(-y0, y0) for i in range(n)]
                 
def show():
    for i in range(n):
        goto(x[i], y[i])
        dot(d)

create(20)
show()
```

## Visualiser un algorithme

Pour visualiser l'algorithme du minimum, nous dessinons en rouge les valeurs du minimum courant.
Cet algorithme :

- prend la première valeur comme minimum courant,
- parcourt le reste de la liste,
- garde la valeur comme nouveau minimum si elle est plus petite.

```{exercise}
Modifiez l'algorithme pour visualiser le minimum ET le maximum.
```

```{codeplay}
:file: sort5.py
from turtle import *
from random import *

color('blue')
speed(0)
up()

def create(size, bg='skyblue'):
    global n, d, x, y
    getscreen().bgcolor(bg)
    n = size
    d = 600/n
    x0 = 300 - d//2
    y0 = 200 - d//2
    x = [-x0 + i * d for i in range(n)]
    y = [randint(-y0, y0) for i in range(n)]
                 
def show():
    for i in range(n):
        goto(x[i], y[i])
        dot(d)
=== 
create(30)
show()

speed(3)
color('red')
for i in range(n):
    if i == 0:
        min = y[i]
    else:
        if y[i] < min:
            min = y[i]
    goto(x[i], min)
    down()
    dot(d/2)
```

## L'indice du minimum

Souvent, on ne doit pas seulement trouver la valeur minimum, mais aussi son indice dans la liste.
Contrairement au cas précédent, ici nous ne parcourons pas les valeurs, mais les indices.

```{exercise}
Modifiez l'algorithme pour trouver l'indice du minimum ET maximum.
```

```{codeplay}
:file: sort6.py
liste = [3, 4, 1, 2, 6, 5]

min = liste[0]
i_min = 0
n = len(liste)

for i in range(1, n):
    if liste[i] < min:
        min = liste[i]
        i_min = i
        
print(i_min)
```

## Échanger deux éléments

Pour échanger deux éléments d'une liste, nous utilisons une affectation multiple.
Ici nous échangeons les deux premiers éléments, donc les éléments avec les indices 0 et 1.

```{codeplay}
:file: sort7.py
liste = [3, 4, 1, 2, 6, 5]

print(liste)
liste[0], liste[1] = liste[1], liste[0]
print(liste)
```

Le programme devient plus lisible si nous définissons une fonction `echange()`.

```{codeplay}
:file: sort8.py
liste = [3, 4, 1, 2, 6, 5]

def echange(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]

print(liste)
echange(liste, 0, 2)
print(liste)
```

## Déplacer un point

Pour visualiser le déplacement d'un point de l'indice `i` vers l'indice `j` nous effaçons le premier point en le dessinant en blanc, et nous indiquons avec une ligne le déplacement vers la nouvelle position.

```{codeplay}
:file: sort9.py
from turtle import *
from random import *

color('blue')
speed(0)
up()

def create(size, bg='skyblue'):
    global n, d, x, y
    getscreen().bgcolor(bg)
    n = size
    d = 600/n
    x0 = 300 - d//2
    y0 = 200 - d//2
    x = [-x0 + i * d for i in range(n)]
    y = [randint(-y0, y0) for i in range(n)]
                 
def show():
    for i in range(n):
        goto(x[i], y[i])
        dot(d)
===
def move(i, j):
    goto(x[i], y[i])
    color('white')
    dot(d)
    down()
    goto(x[j], y[i])
    color('blue')
    dot(d)
    up()

create(15)
show()

speed(3)
move(3, 13)
```

## Échanger deux points

Pour échanger deux points, il faut :

- déplacer point `i` vers `j`
- déplacer point `j` vers `i`
- échanger les deux éléments dans la liste

```{codeplay}
:file: sort10.py
from turtle import *
from random import *

color('blue')
speed(0)
up()

def create(size, bg='skyblue'):
    global n, d, x, y
    getscreen().bgcolor(bg)
    n = size
    d = 600/n
    x0 = 300 - d//2
    y0 = 200 - d//2
    x = [-x0 + i * d for i in range(n)]
    y = [randint(-y0, y0) for i in range(n)]
                 
def show():
    for i in range(n):
        goto(x[i], y[i])
        dot(d)

def move(i, j):
    goto(x[i], y[i])
    color('white')
    dot(d)
    down()
    goto(x[j], y[i])
    color('blue')
    dot(d)
    up()
===
def swap(i, j):
    move(i, j)
    move(j, i)
    y[i], y[j] = y[j], y[i]

create(15)
show()

speed(3)
swap(3, 13)
```

## Échanger tous les points

Dans l'exemple suivant, nous échangeons deux points successifs pour toute la liste. Nous observons que :

- le premier point avance complètement de gauche à droite
- tous les autres points reculent d'une position

```{codeplay}
:file: sort11.py
from turtle import *
from random import *

color('blue')
speed(0)
up()

def create(size, bg='skyblue'):
    global n, d, x, y
    getscreen().bgcolor(bg)
    n = size
    d = 600/n
    x0 = 300 - d//2
    y0 = 200 - d//2
    x = [-x0 + i * d for i in range(n)]
    y = [randint(-y0, y0) for i in range(n)]
                 
def show():
    for i in range(n):
        goto(x[i], y[i])
        dot(d)

def move(i, j):
    goto(x[i], y[i])
    color('white')
    dot(d)
    down()
    goto(x[j], y[i])
    color('blue')
    dot(d)
    up()

def swap(i, j):
    move(i, j)
    move(j, i)
    y[i], y[j] = y[j], y[i]
===
create(15)
show()

speed(3)
for i in range(n-1):
    swap(i, i+1)
```

## Tri par sélection

L’algorithme du **tri par sélection** commence par rechercher le plus petit élément de la liste et l’échange avec le premier élément de la liste.

```{image} media/tri_selection.jpg
:width: 200px
```

 Il recherche ensuite le plus petit élément de la liste restante. Il sélectionne ainsi le deuxième plus petit élément de la liste et l’échange avec le deuxième élément de la liste. Et ainsi de suite.

```{codeplay}
:file: sort12.py
liste = [3, 4, 1, 2, 6, 5]
print(liste)

def echange(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]

n = len(liste)
for i in range(n-1):
    i_min = i
    min = liste[i]
    for j in range(i+1, n):
        if liste[j] < liste[i_min]:
            i_min = j
            min = liste[j]
    echange(liste, i, i_min)
    print(liste)
```

Avec les fonctions `min()` et `index()` nous pouvons écrire cet algorithme de façon encore plus compacte.

```{codeplay}
:file: sort13.py
liste = [3, 4, 1, 2, 6, 5]

def tri_selection(liste):
    for i in range(0,len(liste)-1):
        i_min = liste.index(min(liste[i:]))
        liste[i], liste[i_min] = liste[i_min], liste[i]
        print(liste)

print(liste)
tri_selection(liste)
```

Voici une visualisation du tri par sélection.

```{exercise}
Modifiez la taille de la liste.
```

```{codeplay}
:file: sort14.py
from turtle import *
from random import *

color('blue')
speed(0)
up()

def create(size, bg='skyblue'):
    global n, d, x, y
    getscreen().bgcolor(bg)
    n = size
    d = 600/n
    x0 = 300 - d//2
    y0 = 200 - d//2
    x = [-x0 + i * d for i in range(n)]
    y = [randint(-y0, y0) for i in range(n)]

def show():           
    for i in range(n):
        goto(x[i], y[i])
        dot(d)

def move(i, j):
    goto(x[i], y[i])
    color('white')
    dot(d)
    down()
    goto(x[j], y[i])
    color('blue')
    dot(d)
    up()

def swap(i, j):
    move(i, j)
    move(j, i)
    y[i], y[j] = y[j], y[i]
===
create(20)
show()

for i in range(n-1):
    i_min = i
    min = y[i]
    for j in range(i+1, n):
        if y[j] < y[i_min]:
            i_min = j
            min = y[j]
    swap(i, i_min)
show()
```

## Tri par insertion

L'algorithme du **tri par insertion** est utilisé par la plupart des personnes pour trier des cartes à jouer. On prend les cartes non triées depuis la table, et on les insère à l'endroit correct dans sa main.

```{image} media/tri_insertion.jpg
:width: 200px
```

L’algorithme du tri par insertion parcourt la liste d’éléments à trier du deuxième au dernier élément. Pour chaque nouvel élément considéré, il l’insère à l’emplacement correct dans la liste déjà parcourue.

```{codeplay}
:file: sort15.py
y = [3, 4, 1, 2, 6, 5]

n = len(y)
for i in range(1, n):
    for j in range(i, 0, -1):
        if y[j] < y[j-1]:
            y[j], y[j-1] = y[j-1], y[j]
        else:
            break
    print(y)
```

Voici une visualisation du tri par insertion.

```{exercise}
Modifiez la taille de la liste.
```

```{codeplay}
:file: sort16.py
from turtle import *
from random import *

color('blue')
speed(0)
up()

def create(size, bg='skyblue'):
    global n, d, x, y
    getscreen().bgcolor(bg)
    n = size
    d = 600/n
    x0 = 300 - d//2
    y0 = 200 - d//2
    x = [-x0 + i * d for i in range(n)]
    y = [randint(-y0, y0) for i in range(n)]

def show():          
    for i in range(n):
        goto(x[i], y[i])
        dot(d)

def move(i, j):
    goto(x[i], y[i])
    color('white')
    dot(d)
    down()
    goto(x[j], y[i])
    color('blue')
    dot(d)
    up()

def swap(i, j):
    move(i, j)
    move(j, i)
    y[i], y[j] = y[j], y[i]
===
create(20)
show()

for i in range(1, n):
    for j in range(i, 0, -1):
        while y[j] < y[j-1]:
            swap(j, j-1)
show()
```

## Tri à bulles

L’algorithme du **tri à bulles** compare les éléments voisins, deux par deux, et les met dans le bon ordre. Le mot 'bulles' fait référence aux bulles dans une boisson qui montent à la surface.

```{image} media/bulles.jpg
:width: 300px
```

Dans l'exemple suivant, nous pouvons voir comment le `4` flotte vers le haut, jusqu'à ce qu'il rencontre le le `6` qui monte alors tout vers la surface, comme des bulles dans une boisson.

```{image} media/tri_bulles.jpg
:width: 200px
```

```{codeplay}
:file: sort17.py
y = [3, 4, 1, 2, 6, 5]
print(y)

n = len(y)
for i in range(n-1):
    for j in range(n-i-1):
        if y[j] > y[j+1]:
            y[j], y[j+1] = y[j+1], y[j]
        print(y)
```

Voici une visualisation du tri à bulles.

```{exercise}
Modifiez la taille de la liste.
```

```{codeplay}
:file: sort18.py
from turtle import *
from random import *

color('blue')
speed(0)
up()

def create(size, bg='skyblue'):
    global n, d, x, y
    getscreen().bgcolor(bg)
    n = size
    d = 600/n
    x0 = 300 - d//2
    y0 = 200 - d//2
    x = [-x0 + i * 600/n for i in range(n)]
    y = [randint(-y0, y0) for i in range(n)]

def show():              
    for i in range(n):
        goto(x[i], y[i])
        dot(d)

def move(i, j):
    goto(x[i], y[i])
    color('white')
    dot(d)
    down()
    goto(x[j], y[i])
    color('blue')
    dot(d)
    up()

def swap(i, j):
    move(i, j)
    move(j, i)
    y[i], y[j] = y[j], y[i]
===
create(20)
show()

for i in range(n-1):
    for j in range(n-i-1):
        if y[j] > y[j+1]:
            swap(j, j+1)
show()
```
