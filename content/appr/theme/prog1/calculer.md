# Calculer - `int`

Dans ce chapitre, nous allons voir comment un programme peut calculer avec des nombres.
Ceci est utilisé dans une calculatrice ou un tableur.

Les nombres entiers forment une catégorie très importante. En anglais, un entier est appelé **integer** (`int`). Nous allons voir que :

- les opérateurs de base sont `+`, `-`, `*` et `/`,
- les nombres sont du type `int` ou `float`,
- un texte est du type `str`.

```{question}
En informatique, `int` est l'abbréviation pour

{f}`international`  
{v}`entier`  
{f}`interne`  
{f}`intelligent`
```

## Un calcul simple

Dans ce chapitre, nous allons explorer comment nous pouvons calculer avec des nombres. Voici un exemple qui affiche dans une première ligne sous forme de texte une expression mathématique, et dans une deuxième ligne une expression mathématique qui sera évaluée vers son résultat numérique.

```{codeplay}
:file: int0.py
print('2 à la puissance 32 =')
print(2 ** 32)
```

## Opérateurs de base

En Python, nous retrouvons les 4 opérations arithmétiques de base :

- addition (`+`)
- soustraction (`-`)
- multiplication (`*`)
- division (`/`)

```{codeplay}
:file: int1.py
print('3 + 4 =', 3 + 4)
print('3 - 4 =', 3 - 4)
print('3 * 4 =', 3 * 4)
print('3 / 4 =', 3 / 4)
```

**Exercice** : Modifiez les 4 calculs et exécutez de nouveau.

```{question}
Quel est le résultat de l'expression `'12' + '12'` ?  
{f}`12`  
{f}`24`  
{v}`1212`  
{f}`1221`  
```

## Opérateurs avancés

En Python, nous avons également 3 opérateurs supplémentaires :

- puissance (`**`),
- division entière (`//`),
- reste de la division entière ou modulo (`%`).

```{codeplay}
:file: int2.py
print('7 ** 3 =', 7 ** 3)
print('7 // 3 =', 7 // 3)
print('7 % 3 =', 7 % 3)
```

**Exercice** : Modifiez les 3 calculs et exécutez de nouveau.

```{question}
Quel est le résultat de l'expression `1 + 2 * 3` ?

{f}`1`
{f}`2`
{f}`3`
{f}`6`
{v}`7`
{f}`9`
```

## Les variables

Une **variable** est une manière de designer une valeur par un nom. Le terme technique pour associer une valeur à une variable est **affectation** et elle utilise le symbole `=` (égal).

Mais faites attention ! Il ne s'agit pas d'une équation dans le sens mathématique. La variable doit toujours figurer seule à gauche.
La forme générique d'une affectation est `var = expression`.

```{codeplay}
:file: int3.py
r = 2
pi = 3.14

print('rayon =', r)
print('diamètre =', 2 * r)
print('circonférence =', pi * 2 * r)
```

**Exercice** : Ajoutez le calcul de la surface du cercle.

Pour nommer une variable vous pouvez utiliser :

- lettres (`a...z` et `A...Z`),
- chiffres (`0...9`),
- le tiret bas (`_`).

Le nom de variable :

- est sensible aux majuscules/minuscules,
- ne peut pas commencer avec un chiffre,
- ne doit pas consister d'un mot-clé (`if`, `else`, `for`),
- ne doit pas contenir un caractère spécial (`* + % & $ - / ?`).

Ces noms de variables sont donc valides : `a2`, `_a`, `speed`, `pos_x`, `POS_X`

Ceux-ci sont invalides :

- `2var` (commence avec un chiffre),
- `if` (correspond à un mot-clé),
- `var$2` (contient un caractère spécial),
- `mon nom` (contient une espace et est interprété comme deux noms de variables).

```{question}
Lesquels des noms de variable sont valides ?

{f}`var 2`  
{v}`var2`  
{f}`2var`  
{f}`if`  
{v}`IF_VAR`
```

Voici un autre calcul où `a` et `b` désignent largeur et hauteur d'un rectangle.

