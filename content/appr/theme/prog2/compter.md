# Compter - `bin`

Compter est l'opération utilisée pour savoir combien d'objets il y a dans un ensemble de taille fini. On utilise alors les nombres naturels, aussi appelé les entiers non-négatifs.

Les humains ont 10 doigts, c'est la raison que nous avons adopté le système décimal. Un ordinateur par contre représente les nombre en système binaire.

- la fonction `bin(d)` retourne un code binaire
- la fonction `oct(d)` retourne un code octale
- la fonction `hex(d)` retourne un code hexadécimale

## Le système décimal

Voici les nombres entiers de 0 à 99.

```{codeplay}
print('décimal')
for i in range(100):
    print(i, end=' ')

print('\nbinaire')
for i in range(16):
    print(bin(i), end=' ')
```

## Compter avec les doigts

Nous pouvons utiliser nos doigts pour compter et pour représenter des nombres.
Le système le plus simple est le système **unaire**, ou chaque nombre est représenté par le nombre équivalent de doigts levés.

Le petit programme ci-dessous dessine les 5 doigts d'une main pour créer une animation qui montre comment compter avec les doigts de 0 à 5.

```{codeplay}
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
    back(40)
    write(i, font=('Courier', 100), align='right')
    left(90)
    fillcolor('pink')
    for j in range(5-i):
        finger(30)
    for j in range(i):
        finger(120)
    sleep(2)
```

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

## Système binaire

La fonction `bin(i)` retourne le code binaire du nombre entier `i` précédé de `0b`.

```{codeplay}
for i in range(16):
    print(i, '=', bin(i))
````

La chaîne formaté (f-string) '{i:4b}' à l'intérieur de la fonction `print()` affiche le code binaire sur 4 positions.

```{codeplay}
for i in range(16):
    print(f'{i:2} = {i:4b}')
```

```{codeplay}
for i in range(100, 105):
    print(f'{i:2} = b{i:08b} = x{i:2x}')
```

```{codeplay}
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
for i in range(100):
    print(f'{i}={i:x}', end=' ')
```

## Compter en binaire

Si nous utilisons le système binaire, nous pouvons compter de 0 à 31 avec les 5 doigts d'une main. Voici une animation qui fait la démonstration.

```{codeplay}
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
````

## Entier naturel sur 4 bits

```{codeplay}
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
````

## Entier relatif sur 4 bits

```{codeplay}
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
````

```{codeplay}

````

```{codeplay}

````

```{codeplay}

````

```{codeplay}

````
