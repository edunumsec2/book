# Récursif - `f(n)`

La définition d'une fonction `f(n)` qui contient à l'intérieur de sa définition le terme `f(n-1)` représente une **fonction récursive**, c'est à dire une fonction qui s'appelle soi-même. Elle s'appelle souvent soi-même avec une valeur plus simple.

## Boucle infinie

Il est très facile de créer une boucle qui ne se termine jamais. La façon standard pour une boucle infini est d'utiliser le terme `while True:` qui répète à l'infini le bloc qui suit, car la condition de terminaison est toujours vraie.

Souvent ceci est un bug, et représente le cas ou l'exécution reste bloqué dans une boucle et le programme ne réagit plus.

```{codeplay}
n = 100
while True:
    print(n)
    n = n-1
```

**Attention** : pour terminer ce programme, cliquez sur **Interrompre**.

Pour terminer une boucle infinie et en sortir, nous pouvons utiliser le mot-clé `break`. La boucle `while True:` est alors quittée et le programme continue avec l'instruction suivante à l'extérieur de la boucle.

```{codeplay}
n = 100
while True:
    print(n)
    if n == -100:
        break
    n = n-1
print('continuer')
```

Dans ce cas, on aurait pu écrire de façon plus simple encore:

```{codeplay}
n = 100
while n >= -100:
    print(n)
    n = n-1
print('continuer')
```

## Fonction récursive

Nous faisons maintentant la même chose, mais cette fois en utilisant une fonction récursive. Dans ce premier exemple nous avons pas de condition de terminaison, et donc la fonction est appelée en continue. La fonction `f(n)` imprime la valeur `n` et s'appelle ensuite elle même avec une valeur plus petite `f(n-1)` et ainsi de suite.

```{codeplay}
def f(n):
    print(n)
    f(n-1)

f(100)
```

Le comportement est différent. Nous constatons que la fonction s'arrête après quelques centaines d'appels récursifs. C'est une limite qui peut être défini dans le compilateur Python.

## Condition de terminaison

Cette fois dans notre fonction récursive, nous prévoyons une **condition de terminaison** qui va interrompre la récursivité.

```{codeplay}
def f(n):
    print(n)
    if n == 0:
        print('terminaison')
    else:
        f(n-1)

f(100)
```

## Factorielle

La fonction factorielle est une fonction que nous pouvons écrire très facilement sous forme récursive. La factorielle retourne le produit de tous les entiers de 1 à n.

```{codeplay}
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

for i in range(1, 14):
    print(fact(i))
```

## Carré

Mais aussi la fonction `carre(n)` peut être écrite sous forme récursive.

```{codeplay}
def carre(n):
    if n == 1:
        return 1
    else:
        return carre(n-1) + 2 * n - 1

for i in range(1, 14):
    print(carre(i))
```

**Exercice** : Définissez la fonction `cube(n)` sous forme récursive.

## Flocon de Koch

La courbe de Koch est un ligne coupé en 3 avec un triangle isocèle dessiné sur le segment du milieu. Il est possible d'appliquer cette règle de nouveau sur les 4 segments obtenus, et ainsi de suite.

```{codeplay}
from turtle import *

getscreen().bgcolor('deepskyblue')
color('white')
goto(-100, 70)
clear()

def koch(d, n):
    if n == 0:
        forward(d)
    else:
        koch(d/3, n-1)
        left(60)
        koch(d/3, n-1)
        right(120)
        koch(d/3, n-1)
        left(60)
        koch(d/3, n-1)
        
def flocon(d, n):
    for i in range(3):
        koch(d, n)
        right(120)
    
for i in range(5):
    flocon(200, i)
```

**Exercice** : Calculez la longueur de la courbe.

## Pyramide fractale

La règle de construction de cette courbe est similaire à la courbe de Koch. Le segment de départ est coupé en 3 est un carré est dessiné sur le segment du milieu.

```{codeplay}
from turtle import *

getscreen().bgcolor('navy')
color('white')
speed(0)
up()

def koch(d, n):
    if n == 0:
        forward(d)
    else:
        koch(d/3, n-1)
        left(90)
        koch(d/3, n-1)
        right(90)
        koch(d/3, n-1)
        right(90)
        koch(d/3, n-1)
        left(90)
        koch(d/3, n-1)
    
for i in range(6):
    goto(-200, -100)
    down()
    koch(400, i)
```

**Exercice** : Calculez la longueur de la courbe.

## Triangle de Sierpinski

```{codeplay}
from turtle import *

getscreen().bgcolor('crimson')
color('yellow')
speed(0)
goto(-200, -170)
clear()

def sierpinski(d, n):
    for i in range(3):
        if n > 1:
            sierpinski(d//2, n-1)
        forward(d)    
        left(120)
        
sierpinski(400, 5)
```

**Exercice** : Augmentez le degré de la courbe.
