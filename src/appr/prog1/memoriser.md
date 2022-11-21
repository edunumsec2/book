(prog1.memoriser)=
# Mémoriser - `a=100`

Dans ce chapitre, nous allons voir comment un programme peut mémoriser des valeurs et les utiliser par la suite pour dessiner et pour calculer. Ces valeurs sont associées à des variables que nous définissons au début du programme. Nous allons voir que :

- L'expression `a = 100` crée une variable `a` à laquelle on donne la valeur 100,
- Ceci est appelé **affectation**, ce n'est pas une équation mathématique
- On appelle `a` une variable et `100` sa valeur.

```{question}
En informatique, une variable est

{v}`une place en mémoire`  
{v}`une étiquette pour un objet`  
{v}`un endroit spécifique de stockage`  
{v}`un nom pour une valeur`
```

## Rectangle

Dans le chapitre [Dessiner](prog1.dessiner), nous avons vu un programme commme une séquence d'instructions.

```{codeplay}
from turtle import *

forward(160)
left(90)
forward(100)
left(90)
forward(160)
left(90)
forward(100)
left(90)
```

Dans le chapitre [Définir](prog1.definir), nous avons vu que nous pouvons définir nos propres instructions avec le mot-clé `def` en donnant un nom à une séquence.

```{codeplay}
from turtle import *

def rectangle():    # définir une fonction
    forward(160)    # séquence de 8 instructions
    left(90)
    forward(100)
    left(90)
    forward(160)
    left(90)
    forward(100)
    left(90)

rectangle()         # appeler une fonction
```

Dans le chapitre [Répéter](prog1.repeter), nous avons vu que nous pouvons répéter des instructions pluseurs fois avec le mot-clé `for`.

```{codeplay}
from turtle import *

def rectangle():            # définir une fonction
    for i in range(2):      # répéter 2 fois
        forward(160)        # sequence de 4 instructions
        left(90)
        forward(100)
        left(90)

rectangle()                 # appeler une fonction
```

Maintenant, nous allons définir deux variables `a` et `b` au début du programme.  Avec un commentaire nous expliquons leur signification dans le programme. Plus tard dans le programme nous pouvons utiliser ces variables.

```{admonition} Exercice
Aujoutez une variable `alpha` pour l'angle et utilisez-la dans le corps de la fonction.
```

```{codeplay}
from turtle import *

a = 160     # longueur du rectangle
b = 100     # largeur du rectangle

def rectangle():            # définir une fonction
    for i in range(2):      # répéter 2 fois
        forward(a)          # sequence de 4 instructions
        left(90)
        forward(b)
        left(90)

rectangle()
```

## Losange

Dans ce programme nous définissons trois variables `a`, `b` et `angle` au début du programme. Avec un commentaire nous expliquons leur significations dans le programme. Plus tard dans le programme nous pouvons utiliser ces variables dans des dessins.

Quel est l'avantage ?

- toutes les valeurs sont définies au début du programme
- il devient facile de changer les dimensions

```{admonition} Exercice
Modifiez la variable `angle` en mettant 80 et ensuite 90 degrés.
```

```{codeplay}
from turtle import *

a = 150     # longueur du losange
b = 100     # largeur du losange
angle = 60  # premier angle du losange

def losange():
    for i in range(2):
        forward(a)
        left(angle)
        forward(b)
        left(180-angle)     # angle complémentaire

losange()
```

## Changer les variables

À n'importe quel moment dans un programme nous pouvons changer les variables. Ils auront dorénavant ces nouvelles valeurs.

```{codeplay}
from turtle import *

a = 100     # longueur du rectangle
b = 50      # largeur du rectangle

def rectangle():
    forward(a)
    left(90)
    forward(b)
    left(90)
    forward(a)
    left(90)
    forward(b)
    left(90)

rectangle()

a = 120
b = 180
rectangle()
```

## Polygone

