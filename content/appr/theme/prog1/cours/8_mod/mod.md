# 7. Modules

Lorsqu'on crée de multiples programmes dans des domaines similaires, il est fort probable que des parties de code puissent être réutilisées très fréquemment. Il serait donc plus efficace de placer ce code d'utilité générale dans un endroit spécifique.

Un **module** est un ou plusieurs fichiers en Python que l'on peut importer au début d'un programme.
Ce sont des scripts, contenant un ensemble de définitions — typiquement des fonctions, mais aussi des variables ou constantes (comme *pi* du module `math`).

Python est accompagné d'une bibliothèque de modules standards, tels que :

- `math`,
- `random`,
- `time`,
- `turtle`.

Pour d'autres modules, on peut consulter l'[index des modules Python](https://docs.python.org/3/py-modindex.html).

## Importer un module

Le mot-clé `import` permet d'importer un module. La fonction `dir` permet de voir le contenu du module.
Normalement tous les modules sont importés au début d'un programme.

```{codeplay}
import math

print(dir(math))
````

**Exercice :** importez le module `random` et affichez son contenu avec `dir`.

Pour utiliser une fonction du module importé, il faut faire précéder le nom de la fonction par le nom du module, séparé d'un point.

```{codeplay}
import math


print('e =', math.e)
print('pi =', math.pi)
print('fact(7) =', math.factorial(7))
````

**Exercice :** utilisez la fonction `pow` (puissance) et affichez le résultat.

## Module `math`

On retrouve dans le module `math` des fonctions ainsi que des constantes :

- arithmétiques,
- logarithmiques et exponentielles,
- trigonométriques.

Voici quelques utilisations du module `math` avec des fonctions trigonométriques.

![trigonometry](trigo.gif)

```{codeplay}
from math import asin, acos, atan, degrees

opp = 3
adj = 4
hyp = 5

print(degrees(asin(opp/hyp)))
print(degrees(acos(adj/hyp)))
print(degrees(atan(opp/adj)))
```

Dans cet exemple, on importe les fonctions `asin`, `acos`, `atan` et `degrees` du module `math`. Les trois premières renvoient un angle en radian et la dernière permet de convertir radian en degré.

## Module `random`

Le module `random` permet de créer des nombres pseudo-aléatoires.

La fonction `random()` retourne un nombre aléatoire dans l'intervalle [0, 1].

```{codeplay}
from random import random
    
for i in range(3):
    print(random())
```

La fonction `randint(a, b)` retourne un entier aléatoire dans l'intervalle [a, b].

```{codeplay}
from random import randint
    
print('randint - random integer')
for i in range(15):
    print(randint(0, 9), end=' ')
```

La fonction `choice(liste)` retourne un élément aléatoire de la liste.

```{codeplay}
from random import choice

for i in range(5):
    c = choice(['gagné', 'perdu', 'match nul'])
    print(c)
```

## Module `turtle`

Le module `turtle` permet de déplacer une tortue virtuelle sur un écran en lui donnant des commandes pour se déplacer.
En se déplaçant elle dessine une trace :

- la fonction `forward(200)` fait avancer la tortue de 200 pixels,
- la fonction `left(90)` fait tourner la tortue de 90 degrés vers la gauche.

```{codeplay}
from turtle import *

forward(200)
left(90)
forward(100)
```

La tortue connait aussi les commandes :

- `backward()` pour faire reculer la tortue,
- `right()` pour la faire tourner vers la droite.

Ceci dessine un pentagone.

```{codeplay}
from turtle import *

n = 5
for i in range(n):
    forward(100)
    left(360/n) 
```

**Exercice :** dessinez un hexagone, changez la taille.

```{codeplay}
from turtle import *
from math import atan2, degrees, sqrt

a = 200
b = 100
c = sqrt(a*a + b*b)
alpha = degrees(atan2(a, b))

forward(a)
left(90)
forward(b)
left(180 - alpha)
forward(c)
```

**Exercice :** modifiez a et b. Affichez a, b et c avec la fonction `write()` au milieu du segment.

Il est possible de personnaliser le pinceau et l'apparence du curseur ou de choisir si le pinceau est en train d'écrire ou s'il est relevé.
Plus d'infos sous [Python - Tortue graphique](https://docs.python.org/fr/3/library/turtle.html#module-turtle).

## Dessiner

Le module `turtle` présente une façon sympathique pour faire des dessins.
On s'imagine une tortue qui se déplace dans un rectangle et laisse une trace.

Elle peut se déplacer avec les 4 fonctions:

- `forward()` pour avancer,
- `back()` pour reculer,
- `left()` pour tourner à gauche,
- `right()` pour tourner à droite.

Au début elle se trouve au centre d'une zone rectangulaire.
Ce rectangle a les propriétés suivants:

- l'origine (0, 0) se trouve au centre,
- l'axe x s'étend de -300 à +300,
- l'axe y s'étend de -200 à +200.

Voici comment dessiner un carré.

```{codeplay}
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

Si nous regardons le code de près, nous remarquons que 2 lignes de code sont répétées 4 fois.
Nous pouvons utiliser une boucle `for` et réduire le code de 8 à 3 lignes.

```{codeplay}
from turtle import *

for i in range(4):
    forward(100)
    left(90)
```

Dessiner un carré est assez utile. C'est une forme qu'on pourrait réutiliser certainement.
Il serait pratique de définir un nom pour ces 3 lignes de code.
Avec le mot-clé `def` nous pouvons définir une nouvelle commande que nous allons appeler `square()`.
On appelle cette façon de faire **définir** une fonction.

Ensuite il suffit d'écrire `square()`pour dessiner le carré. On appelle ceci **appeler** une fonction.
Rappelez vous ceci:

- on définit une fonction une seule fois,
- on peut appeler une fonction autant de fois qu'on veut.

De nouveau nous réduisons les lignes de code nécessaires.
Au lieu d'écrire 3 lignes, nous n'écrivons qu'une seule ligne de code.

```{codeplay}
from turtle import *

def square():
    for i in range(4):
        forward(100)
        left(90)
        
square()
```

Que se passe-t-il si nous tournons de 90° et recommençons à dessiner un carré ?

```{codeplay}
from turtle import *

def square():
    for i in range(4):
        forward(100)
        left(90)
        
square()
left(90)
square()
left(90)
square()
left(90)
```

De nouveau nous avons répété 3 fois la même séquence de 2 lignes.
Nous pensons toute suite à la boucle `for`.
Que se passe t'il si nous dessinons des carrés et tournons de 45° à chaque tour ?

```{codeplay}
from turtle import *

def square():
    for i in range(4):
        forward(100)
        left(90)

for i in range(8):
    square()
    left(45)
```

Que se passe-t-il si nous dessinons une ligne (`forward/back`) et tournons d'un petit angle à chaque fois?

```{codeplay}
from turtle import *

for i in range(36):
    forward(100)
    back(100)
    left(10)
```

Une autre façon serait de toujours avancer, mais tourner à chaque fois d'un angle un peu plus petit que 180°.
Essayons !

```{codeplay}
from turtle import *

back(150)
for i in range(9):
    forward(300)
    left(160)
```

Jusqu'à maintenant notre carré a toujours la même taille.
Il serait bien si notre nouvelle commande `square()` pouvait dessiner des carrés de taille variable.
C'est possible en spécifiant un argument pour la fonction.
L'argument de la fonction est une valeur (variable locale) qui est passée à la fonction quand elle est appelée.

```{codeplay}
from turtle import *

def square(a):
    for i in range(4):
        forward(a)
        left(90)
        
square(30)
square(60)
square(90)
```

De nouveaux nous constatons une suite de nombres `30, 60, 90, ...`.
Nous pouvons utiliser une boucle avec une plage `range(start, end, increment)`.

```{codeplay}
from turtle import *

def square(a):
    for i in range(4):
        forward(a)
        left(90)
      
for x in range(30, 180, 30):
    square(x)
```

Au lieu d'imbriquer les carrés, nous pouvons aussi les dessiner les uns après les autres.
Le terme technique est de les **juxtaposer**.

```{codeplay}
from turtle import *

def square(a):
    for i in range(4):
        forward(a)
        left(90)
        
back(200)
for x in range(30, 180, 30):
    square(x)
    forward(x)
```

Maintenant nous sommes prêts pour définir une deuxième fonction que nous appelons `triangle()`.
Dessinés ensemble avec `square()`, nous obtenons une petite maisonnette.

```{codeplay}
from turtle import *

def square(a):
    for i in range(4):
        forward(a)
        right(90)
        
def triangle(a):
    for i in range(3):
        forward(a)
        left(120)
        
square(100)
triangle(100)
```

Donc nous décidons de définir une troisième fonction `house()` pour dessiner une maisonnette.

```{codeplay}
from turtle import *

def square(a):
    for i in range(4):
        forward(a)
        right(90)
        
def triangle(a):
    for i in range(3):
        forward(a)
        left(120)
    
def house(a):
    square(a)
    triangle(a)
    forward(a)
    
back(200)
house(100)
house(110)
house(120)
```

Si nous déformons les angles d'un carré, nous obtenons un losange (`diamond`).
Quelle forme obtenons-nous en dessinant un carré et deux losanges ?

```{codeplay}
from turtle import *

def square(a):
    for i in range(4):
        right(90)
        forward(a)

def diamond(a):
    for i in range(2):
        forward(a)
        left(120)
        forward(a)
        left(60)
        
square(100)
right(90)
diamond(100)
left(120)
diamond(100)
```

Si nous dessinons le losange 6 fois, nous obtenons une jolie fleur.

```{codeplay}
from turtle import *

def diamond(a):
    for i in range(2):
        forward(a)
        left(60)
        forward(a)
        left(120)

for i in range(6):
    diamond(100)
    left(60)
```

## Polygone

Un polygone régulier est une forme géométrique où tous les côtés ont même longueur et tous les angles sont identiques.

```{codeplay}
from turtle import *

def polygon(n, a):
    for i in range(n):
        forward(a)
        dot(8)
        left(360/n)
        
polygon(3, 100)
polygon(4, 100)
polygon(5, 100)
polygon(6, 100)
```

Pour dessiner des formes qui ne sont pas connectées par une ligne, nous utilisons les deux fonctions :

- `up()` pour lever le stylo,
- `down()` pour baisser le stylo.

```{codeplay}
from turtle import *

def polygon(n, a):
    for i in range(n):
        forward(a)
        dot(8)
        left(360/n)

up()
back(200)

for i in range(3, 7):
    down()
    polygon(i, 60)
    up()
    forward(120)
```

## Couleur

Avec la fonction `fill_color()` nous pouvons définir une couleur de remplissage.
Pour remplir une forme avec une couleur, nous devons ajouter les deux fonctions :

- `begin_fill()` au début de la forme,
- `end_fill()` à la fin de la forme.

```{codeplay}
from turtle import *

fillcolor('yellow')
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()
```

La forme ne doit pas nécessairement être fermée pour être remplie d'une couleur.
Dans l'exemple suivant nous dessinons une forme ouverte avec seulement deux lignes.
Le résultat est un triangle.

```{codeplay}
from turtle import *

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

Comme avant nous allons définir une fonction `square()`.
Cette fois elle a deux arguments :
- `a` pour la taille du carré,
- `color` pour la couleur du carré.

```{codeplay}
from turtle import *

def square(a, color):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(a)
        left(90)
    end_fill()
    forward(a)

back(100)
square(100, 'yellow')
square(100, 'orange')
square(100, 'red')
```
Voici une liste des couleurs disponibles.

![couleurs](colors.png)

Pour dessiner de multiples couleurs, nous pouvons définir une liste de couleurs et itérer sur cette liste.

```{codeplay}
from turtle import *

def square(a, color):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(a)
        left(90)
    end_fill()
    forward(a)

colors = ['blue', 'cyan', 'red', 'magenta', 'pink', 'lime', 'yellow']

back(200)
for color in colors:
    square(50, color)
```

Nous pouvons aussi utiliser une entrée interactive avec la fonction `input()`
et demander à l'utilisateur d'entrer une couleur valide.

```{codeplay}
from turtle import *

def square(a, color):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(a)
        left(90)
    end_fill()
    forward(a)

back(200)
color = input('Enter a color: ')
while color:
    square(100, color)
    color = input('Enter a color: ')
```

De nouveaux nous définissons une fonction `line()` pour dessiner une liste de couleurs.
En fin de liste, la tortue est placée à la position prête pour dessiner la ligne suivante.

```{codeplay}
from turtle import *

def square(a, color):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(a)
        left(90)
    end_fill()
    forward(a)

a = 50

def line(colors):
    for color in colors:
        square(a, color)
    back(len(colors) * a)
    up()
    sety(ycor() - a)
    down()

back(2 * a)
line(['black', 'yellow', 'yellow', 'black'])
line(['white', 'red', 'yellow', 'white'])
line(['yellow', 'yellow', 'yellow', 'yellow'])
line(['yellow', 'yellow', 'yellow', 'white'])
```

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```

## Objets
Quelles sont toutes les fonctions que nous importons avec le module `turtle` ?
La fonction `dir()` retourne une liste avec tous les noms de fonctions et classes qui appartiennent au module.

```{codeplay}
import turtle
print(dir(turtle))
```


```{codeplay}

```

## Epaisseur de ligne

La fonction `width()` permet de spécifier l'épaisseur de ligne.

```{codeplay}
from turtle import *

for i in range(10):
    forward(50)
    write(i, font=('Arial', 12))
    width(i)
    left(36)
```
## Ajouter un texte

La fonction `write()` permet d'afficher du texte.

```{codeplay}
from turtle import *

left(90)
write('default text size')

fillcolor('red')
forward(30)
write('Courier 24', font=('Courier', 24))

fillcolor('blue')
forward(30)
write('Arial 36', font=('Arial', 36))
```

```{codeplay}

```

## Exercices

````{admonition} Exercice 1 : Pythagore (toujours...) 🔌
:class: note
<!-- <span style="color:green">Niveau débutant</span> 🔌 -->

Faites un programme permettant de retourner la valeur en degré d'un des angles quelconques d'un triangle rectangle.

Le programme doit demander à l'utilisateur les longueurs des côtés opposé et adjacent par rapport à l'angle à calculer, ainsi que de l'hypoténuse. Avec ces informations, le programme doit retourner la valeur de l'angle en degrés.
````

````{admonition} Exercice 2 : jeu 🔌
:class: note
<!-- <span style="color:orange">Niveau intermédiaire</span> 🔌 -->

Faites un programme contre lequel on peut jouer à feuille-cailloux-ciseaux.

Le programme doit demander à l'utilisateur de faire son choix parmi les trois possibilités. Si l'utilisateur fait un choix qui n'existe pas, le programme retourne une information et repose la question. L'ordinateur doit faire un choix aléatoire. Le programme doit confronter le choix de l'utilisateur et celui de l'ordinateur puis retourner une information sur le gagnant du jeu.

Ce programme peut être amélioré en mettant en œuvre un système de score, de manches ou multi-joueurs.
````

````{admonition} Exercice 3 : étoile 🔌
:class: note
<!-- <span style="color:red">Niveau avancé</span> 🔌 -->

Dessinez une étoile avec la tortue.
````

````{admonition} Exercice 4 : maison 🔌
:class: note
<!-- <span style="color:red">Niveau avancé</span> 🔌 -->

Dessinez une maison comprenant une porte et une fenêtre avec la tortue.
````
