(prog1.grouper)=
# Grouper - `list`

Dans ce chapitre, nous découvrons une nouvelle structure de données - la liste. C'est une séquence ordonnée d'objets quelconques. Contrairement au `tuple` qui est immuable, la liste est *muable*, c'est-à-dire que nous pouvons réassigner ces éléments. Nous allons voir que :

- la liste est une séquence d'objets entre crochets tels que `[2, 3, 5]`,
- la notion d'index `liste[i]` permet d'accéder au i-ème élément de la liste,
- la notion de tranche `liste[i:j]` permet d'accéder à une sous-liste.

```{question}
En informatique, une liste est

{v}`ordonnée`  
{f}`jamais vide`  
{f}`toujours hétérogène`  
{f}`un ensemble mathématique`
```

## Des groupes d'objets

Une liste permet de manipuler des groupes d'objets tels que :

- noms d'élèves
- notes d'un cours
- couleurs

En Python, on peut grouper des objets divers dans une liste. Une liste est ordonnée, ce qui veut dire qu'il y a un premier objet et un dernier objet.

```{exercise}
Ajoutez une nouvelle liste et affichez-la.
```

```{codeplay}
:file: list1.py
noms = ['Tim', 'Kim', 'Anna', 'Cindy']
notes = [4, 5, 4, 5.5, 6, 3.5]
couleurs = ['fuchsia', 'pink', 'orange']

print(noms)
print(notes)
```

En Python, une liste est délimitée par des crochets `[]` et ses éléments sont séparés par des virgules `,`.

## La fonction `len()`

La fonction `len()` retourne la longueur d'une liste, c'est-à-dire le nombre d'éléments qu'elle contient.

```{exercise}
Ajoutez des éléments à une liste at affichez de nouveau sa longueur.
```

```{codeplay}
:file: list2.py
noms = ['Tim', 'Kim', 'Anna', 'Cindy']
notes = [4, 5, 4, 5.5, 6, 3.5]
couleurs = ['fuchsia', 'pink', 'orange']

print(len(noms))
print(len(notes))
```

## La fonction `list()`

La fonction `list()` peut transformer une chaîne de caractères ou une plage numérique en liste.

```{codeplay}
:file: list3.py
print(list('Python'))
print(list(range(10)))
print(list(range(100, 150, 7)))
```

## Index `[i]`

Nous pouvons accéder à un élément de la liste en utilisant un numéro entre crochets `[]`, appelé **index**. L'index d'un élément est toujours un nombre entier. En Python, comme dans beaucoup de langages de programmation, l'index pour le premier élément de la liste est 0 et non pas 1. Ainsi, les éléments d'une liste de longueur `n` auront comme premier index 0 et comme dernier index `n - 1`.

```{codeplay}
:file: list4.py
noms = ['Tim', 'Mia', 'Kim', 'Anna', 'Cindy', 'Léa']
print(noms[0])
print(noms[2])
print(noms[-1])
print(noms[-2])
```

Un index négatif désigne un élément d'une liste pris depuis la fin de la liste.

Les chaînes de caractères (`str`) peuvent aussi être indexées.

```{codeplay}
:file: list5.py
noms = ['Tim', 'Mia', 'Kim', 'Anna', 'Cindy', 'Léa']
print(noms[0][0])
print(noms[2][1])
print(noms[-1][2])
```

## Tranche `[i:j]`

La notation `[i:j]`, après le nom d'une variable qui contient une liste, permet d'extraire une sous-liste de la liste. Cette sous-liste, aussi appelée **tranche**, est une partie de la liste identifiée par les deux index `i` et `j`.

```{exercise}
Modifiez l'expression de tranche et exécutez de nouveau.
```

```{codeplay}
:file: list6.py
noms = ['Tim', 'Mia', 'Kim', 'Anna', 'Cindy', 'Léa']

print(noms[:2])    # élément 0 et 1
print(noms[2:4])   # élément 2 et 3
print(noms[4:])    # élément 4 et 5

print(noms[::2])   # chaque 2e élément
print(noms[1::2])  # chaque 2e élément
```

```{question}
Quel est le résultat de l'expression `'python'[:2]` ?

{f}`thon`
{f}`y`
{f}`p`
{v}`py`
```

## Itérer sur une liste

La boucle `for` peut itérer sur les éléments d’une liste. La variable d’itération prend successivement la valeur de chaque élément de la liste.
La pratique est d'utiliser pour la liste un nom de variable au pluriel (`noms`) et pour la variable d'itération le même nom au singulier (`nom`).

