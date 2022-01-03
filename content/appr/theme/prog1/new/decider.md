# Décider - `if`

Un programme doit parfois faire un choix, basé sur une conditions. Ceci est exprimé par la fameuse expression `if-else` ou si-sinon en français.

## Etes vous majeur ?

```{codeplay}
age = input('Entrez votre age: ')

if int(age) < 17:
    print('accès interdit - vous êtes mineur')
else:
    print('accès OK - vous êtes majeur')
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