Utiliser des variables permet aussi de faire des calculs avec ces variables. Par exemple nous pouvons calculer l'angle à tourner dans un polygone qui est de `360/n`. 

```{codeplay}
from turtle import *

a = 100     # longueur du polygone
n = 3       # nombre de sommets

def polygone():
    for i in range(n):
        forward(a)
        left(360/n)

polygone()
```

## Maison

Utiliser des variables permet aussi de faire des calculs avec ces variables. Par exemple nous pouvons calculer la longueur de la base de la maison qui est $ \sqrt{2} a$.

Nous pouvons donc facilement dessiner une maison qui mesure que la moitié.

```{codeplay}
from turtle import *
up()

a = 20     # longueur de base

def maison():
    down()
    forward(1.41 * a)
    left(90)
    forward(a)
    left(45)
    forward(a)
    left(90)
    forward(a)
    left(45)
    forward(a)
    left(90)
    up()

backward(200)  
maison()

forward(100)
a = 50
maison()

forward(150)
a = 100
maison()
```

## Nommer une variable

Pour nommer une variable, vous pouvez utiliser :

- lettres (`a...z` et `A...Z`),
- chiffres (`0...9`),
- le tiret bas (`_`).

Le nom de variable :

- est sensible aux majuscules/minuscules,
- ne peut pas commencer avec un chiffre,
- ne doit pas consister d'un mot-clé (`if`, `else`, `for`),

Ces noms de variables sont donc valides : `a2`, `_a`, `speed`, `pos_x`, `POS_X`

```{question}
Lesquels des noms de variable sont valides ?

{f}`var 2`  
{v}`var2`  
{f}`2var`  
{v}`IF`
===
`var 2` contient une espace  
`2var` commence par un chiffre  
`IF` n'est pas un mot-clé  
```



## Exercices

Dans ces exercices nous retournons aux formes précédents. Nous utilisons maintenant des variables définies au début du programme pour dessiner deux ou plusieurs variantes de la forme.

### Coeur

Définissez une fonction `coeur()` dont la taille dépend du rayon `r`. Dessinez alors trois coeurs de tailles différentes.

```{codeplay}
:file: coeur.py
from turtle import *
r = 20      # rayon du coeur

def coeur():
    left(90)
    circle(50, 225)     # exprimez 50 par r
    forward(120)        # exprimez 120 par r 
    left(90)
    forward(120)        # exprimez 120 par r
    circle(50, 225)     # exprimez 50 par r
    left(90)

coeur()
```

### Infini

Définissez une fonction `infini()` dont la taille dépend du rayon `r`. Dessinez alors trois symboles de tailles différentes.

```{codeplay}
:file: infini.py
from turtle import *
r = 30      # rayon du symbole
w = 1       # épaisseur

def infini():
    forward(100)        # exprimez 100 par r
    circle(50, 270)     # exprimez 50 par r
    forward(100)        # exprimez 100 par r
    circle(-50, 270)    # expriemz -50 par r

infini()
```

### Bretzel

Définissez une fonction `bretzel()` dont la taille dépend du rayon `r`. Dessinez alors trois symboles de tailles différentes.

```{codeplay}
:file: bretzel.py
from turtle import *
r = 50      # rayon du symbole

def bretzel():
    for i in range(4):
        forward(80)         # exprimez 80 par r
        circle(30, 270)     # exprimez 30 par r

bretzel()
```

### Lettres

Définissez des fonctions de lettres dont la taille dépand de la variable `a`. Ecrivez alors plusieurs textes avec des tailles différentes.

```{codeplay}
:file: lettres.py
from turtle import *
up()
a = 50      # hauteur d'une lettre

def n():
    down()
    left(90)
    forward(80)         # exprimez 80 par a
    backward(40)
    circle(-40, 180)    # exprimez -40 par a
    forward(40)         # exprimez 40 par a
    left(90)
    up()
    forward(20)

def o():
    forward(40)
    down()
    circle(40)
    up()
    forward(60)

backward(200)
o()
n()
```
