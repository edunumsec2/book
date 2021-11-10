# Dictionnaires

En Python, un _dictionnaire_ est une structure de données qui, comme une liste, contient plusieurs éléments, mais plus puissant. Dans une liste les indices sont des entiers. Dans un dictionnaire les indices peuvent être de n'importe quel type immuable (entier, nombre, texte, tuple, ...).

![](dict.jpg)

La fonction `dict` crée un dictionnaire vide. On pourrait aussi le créer avec une paire d'accolades `{}`. 

```{code-cell} ipython3
d = dict()
d
```

## Mémoire associative

Un dictionnaire associe une série de **clés** à une autre série de **valeurs**. Cette structure est aussi appelée 

- <span commented>mémoire</span><!-- REVIEW/JPP: structure plutôt que mémoire --> associative
- table de hachage

Ce type de structures de données est standard dans les langages récentes (JavaScript, Python, Ruby) mais absent les langages plus anciens (C, Fortran).

## Un pair `key:value`
Un dictionnaire est un ensemble de pairs `key:value` (clé:valeur) qui sont séparé par un deux-points(`:`). Un dictionnaire est un ensemble ayant la forme `{k:v, k1:v1, ...}`

Voici un exemple d'un dictionnaire avec deux entrées.

```{codeplay}
fr_en = {'un':'one', 'deux':'two'}
print(fr_en)
```
**Exercice**: ajoutez une paire clé:valeur supplémentaire.

Un autre exemple pour un dictionnaire est la table du code Morse

```{codeplay}
Morse = {'a':'.-', 'b':'-...', 'c':'-.-.'}
print(Morse)
```

**Exercice**: ajoutez le code pour 3 lettres en plus.

Un dictionnaire est représenté par ceci:

- il est délimité par des accolades (`{}`)
- ses éléments sont séparés par des virgules (`,`)
- chaque élément est une paire **clé:valeur**, où la clé vient en premier, séparée de la valeur associée par un deux-points (`:`)

## Accéder par une clé
Pour récupérer la valeur associée à une clé, nous utilisons la clé entre crochets (`[]`) — de façon similaire à ce que nous avions fait avec les index des éléments d'une liste.

```{codeplay}
en_fr = {'un':'one', 'deux':'two'}
Morse = {'a':'.-', 'b':'-...', 'c':'-.-.'}

print(en_fr['un'])
print(Morse['a'])
```

De nouveaux éléments peuvent être ajoutés dans n'importer quel ordre avec l'expression `d[key]=value`

```{codeplay}
en_fr = {'un':'one', 'deux':'two'}
en_fr['dix'] = 'ten'
print(en_fr)
```

Avec la fonction `len`, nous trouvons la taille du dictionnaire, c'est-à-dire le nombre de paires clé-valeur qu'il contient.

```{codeplay}
Morse = {'a':'.-', 'b':'-...', 'c':'-.-.'}
print(len(Morse))
```

**Exercice**: Ajoutez une paire et vérifiez la nouvelle longueur du dictionnaire.

Avec l'opérateur spécial `in`, on peut tester si une clé donnée fait partie du dictionnaire.

```{codeplay}
fr_en = {'un':'one', 'deux':'two'}
print('deux' in fr_en)
print('trois' in fr_en)
```

Attention, le test est fait avec les clés, et non pas avec les valeurs.

## Compter (histogramme)

Un dictionnaire est une structure idéale pour compter les éléments appartenant à différentes catégories. Par exemple si nous voulons compter l'apparence de chaque lettre dans un texte nous pouvons utiliser un dictionnaire.<!-- REVIEW/JPP: J'ai un peu de peine avec ces esemples où beaucoup de variables n'ont plus qu'une lettre. Un œil avertit comprend que d est un dictonnaire, c est un caractère, etc., mais je pense que c'est promouvoir, par les exemples mêmes qui sont censés être exemplaires, un style volontairement cryptique et difficile d'accès. On pourrait appeler ce dictionnaire letter_counts, et la variable de boucle letter par exemple. -->

```{codeplay}
phrase = 'dictionnaire'
d = {}
for lettre in phrase:
    if lettre in d:
        d[lettre] += 1
    else:
        d[lettre] = 1
print(d)
```

On appelle cette structure aussi un **histogramme**. Il nous montre que

- la lettre **d** apparait une fois,
- la lettre **i** apparait trois fois.

Si nous accédons à une clé qui n'existe pas dans le dictionnaire, nous obtenons une erreur du type `KeyError`.
```{codeplay}
fr_en = {'un':'one', 'deux':'two'}
print(fr_en['trois'])
```

<span commented>La fonction `get` permet d'obtenir une valeur par défaut</span><!-- REVIEW/JPP: dire auparavant que faire un lookup avec [] et une clé non existante est une erreur -->, si la clé n'existe pas encore dans_ le dictionnaire. Par exemple la lettre **b** n'est pas une clé du dictionnaire. La fonction retourne alors sa valeur par défaut qui est 0.

```ipython
d.get('b', 0)
```

Ceci nous permet de raccourcir le programme de l'histogramme encore plus.

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
d = {'d': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 2, 'a': 1, 'r': 1, 'e': 1}
for c in d:
    print(c, d[c])
```

Transformer un dictionnaire en liste nous retourne une liste de ses clés.

```{codeplay}
d = {'d': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 2, 'a': 1, 'r': 1, 'e': 1}
print(list(d))
```

La fonction `sorted` nous retourne une liste de ses clés, triée.

```{codeplay}
d = {'d': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 2, 'a': 1, 'r': 1, 'e': 1}
print(sorted(d))
```

## List et ensemble des valeurs

La méthode `values` retourne toutes les valeurs.

```{codeplay}
d = {'d': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 2, 'a': 1, 'r': 1, 'e': 1}
print(d.values())
```

Nous pouvons les transformer en liste ordinaire.

```{codeplay}
d = {'d': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 2, 'a': 1, 'r': 1, 'e': 1}
print(list(d.values()))
```

Nous pouvons également la transformer en **ensemble** et <span commented>éliminer les doublons</span><!-- REVIEW/JPP: c'est la première fois qu'on parle de sets... à mon avis, soit on en fait une section à part entière parce qu'on se dit que ça vaut la peine, soit on laisse tomber parce qu'il y a déjà assez comme ça. Préférence pour la seconde solution. -->.

```{codeplay}
d = {'d': 1, 'i': 3, 'c': 1, 't': 1, 'o': 1, 'n': 2, 'a': 1, 'r': 1, 'e': 1}
print(set(d.values()))
```

## Inverser un dictionnaire

<span commented>Toutes les clés d'un dictionnaire sont uniques</span><!-- REVIEW/JPP: Nous devrions mentionner ceci plutôt lors de la description de la structure d'un dictionnaire, aussi avec un exemple qui montre qu'insérer deux fois la même clé remplace la première valeur associée -->. Par contre, il est tout à fait possible d'avoir plusieurs valeurs qui sont identiques. Si nous <span commented>inversons</span><!-- REVIEW/JPP: il faut mieux définir ce qu'“inverser” veut dire, à mon avis --> un dictionnaire, une valeur peut correspondre à plusieurs clés, ce que nous pouvons alors stocker dans une liste. <!-- REVIEW/JPP: Je trouve très complexe, il y a beaucoup de choses qui se cachent dans cet exemple et qui ne sont à mon avis pas assez explicites. -->

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
