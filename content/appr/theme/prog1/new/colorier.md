# Colorier - `color`

Dans ce chapitre nous continuons à dessiner et nous introduisons la couleur.
Une couleur peut être appliquée à une ligne, à un point, à une forme ou à l'arrière-fond. Nous allons voir que

- la fonction `color()` permet de choisir une couleur,
- la fonction `dot(d)` dessine un disque de diamètre `d`,
- la structure `['red', 'pink']` représente une liste.

## Liste de couleurs

Voici une liste des couleurs disponibles. Pour les utiliser vous devez les écrire entre des apostrophes, comme par exemple `'pink'` ou `'hotpink'`.

![couleurs](media/colors.png)

## Couleur de ligne

La fonction `color()` permet de définir la couleur de ligne.
Entre les parenthèses de la fonction vous devez écrire le nom d'une couleur, entouré d'apostrophes, par exemple `color('red')` pour dessiner une ligne rouge.

Voici un triangle avec 3 segments de couleurs différentes.

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

**Exercice** : Modifiez les 3 couleurs en vous inspirant de la liste.

## Couleur de point

Nous pouvons afficher des points à chaque sommet :

- la fonction `dot()` dessine un point standard,
- la fonction `dot(d)` dessine un disque d'un diamètre `d`,
- la fonction `dot(d, couleur)` dessine un disque dans la couleur spécifiée.

```{codeplay}
from turtle import *
up()

dot(40, 'red')
forward(150)

dot(60, 'lime')
left(120)
forward(150)

dot(80, 'blue')
```

**Exercice** : Modifiez la taille et la couleurs des 3 points.

## Couleur de forme

Avec la fonction `fillcolor()` nous pouvons définir une couleur de remplissage de forme. Pour remplir une forme avec une couleur, nous devons ajouter les deux fonctions :

- `begin_fill()` au début de la forme,
- `end_fill()` à la fin de la forme.

Par exemple ce programme-ci dessine un carré jaune.

```{codeplay}
from turtle import *

fillcolor('yellow')
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()
```

**Exercice** : Ajoutez un triangle d'une couleur différente.

## Couleur d'arrière-fond

Le fonction `getscreen()` retourne un objet `Screen`. Cet objet possède une méthode `bgcolor()`.
Tout ce qu'il faut retenir en ce moment c'est que la combinaison `getscreen().bgcolor()` permet de définir la couleur d'arrière-fond (bg = background).

Dans l'exemple suivant, nous dessinons un carré jaune sur un arrière-fond rose.

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
Le résultat est un triangle avec deux bordures et un troisième segment sans bordure.

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

**Exercice** : Dessinez un drapeau bi-colore.

## Smiley

Avec des cercles `dot(d)` de taille différentes nous pouvons dessiner un smiley.
Voici un smiley qui exprime l'indifférence.

```{codeplay}
from turtle import *

getscreen().bgcolor('linen')
up()
dot(300, 'yellow')

color('black')
goto(50, 40)
dot(40)
goto(-50, 40)
dot(40)

goto(-50, -50)
width(10)
down()
forward(100)
```

Voici un autre smiley qui exprime la surprise.

```{codeplay}
from turtle import *

getscreen().bgcolor('linen')
up()
dot(300, 'yellow')

color('black')
goto(50, 40)
dot(40)
goto(-50, 40)
dot(40)

goto(0, -50)
dot(80)
```

**Exercice** : Dessinez encore un autre smiley.

## Itérer dans un séquence

Pour dessiner multiples couleurs, nous pouvons définir une séquence (tuple) de couleurs et itérer sur cette séquence.
En Python une séquence est délimitée par des parenthèses `()` et les éléments sont séparé par une virgule.

Dans l'expression `for x in (...)` la variable `x` va prendre à tour de rôle les valeurs dans la séquence. Dans l'exemple ci-dessous, `x` prendra successivement les valeurs : `'blue'`, `'cyan'`, `'red'`, etc.

```{codeplay}
from turtle import *
up()

back(200)
for x in ('blue', 'cyan', 'red', 'magenta', 'pink', 'lime'):
    dot(80, x)
    forward(80)
```

