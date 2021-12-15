# Colorier

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
Voici une liste des couleurs disponibles.

![couleurs](colors.png)

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

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```