# Colorier - `color`

Dans ce chapitre nous continuons à dessiner et nous introduisons la couleur.
Une couleur peut être appliquée à une ligne, à un point, à une forme ou à l'arrière-fond. Nous allons voir que

- la fonction `color()` permet de choisir une couleur,
- la fonction `dot(d)` dessine un disque de diamètre `d`,
- la fonction `begin_fill()/end_fill()` permet le remplissage.

## Liste de couleurs

Voici une liste des couleurs disponibles. Pour les utiliser vous devez les écrire entre des apostrophes, comme par exemple `'pink'` ou `'hotpink'`.

![couleurs](media/colors.png)

## Couleur de ligne

La fonction `color()` permet de définir la couleur de ligne.
Entre les parenthèses de la fonction vous devez écrire le nom d'une couleur, entouré d'apostrophes, par exemple `color('red')` pour dessiner une ligne rouge.

Voici un triangle avec 3 segments de couleurs différentes.

```{codeplay}
from turtle import *
width(20)

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

dot(300, 'red')
forward(150)

dot(160, 'lime')
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

def triangle():
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)

fillcolor('chartreuse')
begin_fill()
triangle()
end_fill()
```

**Exercice** : Ajoutez un triangle d'une couleur différente.

## Couleur de fond

Le fonction `getscreen()` retourne un objet `Screen`. Cet objet possède une méthode `bgcolor()`.
Tout ce qu'il faut retenir pour l'instant c'est que la combinaison `getscreen().bgcolor()` permet de définir la couleur d'arrière-fond (bg = background).

Dans l'exemple suivant, nous dessinons un carré jaune sur un arrière-fond rose.

```{codeplay}
from turtle import *

def triangle():
    forward(150)
    left(120)
    forward(150)
    left(120)
    forward(150)
    left(120)

getscreen().bgcolor('tan')
fillcolor('gold')

begin_fill()
triangle()
end_fill()
```

## Forme ouverte

La forme ne doit pas nécessairement être fermée pour être remplie d'une couleur.
Dans l'exemple suivant nous dessinons une forme ouverte avec seulement deux lignes.
Le résultat est un triangle avec deux bordures et un troisième segment sans bordure.

Une équerre est un instrument formé de deux pièces ajustées à angle droit. l'équerre est utilisée soit pour vérifier des angles dièdres droits, soit pour tracer des angles plans droits.

```{codeplay}
from turtle import *
getscreen().bgcolor('moccasin')

def equerre():
    forward(150)
    left(90)
    forward(100)
    left(90)

fillcolor('sienna')
begin_fill()
equerre()
end_fill()

up()
forward(50)
down()

fillcolor('gold')
begin_fill()
equerre()
end_fill()
```

**Exercice** : Dessinez le drapeau bi-colore du canton de Zurich.

## Smiley

Avec des cercles `dot(d)` de tailles différentes nous pouvons dessiner un smiley.
Voici un smiley qui exprime l'indifférence.

```{codeplay}
from turtle import *
getscreen().bgcolor('linen')
dot(300, 'yellow')

left(45)
forward(60)
dot(40)

right(45)
back(100)
dot(40)

right(90)
forward(100)
left(90)
width(20)
forward(100)
```

**Exercice** : Ajoutez `up()` au début du programme pour ne plus montrer la trajectoire de la tortue.

Voici un autre smiley qui exprime la surprise.

```{codeplay}
from turtle import *

getscreen().bgcolor('azure')
dot(300, 'palegreen')

left(45)
forward(60)
dot(40)

right(45)
back(90)
dot(40)

right(60)
forward(100)
dot(80)
```

**Exercice** : Dessinez encore un autre smiley.

## Croix

La fonction `boite()` dessine les 3 côtés d'un carré.
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

def croix():
    boite()
    boite()
    boite()
    boite()
    
fillcolor('white')
begin_fill()
croix()
end_fill()
```

**Exercice** : Inversez les couleurs pour trouver le drapeau de la Croix-Rouge.

## Maison

Nous reprenons l'exemple du chapitre précédent de la fonction `maison()`. Cette fois nous y intégrons `begin_fill()` et `end_fill()` pour pouvoir les colorier..

```{codeplay}
from turtle import *
getscreen().bgcolor('lightgreen')

def maison():
    begin_fill()
    forward(100)
    left(90)
    forward(60)
    left(45)
    forward(71)
    left(90)
    forward(71)
    left(45)
    forward(60)
    left(90)
    end_fill()
    
back(200)
fillcolor('pink')
maison()
forward(150)
fillcolor('lightblue')
maison()
```

**Exercice** : Ajoutez encore une maison dans une autre couleur.

## Export vers un fichier

Pour sauvegarder votre dessin vers un fichier copiez le code du dessin dans l'éditeur Thonny. Ensuite copiez ces lignes de code ci-dessous à la fin de de votre fichier.

```{code-block} python
from tkinter import * 
cn = getscreen().getcanvas()
cn.postscript(file='file.eps')
```

Votre image va être exporté vers un fichier qui s'appelle `file.eps` et qui se trouve dans le même dossier ou se trouve votre fichier Python.
Vous pouvez changer le nom du fichier, mais vous devez garder l'extension `.eps`.

Sur un Mac, vous pouvez ouvrir un fichier `.eps` avec l'application **Aperçu** et ensuite exporter l'image vers le format PDF, JPG ou PNG.

**Exercice**  
Copiez le code suivant dans Thonny, sauvegardez-le avec le nom `smiley.py`, exécutez le code et retrouvez le fichier `smiley.eps` dans le même dossier où vous avez enregistré votre programme.

```python
from turtle import *
getscreen().bgcolor('azure')
dot(1000, 'azure')

dot(300, 'palegreen')
up()

left(45)
forward(60)
dot(40)

right(45)
back(90)
dot(40)

right(60)
forward(100)
dot(100)

from tkinter import * 
cn = getscreen().getcanvas()
cn.postscript(file='smiley.eps')
```

## Export en PNG/JPG

Pour directement sauvegarder votre dessin en format PNG, ajoutez ces lignes de code à la fin de votre dessin.

```{code-block} python
from tkinter import *
from PIL import Image
import io

cn = getscreen().getcanvas()
ps = cn.postscript(colormode='color')
file = io.BytesIO(ps.encode('utf-8'))
img = Image.open(file)
img.save('file.png')
```

Pour sauvegarder en format JPG utilisez tout simplement l'extension `.jpg`.

## Exercices

Dans tous les exercices suivants commencez par définir une couleur d'arrière-fond appropriée.

1. Dessinez et coloriez un sapin de Noël. Définissez des fonctions pour des boules et des étoiles.
1. Dessinez et coloriez une ville. Définissez des fonctions pour des maisons et des immeubles.
1. Dessinez et coloriez un paysage. Définissez des fonctions pour des montagnes et des sapins.
1. Dessinez et coloriez un jardin. Définissez des fonctions pour les feuilles, les pétales et les fleurs.
1. Dessinez et coloriez un aquarium. Définissez des fonctions pour les poissons, l'herbe, et les bulles.
