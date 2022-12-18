(prog1.decider)=

# Décider - `if`

Dans ce chapitre, nous allons voir comment un programme peut faire des choix, et comment il peut exécuter du code de façon sélective. Nous allons voir que :

- le mot-clé `if` permet une exécution conditionnelle,
- les mots-clés `if-else` permettent de choisir entre deux alternatives,
- le mot-clé `elif` (else if) permet d'ajouter différentes conditions.

```{question}
En Python, `if` est suivi

{f}`d'un bloc`  
{v}`d'une condition`  
{f}`de parenthèses`  
{f}`d'un deux-points`
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

Dans des formules mathématiques nous utilisons les symboles ≤,  ≥ et ≠. En Python vous devez utiliser deux symboles: `<=`, `>=` et `!=` à la place.

```{exercise}
Ajoutez des exemples avec les autres 5 comparateurs.
````

```{codeplay}
x = 3
print('x =', x)
print('(x > 2) =', x > 2)
```

```{question}
L'expression `x == 2`

{f}`met la valeur 2 dans la variable x`  
{v}`compare deux valeurs`  
{f}`affecte la variable x avec une valeur`  
{v}`retourne True ou False`
```

```{caution}
Il ne faut pas confondre l'opérateur d'affectation (`x = 2`) avec l'opérateur de comparaison (`x == 2`).
```

Le résultat d'une comparaison est une valeur booléenne, soit `True` soit `False`.

```{exercise}
Que se passe-t-il si vous échangez les deux éléments dans `x == 2` ?  
Et si vous échangez les deux éléments dans `x = 2`  ?
```

```{codeplay}
x = 2       # affectation
x == 2      # comparaison
print(x)
print(x == 2)
```

## Visuliser la comparaison

Dans l'exemple suivante, nous visualisons le résultat des 6 comparateurs en affichant grafiquement le résultat des 6 comparaisons du type `i < n`. 

- La variable `i` va de -9 à 9
- La variable `n` est marqué en rouge
- Le resultat `True ` est exprimé avec un grand point, `False` avec un petit

Que fait l'expression `'red' if i == n else 'black'` ?

Elle renvoie `'red'` si `i == n` et `'black'` autrement.

```{exercise}
Modifiez la variable `n` et réexecutez le code.
```

```{codeplay}
from turtle import *
d = 20      # dimension de base
n = 2       # valeur de comparison
up()

