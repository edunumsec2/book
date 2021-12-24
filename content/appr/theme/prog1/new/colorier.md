# Colorier - `color`

Dans ce chapitre nous explorons ce que c'est la couleur.
Une ligne peut être coloriée et une forme peut être rempli d'une couleur.

- la fonction `color()` permet de choisir une couleur.
- une couleur est définie avec trois nombres
- Le système RVB (Rouge Vert Bleu) définit une couleur avec 3 nombres

## Couleur de ligne

La fonction `color()` permet de définir la couleur de ligne.

```{codeplay}
from turtle import *

width(10)
color('red')
forward(150)
left(120)

color('lime')
forward(150)
left(120)

color('blue')
forward(150)
left(120)
```

## Couleur de point

Nous pouvons afficher des points à chaque sommet. La fonction `dot(d)` dessine un disque avec le diamètre `d`.

```{codeplay}
from turtle import *

up()
color('red')
dot(40)

forward(150)
color('lime')
dot(40)

left(120)
forward(150)
color('blue')
dot(40)
```

## Couleur de forme

Avec la fonction `fill_color()` nous pouvons définir une couleur de remplissage d'une forme. Pour remplir une forme avec une couleur, nous devons ajouter les deux fonctions :

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

getscreen().bgcolor('pink')
fillcolor('yellow')

begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()
```

## Forme ouverte

La forme ne doit pas nécessairement être fermée pour être remplie d'une couleur.
Dans l'exemple suivant nous dessinons une forme ouverte avec seulement deux lignes.
Le résultat est un triangle.

```{codeplay}
from turtle import *

getscreen().bgcolor('azure')
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

## Rouge-Vert-Bleu (RVB)

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

## Mode couleur

Il a deux façon d'exprimer les 3 composantes RVB :

- avec un nombre à virgule flottante dans l'intervalle [0, 1]
- avec un entier dans l'intervalle [0, 255]

La fonction `colormode()` retourne le mode actuelle si utilisé sans argument. Si un argument est fourni (1 ou 255), ce mode est activé.

```{codeplay}
from turtle import *
print(colormode())

colormode(255)
print(colormode())
```

## Intensité

Voici un programme qui affiche les intensité pour rouge et vert de 0 à 1.

```{codeplay}
from turtle import *
up()
n = 11

goto(-200, 0)
for i in range(n):
    color((i/(n-1), 0, 0))
    dot(30)
    forward(400/n)
write('rouge', font=(None, 18))

goto(-200, 50)
for i in range(n):
    color((0, i/(n-1), 0))
    dot(30)
    forward(400/n)
write('vert', font=(None, 18)) 
```

**Exercice** : Ajoutez une ligne de points pour la couleur bleue.

## Liste de couleurs

Voici une liste des couleurs disponibles.

![couleurs](media/colors.png)

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

## Erreurs

Il est important de bien comprendre les messages d'erreurs.
Dans cette section vous allez découvrir les différentes catégories d'erreur et les corriger.


### ImportError

Cet erreur est produit si vous essayez d'importer un module qui n'existe pas.

```{codeplay}
from turtl import *

for i in range(3):
    forward(100)
    left(120)
```

**Exercice** : Corrigez l'erreur d'importation.

### SyntaxError

Cet erreur est produit quand vous écrivez mal un mot-clé, ou si vous oubliez une ponctuation. Dans ce cas le mot-clé mal écrit n'est pas reconnu et il n'est pas colorié.

```{codeplay}
fro turtle import *

fore i in range(3)
    forward(100)
    left(120)
```

**Exercice** : Corrigez les 3 erreurs de syntaxe.

### NameError

Cet erreur est produit quand vous écrivez mal le nom d'une variable ou fonction.

```{codeplay}
from turtle import *

for i in range(n):
    forwarde(100)
    lefft(120)
```

**Exercice** : Corrigez les 3 erreurs de nom.

### TypeError

Cet erreur est produit si vous ne mettez pas le nombre d'arguments correcte pour une fonction.

```{codeplay}
from turtle import *

for i in 3:
    forward()
    left(100, 120)
```

**Exercice** : Corrigez les 3 erreurs de type.
