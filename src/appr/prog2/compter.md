# Compter - `bin`

Compter est l'opération utilisée pour savoir combien d'objets il y a dans un ensemble de taille fini. Nous utilisons alors les nombres naturels, aussi appelés les entiers non négatifs.
Le fait que nous humains avons dix doigts nous a menés à adopter le système décimal (base 10).

Un ordinateur par contre représente les nombres en système binaire (base 2). Une des principales raisons est l'extrême simplicité de représentation de l'information dans un système matériel avec seulement 2 états (électrique, magnétique ou optique). Nous allons voir que :

- la fonction `bin(d)` retourne un code binaire (précédé par `0b`),
- la fonction `oct(d)` retourne un code octal (précédé par `0o`),
- la fonction `hex(d)` retourne un code hexadécimal (précédé par `0x`).

```{question}
La fonction `bin()` renvoie une valeur de type

{f}`int`  
{f}`bin`  
{f}`bool`  
{v}`str`
```

## Le système décimal

Voici les nombres entiers de 0 à 99.

```{codeplay}
:file: bin1.py
print('décimal')
for i in range(100):
    print(i, end=' ')

print('\nbinaire')
for i in range(16):
    print(bin(i), end=' ')
```

En informatique, nous utilisons fréquemment trois autres représentations :

- binaire (base 2)
- octale (base 8)
- hexadécimale (base 16)

```{exercise}
Modifiez le nombre `n` et réexécutez le code.
```

```{codeplay}
:file: bin2.py
n = 123

print('décimal =', n)
print('binaire =', bin(n))
print('octal =', oct(n))
print('hexadécimal =', hex(n))
```

## Compter avec les doigts

Nous pouvons utiliser nos doigts pour compter et pour représenter des nombres.
Le système le plus simple est le système **unaire**, ou chaque nombre est représenté par le nombre équivalent de doigts levés.

Le petit programme ci-dessous dessine les 5 doigts d'une main pour créer une animation qui montre comment compter avec les doigts de 0 à 5.

```{codeplay}
:file: bin3.py
from turtle import *
from time import *

getscreen().bgcolor('azure')

def finger(x):
    begin_fill()
    forward(x)
    circle(-20, 180)
    forward(x)
    left(180)
    end_fill()

for i in range(6):
    reset()
    speed(0)
    backward(40)
    write(i, font=('Courier', 100), align='right')
    left(90)
    fillcolor('pink')
    for j in range(5-i):
        finger(30)
    for j in range(i):
        finger(120)
    sleep(2)
```

## Système binaire

La fonction `bin(i)` retourne le code binaire du nombre entier `i` précédé de `0b`.

```{codeplay}
:file: bin4.py
for i in range(16):
    print(i, '=', bin(i))
````

La chaîne formaté (f-string) `{i:4b}` à l'intérieur de la fonction `print()` affiche le code binaire sur 4 positions.

```{codeplay}
:file: bin5.py
for i in range(16):
    print(f'{i:2} = {i:4b}')
```

```{codeplay}
:file: bin6.py
for i in range(100, 105):
    print(f'{i:2} = b{i:08b} = x{i:2x}')
```

```{codeplay}
:file: bin7.py
from random import *

n = 10
score = 0

for i in range(10):
    num = randint(2, 15)
    x = input(f'{num:4b} = ')
    if int(x) == num:
        score += 1
    else:
        print('Faux. Réponse correcte =', num)

print('score =', score, '/', n)
```

```{codeplay}
:file: bin8.py
for i in range(100):
    print(f'{i}={i:x}', end=' ')
```

## Compter en binaire

Si nous utilisons le système binaire, nous pouvons compter de 0 à 31 avec les 5 doigts d'une main. Voici une animation qui fait la démonstration.

```{codeplay}
:file: bin9.py
from turtle import *
from time import *

getscreen().bgcolor('azure')

def finger(x):
    begin_fill()
    forward(x)
    circle(-20, 180)
    forward(x)
    left(180)
    end_fill()
    
    
def hand(n):
    speed(0)
    width(5)
    left(90)
    for i in range(5):
        digit = 2 ** (4-i) & n
        fillcolor('pink')
        if digit:
            finger(120)
        else:
            finger(30)
        fillcolor('black')
        write(digit, font=('Courier', 24), align='right')

for i in range(32):
    reset()
    write(i, font=('Courier', 100), align='right')
    hand(i)
    sleep(2)
```

## Entier naturel sur 4 bits

Cette visualisation montre le cercle des entiers naturels encodé sur 4 bits.

```{codeplay}
:file: bin10.py
from turtle import *
from time import *

getscreen().bgcolor('azure')
hideturtle()
up()
goto(0, 120)

right(360/32)
for i in range(16):
    write(i, font=('Courier', 14), align='center')
    sety(ycor() - 15)
    write(f'{i:04b}', font=('Courier', 8), align='center')
    sety(ycor() + 15)
    forward(50)
    right(360/16)
```

## Entier relatif sur 4 bits

Cette visualisation montre le cercle des entiers relatifs encodé sur 4 bits.

```{codeplay}
:file: bin11.py
from turtle import *
from time import *