```{codeplay}
:file: list7.py
noms = ['Tim', 'Mia', 'Kim', 'Anna', 'Cindy', 'Léa']
for nom in noms:
    print(nom)
```

```{question}
Quel est le résultat de l'expression `'pikachu'[-3:]` ?

{f}`pik`
{v}`chu`
{f}`p`
{f}`pika`
```

## Concaténation

L'opérateur `+` permet de concaténer (mettre bout à bout) deux listes.

```{codeplay}
:file: list8.py
noms = ['Kim', 'Wendy']

print([1, 2, 3] + [5, 4, 99])
print(noms + ['George'])
```

## Répétition

L'opérateur `*` permet de répéter une liste.

```{codeplay}
:file: list9.py
noms = ['Kim', 'Ada'] * 2
print(noms)
print([0] * 6)
print(5 * [1])
```

## Ajouter des éléments

Une **méthode** fonctionne comme une fonction, mais est rattachée à une liste avec la notation (`.`).
Par exemple, si `a` désigne une liste, on peut ajouter un élément `x` à la fin de cette liste avec l'expression `a.append(x)`.

<!-- Ne devrait-on pas préciser qu'une méthode peut-être utilisée avec d'autres objets Python que des listes ?  -->

Ces trois méthodes permettent toutes d’ajouter des éléments à une liste existante :

- `append(x)`,
- `extend(iterable)`,
- `insert(i, x)`.

```{codeplay}
:file: list10.py
a = [1, 2, 3]
a.append(99)
print(a)
```

La méthode `extend(sequence)` ajoute plusieurs éléments d'une **séquence** tels qu'une liste ou une chaîne de caractères (texte).

```{codeplay}
:file: list11.py
a = [1, 2, 3]
a.extend([10, 11])
a.extend('abc')
print(a)
```

La méthode `insert(i, x)` insère un nouveau élément `x` à la position `i`.

```{codeplay}
:file: list12.py
a = [1, 2, 3]
a.insert(2, 999)
print(a)
```

## Enlever des éléments

Les méthodes suivantes permettent d'enlever des éléments à une liste :

- `remove(x)`,
- `pop(i)`,
- `clear()`.

La méthode `remove(x)` enlève l'élément `x` s'il existe, et donne une erreur autrement.

```{codeplay}
:file: list13.py
a = [1, 2, 3, 4]
a.remove(3)
print(a)
```

La méthode `pop()` enlève le dernier élément.

```{codeplay}
:file: list14.py
a = [1, 2, 3, 4]
a.pop()
print(a)
```

La méthode `pop(i)` enlève l'élément avec l'index `i`.

```{codeplay}
:file: list15.py
a = [1, 2, 3, 4]
a.pop(1)
print(a)
```

La méthode `clear()` enlève tous les éléments.

```{codeplay}
:file: list16.py
a = [1, 2, 3, 4]
a.clear()
print(a)
```

## Opérations

Les listes disposent aussi de méthodes avec notation dotée :

- `liste.sort()` pour trier une liste,
- `liste.reverse()` pour inverser l'ordre des éléments,
- `liste.count(x)` pour compter l'occurrence d'un élément x.

### Trier une liste

La méthode `sort()` trie la liste dans l'ordre croissant (pour les caractères, on se réfère au code ASCII ou UTF utilisé).
Cette méthode fonctionne uniquement si tous les éléments sont du même type (nombre, texte) et peuvent être comparés.

```{codeplay}
:file: list17.py
a = [23, 10, -89, -54, 99, 2, 13]
a.sort()
print('trié', a)
```

Le programme suivant montre le même tri de liste sous forme graphique.

```{exercise}
Ajoutez 5 éléments en plus.
```

```{codeplay}
:file: list18.py
from turtle import *
up()

def affiche(liste, couleur, etiquette):
    n = len(liste)
    color(couleur)
    for i in range(n):
        goto(i/n*500-250, liste[i])
        down()
        dot(10)
    write('  ' + etiquette, font=(None, 12))
    up()

a = [23, 10, -89, -54, 99, 2, 13]

affiche(a, 'blue', 'originale')
a.sort()
affiche(a, 'red', 'triée')
hideturtle()
```

### Inverser une liste

La méthode `reverse()` inverse l'ordre de la liste.

```{codeplay}
:file: list19.py
a = [1, 23, 10, -89, -54, 99]
a.reverse()
print('inversé', a)
```

De nouveau nous donnons un exemple graphique.

