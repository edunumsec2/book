# Aléatoire - `random`

Le module `random` permet de créer des nombres pseudo-aléatoires. Il met à disposition 13 fonctions:

- `choice`
- `expovariage`
- `gauss`
- ...

```{codeplay}
import random
print(dir(random))
```

## Nombre aléatoire dans [0 ... 1]
La fonction `random()` retourne une valeur aléatoire dans la plage [0, 1].

```{codeplay}
from turtle import *
from random import *

n = 20
for i in range(n):
    setx((i/n - 0.5) * 600)
    write(i)
    y = random()
    sety((y - 0.5) * 400)
    dot()
    write(y)
    sety(0)
```

## Entier aléatoire

La fonction `random.randint(a, b)` retourne une valeur aléatoire dans la plage [a, b].

```{codeplay}
from turtle import *
from random import *

n = 20
for i in range(n):
    setx((i/n - 0.5) * 600)
    write(i)
    y = randint(-200, 200)
    sety(y)
    dot()
    write(y)
    sety(0)
```

## Choisir dans une liste

La fonction `choice(liste)` retourne un élément aléatoire d'une liste.
Dans l'exemple suivant nous choisissons entre 5 couleurs.

```{codeplay}
from turtle import *
from random import *

up()
n = 60
for y in range(200-n, -200, -n):
    for x in range(-300+n, 300, n):
        setpos(x, y)
        color(choice(['red', 'lime', 'pink', 'yellow', 'cyan']))
        dot(n)
```

Dans l'exemple suivant nous choisissons entre 3 chaînes de texte.

```{codeplay}
from random import choice

for i in range(5):
    c = choice(['gagné', 'perdu', 'match nul'])
    print(c)
```

La fonction `random()` retourne un nombre aléatoire dans l'intervalle [0, 1].

```{codeplay}
from random import random
    
for i in range(3):
    print(random())
```

La fonction `randint(a, b)` retourne un entier aléatoire dans l'intervalle [a, b].

```{codeplay}
from random import randint
    
print('randint - random integer')
for i in range(15):
    print(randint(0, 9), end=' ')
```



## Permuter

La function `shuffle()` permet de permuter les éléments d'une liste. Ceci est l'équivalent de ce qu'on fait avec des cartes de jeux, quand on les mélange.

```{codeplay}
from random import *

a = list(range(10))
print(a)

for i in range(3):
    shuffle(a)
    print(a)
```

## Distribution normale

Dans l'exemple suivant les variables x e y suivent une distribution normale avec mu=0 et sigma=50.

```{codeplay}
from turtle import *
from random import *

speed(0)
up()

for i in range(1000):
    x = gauss(0, 50)
    y = gauss(0, 50)
    goto(x, y)
    dot()
```