**Exercice** : Modifiez la séquence des couleurs.

Nous pouvons également itérer dans une séquence numérique et spécifier l'épaisseur.

```{codeplay}
from turtle import *
up()

back(220)
for x in (20, 40, 60, 80, 100):
    dot(x, 'red')
    forward(x + 40)
```

**Exercice** : Modifiez la séquence des diamètres.

## Dessiner une croix

La fonction `boite()` dessine les 3 cotés d'un carré.
Répété 4 fois, ceci donne la forme d'une croix.

```{codeplay}
from turtle import *

getscreen().bgcolor('red')

def boite():
    forward(60)
    left(90)
    forward(60)
    left(90)
    forward(60)
    right(90)
    
fillcolor('white')
begin_fill()
boite()
boite()
boite()
boite()
end_fill()
```

**Exercice** : Faites ce programme plus court en utilisant une boucle.

## Dessiner une maison

Nous reprenons l'exemple du chapitre précédent et ajoutons de la couleur pour dessiner des maisons jaunes avec un toit rouge.

```{codeplay}
from turtle import *

getscreen().bgcolor('lightgreen')
up()

def carre():
    fillcolor('yellow')
    begin_fill()
    for i in range(4):
        forward(100)
        right(90)
    end_fill()
        
def triangle():
    fillcolor('red')
    begin_fill()
    for i in range(3):
        forward(100)
        left(120)
    end_fill()
    
def maison():
    down()
    carre()
    triangle()
    up()
    
back(200)
for i in range(3):
    maison()
    forward(150)
```

## Dessiner une fleur

Ci-dessous nous dessinons un losange 6 fois pour obtenir une fleur.
Avec une boucle `for` nous alternons entre deux couleurs de pétale.

```{codeplay}
from turtle import *

getscreen().bgcolor('azure')

def losange():
    begin_fill()
    for i in range(2):
        forward(100)
        left(60)
        forward(100)
        left(120)
    end_fill()

for i in range(3):
    for x in ['pink', 'hotpink']:
        fillcolor(x)
        losange()
        left(60)
```

**Exercice** : Changez le nombre de pétales.

## Erreurs

Il est important de bien comprendre les messages d'erreurs.
Dans cette section vous allez découvrir les différentes catégories d'erreur et comment les corriger.

### ImportError

Cette erreur est produite si vous essayez d'importer un module qui n'existe pas.

```{codeplay}
from turtl import *

for i in range(3):
    forward(100)
    left(120)
```

**Exercice** : Corrigez l'erreur d'importation.

### SyntaxError

Cette erreur est produite quand vous écrivez mal un mot-clé, ou si vous oubliez une ponctuation. Dans ce cas le mot-clé mal écrit n'est pas reconnu et il n'est pas colorié.

```{codeplay}
fro turtle import *

fore i in range(3)
    forward(100)
    left(120)
```

**Exercice** : Corrigez les 3 erreurs de syntaxe.

### NameError

Cette erreur est produite quand vous écrivez mal le nom d'une variable ou fonction.

```{codeplay}
from turtle import *

for i in range(n):
    forwarde(100)
    lefft(120)
```

**Exercice** : Corrigez les 3 erreurs de nom.

### TypeError

Cette erreur est produite si vous ne mettez pas le nombre d'arguments correcte pour une fonction.

```{codeplay}
from turtle import *

for i in 3:
    forward()
    left(100, 120)
```

**Exercice** : Corrigez les 3 erreurs de type.

## Exercices

Dans tous les exercices suivants commencez par définir une couleur d'arrière-fond appropriée.

1. Dessinez et coloriez un sapin de Noël. Définissez des fonctions pour des boules et des étoiles.
1. Dessinez et coloriez une ville. Définissez des fonctions pour des maisons et des immeubles.
1. Dessinez et coloriez un paysage. Définissez des fonctions pour des montagnes et des sapins.
1. Dessinez et coloriez un jardin. Définissez des fonctions pour les feuilles, les pétales et les fleurs.
1. Dessinez et coloriez un aquarium. Définissez des fonctions pour les poissons, l'herbe, et les bulles.