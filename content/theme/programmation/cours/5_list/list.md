---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Listes

Une liste est un <span commented>ensemble d'objets</span><!-- REVIEW/JPP: pas un ensemble, mais une séquence (linéaire). et, de nouveau, je parlerais de valeurs plutôt que d'objets -->. En Python, syntaxiquement, une liste

- est délimitée par des crochets `[]`
- ses éléments sont séparés par des virgules `,`

Voici un <span commented>exemple</span><!-- REVIEW/JPP: il me semble que c'est un mauvais exemple que de leur montrer directement des listes hétérogènes, alors que les bonnes pratiques tendent quand même à faire en sorte que les listes soient homogènes et qu'on utilise plutôt des tuples pour des données hétérogènes -->:

```{code-cell} ipython3
a = [123, 'abc', True]
```

La fonction `len` retourne la longueur d'une liste, le nombre d'éléments qu'elle contient.

```{code-cell} ipython3
len(a)
```

La fonction `print` peut imprimer une liste. 

```{code-cell} ipython3
print(a)
```

Nous pouvons accéder à un élément de la liste en utilisant un numéro entre crochets `[]`, appelé _index_. L'index d'un élément est toujours un nombre entier. En Python, comme dans beaucoup de langages de programmation, l'index pour le premier élément de la liste est 0 et non pas 1. Ainsi, les éléments d'une liste de longueur `n` auront comme premier index 0 et comme dernier index `n - 1`.

```{code-cell} ipython3
a[0]
```

## La fonction `list`

La fonction `list` peut transformer un <span commented>itérable (plage, chaine, ensemble, ...)</span><!-- REVIEW/JPP: on ne connaît encore rien à part la chaîne de caractères, et on n'a que brièvement parlé de range() sans bien la définir. À mon avis, on n'en a pas besoin à ce stade. --> en liste.

```{code-cell} ipython3
list(range(10))
```

La fonction `list` transforme une chaîne en liste.

```{code-cell} ipython3
m = list('Monty Python')
m
```

## Index

+++

<span commented>Les crochets</span><!-- REVIEW/JPP: On a déjà mentionné cela une sous-section plus haut. Proposition: virer la fonction list() (ou la mettre en en bas de la page) et fusionner ces indications-ci avec la première section de la page --> permettent d'accéder à un élément spécifique de la liste, à l'aide d'un entier, commençant par 0. Cet index est placé entre <span commented>crochets</span><!-- REVIEW/JPP: je n'aime pas trop que ces exemples donnent la même chose si m est un str ou si m est une liste de str, syntaxiquement; ça incite à la confusion. On pourrait utiliser une liste de int pour ne pas avoir ce souci --> `[]`.

```{code-cell} ipython3
m[0], m[4], m[6]
```

Un index négatif désigne un élément d'une liste depuis la fin de la liste.

```{code-cell} ipython3
m[-1], m[-2], m[-5]
```

## Tranche

La notation `[i:j]`, après le nom d'une variable qui contient une liste, permet d'extraire <span commented>une tranche (un sous-ensemble) de la liste</span><!-- REVIEW/JPP: pas un sous-ensemble. Proposition: d'extraire une partie de la liste telle qu'identifiée par les deux index `i` et `j`. -->.

L'expression suivante extrait la <span commented>sous-liste du 3e au 5e élément</span><!-- REVIEW/JPP: ceci est tellement bizarre pour qui le lit la première fois que ça mérite une explication sur comment ces index sont traités -->.

```{code-cell} ipython3
m[2:5]
```

L'expression suivante extrait la sous-liste du début au 4e élément.

```{code-cell} ipython3
m[:4]
```

Ceci extrait la sous-liste du 8e élément à la fin.

```{code-cell} ipython3
m[8:]
```

Ceci extrait les éléments à partir de l'avant-dernier, jusqu'à la fin.

```{code-cell} ipython3
m[-2:]
```

## Itération sur une liste

La boucle `for` peut itérer sur les éléments d’une une liste. La variable d’itération prend successivement la valeur de chaque élément de la liste.

```{code-cell} ipython3
for x in a:
    print(x)
```

## Ajouter des éléments

Différentes <span commented>méthodes</span><!-- REVIEW/JPP: on n'a encore jamais parlé de méthode, à mon avis on ne peut pas leur poser ça comme ça sur la table sans autre forme de procès. On pourrait commencer par dire qu'une liste est modifiable, montrer comment modifier des éléments existants, puis dans un deuxième temps montrer qu'on peut faire des changements plus conséquents en utilisant une nouvelle notation consistant en ce qu'on appelle les méthodes --> permettent d’ajouter des éléments à une liste existante:

