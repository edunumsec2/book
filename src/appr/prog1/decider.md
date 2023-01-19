(prog1.decider)=

# Décider - `if`

Dans ce chapitre, nous allons voir comment un programme peut faire des choix, et comment il peut exécuter du code de façon sélective. Nous allons voir que :

- le mot-clé `if` permet une exécution conditionnelle,
- le mot-clé `if-else` permet de choisir entre deux alternatives,
- le mot-clé `elif` (else if) permet d'ajouter différentes conditions.

```{question}
En Python, `if` est suivi

{f}`d'un bloc`  
{v}`d'une condition`  
{f}`de parenthèses`  
{f}`d'un deux-points`
```

## Comparer

Un programme doit parfois comparer deux valeurs.
Python connait six types de comparaisons :

- plus petit (`<`),
- plus petit ou égal (`<=`),
- égal (`==`),
- différent (`!=`),
- plus grand  (`>`),
- plus grand ou égal (`>=`).

Dans des formules mathématiques nous utilisons les symboles ≤,  ≥ et ≠. En Python vous devez utiliser deux symboles: `<=`, `>=` et `!=` à la place.

```{exercise}
Ajoutez des exemples avec les autres 5 comparateurs.
````

```{codeplay}
x = 3
print('x =', x)
print('(x > 2) =', x > 2)
```

```{question}
L'expression `x == 2`

{f}`met la valeur 2 dans la variable x`  
{v}`compare deux valeurs`  
{f}`affecte la variable x avec une valeur`  
{v}`retourne True ou False`
```

```{caution}
Il ne faut pas confondre l'opérateur d'affectation (`x = 2`) avec l'opérateur de comparaison (`x == 2`).
```

Le résultat d'une comparaison est une valeur booléenne, soit `True` soit `False`.

```{exercise}
Que se passe-t-il si vous échangez les deux éléments dans `x == 2` ?  
Et si vous échangez les deux éléments dans `x = 2`  ?
```

```{codeplay}
x = 2       # affectation
x == 2      # comparaison
print(x)
print(x == 2)
```

### Êtes-vous majeur ?

Basé sur votre âge, le programme exécute soit le premier bloc (`if`) soit le  deuxième bloc (`else`).  Il affiche si vous êtes majeur ou pas.

```{codeplay}
:file: if1.py
age = input('Entrez votre âge: ')

if int(age) < 18:
    print('accès interdit - vous êtes mineur')
else:
    print('accès OK - vous êtes majeur')
```

### Le signe d'un nombre

Le mot-clé `elif` est une contraction de **else if** et permet de continuer à tester d'autres conditions.
Trouvez le signe d'un nombre.

```{codeplay}
:file: if4.py
n = input('Entrez un nombre: ')
n = int(n)

if n > 0:
    print('positif')
elif n < 0:
    print('négatif')
else:
    print('zéro')
```

Sans le mot-clé `elif` nous devrions mettre le bloc `if` à l'intérieur du bloc  `else` en indentation.
Avec multiples conditions, les blocs se décalent de plus en plus et rendent le programme illisible.

```{exercise}
Testez le programme avec -2, 0, 3.
```

```{codeplay}
:file: if4.py
n = input('Entrez un nombre: ')
n = int(n)

if n > 0:
    print('positif')
else:
    if n < 0:
        print('négatif')
    else:
        print('zéro')
```

## Visualiser la comparaison

Dans l'exemple suivant, nous visualisons le résultat des 6 comparateurs en affichant graphiquement le résultat des 6 comparaisons du type `i < n`. 

- La variable `i` va de -9 à 9
- La variable `n` est marquée en rouge
- Le résultat `True ` est exprimé avec un grand point, `False` avec un petit

Que fait l'expression `'red' if i == n else 'black'` ?

Elle renvoie `'red'` si `i == n` et `'black'` autrement.

```{exercise}
Modifiez la variable `n` et exécutez le code de nouveau.
```

```{codeplay}
from turtle import *
d = 20      # dimension de base
n = 2       # valeur de comparaison
up()

for j in range(7):
    for i in range(-10, 10):
        goto(i*d, 100-j*d)
        color('red' if i == n else 'black')
        if i == -10:
            c = ('i', '< n', '<= n', '== n', '!= n', '>= n', '> n')[j]
            write(c, font=(None, d//2), align='right')
        elif j == 0:
            write(i, font=(None, d//2), align='center')
        else:
            result = (0, i<n, i<=n, i==n, i!=n, i>=n, i>n)[j]
            dot(d if result else d/4)
```

