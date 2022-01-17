# Dessiner - `forward`

Dans ce chapitre nous explorons ce que c'est un programme et nous prenons
 la métaphore du dessin. Ici, un programme est une séquence d'instructions pour dessiner une image.

Allons-y en avant (forward) avec la programmation. Nous allons voir que

- les instructions `forward()`, `back()`, `left()`, `right()` permettent de dessiner,
- le mot-clé `def` permet de nommer (définir) une séquence,
- la fonction `width(d)` permet de choisir l'épaisseur,
- les fonctions `up()/down()` permettent de lever et baisser le stylo.

## Le module tortue

Dans le langage de programmation Python, le module `turtle` (tortue en anglais) présente une façon sympathique pour faire des dessins. Ce pour cela que nous commençons notre aventure de programmation avec cet animal qui avance tout doucement à son propre rythme à lui.

On s'imagine une tortue qui se déplace sur un canevas et laisse une trace.

Ci-dessus vous trouvez notre premier programme de trois ligne :

- dans la première ligne nous importons toutes (`*`) les fonctions du module `turtle`,
- avec `shape('turtle')` nous affichons une tortue (au lieu de la flèche),
- avec `forward(150)` nous faisons avancer la tortue de 150 pixels.

```{codeplay}
from turtle import *

shape('turtle')
forward(150)
```

**Exercice** : Ajoutez d'autre fonctions tel que `back()`, `left()`, `right()` pour faire un dessin.

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

```{question}
La largeur de la zone de dessin de la tortue est de
{f}`200`,
{f}`300`,
{f}`400`,
{v}`600` ou
{f}`800`
pixels.
```

## Une séquence

Un programme est une séquence d'instructions. Le bloc des 8 instructions ci-dessous indique comment dessiner un carré. La tortue doit avancer, tourner, avancer, tourner etc.

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

**Exercice** : Modifiez ce code pour faire le rectangle plus long.

```{question}

Le code

    forward(100)
    left(90)
    back(20)

place la tortue à la position
{f}`(0, 0)` 
{f}`(100, 0)`
{v}`(100, -20)`
{f}`(100, 20)`
{f}`(20, 100)`
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
L'expression `left(90)` est équivalent à deux autres expressions

{v}`right(-90)`
{f}`right(180)`
{f}`left(180)`
{f}`left(270)`
{v}`right(270)`
```

## Donner du sens

Une fonction ne permet pas seulement d'économiser des lignes de code.
Elle permet aussi de structurer le code et de lui donner un sens. Prenez par exemple ce code-ci. C'est presque impossible de comprendre ce que fait le programme en regardant les 17 lignes de code.

```{codeplay}
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

    batiment()
    forward(30)
    porte()

La définition d'une fonction permet d'ajouter des nouveaux mots à un langage de programmation. Contrairement aux commandes natives de Python qui sont tous en anglais, nous sommes libre de les choisir en français.

**Attention** : Ecrivez les fonctions sans accents et sans circonflexes : `batiment()`, `carre()`, `boite()`.

```{codeplay}
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

Nous avons maintenant tout ce qui est nécessaire pour définir deux nouvelles commande : une pour dessiner une porte une autre pour dessiner une maison.

```{codeplay}
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

forward(30)
porte()
forward(70)
maison()
```

**Exercice** : Intégrez la porte dans la définition da la maison, et dessinez 2 fois la nouvelle maison avec porte.

```{question}
La définition de la fonction `maison()` comporte :
{f}`5`,
{f}`8`, 
{v}`10`,
{f}`11` ou
{f}`12`
lignes de code.
```

## Appeler une fonction

Une stratégie importante dans la programmation est de reconnaitre des structure identiques. Par exemple quand vous voyez une symétrie dans un dessin,
vous devez repérer la partie qui est répétée et en créer une fonction.

Ensuite il suffit d'**appeler** cette fonction.
En appelant la fonction `boite()`, au lieu d'écrire 6 lignes, nous écrivons que 1 ligne de code.

```{codeplay}
from turtle import *

def boite():
    forward(60)
    left(90)
    forward(60)
    left(90)
    forward(60)
    right(90)
    
boite()
boite()
boite()
boite()
```

**Exercice** : Allongez la boite à 120 pas.



## Epaisseur de ligne

La fonction `width(d)` (épaisseur en anglais) permet de définir l'épaisseur de la ligne.
Voici un triangle ou chaque côté a une épaisseur différente.

```{codeplay}
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

Nous reprenons l'exemple de la maison et dessinons le toit plus épais.

```{codeplay}
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
Ceci nous permet dessiner des formes séparées, ou ce trait discontinu.

```{codeplay}
from turtle import *

forward(100)
up()
forward(50)
down()
forward(100)
```

**Exercice** : Définissez une fonction `ligne()` et utilisez-la pour dessiner un triangle.

## Bâtiment avec fenêtre

Dans le programme ci-dessous nous dessinons de nouveau un bâtiment avec cette fois-ci une fenêtre. Les fonctions `up()/down()` nous permettent de dessiner des formes disjoints.

```{codeplay}
from turtle import *

def fenetre():
    for i in range(4):
        forward(30)
        left(90)
        
def batiment():
    for i in range(2):
        forward(200)
        left(90)
        forward(100)
        left(90)

batiment()
up()
forward(230)
down()
fenetre()
```

**Exercice** : Modifiez le programme pour que la fenêtre soit dessinée à l'intérieur du bâtiment.

## Décomposer en sous-problèmes

Les fonctions nous permettent de décomposer un problème en sous-problèmes.

Ici nous avons une construction hiérarchique :

- la fonction `fenetre()` appelle deux fois la fonction `carre2()`
- la fonction `carre2()` appelle deux fois la fonction `carre()`
- la fonction `carre()` appelle deux fois la fonction `cote2()`
- la fonction `cote2()` appelle deux fois la fonction `cote()`

```{codeplay}
from turtle import *

def cote():
    forward(100)
    left(90)

def cote2():
    cote()
    cote()

def carre():
    cote2()
    cote2()
    left(90)

def carre2():
    carre()
    carre()

def fenetre():
    carre2()
    carre2()

fenetre()
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

## Exercices

1. On vous demande de dessiner des logos pour les toilettes avec le symbole traditionnel ♂ et ♀.
1. La communauté LGBTQ+ vous demande d'y ajouter un troisième logo.
1. Dessinez un sapin de Noël. Définissez des fonctions pour des boules et des étoiles.
1. Dessinez une ville. Définissez des fonctions pour des maisons et des immeubles.
1. Dessinez un paysage. Définissez des fonctions pour des montagnes et des sapins.
1. Dessinez un jardin. Définissez des fonctions pour les feuilles, les pétales et les fleurs.
1. Dessinez un aquarium. Définissez des fonctions pour les poissons, l'herbe, et les bulles.
