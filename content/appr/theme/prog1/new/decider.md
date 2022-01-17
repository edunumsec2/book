# Décider - `if`

Dans ce chapitre nous allons voir comment un programme peut faire des choix, et comment il peut exécuter du code de façon sélective. Nous allons voir que : 

- le mot-clé `if` permet une exécution conditionnelle,
- les mot-clés `if-else` permettent de choisir entre deux alternatives,
- le mot-clé `elif` (else if) permet d'ajouter différentes conditions.

## Êtes-vous majeur ?

Basé sur votre âge, le programme décide si vous êtes majeur ou pas.

```{codeplay}
age = input('Entrez votre age: ')

if int(age) < 18:
    print('accès interdit - vous êtes mineur')
else:
    print('accès OK - vous êtes majeur')
```

## Comparer

Un programme doit parfois comparer deux valeurs.
Python connait six types de comparaisons :

- plus petit (`<`),
- plus petit ou égal (`<=`),
- égal (`==`),
- différent (`!=`),
- plus grand  (`>`),
- plus grand ou égal (`>=`).

Le résultat d'une comparaison est une valeur booléenne, soit `True` soit `False`.

Voici quelques exemples :

```{codeplay}
x = 3
print(x > 2)
print(x < 2)
print(x != 2)
```

**Attention** : Il ne faut pas confondre l'opérateur d'affectation (`=`) avec l'opérateur de comparaison (`==`).

```{codeplay}
a = 2           # affectation
print(a)
print(a == 2)   # comparaison
```

## Le signe d'un nombre

Trouvez le signe d'un nombre.

```{codeplay}
n = input('Entrez un nombre: ')
n = int(n)

if n > 0:
    print('positif')
elif n < 0:
    print('négatif')
else:
    print('zéro')
```

**Exercice** : Testez le programme avec -2, 0, 3.

## Pair ou impair ?

Le programme vous dit si le nombre que vous entrez est pair ou impair.

```{codeplay}
x = input('Entrez un entier: ')

if int(x) % 2 == 0:
    print('pair')
else:
    print('impair')
```

## Factoriser

Le programme va factoriser le nombre que vous entrez

```{codeplay}
n = int(input('Entrez un entier: '))
i = 2

while i < n:
    if n % i == 0:
        print(i)
        n = n // i 
    else:
        i = i + 1

print(n)
```

## En code binaire

Le programme transforme l'entier en code binaire.

```{codeplay}
n = int(input('Entrez un entier: '))

code = ''
while n > 0:
    if n % 2 == 1:
        code = '1' + code
    else:
        code = '0' + code
    n = n // 2

print(code)
```

## Décrire un chemin

Un programme de dessin avec la tortue est une séquence d'instructions. Si la tortue ne se déplace que sur les lignes d'une grille, nous pouvons représenter un chemin par une séquence d'actions où chaque action peut être représentée avec une seule lettre :

- `f` = avancer
- `l` = tourner à gauche
- `r` = tourner à droite
- `b` = reculer

On voit que le contour de la lettre E contient 24 segments de  base.

```{codeplay}
from turtle import *

d = 20
def walk(path):
    for c in path:
        if c == 'f':
            forward(d)
        elif c == 'l':
            left(90)
            forward(d)
        elif c == 'r':
            right(90)
            forward(d)
        elif c == 'b':
            back(d)

E = 'lffffrffrrfllfrrfllfrrff'
print(len(E)) 
walk(E)
```

**Exercice** : Dessinez la lettre F.

## Opérations logiques

Les opérateurs logiques permettent de combiner des valeurs logiques. En Python nous avons : 

- *et* logique (`and`),
- *ou* logique (`or`),
- négation (`not`).

Pour tester si un nombre x est dans l'intervalle (a, b) il faut combiner deux comparaisons avec une opération logique.

```{codeplay}
a = 5
b = 10

x = 8

if (a < x) and (x < b):
    print(x, 'est entre', a, 'et', b)

if (x < a) or (b < x):
    print(x, "est dehors l'interval (", a, '...', b, ')')
```

L'opérateur `not` inverse la valeur logique :

- `True` devient `False`,
- `False` devient `True`.

Une double inversion revient à l'identité.

Dans l'exemple suivant, essayez de changer la valeur de `p`.

```{codeplay}
p = True

print('p =', p)
print('not p =', not p)
print('not not p =', not not p)
```

## Dans une intervalle ?

Python permet de remplacer `(a < x) and (x < b)` par l'expression plus compacte `a < x < b`.

```{codeplay}
a = 5
b = 10

x = 8

if a < x < b:
    print(x, 'est entre', a, 'et', b)

if not (a < x < b):
    print(x, "est dehors l'interval (", a, '...', b, ')')
```
