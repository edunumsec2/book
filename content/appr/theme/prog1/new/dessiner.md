# Dessiner - `forward`

Dans ce chapitre nous explorons ce que c'est un programme et nous prenons
 la métaphore du dessin. Ici, un programme est une séquence d'instructions pour dessiner une image.

Allons-y en avant (forward) avec la programmation. Nous allons voir que :

- les instructions `forward()`, `back()`, `left()`, `right()` permettent de dessiner,
- le mot-clé `def` permet de nommer (définir) une séquence,
- la fonction `width()` permet de choisir l'épaisseur,
- les fonctions `up()/down()` permettent de lever et baisser le stylo.

```{question}
Un programme informatique est

{f}`une instruction de séquence`  
{v}`une séquence d'instructions`  
{f}`un algorithme`  
{f}`une recette de cuisine`
```

## Le module `turtle`

Dans le langage de programmation Python, le module `turtle` (tortue en anglais) présente une façon sympathique pour faire des dessins. C'est pour cela que nous commençons notre aventure de programmation avec cet animal qui avance tout doucement à son propre rythme à lui.

On s'imagine une tortue qui se déplace sur un canevas et laisse une trace.

Ci-dessus vous trouvez notre premier programme de trois ligne :

- dans la première ligne nous importons toutes (`*`) les fonctions du module `turtle`,
- avec `shape('turtle')` nous affichons une tortue (au lieu de la flèche),
- avec `forward(150)` nous faisons avancer la tortue de 150 pixels.

```{codeplay}
:file: forward1.py
from turtle import *

shape('turtle')
forward(150)
```

**Exercice** : Ajoutez d'autre fonctions tel que `back()`, `left()`, `right()` pour faire un dessin.

```{question}
En Python `turtle` est

{v}`un module standard`  
{f}`un éditeur de dessin`  
{f}`une tortue`  
{f}`une commande`
```

## La tortue

La tortue peut se déplacer et dessiner une trace avec les 4 fonctions:

- `forward(d)` pour avancer d'une distance `d` (en pixels)
- `back(d)` pour reculer
- `left(a)` pour tourner à gauche d'un angle `a` (en degrés)
- `right(a)` pour tourner à droite

Au début, la tortue se trouve au centre d'une zone rectangulaire.
Ce rectangle a les propriétés suivantes :

- l'origine (0, 0) se trouve au centre,
- l'axe x s'étend de -300 à +300,
- l'axe y s'étend de -200 à +200.

```{codeplay}
:file: forward2.py
from turtle import *

shape('turtle')

forward(300)
back(600)
forward(300)

left(90)
forward(200)
right(180)
forward(400)
```

```{question}
La largeur de la zone de dessin de la tortue est

{f}`200 pixels`   
{f}`400 pixels`  
{v}`600 pixels`  
{f}`800 pixels`  
```

## Une séquence

Un programme est une séquence d'instructions. Le bloc des 8 instructions ci-dessous indique comment dessiner un carré. La tortue doit avancer, tourner, avancer, tourner etc.

```{codeplay}
:file: forward3.py
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

**Exercice** : Modifiez ce code pour faire le rectangle plus long.

```{question}
La hauteur de la zone de dessin de la tortue est

{f}`200 pixels`   
{v}`400 pixels`  
{f}`600 pixels`  
{f}`800 pixels`  
```

## Redondance

La tortue possède 4 fonctions de déplacement, mais strictement parlé, on pourrait s'en sortir avec seulement deux fonctions, `forward()` et `left()`, car :

- `back(d)` est équivalent à `forward(-d)`
- `right(a)` est équivalent à `left(-a)`

En plus la rotation est cyclique,

```{codeplay}
:file: forward4.py
from turtle import *

forward(160)
left(90)
forward(100)
right(-90)
back(-160)
left(-270)
forward(100)
right(270)
```

```{question}
L'expression `left(90)` est équivalent à

{v}`right(-90)`  
{f}`right(180)`  
{f}`left(180)`  
{f}`left(270)`  
```

## Nommer une séquence

Dessiner un rectangle est assez utile. C'est une forme qu'on pourra réutiliser certainement souvent. Il serait pratique de définir un nom pour ces 8 lignes de code. Pouvons nous définir des nouvelles commandes ?

Oui, c'est possible. Avec le mot-clé `def` nous pouvons définir une nouvelle commande que nous pouvons par exemple appeler `rectangle()`.
Cette façon de créer un raccourci est appelé **définir** une fonction.

Ensuite il suffit d'écrire `rectangle()` pour dessiner un rectangle. On appelle ceci **appeler** une fonction.
Rappelez vous ceci:

- on définit une fonction une seule fois,
- on appelle une fonction autant de fois que l'on veut.

Définir une fonction nous permet de réduire les lignes de code nécessaire.
A chaque fois que nous utilisons `rectangle()`,
au lieu d'écrire 8 lignes, nous écrivons seulement 1 ligne de code.

