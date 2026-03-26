# Manipuler - `&`

La [manipulation de bits](https://fr.wikipedia.org/wiki/Manipulation_de_bits) consiste à agir sur des données au niveau d'un bit à l'aide d'opérations booléennes. Cette technique est utilisée pour des opérations de bas niveau comme le contrôle des périphériques, la détection et la correction d'erreur, le chiffrement, ainsi que pour l'optimisation.

Dans ce chapitre nous allons explorer des opérateurs qui manipulent un nombre au niveau de ses bits (bitwise operation). Nous allons voir que :

- l'opérateur `&` effectue une opération **and** par bit,
- l'opérateur `|` effectue une opération **or** par bit,
- l'opérateur `^` effectue une opération **xor** par bit.

```{question}
L'expression `2 & 3` donne comme résultat

{f}`0`  
{f}`1`  
{v}`2`  
{f}`3`
```

## Bitwise and (`&`)

```{codeplay}
:file: bit1.py
a = 0b11110000
b = 0b10110111

print('a   =', bin(a))
print('b   =', bin(b))
print('a&b =', bin(a & b))
```

## Bitwise or (`|`)

```{codeplay}
:file: bit2.py
a = 0b11110000
b = 0b10110111

print('a   =', bin(a))
print('b   =', bin(b))
print('a|b =', bin(a | b))
```

## Bitwise xor (`^`)

```{codeplay}
:file: bit3.py
a = 0b11110000
b = 0b10110111

print(f'a   = {a:08b}')
print(f'b   = {b:08b}')
print(f'a^b = {a ^ b:08b}')
```

## Bitwise inversion (`~`)

```{codeplay}
:file: bit4.py
a = 0b11110010

print(f'a  = {a:08b}')
print(f'~a = {~a & 0xff:08b}')
```

## Pixels noir et blanc

Par la suite nous affichons les pixels comme une image noir est blanc:

- 0 = pixel blanc
- 1 = pixel noir

```{codeplay}
:file: bit5.py
from turtle import *

up()
a = 0b11011001
d = 50
backward(200)
write(f'{a:08b} = {a:02x}', font=('Courier', 24))

goto(-200, -50)
for i in range(8):
    dot(d)
    if a & 2 ** (7-i) == 0:
        color('white')
        dot(d-2)
        color('black')
    forward(d)  
```

## Code binaire et hex

```{codeplay}
:file: bit6.py
from turtle import *

up()
d = 20
goto(-100, 150)

def ligne(n):
    for i in range(4):
        dot(d)
        if n & 2 ** (3-i) == 0:
            color('white')
            dot(d-2)
            color('black')
        forward(d)  
    write(f'{n:04b} = {n:1x}', font=('Courier', 12))
    goto(-100, ycor()-d)
     
for i in range(16):
    ligne(i)
````

## Bitwise and

L'opérateur `&` effectue l'opération logique `and` pour chaque bit d'un nombre.
Dans une image noir et blanc, ceci correspond à l'intersection des pixels des deux images.

```{codeplay}
:file: bit7.py
from turtle import *

up()
d = 20
goto(-100, 180)

def ligne(n):
    for i in range(4):
        dot(d)
        if n & 2 ** (3-i) == 0:
            color('white')
            dot(d-2)
            color('black')
        forward(d)
    write(f'{n:04b} = {n:1x}', font=('Courier', 12))
    goto(-100, ycor()-d)
     
ligne(7)
ligne(4)
ligne(4)
ligne(7)
sety(ycor()-d)

ligne(1)
ligne(1)
ligne(1)
ligne(1)
sety(ycor() - d)

ligne(7 & 1)
ligne(4 & 1)
ligne(4 & 1)
ligne(7 & 1)
```

## Bitwise ou

L'opérateur `|` effectue l'opération logique `or` pour chaque bit d'un nombre.
Dans une image noir et blanc, ceci correspond à l'union des pixels des deux images.

```{codeplay}
:file: bit8.py
from turtle import *

up()
d = 20
goto(-100, 180)

def ligne(n):
    for i in range(4):
        dot(d)
        if n & 2 ** (3-i) == 0:
            color('white')
            dot(d-2)
            color('black')
        forward(d)
    write(f'{n:04b} = {n:1x}', font=('Courier', 12))
    goto(-100, ycor()-d)
     
ligne(7)
ligne(4)
ligne(4)
ligne(7)
sety(ycor()-d)

ligne(1)
ligne(1)
ligne(1)
ligne(1)
sety(ycor() - d)

ligne(7 | 1)
ligne(4 | 1)
ligne(4 | 1)
ligne(7 | 1)
```

## Bitwise exclusive-or

L'opérateur `^` effectue l'opération **ou exclusif** pour chaque bit du nombre.
Dans une image noir et blanc, ceci correspond à inverser les pixels de la première image qui sont indiqué par la deuxième image.

```{codeplay}
:file: bit9.py
from turtle import *

up()
d = 20
goto(-100, 150)

def ligne(n):
    for i in range(4):
        dot(d)
        if n & 2 ** (3-i) == 0:
            color('white')
            dot(d-2)
            color('black')
        forward(d)
    write(f'{n:04b} = {n:1x}', font=('Courier', 12))
    goto(-100, ycor() - d)
===   
ligne(7)
ligne(4)
ligne(4)
ligne(7)
sety(ycor() - d)

ligne(1)
ligne(1)
ligne(1)
ligne(1)
sety(ycor() - d)

ligne(7 ^ 1)
ligne(4 ^ 1)
ligne(4 ^ 1)
ligne(7 ^ 1)
```
## Quiz

### AND logique

Rappel

```python
0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
```

```{codeplay}
from random import randint
score = 0
n = 3

for i in range(n):
    a = randint(1, 15)
    b = randint(1, 15)

    print(f'  {a:04b}')
    print(f'& {b:04b}')
    reponse = input('= ')
    solution = f'{a & b:04b}'

    if reponse == solution:
        score += 1
    else:
        print(f'faux! Réponse correcte = {solution}')
    print()
print(f'score = {score}/{n}')
===
# Appliquez l'opération logique AND aux 2 nombres en code binaire
```

### OR logique

Rappel

```python
0 | 0 = 0
0 | 1 = 1
1 | 0 = 1
1 | 1 = 1
```

```{codeplay}
from random import randint
score = 0
n = 3

for i in range(n):
    a = randint(1, 15)
    b = randint(1, 15)

    print(f'  {a:04b}')
    print(f'| {b:04b}')
    reponse = input('= ')
    solution = f'{a | b:04b}'

    if reponse == solution:
        score += 1
    else:
        print(f'faux! Réponse correcte = {solution}')
    print()
print(f'score = {score}/{n}')
===
# Appliquez l'opération logique OR aux 2 nombres en code binaire
```

### XOR logique

Rappel

```python
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
```

```{codeplay}
from random import randint
score = 0
n = 3

for i in range(n):
    a = randint(1, 15)
    b = randint(1, 15)

    print(f'  {a:04b}')
    print(f'^ {b:04b}')
    reponse = input('= ')
    solution = f'{a ^ b:04b}'

    if reponse == solution:
        score += 1
    else:
        print(f'faux! Réponse correcte = {solution}')
    print()
print(f'score = {score}/{n}')
===
# Appliquez l'opération logique XOR aux 2 nombres en code binaire
```
