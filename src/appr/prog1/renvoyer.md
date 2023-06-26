(prog1.renvoyer)=
# Renvoyer - `return`

Dans ce chapitre, nous allons voir comment une fonction peut renvoyer une valeur. Ceci est très important pour pouvoir utiliser une fonction dans une expression mathématique. Nous allons voir que :

- le mot-clé `return` permet de renvoyer une valeur,
- la fonction qui ne renvoie rien renvoie `None`,
- l'expression `return x, y` renvoie un tuple.

```{question}
En informatique, le mot-clé `return` est utilisé pour

{f}`changer de direction`  
{v}`renvoyer une valeur`  
{f}`répéter encore une fois`  
{f}`rentrer au début`
```

## Valeur de retour

L'instruction `return` permet de retourner une valeur.
Le grand intérêt d'une valeur de retour est qu'on peut l'utiliser de nouveau dans des expressions.

Par exemple, nous pouvons créer une expression comme celle-ci : `square(x) + cube(x)`

```{exercise}
Testez le code avec 2, 3 et 4.  
Ajoutez une fonction `identite(x)` qui renvoie juste `x`.  
Ajoutez une ligne qui calcule **identité + carré + cube**.
```

```{codeplay}
:file: return.py
def carre(x):
    return x ** 2

def cube(x):
    return x ** 3

x = input('Entrez un nombre: ')
x = int(x)
print('carré =', carre(x))
print('cube =', cube(x))
print('carré + cube =', carre(x) + cube(x))
```

## Points de sortie

Une fonction peut avoir plusieurs points de sortie. En fait quand une ligne avec `return` est exécutée, toutes les lignes qui suivent ne sont plus exécutées.

La fonction `signe()` possède 3 points de sortie.

```{exercise}
Testez avec -2, 0 et 3.
```

```{codeplay}
:file: return.py
def signe(x):
    if x > 0:
        return 'positif'
    elif x < 0:
        return 'négatif'
    else:
        return 'zéro'

x = int(input('Entrez un nombre: '))
print(x, 'est', signe(x))
```

## Fonction linéaire

En mathématique une fonction linéaire a la forme:

$$ f(x) = a x + b $$

Le paramètre `a` est appelé la pente de cette fonction. C'est l'équation d'une droite.

Nous pouvons définir une telle fonction avec la commande `def f(x):` et le mot-clé `return` qui calcule une expression linéaire avec la variable `x`.

Voici la définition de la fonction et cette fonction appelée avec trois valeurs particuliers: 3, 6, et 9.

```{exercise}
Changez la fonction en $ f(x) = 2x - 3 $. 
```

```{codeplay}
def f(x):
    return 0.5*x + 2

print('f(3) =', f(3))
print('f(6) =', f(6))
print('f(9) =', f(9))
```

## Tracer une fonction

Nous pouvons tracer une fonction `f(x)` comme graphe dans un système de coordonnées.

La fonction `axis()` affiche l'axe x dans une plage de -5 à +5.

