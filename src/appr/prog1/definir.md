(prog1.definir)=

# Définir - `def`

Dans ce chapitre, nous allons découvrir comment augmenter le vocabulaire de notre langage de programmation en définissant de nouvelles instructions, qu'on appelle aussi **fonction**. Ceci permet de rendre un code plus compact, mais surtout plus lisible. Nous allons voir que :

- le mot-clé `def` permet de nommer (définir) une séquence,
- le bloc qui suit doit être en **indentation** (décalé à droite),
- les fonctions `up()/down()` permettent de lever et baisser le stylo.

```{question}
Une fonction permet de

{v}`donner un nom à une séquence`  
{f}`nous dire si ça fonctionne`  
{v}`augmenter le vocabulaire du langage de programmation`  
{v}`rendre un programme plus lisible`
```

## Nommer une séquence

Dessiner un rectangle est assez utile. C'est une forme qu'on pourra réutiliser certainement souvent. Il serait pratique de définir un nom pour ces 8 lignes de code. Pouvons-nous définir de nouvelles commandes ?

```python
forward(160)
left(90)
forward(100)
left(90)
forward(160)
left(90)
forward(100)
left(90)
```

Oui, c'est possible. Avec le mot-clé `def`, nous pouvons définir une nouvelle commande que nous pouvons par exemple appeler `rectangle()`.
Cette façon de créer un raccourci est appelée **définir** une fonction.
Le code à exécuter suit l'expression `def rectangle():` et se trouve en **indentation** (décalé vers la droite).

Ensuite, il suffit d'écrire `rectangle()` pour dessiner un rectangle. On appelle ceci **appeler** une fonction.
Rappelez-vous ceci :

- on définit une fonction une seule fois,
- on appelle une fonction autant de fois que l'on veut,
- si on ne l'appelle pas, elle n'est pas exécutée et il ne se passe rien.

Définir une fonction nous permet de réduire le nombre de lignes de code nécessaires.
Chaque fois que nous utilisons `rectangle()`,
au lieu d'écrire 8 lignes, nous écrivons seulement une ligne de code.

```{exercise}
Dessinez encore d'autres rectangles en appelant la nouvelle fonction `rectangle()`.
```

```{codeplay}
:file: def1.py
from turtle import *

def rectangle():
    forward(160)
    left(90)
    forward(100)
    left(90)
    forward(160)
    left(90)
    forward(100)
    left(90)
        
rectangle()
left(90)
rectangle()
```

```{question}
Une **indentation** de texte est 

{f}`un décalage vers la gauche`  
{v}`un décalage vers la droite`  
{f}`une mise en paragraphe`  
{f}`une mise en sous-section`  
```

## Donner du sens

Une fonction ne permet pas seulement d'économiser des lignes de code.
Elle permet aussi de structurer le code et de lui donner un sens. Considérez par exemple le code ci-dessous. Il est presque impossible de comprendre ce que fait le programme en regardant les 17 lignes de code.

```{codeplay}
:file: def2.py
from turtle import *

forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(30)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
left(90)
```

Si nous observons la tortue, nous comprenons finalement qu'elle dessine deux fois un rectangle. Nous pouvons même interpréter cette image et donner le sens de bâtiment au premier rectangle, et de porte au second.

Essayons maintenant de découper le code en **sous-programmes** en utilisant deux fonctions `batiment()` et `porte()`.
En regardant ces 3 lignes de code, on comprend immédiatement le sens du programme.

``` python
batiment()
forward(30)     # repositionner la tortue
porte()
```

La définition d'une fonction permet d'ajouter de nouveaux mots à un langage de programmation. Contrairement aux commandes natives de Python qui sont toutes en anglais, nous sommes libres de les choisir en français.

**Attention** : écrivez les fonctions sans accents et sans circonflexes : `batiment()`, `carre()`, `boite()`.

```{exercise}
Ajoutez une deuxième porte au bâtiment. Ensuite, faites-en une porte double.
````

```{codeplay}
:file: def3.py
from turtle import *

