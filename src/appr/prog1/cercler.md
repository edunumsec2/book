(prog1.cercler)=

# *Cercler - `circle()`

Dans ce chapitre, nous explorons les cercles et les arcs de cercle. Nous allons voir que :

- la fonction `circle(r)` dessine un cercle de rayon `r`, vers la gauche,
- la fonction `circle(-r)` dessine un cercle de rayon `r`, vers la droite,
- la fonction `circle(r, a)` dessine un arc de cercle de rayon `r` avec un angle `a`.

```{question}
Un cercle affiché sur un écran d'ordinateur est créé par

{f}`une rotation de lumière`  
{f}`un agrandissement d'un point`  
{v}`un polygone régulier d'ordre élevé`  
{f}`une boucle refermée`
```

## Fonction `circle()`

La fonction `circle(r)` dessine un cercle de rayon `r`.
Ce cercle est dessiné :

- vers la gauche si `r` est positif,
- vers la droite si `r` est négatif.

```{codeplay}
from turtle import *

left(90)
circle(20)
circle(40)
circle(60)
circle(80)

circle(-20)
circle(-40)
circle(-60)
circle(-80)
```

## Fleur

Dessinons des cercles dans une boucle, et tournons chaque fois.

```{exercise}
Modifiez le nombre de répétitions et l'angle de rotation.
```

```{codeplay}
from turtle import *

for i in range(6):
    circle(50)
    left(60)
```

## Arc de cercle

Cette fonction peut avoir un deuxième paramètre sous la forme `circle(r, angle)`,
où `angle` représente l'angle de l'arc de cercle dessiné.
Par défaut, l'angle est de 360°, donc un cercle entier.

Voici un exemple qui utilise deux demi-cercles de 180°.

```{exercise}
Dessinez un bonhomme de neige et utilisez `dot()` pour les yeux.
```

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

## Carré arrondi

Avec la fonction `circle()`, il est maintenant possible de dessiner un carré dont les coins sont arrondis.

```{exercise}
Dessinez maintenant un rectangle avec des coins arrondis.
```

```{codeplay}
:file: circle6.py
from turtle import *

for i in range(4):
    forward(100)
    circle(20, 90)
```

## Pac-Man

Pac-Man est un jeu vidéo créé par l’entreprise japonaise Namco, sorti au Japon en 1980. Le jeu consiste à déplacer Pac-Man, un personnage qui ressemble à un diagramme circulaire à l’intérieur d’un labyrinthe, afin de lui faire manger toutes les pac-gommes qui s’y trouvent en évitant d’être touchées par des fantômes.

```{exercise}
Ajoutez l'œil de Pac-Man, et les points qu'il mange.
```

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

## Cœur

Le cœur est le symbole de l'amour : on donne de façon métaphorique son cœur à la personne que l'on aime pour lui signifier qu'on lui confie sa vie.

```{exercise}
Coloriez le cœur en rouge, ajoutez une flèche.
```

```{codeplay}
:file: circle7.py
from turtle import *
r = 50

left(90)
circle(r, 225)
forward(2.4*r)
left(90)
forward(2.4*r)
circle(r, 225)
```

## Infini — ∞

Le mot **infini** (du latin in-, préfixe négatif, et finitus, *limité*) est un adjectif servant à qualifier quelque chose qui n'a pas de limite en nombre ou en taille. L'infini est représenté par le symbole ∞. Nous allons le dessiner.

```{exercise}
Augmentez un des rayons à `2*r` et ajustez la longueur des segments droits.
```

```{codeplay}
:file: circle8.py
from turtle import *
r = 50

right(45)
forward(r)
circle(r, 270)  # aumentez le rayon à 2*r
forward(2*r)
circle(-r, 270)
forward(r)
```

## Bretzel - ⌘

Le pictogramme ⌘ (Unicode 2318), parfois appelé *Gordon loop* ou *bretzel*, a été dessiné par Susan Kare lors de la création du premier Macintosh pour sa touche de commande. Il sert de préfixe à d'autres touches pour construire des raccourcis tels que :

- ⌘-X pour couper
- ⌘-C pour copier
- ⌘-V pour coller

```{exercise}
Modifiez le bretzel pour avoir 3 ou 4 boucles.
```

```{codeplay}
:file: circle9.py
from turtle import *
r = 40

for i in range(4):
    circle(r, 270)
    forward(3*r)
```

## Lettres

Les lettres sont des signes graphiques qui forment un alphabet et servent à transcrire une langue.

```{exercise}
Ajoutez une fonction `m()` pour écrire le mot `nom`. Ajoutez ensuite des fonctions qui dessinent les lettres pour écrire votre prénom.
```

```{codeplay}
:file: circle10.py
from turtle import *
width(5)
r = 30

def n():
    down()
    left(90)
    forward(2*r)    # montée
    backward(r)     # retour au milieu
    circle(-r, 180) # demi-cercle
    forward(r)      # descente
    left(90)
    up()
    forward(r)      # avance vers la prochaine lettre

def o():
    forward(r)      # avance vers milieu
    down()
    circle(r)
    up()
    forward(2*r)    # avance vers prochaine lettre

n()
o()
n()
```

## Pétales

Un pétale est formé de deux arcs de cercle.

```{exercise}
Coloriez la fleur.
```

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

## Exercices

- Téléchargez un exercice.
- Editez-le dans un éditeur.
- Déposez-le sur Moodle.

### LGBTQ+

On vous demande de dessiner des logos pour les toilettes avec le symbole traditionnel ♂ et ♀. La communauté [LGBT](https://fr.wikipedia.org/wiki/Mouvement_LGBT) vous demande d'y ajouter un troisième logo, et c'est à vous d'un créer un.

```{codeplay}
:file: LGBTQ.py
from turtle import *
# Prénom Nom, classe

left(135)
circle(50)
right(90)
forward(50)
...
```

### Anneaux olympiques

Les cinq anneaux imbriqués, colorés en bleu, jaune, noir, vert et rouge sur un fond blanc, sont appelés *anneaux olympiques*. Le symbole est créé à l'origine en 1913 par Pierre Coubertin. Il semble avoir voulu que les anneaux représentent les cinq continents : Europe, Asie, Afrique, Amérique et Océanie.

```{image} media/olympic_rings.png
:width: 300
```

```{codeplay}
:file: olympique.py
from turtle import *
# Prénom Nom, classe

circle(50)
```

### Chemin de fer

Avec des rails de chemin de fer, dessinez un circuit en forme d'un rond (deux rails avec les traverses).

![rails](media/rails2.png)

Utilisez une boucle `for` pour la répétition des traverses.

```{codeplay}
:file: circuit_rond.py
from turtle import *
# Prénom Nom, classe

def traverse():
    ...

forward(200)
```

### Circuit en huit

Avec des rails de chemin de fer, dessinez un circuit en forme de huit (deux rails avec les traverses). Découpez votre code en sous-programmes.

```{codeplay}
:file: circuit_huit.py
from turtle import *
# Prénom Nom, classe

def traverse():
    ...

forward(200)
```

### Un jardin

Dessinez et coloriez un jardin. Définissez des fonctions pour des pétales, feuilles et fleurs.

```{codeplay}
:file: jardin.py
from turtle import *
# Prénom Nom, classe

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
