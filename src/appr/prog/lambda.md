# Formaliser - `lambda`

Dans ce chapitre nous découvrons la fonction `lambda`. C'est une façon de créer une fonction anonyme (sans nom). Une fonction lambda est composée d'un certain nombre de variables, suivi d'une expression qui utilise ces variables. Nous allons voir que :

- le mot-clé `lambda` permet de définir une fonction anonyme,
- l'expression `lambda x : expression` produit une fonction,
- la fonction `lambda` peut comporter zéro ou plusieurs variables.

```{question}
En Python `lambda` est

{v}`un mot-clé`  
{f}`une fonction`  
{f}`une expression`  
{f}`une variable`
```

## Fonction lambda

Parfois nous avons besoin d'une petite fonction, sans que ça vaille la peine de la définir de façon explicite avec le mot clé `def` et un nom de fonction.

```{codeplay}
:file: lambda1.py
def cube(x):
    return x ** 3

print(cube)
print(cube(2))
print(cube(5))
```

Parfois nous avons juste besoin d'une fonction anonyme (sans nom). Une telle fonction s'appelle une fonction **lambda**. Voici le même exemple cette fois avec une fonction anonyme.

```{codeplay}
:file: lambda2.py
print((lambda x : x ** 3)(2))
print((lambda x : x ** 3)(5))
```

La fonction **lambda** en tant qu'objet, peut être affectée à une variable.

```{codeplay}
:file: lambda3.py
f = lambda x : x ** 3

print(f)
print(f(2))
print(f(5))
```

## Visualiser

L'utilisation principale de la fonction lambda est pour les fonctions qui demandent comme argument une fonction.

Jusqu'à maintenant les arguments de nos fonctions étaient des valeurs tels que: nombres, angles, distances, couleurs.

Avoir une fonction comme argument est nouveau. Pour montrer ce nouveau principe, nous allons définir la fonction `tracer()`. Elle prend comme argument une fonction `f` qu'elle va évaluer dans un intervalle [-300, 300].

```{codeplay}
:file: lambda4.py
from turtle import *
up()

def tracer(f, col='red'):
    color(col)
    for x in range(-300, 300, 10):
        goto(x, f(x))
        down()
    up()

tracer(lambda x : 0)                # fonction constante
tracer(lambda x : x, 'blue')        # fonction identité
tracer(lambda x : 0.5 * x, 'lime')  # fonction linéaire
```

## Exemples de fonctions

Voici encore 3 exemples de fonctions

- la fonction `abs()` renvoie la valeur absolue
- la fonction constante renvoie la valeur 100 partout
- la fonction modulo renvoie une trace en dent de scie

```{codeplay}
:file: lambda5.py
from turtle import *
up()

def tracer(f, col='red'):
    color(col)
    for x in range(-300, 300, 10):
        goto(x, f(x))
        down()
    up()

tracer(abs)                         # fonction valeur absolue
tracer(lambda x : 100, 'blue')      # fonction constante
tracer(lambda x : x % 50, 'lime')   # fonction modulo
```

## Fonction quadratique

La fonction `tracer()` permet de tracer une fonction `f()` dans un intervalle [-300, 300]. Nous traçons deux équations quadratiques.

```{codeplay}
:file: lambda6.py
from turtle import *
speed(0)
up()

def tracer(f, col='red'):
    color(col)
    for x in range(-300, 300, 10):
        goto(x, f(x))
        down()
    up()

tracer(lambda x : -0.01 * x ** 2)
tracer(lambda x : 0.005 * x ** 2 - x - 100, 'blue')
```

## La fonction de rappel

Revenons vers notre tout premier programme avec la fonction `onkey()`. Nous voulons faire avancer la tortue quand la touche `a` est appuyée. Nous sommes tentés de simplifier le programme et d'écrire ceci. Essayez-le, mais malheureusement ça ne fonctionne pas.

```{codeplay}
:file: lambda7.py
from turtle import *
shape('turtle')

s = getscreen()
s.onkey(forward(50), 'a')       # erreur
s.listen()
```

C'est ici que la fonction `lambda` est très pratique. Nous pouvons créer une fonction anonyme (sans nom) et la passer comme argument directement dans `onkey()`.

```{exercise}
Faites avancer la tortue avec la touche `a`.
```

```{codeplay}
:file: lambda8.py
from turtle import *
shape('turtle')

s = getscreen()
s.onkey(lambda : forward(50), 'a')
s.listen()
```

## Bouger la tortue

Avec la fonction lambda, notre programme de définition des fonctions de rappel devient beaucoup plus compact. Nous utilisons les fonctions :

- `xcor()` pour lire la position actuelle de la coordonnée `x`.
- `setx(val)` pour assigner une nouvelle valeur à la coordonnée `x`.

Comme cette dernière fonction n'agit pas sur l'orientation de la souris, nous choisissons le disque (`circle`) comme forme pour la tortue.