def batiment():
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    left(90)

def porte():
    forward(30)
    left(90)
    forward(50)
    left(90)
    forward(30)
    left(90)
    forward(50)
    left(90)

batiment()
forward(30)
porte()
```

```{question}
À combien de lignes de code la fonction `porte()` est-elle équivalente ?

{f}`1 ligne`  
{f}`2 lignes`  
{v}`8 lignes`  
{f}`17 lignes`  
```

## Définir une fonction

Le fait de donner un nom à une séquence d'instructions est appelé **définir une fonction**. Une **définition de fonction** comporte :

1. le mot-clé `def` (définir),
1. le nom de la fonction (`batiment/porte`),
1. les parenthèses `()`,
1. le deux-points `:`,
1. un bloc en indentation.

Qu'est-ce qu'un bloc en indentation ?
C'est un bloc de texte qui comporte des espaces vides à gauche. En Python, ces espaces apparaissent en multiples de 4.

L'indentation est très importante en Python. C'est l'indentation qui indique l'étendue des instructions qui font partie de la fonction.

```{question}
Parmi les 4 définitions de fonction ci-dessous, laquelle est correcte ?

{f}`def() rectangle:`  
{f}`def: rectangle`  
{v}`def rectangle():`  
{f}`def(rectangle):`  
```

## Indenter avec un raccourci

Comme l'indentation est tellement importante en Python, il en existe un raccourci.
Il faut d'abord sélectionner les lignes de code dont vous voulez changer l'indentation.
Ensuite, vous appuyez sur :

- la touche **tab** pour augmenter l'indentation
- la touche **maj+tab** pour diminuer l'indentation

```{exercise}
Essayez ces raccourcis dans le code ci-dessous. Transformez le code en deux fonctions `batiment()` et `porte()`, que vous appelez ensuite.
```

```{codeplay}
:file: def2.py
from turtle import *

forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(30)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(50)
left(90)
```

Voici encore un raccourci très utile : **cmd+Enter** pour exécuter le code.

## Maison avec porte

Une fois qu'une fonction est définie, elle peut être utilisée partout, même dans la définition d'une autre fonction.

Ici, nous avons une fonction `porte()`, qui est utilisée à l'intérieur d'une deuxième fonction `maison()`. Pour que ceci soit possible, la définition de porte doit être placée avant la définition de `maison()`.

```{exercise}
Déplacez la porte vers le milieu de la maison, et dessinez une deuxième maison.
```

```{codeplay}
:file: def4.py
from turtle import *

def porte():
    forward(20)
    left(90)
    forward(40)
    left(90)
    forward(20)
    left(90)
    forward(40)
    left(90)

def maison():
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
    porte()

maison()
```

## Variable globale

Une variable est le concept d'associer un **nom symbolique** à une valeur.

Avant de pouvoir utiliser une variable, elle doit être créée.
On appelle ce processus une **affectation** et on dit qu'on associe une valeur à une variable.
La forme générale est `var = valeur` ou `var` est le nom de la variable et `valeur` est sa valeur.
Attention, ceci n'est pas une égalité au sens mathématique.

Dans le programme chaque instance de `d` est remplacée par 80. La commande `forward(d)` va donc prendre le sens de `forward(80)` et faire avancer la tortue de 80 pas.

```{exercise}
Modifiez la valeur de la variable globale `d` et exécutez le programme.
```

```{codeplay}
from turtle import *

d = 80      # variable globale (d = distance)

def triangle():
    forward(d)
    left(120)
    forward(d)
    left(120)
    forward(d)

triangle()
triangle()
triangle()
```

Une variable globale apparait au début du programme et sert à configurer une propriété générale d'un programme. Ici nous choisissons une variable globale `d` pour indiquer une **distance** de base.
Cette distance est utilisée pour pouvoir dessiner des formes d'une hauteur standard.

```{caution}
Utilisez les variables globales avec beaucoup de modération !
```

## Le point `dot()`

La fonction `dot()` dessine un point à la position actuelle de la tortue.

```{exercise}
Ajoutez un point (`dot`) au sommet du triangle.
```

```{codeplay}
from turtle import *

