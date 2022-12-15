(prog1.repeter)=

# Répéter - `for`

Dans ce chapitre, nous découvrons comment utiliser une boucle `for` pour répéter un bloc d'instructions un certain nombre de fois. Nous allons voir que :

- la boucle `for` permet de répéter des instructions,
- la structure `for i in range(n):` permet de répéter un bloc un nombre `n` fois,
- le deux-points `:` est toujours suivi d'un bloc en indentation.

```{question}
Une boucle informatique est

{f}`une instruction`  
{f}`un passage ondulé`  
{v}`une section de code répétée`  
{f}`une protection thermique`
```

## La répétition

Revenons vers un exemple simple : dessiner un carré.

Si nous regardons le code de près, nous pouvons voir que nous répétons 4 fois les mêmes deux instructions `forward()` et `left()`.

```{codeplay}
:file: for1.py
from turtle import *
d = 100

forward(d)
left(90)
forward(d)
left(90)
forward(d)
left(90)
forward(d)
left(90)
```

Ne serait-ce pas pratique de pouvoir dire à la tortue de répéter ces instructions 4 fois ?
Ceci est possible avec une boucle `for`. La ligne `for i in range(4):` va répéter `4` fois le bloc en indentation qui suit.

```{exercise}
Transformez le rectangle en triangle.
```

```{codeplay}
:file: for2.py
from turtle import *
d = 100

for i in range(4):
    forward(d)
    left(90)
```

## Variable d'itération `i`

Que représente `i` dans l'expression `for i in range(n)` ?  
C'est ce qu'on appelle une **variable d'itération**. Cette variable commence à 0 et augmente de 1 à chaque répétition jusqu'à $n-1$. Pour visualiser cette valeur nous pouvons l'afficher dans le dessin avec l'instruction `write(i)`.

```{codeplay}
:file: for2.py
from turtle import *
d = 100

for i in range(4):
    write(i)
    forward(d)
    left(90)
```

## Polygone régulier

Avec une boucle `for`, nous pouvons simplifier le dessin des formes symétriques.

Observez bien la double indentation :

- la première pour `def`
- la deuxième pour `for`

Dans les deux cas un `:` est suivi d'un bloc en indentation. En Python vous pouvez avoir multiples niveaux d'indentation.

```{exercise}
Définissez la fonction `hexagone()` pour dessiner un hexagone, et appelez cette fonction.
```

```{codeplay}
:file: for3.py
from turtle import *

def triangle():
    for i in range(3):      # indentation 1 (bloc pour def)
        forward(100)        # indentation 2 (bloc pour for)
        left(120)

def carre():
    for i in range(4):
        forward(100)
        left(90)

def pentagone():
    for i in range(5):
        forward(100)
        left(72)

triangle()
carre()
pentagone()
```

## Escalier

Pour dessiner un escalier, il faut simplement répéter dans une boucle le dessin pour une seule marche. Nous utilisons la variable `i` pour numéroter les marches.

```{codeplay}
:file: for4.py
from turtle import *

for i in range(5):
    write(i)
    forward(20)
    left(90)
    forward(20)
    right(90)

forward(100)
```

Pour dessiner des dents de scie, il faut simplement répéter dans une boucle le dessin pour une seule dent.

```{exercise}
Dessinez une usine avec un toit en dents de scie.
```

```{codeplay}
:file: for5.py
from turtle import *

for i in range(4):
    left(45)
    forward(71)
    write(i)
    right(135)
    forward(50)
    left(90)

forward(80)
```

## Éventail

Que se passe-t-il si nous dessinons une ligne (`forward()`/`backward()`) et tournons chaque fois d'un petit angle ?
C'est un peu comme un éventail qui s'ouvre. Les lignes de l'éventail sont numérotés en utilisant la variable `i`.

```{exercise}
Doublez l'angle de rotation dans `left()`.
```

```{codeplay}
:file: for6.py
from turtle import *
d = 100

for i in range(18):
    forward(d)
    write(i)
    backward(d)
    left(10)
```

Que se passe-t-il si nous avançons plus que nous reculons ?
Une toute petite modification du programme peut faire une chouette différence.

```{exercise}
Modifiez les valeurs dans `forward()` et `backward()`.
```

```{codeplay}
:file: for7.py
from turtle import *

for i in range(18):
    forward(100)
    write(i)
    backward(90)
    left(20)
```

## Étoile

