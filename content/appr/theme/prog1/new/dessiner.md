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

## Une séquence

Un programme est une séquence d'instructions. Le bloc des 8 instructions ci-dessous indique comment dessiner un carré. La tortue doit avancer, tourner, avancer, tourner etc.

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

**Exercice** : Modifiez ce code pour dessiner une maison.

## Répéter une séquence

Si nous regardons le code de près, nous remarquons que 2 lignes de code sont répétées 4 fois.
Nous pouvons utiliser une boucle `for` et réduire le code de 8 à 3 lignes.

A ce stade, nous apprenons juste que `for i in range(n):` va répéter le bloc qui suit `n` fois.
Le bloc à répéter doit être indenté.

```{codeplay}
from turtle import *

for i in range(4):
    forward(100)
    left(90)
```

**Exercice** : Ajoutez une deuxième boucle pour dessiner un triangle.

## Nommer une séquence

Dessiner un carré est assez utile. C'est une forme qu'on pourra réutiliser certainement plein de fois. Il serait pratique de définir un nom pour ces 3 lignes de code.
Avec le mot-clé `def` nous pouvons définir une nouvelle commande que nous allons appeler `square()`.
On appelle cette façon de faire **définir** une fonction.

Ensuite il suffit d'écrire `square()`pour dessiner le carré. On appelle ceci **appeler** une fonction.
Rappelez vous ceci:

- on définit une fonction une seule fois
- on peut appeler une fonction autant de fois qu'on veut

De nouveau nous réduisons les lignes de code nécessaires.
Au lieu d'écrire 3 lignes, nous écrivons que 1 ligne de code.

- la boucle `for` nous a permit réduire 8 lignes en 3 lignes,
- la fonction `def` nous permet de réduire encore plus de 3 ligne en 1. 

```{codeplay}
from turtle import *

def square():
    for i in range(4):
        forward(100)
        left(90)
        
square()
```

## Définir une fonction

Nous avons maintenant tout pour définir une nouvelle commande pour dessiner une maison.
Le dessin commence en bas à gauche de maison et se termine au même endroit.

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

## Appeler une fonction

Nous pouvons appeler une fonction autant de fois que nous voulons. Ceci ajoute juste une ligne de code, mais pourrait représenter des centaines de ligne de code exécuté.

Que se passe-t-il si nous tournons de 90° et recommencions a dessiner un carré ?

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

**Exercice** : Si nous tournons de seulement 30°, combien de fois devons-nous répéter ?

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
**Exercice** : Dessinez une grille avec des lignes horizontales.

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

## Paramétrer la fonction

Jusqu'a maintenant notre carré a toujours la même taille.
Il serait bien si notre nouvelle commande `square()` pouvait dessiner des carrés de taille variable.
C'est possible en spécifiant un argument pour la fonction.
L'argument de la fonction est une valeur (variable locale) qui est passé à la fonction quand elle est appelé.

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

## La fonction `range()`

De nouveaux nous constatons une suite de nombres `30, 60, 90, ...`.
Nous pouvons utiliser une boucle avec une plage `range(start, stop, step)`

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
    down()
    for i in range(4):
        forward(a)
        left(90)
    up()
  
up()
back(250)
for x in range(30, 180, 30):
    square(x)
    forward(x)
```

**Exercice** : Ecartez les carrés de 10-20 pixels.

## Ajouter un triangle

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

## Dessiner une maisonnette

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

**Exercice** : Modifiez le code pour écarter les maisons.

## Dessiner un losange

Si nous déformons les angles d'un carré, nous obtenons un losange (diamant).
Quelle forme obtenons-nous en dessinant un carré et deux losanges

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

## Dessiner une fleur

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

**Exercice** : Choisissez un angle plus petit que 60°
