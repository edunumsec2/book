# Logique par bit - `&`

Dans ce chapitre nous allons explorer des opérateurs logiques qui opèrent sur chaque bit d'une opérande séparément.

- l'opérateur `&` effectue un **and** par bit
- l'opérateur `|` effectue un **or** par bit
- l'opérateur `^` effectue un **xor** par bit

## Bitwise and (`&`)

```{codeplay}
a = 0b11110000
b = 0b10110111

print('a   =', bin(a))
print('b   =', bin(b))
print('a&b =', bin(a & b))
```

## Bitwise or (`|`)

```{codeplay}
a = 0b11110000
b = 0b10110111

print('a   =', bin(a))
print('b   =', bin(b))
print('a|b =', bin(a | b))
```

## Bitwise xor (`^`)

```{codeplay}
a = 0b11110000
b = 0b10110111

print(f'a   = {a:08b}')
print(f'b   = {b:08b}')
print(f'a^b = {a ^ b:08b}')
```

## Bitwise inversion (`~`)

```{codeplay}
a = 0b11110010

print(f'a  = {a:08b}')
print(f'~a = {~a & 0xff:08b}')
```

## Pixels noir et blanc

Par la suite nous affichons les pixels comme une image noir est blanc:

- 0 = pixel blanc
- 1 = pixel noir

```{codeplay}
from turtle import *

up()
a = 0b11011001
d = 50
back(200)
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