Voici une autre façon de toujours avancer, mais en tournant chaque fois d'un angle un peu plus petit que 180°.
Essayons !

```{exercise}
Changez le nombre de pics de l'étoile.
```

```{codeplay}
:file: for8.py
from turtle import *

for i in range(9):
    write(i)
    forward(200)
    left(160)
```

## Losange

Si nous déformons les angles d'un carré, nous obtenons un losange (diamant).
Quelle forme obtenons-nous en dessinant un carré et deux losanges ?

```{codeplay}
:file: for9.py
from turtle import *
d = 100

def carre():
    for i in range(4):
        right(90)
        forward(d)

def losange():
    for i in range(2):
        forward(d)
        left(120)
        forward(d)
        left(60)
        
carre()
right(90)
losange()
left(120)
losange()
```

Si nous dessinons un losange 6 fois, nous obtenons une jolie fleur.

```{exercise}
Tournez un angle plus petit que 60°
```

```{codeplay}
:file: for10.py
from turtle import *
d = 100

def losange():
    for i in range(2):
        forward(d)
        left(60)
        forward(d)
        left(120)

for i in range(6):
    losange()
    left(60)
```

## Paquebot

Une boucle `for` est utilisée dans l'exemple suivant pour dessiner les hublots d'un paquebot. Les hublots sont numérotés en utilisant la variable `i`.

```{exercise}
Créez une fonction `paquebot()` et dessinez-en un deuxième.
```

```{codeplay}
from turtle import *

forward(200)
left(80)
forward(60)
left(100)
forward(220)
left(100)
forward(60)

up()
left(125)
forward(40)
right(45)

for i in range(6):
    dot(20, 'lightgray')
    write(i)  
    forward(30)
```

## Cube de Rubik

