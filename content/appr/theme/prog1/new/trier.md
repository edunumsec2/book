# Trier - `sort`

Pouvoir trier les éléments dans une liste est une fonctionnalité fondamentale dans l'informatique. Le succès énorme de Google est basé sur un tri efficace de l'information.

Les éléments de la liste peuvent être des nombres, des mots, ou des phrases. Si une liste est triée il devient très facile de trouver un élément dans la liste.

## Fonction `min` et `max`

Les fonctions `min()` et `max()` retournent le minimum et le maximum d'une liste.

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]

print(min(liste))
print(max(liste))
```

**Exercice** : Modifiez la liste et essayez de nouveau.

Comment marche l'algorithme de ces fonctions ?

## Trouver le minimum

Pour trouver le minimum dans une liste nous :

- prenons la première valeur comme minimum courant,
- parcourons le reste de la liste,
- gardons la valeur comme nouveau minimum si elle est plus petite.

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]

min = liste[0]
for val in liste[1:]:
    if val < min:
        min = val
        
print(min)
```

**Exercice** : Modifiez l'algorithme pour trouver le maximum.

## L'indice du minimum

Souvent on ne doit pas seulement trouver la valeur minimum, mais aussi son indice dans la liste.
Différent au cas précédent, nous itérons pas sur les valeurs, mais sur les indices.

```{codeplay}
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

**Exercice** : Modifiez l'algorithme pour trouver l'indice du maximum.

## Enumérer une liste

La fonction `enumerate()` permet d'énumérer une liste. Nous utilisons cette fonction dans une boucle `for` pour itérer à la fois sur l'indice et la valeur. Nous avons donc deux variables d'itération :

- `i` - index de l'élément
- `val` - valeur de l'élément

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]

for i, val in enumerate(liste):
    print(i, val)
```

**Exercice** : Modifier la liste et exécutez de nouveau.

Il est également possible d'énumérer une chaîne de caractères.

```{codeplay}
for i, val in enumerate('Python'):
    print(i, val)
```

## Minimum et son indice

Avec la fonction `enumerate()` nous pouvons itérer sur index et valeur à la fois.

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]

i_min, min = 0, liste[0]

for i, val in enumerate(liste):
    if val < min:
        i_min, min = i, val
        
print(i_min, min)
```

## Echanger deux éléments

Pour échanger deux éléments d'une liste nous utilisons une affectation multiple.

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]

print(liste)
liste[0], liste[1] = liste[1], liste[0]
print(liste)
````

Le programme devient plus lisible si nous définissons une fonction `echange()`.

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]

def echange(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]

print(liste)
echange(liste, 0, 2)
print(liste)
```

## Tri par sélection

L’algorithme du tri par sélection commence par rechercher le plus petit élément de la liste et l’échange avec le premier élément de la liste.

```{codeplay}
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

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]

def tri_selection(liste):
    for i in range(0,len(liste)-1):
        i_min = liste.index(min(liste[i:]))
        liste[i], liste[i_min] = liste[i_min], liste[i]

print(liste)
tri_selection(liste)
print(liste)
```

## Tri par insertion

Le **tri par insertion** est un algorithme de tri utilisé par la plupart des personnes pour trier des cartes à jouer.

Ci-dessous mous trions une liste en ordre décroissante, ce qui permet de bien voir ce qui se passe.
On peut alors observer comment le `4` descend vers le bas, ensuite c'est le tour du `3` de descendre vers le bas, et ainsi de suite.

```{codeplay}
a = [5, 4, 3, 2, 1]
print(a)

n = len(a)
for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break
        print(a)
```

## Tri à bulles

L’algorithme du tri à bulles compare les éléments voisins, deux par deux, et les met dans le bon ordre.
Ci-dessous mous trions une liste en ordre décroissante, ce qui permet de bien voir ce qui se passe.

On peut alors observer comment le `5` flotte vers le haut, ensuite c'est le tour du `4` monte vers la surface, comme des bulles dans l'eau.

```{codeplay}
a = [5, 4, 3, 2, 1]
print(a)

n = len(a)
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        print(a)
```

## Afficher des valeurs

Le programme ci-dessous crée et affiche `n` valeur aléatoires. Par la suite nous les utilisons pour illustrer les trois algorithmes de tri :

- par bulles
- par insertion
- par sélection