- La fonction `stamp()` ajoute une flèche (c'est la forme de la tortue),
- La fonction `write('x')` ajoute l'étiquette de l'axe x.

```{codeplay}
from turtle import *
hideturtle()
d = 50

def axis():
    for x in range(-5, 6):
        goto(x*d, 0)
        dot()
        write(x)
    forward(d/2)    # avance la distance d/2
    stamp()         # ajoute la flèche
    write('x')      # écrit l'étiquette x
    up()

axis()
```

Ensuite nous définissons une fonction `tracer(f, c)` qui permet de tracer une fonction `f` avec une couleur `c`.

L'argument `f` est la fonction à afficher.

```{exercise}
Changez la pente de f en 0.4 et la pente de g en -0.3.  
Définissez une fonction $ h(x) = 0.1 x - 2 $ et affichez-la avec la couleur verte.
```

```{codeplay}
from turtle import *
hideturtle()
d = 50

def axis():
    for x in range(-5, 6):
        goto(x*d, 0)
        dot()
        write(x)
    forward(d/2)
    stamp()
    write('x')
    up()
===
def f(x):
    return 0.5*x + 1

def g(x):
    return -0.5*x + 1
    
def tracer(f, c):
    color(c)
    for x in range(-5, 6):
        goto(x*d, f(x)*d)
        down()
        dot()
        write(round(f(x), 1))
    up()

axis()        
tracer(f, 'red')
tracer(g, 'blue')
```

## Fonction quadratique

En mathématique une fonction quadratique a la forme:

$$ f(x) = a x^2 + b x + c $$

Donc voici deux fonctions quadratiques tracées en rouge et bleu.

```{exercise}
Définissez une troisième fonction `h(x)` et affichez-la avec la couleur verte.
```

```{codeplay}
from turtle import *
hideturtle()
d = 50

def axis():
    for x in range(-5, 6):
        goto(x*d, 0)
        dot()
        write(x)
    forward(d/2)
    stamp()
    write('x')
    up()
===
def f(x):
    return 0.2*x**2 - 2

def g(x):
    return -0.3*x**2 + x + 2
    
def tracer(f, c):
    color(c)
    for x in range(-5, 6):
        goto(x*d, f(x)*d)
        down()
        dot()
        write(round(f(x), 1))
    up()

axis()        
tracer(f, 'red')
tracer(g, 'blue')
```

## Renvoyer des tuples

Dans un tuple avec multiples points, nous pouvons extraire un point particulier en utilisant un indice entre crochets. Nous obtenons :

- le premier point avec l'indice 0
- le dernier point avec l'indice -1

```{codeplay}
points = ((20, 20), (100, -40), (130, 80))

print(points)       # tous les points
print(points[0])    # le premier point
print(points[-1])   # le dernier point
```

La fonction `first(points)` prend comme argument un tuple de points et renvoie seulement le premier point.

```{exercise}
Ajoutez une fonction `last(points)` qui renvoie seulement le dernier point et affichez le résultat.
```

```{codeplay}
points = ((20, 20), (100, -40), (130, 80))

def first(points):
    return points[0]

print('first =', first(points))
```

L'opérateur `+` permet de concaténer le premier point à la fin du tuple `points`.  
Attention de placer le dernier point dans un tuple

```{codeplay}
points = ((20, 20), (100, -40), (130, 80))

print(points + points[0])           # ajoute x et y
print(points + (points[0]))         # parenthèses mathématiques
print(points + (points[0], ))       # parenthèses de tuple, ajoute (x, y)
```

La fonction `polyline(points, c)` affiche le polygone fermé qui est donné par le tuple de coordonnées `points`. 

```{codeplay}
from turtle import *
up()

points = ((20, 20), (100, -40), (130, 80))

def polyline(points, c):
    color(c)
    for p in points + (points[0],):
        goto(p)
        down()
        dot()
    up()

polyline(points, 'red')
```

## Extraire x et y

L'expression `for p in points` parcourt tous les éléments dans `points` et les associe à `p`.
Nous pouvons l'utiliser pour extraire x ou y.

```{codeplay}
points = ((20, 20), (100, -40), (130, 80))

print(tuple(p for p in points))         # le point p entier (x, y)
print(tuple(p[0] for p in points))      # seulement le premier élément (x)
print(tuple(p[1] for p in points))      # seulement le deuxième élément (y)
```

Une autre façon d'obtenir la même chose est:

```{codeplay}
points = ((20, 20), (100, -40), (130, 80))

print(points)
print(tuple(x for (x, y) in points))
print(tuple(y for (x, y) in points))
```

La fonction `xcors(points)` retourne le tuple des coordonnées x des points du polygone défini par `points`.

La fonction `ycors(points)` retourne le tuple des coordonnées y des points du polygone défini par `points`.


```{codeplay}
points = ((20, 20), (100, -40), (130, 80))

def xcors(points):
    return tuple(x for (x, y) in points)

def ycors(points):
    return tuple(y for (x, y) in points)

print(points)
print(xcors(points))
print(ycors(points))
```

## Changer l'échelle

La fonction `scale(points, s)` retourne les points du polygone défini par `points` qui est changé d'échelle par le facteur de taille `s` (size ou scale) qui est définie par un tuple `(dx, dy)`.

```{exercise}
Ajoutez un point supplémentaire au polygone pour en faire un rectangle.  
En plus, changez l'échelle du polygone d'un facteur (4, 1) et affichez-le avec la couleur verte.
```

```{codeplay}
from turtle import *
dot()
up()

points = ((-20, -20), (50, -40), (30, 80))

def polyline(points, c):
    color(c)
    for p in points + (points[0],):
        goto(p)
        down()
        dot()
    up()

def scale(points, s):
    return tuple((x * s[0], y * s[1]) for (x, y) in points)

polyline(points, 'red')
polyline(scale(points, (2, 2)), 'blue')
```

## Changer la position

La fonction `place(points, p)` retourne les points du polygone défini par `points` qui est déplacé par le vecteur de position `p`.

```{exercise}
Ajoutez un point supplémentaire au polygone pour en faire un rectangle.  
Changez la position du polygone d'un vecteur (-200, 100) et affichez-le avec la couleur verte.
```

```{codeplay}
from turtle import *
dot()
up()

points = ((-20, -20), (50, -40), (30, 50))

def polyline(points, c):
    color(c)
    for p in points + (points[0],):
        goto(p)
        down()
        dot()
    up()

def place(points, p):
    return tuple((x+p[0], y+p[1]) for (x, y) in points)

polyline(points, 'red')
polyline(place(points, (-100, 0)), 'blue')
```

## Centre du polygone

La fonction `center(points)` retourne le point qui est au centre du polygone défini par `points`.

Le centre est calculé en prenant la valeur moyenne des coordonnées x et la valeur moyenne des coordonnées y.

```{codeplay}
from turtle import *
up()

poly1 = ((-20, -20), (50, -40), (30, 50))
poly2 = ((-120, -120), (-250, -40), (-130, 50))

def polyline(points, c):
    color(c)
    for p in points + (points[0],):
        goto(p)
        down()
        dot()
    up()

def center(points):
    n = len(points)
    xc = sum(tuple(x for (x, y) in points))/n
    yc = sum(tuple(y for (x, y) in points))/n
    return (xc, yc)

polyline(poly1, 'red')
goto(center(poly1))
dot()

polyline(poly2, 'blue')
goto(center(poly2))
dot()
```

## Rectangle du polygone

La fonction `box(points)` retourne les 4 points du rectangle qui entoure le polygone défini par `points`.

```{exercise}
Ajoutez 1-2 points supplémentaire aux deux polygones.  
Vérifiez que la boite s'adapte pour toujours entourer exactement les points.
```

```{codeplay}
from turtle import *
up()

poly1 = ((-20, -20), (50, -40), (30, 50))
poly2 = ((-120, -120), (-250, -40), (-130, 50))

def polyline(points, c):
    color(c)
    for p in points + (points[0],):
        goto(p)
        down()
        dot()
    up()

def box(points):
    x0 = min(tuple(x for (x, y) in points))
    x1 = max(tuple(x for (x, y) in points))
    y0 = min(tuple(y for (x, y) in points))
    y1 = max(tuple(y for (x, y) in points))
    return ((x0, y0), (x1, y0), (x1, y1), (x0, y1)) 

polyline(poly1, 'red')
polyline(box(poly1), 'blue')

polyline(poly2, 'red')
polyline(box(poly2), 'blue')
```
