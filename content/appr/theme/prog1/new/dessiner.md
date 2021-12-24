# Dessiner - `turtle`

Dans ce chapitre nous explorons ce que c'est un programme et nous prenons
ici la métaphore du dessin. Un dessin est une séquence de lignes qui forment une image.

- un programme est une séquence d'instructions
- les instructions `forward, back, left, right` permettent de dessiner
- une boucle `for` permet de répéter des instructions
- le mot-clé `def` permet de nommer (définir) une séquence

## Le module tortue

Le module `turtle` présente une façon sympathique pour faire des dessins.
On s'imagine une tortue qui se déplace sur un canevas et laisse une trace.

- dans la première ligne nous importons toutes les fonctions du module `turtle`
- avec `shape('turtle')` nous affichons une tortue (au lieu de la flèche)
- avec `forward(150)` nous faisons avancer la tortue de 150 pixels

```{codeplay}
from turtle import *

shape('turtle')
forward(150)
```

**Exercice** : Ajoutez d'autre fonctions tel que `back, left, right` pour faire un dessin.

La tortue peut se déplacer avec les 4 fonctions:

- `forward()` pour avancer
- `back()` pour reculer
- `left()` pour tourner à gauche
- `right()` pour tourner à droite

Au début elle se trouve au centre d'une zone rectangulaire.
Ce rectangle a les propriétés suivants:

- l'origine (0, 0) se trouve au centre
- l'axe x s'étend de -300 à +300
- l'axe y s'étend de -200 à +200

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

forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
```

**Exercice** : Modifiez ce code pour dessiner une maison.

## Nommer une séquence

Dessiner un rectangle est assez utile. C'est une forme qu'on pourra réutiliser certainement plein de fois. Il serait pratique de définir un nom pour ces 8 lignes de code.
Avec le mot-clé `def` nous pouvons définir une nouvelle commande que nous allons appeler `rectangle()`.
On appelle cette façon de faire **définir** une fonction.

Ensuite il suffit d'écrire `rectangle()`pour dessiner un rectangle. On appelle ceci **appeler** une fonction.
Rappelez vous ceci:

- on définit une fonction une seule fois
- on peut appeler une fonction autant de fois qu'on veut

De nouveau nous réduisons les lignes de code nécessaires.
Au lieu d'écrire 8 lignes, nous écrivons que 1 ligne de code.

```{codeplay}
from turtle import *

def rectangle():
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
    left(90)
        
rectangle()
left(180)
rectangle()
```

**Exercice** : Dessinez plusieurs rectangles en utilisant la nouvelle fonction.

## Définir une fonction

Le fait de donner un nom à une séquence d'instructions est aussi appelé **définir un fonction**. Une **définition de fonction** comporte :

- le mot-clé `def` (définir)
- le nom de la fonction
- le deux-points `:``
- un bloc indentée

L'indentation est très importante en Python. C'est l'indentation qui indique la séquence d'instructions qui fait partie de la définition de fonction.

Nous avons maintenant tout pour définir une nouvelle commande qui va dessiner une maison. Le dessin commence en bas à gauche de maison et se termine au même endroit.

```{codeplay}
from turtle import *

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

backward(150)
maison()
forward(140)
maison()
forward(140)
maison()
```

**Exercice** : Ajoutez une porte à la maison.

```{question}
La définition de la fonction `maison` comporte :
{f}`5`,
{f}`8`, 
{v}`10`,
{f}`11` ou
{f}`12`
lignes de code.
```

## Appeler une fonction

Une stratégie importante dans la programmation est de reconnaitre des structure identiques. Par exemple quand vous voyez une symmétrie dans un dessin,
vous devez repérer la partie qui est répétée et en créer une fonction.

Ensuite il suffit d'**appeler** cette fonction.
Rappelez vous ceci:

- on définit une fonction une seule fois
- on peut appeler une fonction autant de fois qu'on veut

De nouveau nous réduisons les lignes de code nécessaires.
Avec la fonction `boite`, au lieu d'écrire 6 lignes, nous écrivons que 1 ligne de code.

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

## Dessiner une étoile

Par exemple dans une étoile nous repérons des pics qui sont répétés.
Nous pouvons en créer une fonction.

