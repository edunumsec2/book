(prog1.write)=
# Typographier - `write()`

Dans ce chapitre, nous allons voir la **composition typographique** d'un texte dans un contexte graphique. Nous allons découvrir sa taille, sa couleur, sa police et son alignement. Nous allons voir que :

- la fonction `write()` écrit un texte à la position de la tortue,
- l'option `font=(police, taille, style)` permet de choisir son style,
- l'option `align='center'` permet de choisir son alignement.

```{question}
La fonction `write()` écrit un texte dans le canvas de la tortue. Avec des options nous pouvons changer

{v}`la taille`  
{v}`la police`  
{v}`le style`  
{v}`l'alignement`
```

## La fonction `write()`

La fonction `write()` permet d'afficher un texte à la position de la tortue.

```{admonition} Exercice
Déplacez la tortue quelque part et ajoutez un deuxième bout de texte.
```

```{codeplay}
from turtle import *

write('ceci est une phrase écrite par la tortue.')
```

## Taille

La fonction `write()` possède un paramètre optionnel `font` pour indiquer la police, la taille et le style.
La valeur par défaut est `('Arial', 8, 'normal')`

```{admonition} Exercice
Essayez de trouvez la taille maxiumum de texte que vous pouvez écrire.
```

```{codeplay}
from turtle import *

left(90)
forward(120)
for taille in (8, 12, 18, 24, 36, 64):
    backward(1.5 * taille)
    write(taille, font=('Arial', taille))
```

## Police

En typographie, une **police d'écriture** est un ensemble de signes graphiques (caractères) dont le style est coordonné, afin de former un alphabet. Voici quelques polices notoires :

- **Arial** - utilisé sur l'écran
- **Times** - utilisé dans des livres, journaux
- **Courier** - police mono-espace, utilisée pour du code
- **Didot** - police ancienne et élégante
- **Zapfino** - police manuscrite

```{admonition} Exercice
Ecrivez deux lignes de texte en style manuscrit utilsant la police Zapfino.
```

```{codeplay}
from turtle import *

left(90)
forward(150)
for police in ('Arial', 'Times', 'Courier', 'Didot', 'Zapfino'):
    back(60)
    write(police, font=(police, 24))
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
for style in ('normal', 'italic', 'bold', 'bold italic'):
    backward(90)
    write(style, font=('Arial', 48, style))
```

## Alignement

Le paramètre optionnel `align` permet de choisir parmi 3 types d'alignements :

- gauche (`'left'`)
- centre (`'center'`)
- droite (`'right'`)

```{admonition} Exercice
Ecrivez 3-4 lignes de texte en forme de poème qui sont centrées.
```

```{codeplay}
from turtle import *

left(90)
forward(150)
for a in ('left', 'center', 'right'):
    backward(100)
    write(a, font=('Arial', 48), align=a)
```

## Texte en escalier

Le paramètre optionnel `move` permet de choisir si la tortue se déplace à la fin du texte. Par défaut ce paramètre est `False`.
Ce programme place chaque mot en escalier.

```{admonition} Exercice
Que se passe-t-il si vous mettez `move=False` ?
```

```{codeplay}
from turtle import *

mots = ('des', 'mots', 'en', 'escalier')

left(90)
for mot in mots:
    write(mot, font=('Arial', 16), move=True)
    forward(30)
```

## Texte en couleur

```{admonition} Exercice
Ecrivez les lignes sur la même ligne, en utilisant l'option `move=True`.
```

```{codeplay}
from turtle import *

right(90)
back(100)
for couleur in ('red', 'blue', 'lime', 'indigo'):
    color(couleur)
    forward(50)
    write(couleur, font=('Arial', 24, 'bold'))