d = 100      # variable globale (d = distance)

def triangle():
    dot()
    forward(d)
    left(120)
    dot()
    forward(d)
    left(120)
    forward(d)

triangle()
```

## Lever le stylo

Les deux commandes `up()` et `down()` permettent de lever et de baisser le stylo.
Ceci nous permet de dessiner des formes séparées, comme ici le petit i avec son point.

```{exercise}
Transformez le i vers un i avec trema (deux points).
```

```{codeplay}
from turtle import *
d = 50

def i():
    dot()
    down()      # poser le stylo
    left(90)
    forward(d)
    up()        # lever le stylo
    forward(d)
    dot()
    backward(2*d)
    right(90)
    forward(d/2)    # avancer à la prochaine lettre
    
i()
i()
```

```{caution}
Contrairement aux fonctions `forward(d)` et `backward(d)` qui nécessitent un argument, les fonctions `up()` et `down()` ne nécessitent pas d'argument.
```

## Dessiner des lettres

Voici quelques astuces pour dessiner des lettres:

- Basez la dimension de chaque lettre sur la variable `d`. Ceci permet de choisir la taille des lettres.
- Marquez le point de départ avec un point (dot).
- Posez le stylo au début de chaque lettre (down), levez-le à la fin (up).

- À la fin, avancez la tortue à la position de la prochaine lettre.

```{codeplay}
from turtle import *
d = 50

def h():
    dot()
    down()
    left(90)
    forward(2*d)
    backward(d)
    right(90)
    forward(d)
    right(90)
    forward(d)
    left(90)
    up()
    forward(d/2)

def i():
    dot()
    down()
    left(90)
    forward(d)
    up()
    forward(d)
    dot()
    backward(2*d)
    right(90)
    forward(d/2)

h()
i()
h()
i()
```

## Trouver des motifs

Une stratégie importante dans la programmation est de **reconnaître des structures identiques**. Par exemple, quand vous voyez un motif répété dans un dessin, vous devez repérer la partie qui est répétée et en créer une fonction.

La fonction `bras()` dessine les 3 côtés d'un carré et tourne, à la fin, dans le sens approprié pour la suite.
Ensuite, il suffit d'**appeler** 4 fois cette fonction pour dessiner une croix.
En appelant la fonction `bras()`, au lieu d'écrire 6 lignes, nous n'écrivons qu'une ligne de code.

```{exercise}
Allongez le bras de la croix à `2*d`, et diminuez sa largeur à `d/2` pour en faire une croix plus mince.
```

```{codeplay}
:file: def8.py
from turtle import *
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

croix()
```

## Exercices

- Téléchargez un exercice.
- Ouvrez-le dans un éditeur externe (tel que Thonny).
- Mettez votre prénom, nom et classe.
- Basez vos dimensions sur la variable globale `d`
- Remplacez `...` par votre code.
- Déposez votre exercice sur Moodle (ou plateforme équivalente).

### Rectangles

Définissez une fonction pour dessiner un rectangle.
Ensuite, dessinez 3 rectangles qui ne se touchent pas, à des endroits différents.

```{codeplay}
:file: rectangles.py
from turtle import *
# Prénom Nom, classe
d = 100

def rectangle():
    ...

rectangle()
...
done()
```

### Maisons

Définissez une fonction pour dessiner une maison.
Ensuite, dessinez 3 maisons qui ne sont pas connectées, à des endroits différents.

```{codeplay}
:file: maisons.py
from turtle import *
# Prénom Nom, classe
d = 100

def maison():
    ...


maison()
...
done()
```

### Meubles

Définissez 3 fonctions pour dessiner une chaise, une table et un lit.
Ensuite placez plusieurs meubles dans l'espace

```{codeplay}
:file: chaises.py
from turtle import *
# Prénom Nom, classe
d = 100

def chaise():
    ...

def table():
    ...

def lit():
    ...