```{codeplay}
from turtle import *
from random import *

getscreen().bgcolor('skyblue')
color('blue')
hideturtle()
speed(0)
up()
a = []

def create(size):
    global n, d, x0, y0
    
    n = size
    d = 600//n
    x0 = -300+d//2
    y0 = 200 - d//2
    
    for i in range(n):
        y = randint(-y0, y0)
        a.append(y)
    
def show():
    for i in range(n):
        x = x0 + i * d
        y = a[i]
        goto(x, y)
        dot(d)

create(20)      
show()
```

## Echanger deux éléments

```{codeplay}
from turtle import *
from random import *

getscreen().bgcolor('skyblue')
color('blue')
hideturtle()
speed(0)
up()
a = []

def create(size):
    global n, d, x0, y0
    
    n = size
    d = 600 //n
    x0 = -300 + d // 2
    y0 = 200 - d // 2
    
    for i in range(n):
        y = randint(-y0, y0)
        a.append(y)
    
def show():
    for i in range(n):
        x = x0 + i * d
        y = a[i]
        goto(x, y)
        dot(d)

===    
def swap(i, j):
    color('white')
    goto(x0 + i * d, a[i])
    dot(d)
    goto(x0 + j * d, a[j])
    dot(d)
    
    color('blue')
    goto(x0 + i * d, a[j])
    dot(d)
    goto(x0 + j * d, a[i])
    dot(d)
    
    a[i], a[j] = a[j], a[i]

create(20)
show()

for i in range(n-1):
    swap(i, i+1)
```


## Bubble sort en action

```{codeplay}
from turtle import *
from random import *

getscreen().bgcolor('skyblue')
color('blue')
hideturtle()
speed(0)
up()
a = []

def create(size):
    global n, d, x0, y0
    
    n = size
    d = 600 //n
    x0 = -300 + d // 2
    y0 = 200 - d // 2
    
    for i in range(n):
        y = randint(-y0, y0)
        a.append(y)
    
def show():
    for i in range(n):
        x = x0 + i * d
        y = a[i]
        goto(x, y)
        dot(d)
   
def swap(i, j):
    color('white')
    goto(x0 + i * d, a[i])
    dot(d)
    goto(x0 + j * d, a[j])
    dot(d)
    
    color('blue')
    goto(x0 + i * d, a[j])
    dot(d)
    goto(x0 + j * d, a[i])
    dot(d)
    
    a[i], a[j] = a[j], a[i]

===
create(20)
show()

for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            swap(j, j+1)
```

## Tri par insertion en action

```{codeplay}
from turtle import *
from random import *

getscreen().bgcolor('skyblue')
color('blue')
hideturtle()
speed(0)
up()
a = []

def create(size):
    global n, d, x0, y0
    
    n = size
    d = 600 //n
    x0 = -300 + d // 2
    y0 = 200 - d // 2
    
    for i in range(n):
        y = randint(-y0, y0)
        a.append(y)
    
def show():
    for i in range(n):
        x = x0 + i * d
        y = a[i]
        goto(x, y)
        dot(d)
        
def swap(i, j):
    color('white')
    goto(x0 + i * d, a[i])
    dot(d)
    goto(x0 + j * d, a[j])
    dot(d)
    
    color('blue')
    goto(x0 + i * d, a[j])
    dot(d)
    goto(x0 + j * d, a[i])
    dot(d)
    
    a[i], a[j] = a[j], a[i]

===
create(20)
show()

for i in range(1, n):
    for j in range(i, 0, -1):
        while a[j] < a[j-1]:
            swap(j, j-1)
```

## Tri par sélection en action

```{codeplay}
from turtle import *
from random import *

getscreen().bgcolor('skyblue')
color('blue')
hideturtle()
speed(0)
up()
a = []

def create(size):
    global n, d, x0, y0
    
    n = size
    d = 600 //n
    x0 = -300 + d // 2
    y0 = 200 - d // 2
    
    for i in range(n):
        y = randint(-y0, y0)
        a.append(y)
    
def show():
    for i in range(n):
        x = x0 + i * d
        y = a[i]
        goto(x, y)
        dot(d)
        
def swap(i, j):
    color('white')
    goto(x0 + i * d, a[i])
    dot(d)
    goto(x0 + j * d, a[j])
    dot(d)
    
    color('blue')
    goto(x0 + i * d, a[j])
    dot(d)
    goto(x0 + j * d, a[i])
    dot(d)
    
    a[i], a[j] = a[j], a[i]

===
create(20)
show()

for i in range(n-1):
    i_min = i
    min = a[i]
    for j in range(i+1, n):
        if a[j] < a[i_min]:
            i_min = j
            min = a[j]
    swap(i, i_min)
```
