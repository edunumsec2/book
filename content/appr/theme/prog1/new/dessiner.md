# Dessiner - `forward`

Dans ce chapitre nous explorons ce que c'est un programme et nous prenons
ici la métaphore du dessin. Un dessin est une séquence de lignes qui forment une image.

Allons-y en avant (forward) avec la programmation. Nous allons voir que

- un programme est une séquence d'instructions,
- les instructions `forward()`, `back()`, `left()`, `right()` permettent de dessiner,
- le mot-clé `def` permet de nommer (définir) une séquence,
- une boucle `for` permet de répéter des instructions.

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
Elle permet aussi de structurer notre code et de lui donner un sens.
Dans l'exemple ci-dessus nous dessinons deux fois un rectangle. 
Mais une fois nous lui donnons le sens de bâtiment, la deuxième fois de porte.

Vous voyez tout de suite que les 3 lignes

    batiment()
    forward(30)
    porte()

font beaucoup plus de sens que les 16 lignes `forward()` et `left()`.

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
1. un bloc indenté.

C'est quoi un bloc indenté, ou une indentation ?
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
Rappelez vous ceci:

- on définit une fonction une seule fois,
- on peut appeler une fonction autant de fois que l'on veut.

De nouveau nous réduisons les lignes de code nécessaires.
Avec la fonction `boite()`, au lieu d'écrire 6 lignes, nous écrivons que 1 ligne de code.

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

## Répéter une séquence

Revenons vers un exemple simple : dessiner un carré.

Si nous regardons le code de près, nous pouvons voir que nous répétons 4 fois les mêmes deux instruction `forward()` et `left()`.

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

Ne serait-il pas pratique de pouvoir dire à la tortue de répéter ces instructions 4 fois ?  
Ceci est possible avec une boucle `for`. La ligne `for i in range(x):` va répéter `x` fois le bloc indenté qui suit.

```{codeplay}
from turtle import *

for i in range(4):
    forward(100)
    left(90)
```

**Exercice** : Transformez le rectangle en triangle.

## Dessiner des polygones

Avec une boucle `for` nous pouvons simplifier le dessins des formes symétriques.

```{codeplay}
from turtle import *

def triangle():
    for i in range(3):
        forward(100)
        left(120)

def carre():
    for i in range(4):
        forward(100)
        left(90)

def hexagone():
    for i in range(6):
        forward(100)
        left(60)

triangle()
carre()
hexagone()
```

**Exercice** : Définissez la fonction `pentagone()` pour dessiner un pentagone.

## Dessiner un éventail

Que se passe-t-il si nous dessinons une ligne (`forward/back`) et tournons d'un petit angle à chaque fois ?
C'est un peu comme un éventail qui s'ouvre.

```{codeplay}
from turtle import *

for i in range(18):
    forward(100)
    back(100)
    left(10)
```

**Exercice** : Utilisez cette méthode pour dessiner les rayons du soleil sur 360°.

## Dessiner une étoile

Une autre façon de toujours avancer, mais tourner à chaque fois d'un angle un peu plus petit que 180°.
Essayons !

```{codeplay}
from turtle import *

for i in range(9):
    forward(200)
    left(160)
```

**Exercice** : Changez le nombre de pics de l'étoile.

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
for i in range(3):
    maison()
    forward(150)
```

**Exercice** : Modifiez l'épaisseur du toit.

## Lever/baisser le stylo

Les deux commandes `up()` et `down()` permettent de lever et baisser le stylo.
Ceci nous permet dessiner des lignes séparées, comme cette ligne en traitillé.

```{codeplay}
from turtle import *

for i in range(7):
    down()
    forward(20)
    up()
    forward(10)
```

**Exercice** : Définissez une fonction `ligne()` et utilisez-la pour dessiner un triangle.

## Bâtiment avec fenêtre

Dans le programme ci-dessous nous dessinons de nouveau un bâtiment avec cette fois-ci une fenêtre. Mais vous remarquerez une différence :

- au début du programme le stylo est levé,
- au début de chaque forme le stylo est baissé,
- à la fin de chaque forme le stylo est de nouveau levé.

Ceci nous permet de dessiner des formes disjoints.

```{codeplay}
from turtle import *
up()

def fenetre():
    down()
    for i in range(4):
        forward(30)
        left(90)
    up()
        
def batiment():
    down()
    for i in range(2):
        forward(200)
        left(90)
        forward(100)
        left(90)
    up()

fenetre()
forward(70)
batiment()
```

**Exercice** : Modifiez le programme pour que la fenêtre soit dessiné à l'intérieur du bâtiment.

## Dessiner un losange

Si nous déformons les angles d'un carré, nous obtenons un losange (diamant).
Quelle forme obtenons-nous en dessinant un carré et deux losanges ?

```{codeplay}
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

## Dessiner une fleur

Si nous dessinons un losange 6 fois, nous obtenons une jolie fleur.

```{codeplay}
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

## Exercices

1. On vous demande de dessiner des logos pour les toilettes avec le symbole traditionnel ♂ et ♀.
1. La communauté LGBTQ+ vous demande d'y ajouter un troisième logo.
1. Dessinez un sapin de Noël. Définissez des fonctions pour des boules et des étoiles.
1. Dessinez une ville. Définissez des fonctions pour des maisons et des immeubles.
1. Dessinez un paysage. Définissez des fonctions pour des montagnes et des sapins.
1. Dessinez un jardin. Définissez des fonctions pour les feuilles, les pétales et les fleurs.
1. Dessinez un aquarium. Définissez des fonctions pour les poissons, l'herbe, et les bulles.
