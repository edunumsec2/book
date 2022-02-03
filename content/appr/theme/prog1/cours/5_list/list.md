# 4. Listes

Une liste est un séquence linéaire d'objets. En Python, syntaxiquement, une liste :

- est délimitée par des crochets `[]`,
- voit ses éléments séparés par des virgules `,`.

Voici des exemples de listes homogènes (même type de variables).

    a = [123, 43, 5]
    b = [`chat`, `chien`, `5`]

On peut également créer des listes non-homogènes, mais les "bonnes pratiques" de programmation induisent alors qu'on utilise plutôt des *tuples*.

La fonction `len` retourne la longueur d'une liste, c'est à dire le nombre d'éléments qu'elle contient.

```{codeplay}
fruits = ['banane', 'pomme', 'orange']
print(len(fruits))
```

La fonction `print` peut imprimer une liste. 
```{codeplay}
fruits = ['banane', 'pomme', 'orange']
print(fruits)
````

**Exercice** : ajoutez un élément à la liste `fruits`. Ajoutez une deuxième liste `prix` avec des éléments numériques.

## La fonction `list`

La fonction `list` peut transformer un <span commented>itérable (plage, chaine, ensemble, ...)</span><!-- REVIEW/JPP: on ne connaît encore rien à part la chaîne de caractères, et on n'a que brièvement parlé de range() sans bien la définir. À mon avis, on n'en a pas besoin à ce stade. --> en liste.

```{codeplay}
b = list(range(10))
print(b)
```

La fonction `list` transforme une chaîne en liste.

```{codeplay}
m = list('Monty Python')
print(m)
```

## Index

Nous pouvons accéder à un élément de la liste en utilisant un numéro entre crochets `[]`, appelé _index_. L'index d'un élément est toujours un nombre entier. En Python, comme dans beaucoup de langages de programmation, l'index pour le premier élément de la liste est 0 et non pas 1. Ainsi, les éléments d'une liste de longueur `n` auront comme premier index 0 et comme dernier index `n - 1`.

```{codeplay}
fruits = ['banane', 'pomme', 'orange']
print(fruits[0])
```

**Exercice** : essayez d'accéder aux éléments `fruits[2]` et `fruits[3]`.

```{codeplay}
m = list('Monty Python')
print(m[0])
print(m[4])
```

Un index négatif désigne un élément d'une liste pris depuis la fin de la liste.

```{codeplay}
m = list('Monty Python')
print(m[-1])
print(m[-2])
```

## Tranche


La notation `[i:j]`, après le nom d'une variable qui contient une liste, permet d'extraire une tranche de la liste, c'est à dire une partie de la liste telle qu'identifiée par ses bornes, les deux index `i` et `j`.

L'expression suivante extrait la sous-liste du 3e au 5e élément.

```{codeplay}
m = list('Monty Python')
print(m[2:5])
```

L'expression suivante extrait la sous-liste du début au 4e élément.
La deuxième extrait la sous-liste du 8e élément à la fin.

```{codeplay}
m = list('Monty Python')
print(m[:4])
print(m[8:])
```

Ici on extrait les éléments à partir de l'avant-dernier, jusqu'à la fin.

```{codeplay}
m = list('Monty Python')
print(m[-2:])
```

## Itération sur une liste

La boucle `for` peut itérer sur les éléments d’une liste. La variable d’itération prend successivement la valeur de chaque élément de la liste.
La pratique est d'utiliser pour la liste un nom de variable au pluriel (fruits) et pour l'itérateur le même nom au singulier (fruit).

```{codeplay}
fruits = ['banane', 'pomme', 'orange']
for fruit in fruits:
    print(fruit)
