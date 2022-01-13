# Définir - `def`

Dans ce chapitre nous allons voir de plus près le concept de la fonction, concept que nous avons vu dès le premier chapitre comme façon de donner un nom à une séquence d'instructions.

En fait, la fonction est peut-être le concept le plus important dans la programmation.
C'est un moyen puissant pour inventer des nouvelles commandes dans un langage de programmation. Nous allons voir que

- le mot-clé `def` permet de définir une fonction,
- le mot-clé `return` permet de retourner une valeur,
- un paramètre `f(param0, ...)` est une variable dans la définition de fonction,
- un argument `f(arg0, ...)` est une valeur dans l'appel de fonction.

## Un fonction simple

Dès le premier chapitre nous avons vu la fonction comme façon de donner un nom à une séquence d'instructions.

```{codeplay}
from turtle import *

def carre():
    for i in range(4):
        forward(100)
        left(90)

for i in range(10):
    carre()
    left(36)
```

## Paramétrer la fonction

Jusqu'à maintenant notre carré a toujours eu la même taille.
Il serait très utile si notre nouvelle commande `carre(longueur)` pouvait dessiner des carrés de taille différentes.
C'est possible en spécifiant un paramètre pour la fonction.
Le paramètre de la fonction est une variable locale qui est utilisé dans sa définition.

Lors de l'appel de la fonction nous donnons une valeur à la fonction.
Cette valeur placée entre parenthèses s'appelle l'**argument** de la fonction.
Ici, la fonction `carre()` est appelé successivement avec les valeurs 50, 100 et 150.

```{codeplay}
from turtle import *

def carre(longueur):
    for i in range(4):
        forward(longueur)
        left(90)
        
carre(50)
carre(100)
carre(150)
```

Une fonction peut être appelée avec une valeur numérique directe tel que `carre(50)`, mais aussi avec une valeur numérique donnée par une variable tel que `carre(x)`, obtenu par une variable d'itération sur une plage numérique donnée avec `range(start, stop, step)`.

```{codeplay}
from turtle import *

def carre(a):
    for i in range(4):
        forward(a)
        left(90)

for x in range(30, 180, 30):
    carre(x)
```

Au lieu d'imbriquer les carrés, nous pouvons aussi les dessiner les uns après les autres.
Le terme technique est de les **juxtaposer**.

```{codeplay}
from turtle import *

def carre(a):
    down()
    for i in range(4):
        forward(a)
        left(90)
    up()

up()
back(250)
for x in range(30, 180, 30):
    carre(x)
    forward(x)
```

**Exercice** : Ecartez les carrés de 20 pixels.

## Fonctions natives

Voici quelques fonctions natives, c'est à dire des fonctions standards qui font partie de Python :

- la fonction `pow(m, e)` retourne la puissance de ses deux arguments ($m^e$),
- la fonction `len()` retourne la longueur d'une chaine de caractères ou d'une liste,
- la fonction `round()` retourne l'arrondi d'une valeur numérique.

```{codeplay}
print(pow(3, 5))
print(len("Bonjour"))
print((round(333.76)))
```

**Exercice** : Ajoutez une ligne de code avec la fonction `min` qui retourne la valeur minimale des arguments qu'on lui fournit.

## Valeur de retour

L'instruction `return` permet de retourner une valeur.
Le grand intérêt d'une valeur de retour est qu'on peut l'utiliser de nouveau dans des expression.

Par exemple nous pouvons créer une expression comme celle-ci : `square(x) + cube(x)`

```{codeplay}
def carre(x):
    return x ** 2

def cube(x):
    return x ** 3

x = input('Entrez un nombre: ')
x = int(x)
print('carré =', carre(x))
print('cube =', cube(x))
print('carré + cube =', carre(x) + cube(x))
```

## Points de sortie

Une fonction peut avoir plusieurs points de sortie. En fait quand une ligne avec `return` est exécutée, toutes les lignes qui suivent ne sont plus exécutées.

La fonction `signe()` possède 3 points de sortie.

```{codeplay}
def signe(x):
    if x > 0:
        return 'positif'
    elif x < 0:
        return 'négatif'
    else:
        return 'zéro'

x = int(input('Entrez un nombre: '))
print(x, 'est', signe(x))
```

**Exercice** : Testez avec -2, 0 et 3.

## Squid Game logo

Squid Game, ou Le Jeu du calmar, est une série télévisée dramatique de survie sud-coréenne de 9 épisodes, diffusée dans le monde entier en 2021 sur Netflix.
La série raconte l'histoire d'un groupe de personnes, fortement endettées, voire ruinées, qui risquent leur vie dans un jeu de survie mystérieux avec comme récompense une somme énorme.

Nous définissons une fonction `polygone(a, n)` pour dessiner le cercle, le triangle et le carré du logo.

```{codeplay}
from turtle import *
getscreen().bgcolor('peru')
width(5)
up()

def polygone(a, n):
    down()
    for i in range(n):
        forward(a)
        left(360/n)
    up()
    
back(150)
polygone(10, 36)
forward(100)
polygone(120, 3)
forward(170)
polygone(100, 4)
```

**Exercice** : Ajoutez votre nom et vos coordonnées à la carte de visite en utilisant la fonction `write()`.

## Dessiner un pixel

Similaire à notre fonction pour dessiner un carré nous allons définir une fonction `pixel()`, mais cette fois nous ajoutons un deuxième argument :

- `taille` pour la taille du carré,
- `couleur` pour la couleur du carré.

```{codeplay}
from turtle import *

def carre(taille):
    for i in range(4):
        forward(taille)
        left(90)
        
def pixel(taille, couleur):
    fillcolor(couleur)
    begin_fill()
    carre(taille)
    end_fill()
    forward(taille)

back(200)
for x in ('yellow', 'orange', 'red'):
    pixel(100, x)
```

## Dessiner Pikachu

Nous définissons une nouvelle fonction `ligne(couleurs)` pour dessiner une série de pixels, qui sont donnés par une liste de couleurs.
Quand le dernier pixel de la ligne est dessiné, la tortue est retournée à la position prête pour dessiner la ligne suivante.

```{codeplay}
from turtle import *

def pixel(taille, couleur):
    fillcolor(couleur)
    begin_fill()
    for i in range(4):
        forward(taille)
        left(90)
    end_fill()
    forward(taille)

taille = 50

def ligne(couleurs):
    for couleur in couleurs:
        pixel(taille, couleur)
    back(len(couleurs) * taille)
    up()
    sety(ycor() - taille)
    down()

back(2 * taille)
ligne(['black', 'yellow', 'yellow', 'black'])
ligne(['white', 'red', 'yellow', 'white'])
ligne(['yellow', 'yellow', 'yellow', 'yellow'])
ligne(['yellow', 'yellow', 'yellow', 'white'])
```

**Exercice** : Dessinez un autre Pokemon.
