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

+++

Pour ajouter un élément à un dictionnaire stocké dans une variable `d`, <span commented>nous</span><!-- REVIEW/JPP: il y a une alternance de 'nous' et de 'on', il faudrait en choisir un et s'y tenir pour être cohérent --> utilisons une <span commented>expression</span><!-- REVIEW/JPP: instruction (en Python, l'affectation avec = n'est pas une expression) --> de la forme `d[clé] = valeur`. Comme pour un 'vrai' dictionnaire qui associe des mots de deux langues, <span commented>nous pouvons définir ceci</span><!-- REVIEW/JPP: Nous avons défini la liste en parlant directement de la syntaxe avec [a,b] pour construire une liste. Pourrions-nous faire la même chose en commençant par construire un dict tout prêt avec {k:v, k:v, etc.} avant de passer par la construction dynamique? Ça aiderait à conceptualiser cette structure diffile à aborder -->.

```{code-cell} ipython3
d['un'] = 'one'
d['deux'] = 'two'
d
```

Un dictionnaire est représenté par ceci:

- il est délimité par des accolades (`{}`)
- ses éléments sont séparés par des virgules (`,`)
- chaque élément est une paire **clé:valeur**, où la clé vient en premier, séparée de la valeur associée par un deux-points (`:`)

Pour récupérer la valeur associée à une clé, nous utilisons la clé entre crochets (`[]`) — de façon similaire à ce que nous avions fait avec les index des éléments d'une liste.

```{code-cell} ipython3
d['deux']
```

De nouveaux éléments peuvent être ajoutés dans n'importer quel ordre.

```{code-cell} ipython3
d['dix'] = 'ten'
d
```

Avec la fonction `len`, nous trouvons la taille du dictionnaire, c'est-à-dire le nombre de paires clé-valeur qu'il contient.

```{code-cell} ipython3
len(d)
```

Avec l'opérateur spécial `in`, on peut tester si une clé donnée fait partie du dictionnaire.

```{code-cell} ipython3
'deux' in d
```

Attention, le test est fait avec les clés, et non pas avec les valeurs.

```{code-cell} ipython3
'two' in d
```

## Compter (histogramme)

+++

Un dictionnaire est une structure idéale pour compter les éléments appartenant à différentes catégories. Par exemple si nous voulons compter l'apparence de chaque lettre dans un texte nous pouvons utiliser un dictionnaire.<!-- REVIEW/JPP: J'ai un peu de peine avec ces esemples où beaucoup de variables n'ont plus qu'une lettre. Un œil avertit comprend que d est un dictonnaire, c est un caractère, etc., mais je pense que c'est promouvoir, par les exemples mêmes qui sont censés être exemplaires, un style volontairement cryptique et difficile d'accès. On pourrait appeler ce dictionnaire letter_counts, et la variable de boucle letter par exemple. -->

```{code-cell} ipython3
phrase = 'dictionnaire'
d = {}
for c in phrase:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
d
```

On appelle cette structure aussi un **histogramme**. Il nous montre que 
- la lettre **d** apparait une fois, 
- la lettre **i** apparait trois fois.

+++

<span commented>La fonction `get` permet d'obtenir une valeur par défaut</span><!-- REVIEW/JPP: dire auparavant que faire un lookup avec [] et une clé non existante est une erreur -->, si la clé n'existe pas encore dans le dictionnaire. Par exemple la lettre **b** n'est pas une clé du dictionnaire. La fonction retourne alors sa valeur par défaut qui est 0.

```{code-cell} ipython3
d.get('b', 0)
```

Ceci nous permet de raccourcir le programme de l'histogramme encore plus.

```{code-cell} ipython3
d = {}
for c in phrase:
    d[c] = d.get(c, 0) + 1
d
```

## Itération sur les clés
Nous pouvons itérer sur les clés d'un dictionnaire.<!-- REVIEW/JPP: Cet exemple me semble aussi très cryptique avec ces noms de variables -->

```{code-cell} ipython3
for c in d:
    print(c, d[c])
```

Transformer un dictionnaire en liste nous retourne une liste de ses clés.

```{code-cell} ipython3
list(d)
```

La fonction `sorted` nous retourne une liste de ses clés, triée.

```{code-cell} ipython3
sorted(d)
```

## List et ensemble des valeurs

La méthode `values` retourne toutes les valeurs.

```{code-cell} ipython3
d.values()
```

Nous pouvons les transformer en liste ordinaire.

```{code-cell} ipython3
list(d.values())
```

Nous pouvons également la transformer en **ensemble** et <span commented>éliminer les doublons</span><!-- REVIEW/JPP: c'est la première fois qu'on parle de sets... à mon avis, soit on en fait une section à part entière parce qu'on se dit que ça vaut la peine, soit on laisse tomber parce qu'il y a déjà assez comme ça. Préférence pour la seconde solution. -->.

```{code-cell} ipython3
set(d.values())
```

## Inverser un dictionnaire

<span commented>Toutes les clés d'un dictionnaire sont uniques</span><!-- REVIEW/JPP: Nous devrions mentionner ceci plutôt lors de la description de la structure d'un dictionnaire, aussi avec un exemple qui montre qu'insérer deux fois la même clé remplace la première valeur associée -->. Par contre, il est tout à fait possible d'avoir plusieurs valeurs qui sont identiques. Si nous <span commented>inversons</span><!-- REVIEW/JPP: il faut mieux définir ce qu'“inverser” veut dire, à mon avis --> un dictionnaire, une valeur peut correspondre à plusieurs clés, ce que nous pouvons alors stocker dans une liste. <!-- REVIEW/JPP: Je trouve très complexe, il y a beaucoup de choses qui se cachent dans cet exemple et qui ne sont à mon avis pas assez explicites. -->

```{code-cell} ipython3
inverse = {}
for c in d:
    val = d[c]
    if val in inverse:
        inverse[val].append(c)
    else:
        inverse[val] = [c]
inverse
```

```{code-cell} ipython3

```