## Une position aléatoire

Dans ce chapitre nous allons prendre des décisions basées sur la position `(x, y)` d'un point.
Nous avons donc besoin d'un certain nombre de points, pour ensuite prendre des décisions.

```{exercise}
Les variables `w, h` (width, height) représentent largeur et hauteur de la plage rectangulaire des valeurs aléatoires. 
Modifiez-les vers `280, 180` et exécutez le code de nouveau.
```

```{codeplay}
from turtle import *
from random import *

w, h = 300, 200
d, n = 10, 100
up()
speed(0)

for i in range(n):
    x, y = randint(-w, w), randint(-h, h)
    goto(x, y)
    dot(d)
```

## Exécution conditionnelle

La structure `if` ci-dessous permet d'exécuter une action seulement si `condition` est `True`.

``` python
if condition:
    action
```

Dans notre exemple nous affichons un point rouge seulement si x est positif (`x > 0`)

```{exercise}
Ajoutez une deuxième condition `if` pour colorier un point en `lime` si `x < -100`.
```

```{codeplay}
from turtle import *
from random import *

w, h = 300, 200
d, n = 10, 100
up()
speed(0)

for i in range(n):
    x, y = randint(-w, w), randint(-h, h)
    goto(x, y)
    if x > 100:
        dot(2*d, 'red')
    dot(d)
```

## La structure `if else`

La structure `if else` ci-dessous permet d'exécuter une **action_1** seulement si une **condition** est vraie et une **action_2** autrement

``` python
if condition:
    action_1
else:
    action_2
```

Dans l'exemple ci-dessous la condition de test est `y > 0`. 
Si cette condition est vraie, le point est colorié en rouge, autrement en bleu.

```{codeplay}
from turtle import *
from random import *

w, h = 300, 200
d, n = 20, 300
up()
speed(0)

for i in range(n):
    x, y = randint(-w, w), randint(-h, h)
    goto(x, y)
    if y > 0:
        dot(d, 'red')
    else:
        dot(d, 'blue')
```

## L'opération `and`

L'opération logique `and` permet de connecter deux conditions.
Les deux conditions doivent être vraies pour que l'expression soit vraie.

Pour accélérer le dessin, nous désactivons l'animation avec `tracer(0)`.
Pour afficher le résultat, nous devons alors appeler la fonction `update()` à la fin.

```{exercise}
Modifiez le code pour que les points aient une couleur différente dans chaque quadrant.
```

```{codeplay}
from turtle import *
from random import *

w, h = 280, 180
d, n = 10, 2000
tracer(0)
up()

for i in range(n):
    x, y = randint(-w, w), randint(-h, h)
    goto(x, y)
    if x > 0 and y > 0:
        dot(d, 'red')
    else:
        dot(d, 'blue')
update()
```

## Région en diagonale

```{exercise}
Modifiez le code pour que les points aient 4 couleurs, divisées par les 2 diagonales.
```

```{codeplay}
from turtle import *
from random import *

w, h = 280, 180
d, n = 10, 1000
tracer(0)
up()

for i in range(n):
    x, y = randint(-w, w), randint(-h, h)
    goto(x, y)
    if x > y:
        dot(d, 'red')
    else:
        dot(d, 'blue')
update()
```

## Dans un cercle

Un cercle est défi par une distance donnée d'un point. 
Le cercle autour de l'origine avec un rayon r est donné par la formule

$ x^2 + y^2 = r^2 $

Cette formule nous permet de décider si un point aléatoire est à l'intérieur ou à l'extérieur d'un cercle.

```{codeplay}
from turtle import *
from random import *

w, h = 280, 180
d, n = 10, 2000
tracer(0)
up()

for i in range(n):
    x, y = randint(-w, w), randint(-h, h)
    goto(x, y)
    if (x**2 + y**2) > 150**2 :
        dot(d, 'red')
    else:
        dot(d, 'blue')
update()
```

La fonction `in_circle(p, q, r)` vérifie si le point `p` se trouve
à l'intérieur d'un cercle de rayon `r` qui se trouve à la position `q`.

```{exercise}
Ajoutez un deuxième cercle avec un rayon r=100, colorié en rouge, qui se trouve à la position (100, -50).
```

```{codeplay}
from turtle import *
from random import *

w, h = 280, 180
d, n = 10, 2000
tracer(0)
up()

def in_circle(p, q, r):
    d = (p[0]-q[0])**2 + (p[1]-q[1])**2
    return d < r**2
    
for i in range(n):
    p = randint(-w, w), randint(-h, h)
    goto(p)
    if in_circle(p, (-100, 50), 80):
        dot(d, 'lime')
    else:
        dot(d, 'blue')
update()
```

