# Structures de contrôle

Jusqu'à maintenant un programme était une **séquence linéaire**.
Les instructions s'exécutaient

- les unes après les autres,
- de haut en bas,
- chacune une seule fois.

Dans cette section nous allons voir des structures de contrôle qui permet de changer cette séquence purement linéaire:

- L'**instruction conditionnelle**  permet de ne pas exécuter certaines instructions.
- La **boucle** permet d'exécuter certaines instructions plusieurs fois.

## Indentation

On appelle **bloc** une ou plusieurs instructions qui forment un ensemble.
En C ou JavaScript un bloc est délimité avec des accolades `{...}`.
L'indentation est encouragé mais reste optionnelle.

En Python l'indentation est obligatoire. C'est la façon officiel de designer un bloc.
Ceci a deux avantages:

- pas besoin d'accolades pour délimiter une bloc
- la structure des blocs est clair et visuel

Une **indentation** est un retrait du code par rapport à la marge gauche de 4 caractères.
Elle peut être insérée avec la touche tabulateur **TAB** (symbolisée par une flèche à gauche du clavier).

Une suite d'instructions indentée de la même manière forme un bloc.
Ces blocs se trouvent dans

- la définition de fonction (`def`),
- l'instruction conditionnelle (`if-else`)
- la boucles (`for`, `while`)

En Python le symbole `:` en fin de ligne introduit un sous-bloc qui doit être indenté.
Voici des sous-blocs à la suite des mot-clés `def`, `if`, `else`, `for`.

```python
def f(x):
    return x * x

if x > 0:
    print('positif')
else:
    print('négatif)

for i in range(3):
    print('itération', i) 
```

Dans l'exemple suivant nous avons deux fois une boucle qui fait 3 itérations.

Dans la première boucle l'instruction `print('dedans')` fait parti du bloc d'itération et elle est exécutée 3 fois.

Dans la deuxième boucle l'instruction `print('dehors')` ne fait pas parti du bloc d'itération et elle est exécutée seulement 1 fois.

```{codeplay}
for i in range(3):
    print('itération', i)
    print('dedans')

print()
for i in range(3):
    print('itération', i)
print('dehors')
```

## Opérations de comparaison

Les 6 opérateurs de comparaison permettent de comparer 2 valeurs.

- plus grand que (`>`)
- plus petit que (`<`)
- plus petit ou égal à (`<=`)
- plus grand ou égal à (`>=`)
- égal à (`==`)
- non égal à (`!=`)

Dans l'exemple suivant nous affectons une valeur à la variable `a` et nous effectuons 3 comparaisons.
Le résultat d'une comparaison est une valeur booléenne (valeur logique) qui prend la valeur `True` ou `False`

```{codeplay}
a = 3
print(a > 2)
print(a < 2)
print(a != 2)
```

**Note**:
Ne confondez pas l'opérateur d'_affectation_ (`=`) avec l'opérateur de _comparaison_ (`==`).

```{codeplay}
a = 2           # affectation
print(a)
print(a == 2)   # comparaison
```

## L'instruction if

L'instruction `if` permet d'exécuter un bloc si une condition est vraie, sinon le programme suit son cours sans exécuter ce bloc.

L'exemple suivant affiche `majeur` si l'âge est plus grand ou égale à 18.

```{codeplay}
age = 21

if age >= 18:
    print('majeur')
```

## L'instruction if...else

L'instruction `if...else` permet de choisir entre deux blocs selon une condition.
Si la condition est vraie, le bloc **if** est exécuté; sinon, le bloc **else** est exécuté.

```{codeplay}
note = 4.5

if note >= 4:
    print('réussi')
else:
    print('echec')
```

## L'instruction if...elif...else

L'instruction `if...elif...else` permet d'exécuter un bloc d'instruction si une condition est vraie. Si la première condition n'est pas remplie, une autre est testée.

```{codeplay}
n = -3
print('le nombre', n, 'est')

if n > 0:
    print('positif')
elif n < 0:
    print('négatif')
else:
    print('zéro')
```

