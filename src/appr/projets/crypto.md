# Cryptographie

## Calculer une somme

Calculez cette somme

$$ \sum_{k=3}^7\frac{1}{ln(3k + 1)} $$

```{codeplay}
from math import *

sum = 0
for k in range(3, 7):
    sum += 1/(log(3*k + 1))
print(sum)
```

Calculez cette somme

$$ \sum_{i=5}^{12}\frac{i}{\sqrt{2i-1}} $$

```{codeplay}
from math import *

sum = 0
for i in range(5, 13):
    sum += i/sqrt(2*i - 1))
print(sum)
```

## Combinaison

Calculez le nombre de combinaison :

```{codeplay}
from math import *

def combinaison(n, p):
    return factorial(n) // (factorial(p) * factorial(n-p))

print(combinaison(9, 3))
```

## Suite de Syracuse

```{codeplay}
def syracuse(n):
    if n % 2: 
        return 3 * n + 1
    else:
        return n // 2

n = 6
while n != 1:
    n = syracuse(n)
    print(n, end=', ')
```

## Nombre premier

Un entier naturel est dit **premier** s'il est supérieur ou égal à 2 et n'est divisible que par 1 et lui-même.

Pourquoi les nombres premiers sont-ils tellement importants ?

Il existe deux  manières d'engendrer $\mathbb{N}$ :

- en utilisant l'**addition** il suffit le nombre 1 et l'addition de 1,

- en utilisant la **multiplication** on a besoin de tous les nombres premiers.

Les nombres premiers sont donc ces éléments qui nous permettent de fabriquer tous les autres.

## Nombre premier ?

Le nombre 1321 est-il premier ?

```{codeplay}
for i in range(1, 1231):
    if 1231 % i == 0:
        print(i)
        break
```

```{codeplay}
def est_premier(p):
    if p in (0, 1):
        return False
    elif p == 2:
        return True
    else:
        for i in range(2, p):
            if p % i == 0:
                return False
        return True

for i in range(100):
    if est_premier(i):
        print(i, end=', ')
```

```{codeplay}
from math import *

def est_premier(p):
    if p in (0, 1):
        return False
    elif p == 2:
        return True
    else:
        for i in range(2, int(sqrt(p)) + 1):
            if p % i == 0:
                return False
        return True

for i in range(1000):
    if est_premier(i):
        print(i, end=', ')
```

## La crible d'Eratoshène

```{codeplay}
from math import *

def est_premier(p):
    if p in (0, 1):
        return False
    elif p == 2:
        return True
    else:
        for i in range(2, int(sqrt(p)) + 1):
            if p % i == 0:
                return False
        return True

def crible(n):
    L = []
    for i in range(n+1):
        if est_premier(i):
            L.append(i)
    return L

print(crible(1000))
```

## Le nombre de Fermat

```{codeplay}
from math import *

def est_premier(p):
    if p in (0, 1):
        return False
    elif p == 2:
        return True
    else:
        for i in range(2, int(sqrt(p)) + 1):
            if p % i == 0:
                return False
        return True

def fermat(n):
        return 2 ** 2 ** n + 1

for i in range(1, 100):
    if est_premier(fermat(i)):
        print(i)
```

## Chiffrement de César

```{codeplay}
from math import *

print(factorial(26))
```

## Message secret

```{codeplay}
msg = 'ce message est secret'

for c in msg:
    print(c, chr(ord(c)+3))
```

## Message encodé

```{codeplay}
msg = 'ce message est secret'

for c in msg:
    print(c, chr(ord(c)+3))
```

## Code ASCII de A-Z

Dans les deux exemples notez bien la distinction entre `i` et `c`. La variable d'itération 

- `i` est un entier,
- `c` est un caractère.

```{codeplay}
:max_output_lines: 26
for i in range(ord('A'), ord('Z')+1):
    print(i, '=', chr(i), end='\t')
```

Une autre façon est celle-ci.

```{codeplay}
:max_output_lines: 26
for c in 'ABCDEFGHIJKLMNOPQRSTUVWYYZ':
    print(c, '=', ord(c), end='\t')
```