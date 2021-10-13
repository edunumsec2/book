# Modules

Lorsque vous créez multiples programmes dans un domaine similiare, il est for probable que vous pourriez réutiliser des parties de code. Il serait donc plus éfficace de placer ce code d'utilité générale dans un endroit spécifique. 

Un **module** est un ou plusieurs fichiers en Python que vous pouvez importer au début de votre programme.
Ce sont des scripts, contenant un ensemble de définitions — typiquement des fonctions, mais aussi des variables ou constantes (comme pi du module `math`).

Python est accompagné d'une bibliothèque de modules standards, tel que

- `math`
- `random`
- `time`
- `turtle`

Vous trouvez l'index des modules ici: https://docs.python.org/3/py-modindex.html

## Importer un module

Le mot-clé `import` permet d'importer un module. La fonction `dir` permet de voir le contenu du module. 
Normalement toutes les modules sont importé au début d'un programme.

```{codeplay}
import math

print(dir(math))
````

**Exericice:** Importe le module `random` et affiche son contenu avec `dir`.

Pour utiliser une fonction du module importé, il faut précéder le nom de la fonction par le nom du module, séparé par un point.

```{codeplay}
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

![](trigo.gif)

```{codeplay}
from math import asin, acos, atan, degrees

opp = 3
adj = 4
hyp = 5

print(degrees(asin(opp/hyp)))
print(degrees(acos(adj/hyp)))
print(degrees(atan(opp/adj))
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

Python peut être utilisé pour donner des ordres à un robot afin qu'il execute des tâches. Ceci demande une perception particulière de l'espace pour se mettre à la place du robot et ainsi détérminer où est la droite et la gauche en fonction des actions déjà executées. Le module `turtle` permet de reproduire cette logique en animant une tortue virtuelle.

```{codeplay}
from turtle import *

forward(100)
left(90)
forward(100)
```

La tortue peut faire différents déplacements: avancer, reculer, tourner à droite et tourner à gauche. 

Pour avancer, l'instruction s'appelle `forward`, elle est suivie du nombre de pixels entre parenthèses.

Pour reculer, l'instruction s'appelle `backward`, elle est suivie du nombre de pixels entre parenthèses.

Pour tourner à gauche, l'instruction s'appelle `left`, elle est suivie du nombre de degrés entre parenthèses.

Pour tourner à droite, l'instruction s'appelle `right`, elle est suivie du nombre de degrés entre parenthèses 

```{code-cell} ipython3
from turtle import *
forward(100)
```

Mettre un GIF

```{code-cell} ipython3
from turtle import *
backward(100)
```

Mettre un GIF

```{code-cell} ipython3
from turtle import *
left(90)
```

Mettre un GIF

```{code-cell} ipython3
from turtle import *
right(90)
```

Mettre un GIF

+++

Il est possible de personnaliser le pinceau et l'apparence du curseur ou de choisir si le pinceau est en train d'écrire ou s'il est relevé avec d'autres instructions que l'on peut retrouver via l'index des modules python cité au début de ce chapitre. 

+++

## Exercices

+++

### Ex1
Faites un programme permettant de retourner la taille de l'angle en degrés d'un triangle rectangle.

Le programme doit demander à l'utilisateur les longueurs des côtés opposé et adjacent par rapport à l'angle à calculer ainsi que de l'hypoténuse. Si l'utilisateur ne connait pas la longueur d'un côté, il doit inscrire un **x** comme longueur du côté manquant. Avec ces informations, le programme doit retourner la taille de l'angle en degrés.

+++

### Ex2
Faites un programme contre lequel on peut jouer à feuille-cailloux-ciseaux.

Le programme doit demander à l'utilisateur de faire son choix parmi les 3 possibiliés. Si l'utilisateur fait un choix qui n'existe pas, retourner une information et reposer la question. L'ordinateur doit faire un choix aléatoire. Le programme doit confronter le choix de l'utilisateur et celui de l'ordinateur puis retourner une information sur le gagnant du jeu.

Ce programme peut être amélioré en mettant en œuvre un système de score, de manches ou multijoueurs.

+++

### Ex3
Dessinez une étoile avec la tortue.

+++

### Ex4
Dessinez une maison avec une porte et une fenêtre avec la tortue

```{code-cell} ipython3

```
