# Logique - `and`

La logique analyse de façon rigoureux des propositions qui sont soit vrai soit faux.

- Les deux valeurs logiques sont `True` et `False`
- L'opération de négation `not` donne l'inverse
- L'opérateur `and` est le **et** logique
- L'opérateur `or` est le **ou** logique
- L'opérateur `xor` est le **ou exclusif** logique

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

p     |not p
------|-----
False |True
True  |False

```{codeplay}
print('p', 'not p', sep='\t| ')
print('--------' * 2)
for p in (False, True):
    print(p, not p, sep='\t| ')
```

`not False =` {bl}`False|>True`  
`not True  =`  {bl}`>False|True`  

## Et logique

La fonction `et` donne vrai si toutes les entrées sont vrai.

p     | q     | p and q
------|-------|--------
False | False | False
False | True  | False
True  | False | False
True  | True  | True

```{codeplay}
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

La fonction `or` donne vrai si au moins une des entrées est vrai.

p   | q   | p and q
----|-----|---------
0   | 0   | 0
0   | 1   | 1
1   | 0   | 1
1   | 1   | 1

```{codeplay}
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
print('p', 'q', 'p ^ q', sep='\t')
print('---------------------')
for p in (False, True):
    for q in (False, True):
        print(p, q, p ^ q, sep='\t')
```

## Dessiner une porte AND

```{codeplay}
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

## Une porte AND interactive

Dans la porte AND ci-dessous nous ajoutons 3 objets de la classe `Dot` et nous rendons la porte interactive. Avec la souris nous pouvons cliquer sur les 2 terminaux d'entrée et la sortie va afficher la logique de la porte.

```{codeplay}
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

## Dessiner une porte OR

```{codeplay}
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

## Une porte OR interactive

Dans la porte OR ci-dessous nous ajoutons 3 objets de la classe `Dot` et nous rendons la porte interactive. Avec la souris nous pouvons cliquer sur les 2 terminaux d'entrée et la sortie va afficher la logique de la porte.

La classe `Dot` est toujours définie, mais elle n'est plus affichée.

```{codeplay}
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

## Dessiner une porte XOR

```{codeplay}
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

## Une porte XOR interactive

Dans la porte XOR ci-dessous nous ajoutons 3 objets de la classe `Dot` et nous rendons la porte interactive. Avec la souris nous pouvons cliquer sur les 2 terminaux d'entrée et la sortie va afficher la logique de la porte.

```{codeplay}
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

## Dessiner une porte EQ

```{codeplay}
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

## Dessiner une porte NOT

```{codeplay}
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
