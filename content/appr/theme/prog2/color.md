# Couleur - `dot`

## Rouge-Vert-Bleu (RVB)

Dans un ordinateur les couleurs sont exprimé par un triplet de nombres.
Ces nombres indiquent l'intensité des trois couleurs de base : rouge-vert-bleu (RVB)

L'intensité de couleur est exprimé soit :

- en virgule flottante sur dans une plage de 0.0 ... 1.0
- en entiers sur une plage de 0 ... 255

En utilisant la définition précédente nous pouvons exprimer les couleurs aussi avec un triplet.

```{codeplay}
from turtle import *
up()

color(1, 0, 0)  # rouge
back(200)
dot(80)

color(1, 1, 0)  # jaune
forward(100)
dot(80)

color(0, 1, 0)  # vert
forward(100)
dot(80)

color(0, 1, 1)  # cyan
forward(100)
dot(80)

color(0, 0, 1)  # bleu
forward(100)
dot(80)
```

## Mode couleur

Il a deux façon d'exprimer les 3 composantes RVB :

- avec un nombre à virgule flottante dans l'intervalle [0, 1]
- avec un entier dans l'intervalle [0, 255]

La fonction `colormode()` retourne le mode actuelle si utilisé sans argument. Si un argument est fourni (1 ou 255), ce mode est activé.

```{codeplay}
from turtle import *
print(colormode())

colormode(255)
print(colormode())
```

```{codeplay}
from turtle import *
colormode(255)
up()

color(255, 0, 0)  # rouge
back(200)
dot(80)

color(255, 255, 0)  # jaune
forward(100)
dot(80)

color(0, 255, 0)  # vert
forward(100)
dot(80)

color(0, 255, 255)  # cyan
forward(100)
dot(80)

color(0, 0, 255)  # bleu
forward(100)
dot(80)
```

## Intensité

Voici un programme qui affiche les intensité pour rouge en incréments de 25%.

```{codeplay}
from turtle import *
up()

color(0, 0, 0)  # 0%
back(200)
dot(80)

color(0.25, 0, 0)  # 25%
forward(100)
dot(80)

color(0.5, 0, 0)  # 50%
forward(100)
dot(80)

color(0.75, 0, 0)  # 75%
forward(100)
dot(80)

color(1, 0, 0)  # 100%
forward(100)
dot(80)
```

**Exercice** : Faites un dégradé pour la couleur bleu.

## Mélanger RVB

```{codeplay}
from turtle import *

d = 120
up()
goto(-d, -d)

color('red')
dot(d)

color('yellow')
forward(d)
dot(d)

color('lime')
forward(d)
left(120)
dot(d)

color('cyan')
forward(d)
dot(d)

color('blue')
forward(d)
left(120)
dot(d)

color('magenta')
forward(d)
dot(d)
```

## Intensité des couleurs

Dans l'exemple ci-dessous nous agissons sur la cou

```{codeplay}
from turtle import *
up()

goto(-150, -150)
left(90)
d = 50

for x in [0, 0.2, 0.4, 0.6, 0.8, 1]:
    c = (x, 0, 0)
    color(c)
    dot(d)
    setx(xcor() + 40)
    write(c, font=(None, 18))
    setx(xcor() - 40)
    forward(d + 10) 
```

**Exercice** : Dessiner un dégradé pour vert, bleu, magenta, cyan

## Matrice des couleurs

Dans ce programme les axes x et y correspondent à une des couleurs RVG.

```{codeplay}
from turtle import *

getscreen().bgcolor('gray')
colormode(255)
speed(0)
up()

d = 30
for y in range(0, 255, d):
    for x in range(0, 255, d):
        goto(x-127, y-127)
        color((y, x, 0))
        dot(d)
```

**Exercice** : Modifiez `color((y, x, x))`, `color((y, 0, x))`, etc.

## Cube des couleurs

Dans l'exemple suivant nous dessinons les 3 axes

- rouge
- vert
- bleu

Ensuite nous dessinons un cube de couleurs.
Voici les 8 sommets du cube :

- noir - (0, 0, 0)
- rouge - (1, 0, 0)
- vert - (0, 1, 0)
- bleu - (0, 0, 1)
- jaune - (1, 1, 0)
- cyan - (0, 1, 1)
- magenta - (1, 0, 1)
- blanc - (1, 1, 1)

```{codeplay}
from turtle import *

def axe(angle, couleur):
    left(angle)
    forward(180)
    stamp()
    write('  '+couleur, font=(None, 18))
    back(180)
    
getscreen().bgcolor('black')
color('white')
axe(0, 'red')
axe(90, 'green')
axe(135, 'blue')
speed(0)
up()

n = 8
d = 150/n
for z in range(n):
    for y in range(n):
        for x in range(n):
            goto(d*(x-z/2), d*(y-z/2))
            color((x/(n-1), y/(n-1), z/(n-1)))
            dot(d)
```

## Synthèse additive

La **synthèse additive** des couleurs est le procédé consistant à combiner trois lumières colorées dans le but d'obtenir une lumière colorée quelconque.

Dans un écran d'ordinateur (ou smartphone) on utilise les couleurs rouge, vert, et bleu, d'ou l'acronyme **RVB**. Le mélange de :

- rouge et bleu donne magenta,
- rouge et vert donne jaune,
- vert et bleu donne cyan.

La combinaison de toutes les trois couleurs de base donne blanc.

```{codeplay}
from turtle import *
getscreen().bgcolor('black')
r = 120
goto(-50, -50)

for x in ('red', 'lime', 'blue'):
    dot(2 * r, x)
    forward(r)
    left(120)

left(30)
for x in ('yellow', 'cyan', 'magenta', 'white'):
    color(x)
    begin_fill()
    for i in range(4):
        circle(-r, 60)
        right(60)
    end_fill()
    right(60 if x == 'magenta' else 120) 
````

## Synthèse soustractive

La **synthèse soustractive** des couleurs et le procédé consistant à combiner l'absorption de trois colorant pour obtenir les nuances des couleurs.

Les trois colorant généralement utilisé en impression sont cyan, jaune et magenta, d'ou le terme CJM.

Le mélange de :

- jaune et cyan donne vert,
- jaune et magenta donne rouge,
- cyan et magenta donne bleu.

La combinaison de toutes les trois couleurs de base donne noir.

```{codeplay}
from turtle import *
r = 120
goto(-50, -50)

for x in ('cyan', 'magenta', 'yellow'):
    dot(2 * r, x)
    forward(r)
    left(120)

left(30)
for x in ('blue', 'red', 'lime', 'black'):
    color(x)
    begin_fill()
    for i in range(4):
        circle(-r, 60)
        right(60)
    end_fill()
    right(60 if x == 'lime' else 120)  
````

```{codeplay}

````

```{codeplay}

````
