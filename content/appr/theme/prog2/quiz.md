# Quiz

## Taille image

```{codeplay}
solution = 640 * 480 * 3
reponse = 0
===
print("Quelle est taille d'une image couleur de 640 x 480 pixels ?")
while reponse != solution:
  reponse = int(input())
print('Bravo')
```

```{codeplay}
solution = 2 ** 8
reponse = 0
===
while reponse != solution:
    reponse = int(input('nombre de combinaisons dans un octet: '))
print('Bravo')
```

## Octets, kilo/méga-octet

```{codeplay}
def quiz(question, solution):
  print(question)
  answer = ''
  while answer != solution:
    answer = int(input())
  print('Bravo')

quiz('Quel est le nombre de combinaison dans un octet?', 2**8)
===
# octet
```

```{codeplay}
def quiz(question, solution):
  print(question)
  answer = ''
  while answer != solution:
    answer = int(input())
  print('Bravo')

quiz("Quel est le nombre d'octets dans 1 ko?", 2**10)
===
# kilo-octet
```

```{codeplay}
def quiz(question, solution):
  answer = ''
  while answer != solution:
    answer = int(input(question))
  print('Bravo')
quiz("Quel est le nombre d'octets dans 1 Mo:", 2**20)
===
# méga-octet
```

## Compter avec les doigts

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

## Liste

```{codeplay}
liste = list('python')
===
# Trouve les 2 derniers éléments de liste
solution = liste[2]
===
if solution == liste[-2:]:
  print('Bravo')
else:
  print(solution)
  print('Essaye encore une fois')
```

## Code binaire

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

## Compter avec la main

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

## Code hexadécimal

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

## Incrémentation

Incrémenter veux dire *additionner 1*

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

## Addition

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

## Soustraction

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

## AND logique

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

## OR logique

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

## XOR logique

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
