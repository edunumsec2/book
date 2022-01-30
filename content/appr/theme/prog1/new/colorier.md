# Colorier - `color`

Dans ce chapitre nous continuons à dessiner et nous introduisons la couleur.
Une couleur peut être appliquée à une ligne, à un point, à une forme ou à l'arrière-fond. Nous allons voir que :

- la fonction `color()` permet de choisir une couleur,
- la fonction `dot(d)` dessine un disque de diamètre `d`,
- la fonction `begin_fill()/end_fill()` permet le remplissage.

```{question}
Une couleur sur un écran d'ordinateur est produite par

{f}`des pigments`  
{f}`du mouvement rapide`  
{f}`un liquide colorié`  
{v}`la combinaison de trois lumières`
```

## Liste de couleurs

Voici une liste des couleurs disponibles. Pour les utiliser vous devez les écrire entre des apostrophes, comme par exemple `'pink'` ou `'hotpink'`.

![couleurs](media/colors.png)

## Couleur de ligne

La fonction `color()` permet de définir la couleur de ligne.
Entre les parenthèses de la fonction vous devez écrire le nom d'une couleur, entouré d'apostrophes, par exemple `color('red')` pour dessiner une ligne rouge.

Voici un triangle avec 3 segments de couleurs différentes.

```{codeplay}
:file: color1.py
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
:file: color2.py
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

### Drapeau du Japon

Le drapeau du Japon est un drapeau blanc avec un grand disque rouge en son centre. Ce disque représente le soleil, plus précisément la déesse shinto du soleil Amaterasu.

Le rapport entre la hauteur et la largeur du drapeau est de 2:3, et le diamètre du disque est trois cinquièmes de la hauteur du drapeau.

```{codeplay}
from turtle import *
dot(240, 'red')
hideturtle()
```

**Exercice** : Enlevez la fonction `hideturtle()`. Quelle est sa fonction ?

### Lignes et points

La fonction `dot()` sans argument de taille, va automatiquement choisir une taille qui est environ le double de l'épaisseur du trait.

```{codeplay}
from turtle import *

forward(100)
left(120)
dot()

forward(100)
left(120)
dot()

forward(100)
left(120)
dot()
```

**Exercice** : Augmentez l'épaisseur de la ligne à 10 pour vérifier que la taille des points change en conséquence.

### Points et couleurs

Il est possible de colorier les points différemment de la ligne. Dans ce cas il faut spécifier taille et couleur dans la fonction `dot()`.

```{codeplay}
from turtle import *
pencolor('blue')

forward(100)
left(120)
dot(10, 'red')

forward(100)
left(120)
dot(10, 'red')

forward(100)
left(120)
dot(10, 'red')
```

## Couleur de forme

Avec la fonction `fillcolor()` nous pouvons définir une couleur de remplissage de forme. Pour remplir une forme avec une couleur, nous devons ajouter les deux fonctions :

- `begin_fill()` au début de la forme,
- `end_fill()` à la fin de la forme.

Par exemple ce programme-ci dessine un carré jaune.

```{codeplay}
:file: color3.py
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

Le fonction `getscreen()` retourne un objet `Screen`. Cet objet possède une méthode `bgcolor()`. La combinaison `getscreen().bgcolor()` permet de définir la couleur d'arrière-fond (bg = background).

Dans l'exemple suivant, nous dessinons le drapeau du Bangladesh. Il est vert frappé d'un disque rouge.

```{codeplay}
:file: color4.py
from turtle import *
getscreen().bgcolor('green')

back(30)
dot(266, 'red')
hideturtle()
```

Le drapeau au soleil rouge a été utilisé pour la première fois en 1971. Le rouge symbolise le sang des Bangladais tués depuis 1947 lors des affrontements avec le Pakistan. Le vert symbolise la vitalité, la jeunesse et les terres agricoles.

```{caution}
La fonction `bgcolor()` ne fonctionne pas pour l'exportation vers un fichier image au format `.eps`. 

Pour remédier à ce problème nous utilisons une solution simpliste.
A la place de `bgcolor()` nous utilisons tout simplement un très grand disque `dot()` qui dépasse les bornes de l'image.
```

Le disque est décentré, légèrement décalé vers la fixation, de manière à apparaître centré lorsque le drapeau flotte dans le vent.