## Opérations logiques

Les opérateurs logiques permettent de combiner deux valeurs logiques.

- et logique (`and`)
- ou logique (`or`)

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

L'opérateur `not` inverse de la valeur logique.

- `True` devient `False`
- `False` devient `True`

Une double inversion revient à l'identité.

Dans l'exemple suivant, essayez de changer la valeur de `p`.

```{codeplay}
p = True

print('p =', p)
print('not p =', not p)
print('not not p =', not not p)
```

## La boucle for

Le boucle `for` permet d'itérer sur un ensemble de valeurs.
Par exemple une chaine de texte est un ensemble de caractères.

Le mot **itérer** veut dire de parcourir l'ensemble et assumer une valeur particulière à chaque tour,
en passant dans l'ordre, de la première valeur à la dernière.

Dans l'exemple suivant nous itérons à travers la chaine `'hello'`

```{codeplay}
for c in 'hello':
    print(c)
````

Nous pouvons aussi itérer sur une plage numérique.
L'expression `range(a, b)` exprime la plage numérique allant de `a` à `b-1`.
Dans notre cas nous itérons de 3 à 9.

```{codeplay}

for i in range(3, 10):
    print(i)
```

Nous pouvons faire des calculs avec chaque valeur de la boucle.

```{codeplay}
for i in range(1, 10):
    print(i, 'au carré est', i ** 2)
```

## La boucle while

La boucle `while` exécute un bloc tant qu'une condition est vraie.

Nous pouvons l'utiliser pour créer un compteur à rebours.
Pour faire l'attente d'une seconde nous importons la fonction `sleep()` du module `time`.

```{codeplay}
from time import sleep

n = input('Entrez la valeur de départ: ')
while n > 0:
    print(n)
    sleep(1)
    n = n - 1

print('boum!!!')
```

Nous pouvons aussi utiliser pour deviner un nombre.
Ici nous importons la fonction `randint()` du module `random`.
Elle fournit un nombre entier aléatoire entre deux bornes (1, 99).

La fonction `input()` ne retourne que le type `string`.
La fonction `int()` transforme le type string (chaine) en entier (integer).

```{codeplay}
from random import randint

n = randint(1, 99)
x = input('Devinez un nombre entre 1 et 99: ')
x = int(x)

while x !=  n:
    if x > n:
        print(x, 'est trop grand')
    else:
        print(x, 'est trop petit')
        
    x = input('Essayez encore:')
    x = int(x)

print()
print('Bravo. Vous avez réussi')
```

## Exercices

### Exercice 1 - intervalle

Vérifiez si une variable `x` contient une valeur qui est entre deux bornes [a, b].

### Exercice 2 - question

Faites un programme qui pose une question simple à l'utilisateur. Si sa réponse est juste, affichez `Bravo`.

### Exercice 3 - age

Faites un programme qui demande à l'utilisateur son âge.
Si l'âge est supérieur ou égal à 18, le programme doit afficher: "Vous êtes majeur, vous pouvez voter" et si l'âge est inférieur à 18, le programme doit afficher: "Vous êtes mineur, vous pourrez voter dans (*calcul de la différence*) année(s)"

### Exercice 4 - jeu

Faites un programme qui demande à l'utilisateur d'entrer un chiffre entre 0 et 2.
Si l'utilisateur choisit

- 0: affichez **Caillou**
- 1: affichez **Feuille**
- 2: affichez **Ciseaux**.

### Exercice 5 - carré

Faites un programme qui affiche un carré de longueur `n` avec le caractère `'x'`.
Mais vide à l'intérieur

```{codeplay}
n = int(input('Entrez n: '))

for i in range(n):
    print('x' * n) 
```

### Exercice 6 - triangle

Faites un programme qui affiche un triangle de hauteur `n` avec des `x`.

### Exercice 7 - rectangle

Faites un programme qui affiche une boite de hauteur `a` et longueur `b` avec des `x`.
L'intérieur de la boite doit rester vide.
