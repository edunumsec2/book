(prog1.colorier)=

# *Colorier - `color()`

Dans ce chapitre, nous continuons à dessiner et nous introduisons la couleur.
Une couleur peut être appliquée à une ligne, à un point, à une forme ou à l'arrière-fond. Nous allons voir que :

- la fonction `color(c)` permet de choisir une couleur `c`,
- la fonction `dot(d, c)` dessine un disque de diamètre `d` et de couleur `c`,
- la fonction `begin_fill()/end_fill()` permet le remplissage.

```{question}
Une couleur sur un écran d'ordinateur est produite par

{f}`des pigments`  
{f}`du mouvement rapide`  
{f}`un liquide coloré`  
{v}`la combinaison de trois lumières`
```

## Liste de couleurs

Voici une liste des couleurs disponibles. Pour les utiliser vous devez les écrire entre apostrophes, comme par exemple `'pink'` ou `'hotpink'`.

![couleurs](media/colors.png)

## Couleur de ligne

La fonction `color(c)` permet de définir la couleur de ligne `c`.
Entre les parenthèses de la fonction, vous devez écrire le nom d'une couleur, entouré d'apostrophes — par exemple `color('red')` pour dessiner une ligne rouge.

Voici un triangle avec 3 segments de couleurs différentes.

```{exercise}
Modifiez les 3 couleurs en vous inspirant de la liste.
```

```{codeplay}
:file: color1.py
from turtle import *
d = 150
width(20)

color('red')
forward(d)
left(120)

color('lime')
forward(d)
left(120)

color('blue')
forward(d)
left(120)
```

## Couleur de point

Nous pouvons afficher des points à chaque sommet :

- la fonction `dot()` dessine un point standard,
- la fonction `dot(d)` dessine un disque d'un diamètre `d`,
- la fonction `dot(d, c)` dessine un disque de diamètre `d` et de couleur `c`.

```{exercise}
Modifiez la taille et la couleur des 3 points.
```

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

### Drapeau du Japon

Le drapeau du Japon est un drapeau blanc avec un grand disque rouge en son centre. Ce disque représente le soleil, plus précisément la déesse shinto du soleil Amaterasu.

Le rapport entre la hauteur et la largeur du drapeau est de 2:3, et le diamètre du disque est $\frac{3}{5}$ de la hauteur du drapeau.

```{exercise}
Supprimez l'appel de la fonction `hideturtle()`. À quoi sert cette fonction ?
```

```{codeplay}
:file: color3.py
from turtle import *
dot(240, 'red')
hideturtle()
```

### Lignes et points

La fonction `dot()` sans argument de taille, va automatiquement choisir une taille qui est environ le double de l'épaisseur du trait.

```{exercise}
Augmentez l'épaisseur de la ligne à 10 pour vérifier que la taille des points change en conséquence.
```

```{codeplay}
:file: color4.py
from turtle import *
d = 100

forward(d)
left(120)
dot()

forward(d)
left(120)
dot()

forward(d)
left(120)
dot()
```

### Points et couleurs

Il est possible de colorier les points différemment de la ligne. Dans ce cas, il faut spécifier la taille _et_ la couleur dans la fonction `dot()`.

```{codeplay}
:file: color5.py
from turtle import *
pencolor('blue')
d = 100

forward(d)
left(120)
dot(10, 'red')

forward(d)
left(120)
dot(10, 'red')

forward(d)
left(120)
dot(10, 'red')
```

## Couleur de remplissage

Avec la fonction `fillcolor()`, nous pouvons définir une couleur de remplissage pour une forme quelconque que nous voulons dessiner. Pour remplir une forme avec une couleur, nous devons ajouter les deux fonctions :

- `begin_fill()` au début de la forme,
- `end_fill()` à la fin de la forme.

Par exemple, ce programme-ci dessine un triangle vert.

```{exercise}
Ajoutez un triangle d'une couleur différente.
```

```{codeplay}
:file: color6.py
from turtle import *
d = 100

def triangle():
    forward(d)
    left(120)
    forward(d)
    left(120)
    forward(d)
    left(120)

fillcolor('chartreuse')
begin_fill()
triangle()
end_fill()
```

