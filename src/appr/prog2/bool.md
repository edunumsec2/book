# Raisonner - `bool`

Raisonner c'est lier logiquement entre elles des propositions pour aboutir à une proposition nouvelle, à une conclusion. La logique analyse de façon rigoureuse des propositions qui sont soit vraies soit fausses. On parle de la logique booléenne. Nous allons voir que :

- les deux valeurs logiques sont `True` et `False`,
- l'opération de négation `not` donne l'inverse,
- les mots-clés `and` et `or`  sont des opérations logiques.

```{question}
Une porte logique est

{f}`un port d'entrée`  
{f}`une table de vérité`  
{v}`un circuit électronique`  
{f}`une opération booléenne`
```

## Table de vérité

Une table de vérité donne sous forme de tableau le résultat pour une opération logique pour toutes ses configurations. Par exemple pour deux propositions `p` et `q` nous avons 4 possibilités de combinaison et 4 résultats possibles pour l'opération `and`.

p     | q     | p and q
------|-------|---------
False | False | False
False | True  | False
True  | False | False
True  | True  | True



## Négation

Voici la table de vérité pour l'opérateur `not`.

```{logic}
:height: 100
:mode: tryout

{
  "v": 2,
  "out": [{"pos": [210, 50], "id": 0}],
  "gates": [{"type": "NOT", "pos": [140, 50], "in": 1, "out": 2}],
  "in": [{"pos": [70, 50], "id": 3, "name": "p", "val": 0}],
  "wires": [[2, 0], [3, 1]]
}
```

p     |not p
------|-----
False |True
True  |False

```{codeplay}
:file: bool1.py
print('p', 'not p', sep='\t| ')
print('--------' * 2)
for p in (False, True):
    print(p, not p, sep='\t| ')
```

`not False =` {bl}`False|>True`  
`not True  =`  {bl}`>False|True`  

## Et logique

```{logic}
:height: 140
:mode: tryout

{
  "v": 2,
  "opts": {"showGateTypes": true},
  "gates": [{"type": "AND", "pos": [160, 70], "in": [0, 1], "out": 2}],
  "in": [{"pos": [60, 40], "id": 3, "name": "p", "val": 0}, {"pos": [60, 100], "id": 4, "name": "q", "val": 0}],
  "out": [{"pos": [230, 70], "id": 5}],
  "wires": [[3, 0], [4, 1], [2, 5]]
}
```

La fonction `et` donne vrai si toutes les entrées sont vraies.

p     | q     | p and q
------|-------|--------
False | False | False
False | True  | False
True  | False | False
True  | True  | True

```{codeplay}
:file: bool2.py
print('p', 'q', 'p and q', sep='\t| ')
print('--------' * 3)
for p in (False, True):
    for q in (False, True):
        print(p, q, p and q, sep='\t| ')
```

`False and False =` {bl}`>False|True`  
`False and True  =` {bl}`>False|True`  
`True  and False =` {bl}`>False|True`  
`True  and True  =` {bl}`False|>True`  

## Ou logique

La fonction `or` donne vrai si au moins une des entrées est vraie.

p   | q   | p and q
----|-----|---------
0   | 0   | 0
0   | 1   | 1
1   | 0   | 1
1   | 1   | 1

```{codeplay}
:file: bool3.py
print('p', 'q', 'p or q', sep='\t| ')
print('-------------------------')
for p in (False, True):
    for q in (False, True):
        print(p, q, p or q, sep='\t| ')
```

`False or False =` {bl}`>False|True`  
`False or True  =` {bl}`False|>True`  
`True  or False =` {bl}`False|>True`  
`True  or True  =` {bl}`False|>True`

## Exclusive ou

p   | q   | p xor q
----|-----|---------
0   | 0   | 0
0   | 1   | 1
1   | 0   | 1
1   | 1   | 0

`False xor False =` {bl}`>False|True`  
`False xor True  =` {bl}`False|>True`  
`True  xor False =` {bl}`False|>True`  
`True  xor True  =` {bl}`>False|True`

```{codeplay}
:file: bool4.py
print('p', 'q', 'p ^ q', sep='\t')
print('---------------------')
for p in (False, True):
    for q in (False, True):
        print(p, q, p ^ q, sep='\t')