- `append(x)`
- `extend(iterable)`
- `insert(i, x)`

Partons d'une liste simple.

```{code-cell} ipython3
a = [1, 2, 3]
```

La méthode `<span commented>list</span><!-- REVIEW/JPP: il faut dire que list est une variable qui contient une liste, parce qu'autrement on se plante en se demandant tout à coup pourquoi list n'est plus la fonction pour convertir en liste qu'on connaît d'avant... -->.append(x)` permet d'ajouter un élément `x` à la fin de la liste.

```{code-cell} ipython3
a.append(99)
a
```

La méthode `list.extend(itéarable)` ajoute plusieurs éléments. Un itérable est une séquence tel que liste, chaîne de texte, ensemble, tuple, ...

```{code-cell} ipython3
a.extend([10, 11])
a.extend('abc')
a
```

La méthode `list.insert(i, x)` insert un nouveau élément `x` à la i-ième position.

```{code-cell} ipython3
a.insert(2, 999)
a
```

## Enlever des éléments

Les méthodes suivantes permettent d'enlever des éléments:

- `remove(x)`
- `pop(i)`
- `clear()`

La méthode `list.remove(x)` enlève l'élément `x` s'il existe, et donne une erreur autrement.

```{code-cell} ipython3
a.remove(999)
a
```

La méthode `list.pop()` enlève le dernier élément.

```{code-cell} ipython3
a.pop()
a
```

La méthode `list.pop(i)` enlève le i-ème élément.

```{code-cell} ipython3
a.pop(1)
a
```

La méthode `list.clear()` enlève tous les éléments.

```{code-cell} ipython3
a.clear()
a
```

## Opérations

Les listes disposent aussi de méthodes pour trier et inverser ses éléments et pour compter un élément spécifique.

```{code-cell} ipython3
m = list('Monty Python')
m
```

La méthode `list.sort()` trie la liste. 
Cette méthode fonctionne uniquement si tous les éléments sont du même type (nombre, texte) et peuvent être comparés. 

```{code-cell} ipython3
m.sort()
m
```

La fonction `list.reverse()` inverse la <span commented>liste</span><!-- REVIEW/JPP: encore une fois, je ne suis pas fan du manque d'idempotence des cellules ici -->.

```{code-cell} ipython3
m.reverse()
m
```

La fonction `list.count(x)` compte le nombre d'occurences de l'élément `x`.

```{code-cell} ipython3
m.count('y')
```

## <span commented>La pile (LIFO)</span><!-- REVIEW/JPP: je pense qu'on a besoin de faire maintenant pas mal d'exercices sur les listes avant de pouvoir comprendre le reste. Je ne trouve pas super clair dans la présentation actuelle le parallèle entre list et stack. On vient d'apprendre à manier des listes en Python avec leurs primitives, bien; mais maintenant, on a l'impression qu'on va aprrendre d'autres structures de données (pile et tampon) et on ne sait pas si c'est différent des listes ou pas. Il faudrait que ce soit vraiment clair, et que les exemples sont plus concrets, parce que ces valeurs numériques ne veulent pas dire grand-chose ou ne représente pas un problème ou une situation de la vie réelle. Pour moi, on n'a simplement pas besoin de parler de stack ou queue ici, mais on peut mettre en pratique des listes dans des exercices où elles ont ce genre de fonctionnement -->

Une **pile** est une structure de données qui permet de gérer un <span commented>ensemble</span><!-- REVIEW/JPP: pas un ensemble; une séquence, voire une série si on veut être un peu plus souple avec les termes --> d'éléments et leur arrivée et départ dans le temps. Dans une pile le dernier élément arrivé est le premier à partir.

Cette structure s'appelle **stack** en anglais ou **LIFO** (last in first out)

```{code-cell} ipython3
pile = [3, 1]
pile.append(4)
pile.append(1)
pile
```

```{code-cell} ipython3
pile.pop()
```

```{code-cell} ipython3
pile
```

## Le tampon (FIFO)