On aurait pu inclure les deux fonctions qui indiquent le remplissage directement dans la fonction `triangle()`. Ceci simplifie le code quand on dessine plusieurs triangles.

```{codeplay}
:file: color7.py
from turtle import *
d = 100

def triangle():
    begin_fill()
    forward(d)
    left(120)
    forward(d)
    left(120)
    forward(d)
    left(120)
    end_fill()

fillcolor('chartreuse')
triangle()
left(60)
fillcolor('cyan')
triangle()
```

## Couleur de fond

La combinaison `getscreen().bgcolor()` permet de définir la couleur d'arrière-fond (bg = background).

Dans l'exemple suivant, nous dessinons le drapeau du Bangladesh. Il est vert avec un disque rouge.

```{codeplay}
:file: color8.py
from turtle import *
getscreen().bgcolor('green')

backward(30)
dot(266, 'red')
hideturtle()
```

Le drapeau au soleil rouge a été utilisé pour la première fois en 1971. Le rouge symbolise le sang des Bangladais tués depuis 1947 lors des affrontements avec le Pakistan. Le vert symbolise la vitalité, la jeunesse et les terres agricoles.

```{caution}
La fonction `bgcolor()` ne fonctionne pas pour l'exportation vers un fichier image au format `.eps`. 

Pour remédier à ce problème, nous utilisons une solution simpliste.
À la place de `bgcolor()` nous utilisons tout simplement un très grand disque `dot()` qui dépasse les bornes de l'image.
```

Le disque est décentré, légèrement décalé vers la fixation, de manière à apparaître centré lorsque le drapeau flotte dans le vent.

```{codeplay}
:file: color9.py
from turtle import *
dot(1000, 'green')  # astuce pour changer le background

backward(30)
dot(266, 'red')
hideturtle()
```

## Forme ouverte

La forme ne doit pas nécessairement être fermée pour être remplie d'une couleur.
Dans l'exemple suivant, nous dessinons une forme ouverte avec seulement deux lignes.
Le résultat est un triangle avec deux bordures et un troisième segment sans bordure.

Une équerre est un instrument formé de deux pièces ajustées à angle droit. L'équerre est utilisée soit pour vérifier des angles dièdres droits, soit pour tracer des angles plans droits.

```{exercise}
Dessinez le drapeau bicolore du canton de Zurich.
```

```{codeplay}
:file: color10.py
from turtle import *
dot(1000, 'moccasin')

def equerre():
    down()
    begin_fill()
    forward(150)
    left(90)
    forward(100)
    left(90)
    end_fill()
    up()

fillcolor('sienna')
equerre()
forward(30)
fillcolor('gold')
equerre()
```

## Smiley

Avec des cercles de tailles différentes dessinées avec `dot(d)`, nous pouvons dessiner un smiley.
Voici un smiley qui exprime l'indifférence.

```{exercise}
Ajoutez `up()` au début du programme pour ne plus montrer la trajectoire de la tortue.
```

```{codeplay}
:file: color11.py
from turtle import *
dot(1000, 'linen')

dot(300, 'yellow')      # visage

left(45)
forward(60)
dot(40)                 # oeuil droite

right(45)
backward(100)
dot(40)                 # oeuil gauche

right(90)
forward(100)
left(90)
width(20)
forward(100)            # bouche
```

Voici un autre smiley qui exprime la surprise.

```{exercise}
Dessinez encore un autre smiley.
```

```{codeplay}
:file: color12.py
from turtle import *
dot(1000, 'azure')

dot(300, 'palegreen')

left(45)
forward(60)
dot(40)

right(45)
backward(90)
dot(40)

right(60)
forward(100)
dot(80)
```

## Croix

La fonction `bras()` dessine les 3 côtés d'un carré et tourne, à la fin, dans le sens approprié pour la suite.
Répété 4 fois, ceci donne la forme d'une croix.

Ici, nous utilisons la fonction `color('white')` pour changer simultanément la couleur de ligne **et** la couleur de remplissage en blanc.

```{exercise}
Inversez les couleurs pour trouver le drapeau de la Croix-Rouge.
```