```{codeplay}
:file: forward5.py
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

**Exercice** : Dessinez encore d'autres rectangles en appelant la nouvelle fonction `rectangle()`.

```{question}
L'expression `left(90)` est équivalent à

{f}`right(180)`  
{f}`left(180)`  
{f}`left(270)`  
{v}`right(270)`  
```

## Donner du sens

Une fonction ne permet pas seulement d'économiser des lignes de code.
Elle permet aussi de structurer le code et de lui donner un sens. Prenez par exemple ce code-ci. C'est presque impossible de comprendre ce que fait le programme en regardant les 17 lignes de code.

```{codeplay}
:file: forward6.py
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

Si nous observons la tortue, nous comprenons finalement qu'elle dessine deux fois un rectangle. Nous pouvons même interpréter cette image et donner le sens de bâtiment au premier, et de porte au deuxième rectangle.

Essayons maintenant de découper le code en **sous-problèmes** en utilisant deux fonctions `batiment()` et `porte()`.
En regardant ces 3 lignes de code, on comprend immédiatement le sens du programme.

``` python
batiment()
forward(30)
porte()
```

La définition d'une fonction permet d'ajouter des nouveaux mots à un langage de programmation. Contrairement aux commandes natives de Python qui sont tous en anglais, nous sommes libre de les choisir en français.

**Attention** : Ecrivez les fonctions sans accents et sans circonflexes : `batiment()`, `carre()`, `boite()`.

```{codeplay}
:file: forward7.py
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

**Exercice** : Ajoutez une deuxième porte au bâtiment.

```{question}
La fonction `porte())` est équivalent à combien de code

{f}`1 ligne`  
{f}`2 lignes`  
{v}`8 lignes)`  
{f}`17 lignes`  
```

## Définir une fonction

Le fait de donner un nom à une séquence d'instructions est appelé **définir un fonction**. Une **définition de fonction** comporte :

1. le mot-clé `def` (définir),
1. le nom de la fonction (`batiment/porte`),
1. les parenthèses `()`,
1. le deux-points `:`,
1. un bloc en indentation.

C'est quoi un bloc en indentation ?
C'est un bloc de texte qui comporte des espaces vides à gauche. En Python, ces espaces apparaissent en multiples de 4.

L'indentation est très importante en Python. C'est l'indentation qui indique l'étendu des instructions qui font partie de la fonction.

```{question}
Laquelle est une définition de fonction correcte ?

{f}`def() rectangle:`  
{f}`def: rectangle`  
{v}`def rectangle():`  
{f}`def(rectangle):`  
```

## Maison avec porte

Une fois une fonction est définie, elle peut être utilisé partout, même dans la définition d'une autre fonction.

Ici nous avons une fonction `porte()` qui est utilisé à l'intérieur d'une deuxième fonction `maison()`. Pour que ceci est possible, la définition de porte doit être placé avant la définition de `maison()`.

```{codeplay}
:file: forward8.py
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

**Exercice** : Mettez la porte au milieu de la maison, et dessinez une deuxième maison.

## Chaise et table

Essayez maintenant vous-même de définir deux fonctions. Dessinez une chaise en forme de la lettre h et une table en forme de la lettre T.

Vous devez d'abord les définir, ensuite vous pouvez les appeler.

```{codeplay}
:file: forward9.py
from turtle import *

def chaise():
    # mettez votre code ici
    ...

def table():
    # mettez votre code ici
    ...

chaise()
forward(100)
table()
```

## Epaisseur de ligne

La fonction `width(d)` (épaisseur en anglais) permet de définir l'épaisseur de la ligne.
Voici un triangle ou chaque côté a une épaisseur différente.

```{codeplay}
:file: forward10.py
from turtle import *

forward(200)
left(120)

width(5)
forward(200)
left(120)

width(10)
forward(200)
left(120)
```

**Exercice** : Explorez les différents épaisseurs de ligne.

## Maison avec toit

Nous reprenons l'exemple de la maison et dessinons le toit plus épais.

```{codeplay}
:file: forward11.py
from turtle import *

def maison():
    forward(100)
    left(90)
    forward(60)
    left(45)
    width(5)
    forward(71)
    left(90)
    forward(71)
    width(1)
    left(45)
    forward(60)
    left(90)

back(200)
maison()
forward(150)
maison()
forward(150)
maison()
```

**Exercice** : Modifiez l'épaisseur du toit.

## Lever/baisser le stylo

Les deux commandes `up()` et `down()` permettent de lever et baisser le stylo.
Ceci nous permet dessiner des formes séparées, comme ces deux triangles.

```{codeplay}
:file: forward12.py
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

**Exercice** : Ajoutez encore un triangle disjoint.

```{caution}
Contrairement aux fonctions `forward(d)` et `back(d)` qui nécessitent un argument, les fonctions `up()` et `down()` ne nécessitent pas d'argument.
```

## Maison avec fenêtre

Dans le programme ci-dessous nous dessinons de nouveau une maison avec cette fois-ci une fenêtre. Les fonctions `up()/down()` nous permettent de dessiner des formes disjointes, telle qu'une fenêtre à l'intérieur de la maison.

```{codeplay}
:file: forward13.py
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

