# Cercler - `circle`

Dans ce chapitre nous explorons les cercles et les arcs de cercle. Nous allons voir que

- un cercle est approximé par un polygone,
- la fonction `circle(r)` dessine un cercle de rayon `r`,
- la fonction `circle(r, a)` dessine un arc de cercle d'un angle `a`.

## Du polygone au cercle

Plus que le polygone régulier a de sommets, plus il ressemble à un cercle.
Tandis qu'avec 9 sommets il ressemble clairement à un polygone,
avec 36 sommets, il ressemble déjà raisonnablement à un cercle.

```{codeplay}
from turtle import *

for i in range(9):
    forward(40)
    left(40)
    
right(15)

for i in range(36):
    forward(10)
    left(10)
```

## Périmètre et rayon

Quel est le rayon `r` du cercle approximé par par le polygone ?
Nous pouvons le trouver à partir du périmètre avec la relation suivante :

$$ p = 2r \pi $$

Donc

$$ r = \frac{p}{2 \pi} $$

La valeur numérique du rayon est

$$ r = \frac{360}{6.28} = 57 $$

La fonction `circle(57)` dessine un cercle dont le rayon est 57. L'expérience montre que le polygone et le cercle ont effectivement la même taille.

```{codeplay}
from turtle import *

for i in range(36):
    forward(10)
    left(10)

right(5)
circle(57)
```

## Fonction `circle()`

La fonction `circle(r)` dessine un cercle de rayon `r`.
Le cercle est dessiné :

- vers la gauche si `r` est positif,
- vers la droite si `r` est négatif.

```{codeplay}
from turtle import *

forward(50)
circle(40)
forward(100)
circle(-30)
forward(100)
```

**Exercice** : Inverser le signe du rayon dans la fonction `circle()`.

## Fleur

Dessinons des cercles dans une boucle, et tournons à chaque fois.

```{codeplay}
from turtle import *

for i in range(6):
    circle(50)
    left(60)
```

**Exercice** : Modifier l'angle le nombre de répétitions et l'angle de rotation.

## Arc de cercle

Cette fonction peut avoir un deuxième paramètre sous la forme `circle(r, angle)`
ou `angle` représente l'angle de l'arc de cercle dessiné.
Par défaut l'angle est de 360°, donc un cercle entier.

Voici un exemple qui utilise deux demi-cercles de 180°.

```{codeplay}
from turtle import *

forward(100)
circle(40, 180)
forward(50)
circle(-30)
forward(50)
circle(40, 180)
```

**Exercice** : Dessinez un bonhomme de neige et utilisez `dot()` pour les yeux.

## Carré arrondi

Avec la fonction `circle()` il est maintenant possible de dessiner un carré arrondie.

```{codeplay}
from turtle import *

for i in range(4):
    forward(100)
    circle(20, 90)
```

**Exercice** : Dessinez un rectangle arrondi.

## Coeur

Le cœur est le symbole de l'amour : on donne de façon métaphorique son cœur à la personne que l'on aime pour lui signifier qu'on lui confie sa vie.

```{codeplay}
from turtle import *
width(10)

left(90)
circle(50, 225)
forward(120)
left(90)
forward(120)
circle(50, 225)
```

**Exercice** : Coloriez le coeur en rouge, ajoutez une flèche.

## Infini - ∞

Le mot **infini** (du latin in-, préfixe négatif, et finitus, *limité*) est un adjectif servant à qualifier quelque chose qui n'a pas de limite en nombre ou en taille. L'infini est représenté par le symbole ∞.

```{codeplay}
from turtle import *
width(10)

right(45)
forward(100)
circle(100, 270)
forward(200)
circle(-100, 270)
forward(100)
```

## Bretzel - ⌘

Le pictogramme ⌘ (Unicode 2318), parfois appelé *Gordon loop* ou *bretzel*, a été dessiné par Susan Kare lors de la création du premier Macintosh pour sa touche de commande. Elle sert de préfixe à d'autres touches pour construire des raccourcis tel que :

- cmd+X pour couper
- cmd+C pour Copier
- cmd+V pour Coller

```{codeplay}
from turtle import *
width(10)

for i in range(4):
    circle(50, 270)
    forward(150)
```

## Lettres

Les lettres sont des signes graphiques qui formant un alphabet et servant à transcrire une langue.

```{codeplay}
from turtle import *
width(10)

def espace():
    up()
    forward(30)
    down()

def n():
    left(90)
    forward(80)
    back(40)
    circle(-40, 180)
    forward(40)
    left(90)
    espace()

def o():
    espace()
    circle(40)
    espace()
    espace()

n()
o()
n()
```

**Exercice** : Ajoutez und fonction `m()` pour écrire le mot `nom`. Ajoutez ensuite les lettres pour écrire votre prénom.

## Pétales

Un pétale est formé de deux arcs de cercle.

```{codeplay}
from turtle import *

def petale():
    for i in range(2):
        circle(100, 120)
        left(60)

for i in range(6):
    petale()
    left(60)
```

**Exercice** : Coloriez la fleur.