```

## Porte OUI (identité)

C'est un opérateur logique dont la sortie est égale à l'état de l'entrée. Cette fonction ne présente pas d'intérêt d'un point de vue logique, mais peut être utile d'un point de vue technologique.

Voici son schéma technique.

```{codeplay}
:file: bool11.py
from turtle import *

def line(x, y, d):
    up()
    goto(x, y)
    down()
    goto(x + d, y)
    
up()
goto(-100, -100)
down()
left(90)
for i in range(3):
    forward(200)
    right(120)

line(-200, 0, 100)
line(70, 0, 100)
```

## Porte NON

La fonction NON (NOT en anglais) est un opérateur logique qui produit un résultat qui a la valeur inverse son entrée.

Voici son schéma technique. Le cercle représente une inversion de signal.

```{codeplay}
:file: bool12.py
from turtle import *

def line(x, y, d):
    up()
    goto(x, y)
    down()
    goto(x + d, y)
    
up()
goto(-100, -100)
down()
left(90)
for i in range(3):
    forward(200)
    right(120)

up()
goto(72, 0)
down()
circle(-10)

line(-200, 0, 100)
line(92, 0, 100)
```
## Porte ET

La fonction ET (AND en anglais) est un opérateur logique qui produit un résultat qui est VRAI seulement si les deux opérandes d'entrée ont la valeur VRAI.

```{codeplay}
:file: bool5.py
from turtle import *

up()
goto(-100, -100)
down()
left(90)
forward(200)
right(90)
forward(100)
circle(-100, 180)
forward(100)

up()
goto(-200, 50)
seth(0)
down()
forward(100)

up()
goto(-200, -50)
down()
forward(100)

up()
goto(100, 0)
down()
forward(100)
```

Dans la porte ET ci-dessous nous ajoutons 3 objets de la classe `Dot` et nous rendons la porte interactive. Avec la souris nous pouvons cliquer sur les 2 terminaux d'entrée et la sortie va afficher la logique de la porte.

```{codeplay}
:file: bool6.py
from turtle import *

def line(x, y, d):
    up()
    goto(x, y)
    down()
    goto(x + d, y)

up()
goto(-100, -100)
down()
left(90)
forward(200)
right(90)
forward(100)
circle(-100, 180)
forward(100)

line(-200, 50, 100)
line(-200, -50, 100)
line(100, 0, 100)