```

## Concaténation

L'opérateur `+` permet de concaténer (mettre bout à bout) deux listes.

```{codeplay}
fruits = ['banane', 'pomme', 'orange'] + ['ananas']
print(fruits)
```
## Répétition

L'opérateur `*` permet de répéter une liste.

```{codeplay}
fruits = ['banane', 'pomme'] * 3
print(fruits)
```
## Ajouter des éléments

Une **méthode** fonctionne comme une fonction, mais est rattachée à une liste avec la notation (`.`). 
Par exemple si `a` désigne une liste, on peux ajouter un élément `x` à la fin de cette liste avec l'expression `a.append(x)`. 

Ces trois méthodes différentes permettent d’ajouter des éléments à une liste existante :

- `append(x)`,
- `extend(iterable)`,
- `insert(i, x)`.


```{codeplay}
a = [1, 2, 3]
a.append(99)
print(a)
```

La méthode `extend(itérable)` ajoute plusieurs éléments. Un *itérable* est une séquence telle qu'une liste, une chaîne de caractères (texte), un ensemble, un tuple, ..., c'est à dire un objet pour lequel on peut itérer sur les objets élémentaires le constituant. 

```{codeplay}
a = [1, 2, 3]
a.extend([10, 11])
a.extend('abc')
print(a)
```

La méthode `insert(i, x)` insère un nouvel élément `x` à la i<sup>ème</sup> position.

```{codeplay}
a = [1, 2, 3]
a.insert(2, 999)
print(a)
```

## Enlever des éléments

Les méthodes suivantes permettent d'enlever des éléments à une liste.

- `remove(x)`,
- `pop(i)`,
- `clear()`.

La méthode `remove(x)` enlève l'élément `x` s'il existe, et donne une erreur autrement.

```{codeplay}
a = [1, 2, 3, 4]
a.remove(3)
print(a)
```

La méthode `pop()` enlève le dernier élément.

```{codeplay}
a = [1, 2, 3, 4]
a.pop()
print(a)
```

La méthode `pop(i)` enlève le i<sup>ème</sup> élément.

```{codeplay}
a = [1, 2, 3, 4]
a.pop(1)
print(a)
```

La méthode `clear()` enlève tous les éléments.

```{codeplay}
a = [1, 2, 3, 4]
a.clear()
print(a)
```

## Opérations

Les listes disposent aussi de méthodes pour trier et inverser leurs éléments et pour compter un élément spécifique.

La méthode `sort()` trie la liste dans l'ordre croissant (pour les caractères, on se réfère au code ASCII ou UTF utilisé). 
Cette méthode fonctionne uniquement si tous les éléments sont évidemment du même type (nombre, texte) et peuvent être comparés. 

```{codeplay}
m = list('Python')
m.sort()
print(m)
```

La fonction `reverse()` inverse l'ordre de la liste.

```{codeplay}
m = list('Python')
m.reverse()
print(m)
```

La fonction `count(x)` compte le nombre d'occurences de l'élément `x`.

```{codeplay}
m = list('Monty Python')
print(m.count('y'))
```

## Vecteurs

Une liste peut représenter un vecteur.
Pour calculer la **norme d'un vecteur** nous additionnons les carrés des éléments et prenons la racine carrée.

```{codeplay}
a = [1, 4, 7]
norm = 0
for i in a:
    norm += i**2
    
norm = norm ** 0.5
print(norm)
```

Pour **additionner deux vecteurs**, il faut additionner chacun de leurs éléments.

```{codeplay}
a = [1, 4, 7]
b = [2, 1, 2]
result = [0, 0, 0]
for i in range(3):
    result[i] = a[i] + b[i]
print(result)
```

Pour multiplier un vecteur avec un **scalaire k**, il faut multiplier chaque élément avec ce scalaire.

```{codeplay}
a = [1, 4, 7]
result = [0, 0, 0]
k = 2
for i in range(3):
    result[i] = a[i] * k
print(result)
```

Pour calculer le **produit scalaire** de deux vecteurs, il faut additionner le produit des éléments des vecteurs.

```{codeplay}
a = [1, 4, 7]
b = [2, 1, 2]
s = 0
for i in range(3):
    s += a[i] * b[i]
print(s)
```

## Compréhension de liste
Une **compréhension de liste** est une spécificité «élégante» du langage Python qui permet de construire de manière compacte des listes sur une seule ligne.

Voici un exemple de construction «traditionnelle» d'une liste où on ajoute un élément après l'autre avec une boucle :


```{codeplay}
cubes = []
for i in range(10):
    cubes.append(i ** 3)
