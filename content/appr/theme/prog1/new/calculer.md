# Calculer - `int`

Dans ce chapitre nous allons voir comment un programme peut calculer avec des nombres.
Ceci est utilisé dans une calculatrice ou un programme de tableur.

Les nombres entiers forment une catégorie très importante. En anglais un entier est appelé **integer** (`int`). Nous allons voir que

- les opérateurs de base sont `+-*/`,
- les nombres sont du type `int` ou `float`,
- un texte est du type `str`.

## Un calcul simple

Dans ce chapitre nous allons explorer comment nous pouvons calculer avec des nombres. Voici un exemple qui affiche dans une première ligne sous forme de texte une expression mathématique, et dans une deuxième ligne une expression mathématique qui sera évaluée vers son résultat numérique.

```{codeplay}
print('2 à la puissance 32 =')
print(2 ** 32)
```

## Les opérations de base

En Python, nous retrouvons les 4 opérations arithmétiques de base :

- addition (`+`)
- soustraction (`-`)
- multiplication (`*`)
- division (`/`)

```{codeplay}
print('3 + 4 =', 3 + 4)
print('3 - 4 =', 3 - 4)
print('3 * 4 =', 3 * 4)
print('3 / 4 =', 3 / 4)
```

**Exercice** : Modifiez les 4 calculs et exécutez de nouveau.

```{question}
Quel est le résultat de l'expression `'12' + '12'` ?  
{f}`12`  
{f}`24`  
{v}`1212`  
{f}`1221`  
```

## Les opérations supplémentaires

En Python, nous avons également 3 opérateurs supplémentaires :

- puissance (`**`),
- division entière (`//`),
- reste de la division entière ou modulo (`%`).

```{codeplay}
print('7 ** 3 =', 7 ** 3)
print('7 // 3 =', 7 // 3)
print('7 % 3 =', 7 % 3)
```

**Exercice** : Modifiez les 3 calculs et exécutez de nouveau.

```{question}
Quel est le résultat de l'expression `1 + 2 * 3` ?

{f}`1`
{f}`2`
{f}`3`
{f}`6`
{v}`7`
{f}`9`
```

## Une variable

Une **variable** est une manière de designer une valeur par un nom. Le terme technique pour associer une valeur à une variable est **affectation** et elle utilise le symbole `=` (égal).

Mais faites attention ! Il ne s'agit pas d'une équation dans le sens mathématique. La variable doit toujours figurer seule à gauche.
La forme générique d'une affectation est `var = expression`.

```{codeplay}
r = 2
pi = 3.14

print('rayon =', r)
print('diamètre =', 2 * r)
print('circonférence =', pi * 2 * r)
```

**Exercice** : Ajoutez le calcul de la surface du cercle.

Pour nommer une variable vous pouvez utiliser :

- lettres (`a...z` et `A...Z`),
- chiffres (`0...9`),
- le tiret bas (`_`).

Le nom de variable :

- est sensible aux majuscules/minuscules,
- ne peut pas commencer avec un chiffre,
- ne doit pas consister d'un mot-clé (`if`, `else`, `for`),
- ne doit pas contenir un caractère spécial (`* + % & $ - / ?`).

Ces noms de variables sont donc valides : `a2`, `_a`, `speed`, `pos_x`, `POS_X`

Ceux-ci sont invalides :

- `2var` (commence avec un chiffre),
- `if` (correspond à un mot-clé),
- `var$2` (contient un caractère spécial),
- `mon nom` (contient une espace et est interprété comme deux noms de variables).

```{question}
Lesquels des noms de variable sont valides ?

{f}`var 2`  
{v}`var2`  
{f}`2var`  
{f}`if`  
{v}`IF_VAR`
```

Voici un autre calcul où `a` et `b` désignent largeur et hauteur d'un rectangle.

```{codeplay}
a = 3
b = 5

print('largeur =', a)
print('hauteur =', b)
print('surface =', a * b)
print('périmètre =')
print('diagonale =')
```

**Exercice** : Complétez le calcul du périmètre et de la diagonale.

```{question}
Quels noms de variable sont valides ?

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
print(type('hello'))
print(type(123))
print(type(3.14))
```

**Exercice** : Trouvez encore d'autres types.

L'exemple ci-dessus nous montre que

- `str` (string) désigne des chaînes de caractères,
- `int` (integer) désigne des nombres entiers,
- `float` (floating point) désigne des nombres à virgule flottante.

## Conversion de type

Les trois fonctions `str()`, `int()` et `float()` permettent de transformer d'un type à un autre.

Par exemple la chaîne `'123'` peut être transformée soit en entier, soit en nombre à virgule flottante.

```{codeplay}
a = '123'
b = int(123)
c = float(123)

print(b, c)
print(type(a))
print(type(b))
print(type(c))
```

Nous reconnaissons la différence entre un entier (`int`) et un nombre à virgule flottante (`float`) par la présence du point décimal (`123.0`).

## La fonction `input()`

La fonction `input()` permet d'obtenir une entrée de l'utilisateur. La valeur retournée est une chaine de caractères. Pour pouvoir l'utiliser dans un calcul nous devons la transformer en virgule flottante avec la fonction de conversion `float()`.

```{codeplay}
r = float(input('Entrez le rayon: '))
pi = 3.14

print('rayon =', r)
print('diamètre =', 2 * r)
print('circonférence =', pi * 2 * r)
print('surface =')
```

**Exercice** : Complétez le programme pour afficher la surface du cercle.

Nous pouvons également créer des programmes où nous demandons plusieurs valeurs à l'utilisateur. Cette fois nous permettons seulement l'utilisation de nombres entiers, et donc transformons la chaine obtenu avec `int()` en nombre entier.

```{codeplay}
a = int(input('Entrez la largeur: '))
b = int(input('Entrez la longeur: '))

print('surface =', a * b)
print('périmètre =')
print('diagonale =')
```

**Exercice** : Complétez le programme pour afficher le périmètre et la diagonale.

## Affectation multiple

Python permet d'affecter plusieurs variables sur une même ligne.
Ceci est parfois utilisé pour assigner des coordonnées.

```{codeplay}
x, y = 3, 4
print(x, y)
```

L'affectation multiple est une manière élégante d'échanger les valeurs de deux variables.

```{codeplay}
x, y = 3, 4
print(x, y)

x, y = y, x
print(x, y)
```

**Exercice** : Ajoutez une 3e variable et faites une permutation cyclique.

## Erreurs

Pour bien programmer vous devez savoir interpréter les messages d'erreurs. Ces messages vous indiquent sur quelle ligne du programme il y a quel type d'erreur.

### SyntaxError

Cette erreur se produit quand vous oubliez un signe de ponctuation (parenthèse, virgule, apostrophe).

```{codeplay}
print('hello'
print(12 34)
print('bonjour)
```

**Exercice** : Corrigez les 3 erreurs de syntaxe.

### TypeError

Cette erreur se produit quand vous mettez des opérandes dont le type n'est pas approprié pour l'opérateur.

```{codeplay}
print('10' > 0)
print('10' * '10')
print('10' + 10)
```

**Exercice** : Corrigez les 3 erreurs de type.

### ZeroDivisionError

Cette erreur se produit quand vous essayez de diviser par zéro.

```{codeplay}
print(10 / 0)
print(10 // 0)
print(10 % 0)
```

**Exercice** : Corrigez les 3 erreurs de division par zéro.

### RangeError

Cette erreur se produit quand une fonction récursive s'appelle elle-même un trop grand nombre de fois.

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
