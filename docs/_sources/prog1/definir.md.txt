(prog1.definir)=
# Définir - `def`

Dans ce chapitre, nous allons découvrir comment augmenter le vocabulaire de notre langage de programmation en définissant de nouvelles instructions. Ceci permet de rendre un code plus compact, mais surtout plus lisible. Nous allons voir que :

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
<!--  -->
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

```{admonition} Exercice
:class: note
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

```{admonition} Exercice
:class: note
Ajoutez une deuxième porte au bâtiment.
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

## Raccourci

Comme l'indentation est tellement importante en Python, il en existe un raccourci.
Il faut d'abord sélectionner les lignes de code dont vous voulez changer l'indentation.
Ensuite, vous appuyez sur :

- la touche **tab** pour augmenter l'indentation
- la touche **maj+tab** pour diminuer l'indentation

```{admonition} Exercice
:class: note
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

```{admonition} Exercice
:class: note
Mettez la porte au milieu de la maison, et dessinez une deuxième maison.
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

## Lever le stylo

Les deux commandes `up()` et `down()` permettent de lever et de baisser le stylo.
Ceci nous permet de dessiner des formes séparées, comme ces deux triangles, car nous nous déplaçons sans laisser de trait derrière nous lorsque le stylo est levé.

```{admonition} Exercice
:class: note
Ajoutez encore un triangle disjoint,  mais pas à la même hauteur.
```

```{codeplay}
:file: def6.py
from turtle import *

def triangle():
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)
    
triangle()
up()
forward(150)
down()
triangle()
```

```{caution}
Contrairement aux fonctions `forward(d)` et `backward(d)` qui nécessitent un argument, les fonctions `up()` et `down()` ne nécessitent pas d'argument.
```

## Maison avec fenêtre

Dans le programme ci-dessous, nous allons dessiner de nouveau une maison, mais avec une fenêtre cette fois-ci. Les fonctions `up()`/`down()` nous permettent de dessiner des formes disjointes, telles qu'une fenêtre à l'intérieur de la maison.

```{admonition} Exercice
:class: note
Modifiez le programme pour que la fenêtre soit dessinée à l'intérieur de la maison. Dessinez une deuxième maison.
```

```{codeplay}
:file: def7.py
from turtle import *

def fenetre():
    forward(20)
    left(90)
    forward(20)
    left(90)
    forward(20)
    left(90)
    forward(20)
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

    fenetre()

maison()
```

## Trouver des motifs

Une stratégie importante dans la programmation est de **reconnaître des structures identiques**. Par exemple, quand vous voyez un motif répété dans un dessin, vous devez repérer la partie qui est répétée et en créer une fonction.

La fonction `bras()` dessine les 3 côtés d'un carré et tourne, à la fin, dans le sens approprié pour la suite.
Ensuite, il suffit d'**appeler** 4 fois cette fonction pour dessiner une croix.
En appelant la fonction `bras()`, au lieu d'écrire 6 lignes, nous n'écrivons qu'une ligne de code.

```{admonition} Exercice
:class: note
Allongez le bras de la croix à 120 pixels, et diminuez son épaisseur à 30 pixels.
```

```{codeplay}
:file: def8.py
from turtle import *

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

croix()
```

## Décomposer

Une stratégie importante en programmation est de **décomposer un programme en sous-programmes**. Les fonctions nous permettent de structurer un problème en objets de plus en plus simples.

Ici, nous dessinons une fenêtre composée de 4 carreaux. Nous pouvons décomposer ce problème en une construction hiérarchique :

- la fonction `fenetre()` appelle quatre fois la fonction  `carreau()`,
- la fonction `carreau()` appelle deux fois la fonction `equerre()`,
- la fonction `equerre()` appelle deux fois la fonction `ligne()`.

```{codeplay}
:file: def9.py
from turtle import *

def ligne():
    forward(100)
    left(90)

def equerre():
    ligne()
    ligne()

def carreau():
    equerre()
    equerre()
    left(90)

def fenetre():
    carreau()
    carreau()
    carreau()
    carreau()

fenetre()
```

```{question}
Combien de lignes de code sont exécutées par la fonction `fenetre()`?

{f}`16`  
{f}`32`  
{v}`36`  
{f}`40`  
```

## Exercices

- Téléchargez un exercice.
- Ouvrez-le dans un éditeur externe (tel que Thonny).
- Mettez votre prénom, nom et classe.
- Remplacez `...` par votre code.
- Déposez votre exercice sur Moodle (ou plateforme équivalente).

### Rectangles

Définissez une fonction pour dessiner un rectangle.
Ensuite, dessinez 3 rectangles qui ne se touchent pas, à des endroits différents.

```{codeplay}
:file: rectangles.py
from turtle import *
# Prénom, nom, classe

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
# Prénom, nom, classe

def maison():
    ...


maison()
...
done()
```

### Chaises

Définissez une fonction pour dessiner une chaise.
Ensuite, dessinez 3 chaises à des endroits différents.

```{codeplay}
:file: chaises.py
from turtle import *
# Prénom, nom, classe

def chaise():
    ...

chaise()
...
done()
```

### Tables

Définissez une fonction pour dessiner une table.
Ensuite, dessinez 3 tables à des endroits différents.

```{codeplay}
:file: tables.py
from turtle import *
# Prénom, nom, classe

def table():
    ...

table()
...
done()
```

### Lits

Définissez une fonction pour dessiner un lit.
Ensuite, dessinez 3 lits à des endroits différents.

```{codeplay}
:file: lits.py
from turtle import *
# Prénom, nom, classe

def lit():
    ...

lit()
...
done()
```

### Tetris

Le jeu vidéo [Tetris](https://fr.wikipedia.org/wiki/Tetris) est un puzzle conçu par l'informaticien russe Alekseï Pajitnov en 1984.
Tetris met le joueur au défi de réaliser des lignes complètes en déplaçant des pièces de formes différentes, les [tétrominos](https://fr.wikipedia.org/wiki/Tétromino), qui défilent du haut jusqu'au bas de l'écran.

```{image} media/tetris.png
```

Les carrés de base d'un tétromino mesurent 20 × 20 pixels. Il y en a 7 formes différentes, qui sont nommées d'après les lettres auxquelles elles ressemblent :

- S
- L
- O (carré)
- Z
- I (bâton)
- J
- T

```{codeplay}
:file: tetris.py
from turtle import *
# Votre prénom, nom, classe
def I():
    down()
    forward(20)
    left(90)
    forward(80)
    left(90)
    forward(20)
    left(90)
    forward(80)
    left(90)
    up()

def O():
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

up()
back(250)
I()
forward(40)
O()
...
done()
```
