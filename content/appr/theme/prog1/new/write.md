# Typographier - `write`

Dans ce chapitre, nous allons voir la **composition typographique** d'un texte dans un contexte graphique. Nous allons découvrir sa taille, sa couleur, sa police et son alignement. Nous allons voir que :

- la fonction `write()` écrit un texte à la position de la tortue,
- l'option `font=(police, taille, style)` permet de choisir son style,
- l'option `align='center'` permet de choisir son alignement.

```{codeplay}
````

## La fonction `write()`

La fonction `write()` permet d'afficher un texte à la position de la tortue.

```{codeplay}
from turtle import *

write('ceci est une phrase écrit par la tortue.')
```

## Taille

La fonction `write()` possède un paramètres optionnel `font` pour indiquer la police, la taille et le style.
La valeur par defaut est `('Arial', 8, 'normal')`

```{codeplay}
from turtle import *

left(90)
forward(120)
for t in (8, 12, 18, 24, 36, 64):
    backward(1.5 * t)
    write('taille ' + str(t), font=(None, t))
```

## Police

En typographie, une **police d'écriture** est un ensembles de signes graphiques (caractères) dont le style est coordonnée, afin de former un alphabet. Voici quelques polices représentatifs.

- **Arial** - utilisé sur l'écran
- **Times** - utilisé dans des livres, journaux
- **Courier** - police mono-espace, utilisé pour du code
- **Didot** - police ancienne et élégante
- **Zapfino** - police manuscrite

```{codeplay}
from turtle import *

left(90)
forward(150)
for p in ('Arial', 'Times', 'Courier', 'Didot', 'Zapfino'):
    back(60)
    write(p, font=(p, 24))
```

## Style

Le troisième argument présente le style de la police :

- gras (`bold`)
- cursive (`italic`)
- gras et cursive (`bold italic`)

```{codeplay}
from turtle import *

left(90)
forward(180)
for s in ('normal', 'italic', 'bold', 'bold italic'):
    backward(90)
    write(s, font=(None, 48, s))
```

## Alignement

Le paramètre optionnel `align` permet de choisir parmi 3 types d'alignements : 

- gauche (`'left'`)
- centre (`'center'`)
- droite (`'right'`)


```{codeplay}
from turtle import *

left(90)
forward(150)
for a in ('left', 'center', 'right'):
    backward(100)
    write(a, font=(None, 48), align=a)
```

## Texte en escalier

Le paramètre optionnel `move` permet de choisir si la tortue se déplace à la fin du texte. Par défaut ce paramètre est `False`.
Ce programme place chaque mot en escalier.

```{codeplay}
from turtle import *

phrase = 'des mots en escalier'

left(90)
for mot in phrase.split():
    write(mot, font=(None, 16), move=True)
    forward(30)
```

**Exercice** : Changez l'angle de rotation dans `left()`.

## Texte en couleur

```{codeplay}
from turtle import *

right(90)
back(100)
for c in ('red', 'blue', 'lime', 'indigo'):
    color(c)
    forward(50)
    write(c, font=(None, 24, 'bold'))
```

```{caution}
Si vous exécutez `write()` dans ce site avec [Skulpt](https://skulpt.org), la couleur du texte est définie par `fillcolor()`. Quand vous exécutez `write()` dans un éditeur externe avec Python standard, la couleur du texte est défini par `pencolor()`.
```

## Sudoku

Le sudoku est un jeu en forme de grille 9x9. Le but du jeu est de remplir la grille avec une série de chiffres, tous différents, qui ne se trouvent jamais plus d’une fois sur une même ligne, dans une même colonne ou dans une même région 3x3, appelé bloc.

```{codeplay}
:file: sudoku.py
from turtle import *
d = 40
speed(10)

def case(nombre):
    for i in range(4):
        forward(d)
        left(90)
    forward(d/2)
    if nombre > 0:
        left(90)
        up()
        forward(8)
        write(nombre, font=(None, 24), align='center')
        back(8)
        down()
        right(90)
    forward(d/2)
    
back(200)
for i in range(10):
    case(i)
```

## Scrabble

Le [Scrabble](https://fr.wikipedia.org/wiki/Scrabble) est un jeu de société et un jeu de lettres où l'objectif est de cumuler des points, sur la base de tirages aléatoires de lettres, en créant des mots sur une grille carrée.
Le jeu a été conçu par l'architecte new-yorkais Alfred Mosher Butts  pendant la crise de 1929, et publié en 1931.

```{codeplay}
:file: scrabble.py
from turtle import *
d = 40
speed(10)

def case(lettre):
    for i in range(4):
        forward(d)
        left(90)
    forward(d/2)
    up()
    sety(ycor() + 8)
    write(lettre, font=(None, 24), align='center')
    sety(ycor() - 8)
    down()
    forward(d/2)
    
back(200)
for c in 'SCRABBLE':
    case(c)
```

```{codeplay}
```

## Exercice

### Sudoku

Reproduisez l'image ci dessous

```{image} media/sudoku.png
:width: 200
```

```{codeplay}
from turtle import *

ligne1 = (5, 3, 0, 0, 7, 0, 0, 0, 0)
ligne2 = (6, 0, 0, 1, 9, 5, 0, 0, 0)
...
```