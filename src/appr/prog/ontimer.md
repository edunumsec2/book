# Interrompre - `ontimer()`

Dans ce chapitre nous allons voir comment un programme peut planifier d'appeler une fonction dans le futur. Cette fonctionnalité est importante pour programmer des simulations, des animations, des jeux vidéos, des horloges, etc. Nous allons voir que :

- la fonction `ontimer(f, t)` installe une fonction qui va être appelée après `t` ms,
- après `t` ms le programme actuel s'interrompt pour exécuter la fonction `f()`,
- le module `time` met à disposition des fonctions de date et de temps.

```{question}
La méthode `ontimer()` installe une fonction de rappel qui

{f}`compte le temps`  
{f}`affiche le temps`  
{v}`s'exécute dans le futur`  
{f}`affiche le retard`
```

## Fonction de rappel

En informatique, une fonction de rappel (**callback** en anglais) ou fonction de post-traitement est une fonction qui est passée en argument à une autre fonction. Cette dernière peut alors faire usage de cette fonction de rappel comme de n'importe quelle autre fonction, alors qu'elle ne la connaît pas par avance.

## Fonction `ontimer`

La fonction  `ontimer(f, t)` permet d'appeler une fonction dans le futur, après `t` millisecondes. Nous l'utilisons dans l'exemple suivant pour afficher pendant 60 secondes un point qui fait le tour du cadran d'une horloge.

```{codeplay}
:file: ontimer1.py
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
:file: ontimer2.py
import time

a = [x for x in dir(time) if not x.startswith('_')]
print(a)
print(len(a))
```

## Méthodes

L'**epoch** est le point de départ du temps et dépend de la plateforme. Pour Unix l'epoch est le 1. janvier 1970.

- `timezone()` renvoie le décalage horaire (exprimé en secondes)
- `time()` renvoie le nombre de secondes depuis l'époque (1970),
- `asctime()` renvoie le temps et la date sous forme de chaîne de texte.

```{codeplay}
:file: ontimer3.py
from time import *

print('timezone =', timezone)
print('time =', time())
print('asctime =', asctime())
```

## Structure temps

La fonction `gmtime()` renvoie une séquence de valeurs temporelles. Ses valeurs sont accessibles par index et par nom d’attribut. Voici les index, les attributs et leur signification :

- 0 - `tm_year` - année
- 1 - `tm_mon` - mois
- 2 - `tm_day` - jour
- 3 - `tm_hour` - heur
- 4 - `tm_min` - minute
- 5 - `tm_sec` - seconde
- 6 - `tm_wday` - jour de la semaine
- 7 - `tm_yday` - jour de l'année

```{codeplay}
:file: ontimer4.py
from time import *

print('gmtime =', gmtime())
print()
for t in gmtime():
    print(t)
```

## Date et temps

La fonction `asctime()` retourne une chaine avec date et temps. Nous pouvons la découper avec l'opérateur de tranche.

```{codeplay}
:file: ontimer5.py
from time import *

print('asctime =', asctime())
date = asctime()[:11]
temps = asctime()[11:20]
print('date =', date)
print('temps =', temps)
```

Une tortue peut écrire temps et date en grandes lettre sur le canevas.

```{codeplay}
:file: ontimer6.py
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
Comme dernière instruction nous installons une fonction de rappel, cette même fonction, qui sera appelée de nouveau dans 1000 ms.

```{codeplay}
:file: ontimer7.py
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

Pour avoir une idée du temps d'exécutions d'une itération, nous mesurons le temps pour `n` itérations et nous calculons la durée d'une itération en microsecondes (um).

```{codeplay}
:file: ontimer8.py
from time import *

t0 = time()
n = int(1e5)
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

```{caution}
Sur ce site votre code Python est traduit en JavaScript et exécuté par [Skulpt](https://skulpt.org) directement dans votre navigateur.
Une instruction de base prend environ 10 µs. 

Si vous téléchargez le fichier et exécutez votre code directement en Python avec un éditeur externe comme Thonny, les instructions de base exécutent 100 fois plus vite (environ 0.1 µs). Par contre pour ce qui concerne l'affichage, les vitesses sont très comparables, ce que vous pouvez constater dans l'exemple suivant.
```

## Vitesse d'affichage

Nous allons mesurer le temps nécessaire pour écrire 600 pixels sur tout l'écran.

```{exercise}
Diminuez le diamètre `d` des pixels à 5.
```

```{codeplay}
:file: ontimer9.py
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

## Horloge

```{codeplay}
from turtle import *
from time import *
from math import *
r = 150

def cadran():
    up()
    home()
    dot(2.3 * r, 'silver')
    for i in range(12):
        x = r * sin(2 * pi * i / 12)
        y = r * cos(2 * pi * i / 12)
        goto(x, y)
        dot()

def aiguille(d, r, angle):
    home()
    down()
    width(d)
    x = r * sin(2 * pi * angle)
    y = r * cos(2 * pi * angle)
    goto(x, y)

def horloge():
    clear()
    cadran()
    h, m, s = localtime()[3:6]
    aiguille(5, 0.6 * r, h/12)
    aiguille(3, 0.8 * r, m/60)
    aiguille(1, 0.9 * r, s/60)
    hideturtle()
    tracer(0)
    update()
    Screen().ontimer(horloge, 1000)
    
horloge()
done()
```

## Exercice

### Tetris

Les flèches gauche/droite permettent de déplacer le tétronimo. Programmez les touches :

- haut/bas pour le tourner,
- espace pour le faire tomber.

```{codeplay}
:file: tetris.py
from turtle import *
hideturtle()
tracer(0)
up()
d = 20
sety(200 - d)

def L():
    fillcolor('orange')
    begin_fill()
    for a in 0, 90, 90, -90, 0, 90, 90, 0, 0, 90:
        forward(d)
        left(a)
    end_fill()
    
L()
update()

def gauche():
    clear()
    backward(d)
    L()
    update()
    
def droite():
    clear()
    forward(d)
    L()
    update()

def fall():
    clear()
    sety(ycor() - d)
    L()
    update()
    if ycor() <= -200:
        sety(200 - d)
        s.ontimer(fall, 2000)
    else:
        s.ontimer(fall, 500)

s = getscreen()
s.onkey(gauche, 'Left')
s.onkey(droite, 'Right')
s.onkey(clear, 'c')
s.listen()
fall()
```
