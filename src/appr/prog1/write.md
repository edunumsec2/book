# Typographier - `write`

Dans ce chapitre, nous allons voir la **composition typographique** d'un texte dans un contexte graphique. Nous allons découvrir sa taille, sa couleur, sa police et son alignement. Nous allons voir que :

- la fonction `write()` écrit un texte à la position de la tortue,
- l'option `font=(police, taille, style)` permet de choisir son style,
- l'option `align='center'` permet de choisir son alignement.

## La fonction `write()`

La fonction `write()` permet d'afficher un texte à la position de la tortue.

```{codeplay}
from turtle import *

write('ceci est une phrase écrite par la tortue.')
```

## Taille

La fonction `write()` possède un paramètre optionnel `font` pour indiquer la police, la taille et le style.
La valeur par défaut est `('Arial', 8, 'normal')`

```{codeplay}
from turtle import *

left(90)
forward(120)
for t in (8, 12, 18, 24, 36, 64):
    backward(1.5 * t)
    write('taille ' + str(t), font=(None, t))
```

## Police

En typographie, une **police d'écriture** est un ensemble de signes graphiques (caractères) dont le style est coordonné, afin de former un alphabet. Voici quelques polices notoires :

- **Arial** - utilisé sur l'écran
- **Times** - utilisé dans des livres, journaux
- **Courier** - police mono-espace, utilisée pour du code
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
Si vous exécutez `write()` dans ce site avec [Skulpt](https://skulpt.org), la couleur du texte est définie par `fillcolor()`. Quand vous exécutez `write()` dans un éditeur externe avec Python standard, la couleur du texte est définie par `pencolor()`.
```

## Aligner des mots

Le texte suivant est un extrait du *Petit Prince* d'Antoine de Saint-Exupéry. Pour ne pas introduire des retours à la ligne, la phrase est délimitée avec le symbole `\` en fin de ligne.

Les mots sont alignés à gauche, au centre et à droite.

```{codeplay}
from turtle import *

texte = """Les grandes personnes aiment les chiffres. \
Quand vous leur parlez d'un nouvel ami, elles ne vous questionnent \
jamais sur l'essentiel. Elles ne vous disent jamais : \
"Quel est le son de sa voix ? Quels sont les jeux qu'il préfère ?
"""

mots = texte.split(' ')
print('caractères: ', len(texte))
print('mots: ', len(mots))

up()
goto(-200, 180)
for t in mots:
    write(t)
    goto(-200, ycor()-10) 

goto(0, 180)
for t in mots:
    write(t, align='center')
    goto(0, ycor()-10) 

goto(200, 180)
for t in mots:
    write(t, align='right')
    goto(200, ycor()-10) 
```

## Aligner des phrases

Ici, plusieurs mots sont affichés, jusqu'à ce que la position finale dépasse une limite.

Chaque ligne est ajoutée à la liste `lignes`. Cette liste est utilisée pour afficher le texte avec un alignement à droite.

```{codeplay}
from turtle import *

texte = """Les grandes personnes aiment les chiffres. \
Quand vous leur parlez d'un nouvel ami, elles ne vous questionnent \
jamais sur l'essentiel. Elles ne vous disent jamais : \
"Quel est le son de sa voix ? Quels sont les jeux qu'il préfère ? \
Est-ce qu'il collectionne les papillons ?" \
Elles vous demandent : "Quel âge a-t-il ? Combien a-t-il de frères ? \
Combien pèse-t-il ? Combien gagne son père ?"
"""

speed(5)
mots = texte.split(' ')
lignes = []
ligne = ''
up()
goto(-220, 175)
for t in mots:
    write(t + ' ', move=True, font=('Arial', 12))
    ligne += t + ' '
    if xcor() > -100:
        goto(-220, ycor()-20)
        lignes.append(ligne)
        ligne = ''

goto(220, 175)
right(90)
for t in lignes:
    write(t, align='right', font=('Arial', 12))
    forward(20)
```

## Ajuster un texte

Pour ajuster un texte, il faut connaitre la longueur des mots. On ajuste alors les espaces entre les mots, pour faire aligner une ligne de texte des deux côtés.

```{codeplay}
from turtle import *

texte = """Les grandes personnes aiment les chiffres. \
Quand vous leur parlez d'un nouvel ami, elles ne vous questionnent \
jamais sur l'essentiel. Elles ne vous disent jamais : \
"Quel est le son de sa voix ? Quels sont les jeux qu'il préfère ? \
Est-ce qu'il collectionne les papillons ?" \
Elles vous demandent : "Quel âge a-t-il ? Combien a-t-il de frères ? \
Combien pèse-t-il ? Combien gagne son père ?"
"""

longueurs = []
up()
goto(-200, 180)
for t in texte.split(' '):
    x0 = xcor()
    write(t, move=True, font=('Arial', 12))
    x1 = xcor()
    write(' ', move=True, font=('Arial', 12))
    longueurs.append(x1-x0)
    x0 = x1
    if xcor() > -100:
        goto(-200, ycor()-20)

goto(0, 180)
for i in range(len(mots)):
    l = 0
    if 
    while l < 200:
        l += longeurs[0]
for t in texte.split(' '):
    write(' ' + t, move=True, align='right', font=('Arial', 12))
    if xcor() < 100:
        goto(200, ycor()-20)

print(longueurs)
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

Dans le programme ci-dessous nous allons afficher une conversation entre deux personnes dans le style d'une application de messagerie.

```{codeplay}
from turtle import *

texte = """Comment-vas tu?
Bien
Et toi ?
Très bien.
Moi aussi.
Super."""

lignes = texte.split('\n')
d = 50
gauche = True
width(d)
up()
goto(-280, 200-d)

for ligne in lignes:
    if gauche:
        pencolor('lime')
        down()
        write(ligne, font=('Arial', d/2), move=True)
        up()
        write(ligne, font=('Arial', d/2), align='right')
        goto(280, ycor()-d)
    else:
        pencolor('skyblue')
        x0 = xcor()
        write(ligne, font=('Arial', d/2), move=True)
        a = xcor() - x0
        down()
        backward(2 * a)
        up()
        write(ligne, font=('Arial', d/2))
        goto(-280, ycor()-d)
    gauche = not gauche
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
