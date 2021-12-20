# Trier - `sort`

Pouvoir trier les éléments dans une liste est une fonctionalité fondamentale dans l'informatique. Le succès énorme de Google est basé sur un tri efficace de l'information. 

Les éléments de la liste peuvent être des nombres, des mots, ou des phrases. Si la liste est trié il devient très facile de trouver un certain élément.

## Trouver une liste aléatoire

Pour tester les fonctions de tri, nous avons besoin de liste avec de valeur aléatoires.
Ici nous créons d'abord une liste avec les valeur 0 à 9. Ensuite nous les mélangeons comme on le ferait avec un jeu de cartes.

```{codeplay}
from random import *

liste = list(range(10))
print(liste)

shuffle(liste)
print(liste)
```

## Visualiser une liste

Nous visualisons les valeurs numériques dans la liste avec un diagramme de barres

```{codeplay}
from random import *
from turtle import *

liste = list(range(10))
shuffle(liste)
print(liste)

speed(10)
color('blue')
up()
left(90)
goto(-250, -50)
width(20)

for i in liste:
    write(i)
    forward(20)
    down()
    forward(i * 20 + 1)
    up()
    goto(xcor() + 50, -50)
```

## Trouver un minimum

Pour trouver un minimum nous : 

- prenons la première valeur comme minimum courant 
- parcourons le reste de la liste
- gardons la valeur comme nouveau minimum si elle est plus petite

```{codeplay}
liste = [3, 6, 8, 2, -3, 20, 12]
print(liste)

min = liste[0]
print(min)

for val in liste[1:]:
    if val < min:
        min = val
        print(min)
```

**Exercice** : Modifiez la liste et essayez de nouveau.

## Trouver un maximum

Pour trouver un maximum nous : 

- prenons la première valeur comme maximum courant 
- parcourons le reste de la liste
- gardons la valeur comme nouveau maximum si elle est plus grande

```{codeplay}
liste = [3, 6, 8, 2, -3, 20, 12]
print(liste)

max = liste[0]
print(max)

for val in liste[1:]:
    if val > max:
        max = val
        print(max)
```

**Exercice** : Modifiez la liste et essayez de nouveau.

## Compter des éléments



## Importer un module

Le mot-clé `import` permet d'importer un module. La fonction `dir` permet de voir le contenu du module.
Normalement tous les modules sont importés au début d'un programme.

```{codeplay}
import math

print(dir(math))
````

**Exercice :** importez le module `random` et affichez son contenu avec `dir`.

Pour utiliser une fonction du module importé, il faut faire précéder le nom de la fonction par le nom du module, séparé d'un point.

```{codeplay}
import math


print('e =', math.e)
print('pi =', math.pi)
print('fact(7) =', math.factorial(7))
````

**Exercice :** utilisez la fonction `pow` (puissance) et affichez le résultat.

## Module `math`

On retrouve dans le module `math` des fonctions ainsi que des constantes :

- arithmétiques,
- logarithmiques et exponentielles,
- trigonométriques.

Voici quelques utilisations du module `math` avec des fonctions trigonométriques.

![trigonometry](trigo.gif)

```{codeplay}
from math import asin, acos, atan, degrees

opp = 3
adj = 4
hyp = 5

print(degrees(asin(opp/hyp)))
print(degrees(acos(adj/hyp)))
print(degrees(atan(opp/adj)))
```

Dans cet exemple, on importe les fonctions `asin`, `acos`, `atan` et `degrees` du module `math`. Les trois premières renvoient un angle en radian et la dernière permet de convertir radian en degré.

## Constantes

Voici toutes les objets importé par le module `math`:

```{codeplay}
import math
print(dir(math))
```

Parmi ces objets il y en a 5 qui sont des constantes:

- `math.e  ` base des logarithmes naturels (nombre d'Euler)
- `math.inf` symbole pour infinité
- `math.nan` symbole pour *not a number*
- `math.pi ` rapport de la circonférence d'un cercle à son diamètre
- `math.tau` rapport de la circonférence d'un cercle à son rayon


```{codeplay}
import math

print('Constantes:')
print('e   =', math.e)
print('inf =', math.inf)
print('nan =', math.nan)
print('pi  =', math.pi)
print('tau =', math.tau)
```

## Fonctions trigonométriques

Voici les fonctions trigonométriques:

- `math.sin/cos` fonction sinus/cosinus
- `math.sinh/cosh` fonctions sinus/cosinus hyperbolique
- `math.tan/tan2` fonction tangente avec 1 ou 2 arguments
- `math.tanh` fonction tangente hyperbolique

Et leurs fonctions inverses (arc):

- `math.asin/asinh`
- `math.acos/acosh`
- `math.atan/atanh`

Affichons donc les fonctions `math.sin()` et `math.cos()` avec deux couleurs différentes.

```{codeplay}
import math
from turtle import *

color('red')
for x in range(-300, 300, 10):
    y = 100 * math.sin(x/50)
    setpos(x, y)
    dot()
    
color('blue')
for x in range(-300, 300, 10):
    y = 100 * math.cos(x/50)
    setpos(x, y)
    dot()
```

Dessinons aussi des axes :

```{codeplay}
import math
from turtle import *

for x in range(-6, 7, 1):
    setx(x * 50)
    dot()
    write(' ' + str(x))
```

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```


