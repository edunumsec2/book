# Modules

Lorsque vous créez multiples programmes dans un domaine similiare, il est for probable que vous pourriez réutiliser des parties de code. Il serait donc plus éfficace de placer ce code d'utilité générale dans un endroit spécifique.

Un **module** est un ou plusieurs fichiers en Python que vous pouvez importer au début de votre programme.
Ce sont des scripts, contenant un ensemble de définitions — typiquement des fonctions, mais aussi des variables ou constantes (comme pi du module `math`).

Python est accompagné d'une bibliothèque de modules standards, tel que

- `math`
- `random`
- `time`
- `turtle`

Pour d'autres module consultez l'[index des modules Python](Vous trouvez l'index des modules ici: <)https://docs.python.org/3/py-modindex.html).

## Importer un module

Le mot-clé `import` permet d'importer un module. La fonction `dir` permet de voir le contenu du module.
Normalement toutes les modules sont importé au début d'un programme.

```{codeplay}
import math

print(dir(math))
````

**Exercice:** Importe le module `random` et affiche son contenu avec `dir`.

Pour utiliser une fonction du module importé, il faut précéder le nom de la fonction par le nom du module, séparé par un point.

```{codeplay}
import math


print('e =', math.e)
print('pi =', math.pi)
print('fact(7) =', math.factorial(7))
````

**Exercice:** Utilisez la fonction `pow` (puissance) et affichez le résultat.

## Module `math`

On retrouve dans le module `math` des <span commented>fonctions</span><!-- REVIEW/JPP: ainsi que des constantes -->

- arithmétiques
- logarithmiques et exponentielles
- trigonométriques

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

Dans cet exemple on importe les fonction `asin`, `acos`, `atan` et `degrees` du module `math`. Les 3 premières renvoient un angle en radian et la dernière permet de convertir radian en degré.

## Module `random`

Le module `random` permet de créer des nombres pseudo-aléatoires.

La fonction `random()` retourne un nombre aléatoire dans l'intervalle [0, 1].

```{codeplay}
from random import random
    
for i in range(3):
    print(random())
```

La fonction `randint(a, b)` retourne un entier aléatoire dans l'interval [a, b].

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
En se déplaçant elle dessine une trace.

- la fonction `forward(200)` fait avancer la tortue de 200 pixels,
- la fonction `left(90)` fait tourner la tortue de 90 degrés vers la gauche

```{codeplay}
from turtle import *

forward(200)
left(90)
forward(100)
```

La tortue connait aussi les commandes:

- `backward()` pour faire reculer la tortue, et
- `right()` pour la faire tourner vers la droite.

Ceci dessine un pentagone.

```{codeplay}
from turtle import *

n = 5
for i in range(n):
    forward(100)
    left(360/n) 
```

**Exercice:** Déssinez un héxagone, changez la taille.

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

**Exercice:** Modifiez a et b. Affichez a, b, et c avec la fonction `write()` au milieu du segment.

Il est possible de personnaliser le pinceau et l'apparence du curseur ou de choisir si le pinceau est en train d'écrire ou s'il est relevé.
Vous trouvez plus d'infos sous [Python - Tortue graphique](https://docs.python.org/fr/3/library/turtle.html#module-turtle).

## Exercices

### Exercice 1 - Pythagore

Faites un programme permettant de retourner la taille de l'angle en degrés d'un triangle rectangle.

Le programme doit demander à l'utilisateur les longueurs des côtés opposé et adjacent par rapport à l'angle à calculer ainsi que de l'hypoténuse. Si l'utilisateur ne connait pas la longueur d'un côté, il doit inscrire un **x** comme longueur du côté manquant. Avec ces informations, le programme doit retourner la taille de l'angle en degrés.

### Exercice 2 - Jeu

Faites un programme contre lequel on peut jouer à feuille-cailloux-ciseaux.

Le programme doit demander à l'utilisateur de faire son choix parmi les 3 possibilités. Si l'utilisateur fait un choix qui n'existe pas, retourner une information et reposer la question. L'ordinateur doit faire un choix aléatoire. Le programme doit confronter le choix de l'utilisateur et celui de l'ordinateur puis retourner une information sur le gagnant du jeu.

Ce programme peut être amélioré en mettant en œuvre un système de score, de manches ou multi-joueurs.

### Exercice 3 - Etoile

Dessinez une étoile avec la tortue.

### Exercice 4 - Maison

Dessinez une maison avec une porte et une fenêtre avec la tortue