```{codeplay}
:file: int4.py
a = 3
b = 5

print('largeur =', a)
print('hauteur =', b)
print('surface =', a * b)
print('périmètre =')
print('diagonale =')
```

**Exercice** : Complétez le calcul du périmètre et de la diagonale.

```{question}
Quels noms de variable sont valides ?

{f}`if`  
{v}`VAR_2`  
{v}`_if`  
{v}`elseif`  
{f}`var$2`
```

## Les types

Un ordinateur peut manipuler différentes catégories d'objets telles que image, texte, nombre. On parle alors du type de ces données.

La fonction `type()` retourne le type d'un objet.

```{codeplay}
:file: int5.py
print(type('hello'))
print(type(123))
print(type(3.14))
```

**Exercice** : Trouvez encore d'autres types.

L'exemple ci-dessus nous montre que

- `str` (string) désigne des chaînes de caractères,
- `int` (integer) désigne des nombres entiers,
- `float` (floating point) désigne des nombres à virgule flottante.

## Conversion de type

Les trois fonctions `str()`, `int()` et `float()` permettent de transformer d'un type à un autre.

Par exemple, la chaîne `'123'` peut être transformée soit en entier, soit en nombre à virgule flottante.

```{codeplay}
:file: int6.py
a = '123'
b = int(123)
c = float(123)

print(b, c)
print(type(a))
print(type(b))
print(type(c))
```

Nous reconnaissons la différence entre un entier (`int`) et un nombre à virgule flottante (`float`) par la présence du point décimal (`123.0`).

## Obtenir un nombre

La fonction `input()` permet d'obtenir une entrée de l'utilisateur. La valeur retournée est une chaine de caractères. Pour pouvoir l'utiliser dans un calcul nous devons la transformer en virgule flottante avec la fonction de conversion `float()`.

```{codeplay}
:file: int7.py
r = float(input('Entrez le rayon: '))
pi = 3.14

print('rayon =', r)
print('diamètre =', 2 * r)
print('circonférence =', pi * 2 * r)
print('surface =')
```

**Exercice** : Complétez le programme pour afficher la surface du cercle.

Nous pouvons également créer des programmes où nous demandons plusieurs valeurs à l'utilisateur. Cette fois, nous permettons seulement l'utilisation de nombres entiers, et donc transformons la chaine obtenu avec `int()` en nombre entier.

```{codeplay}
:file: int8.py
a = int(input('Entrez la largeur: '))
b = int(input('Entrez la longeur: '))

print('surface =', a * b)
print('périmètre =')
print('diagonale =')
```

**Exercice** : Complétez le programme pour afficher le périmètre et la diagonale.

## Affectation multiple

Python permet d'affecter plusieurs variables sur une même ligne.
Ceci est parfois utilisé pour assigner des coordonnées.

```{codeplay}
:file: int9.py
x, y = 3, 4
print(x, y)
```

L'affectation multiple est une manière élégante d'échanger les valeurs de deux variables.

```{codeplay}
:file: int10.py
x, y = 3, 4
print(x, y)

x, y = y, x
print(x, y)
```

**Exercice** : Ajoutez une 3e variable et faites une permutation cyclique.

## Revisiter le `tuple`

L'affectation multiple utilise le format du tuple.
Un **n-uplet** (tuple) est une séquence d'objets. Ce sont :

- multiple valeurs séparé par une virgule,
- une seule valeur terminé par une virgule,
- des parenthèses vides pour le tuple vide.

```{codeplay}
x = 1, 2    # deux valeurs
y = 1,      # une seul valeur (virgule !)
z = ()      # tuple vide

print(x)
print(y)    
print(z)
print(type(x))
```

## Position `(x, y)`

Un tuple est la forme idéale pour représenter les deux coordonnées `(x, y)` d'un point. Nous allons dorénavant utiliser la lettre `p` pour point (ou position). Si deux points sont nécessaire, nous les appellerons `p` et `q`.

Pour accéder aux coordonnées `x` et `y` du point `p` nous utilisons un indice (un entier entre crochets) :

- `x = p[0]`
- `y = p[1]`

