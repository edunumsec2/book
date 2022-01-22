# Interrompre - `ontimer`

Dans ce chapitre nous allons voir comment un programme peut planifier d'appeler une fonction dans le future. Cette fonctionnalité est importante pour programmer des simulations, des animations, des jeux-vidéos, des horloges etc. Nous allons voir que :

- la fonction `ontimer(f, t)` installe une fonction qui va être appelée après `t` millisecondes,
- après `t` millisecondes le programme actuel est interrompue pour exécuter la fonction `f()`,
- le module `time` met a disposition des fonctions de date et temps.

```{question}
La méthode `ontimer()` installe une fonction de rappel qui

{f}`compte le temps`  
{f}`affiche le temps`  
{v}`s'exécute dans le futur`  
{f}`affiche le retard`
```

## Fonction `ontimer`

La fonction  `ontimer(f, t)` permet d'appeler une fonction dans le futur, après `t` millisecondes. Nous l'utilisons dans l'exemple suivant pour afficher pendant 60 secondes un point qui fait le tour du cadran d'une horloge.

```{codeplay}
from turtle import *

up()
goto(0, 150)
hideturtle()
n = 0

def f():
    global n
    dot(10)
    forward(15)
    right(6)
    n += 1
    if n < 60:
        getscreen().ontimer(f, 1000)
        
f()
```

## Le module `time`

Le module `time` comporte 17 méthodes et attributs.

```{codeplay}
import time

a = [x for x in dir(time) if not x.startswith('_')]
print(a)
print(len(a))
```

## Méthodes

L'**epoch** est le point de départ du temps et dépend de la plateforme. Pour Unix l'epoch est le 1. janvier 1970.

- `clock()` renvoie le nombre de secondes depuis la première exécution
- `time()` renvoie le nombre de secondes depuis l'époque (1970)


```{codeplay}
from time import *

print('altzone =', altzone)
print('timezone =', timezone)

print('asctime =', asctime())
print('gmtime =', gmtime())

print('time =', time())
print('clock =', clock())
```

## Date et temps

La fonction `asctime()` retourne une chaine avec date et temps. Nous pouvons la découper avec l'opérateur de tranche.

```{codeplay}
from time import *

print('asctime =', asctime())
date = asctime()[:11]
temps = asctime()[11:20]
print('date =', date)
print('temps =', temps)
```

Une tortue peut écrire temps et date en grandes lettre sur le canevas.

```{codeplay}
from turtle import *
from time import *
up()
speed(0)
hideturtle()

date = asctime()[:11]
temps = asctime()[11:20]

write(temps, font=(None, 100), align='center')
goto(0, -100)
write(date, font=(None, 40), align='center')
```

## Horloge automatique

La fonction `horloge()` affiche le temps et la date.
Comme dernière instructions nous installons une fonction de rappel, cette même fonction, qui sera appelé de nouveau dans 1000 ms.

```{codeplay}
from turtle import *
from time import *
hideturtle()

def horloge():
    temps = asctime()[11:20]
    clear()
    write(temps, font=(None, 80), align='center')
    getscreen().ontimer(horloge, 1000)

horloge()
```

## Chronométrer

Pour avoir une idée du temps d'exécutions d'une itération, nous mesurons le temps pour `n` itérations et nous calculons la durée d'une itération en micro-secondes (um).

```{codeplay}
from time import *

t0 = time()
n = int(1e4)
a = 1.0

def chrono(msg):
    global t0
    t1 = time()
    dt = (t1-t0) * 1e6/n
    print(msg, round(dt, 1) , 'us')
    t0 = t1

for i in range(n):
    pass
chrono('boucle vide')

for i in range(n):
    a += i
chrono('addition')

for i in range(n):
    a *= i
chrono('multiplication')
```

## Vitesse d'affichage

Nous allons mesurer le temps nécessaire pour écrire 600 pixels sur tout l'écran.

```{codeplay}
from turtle import *
from time import *
from random import *
up()
speed(0)
tracer(0)

x0, y0, d = 300, 200, 20
t0 = time()
for y in range(y0, -y0-1, -d):
    for x in range(-x0, x0+1, d):
        goto(x+d/2, y-d/2)
        r = random()
        dot(d, (r, r, r))
update()
print(time()-t0)
```

**Exercice** : Diminuez le diamètre `d` des pixels à 5.