print(cubes)
```

En utilisant la compréhension de liste, on peut construire la même liste sur une seule ligne :

```{codeplay}
cubes = [i ** 3 for i in range(10)]
print(cubes)
```

On peut comprendre cette formulation de la manière suivante : *«la liste cubes indicée par i prend la valeur i<sup>3</sup> pour toutes les valeurs de i de 0 à 9.»*

Une condition peut être ajoutée dans la compréhension (par exemple, pour n'ajouter à la liste que les valeurs impaires) :

```{codeplay}
a = []
for i in range(10):
    if i % 2 == 1:
        a.append(i ** 2)
print(a)
```
*Note : l'opérateur % est l'opérateur modulo, c'est à dire renvoie le reste de la division par 2.*

Nous pouvons alors écrire la formation de cette liste en une seule ligne.

```{codeplay}
a = [i**2 for i in range(10) if i % 2 == 1]
print(a)
```

## <span commented>La pile (LIFO)</span><!-- REVIEW/JPP: je pense qu'on a besoin de faire maintenant pas mal d'exercices sur les listes avant de pouvoir comprendre le reste. Je ne trouve pas super clair dans la présentation actuelle le parallèle entre list et stack. On vient d'apprendre à manier des listes en Python avec leurs primitives, bien; mais maintenant, on a l'impression qu'on va aprrendre d'autres structures de données (pile et tampon) et on ne sait pas si c'est différent des listes ou pas. Il faudrait que ce soit vraiment clair, et que les exemples sont plus concrets, parce que ces valeurs numériques ne veulent pas dire grand-chose ou ne représente pas un problème ou une situation de la vie réelle. Pour moi, on n'a simplement pas besoin de parler de stack ou queue ici, mais on peut mettre en pratique des listes dans des exercices où elles ont ce genre de fonctionnement -->

Une **pile** est une structure de données qui permet de gérer un <span commented>ensemble</span><!-- REVIEW/JPP: pas un ensemble; une séquence, voire une série si on veut être un peu plus souple avec les termes --> d'éléments et leur arrivée et départ dans le temps. Dans une pile le dernier élément arrivé est le premier à partir.

Cette structure s'appelle **stack** en anglais ou **LIFO** (last in first out)

```{codeplay}
pile = [3, 1]
pile.append(4)
pile.append(1)
print(pile)
pile.pop()
print(pile)
```

## Le tampon (FIFO)

Le **tampon** (ou file d'attente) est une structure de données qui permet de gérer des éléments et leur arrivée et départ. Dans une file d'attente, le premier élément arrivé est le premier à partir.

Cette structure s'appele **buffer** en anglais ou **FIFO** (first in first out)

```{codeplay}
tampon = ['h', 'a']
tampon.append('m')
print(tampon)
pop(0)
print(tampon)
```
<br> <br>

## Exercices

````{admonition} Exercice 1 : semaine permutée
:class: note
Écrivez un programme qui créé une liste *semaine* comprenant tous les jours de la semaine, puis successivement effectuez les actions suivantes :

1 - affichez la liste *semaine*

2 - affichez le 3ème jour de la semaine

3 - permutez le 2ème et le 4ème jour de la semaine en utilisant la valeur d'index -1

4 - affichez à nouveau la liste *semaine* ; que constatez-vous ?

4 - affichez 7 fois la valeur du dernier terme de la liste

```` 


````{admonition} Solution
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 
           'samedi', 'dimanche']

print(semaine)

<br>

print(semaine[2])

<br>

semaine[-1] = semaine[1]

semaine[1] = semaine[3]

semaine[3] = semaine[-1]

<br>

print(semaine)

<br>

print(7*semaine[len(semaine)-1])

```
````


````{admonition} Exercice 2 : 
:class: note
......
```` 

````{admonition} Exercice 3 : 
:class: note
......
````

````{admonition} Exercice 4 : 
:class: note
......
```` 

````{admonition} Exercice 5 : 
:class: note
......
```` 

 