```{codeplay}
:file: lambda9.py
from turtle import *
shape('circle')
speed(0)
d = 50

s = getscreen()
s.onkey(lambda : setx(xcor() + d), 'Right')
s.onkey(lambda : setx(xcor() - d), 'Left')
s.onkey(lambda : sety(ycor() + d), 'Up')
s.onkey(lambda : sety(ycor() - d), 'Down')
s.listen()
```

## Mettre tout ensemble

Faisons maintenant un programme qui met ensemble tout ce que nous avons vu dans le chapitre précédent dans un seul programme.

```{codeplay}
:file: lambda10.py
from turtle import *
shape('circle')
speed(0)
d = 50

s = getscreen()
s.onkey(lambda : setx(xcor() + d), 'Right')
s.onkey(lambda : setx(xcor() - d), 'Left')
s.onkey(lambda : sety(ycor() + d), 'Up')
s.onkey(lambda : sety(ycor() - d), 'Down')
s.onkey(up, 'u')
s.onkey(down, 'd')
s.onkey(home, 'h')
s.onkey(clear, 'x')
s.onkey(lambda : width(1), '1')
s.onkey(lambda : width(3), '2')
s.onkey(lambda : width(10), '3')
s.onkey(lambda : color('red'), 'r')
s.onkey(lambda : color('lime'), 'v')
s.onkey(lambda : color('blue'), 'b')
s.onkey(lambda : circle(50), 'c')
s.listen()
```

## Écrire un nombre

Nous pouvons utiliser les touches pour écrire dans le canevas de la tortue. Pour avancer la tortue avec chaque lettre, nous choisissons l'option `move=True`.

Il est nécessaire de définir une fonction de rappel pour chaque touche du clavier que nous voulons utiliser.

```{codeplay}
:file: lambda11.py
from turtle import *
s = getscreen()

def ecrire(x):
    write(str(x), font=(None, 50), move=True)

s.onkey(lambda : ecrire(0), '0')
s.onkey(lambda : ecrire(1), '1')
s.onkey(lambda : ecrire(2), '2')
s.onkey(lambda : ecrire(3), '3')
s.onkey(lambda : ecrire(4), '4')
s.onkey(lambda : ecrire(5), '5')
s.onkey(lambda : ecrire(6), '6')
s.onkey(lambda : ecrire(7), '7')
s.onkey(lambda : ecrire(8), '8')
s.onkey(lambda : ecrire(9), '9')
s.onkey(reset, 'r')
s.listen()
```

La fonction lambda nous permet de simplifier aussi la création des fonctions de rappel. Nous pouvons les créer dans une boucle, en parcourant une chaine de caractères auxquels nous voulons associer une fonction de rappel. Nous utilisons ici l'astuce de la valeur par défaut, pour passer un argument à la fonction `f()`.

Ce programme interactif permet d'utiliser les 10 chiffres pour écrire un nombre.

```{codeplay}
from turtle import *
s = getscreen()
speed(0)

def f(x):
    write(x, font=(None, 24), move=True)

for c in '0123456789':
    s.onkey(lambda x=c: f(x), c)
    
s.listen()
done()
```

## Écrire des lettres

Ce programme interactif permet d'utiliser les 26 lettres pour écrire un mot.

```{codeplay}
from turtle import *
s = getscreen()
speed(0)

def f(x):
    write(x, font=(None, 24), move=True)

for c in 'abcdefghijklmnopqrstuvwxyz':
    s.onkey(lambda x=c: f(x), c)
    
s.listen()
done()
```

Le programme suivant permet d'écrire du texte.
Du au limitations de la tortue, nous pouvons écrire seulement les lettres minuscules et l'espace.
Les signes de ponctuation ne sont pas possible.

Deux touches particuler sont disponible:

- `Enter` pour placer le curseur vers une nouvelle ligne
- `Back` pour reculer d'un caractère

```{codeplay}
from turtle import *
s = getscreen()
speed(0)
x, y = -280, 150
d = 24
up()
goto(x, y)

def f(x):
    write(x, font=('Courier', d), move=True)
    
def enter():
    global x, y
    y = y - 1.5 * d
    goto(x, y)

def back():
    setx(xcor() - 0.8 * d)

for c in 'abcdefghijklmnopqrstuvwxyz ':
    s.onkey(lambda x=c: f(x), c)
    
s.onkey(enter, 'Enter')     # touche Enter
s.onkey(back, 'Back')       # touche effacer
s.listen() 
done()
```

## Écrire des couleurs

Ce programme permet d'utiliser les 26 touches de l'alphabet pour écrire des pixels avec des couleurs aléatoires.

```{codeplay}
from turtle import *
from random import *
s = getscreen()
speed(0)

d = 60
goto(-300+d/2, 200-d/2)

def f(x):
    dot(d, (random(), random(), random()))
    if xcor() < 300 - d/2:
        forward(d)
    else:
        goto(-300+d/2, ycor()-d)

for c in 'abcdefghijklmnopqrstuvwxyz':
    s.onkey(lambda x=c: f(x), c)
    
s.listen()
```