```{codeplay}
:file: color13.py
from turtle import *
dot(1000, 'red')
d = 60

def bras():
    forward(d)
    left(90)
    forward(d)
    left(90)
    forward(d)
    right(90)

def croix():
    bras()
    bras()
    bras()
    bras()
    
color('white')
begin_fill()
croix()
end_fill()
```

## Maison

Nous reprenons l'exemple du chapitre précédent de la fonction `maison()`. Cette fois, nous y intégrons `begin_fill()` et `end_fill()` pour pouvoir les colorier..

```{exercise}
Ajoutez encore une maison d'une autre couleur.
```

```{codeplay}
:file: color9.py
from turtle import *
dot(1000, 'lightgreen')

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
    
backward(200)
fillcolor('pink')
maison()
forward(150)
fillcolor('lightblue')
maison()
```

## Exporter une image

Pour enregistrer votre dessin vers un fichier image, faites ceci :

- Téléchargez le code.
- Ouvrez-le avec un éditeur externe.
- Ajoutez les 2 lignes de code à la fin.
- Exécutez votre code.

```  python
from tkinter import * 
Screen().getcanvas().postscript(file='fichier.eps')
```

Votre image est exportée vers `fichier.eps`, qui se trouve dans le même dossier que votre code.
Vous pouvez changer le nom du fichier, mais devez garder l'extension `.eps`.

Sur un Mac, vous pouvez ouvrir un fichier `.eps` avec l'application **Aperçu** et ensuite exporter l'image vers le format PDF, JPG ou PNG.

## Exercices

- Téléchargez un exercice.
- Éditez-le dans un éditeur externe tel que Thonny.
- Déposez-le sur Moodle (ou une plateforme équivalente dans votre école).

### Arc-en-ciel

Dessinez un arc-en-ciel avec des disques de rayons et de couleurs appropriés.

```{codeplay}
:file: arc_en_ciel.py
from turtle import *
# Prénom Nom, classe

left(90)
back(300)
dot(800, 'red')
```

### Sapin de Noël

Dessinez et coloriez un sapin de Noël. Définissez des fonctions pour des boules et des étoiles.

```{codeplay}
:file: sapin.py
from turtle import *
# Prénom Nom, classe

def sapin():
    ...
def boule():
    ...
def etoile():
    ...

sapin()
forward(100)
boule()
done()
```

### Ville

Dessinez et coloriez une ville. Définissez des fonctions pour des maisons et des immeubles.

```{codeplay}
:file: ville.py
from turtle import *
# Prénom Nom, classe

dot(1000, 'skyblue')  # background

def maison():
    ...
def immeuble():
    ...

maison()
forward(100)
immeuble()
done()
```

### Chambre

Dessinez une chambre avec des meubles en couleurs, que vous définissez chacun par une fonction. Vous êtes libre d'inventer d'autres meubles, de les arranger différemment et de les utiliser plusieurs fois.

```{codeplay}
:file: chambre.py
from turtle import *
# Prénom Nom, classe

def chaise():    
    left(90)
    forward(100)
    back(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    left(90)

def table():
    ...
def lit():
    ...

chaise()
table()
lit()
done()
```

### Tetris

Les carrés de base d'un tétromino mesurent 40 × 40 pixels. Il y a 7 formes différentes de tétrominos, qui sont nommées d'après les lettres auxquelles ils ressemblent et qui ont des couleurs standard :

![tétrominos](media/tetromino.png)

Créez des fonctions pour dessiner les 7 tétrominos avec leurs couleurs appropriées, et composez la forme ci-dessous.

![tetris](media/tetris2.png)

```{codeplay}
:file: tetris2.py
from turtle import *
# Prénom Nom, classe
d = 40

def O():
    fillcolor('yellow')
    dot()
    begin_fill()
    forward(2*d)
    left(90)
    forward(2*d)
    left(90)
    forward(2*d)
    left(90)
    forward(2*d)
    left(90)
    end_fill()

def I():
    ...
def T():
    ...
def L():
    ...
def J():
    ...
def Z():
    ...
def S():
    ...

back(200)
O()
...
done()
```