class Dot(): 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = False
        self.draw()
        
    def draw(self):
        color('yellow' if self.state else 'lightgray')
        goto(self.x, self.y)
        dot(40)
        color('black')
        sety(self.y - 10)
        write(int(self.state), font=(None, 18), align='center')
       
    def inside(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2 < (20 ** 2)
    
    def set(self, state):
        self.state = state
        self.draw()
    
    def toggle(self):
        self.set(not self.state)
        
    def click(self, x, y):
        if self.inside(x, y):
            self.toggle()
    
hideturtle()
speed(0)
up()

p0 = Dot(-200, 50)
p1 = Dot(-200, -50)
p2 = Dot(200, 0)

def f(x, y):
    p0.click(x, y)
    p1.click(x, y)
    p2.set(p0.state and p1.state)
            
getscreen().onclick(f)
getscreen().listen()
```

## Porte OU

La fonction OU (OR en anglais) est un opérateur logique qui produit un résultat qui est VRAI seulement si au moins un des deux opérandes d'entrée a la valeur VRAI.

```{codeplay}
:file: bool7.py
from turtle import *

def line(x, y, d):
    up()
    goto(x, y)
    down()
    goto(x + d, y)
    
up()
goto(-100, -100)
down()
left(60)
circle(200, 60)
right(120)
forward(100)
circle(-100, 180)
forward(100)

line(-200, 50, 120)
line(-200, -50, 120)
line(100, 0, 100)
```

Dans la porte OU ci-dessous nous ajoutons 3 objets de la classe `Dot` et nous rendons la porte interactive. Avec la souris nous pouvons cliquer sur les 2 terminaux d'entrée et la sortie va afficher la logique de la porte.

La classe `Dot` est toujours définie, mais elle n'est plus affichée.

```{codeplay}
:file: bool8.py
class Dot(): 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = False
        self.draw()
        
    def draw(self):
        color('yellow' if self.state else 'lightgray')
        goto(self.x, self.y)
        dot(40)
        color('black')
        sety(self.y - 10)
        write(int(self.state), font=(None, 18), align='center')
       
    def inside(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2 < (20 ** 2)
    
    def set(self, state):
        self.state = state
        self.draw()
    
    def toggle(self):
        self.set(not self.state)
        
    def click(self, x, y):
        if self.inside(x, y):
            self.toggle()
===
from turtle import *

def line(x, y, d):
    up()
    goto(x, y)
    down()
    goto(x + d, y)
    
up()
goto(-100, -100)
down()
left(60)
circle(200, 60)
right(120)
forward(100)
circle(-100, 180)
forward(100)

line(-200, 50, 120)
line(-200, -50, 120)
line(100, 0, 100)

hideturtle()
speed(0)
up()

p0 = Dot(-200, 50)
p1 = Dot(-200, -50)
p2 = Dot(200, 0)

def f(x, y):
    p0.click(x, y)
    p1.click(x, y)
    p2.set(p0.state or p1.state)
            
getscreen().onclick(f)
getscreen().listen()
```

## Porte XOR

La fonction OU exclusif, souvent appelé XOR (eXclusive OR) ou disjonction exclusive, produit un résultat qui a lui-même la valeur VRAI seulement si les deux opérandes ont des valeurs distinctes.

```{codeplay}
:file: bool9.py
from turtle import *

def line(x, y, d):
    up()
    goto(x, y)
    down()
    goto(x + d, y)
    
def arc(x, y):
    up()
    goto(x, y)
    down()
    seth(60)
    circle(200, 60)
    
def gate(a):
    seth(0)
    forward(a)
    circle(-100, 180)
    forward(a)

arc(-100, -100)
arc(-80, -100)
gate(80)
line(-200, 50, 120)
line(-200, -50, 120)
line(100, 0, 100)
```

Dans la porte XOR ci-dessous nous ajoutons 3 objets de la classe `Dot` et nous rendons la porte interactive. Avec la souris nous pouvons cliquer sur les 2 terminaux d'entrée et la sortie va afficher la logique de la porte.

```{codeplay}
:file: bool10.py
class Dot(): 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = False
        self.draw()
        
    def draw(self):
        color('yellow' if self.state else 'lightgray')
        goto(self.x, self.y)
        dot(40)
        color('black')
        sety(self.y - 10)
        write(int(self.state), font=(None, 18), align='center')
       
    def inside(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2 < (20 ** 2)
    
    def set(self, state):
        self.state = state
        self.draw()
    
    def toggle(self):
        self.set(not self.state)
        
    def click(self, x, y):
        if self.inside(x, y):
            self.toggle()

from turtle import *

def line(x, y, d):
    up()
    goto(x, y)
    down()
    goto(x + d, y)
    
def arc(x, y):
    up()
    goto(x, y)
    down()
    seth(60)
    circle(200, 60)
    
def gate(a):
    seth(0)
    forward(a)
    circle(-100, 180)
    forward(a)
===
arc(-100, -100)
arc(-80, -100)
gate(80)
line(-200, 50, 120)
line(-200, -50, 120)
line(100, 0, 100)

hideturtle()
speed(0)
up()

p0 = Dot(-200, 50)
p1 = Dot(-200, -50)
p2 = Dot(200, 0)

def f(x, y):
    p0.click(x, y)
    p1.click(x, y)
    p2.set(p0.state ^ p1.state)
            
getscreen().onclick(f)
getscreen().listen()
```

## Nombre 4-bits

Le programme suivant définit une classe `Bin4`. Elle:

- dessine un nombre à 4 digits binaires
- à la position (x, y)
- vérifie si un click est dedans
- incrémente le nombre

```{codeplay}
:file: class9.py
from turtle import *
hideturtle()
speed(0)
up()

class Bin4(): 
    def __init__(self, pos=(0, 0)):
        self.pos = pos
        self.n = 0
        self.draw()
        
    def draw(self):
        goto(self.pos)
        dot(60, 'linen')
        sety(self.pos[1]-8)
        write(f'{self.n:04b}', font=('Courier', 16), align='center')
    
    def inside(self, x, y):
        x0, y0 = self.pos
        return (-30 < x-x0 < 30) and (-30 < y-y0 < 30)
    
    def inc(self):
        self.n = (self.n + 1) % 16
        self.draw()
        
    def set(self, n):
        self.n = n % 16
        self.draw()
        
    def click(self, x, y):
        if self.inside(x, y):
            self.inc()
        
b0 = Bin4((-100, 100))
b1 = Bin4((100, 100))
b2 = Bin4((0, -100))

def f(x, y):
    b0.click(x, y)    
    b1.click(x, y)
    b2.set(b0.n + b1.n)
            
getscreen().onclick(f)
getscreen().listen()
```

## Une ALU

L'unité arithmétique et logique (en anglais arithmetic–logic unit, ALU), est la partie de l'ordinateur chargé d'effectuer les calculs.

```{codeplay}
:file: class10.py
from turtle import *

def alu():
    a = 60
    left(a)
    forward(50)
    right(a)
    forward(150)
    right(180-a)
    forward(150)
    right(a)
    forward(200)
    right(a)
    forward(150)
    right(180-a)
    forward(150)
    right(a)
    forward(50)
    up()

def line(x, y):
    goto(x, y)
    seth(-90)
    down()
    goto(x, y-50)
    stamp()
    up()

alu()
line(-100, 100)
line(100, 100)
line(0, -90) 
```

Dans cette ALU (en anglais arithmetic–logic unit, ALU), nous allons simuler une addition de deux opérandes de 4 bits. En cliquant avec la souris sur un des opérandes d'entrée, la valeur est incrémentée de 1. Les valeurs peuvent aller de 0 à 15.

```{codeplay}
:file: class11.py
from turtle import *

def alu():
    a = 60
    left(a)
    forward(50)
    right(a)
    forward(150)
    right(180-a)
    forward(150)
    right(a)
    forward(200)
    right(a)
    forward(150)
    right(180-a)
    forward(150)
    right(a)
    forward(50)
    up()

def line(x, y):
    goto(x, y)
    seth(-90)
    down()
    goto(x, y-50)
    stamp()
    up()

class Bin4(): 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.n = 0
        self.draw()
        
    def draw(self):
        goto(self.x, self.y)
        dot(60, 'lightgray')
        goto(self.x, self.y-8)
        write(f'{self.n:04b}', font=('Courier', 16), align='center')
    
    def inside(self, x, y):
        return (-30 < x-self.x < 30) and (-30 < y-self.y < 30)
    
    def inc(self):
        self.n = (self.n + 1) % 16
        self.draw()
        
    def set(self, n):
        self.n = n % 16
        self.draw()
        
    def click(self, x, y):
        if self.inside(x, y):
            self.inc()
===
alu()
line(-100, 100)
line(100, 100)
line(0, -90) 
    
b0 = Bin4(-100, 120)
b1 = Bin4(100, 120)
b2 = Bin4(0, -170)

hideturtle()
speed(0)

def f(x, y):
    b0.click(x, y)    
    b1.click(x, y)
    b2.set(b0.n + b1.n)
            
getscreen().onclick(f)
getscreen().listen()
```
