---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Modules
<span commented>Les modules sont des fichiers</span><!-- REVIEW/JPP: On pourrait commencer par une petite motivation sur pourquoi les modules -->, aussi appelés scripts, contenant un ensemble de <span commented>déclarations de fonctions</span><!-- REVIEW/JPP: plus généralement, de définitions — typiquement des fonctions, mais aussi des variables/constantes comme pi de math -->. Lorsqu'on crée un programme, les modules ne sont pas importés d'office, ils sont stockés sur l'ordinateur lors de l'installation de Python et il faut les importer lorsqu'ils sont nécessaires.

+++

## Importer un module
Selon l'utilité qu'on en fait, y a plusieurs façons d'importer un module:

    from module import *
    from module import fonction
    import module
    import module as autre_nom

Selon la façon dont on a importé le module, la forme que l'on va donner aux fonctions est différente.
- Avec la première forme, il suffira d'appeler la fonction par son nom.
- Avec les autres formes, il sera nécessaire de précéder le nom de la fonction par <span commented>celui du module</span><!-- REVIEW/JPP: ce n'est pas vrai pour la 2e ligne -->

**Bonne pratique : Pourquoi ne pas simplement importer tout le module sans sélectionner de fonctions ?**

De manière générale, il ne faut pas faire `from module import *`. Ceci encombre l'espace de nommage de l'importateur et rend la détection de noms non définis beaucoup plus ardue pour les analyseurs de code.

Il est préférable d'importer les module au début d'un programme. Ceci permet d'afficher clairement de quels modules le code a besoin et évite de se demander <span commented>si le module est dans le contexte</span><!-- REVIEW/JPP: je ne comprends pas cette fin de phrase -->.

+++

## Module `math`
On retrouve dans le module `math` des <span commented>fonctions</span><!-- REVIEW/JPP: ainsi que des constantes --> 
- arithmétiques
- logarithmiques et exponentielles
- trigonométriques

Voici quelques utilisations du module `math`.

```{code-cell} ipython3
from math import pi

print(pi)
```

```{code-cell} ipython3
from math import asin, acos, atan, degrees

opp = 4
hyp = 5
adj = 3

a = asin(opp/hyp)
b = acos(adj/hyp)
c = atan(opp/adj)

print(degrees(a),degrees(b),degrees(c), sep='\n')
```

<span commented>Dans cet exemple</span><!-- REVIEW/JPP: ce serait bien d'éviter les arguments nommés et de simplement avoir 3 print ici pour éviter les complications non nécessaires --> on importe les fonction `asin`, `acos`, `atan` et `degrees` du module `math`. Les 3 premières renvoient un angle en radiant et la dernière permet de convertir les radiant en degrés. <span commented>Pour consulter toutes les fonction diponibles dans un module</span><!-- REVIEW/JPP: Ceci m'a l'air mieux en haut de page ou en bas de page, mais pas ici au milieu -->, la documentation de référence se trouve ici : https://docs.python.org/fr et **l'index des modules de Python** ici : https://docs.python.org/fr/3/py-modindex.html

+++

## Le module `random` 
Le module `random` permet d'utiliser des fonctions basées sur la génération de nombres aléatoire dans un programme. 

Exercice jeu de casino: la roulette 

```{code-cell} ipython3
from random import random, randrange, choice

a = random()

b = choice(['gagné', 'perdu', 'match nul'])

c = randrange(9)

d = randrange(20, 101, 5)

print(a,b,c,d,sep='\n')
```

Dans l'exemple ci-dessus, trois fonction sont importées du module `random`. La fonction `random` permet de générer un nombre aléatoire entre 0.0 et 1.0. La fonction `choice` permet de choisir aléatoirement un élément d'une liste. La fonction `randrange` peut être utilisée avec un ou trois arguments: Dans le premier cas, un nombre entier est généré aléatoirement entre 0 et l'argument et dans le deuxième cas, un nombre entier est généré aléatoirement entre le premier et le deuxième argument en respectant des pas définis par le troisième argument.

+++

## Turtle – dessin avec la tortue Python 

+++

Python peut être utilisé pour donner des ordres à un robot afin qu'il execute des tâches. Ceci demande une perception particulière de l'espace pour se mettre à la place du robot et ainsi détérminer où est la droite et la gauche en fonction des actions déjà executées. Le module `turtle` permet de reproduire cette logique en animant une tortue virtuelle.

```{code-cell} ipython3
from turtle import *
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
