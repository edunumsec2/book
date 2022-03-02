# Parcourir - `tuple`

Dans ce chapitre nous allons découvrir le concept très important de la séquence. Ce concept s'appelle `tuple` en langage Python ou **n-uplet** en français. Une séquence est un groupement d'objets, par exemple de couleurs, de distances ou d'angles. Ce qui est très intéressant c'est que nous pouvons parcourir les valeurs d'une séquence l'une après l'autre. Nous allons voir que :

- la structure `(10, 20, 10)` représente une séquence (`tuple`),
- dans `for x in (10, 20, 10):` la variable `x` parcourt des nombres,
- dans `for x in ('red', 'blue'):` la variable `x` parcourt des couleurs.

```{question}
En informatique un `tuple` est 

{v}`une séquence d'objets`  
{f}`une liste numérique`  
{f}`un ensemble mathématique`  
{f}`une chaîne de caractères`
```

## Parcourir des couleurs

Pour dessiner de multiples couleurs, nous pouvons définir une séquence (tuple) de couleurs et parcourir cette séquence.
En Python une séquence est délimitée par des parenthèses `()` et les éléments sont séparé par une virgule.

Dans l'expression `for x in (...)` la variable `x` va prendre à tour de rôle les valeurs dans la séquence. Dans l'exemple ci-dessous, `x` prendra successivement les valeurs : `'blue'`, `'cyan'`, `'red'`, etc.

```{codeplay}
:file: tuple1.py
from turtle import *
up()

back(200)
for x in ('blue', 'cyan', 'red', 'magenta', 'pink', 'lime'):
    dot(80, x)
    forward(80)
```

**Exercice** : Modifiez la séquence des couleurs.

## Parcourir des diamètres

Nous pouvons également itérer dans une séquence numérique et spécifier le diamètre d'un disque.

```{codeplay}
:file: tuple2.py
from turtle import *
up()

back(220)
for x in (20, 40, 60, 80, 100):
    dot(x, 'red')
    forward(x + 40)
```

**Exercice** : Modifiez la séquence des diamètres.

## Parcourir des distances

Nous allons reprendre nos fonctions `batiment()` et `porte()` et avec l'aide d'une séquence nous pouvons l'écrire de manière bien plus compacte.

```{codeplay}
:file: tuple3.py
from turtle import *

def batiment():
    for x in (200, 100, 200, 100):
        forward(x)
        left(90)

def porte():
    for x in (30, 50, 30, 50):
        forward(x)
        left(90)

porte()
forward(50)
batiment()
```

**Exercice** : Placez la porte à l'intérieur du bâtiment et coloriez-la en rouge.

## Parcourir des angles

Nous allons reprendre nos fonctions `maison()` et avec l'aide d'une séquence nous pouvons l'écrire de manière bien plus compacte. Cette fois-ci la séquence représente des angles, donc nous nommons notre variable `a` pour nous rappeler que c'est un angle.

```{codeplay}
:file: tuple4.py
from turtle import *

def maison():
    forward (70)
    for a in (90, 45, 90, 45):
        left(a)
        forward(50)
    left(90)

back(200)        
maison()
forward(100)
maison()
```

**Exercice** : Ajoutez une porte et une fenêtre à la maison.

## Maisons en couleurs

Dans l'exemple nous allons d'abord parcourir une séquence d'angles avec une variable d'itération `a` pour dessiner une maison.

Ensuite nous allons parcourir une séquence de couleurs avec une variable `c` pour dessiner des maisons en différentes couleurs.

```{codeplay}
:file: tuple5.py
from turtle import *

def maison():
    forward (70)
    for a in (90, 45, 90, 45):
        left(a)
        forward(50)
    left(90)

back(250)
for c in ('red', 'yellow', 'pink', 'lightblue', 'lightgreen'):
    fillcolor(c)
    begin_fill()       
    maison()
    end_fill()
    forward(100)
```

**Exercice** : Changez la couleurs des maisons.

## Drapeau LGBT

Le drapeau arc-en-ciel, ou également appelé le drapeau de la paix, est un drapeau représentant plusieurs bandes ayant les couleurs d'un arc-en-ciel. L'usage du drapeau arc-en-ciel est une ancienne tradition commune à de nombreuses cultures. Il évoque généralement la paix, la diversité sexuelle et de genre, ainsi que l'harmonie entre les individus dans le monde entier.

Aujourd'hui, le drapeau arc-en-ciel est majoritairement connu comme celui de la communauté lesbienne, gay, bisexuelle, transgenre, (abréviation : LGBT), depuis 1978.

```{codeplay}
:file: LGBT.py
from turtle import *

back(300)
left(90)
forward(167)
right(90)
width(67)

for x in ('red', 'orange', 'yellow', 'green', 'blue', 'purple'):
    pencolor(x)
    forward(600)
    back(600)
    right(90)
    forward(67)
    left(90)
```

## Fleur

Ci-dessous nous dessinons 6 fois un losange pour obtenir une fleur.
Avec une boucle `for` nous parcourons une séquence de 6 couleurs alternantes.

```{codeplay}
:file: tuple6.py
from turtle import *
getscreen().bgcolor('lightgreen')

def losange():
    begin_fill()
    for a in (60, 120, 60, 120):
        forward(100)
        left(a)
    end_fill()

for c in ('pink', 'red', 'pink', 'red', 'pink'):
    fillcolor(c)
    losange()
    left(60)
```

**Exercice** : Il manque une pétale, corrigez le programme.

## Sourire

Dans cet exemple nous allons parcourir différentes épaisseurs et nous appelons notre variable `w` (width). Voici quatre smiley avec différentes formes de bouche.

```{codeplay}
:file: tuple7.py
from turtle import *
getscreen().bgcolor('lightgreen')
up()

def smiley():
    dot(100, 'yellow')

    left(45)
    forward(20)
    dot(15)

    right(45)
    back(30)
    dot(15)

    right(90)
    forward(30)
    left(90)
    down()
    forward(30)
    up()

back(200)
for w in (1, 5, 10, 20):
    width(w)
    smiley()
    forward(120)
    left(5)
```

**Exercice** : Faites varier un autre paramètres, par exemple la distance des yeux, ou la taille d'un oeil.

## Etonnement

Cette fois nous faisons varier le diamètre de la bouche.

```{codeplay}
:file: tuple8.py
from turtle import *

getscreen().bgcolor('skyblue')
up()

back(200)
for d in (10, 20, 30, 40):
    dot(100, 'yellow')

    left(45)
    forward(20)
    dot(15)

    right(45)
    back(30)
    dot(15)

    right(60)
    forward(35)
    dot(d)
    left(60)
    
    forward(120)
    left(5)
```

## Une séquence dans une séquence

Il est aussi possible de mettre une séquence dans une séquence, un tuple dans un tuple.
Ceci nous permet par exemple de spécifier dans une séquences deux valeurs : un angle et une couleur `(a, c)`.

```{codeplay}
:file: tuple9.py
from turtle import *

getscreen().bgcolor('skyblue')
up()

dot(40, 'blue')
for (a, c) in ((45, 'pink'), (-10, 'lime'), (-30, 'red'), (-60, 'white')):
    left(a)
    forward(50)
    dot(40, c)
```

**Exercice** : Ajoutez un angle et une couleur supplémentaire.