La fonction `goto()` accepte :

- deux coordonnées séparés `goto(x, y)`
- deux coordonnées dans un tuple `goto(p)`

Nous pouvons maintenant définir une fonction compacte et élégante pour dessiner une ligne entre deux points `p` et `q`.

```{codeplay}
from turtle import *
up()

p = (100, -120)

print('p =', p)
print('x =', p[0])
print('y =', p[1])

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

ligne(p, (0, 100))
ligne((-300, 0), (300, 0))
```

## Créer un quiz

Nous continuons ici avec nos quiz. D'abord nous allons ajouter un score. Ensuite nous allons voir comment créer  des quiz mathématiques.

### Ajouter un score

Nous reprenons l'exemple du chapitre précédent et nous ajoutons le calcul du score

```{codeplay}
score = 0
quiz = (('France', 'Paris'),
        ('Allemagne', 'Berlin'),
        ('Suisse', 'Berne'))

for (question, solution) in quiz:
    print('Quelle est la capitale de', question)
    reponse = input('Votre réponse: ')
    if reponse == solution:
        print('correct')
        score = score + 1
    else:
        print('FAUX! La bonne réponse est', solution)
    print()

print('Votre score: ', score, 'sur', len(quiz))
```

### Valeurs aléatoires

Pour les exercices mathématiques il serait pratique d'avoir des valeurs aléatoire. 
Nous allons utiliser la fonction `randint(a, b)` du module `random` qui renvoie un entier aléatoire du l'intervalle [a, b].

```{codeplay}
from random import *

for i in range(10):
    print(randint(10, 99))
```

### Quiz mathématique

Nous utilisons deux valeurs aléatoires pour faire un quiz d'addition.

```{codeplay}
from random import *

print('Quiz addition')
for i in range(3):
    a = randint(10, 50)
    b = randint(10, 50)
    print(a, '+', b, '=')
    reponse = int(input())
    if reponse == a + b:
        print('correct')
    else:
        print('FAUX. La bonne réponse est', a + b)
    print()
```

## Erreurs

En utilisant les calculs, nous allons rencontrer encore d'autres types d'erreurs. Pour bien programmer vous devez savoir interpréter les messages d'erreur. Ces messages vous indiquent sur quelle ligne du programme il y a quel type d'erreur.

### SyntaxError

Cette erreur survient lorsque vous oubliez un signe de ponctuation (parenthèse, virgule, apostrophe).

```{codeplay}
print('hello'
print(12 34)
print('bonjour)
```

**Exercice** : Corrigez les trois erreurs de syntaxe.

### TypeError

Cette erreur survient lorsque vous mettez des opérandes dont le type n'est pas approprié pour l'opérateur.

```{codeplay}
print('10' > 0)
print('10' * '10')
print('10' + 10)
```

**Exercice** : Corrigez les trois erreurs de type.

### ZeroDivisionError

Cette erreur survient lorsque vous essayez de diviser par zéro.

```{codeplay}
print(10 / 0)
print(10 // 0)
print(10 % 0)
```

**Exercice** : Corrigez les trois erreurs de division par zéro.

### RangeError

Cette erreur survient lorsqu'une fonction récursive s'appelle elle-même un trop grand nombre de fois.

```{codeplay}
def f(x):
    if x == 1:
        return 1
    else: 
        return 1 + f(x-1)

print(f(100))
print(f(1000))
print(f(10000))
print(f(20000))
```

## Exercices

### Kahoot

La plate-forme d'apprentissage ludique [Kahoot!](https://fr.wikipedia.org/wiki/Kahoot!) est utilisée comme technologie éducative dans les écoles et autres établissements d'enseignement.

Ses jeux d’apprentissage, *Kahoots*, sont des questionnaires à choix multiples qui permettent à plusieurs utilisateurs de jouer simultanément. Le site est accessible via un navigateur Web mais aussi téléchargable sur smartphone.

Créez un quiz avec des question sur un sujet de culture générale, dans le style des quiz sur le site Kahoot.

```{codeplay}
:file: kahoot.py

print('Quiz Kahoot')
```