for j in range(7):
    for i in range(-10, 10):
        goto(i*d, 100-j*d)
        color('red' if i == n else 'black')
        if i == -10:
            c = ('i', '< n', '<= n', '== n', '!= n', '>= n', '> n')[j]
            write(c, font=(None, d//2), align='right')
        elif j == 0:
            write(i, font=(None, d//2), align='center')
        else:
            result = (0, i<n, i<=n, i==n, i!=n, i>=n, i>n)[j]
            dot(d if result else d/4)
```

## Une position aléatoire

Dans ce chapitre nous allons prendre des décisions basé sur la position `(x, y)` d'un point.
Nous avons donc besoin d'un certain nombre de points, pour ensuite prendre des décisions.

```{exercise}
Les variables `w, h` (width, height) représentent largeur et hauteur de la plage rectangulaire des valeurs aléatoires. 
Modifiez-les vers `500, 300` et réexécutez le code.
```

```{codeplay}
from turtle import *
from random import *

w, h = 600, 400
d, n = 10, 100
up()
speed(0)

for i in range(n):
    x, y = randint(-w/2, w/2), randint(-h/2, h/2)
    goto(x, y)
    dot(d)
```

## Pour x positive

La structure `if` ci-dessous permet d'exécuter une action seulement si `condition` est `True`.

``` python
if condition:
    action
```

Dans notre exemple nous affichons un point rouge seulement si x est positif (`x > 0`)

```{exercise}
Ajoutez une deuxième condition `if` pour colorier un point en `lime` si `x < -100.
```

```{codeplay}
from turtle import *
from random import *

w, h = 600, 400
d, n = 10, 100
up()
speed(0)

for i in range(n):
    x, y = randint(-w/2, w/2), randint(-h/2, h/2)
    goto(x, y)
    if x > 100:
        dot(2*d, 'red')
    dot(d)
```

## La structure `if else`

La structure `if else` ci-dessous permet d'exécuter une **action_1** seulement si une **condition** est vraie et une **action_2** autrment

``` python
if condition:
    action_1
else:
    action_2
```

Dans l'exemple ci-dessous la condition de test est `y > 0`. 
Si cette condition est vraie, le point est colorié en rouge, autrement en bleu.

```{codeplay}
from turtle import *
from random import *

w, h = 600, 400
d, n = 20, 300
up()
speed(0)

for i in range(n):
    x, y = randint(-w/2, w/2), randint(-h/2, h/2)
    goto(x, y)
    if y > 0:
        dot(d, 'red')
    else:
        dot(d, 'blue')
```

## Région en diagonale

```{codeplay}
from turtle import *
from random import *

w, h = 600, 400
d, n = 10, 1000
tracer(0)
up()

for i in range(n):
    x, y = randint(-w/2, w/2), randint(-h/2, h/2)
    goto(x, y)
    if x > y:
        dot(d, 'red')
    else:
        dot(d, 'blue')
update()
```

## Région en cercle

```{codeplay}
from turtle import *
from random import *

w, h = 600, 400
d, n = 10, 2000
tracer(0)
up()

for i in range(n):
    x, y = randint(-w/2, w/2), randint(-h/2, h/2)
    goto(x, y)
    if (x**2 + y**2) > 150**2 :
        dot(d, 'red')
    else:
        dot(d, 'blue')
update()
```

## L'opération `and`

```{codeplay}
from turtle import *
from random import *

w, h = 600, 400
d, n = 10, 2000
tracer(0)
up()

for i in range(n):
    x, y = randint(-w/2, w/2), randint(-h/2, h/2)
    goto(x, y)
    if x > 0 and y > 0:
        dot(d, 'red')
    else:
        dot(d, 'blue')
update()
```

## Êtes-vous majeur ?

Basé sur votre âge, le programme exécute soit le premier bloc (`if`) soit le  deuxième bloc (`else`).  Il affiche si vous êtes majeur ou pas.

```{codeplay}
:file: if1.py
age = input('Entrez votre âge: ')

if int(age) < 18:
    print('accès interdit - vous êtes mineur')
else:
    print('accès OK - vous êtes majeur')
```

## Le signe d'un nombre

Le mot-clé `elif` est une contraction de **else if** et permet de continuer à tester d'autres conditions.
Trouvez le signe d'un nombre.

```{codeplay}
:file: if4.py
n = input('Entrez un nombre: ')
n = int(n)

if n > 0:
    print('positif')
elif n < 0:
    print('négatif')
else:
    print('zéro')
```

Sans le mot-clé `elif` nous devrions mettre le bloc `if` à l'intérieur du bloc  `else` en indentation.
Avec multiples conditions, les blocs se décalent de plus en plus et rendent le programme illisible.

```{exercise}
Testez le programme avec -2, 0, 3.
```

```{codeplay}
:file: if4.py
n = input('Entrez un nombre: ')
n = int(n)

if n > 0:
    print('positif')
else:
    if n < 0:
        print('négatif')
    else:
        print('zéro')
```

## Pair ou impair ?

La fonction modulo `(x % 2)` permet de décider si un nombre est pair ou impair. Le programme suivant affiche si le nombre que vous entrez est pair ou impair.

```{codeplay}
:file: if5.py
x = int(input('Entrez un entier: '))

if (x % 2) == 0:
    print('pair')
else:
    print('impair')
```

## Opérations logiques

Les opérateurs logiques permettent de combiner des valeurs logiques. En Python, nous avons :

- *et* logique (`and`),
- *ou* logique (`or`),
- négation (`not`).

Pour tester si un nombre x est dans l'intervalle (a, b) il faut combiner deux comparaisons avec une opération logique.

```{codeplay}
:file: if9.py
a = 5
b = 10

x = 8

if (a < x) and (x < b):
    print(x, 'est entre', a, 'et', b)

if (x < a) or (b < x):
    print(x, "est dehors l'interval (", a, '...', b, ')')
```

L'opérateur `not` inverse la valeur logique :

- `True` devient `False`,
- `False` devient `True`.

Une double inversion revient à l'identité.

Dans l'exemple suivant, essayez de changer la valeur de `p`.

```{codeplay}
:file: if10.py
p = True

print('p =', p)
print('not p =', not p)
print('not not p =', not not p)
```

## Dans un intervalle ?

Python permet de remplacer `(a < x) and (x < b)` par l'expression plus compacte `a < x < b`.

```{codeplay}
:file: if11.py
a = 5
b = 10

x = 8

if a < x < b:
    print(x, 'est entre', a, 'et', b)

if not (a < x < b):
    print(x, "est dehors l'interval (", a, '...', b, ')')
```
