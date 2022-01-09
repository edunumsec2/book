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

## Mélanger vert et rouge

```{codeplay}
from turtle import *

goto(0, -80)
right(30)
fillcolor('red')
begin_fill()
circle(100, 240)
left(120)
circle(-100, 120)
end_fill()

right(60)
fillcolor('yellow')
begin_fill()
circle(-100, 120)
right(60)
circle(-100, 120)
end_fill()

fillcolor('lime')
begin_fill()
circle(-100, 240)
right(120)
circle(100, 120)
end_fill()
```

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

```{codeplay}
from turtle import *
up()

d = 50

for x in [0, 0.2, 0.4, 0.6, 0.8, 1]:
    c = (x, 0, 0)
    color((x, 0, 0))
    dot(d)
    sety(ycor() + d)
    write(c, font=(None, 8), align='center')
    sety(ycor() - d)
    forward(d)
```

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

```{codeplay}
from turtle import *

getscreen().bgcolor('black')
colormode(255)
speed(0)
up()

d = 30
for z in range(0, 255, d):
    for y in range(0, 255, d):
        for x in range(0, 255, d):
            goto(x-64-z/2, y-64-z/2)
            color((x, y, z))
            dot(d)
```

```{codeplay}

````

```{codeplay}

````

```{codeplay}

````

```{codeplay}

````
