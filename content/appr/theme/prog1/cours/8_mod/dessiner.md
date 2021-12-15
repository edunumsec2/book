# Dessiner

Dans ce chapitre nous explorons ce que c'est un programme.

- un programme est une séquence d'instructions
- les instructions `forward, back, left, right` permettent de dessiner
- une boucle `for` permet de répéter des instructions

## Le module tortue

Le module `turtle` présente une façon sympathique pour faire des dessins.
On s'imagine une tortue qui se déplace sur un canvas et laisse une trace.


```{codeplay}
from turtle import *
shape('turtle')
forward(150)
```

**Exercice :** Essayez d'ajouter d'autre fonctions tel que `back, left, right`

Elle peut se déplacer avec les 4 fonctions:

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

**Exercice :** Transformez le code pour dessiner une maison.

## Répéter un bout de code

Si nous regardons le code de près, nous remarquons que 2 lignes de code sont répétées 4 fois.
Nous pouvons utiliser une boucle `for` et réduire le code de 8 à 3 lignes.

A ce stade, nous apprenons juste que `for i in range(n):` va répéter le bloc qui suit `n` fois.
Le bloc à répéter doit être indentée.

```{codeplay}
from turtle import *

for i in range(4):
    forward(100)
    left(90)
```

**Exercice :** Ajouter du code pour dessiner un triangle.

## Nommer un bout de code

Dessiner un carré est assez utile. C'est une forme qu'on pourrait réutiliser certainement.
Il serait pratique de définir un nom pour ces 3 lignes de code.
Avec le mot-clé `def` nous pouvons définir une nouvelle commande que nous allons appeler `square()`.
On appelle cette façon de faire **définir** une fonction.

Ensuite il suffit d'écrire `square()`pour dessiner le carré. On appelle ceci **appeler** une fonction.
Rappelez vous ceci:

- on définit une fonction une seule fois
- on peut appeler une fonction autant de fois qu'on veut

De nouveau nous réduisons les lignes de code nécessaires.
Au lieu d'écrire 3 lignes, nous écrivons que 1 ligne de code.

```{codeplay}
from turtle import *

def square():
    for i in range(4):
        forward(100)
        left(90)
        
square()
```

## Appeler multiple fois

Que se passe-t-il si nous tournons de 90° et répétions a dessiner un carré?

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

## Dessiner une étoile

Que se passe-t-il si nous dessinons une ligne (`forward/back`) et tournons d'un petit angle à chaque fois?

```{codeplay}
from turtle import *

for i in range(36):
    forward(100)
    back(100)
    left(10)
```

Une autre façon serait de toujours avancer, mais tourner à chaque fois d'un angle un peu plus petit que 180°.
Essayons!

```{codeplay}
from turtle import *

back(150)
for i in range(9):
    forward(300)
    left(160)
```

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

De nouveaux nous constatons une suite de nombres `30, 60, 90, ...`.
Nous pouvons utiliser une boucle avec une plage `range(start, end, increment)`

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
    for i in range(4):
        forward(a)
        left(90)
        
back(200)
for x in range(30, 180, 30):
    square(x)
    forward(x)
```

##  Multiple fonctions

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
## Un losange

Si nous déformons les angles d'un carré, nous obtenons un losange (diamond).
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

## Une fleur
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
