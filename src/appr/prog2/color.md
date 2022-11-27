# Nuancer - `color`

Dans ce chapitre nous allons voir les couleurs dans toutes leurs nuances. En informatique, les couleurs sont basées sur les trois couleurs primaires **rouge**, **vert** et **bleu**. Leur combinaison respective permet de créer tout le spectre des couleurs visibles. Nous allons voir que :

- la fonction `color(r, v, b)` représente une couleur avec trois nombres,
- la fonction `color('#rvb')` représente une couleur avec un hexadécimal,
- la fonction `color(r, v, b, a)` ajoute la transparence `a` (alpha).

```{question}
L'expression `color('#facc00')` représente une couleur

{f}`bleu`  
{f}`très sombre`  
{v}`orange`  
{f}`grise`
```

## Rouge-Vert-Bleu (RVB)

Dans un ordinateur les couleurs sont exprimées par un triplet de nombres.
Ces nombres indiquent l'intensité des trois couleurs de base : rouge-vert-bleu (RVB)

L'intensité de couleur est exprimée soit :

- en virgule flottante dans une plage de 0.0 ... 1.0
- en entier sur une plage de 0 ... 255

En utilisant la définition précédente, nous pouvons exprimer les couleurs aussi avec un triplet.

```{codeplay}
:file: color1.py
from turtle import *
up()

color(1, 0, 0)  # rouge
backward(200)
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

Il a deux façons d'exprimer les 3 composantes RVB :

- avec un nombre à virgule flottante dans l'intervalle [0, 1]
- avec un entier dans l'intervalle [0, 255]

La fonction `colormode()` retourne le mode actuel si utilisé sans argument. Si un argument est fourni (1 ou 255), ce mode est activé.

```{codeplay}
:file: color2.py
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
backward(200)
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

Voici un programme qui affiche les intensités pour rouge en incréments de 25%.

```{exercise}
Faites un dégradé pour la couleur bleue.
```

```{codeplay}
:file: color3.py
from turtle import *
up()

color(0, 0, 0)  # 0%
backward(200)
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

## Mélanger RVB

```{codeplay}
:file: color4.py
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

Dans l'exemple ci-dessous, nous agissons sur la composante rouge.

```{exercise}
Dessinez un dégradé pour vert, bleu, magenta, cyan
```

```{codeplay}
:file: color5.py
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

## Matrice des couleurs

Dans ce programme les axes x et y correspondent à une des couleurs RVG.

```{exercise}
Modifiez `color((y, x, x))`, `color((y, 0, x))`, etc.
```

```{codeplay}
:file: color6.py
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

## Cube des couleurs

Dans l'exemple suivant, nous dessinons les 3 axes

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
:file: color7.py
from turtle import *

def axe(angle, couleur):
    left(angle)
    forward(180)
    stamp()
    write('  '+couleur, font=(None, 18))
    backward(180)
    
getscreen().bgcolor('black')
color('white')
axe(0, 'rouge')
axe(90, 'vert')
axe(135, 'bleu')
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

Dans un écran d'ordinateur (ou smartphone) on utilise les couleurs rouge, vert, et bleu, d'où l'acronyme **RVB**. Le mélange de :

- rouge et bleu donne magenta,
- rouge et vert donne jaune,
- vert et bleu donne cyan.

La combinaison de toutes les trois couleurs de base donne blanc.

```{codeplay}
:file: color8.py
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
        if i == 2:
            end_fill()
    right(60 if x == 'magenta' else 120) 
````

## Synthèse soustractive

La **synthèse soustractive** des couleurs et le procédé consistant à combiner l'absorption de trois colorants pour obtenir les nuances des couleurs.

Les trois colorants généralement utilisés en impression sont cyan, jaune et magenta, d'où le terme CJM.

Le mélange de :

- jaune et cyan donne vert,
- jaune et magenta donne rouge,
- cyan et magenta donne bleu.

La combinaison de toutes les trois couleurs de base donne noir.

```{codeplay}
:file: color9.py
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
        if i == 2:
            end_fill()
    right(60 if x == 'lime' else 120)  
```

## Dégradé radial

```{codeplay}
from turtle import *
colormode(255)
hideturtle()

for x in range(255):
    dot(255-x, (x, x, x))
```

```{codeplay}
from turtle import *
colormode(255)
hideturtle()

for x in range(0, 255, 5):
    dot(255-x, (x, x, x))
    forward(0.5)
```

```{codeplay}
from turtle import *
colormode(255)
hideturtle()

for x in range(0, 255, 5):
    dot(255-x, (x, x, 0))
    forward(0.5)
```

```{codeplay}
from turtle import *
colormode(255)
hideturtle()

for x in range(0, 255, 5):
    dot(255-x, (x, 0, 0))
    forward(0.5)
```

## Dégradé linaire

```{codeplay}
from turtle import *
colormode(255)
hideturtle()
speed(0)

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

for x in range(255):
    color(x, x, x)
    ligne((x, -200), (x, 200))
```

```{codeplay}
from turtle import *
colormode(255)
hideturtle()
left(90)
width(7)
speed(0)

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

for x in range(0, 255, 5):
    color(x, x, x)
    ligne((x, -200), (x, 200))
```

## Quiz

### Taille image

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

### Octets, Ko/Mo/Go

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
