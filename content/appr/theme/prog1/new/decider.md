# Décider - `if`

Un programme doit parfois faire un choix, basé sur une conditions. Ceci est exprimé par la fameuse expression `if-else` ou si-sinon en français.

## Etes-vous majeur ?

Basé sur votre âge, le programme décide si vous êtes majeur ou pas.

```{codeplay}
age = input('Entrez votre age: ')

if int(age) < 17:
    print('accès interdit - vous êtes mineur')
else:
    print('accès OK - vous êtes majeur')
```

## Pair ou impair ?

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

Un programme de dessin avec la tortue est une séquence d'instructions. Si la tortue se déplace que sur les lignes d'une grille, nous pouvons représenter un chemin par une séquence d'action ou chaque action peut être représenter avec une seule lettre :

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

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```