**Exercice** : Modifiez le programme pour que la fenêtre soit dessinée à l'intérieur de la maison. Dessinez une deuxième maison.

## Trouver la symétrie

Une stratégie importante dans la programmation est de **reconnaitre des structure identiques**. Par exemple quand vous voyez une symétrie dans un dessin,
vous devez repérer la partie qui est répétée et en créer une fonction.

La fonction `bras()` dessine les 3 côtés d'un carré et tourne de 90° dans le contre-sens.
Ensuite il suffit d'**appeler** 4 fois cette fonction.
En appelant la fonction `bras()`, au lieu d'écrire 6 lignes, nous écrivons que 1 ligne de code.

```{codeplay}
:file: forward14.py
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

**Exercice** : Allongez le bras à 120 pas. Faites le bras plus mince.

## Décomposer

Une stratégie importante en programmation est de **décomposer un problème en sous-problèmes**. Les fonctions nous permettent de structurer un problèmes en objets de plus en plus simple.

Ici nous dessinons une fenêtre composé de 4 carreau. Nous pouvons décomposer ce problème en une construction hiérarchique :

- la fonction `fenetre()` appelle deux fois la fonction `demi_fenetre()`,
- la fonction `demi_fenetre()` appelle deux fois la fonction `carreau()`,
- la fonction `carreau()` appelle deux fois la fonction `equerre()`,
- la fonction `equerre()` appelle deux fois la fonction `ligne()`.

```{codeplay}
:file: forward15.py
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

def demi_fenetre():
    carreau()
    carreau()

def fenetre():
    demi_fenetre()
    demi_fenetre()

fenetre()
```

```{question}
Combien de lignes de code sont exécutées par la fonction `fenetre()`?

{f}`16`  
{f}`32`  
{v}`36`  
{f}`40`  
```

## Editeur de Python

Jusqu'à maintenant nous avons exécuté nos petits programmes ici dans cette page web. Malheureusement ces programmes disparaissent quand nous rechargeons la page. Pour pouvoir les sauvegarder et programmer indépendamment de ce site web, nous avons besoin d'un éditeur de Python externe.

Nous vous proposons d'utiliser [Thonny](https://thonny.org), qui est un logiciel libre, facile à installer, et un excellent éditeur pour débuter avec Python. Essayez de faire ceci :

1. Ouvrez l'éditeur Thonny
1. Définissez la fonction `maison()`
1. Appelez la fonction
1. Sauvegardez le programme sous `maison.py`
1. Exécutez le programme

```{image} media/thonny.png
```

Quand vous utilisez le module `turtle` avec Thonny, ajoutez toujours la fonction `done()` comme dernière ligne de code, pour que vous puissiez quitter le programme.

## Exercices

- Téléchargez un exercice.
- Editez-le dans un éditeur externe tel que Thonny.
- Déposez-le sur Moodle (ou plateforme équivalente de votre école).

### La chambre

Dessinez une chambre avec des meubles que vous définissez comme une fonction. Vous êtes libre d'inventer d'autres meubles, de les arranger différemment et de les utiliser multiples fois.

```{codeplay}
:file: chambre.py
from turtle import *
# Votre prénom, nom, classe

def chaise():
    ...

def table():
    ...

def lit():
    ...

chaise()
table()
lit()
```

### Jeu du moulin

Le [jeu du moulin](https://fr.wikipedia.org/wiki/Jeu_du_moulin) est un jeu de société traditionnel en Europe. Le tablier de jeu existait déjà dans la Rome antique. Aussi appelé **jeu du charret** (en Suisse), certains lui donnent le nom médiéval de jeu de mérelles, voire de marelle.

```{image} media/moulin.png
:width: 200
```

Pour les points d'intersection utilisez la fonction `dot()` que vous allez découvrir plus en détail dans le chapitre suivant. La distance entre lignes est de 50 pixels.  
Vous constatez aussi une symétrie par 4. Donc avec un choix intelligent d'une fonction vous pouvez réduire le nombre de lignes de code par 4.

```{codeplay}
:file: moulin.py
from turtle import *
# Votre prénom, nom, classe

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
```

### Tetris

Le jeu vidéo [Tetris](https://fr.wikipedia.org/wiki/Tetris) est un puzzle conçu par l'informaticien russe Alekseï Pajitnov en 1984.
Tetris met le joueur au défi de réaliser des lignes complètes en déplaçant des pièces de formes différentes, les tétrominos, qui défilent depuis le haut jusqu'au bas de l'écran.

```{image} media/tetris.png
```

L'éléments de base du tétronimo mesurent 20 x 20 pixels. Il en existent 7 formes de tétronimo qui sont nommé d'après les lettres auxquels ils ressemblent :

- I (bâton)
- O (carré)
- T
- L
- J
- Z
- S

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
T()
L()
```