## Diagramme de Venne

Avec les 3 opérateurs logiques:

- `and`
- `or`
- `not` 

nous pouvons trouver des expressions pour trouver les points qui se trouvent dans l'intersection (`and`) ou dans l'union (`or`) de deux cercles.

```{exercise}
Modifiez le code pour que les points appartenant à l'intersection des deux cercles soient dessinés en jaune.
```

```{codeplay}
from turtle import *
from random import *

w, h = 280, 180
d, n = 10, 2000
tracer(0)
up()
r, q, q2 = 120, (-60, 0), (60, 0)

def in_circle(p, q, r):
    d = (p[0]-q[0])**2 + (p[1]-q[1])**2
    return d < r**2
    
for i in range(n):
    p = randint(-w, w), randint(-h, h)
    goto(p)
    if in_circle(p, q, r) and not in_circle(p, q2, r):
        dot(d, 'lime')
    elif in_circle(p, q2, r):
        dot(d, 'red')
    else:
        dot(d, 'blue')
update()
```

## Dans un rectangle

Dans des programmes interactifs, on doit souvent déterminer si un clic de la souris (x, y) a eu lieu à l'intérieur d'un bouton, qui est normalement une région rectangulaire.

Pour tester si la valeur $x$ se trouve dans l'intervalle $[x_0, x_1]$ nous devons faire deux comparaisons.

Python permet de remplacer `(x0 < x) and (x < x1)` par l'expression plus compacte `x0 < x < x1`.

```{codeplay}
x0, x1 = 5, 10
x = 8

if x0 < x < x1:
    print(x, "est entre", x0, 'et', x1)
else:
    print(x, "n'est entre", x0, 'et', x1)
```

La fonction `in_rect(p, x0, x1, y0, y1)` détermine si la position du point `p` est à l'intérieur du rectangle indiqué par les coordonnées `x0, x1, y0, y1`.

```{exercise}
Ajoutez un deuxième rectangle ou les points ont une autre couleur.
```

```{codeplay}
from turtle import *
from random import *

w, h = 280, 180
d, n = 10, 2000
tracer(0)
up()

def in_rect(p, x0, x1, y0, y1):
    return x0 < p[0] < x1 and y0 < p[1] < y1 
    
for i in range(n):
    p = randint(-w, w), randint(-h, h)
    goto(p)
    if in_rect(p, 50, 220, -50, 100):
        dot(d, 'lime')
    else:
        dot(d, 'blue')

update()
```

## À gauche d'une droite

La fonction `is_left(p, q, q2)` est vraie si le point `p` se trouve à gauche de la droite définie par les deux points (q, q2).

```{codeplay}
from turtle import *
from random import *

w, h = 280, 180
d, n = 10, 2000
tracer(0)
up()
q, q2 = (-160, -100), (60, 0)

def is_left(p, q, q2):
    return (p[0]-q[0])*(q2[1]-q[1]) - (p[1]-q[1])*(q2[0]-q[0]) < 0
    
for i in range(n):
    p = randint(-w, w), randint(-h, h)
    goto(p)
    if is_left(p, q, q2):
        dot(d, 'lime')
    else:
        dot(d, 'blue')

for p in (q, q2): 
    goto(p)
    dot(3*d, 'red')

update()
```

La fonction `in_poly(p, poly)` est vraie si le point `p` se trouve à l'intérieur d'un polygone convexe dont les points sont dans l'ordre du sens de l'horloge.

```{codeplay}
from turtle import *
from random import *

w, h = 280, 180
d, n = 10, 2000
tracer(0)
up()

poly = ((-160, -100), (100, 100), (60, -100))
    
def is_left(p, q, q2):
    return (p[0]-q[0])*(q2[1]-q[1]) - (p[1]-q[1])*(q2[0]-q[0]) < 0
    
def in_poly(p, poly):
    n = len(poly)
    for i in range(n):
        q = poly[i]
        q2 = poly[(i+1)%n]
        if is_left(p, q, q2):
            return False
    return True
    
for i in range(n):
    p = randint(-w, w), randint(-h, h)
    goto(p)
    if in_poly(p, poly):
        dot(d, 'lime')
    else:
        dot(d, 'blue')

for p in poly:
    goto(p)
    dot(3*d, 'red')
    
update()
```