Le [Cube de Rubik](https://fr.wikipedia.org/wiki/Rubik%27s_Cube) est un casse-tête inventé par Ernő Rubik en 1974, et qui s’est rapidement répandu sur toute la planète au cours des années 1980.

Pour dessiner la face rouge, nous dessinons d'abord une ligne, en répétant 3 fois un carré. Ensuite nous répétons 3 fois une ligne pour dessiner une surface.

```{codeplay}
from turtle import *
d = 50

def carre():
    begin_fill()
    for i in range(4):
        forward(d)
        left(90)
    end_fill()

def ligne():
    fillcolor('red')
    for i in range(3):
        carre()
        forward(d)
    backward(3*d)

for i in range(3):
    ligne()
    left(90)
    forward(d)
    right(90)
```

## La tortue

Voici quelques fonctions de la tortue.

### Estampe

Vous pouvez laisser une impression de la tortue à sa position actuelle avec la fonction `stamp()`.

```{codeplay}
:file: for11.py
from turtle import *
shape('turtle')

for i in range(6):
    forward(100)
    left(60)
    stamp()
```

### Forme

Vous pouvez changer la forme de votre tortue avec la fonction `shape()`.

```{exercise}
Essayez les formes `'triangle'` et `'arrow'`.
```

```{codeplay}
:file: for12.py
from turtle import *
backward(200)

stamp()
shape('turtle')
forward(100)

stamp()
shape('circle')
forward(100)

stamp()
shape('square')
forward(100)
```

### Vitesse

Vous pouvez changer la vitesse de la tortue avec la fonction `speed(s)`.
Le paramètre vitesse `s` peut varier entre 1 (le plus lent) et 1000 (le plus rapide). Sa vitesse par défaut est de 3. Mettre la vitesse à 0 choisit automatiquement la vitesse maximum.

```{exercise}
Augmentez graduellement la vitesse de la tortue, en utilisant la variable `i` comme argument de vitesse.
```

```{codeplay}
:file: for13.py
from turtle import *
speed(2)

for i in range(36):
    forward(280)
    left(170)
```

## Erreurs

Il est important de bien lire et comprendre les messages d'erreur.
Dans cette section, vous allez découvrir les différentes catégories d'erreur et comment les corriger.

### ImportError

Cette erreur survient lorsque vous essayez d'importer un module qui n'existe pas.

```{exercise}
Corrigez l'erreur d'importation.
```

```{codeplay}
from turtl import *

for i in range(3):
    forward(100)
    left(120)
```

### SyntaxError

Cette erreur survient lorsque vous écrivez mal un mot-clé, ou si vous oubliez une ponctuation. Dans ce cas, le mot-clé mal écrit n'est pas reconnu et il n'est pas colorié correctement dans votre code.

```{exercise}
Corrigez les trois erreurs de syntaxe et remarquez les éventuelles différences de stylisation.
```

```{codeplay}
fro turtle import *

fore i in range(3)
    forward(100)
    left(120)
```

### NameError

Cette erreur survient lorsque vous écrivez mal le nom d'une variable ou fonction.

```{exercise}
Corrigez les trois erreurs de nom.
```

```{codeplay}
from turtle import *

for i in range(n):
    forwarde(100)
    lefft(120)
```

### TypeError

Cette erreur survient lorsque vous ne mettez pas le nombre d'arguments corrects pour une fonction.

```{exercise}
Corrigez les trois erreurs de type.
```

```{codeplay}
from turtle import *

for i in range():
    forward()
    left(100, 120)
```

## Exercice

- Téléchargez un exercice.
- Éditez-le dans un éditeur externe.
- Déposez-le sur Moodle.

### Pellicule

Une pellicule photographique est un support souple recouvert d'une émulsion contenant des composés sensibles à la lumière.
Dessinez une pellicule photographique. Utilisez une boucle `for` pour créer 4 trous de perforation. Utilisez une deuxième boucle pour répéter une trame.

```{image} media/pellicule.jpg
:width: 200
```

```{codeplay}
:file: pellicule.py
from turtle import *
# Prénom Nom, classe

forward(200)
```

### Chemin de fer

Dessinez les rails d'un chemin de fer.

![rails](media/rails.png)

Utilisez une boucle `for` pour la répétition des traverses.

```{codeplay}
:file: rails.py
from turtle import *
# Prénom Nom, classe

def traverse():
    ...

forward(200)
```

### Wagon de métro

Dessinez un wagon de métro. Utilisez une boucle `for` pour les fenêtres. Utilisez la fonction `dot()` pour les roues.

```{codeplay}
:file: metro.py
from turtle import *
# Prénom Nom, classe

def wagon():
    ...

forward(200)
```

### Gratte-ciel

Dessinez un gratte-ciel avec $n \times m$ fenêtres. Pour ceci, utilisez deux boucles imbriquées.

```{codeplay}
:file: gratte_ciel.py
from turtle import *
# Prénom Nom, classe

def fenetre():
    ...

forward(200)
```

### Jeu du moulin

Le [jeu du moulin](https://fr.wikipedia.org/wiki/Jeu_du_moulin) est un jeu de société traditionnel en Europe. Le plateau de jeu existait déjà dans la Rome antique. Aussi appelé **jeu du charret** (en Suisse), certains lui donnent le nom médiéval de jeu de mérelles, voire de marelle.

```{image} media/moulin.png
:width: 200
```

Pour les points d'intersection, utilisez la fonction `dot()`. La distance entre les lignes est de 50 pixels.

Vous constatez aussi une symétrie par 4. Donc avec un choix intelligent de fonction et de boucle `for`, vous pouvez réduire le nombre de lignes de code considérablement.

```{codeplay}
:file: moulin.py
from turtle import *
# Prénom Nom, classe
width(8)
up()
forward(50)
down()
dot()
forward(50)
dot()
forward(50)
dot()
...
done()
```

### TP

Créez une scène de jeu vidéo en utilisant la répétition, des cercles et de la couleur.

```{codeplay}
:file: tp3.py
"""
tp3 - répéter

Nom : 
Classe :
Date :

- nommez ce fichier : tp3_classe_prenom (minuscules, sans accents)
- créez 5+ fonctions qui utilisent la répétion
- utilisez la variable d (distance) pour vos déplacements
- composez une scène de jeu vidéo (pacman, tetris, minecraft, etc.
- utilisez de la couleur
- déposez sur Moodle :
    tp3_classe_prenom.py     (code)
    tp3_classe_prenom.eps    (image vectorielle)
    tp3_classe_preneom.jpg   (image)
"""
from turtle import *
# from tkinter import *

d = 20

def pacman():
    down()
    left(45)
    forward(d)
    left(90)
    circle(d, 270)
    left(90)
    forward(d)
    right(135)   
    for i in range(5):
        up()
        forward(d)
        dot(d/5)

# ajoutez vos fonctions ici

pacman()

# Screen().getcanvas().postscript(file='tp3.eps')
done()
```