Le **tampon** (ou le file d'attente) est une structure de données qui permet de gérer des éléments et leur arrivée et départ. Dans une file d'attente, le premier élément arrivé est le premier à partir.

Cette structure s'appele **buffer** en anglais ou **FIFO** (first in first out)

```{code-cell} ipython3
tampon = ['h', 'a']
tampon.append('m')
tampon
```

```{code-cell} ipython3
tampon.pop(0)
```

```{code-cell} ipython3
tampon
```

## Vecteurs

+++

Une liste peut représenter un vecteur.

```{code-cell} ipython3
a = [1, 4, 7]
b = [2, 1, 2]
```

Pour calculer la **norme d'un vecteur** nous additionnons les carrés des éléments et prenons la racine carrée.

```{code-cell} ipython3
norm = 0
for i in a:
    norm += i**2
    
norm ** 0.5
```

Pour **additionner deux vecteurs**, il faut additionner chacun de leurs éléments.

```{code-cell} ipython3
c = [0, 0, 0]
for i in range(3):
    c[i] = a[i] + b[i]
c
```

Pour multiplier un vecteur avec un **scalaire k**, il faut multiplier chaque élément avec ce scalaire.

```{code-cell} ipython3
k = 2
for i in range(3):
    c[i] = a[i] * k
c
```

Pour calculer le **produit scalaire** de deux vecteurs, il faut additionner le produit des éléments des vecteurs.

```{code-cell} ipython3
s = 0
for i in range(3):
    s += a[i] * b[i]
s
```

## Compréhension de liste
Une **compréhension de liste** est une manière compacte de construire des listes sur une seule ligne.

Voici un exemple de construction «traditionnelle» d'une liste où on ajoute un élément après l'autre avec une boucle:

```{code-cell} ipython3
carres = []
for i in range(10):
    carres.append(i ** 2)
carres
```

En utilisant les compréhension des listes, on peut construire la même liste sur une seule ligne:<!-- REVIEW/JPP: à mon avis, il faut davantage commenter et expliquer ceci, notamment comment la lire et l'interpréter -->

```{code-cell} ipython3
[i ** 2 for i in range(10)]
```

Une condition peut être ajoutée dans la <span commented>compréhension</span><!-- REVIEW/JPP: oui mais le prochain exemple n'est pas une compréhension de liste, c'est confusing --> (par exemple, pour n'ajouter à la liste que les <span commented>valeurs impaires</span><!-- REVIEW/JPP: le test ' % 2 == 1' va sûrement poser bcp de questions si pas expliqué... je ne sais plus si on a parlé de l'opérateur %-->):

```{code-cell} ipython3
a = []
for i in range(10):
    if i % 2 == 1:
        a.append(i ** 2)
a
```

Nous pouvons alors écrire la formation de cette liste en une seule ligne.

```{code-cell} ipython3
[i**2 for i in range(10) if i % 2 == 1]
```

## <span commented>Tuples</span><!-- REVIEW/JPP: Si on veut parler des tuples, ce qui me semble aussi un peu ambitieux, il nous faut une section qui discute quand on utilise des listes et quand on utilise des tuples. C'est compliqué. Pour éviter la discussion, j'éviterais simplement de parler des tuples. J'ai l'impression qu'à ce stade, ils ne maîtriseront pas encore les listes qu'on leur colle direct un truc qui est un peu la même chose, mais pas tout à fait, et qu'au final ça brouille les pistes. -->

Le tuple est une structure similaire à une liste, mais immuable. On peut accéder à des éléments via un index, mais on ne peut pas réaffecter un élément. Le tuple est une structure statique.

```{code-cell} ipython3
t = (1, 'abc', True)
```

```{code-cell} ipython3
t[1]
```

 Essayer de réaffecter un élément d'un tuple produit une erreur.
 
     t[1] = 'x'
    
    TypeError: 'tuple' object does not support item assignment

+++

La fonction `tuple` transforme un itérable (liste, chaine de caractères, plage...) en tuple

```{code-cell} ipython3
tuple('abc')
```

```{code-cell} ipython3
tuple(range(5))
```

Les parenthèses ne sont pas nécessaires. Une séquence d'objets séparés par des virgules est transformée automatiquement en tuple.

```{code-cell} ipython3
x = 1, 2, 4
x
```

En utilisant des tuples, plusieurs variables peuvent être affectées sur une seule ligne, avec le même nombre de valeurs.

```{code-cell} ipython3
a, b = 1, 9
a, b
```

Ceci est un technique courante pour <span commented>inverser la valeur de deux variables</span><!-- REVIEW/JPP: On en a déjà parlé dans un chapitre précédent. Comme c'est quelque chose qu'on comprend bien avec les tuples, je serais d'avis de le virer de là où il était avant et de le garder ici — à moins qu'on ne garde pas les tuples comme suggéré plus haut, alors je laisserais de manière moins formelle l'exemple a, b = b, a où il est actuellement en premier. -->.

```{code-cell} ipython3
a, b = b, a
a, b
```

```{code-cell} ipython3

```
