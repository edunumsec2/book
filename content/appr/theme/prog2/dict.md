# Associer - `dict`

En Python, un _dictionnaire_ est une structure de données qui, comme une liste, contient plusieurs éléments, mais est plus puissante. Dans une liste les indices sont des entiers. Dans un dictionnaire les indices peuvent être de n'importe quel type immuable (entier, nombre, texte, tuple, ...).

![](media/dict.jpg)

La fonction `dict` crée un dictionnaire vide. On pourrait aussi créer ce dictionnaire avec une paire d'accolades `{}`. 

```{code-block} python
d = dict()
d
```

## Mémoire associative

Un dictionnaire associe une série de **clés** à une autre série de **valeurs**. Cette structure est aussi appelée :

- structure associative,
- table de hachage.

Toutes les clés d'un dictionnaire sont uniques. De ce fait, si on insère deux fois la même clé, on remplace la première valeur associée. 

```{codeplay}
trees = {'un':'peuplier', 'deux':'chêne'}
print(trees)
trees = {'un':'peuplier', 'deux':'chêne', 'un':'hêtre'}
print(trees)
```

Ce type de structures de données est standard dans les langages récents (JavaScript, Python, Ruby, ...) mais absent des langages plus anciens (C, Fortran, etc.).

## La paire `clé:valeur`
Un dictionnaire est un ensemble de paires clé-valeur (`key:value`) séparées par deux-points (`:`). Un dictionnaire est donc un ensemble ayant la forme `{k1:v1, k2:v2, ...}`, par exemple :

    dico = {"voiture": "véhicule à 4 roues", "moto": "véhicule à 2 roues"} 

ou encore :

```{codeplay}
fr_en = {'un':'one', 'deux':'two'}
print(fr_en)
```

**Exercice** : ajoutez une paire *clé:valeur* supplémentaire.

Un autre exemple pour un dictionnaire est la table du code Morse.

```{codeplay}
Morse = {'a':'.-', 'b':'-...', 'c':'-.-.'}
print(Morse)
```

**Exercice** : complétez le code pour trois lettres supplémentaires.

La syntaxe d'un dictionnaire est la suivante :

- un dictionnaire est délimité par des accolades (`{}`),
- ses éléments sont séparés par des virgules (`,`),
- chaque élément est une paire *clé:valeur*, où la clé vient en premier, séparée de la valeur associée par deux-points (`:`).

## Accéder par une clé
Pour récupérer la valeur associée à une clé, nous utilisons la clé entre crochets (`[]`) — de façon similaire à ce que nous avions fait avec les index des éléments d'une liste.

```{codeplay}
en_fr = {'un':'one', 'deux':'two'}
Morse = {'a':'.-', 'b':'-...', 'c':'-.-.'}

print(en_fr['un'])
print(Morse['a'])
```

De nouveaux éléments peuvent être ajoutés dans n'importe quel ordre avec l'expression `d[key]=value`.

```{codeplay}
en_fr = {'un':'one', 'deux':'two'}
en_fr['dix'] = 'ten'
print(en_fr)
```

La fonction `len` sort la taille du dictionnaire, c'est-à-dire le nombre de paires *clé-valeur* qu'il contient.

```{codeplay}
Morse = {'a':'.-', 'b':'-...', 'c':'-.-.'}
print(len(Morse))
```

**Exercice** : ajoutez une paire et vérifiez la nouvelle longueur du dictionnaire.

Avec l'opérateur spécial `in`, on peut tester si une clé donnée fait partie du dictionnaire.

```{codeplay}
fr_en = {'un':'one', 'deux':'two'}
print('deux' in fr_en)
print('trois' in fr_en)
```

Attention, le test est fait avec les clés, et non pas avec les valeurs !

## Compter (histogramme)

Un dictionnaire est une structure idéale pour compter les éléments appartenant à différentes catégories. On peut l'utiliser par exemple si l'on souhaite compter l'occurence de chaque lettre dans un texte.

```{codeplay}
phrase = 'dictionnaire'
letter_count = {}
for letter in phrase:
    if letter in d:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
print(letter_count)
```

On appelle cette structure aussi un **histogramme**. Il montre ici que :

- la lettre **d** apparait une fois,
- la lettre **i** apparait trois fois.

Si on tente d'accéder à une clé qui n'existe pas dans le dictionnaire, on obtient une erreur du type `KeyError`.
```{codeplay}
fr_en = {'un':'one', 'deux':'two'}
print(fr_en['trois'])
```

La fonction `get` permet d'obtenir une valeur par défaut</span><!-- REVIEW/JPP: dire auparavant que faire un lookup avec [] et une clé non existante est une erreur -->, si la clé n'existe pas encore dans le dictionnaire. Par exemple la lettre **b** n'est pas une clé du dictionnaire ; la fonction retourne alors sa valeur par défaut qui est 0.

```ipython
d.get('b', 0)
```

Ceci nous permet de raccourcir encore davantage le programme de l'histogramme.

```{codeplay}
phrase = 'dictionnaire'
d = {}
for c in phrase:
    d[c] = d.get(c, 0) + 1
print(d)
```

## Itération sur les clés
Nous pouvons itérer sur les clés d'un dictionnaire.<!-- REVIEW/JPP: Cet exemple me semble aussi très cryptique avec ces noms de variables -->

```{codeplay}
dico = {'d': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 2, 'a': 1, 'r': 1, 'e': 1}
for c in dico:
    print(c, dico[c])
```

Transformer un dictionnaire en liste nous retourne une liste de ses clés.

```{codeplay}
dico = {'d': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 2, 'a': 1, 'r': 1, 'e': 1}
print(list(dico))
```

La fonction `sorted` nous retourne une liste de ses clés, triée.

```{codeplay}
dico = {'d': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 2, 'a': 1, 'r': 1, 'e': 1}
print(sorted(dico))
```

## Liste et ensemble des valeurs

La méthode `values` retourne toutes les valeurs d'un dictionnaire.

```{codeplay}
dico = {'d': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 2, 'a': 1, 'r': 1, 'e': 1}
print(dico.values())
```

Nous pouvons transformer le dictionnaire en liste ordinaire.

```{codeplay}
dico = {'d': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 2, 'a': 1, 'r': 1, 'e': 1}
print(list(dico.values()))
```

On peut également le transformer en **ensemble** et éliminer les doublons. Les ensembles ou `sets` sont des collections d'éléments non ordonnées, sans index, non redondantes.

```{codeplay}
dico = {'d': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 2, 'a': 1, 'r': 1, 'e': 1}
print(set(dico.values()))
```

## Inverser un dictionnaire

Comme il a été énoncé en début de chapitre, toutes les clés d'un dictionnaire sont uniques. Par contre, il est tout à fait possible d'avoir plusieurs valeurs qui sont identiques. Si on «inverse» un dictionnaire - c'est à dire qu'on cherche pour chaque valeur *image* à retrouver la clé *antécédente* correspondante -, une valeur peut correspondre à plusieurs clés, qui peuvent alors être stockées dans une liste. 

```{codeplay}
d = {'d': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 2, 'a': 1, 'r': 1, 'e': 1}
inverse = {}
for c in d:
    val = d[c]
    if val in inverse:
        inverse[val].append(c)
    else:
        inverse[val] = [c]
print(inverse)
```

<br> <br>

## Exercices

````{admonition} Exercice 1 : 
:class: note
......
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
