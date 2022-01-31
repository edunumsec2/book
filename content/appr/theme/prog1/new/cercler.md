# Cercler - `circle`

Dans ce chapitre nous explorons les cercles et les arcs de cercle. Nous allons voir que :

- le cercle est approximé par un polygone,
- la fonction `circle(r)` dessine un cercle de rayon `r`,
- la fonction `circle(r, a)` dessine un arc de cercle d'un angle `a`.

```{question}
Un cercle affiché sur un écran d'ordinateur est créé par

{f}`une rotation de lumière`  
{f}`un agrandissement d'un point`  
{v}`un polygone régulier d'ordre élevé`  
{f}`une boucle refermée`
```

## Du polygone au cercle

Plus que le polygone régulier a de sommets, plus il ressemble à un cercle.
Tandis qu'avec 9 sommets il ressemble clairement à un polygone,
avec 36 sommets, il ressemble déjà raisonnablement à un cercle.

```{codeplay}
:file: circle1.py
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
:file: circle2.py
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
:file: circle3.py
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
:file: circle4.py
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
:file: circle5.py
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
:file: circle6.py
from turtle import *

for i in range(4):
    forward(100)
    circle(20, 90)
```

**Exercice** : Dessinez maintenant un **rectangle** arrondi.

## Pac-Man

Pac-Man est un jeu vidéo créé par l’entreprise japonaise Namco, sorti au Japon en 1980. Le jeu consiste à déplacer Pac-Man, un personnage qui ressemble à un diagramme circulaire à l’intérieur d’un labyrinthe, afin de lui faire manger toutes les pac-gommes qui s’y trouvent en évitant d’être touché par des fantômes.

```{codeplay}
:file: circle6.py
from turtle import *

fillcolor('yellow')
begin_fill()
left(30)
forward(100)
left(90)
circle(100, 300)
left(90)
forward(100)
end_fill()
```

**Exercice** : Ajoutez l'oeil de Pac-Man.

## Coeur

Le cœur est le symbole de l'amour : on donne de façon métaphorique son cœur à la personne que l'on aime pour lui signifier qu'on lui confie sa vie.

```{codeplay}
:file: circle7.py
from turtle import *

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

Observez l'effet de croisement obtenu en ne pas dessinant un petit bout de l'intersection.

```{codeplay}
:file: circle8.py
from turtle import *

right(45)
up()
forward(15)
down()
forward(85)
circle(100, 270)
forward(200)
circle(-100, 270)
forward(90)
```

**Exercice** : Augmentez l'épaisseur de la ligne.

## Bretzel - ⌘

Le pictogramme ⌘ (Unicode 2318), parfois appelé *Gordon loop* ou *bretzel*, a été dessiné par Susan Kare lors de la création du premier Macintosh pour sa touche de commande. Elle sert de préfixe à d'autres touches pour construire des raccourcis tel que :

- cmd+X pour couper
- cmd+C pour Copier
- cmd+V pour Coller

```{codeplay}
:file: circle9.py
from turtle import *

for i in range(4):
    circle(50, 270)
    forward(150)
```

**Exercice** : Modifiez le programme pour obtenir le même effet de croisement comme avec le symbole infini ∞.

## Lettres

Les lettres sont des signes graphiques qui formant un alphabet et servant à transcrire une langue.

```{codeplay}
:file: circle10.py
from turtle import *
width(10)

def espace():
    up()
    forward(30)
    down()

def n():
    left(90)
    forward(80)
    backward(40)
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
:file: circle11.py
from turtle import *

def petale():
    for i in range(2):
        circle(100, 120)
        left(60)

for i in range(6):
    petale()
    left(60)
```

**Exercice** : Coloriez la fleur.

## Exercices

- Téléchargez un exercice.
- Editez-le dans un éditeur.
- Déposez-le sur Moodle.

### LGBTQ+

On vous demande de dessiner des logos pour les toilettes avec le symbole traditionnel ♂ et ♀. La communauté LGBTQ+ vous demande d'y ajouter un troisième logo.

```{codeplay}
:file: LGBTQ.py
from turtle import *
# Votre prénom, nom, classe

left(135)
circle(50)
right(90)
forward(50)
...
```

### Anneaux olympiques

Les cinq anneaux imbriqués, colorés en bleu, jaune, noir, vert et rouge sur un fond blanc, sont appelés *anneaux olympiques*. Le symbole est créé à l'origine en 1913 par Pierre Coubertin. Il semble avoir voulu que les anneaux représentent les cinq continents : Europe, Asie, Afrique, Amérique et Océanie.

C'est un défi particulier, de dessiner les anneaux imbriqués.

```{image} media/olympic_rings.png
:width: 300
```

```{codeplay}
:file: olympique.py
from turtle import *
# Prénom, nom, classe

circle(50)
```

### Chemin de fer

Avec des rails de chemin de fer dessinez un circuit en forme d'un rond (deux rails avec les traverses).

```{codeplay}
:file: circuit_rond.py
from turtle import *
# Prénom, nom, classe

def traverse():
    ...

forward(200)
```

### Circuit en huit

Avec des rails de chemin de fer dessinez un circuit en forme de huit (deux rails avec les traverses). Découpez en sous-programmes.

```{codeplay}
:file: circuit_huit.py
from turtle import *
# Prénom, nom, classe

def traverse():
    ...

forward(200)
```

### Un jardin

Dessinez et coloriez un jardin. Définissez des fonctions pour des pétales, feuilles et fleurs.

```{codeplay}
:file: jardin.py
from turtle import *
# Votre prénom, nom, classe

dot(1000, 'lightgreen')  # background

def petale():
    ...
def feuille():
    ...
def fleur():
    dot(50, 'red')

feuille()
forward(200)
fleur()
```