```{codeplay}
:file: list20.py
from turtle import *
up()

def affiche(liste, couleur, etiquette):
    n = len(liste)
    color(couleur)
    for i in range(n):
        goto(i/n*500-250, liste[i])
        down()
        dot(10)
    write('  ' + etiquette, font=(None, 12))
    up()

a = [1, 23, 10, -89, -54, 99]

affiche(a, 'blue', 'originale')
a.reverse()
affiche(a, 'red', 'inversée')
hideturtle()
```

### Compter un élément

La méthode `count(x)` compte le nombre d'occurrences de l'élément `x`.

```{codeplay}
:file: list21.py
m = list('Monty Python')
print(m.count('y'))
```

## Vecteurs

Une liste peut représenter un vecteur.
Pour calculer la **norme d'un vecteur** nous additionnons les carrés des éléments et prenons la racine carrée.

```{codeplay}
:file: list22.py
a = [1, 4, 7]
norm = 0
for i in a:
    norm += i**2
    
norm = norm ** 0.5
print(norm)
```

Pour **additionner deux vecteurs**, il faut additionner chacun de leurs éléments.

```{codeplay}
:file: list23.py
a = [1, 4, 7]
b = [2, 1, 2]
result = [0, 0, 0]
for i in range(3):
    result[i] = a[i] + b[i]
print(result)
```

Pour multiplier un vecteur avec un **scalaire k**, il faut multiplier chaque élément avec ce scalaire.

```{codeplay}
:file: list24.py
a = [1, 4, 7]
result = [0, 0, 0]
k = 2
for i in range(3):
    result[i] = a[i] * k
print(result)
```

Pour calculer le **produit scalaire** de deux vecteurs, il faut additionner le produit des éléments des vecteurs.

```{codeplay}
:file: list25.py
a = [1, 4, 7]
b = [2, 1, 2]
s = 0
for i in range(3):
    s += a[i] * b[i]
print(s)
```

## Compréhension de liste

Une **compréhension de liste** est une spécificité «élégante» du langage Python qui permet de construire de manière compacte des listes sur une seule ligne.

Voici un exemple de construction «traditionnelle» d'une liste où on ajoute un élément après l'autre avec une boucle.

```{codeplay}
:file: list26.py
cubes = []
for i in range(10):
    cubes.append(i ** 3)
print(cubes)
```

En utilisant la compréhension de liste, on peut construire la même liste sur une seule ligne.

```{codeplay}
:file: list27.py
print([i ** 3 for i in range(10)])
```

On peut comprendre cette formulation de la manière suivante : la liste cubes indicée par i prend la valeur $i^3$ pour toutes les valeurs de i de 0 à 9.

Une condition peut être ajoutée dans la compréhension (par exemple, pour n'ajouter à la liste que les valeurs impaires).
L'opérateur `%` est l'opérateur modulo qui renvoie le reste de la division.

```{codeplay}
:file: list28.py
a = []
for i in range(10):
    if i % 2 == 1:
        a.append(i ** 2)
print(a)
```

Nous pouvons alors écrire la formation de cette liste en une seule ligne.

```{codeplay}
:file: list29.py
print([i**2 for i in range(10) if i % 2 == 1])
```

## La pile

Une **pile** est une structure de données qui permet de gérer l'arrivée et le départ des éléments. Dans une pile d'assiettes ou de magazines, le dernier élément ajouté est le premier à être enlevé.

En anglais cette structure s'appelle **stack** ou **LIFO** (last in first out).

L'exemple suivant est une pile qui accumule des entiers.
Si répondez avec une chaîne vide, ceci enlève le dernier élément mis sur la pile, jusqu'à ce que la pile soit vide.

```{exercise}
Ajoutez des objets (nombres, texte) sur la pile. Enlevez un élément avec *Enter*.
```

```{codeplay}
:file: list30.py
x = input('[] < ')
pile = []

while x or len(pile):
    if x:
        pile.append(int(x))
    else:
        print(pile.pop()) 
    x = input(str(pile) + ' < ')

print('fin')
```

## La file d'attente

La file d'attente est une structure de données qui permet de gérer l'arrivée et le départ d'éléments.

Dans une file d'attente devant un guichet, la première personne arrivée est la première à être servi.

En anglais cette structure s'appelle **buffer** ou encore **FIFO** (first in first out).

L'exemple suivant est une file d'attente pour des entiers.
Si vous répondez avec une chaîne vide, ceci enlève le plus ancien élément de la file, jusqu'à ce que la file soit vide.

```{exercise}
Ajoutez des objets (nombres, texte) à la file. Enlevez avec *Enter*.
```

```{codeplay}
:file: list31.py
x = input('[] < ')
file = []

while x or len(file):
    if x:
        file.append(int(x))
    else:
        print(file.pop(0))
    x = input(str(file) + ' < ')

print('fin')
```
