# Couleur - `dot`

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