getscreen().bgcolor('azure')
hideturtle()
up()
goto(0, 120)

right(360/32)
for i in range(16):
    if i < 8: 
        write(i, font=('Courier', 14), align='center')
    else:
        color('red')
        write(i-16, font=('Courier', 14), align='center')
    sety(ycor() - 15)
    write(f'{i:04b}', font=('Courier', 8), align='center')
    sety(ycor() + 15)
    forward(50)
    right(360/16)
```

## Quiz

### Compter avec la main

```{codeplay}
:nocontrols:

def quiz(question, solution):
    answer = 0
    print(question)
    while answer != solution:
      answer = int(input())
      if answer > solution:
          print('trop grand')
      elif answer < solution:
          print('trop petit')
      else:
          print('Bravo')

quiz('Quel est le plus grand nombre binaire représentable avec UNE main', 2 ** 5 - 1)
===
# UNE main
```

```{codeplay}
:nocontrols:

def quiz(question, solution):
    answer = 0
    print(question)
    while answer != solution:
      answer = int(input())
      if answer > solution:
          print('trop grand')
      elif answer < solution:
          print('trop petit')
      else:
          print('Bravo')

quiz('Quel est le plus grand nombre binaire représentable avec DEUX mains', 2 ** 10 - 1)
===
# DEUX mains
```

Utilisez vos doigts pour compter en binaire.

```{codeplay}
from random import shuffle
a = 5

nombres = list(range(2 ** a))
shuffle(nombres)
score = 0

for n in nombres[:8]:
    reponse = int(input(f'{n:05b} = '))
    if reponse == n:
        score += 1
    else:
        print('faux! Réponse correcte:', n)
     
print('score =', score, '/ 8')
===
# Transformez 8 codes binaires avec 5 digits en décimal
```

### Code binaire

```{codeplay}
from random import shuffle

nombres = list(range(8))
shuffle(nombres)
score = 0

for n in nombres:
    reponse = int(input(f'{n:03b} = '))
    if reponse == n:
        score += 1
    else:
        print('faux! Réponse correcte:', n)
     
print('score =', score, '/ 8')
===
# Transformez 8 codes binaires avec 3 digits en décimal
```

```{codeplay}
from random import shuffle

nombres = list(range(16))
shuffle(nombres)
score = 0

for n in nombres[:8]:
    reponse = int(input(f'{n:04b} = '))
    if reponse == n:
        score += 1
    else:
        print('faux! Réponse correcte:', n)
     
print('score =', score, '/ 8')
===
# Transformez 8 codes binaires avec 4 digits en décimal
```

### Code hexadécimal

Petit rappel:

```python
a = 1010
b = 1011
c = 1100
d = 1101
e = 1110
f = 1111
```

```{codeplay}
from random import shuffle
a = 4

nombres = list(range(2 ** a))
shuffle(nombres)
score = 0

for n in nombres[:8]:
    reponse = input(f'{n:01x} = ')
    if reponse == f'{n:04b}':
        score += 1
    else:
        print(f'faux! Réponse correcte = {n:04b}')
     
print(f'score = {score}/8')
===
# Transformez 8 codes hexa en code binaire à 4 bits
```

```{codeplay}
from random import shuffle
a = 8
nombres = list(range(2 ** a))
shuffle(nombres)
score = 0

for n in nombres[:8]:
    reponse = input(f'{n:02x} = ')
    if reponse == f'{n:08b}':
        score += 1
    else:
        print(f'faux! Réponse correcte = {n:08b}')
     
print(f'score = {score}/8')
===
# Transformez 8 codes hexa en code binaire à 8 bits
```

### Incrémentation

Le mot en informatique pour *additionner 1* est incrémentation.

```{codeplay}
from random import shuffle
a = 4
nombres = list(range(2 ** a))
shuffle(nombres)
score = 0
n = 3

for i in nombres[:n]:
    print(f'{n:04b} + 1')
    reponse = input()
    solution = f'{n+1:04b}'
    if reponse == solution:
        score += 1
    else:
        print(f'faux! Réponse correcte = {solution}')
    print()
print(f'score = {score}/{n}')
===
# Additionnez 1 au code binaire
```

### Addition

```{codeplay}
from random import randint
score = 0
n = 3

for i in range(n):
    a = randint(1, 7)
    b = randint(1, 7)

    print(f'  {a:04b}')
    print(f'+ {b:04b}')
    reponse = input('= ')
    solution = f'{a + b:04b}'

    if reponse == solution:
        score += 1
    else:
        print(f'faux! Réponse correcte = {solution}')
    print()
print(f'score = {score}/{n}')
===
# Additionnez 2 nombres en code binaire
```

### Soustraction

```{codeplay}
from random import randint
score = 0
n = 3

for i in range(n):
    a = randint(7, 15)
    b = randint(1, 7)

    print(f'  {a:04b}')
    print(f'- {b:04b}')
    reponse = input('= ')
    solution = f'{a - b:04b}'

    if reponse == solution:
        score += 1
    else:
        print(f'faux! Réponse correcte = {solution}')
    print()
print(f'score = {score}/{n}')
===
# Soustrayez 2 nombres en code binaire
```
