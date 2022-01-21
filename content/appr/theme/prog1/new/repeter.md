# Répéter - `for`

Dans ce chapitre nous découvrons comment utiliser une boucle `for` pour répéter un bloc d'instructions un certain nombre de fois. Nous allons voir que :

- la boucle `for` permet de répéter des instructions,
- la structure `for i in range(x):` permet de répéter un bloc x fois,
- le deux-points `:` est toujours suivi d'un bloc en indentation.

```{question}
Une boucle informatique est

{f}`une instruction`  
{f}`un passage ondulé`  
{v}`une section de code répétée`  
{f}`une protéction thérmique`
```

## La répétition

Revenons vers un exemple simple : dessiner un carré.

Si nous regardons le code de près, nous pouvons voir que nous répétons 4 fois les mêmes deux instruction `forward()` et `left()`.

```{codeplay}
:file: for1.py
from turtle import *

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
```

Ne serait-il pas pratique de pouvoir dire à la tortue de répéter ces instructions 4 fois ?  
Ceci est possible avec une boucle `for`. La ligne `for i in range(x):` va répéter `x` fois le bloc en indentation qui suit.

```{codeplay}
:file: for2.py
from turtle import *

for i in range(4):
    forward(100)
    left(90)
```

**Exercice** : Transformez le rectangle en triangle.

## Polygone régulier

Avec une boucle `for` nous pouvons simplifier le dessins des formes symétriques.

```{codeplay}
:file: for3.py
from turtle import *

def triangle():
    for i in range(3):
        forward(100)
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

**Exercice** : Définissez la fonction `hexagone()` pour dessiner un hexagone.

## Escalier

Pour dessiner un escalier, il faut simplement répéter dans une boucle le dessin pour une seule marche.

```{codeplay}
:file: for4.py
from turtle import *

for i in range(5):
    forward(20)
    left(90)
    forward(20)
    right(90)

forward(100)
```

## Dents de scie

Pour dessiner des dents de scie, il faut simplement répéter dans une boucle le dessin pour une seule dent.

```{codeplay}
:file: for5.py
from turtle import *

for i in range(4):
    left(45)
    forward(71)
    right(135)
    forward(50)
    left(90)

forward(80)
```

**Exercice** : Dessinez une usine avec un toit en dents de scie.

## Eventail

Que se passe-t-il si nous dessinons une ligne (`forward/back`) et tournons d'un petit angle à chaque fois ?
C'est un peu comme un éventail qui s'ouvre.

```{codeplay}
:file: for6.py
from turtle import *

for i in range(18):
    forward(100)
    back(100)
    left(10)
```

**Exercice** : Doublez l'angle de rotation dans `left()`.

## Diaphragme

Que se passe-t-il si nous avançons plus que nous reculons ?
Une toute petite modification du programme peut faire une chouette différence.

```{codeplay}
:file: for7.py
from turtle import *

for i in range(18):
    forward(100)
    back(90)
    left(20)
```

**Exercice** : Modifiez les valeurs dans `forward()` et `back()`.

## Etoile

Voici une autre façon de toujours avancer, mais tourner à chaque fois d'un angle un peu plus petit que 180°.
Essayons !

```{codeplay}
:file: for8.py
from turtle import *

for i in range(9):
    forward(200)
    left(160)
```

**Exercice** : Changez le nombre de pics de l'étoile.

## Losange

Si nous déformons les angles d'un carré, nous obtenons un losange (diamant).
Quelle forme obtenons-nous en dessinant un carré et deux losanges ?

```{codeplay}
:file: for9.py
from turtle import *

def carre():
    for i in range(4):
        right(90)
        forward(100)

def losange():
    for i in range(2):
        forward(100)
        left(120)
        forward(100)
        left(60)
        
carre()
right(90)
losange()
left(120)
losange()
```

## Fleur

Si nous dessinons un losange 6 fois, nous obtenons une jolie fleur.

```{codeplay}
:file: for10.py
from turtle import *

def losange():
    for i in range(2):
        forward(100)
        left(60)
        forward(100)
        left(120)

for i in range(6):
    losange()
    left(60)
```

**Exercice** : Tournez un angle plus petit que 60°

## Estamper la tortue

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

**Exercice** : Modifiez le programme pour estamper seulement à chaque deuxième sommet.

## Forme

Vous pouvez changer la forme de votre tortue avec la fonction `shape()`.

```{codeplay}
:file: for12.py
from turtle import *
back(200)

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

**Exercice** : Essayez les formes `triangle` et `arrow`.

## Vitesse

Vous pouvez changer la vitesse de la tortue avec la fonction `speed(s)`.
Le paramètre vitesse `s` peut varier entre 1 (le plus lent) et 1000 (le plus rapide). Sa vitesse par défaut est de 3. Mettre la vitesse à 0 choisit automatiquement la vitesse maximum.

```{codeplay}
:file: for13.py
from turtle import *
speed(2)

for i in range(36):
    forward(280)
    left(170)
```

**Exercice** : Augmentez graduellement la vitesse de la tortue.

## Exporter en PNG/JPG

Pour directement sauvegarder votre dessin en format PNG, ajoutez ces lignes de code à la fin de votre dessin.

``` python
from tkinter import *
from PIL import Image
import io

cn = getscreen().getcanvas()
ps = cn.postscript(colormode='color')
file = io.BytesIO(ps.encode('utf-8'))
img = Image.open(file)
img.save('file.png')
```

Pour sauvegarder en format JPG appelez tout simplement votre fichier `file.jpg`.

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