```{codeplay}
:file: color4.py
from turtle import *
dot(1000, 'green')  # background

back(30)
dot(266, 'red')
hideturtle()
```

## Forme ouverte

La forme ne doit pas nécessairement être fermée pour être remplie d'une couleur.
Dans l'exemple suivant nous dessinons une forme ouverte avec seulement deux lignes.
Le résultat est un triangle avec deux bordures et un troisième segment sans bordure.

Une équerre est un instrument formé de deux pièces ajustées à angle droit. l'équerre est utilisée soit pour vérifier des angles dièdres droits, soit pour tracer des angles plans droits.

```{codeplay}
:file: color5.py
from turtle import *
dot(1000, 'moccasin')  # background

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
:file: color6.py
from turtle import *
dot(1000, 'linen')  # background

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
:file: color7.py
from turtle import *
dot(1000, 'azure')  # background

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

La fonction `bras()` dessine les 3 côtés d'un carré et tourne de 90° dans le contre-sens.
Répété 4 fois, ceci donne la forme d'une croix.

```{codeplay}
:file: color8.py
from turtle import *
dot(1000, 'red')  # background

def bras():
    forward(60)
    left(90)
    forward(60)
    left(90)
    forward(60)
    right(90)

def croix():
    bras()
    bras()
    bras()
    bras()
    
fillcolor('white')
begin_fill()
croix()
end_fill()
```

**Exercice** : Inversez les couleurs pour trouver le drapeau de la Croix-Rouge.

## Maison

Nous reprenons l'exemple du chapitre précédent de la fonction `maison()`. Cette fois nous y intégrons `begin_fill()` et `end_fill()` pour pouvoir les colorier..

```{codeplay}
:file: color9.py
from turtle import *
dot(1000, 'lightgreen')  # background

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

## Exporter une image

Pour enregistrer votre dessin vers un fichier image faites ceci :

- téléchargez le code,
- ouvrez-le avec un éditeur externe,
- ajoutez les 3 lignes de code à la fin,
- exécutez votre code.

```  python
if len(dir(Turtle)) > 100:
    from tkinter import * 
    Screen().getcanvas().postscript(file='file.eps')
```

Votre image est exporté vers un fichier `file.eps` et qui se trouve dans le même dossier que votre code.
Vous pouvez changer le nom du fichier, mais vous devez garder l'extension `.eps`.

Sur un Mac, vous pouvez ouvrir un fichier `.eps` avec l'application **Aperçu** et ensuite exporter l'image vers le format PDF, JPG ou PNG.

**Exercice**

- Téléchargez le code
- Ouvrez-le avec Thonny
- Exécutez le code
- Ouvrez le ficher image `japon.eps`

```{codeplay}
:file: japon.py
from turtle import *
dot(240, 'red')
hideturtle()

if len(dir(Turtle)) > 100:
    from tkinter import * 
    Screen().getcanvas().postscript(file='japon.eps')
```

## Exercices

- Téléchargez un exercice.
- Editez-le dans un éditeur externe tel que Thonny.
- Déposez-le sur Moodle (ou plateforme équivalente de votre école).

### Un arc-en-ciel

Dessinez un arc-en-ciel avec des disques de rayon et de couleurs différents.

```{codeplay}
:file: arc_en_ciel.py
from turtle import *
# Votre prénom, nom, classe

dot(100)
```

### Sapin de Noël

Dessinez et coloriez un sapin de Noël. Définissez des fonctions pour des boules et des étoiles.

```{codeplay}
:file: sapin.py
from turtle import *
# Votre prénom, nom, classe

def sapin():
    ...

def boule():
    ...

def etoile():
    ...

sapin()
forward(100)
boule()

if len(dir(Turtle)) > 100:
    from tkinter import * 
    Screen().getcanvas().postscript(file='sapin.eps')
```

### Une ville

Dessinez et coloriez une ville. Définissez des fonctions pour des maisons et des immeubles.

```{codeplay}
:file: ville.py
from turtle import *
# Votre prénom, nom, classe

dot(1000, 'skyblue')  # background

def maison():
    ...

def immeuble():
    ...

maison()
forward(100)
immeuble()

if len(dir(Turtle)) > 100:
    from tkinter import * 
    Screen().getcanvas().postscript(file='ville.eps')
```