chaise()
table()
lit()
...
done()
```

### ABC

Définissez une fonction pour chaque lettre de l'alphabet.
Ensuite, ecrivez votre nom.

```{codeplay}
:file: abc.py
from turtle import *
# Prénom Nom, classe
d = 30

def A():
    dot()
    down()
    left(70)        # demi-montée
    forward(d)
    right(70)
    forward(0.6*d)  # trait du milieu
    backward(0.6*d)
    left(70)
    forward(d)      # partie haute
    right(140)
    forward(2*d)    # descente
    left(70)
    up()
    forward(d/2)    # avancer à la prochaine lettre

A()
A()
...
done()
```

### Tetris

Le jeu vidéo [Tetris](https://fr.wikipedia.org/wiki/Tetris) est un puzzle conçu par l'informaticien russe Alekseï Pajitnov en 1984.
Tetris met le joueur au défi de réaliser des lignes complètes en déplaçant des pièces de formes différentes, les [tétrominos](https://fr.wikipedia.org/wiki/Tétromino), qui défilent du haut jusqu'au bas de l'écran.

```{image} media/tetris.png
```

Les carrés de base d'un tétromino mesurent 20 × 20 pixels. Il y en a 7 formes différentes, qui sont nommées d'après les lettres auxquelles elles ressemblent :

- Z
- L
- O (carré)
- S
- I (bâton)
- J
- T

Basez les dimensions de vos tétronimos sur la variable globale `d`.

```{codeplay}
:file: tetris.py
from turtle import *
# Prénom Nom, classe
d = 20

def Z():
    down()
    dot()
    forward(2*d)
    left(90)
    forward(d)
    left(90)
    forward(d)
    right(90)
    forward(d)
    left(90)
    forward(2*d)
    left(90)
    forward(d)
    left(90)
    forward(d)
    right(90)
    forward(d)
    left(90)
    up()

def L():
    ...
def O():
    ...
def S():
    ...
def I():
    ...
def J():
    ...
def T():
    ...

up()
back(12*d)
Z()
forward(3*d)
O()
...
done()
```

### TP

Créez une fonction pour dessiner chaque lettre de l'alphabet. 
La taille de chaque lettre doit être basé sur la variable global `d` qui exprime la dimension (hauteur) d'une lettre. Créez une fonction `ABC()` qui affiche chaque lettre de l'alphabet. Ensuite créez une nouvelle fonction `prenom()` pour écrire votre nom.

Pour démontrer que les expressions basées sur `d` sont corrects, affichez les lettres et votre nom avec deux tailles différents.

Pour sauvegarder votre image vers un fichier EPS (image vectorielle) vous devez enlever les commentaires de ces deux lignes de code.

``` python
# from tkinter import *
# Screen().getcanvas().postscript(file='tp2.eps')
```

```{codeplay}
"""
tp2 - définir

Nom : 
Classe :
Date :

- nommez ce fichier : tp2_classe_prenom (minuscules, sans accents)
- créez des fonctions pour les lettres de l'abc
- créer une fonction pour écrire votre nom
- récrivez l'abc et votre nom une deuxième fois plus petit    
- déposez sur Moodle :
    tp2_classe_prenom.py     (code)
    tp2_classe_prenom.eps    (image vectorielle)
    tp2_classe_preneom.jpg   (image)
"""
from turtle import *
# from tkinter import *

d = 30

def A():
    dot()
    down()
    left(70)        # demi-montée
    forward(d)
    right(70)
    forward(0.6*d)  # trait du milieu
    backward(0.6*d)
    left(70)
    forward(d)      # partie haute
    right(140)
    forward(2*d)    # descente
    left(70)
    up()
    forward(d/2)    # avancer à la prochaine lettre


def ABC():
    A()
    A()
    A()
    
def prenom():
    ...

# afficher l'ABC et votre prénom
backward(280)
ABC()
prenom()

# afficher l'ABC et votre prénom avec une autre taille
d = 10
forward(100)
ABC()
prenom()

# Screen().getcanvas().postscript(file='tp2.eps')
done()
```
