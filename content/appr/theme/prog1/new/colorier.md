# Colorier

Dans ce chapitre nous explorons ce que c'est la couleur. 
Les lignes peuvent être colorié et les formes être remplis de couleurs.

- une couleur est défin avec trois nombres
- Le système RVB (Rouge Vert Bleu) définit les couleurs de base

Mais avant de passer aux couleurs, nous allons voir l'épaisseur de ligne.

## Epaisseur de ligne

La fonction `width()` permet de définir l'épaisseur de ligne. 
Les deux extrémités de ligne sont arrondies.

Pour démontrer différents épaisseurs, nous allons itérer sur une liste des épaisseurs.

Ici nous utilisons 3 nouvelles fonctions:

- `write(d)` affiche d à la position actuelle
- `setpos(x, y)`définit une nouvelle position de tortue
- `xcor()` retourne la coordonnée x

```{codeplay}
from turtle import *

up()
back(100)
left(90)

for d in [1, 2, 5, 10, 20, 30]: 
    width(d)
    write(d)
    forward(30)
    down()
    forward(100)
    up()
    setpos(xcor() + 50, 0)
```

## Couleur de ligne

La fonction `color()` déinit deux couleurs:
- la couleur de ligne
- la couleur de remplissage (intérieur de la tortue)


```{codeplay}
from turtle import *
shape('turtle')

color('red', 'yellow')
forward(150)

print(pencolor())
print(fillcolor())
print(color())
```

Les 3 fonctions permettent de définir ou lire les couleurs :

- `pencolor()` retourne la couleur du stylo
- `fillcolor()` retourne la couleur de remplissage
- `color()` retourne un tuple avec les deux couleurs


## Couleur de remplissage

Avec la fonction `fill_color()` nous pouvons définir une couleur de remplissage.
Pour remplir une forme avec une couleur, nous devons ajouter les deux fonctions :

- `begin_fill()` au début de la forme,
- `end_fill()` à la fin de la forme.

```{codeplay}
from turtle import *

fillcolor('yellow')
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()
```

## Couleur d'arrière-fond

Le fonction `getscreen()` retourne un objet `Screen`. Celui ci possède une méthode `bgcolor()`.
L'objet qui appelle sa méthode permet de changer la couleur de l'arrière-fond.

Dans l'exemple suivant, nous commençons avec un fond limette et changeons en pink une fois le carré dessiné.


```{codeplay}
from turtle import *

getscreen().bgcolor('lime')
fillcolor('yellow')

begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()

getscreen().bgcolor('pink')
```

## Forme ouverte

La forme ne doit pas nécessairement être fermée pour être remplie d'une couleur.
Dans l'exemple suivant nous dessinons une forme ouverte avec seulement deux lignes.
Le résultat est un triangle.

```{codeplay}
from turtle import *

fillcolor('yellow')
begin_fill()
for i in range(2):
    forward(100)
    left(90)
end_fill()

fillcolor('lime')
begin_fill()
for i in range(2):
    forward(100)
    left(90)
end_fill()
```

**Exercice** : Dessiner un drapeau bi-colore.

## Dessiner un pixel

Comme avant nous allons définir une fonction `square()`.
Cette fois elle a deux arguments :
- `a` pour la taille du carré,
- `color` pour la couleur du carré.

```{codeplay}
from turtle import *

def square(a, color):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(a)
        left(90)
    end_fill()
    forward(a)

back(100)
square(100, 'yellow')
square(100, 'orange')
square(100, 'red')
```

## Rouge-Vert-Bleu (RGB)

Dans un ordinateur les couleurs sont exprimé par un triplet de nombres.
Ces nombres indiquent l'intensité des trois couleurs de base : rouge-vert-bleu (RVB)

L'intensité de couleur est exprimé soit :

- en virgule flottante sur dans une plage de 0.0 ... 1.0
- en entiers sur une plage de 0 ... 255

En utilisant la définition précédente nous pouvons exprimer les couleurs aussi avec un triplet.

```{codeplay}
from turtle import *

def square(a, color):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(a)
        left(90)
    end_fill()
    forward(a)
===
back(200)
square(50, (0, 0, 0))   # black
square(50, (1, 0, 0))   # red
square(50, (0, 1, 0))   # green
square(50, (0, 0, 1))   # blue
square(50, (1, 1, 0))   # yellow
square(50, (0, 1, 1))   # cyan
square(50, (1, 0, 1))   # magenta
square(50, (1, 1, 1))   # white
```

## Liste de couleurs

Voici une liste des couleurs disponibles.

![couleurs](colors.png)

```{codeplay}
from turtle import *

color = input('Enter a color: ')
while color:
    getscreen().bgcolor(color)
    color = input('Enter a color: ')
```

## Itérer dans un liste

Pour dessiner de multiples couleurs, nous pouvons définir une liste de couleurs et itérer sur cette liste.

```{codeplay}
from turtle import *

def square(a, color):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(a)
        left(90)
    end_fill()
    forward(a)

colors = ['blue', 'cyan', 'red', 'magenta', 'pink', 'lime', 'yellow']

back(200)
for color in colors:
    square(50, color)
```

## Couleur interactive

Nous pouvons aussi utiliser une entrée interactive avec la fonction `input()`
et demander à l'utilisateur d'entrer une couleur valide.

```{codeplay}
from turtle import *

def square(a, color):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(a)
        left(90)
    end_fill()
    forward(a)

back(200)
color = input('Enter a color: ')
while color:
    square(100, color)
    color = input('Enter a color: ')
```

## Dessiner Pikachu

De nouveaux nous définissons une fonction `line()` pour dessiner une liste de couleurs.
En fin de liste, la tortue est placée à la position prête pour dessiner la ligne suivante.

```{codeplay}
from turtle import *

def square(a, color):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(a)
        left(90)
    end_fill()
    forward(a)

a = 50

def line(colors):
    for color in colors:
        square(a, color)
    back(len(colors) * a)
    up()
    sety(ycor() - a)
    down()

back(2 * a)
line(['black', 'yellow', 'yellow', 'black'])
line(['white', 'red', 'yellow', 'white'])
line(['yellow', 'yellow', 'yellow', 'yellow'])
line(['yellow', 'yellow', 'yellow', 'white'])
```

**Exercice** : Dessinez un autre Pokemon.

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```