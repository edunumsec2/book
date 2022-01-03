# Calculer - `int`

Nous avons déjà vu qu'un programme informatique peut manipuler ces différents catégories d’objet :

- image
- texte
- nombre

Dans ce chapitre nous allons explorer comment nous pouvons calculer avec des nombres. Voici un exemple qui affiche texte et nombre :

```{codeplay}
print('2 à la puissance 32 =')
print(2 ** 32)
```

## Les opérations de base

Nous retrouvons les 4 opérations arithmétiques de base :

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


## Les opérations supplémentaires

Dans Python nous avons 3 opérateurs supplémentaires :

- puissance (`**`)
- division entière (`//`)
- reste de la division entière ou modulo (`%`)

```{codeplay}
print('7 ** 3 =', 7 ** 3)
print('7 // 3 =', 7 // 3)
print('7 % 3 =', 7 % 3)
```

**Exercice** : Modifiez les 3 calculs et exécutez de nouveau.

## Une variable

Une **variable** est une manière de designer une valeur par un nom. Le terme technique est **affectation** et elle utilise le symbole `=` (égal).

Mais faites attention ! Il ne s'agit pas d'une équation dans le sens mathématique. La variable dois toujours figurer seul à gauche. 
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

- lettres (`a...z` et `A...Z`)
- chiffres (`0...9`)
- le tiret bas (`_`)

Le nom de variable : 
- est sensible aux majuscules/minuscules
- ne peut pas commencer avec un chiffre
- ne dois pas consister d'un mot-clé (`if`, `else`, `for`)

Voici un autre calcul où `a`  et `b` designent largeur et hauteur d'un rectangle. 

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

## Les types

Un ordinateur peut manipuler différents catégories d'objet tel que image, texte, nombre. On parle alors du type de ces données.

La fonction `type()` retourne le type d'un objet.

```{codeplay}
print(type('hello'))
print(type(123))
print(type(3.14))
```

- `str` (string) designe des chaînes de caractères
- `int` (integer) désigne des nombres entiers
- `float` (floating point) désigne des nombres à virgule flottante

**Exercice** : Trouvez encore d'autres types.



## Conversion de type

Les trois fonctions `str()`, `int()` et `float()` permettent de transformer d'un type à un autre. 

Par exemple la chaîne `'123'` peut être transformé soit en entier, soit en nombre à virgule flottante.

```{codeplay}
a = '123'
b = int(123)
c = float(123)

print(b, c)
print(type(a))
print(type(b))
print(type(c))
```

Nous reconnaissons la différence entre en entier (`int`) et un nombre à virgule flottante (`float`) par la présence du point décimal (`123.0`).

## La fonction `input()`

La fonction `input()` permet d'obtenir une entrée de l'utilisateur. La valeur retourné est une chaine de caractères. Pour pouvoir l'utiliser dans un calcul nous devons la transformer en virgule flottante avec la fonction de conversion `float()`.

```{codeplay}
r = float(input('Entrez le rayon: '))
pi = 3.14

print('rayon =', r)
print('diamètre =', 2 * r)
print('circonférence =', pi * 2 * r)
print('surface =')
```

**Exercice** : Complétez le programme pour afficher la surface du cercle.

Nous pouvons également créer des programmes ou nous demandons plusieurs valeurs à l'utilisateur. Cette fois nous permettons que l'utilisation d'entiers, et donc transformons la chaine obtenu avec `int()` en nombre entier.

```{codeplay}
a = int(input('Entrez la largeur: '))
b = int(input('Entrez la longeur: '))

print('surface =', a * b)
print('périmètre =')
print('diagonale =')
```

**Exercice** : Complétez le programme pour afficher perimètre et la diagonale.

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

**Exercice** : Ajoutez une 3e variable et faites un permutation cyclique.

## Compter en binaire

Si nous utilisons le code binaire pour compter avec nos doigts, alors nous pouvons représenter les codes binaires `00000` à `11111`.

Voici un programme qui affiche le code binaire et dessine les doigts.

```{codeplay}
from turtle import *

def finger(x):
    forward(x)
    circle(-20, 180)
    forward(x)
    left(180)

def binaire(code):
    left(90)
    for c in code :
        write(c, font=('Arial', 24))
        if c == '1':
            finger(120)
        else :
            finger(30)
              
binaire('00110')
```

**Exercice** : modifier le programme pour compter de 0 à 31.