```

```{caution}
Si vous exécutez `write()` dans ce site avec [Skulpt](https://skulpt.org), la couleur du texte est définie par `fillcolor()`. Quand vous exécutez `write()` dans un éditeur externe avec Python standard, la couleur du texte est définie par `pencolor()`.
```

## Texte aligné

Le texte suivant est une phrase celèbre de *Star Wars*.
Les mots sont alignés à gauche, au centre et à droite.

```{codeplay}
from turtle import *

mots = ('que', 'la', 'force', 'soit', 'avec', 'toi')

goto(-200, 100)
right(90)
for mot in mots:
    write(mot, font=('Arial', 24))
    forward(40)

goto(0, 100)
for mot in mots:
    write(mot, font=('Arial', 24), align='center')
    forward(40) 

goto(200, 100)
for mot in mots:
    write(mot, font=('Arial', 24), align='right')
    forward(40)
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
        write(nombre, font=(None, d), align='center')
    forward(d/2)
    
back(200)
for i in range(10):
    case(i)
```

## Scrabble

Le [Scrabble](https://fr.wikipedia.org/wiki/Scrabble) est un jeu de société et un jeu de lettres où l'objectif est de cumuler des points, sur la base de tirages aléatoires de lettres, en créant des mots sur une grille carrée.
Le jeu a été conçu par l'architecte new-yorkais Alfred Mosher Butts pendant la crise de 1929, et publié en 1931.

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

## WhatsApp

L'application [WhatsApp](https://fr.wikipedia.org/wiki/WhatsApp) fournit un système de messagerie instantanée chiffrée de bout en bout aussi bien via les réseaux de téléphonie mobile que par Internet.

WhatsApp a remporté un grand succès au tournant des années 2010. L'application est créée en 2009 par Jan Koum et Brian Acton, deux anciens employés de la société américaine Yahoo! avec pour objectif de remplacer le SMS. Elle est utilisée par plus de deux milliards de personnes en 2020.

En 2014, WhatsApp est acquis par Facebook pour un montant d'environ 22 milliards soit environ 350 millions de dollars par employé ou 40 dollars par utilisateur.

Dans le programme ci-dessous nous allons afficher une conversation entre deux personnes dans le style d'une application de messagerie. Nous utilisons la fonctions `goto()` pour placer la tortue à une position `(x, y)` et la fonction `setx()` placer la tortune vers la marge gauche (-280) ou droite (280).

```{codeplay}
from turtle import *

lignes = (('Comment-vas tu?', 'Bien'), 
          ('Et toi ?', 'Très bien.'), 
          ('Moi aussi.', 'Super.'))

d = 50
up()
goto(-280, 150)
right(90)

for (texte1, texte2) in lignes:
    setx(-280)
    color('red')
    write(texte1, font=('Arial', d/2))
    forward(d)

    setx(280)
    color('indigo')
    write(texte2, font=('Arial', d/2), align='right')
    forward(d)
```

## Exercice

### Sudoku

Reproduisez l'image ci-dessous

```{image} media/sudoku.png
:width: 200
```

```{codeplay}
:file: sudoku.py
from turtle import *

ligne1 = (5, 3, 0, 0, 7, 0, 0, 0, 0)
ligne2 = (6, 0, 0, 1, 9, 5, 0, 0, 0)
...

d = 30

def case(nombre):
    for i in range(4):
        forward(d)
        left(90)
    forward(d/2)
    if nombre > 0:
        write(nombre, font=(None, d), align='center')
    forward(d/2)

backward(4.5 * d)
for n in ligne1:
    case(n)

```

### WhatsApp

Créez une conversation WhatsApp fictive. D'abord en mode claire, ensuite en mode sombre (dark mode).

```{codeplay}
:file: whatsapp.py
from turtle import *

...
```

### Scrabble

Affichez deux mots qui ont une lettre en commun. Un mot à l'horizontale, le deuxième mot à la verticale.

```{codeplay}
:file: scrabble.py
from turtle import *

...
```

### Nuage de mots-clés

Le [nuage de mots-clés](https://fr.wikipedia.org/wiki/Nuage_de_mots-clés), ou nuage de tags (en anglais **tag cloud**) est une représentation visuelle des mots-clés (tags) très souvent utilisée en web. Généralement, les mots s'affichent dans des tailles et graisses de caractères d'autant plus visibles qu'ils sont utilisés ou populaires.

Choisissez 10 mots et affichez-les avec 10 tailles différentes. La taille la plus grande doit apparaitre au milieu. Les mots ne doivent pas se superposer. Utilisez des tuples avec 10 mots, 10 tailles et 10 positions.

```{codeplay}
:file: nuage_mots.py
from turtle import *

...
```
