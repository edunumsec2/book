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

- dans la première ligne nous importons toutes les fonctions du module `turtle`,
- avec `shape('turtle')` nous affichons une tortue (au lieu de la flèche),
- avec `forward(150)` nous faisons avancer la tortue de 150 pixels.

```{codeplay}
from turtle import *

shape('turtle')
forward(150)
```

**Exercice** : Ajoutez d'autre fonctions tel que `back()`, `left()`, `right()` pour faire un dessin.

La tortue peut se déplacer et dessiner une trace avec les 4 fonctions:

- `forward(d)` pour avancer d'une distance `d` (en pas ou pixels)
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

forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
```

**Exercice** : Modifiez ce code pour dessiner une maison.

## Nommer une séquence

Dessiner un rectangle est assez utile. C'est une forme qu'on pourra réutiliser certainement plein de fois. Il serait pratique de définir un nom pour ces 8 lignes de code.
Avec le mot-clé `def` nous pouvons définir une nouvelle commande que nous allons appeler `rectangle()`.
On appelle cette façon de créer un raccourci, **définir** une fonction.

Ensuite il suffit d'écrire `rectangle()` pour dessiner un rectangle. On appelle ceci **appeler** une fonction.
Rappelez vous ceci:

- on définit une fonction une seule fois,
- on peut appeler une fonction autant de fois que l'on veut.

Définir une fonction nous permet de réduire les lignes de code nécessaires.
A chaque fois que nous utilisons `rectangle()`,
au lieu d'écrire 8 lignes, nous écrivons que 1 ligne de code.

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

**Exercice** : Dessinez plusieurs rectangles en utilisant la nouvelle fonction.

## Définir une fonction

Le fait de donner un nom à une séquence d'instructions est appelé **définir un fonction**. Une **définition de fonction** comporte :

- le mot-clé `def` (définir),
- le nom de la fonction,
- le deux-points `:`,
- un bloc indenté.

C'est quoi un bloc indenté, ou une indentation ?
C'est un bloc de texte qui comporte des espaces vides à gauche. En Python, ces espaces apparaissent en multiples de 4.

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

**Exercice** : Ajoutez une porte à la maison.

```{question}
La définition de la fonction `maison` comporte :
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
Nous pouvons en créer une fonction `pic()` et l'appeler 6 fois.

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

Dans l'exemple précédent, la ligne de code `pic()` est répétée 6 fois.
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

**Exercice** : Modifiez le nombre de pics de l'étoile.


```{question}
L'expression `for i in range(4+2)` répète le bloc qui suit
{f}`2`,
{f}`4`,
{v}`6` ou 
{f}`8`
fois.
```

Que se passe-t-il si nous dessinons des carrés et tournons de 45° à chaque tour ?

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

**Exercice** : Si nous tournons de seulement 30°, combien de fois devons-nous répéter pour compléter le dessin ?

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
Ceci nous permet dessiner des lignes séparées, comme cette ligne en traitillé.

```{codeplay}
from turtle import *

for i in range(9):
    down()
    forward(20)
    up()
    forward(10)
```

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

**Exercice** : Utilisez cette méthode pour dessiner les rayons du soleil.

## Dessiner une étoile

Une autre façon de toujours avancer, mais tourner à chaque fois d'un angle un peu plus petit que 180°.
Essayons !

```{codeplay}
from turtle import *

for i in range(9):
    forward(200)
    left(160)
```

**Exercice** : Ajoutez `up()/down()` et définissez une fonction `etoile()`. Ensuite dessinez plein d'étoiles !

## Dessiner un triangle

Maintenant nous sommes prêts pour définir une nouvelle fonction que nous appelons `triangle()`. Dessinés ensemble avec `carre()`, nous obtenons une petite maisonnette.

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

**Exercice** : Dessinez plusieurs triangles en utilisant la nouvelle fonction.

## Dessiner une maison

Donc nous décidons de définir une troisième fonction `maison()` pour dessiner une maisonnette. Elle est composée de `carre()` et de `triangle()`

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

**Exercice** : Modifiez le code pour écarter les maisons.

## Dessiner une fenêtre

Dans la fonction `maison()` nous avons utilisé 2 fonctions: `carre()` et `triangle`.
Dans l'exemple suivant nous utilisons une définition hiérarchique pour dessiner une fenêtre :

- la fonction `cote()` dessine uniquement un seul côté et tourne de 90°,
- la fonction `cote2()` dessine deux côtés,
- la fonction `carre()` appelle `cote2()` deux fois,
- la fonction `carre2()` dessine 2 carrés,
- la fonction `fenetre()` dessine les 4 carrés d'une fenêtre.

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

def carre2():
    carre()
    left(90)
    carre()
    left(90)
    
def fenetre():
    carre2()
    carre2()
    
fenetre()
```

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

**Exercice** : Choisissez un angle plus petit que 60°

```{question}
L'expression `left(90)` est équivalent à

{v}`right(-90)`
{f}`right(180)`
{f}`left(180)`
{f}`left(270)`
{v}`right270)`
{v}`left(-270)`
```

## Exercices

1. On vous demande de dessiner des logos pour les toilettes avec le symbole traditionnel ♂ et ♀.
1. La communauté LGBTQ+ vous demande d'y ajouter un troisième logo.
1. Dessinez le symbole astrologique de Jupiter ♃ et une autre planète.
1. Dessinez un sapin de Noël. Définissez des fonctions pour des boules et des étoiles.
1. Dessinez une ville. Définissez des fonctions pour des maisons et des immeubles.
1. Dessinez un paysage. Définissez des fonctions pour des montagnes et des sapins.
1. Dessinez un jardin. Définissez des fonctions pour les feuilles, les pétales et les fleurs.
1. Dessinez un aquarium. Définissez des fonctions pour les poissons, l'herbe, et les bulles.