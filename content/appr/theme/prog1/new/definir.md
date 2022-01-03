# Définir - `def`

La fonction est le concept le plus important, le plus puissant dans, le plus créatif dans toute langue de programmation.

C'est un moyen incroyable d'inventer des nouveaux mots d'un langage de programmation. Dès le premier chapitre nous avons introduit la fonction comme façon de donner un nom à une séquence.

Ceci nous a permit :

- une économie de code
- plus de lisibilité
- plus de choix

Une fonction permet aussi de découper un problème complexe en sous-problèmes.

```{codeplay}
from turtle import *

def square():
    for i in range(4):
        forward(100)
        left(90)

for i in range(10):
    square()
    left(36)
```

## Paramétrer la fonction

Jusqu'a maintenant notre carré a toujours eu la même taille.
Il serait très utile si notre nouvelle commande `square()` pouvait dessiner des carrés de taille différentes.
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

**Exercice** : Ecartez les carrés de 20 pixels.

## Fonctions natives

Voici quelques fonctions natives, c'est à dire des fonctions standards qui font partie de Python :

- la fonction `pow` retourne la puissance de ses deux arguments (ici, par exemple, $3^5$),
- la fonction `len` retourne la longueur d'une chaine de caractères ou d'une liste,
- la fonction `round` retourne l'arrondi d'une valeur numérique.

```{codeplay}
print(pow(3, 5))
print(len("Bonjour"))
print((round(333.76)))
```

**Exercice :** : Ajoutez une ligne avec la fonction `min` qui retourne la valeur minimale des arguments qu'on lui fournit.

## Valeur de retour

L'instruction `return` permet de retourner une valeur.
Le grand intérêt d'une valeur de retour est qu'on peut l'utiliser de nouveau dans des expression.

Par exemple nous pouvons créer une expression comme celle-ci : `square(x) + cube(x)`

```{codeplay}
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

x = input('Entrez un nombre: ')
x = int(x)
print(square(x))
print(cube(x))
print(square(x) + cube(x))
```

## Points de sortie

Une fonction peut avoir plusieurs points de sortie. En fait quand une ligne avec `return` est exécuté, toutes les lignes qui suivent ne sont plus exécuté.

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

**Exercice** : Testez avec -2, 0 et 3.