```{codeplay}
from turtle import *

def pic():
    forward(100)
    left(160)
    forward(100)
    right(100)
    
pic()
pic()
pic()
pic()
pic()
pic()
```

## Répéter une séquence

Si nous regardons le code de près, nous remarquons que la ligne de code `pic()` est répétée 6 fois.
Nous pouvons utiliser une boucle `for` et répéter ce code.

A ce stade, nous apprenons juste que `for i in range(x):` va répéter le bloc qui suit `x` fois. Le bloc à répéter doit être indenté.

```{codeplay}
from turtle import *

def pic():
    forward(100)
    left(160)
    forward(100)
    right(100)

for i in range(6):
    pic()
```

**Exercice** : Modifier le nombre de pics de l'étoile.


```{question}
L'expression `for i in range(4+2)` répète le bloc qui suit
{f}`2`,
{f}`4`,
{v}`6` ou 
{f}`8`
fois.
```

Que se passe t'il si nous dessinons des carrés et tournons de 45° à chaque tour ?

```{codeplay}
from turtle import *

def carre():
    for i in range(4):
        forward(100)
        left(90)

for i in range(8):
    carre()
    left(45)
```

**Exercice** : Si nous tournons de seulement 30°, combien de fois devons-nous répéter ?

```{question}

    forward(100)
    left(-90)
    back(-20)

place la tortue à la position
{f}`(0, 0)` 
{f}`(100, 0)`
{f}`(100, -20)`
{v}`(100, 20)`
{f}`(20, 100)`
```

## Lever/baisser le stylo

Les deux commandes `up()` et `down()` permettent de lever et baisser le stylo.
Ceci nous permet des lignes séparés.

```{codeplay}
from turtle import *

for i in range(9):
    down()
    forward(20)
    up()
    forward(10)
```

## Epaisseur de ligne

La fonction `width(d)` permet de définir l'épaisseur de la ligne.

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

**Exercice** : Explorez les différent4s épaisseurs de ligne.

## Dessiner un éventail

Que se passe-t-il si nous dessinons une ligne (`forward/back`) et tournons d'un petit angle à chaque fois ?
C'est un peut comme un éventail qui s'ouvre.

```{codeplay}
from turtle import *

for i in range(18):
    forward(100)
    back(100)
    left(10)
```

**Exercice** : Utilisez cette méthode pour dessiner un coucher de soleil.

## Dessiner une étoile

Une autre façon serait de toujours avancer, mais tourner à chaque fois d'un angle un peu plus petit que 180°.
Essayons !

```{codeplay}
from turtle import *

for i in range(9):
    forward(200)
    left(160)
```

**Exercice** : Ajoutez `up()/down()` et définissez une fonction `etoile()`. Ensuite dessinez plein d'étoiles !

## Dessiner un triangle

Maintenant nous sommes prêts pour définir une deuxième fonction que nous appelons `triangle()`.
Dessinés ensemble avec `carre()`, nous obtenons une petite maisonnette.

```{codeplay}
from turtle import *

def carre():
    for i in range(4):
        forward(100)
        right(90)
        
def triangle():
    for i in range(3):
        forward(100)
        left(120)
        
carre()
triangle()
```

**Exercice** : Dessinez plusieurs triangles en utilisant la nouvelle fonction.

## Dessiner une maison

Donc nous décidons de définir une troisième fonction `maison()` pour dessiner une maisonnette.

```{codeplay}
from turtle import *

def carre():
    width(1)
    for i in range(4):
        forward(100)
        right(90)
        
def triangle():
    width(3)
    for i in range(3):
        forward(100)
        left(120)
    
def maison():
    carre()
    triangle()
    forward(100)
    
back(200)
maison()
maison()
maison()
```

**Exercice** : Modifiez le code pour écarter les maisons.

## Dessiner un losange

Si nous déformons les angles d'un carré, nous obtenons un losange (diamant).
Quelle forme obtenons-nous en dessinant un carré et deux losanges

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

Si nous dessinons le losange 6 fois, nous obtenons une jolie fleur.

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

**Exercice** : Choisissez un angle plus petit que 60°

## Quiz

```{question} Turtle
L'expression `left(90)` est équivalent à

{v}`right(-90)`
{f}`right(180)`
{f}`left(180)`
{f}`left(270)`
{v}`right270)`
{v}`left(-270)`
```