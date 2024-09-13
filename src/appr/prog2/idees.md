# Idées

Les programmes de ce chapitre sont des idées sous construction, à développer et à placer à leur endroit approprié.

## Méthodes `Screen`

Cet exemple de code affiche toutes les méthodes de la classe `Screen`. Nous constatons d'en avoir environs 26 méthodes.

```{codeplay}
from turtle import *

methodes = [x for x in dir(Screen) if not x.startswith('_')]
print(methodes)
print(len(methodes))
```

## État de la tortue

Voici quelques méthodes qui renvoient l'état actuel de la tortue.

```{codeplay}
from turtle import *

print('Tortue:')
print('shape =', shape())
print('down =', isdown())
print('visible =', isvisible())
print('fill =', fill())
print('speed =', speed())
print('delay =', delay())
```

## Fonction `shape()`

Voici les 6 formes de la tortue.

```{codeplay}
from turtle import *

shapes = getscreen().getshapes()
print('shapes =', shapes)

left(90)
up()
backward(180)

for s in shapes:
    forward(50)
    write(s + '   ', align='right', font=(None, 18))
    shape(s)
    stamp()
```

La taille des 3 formes géométriques `square`,  `triangle` et `circle` est de 20 pixels. Ces formes peuvent être utilisées dans des animations ou des jeux vidéos.

```{codeplay}
from turtle import *
up()

shape('square')
for i in range(10):
    stamp()
    forward(22)
    
goto(0, 30)
shape('circle')
for i in range(10):
    stamp()
    forward(22) 

goto(0, 60)
shape('triangle')
for i in range(10):
    stamp()
    forward(22)
    
hideturtle()
```

## Fonction `delay()`

La fonction `delay(d)` permet de contrôler l'intervalle (exprimé en millisecondes) entre deux mises à jour (update) de l'écran (canevas).

```{codeplay}
from turtle import *

print('delay =', delay()) # 33 milisecondes = 60 fps
delay(500)  # exprimé en millisecondes (ms)

left(50)    # delai de 500 ms tous les 5 degrees 
forward(50) # delai de 500 ms tous les 5 pixels
```

## Fonction `tracer()`

La fonction `tracer(0/1)` active ou désactive les animations des tortues.
Lorsque le traceur est désactivé, vous devez utiliser la fonction `update()` pour mettre à jour le dessin sur l'écran.

```{codeplay}
from turtle import *

def etoile(n, m):
    for i in range(n):
        forward(100)
        left(360/n*m)

backward(200)
print('tracer =', tracer())
etoile(7, 3)

forward(150)
tracer(0)
print('tracer =', tracer())
etoile(7, 3)
update()

forward(150)
etoile(9, 4)
update()
```

La fonction `tracer(n)` contrôle la fréquence des mises à jour du dessin. Seulement les n-ièmes mises à jour régulières de l'écran seront vraiment effectuées. Cette fonction peut être utilisée pour accélérer le dessin de graphiques complexes. Lorsqu'appelée sans arguments, elle renvoie la valeur actuelle de n.

```{codeplay}
from turtle import *
delay(200)

tracer(2)
print('tracer() =', tracer())
write('tracer(2)', align='right', font=(None, 16))
forward(200)

up()
goto(0, 50)
down()

tracer(5)
print('tracer() =', tracer())
write('tracer(5)', align='right', font=(None, 16))
forward(200)
```

## Fonction `speed()`

La vitesse de la tortue peut varier entre 1 et 1000.
Une vitesse de 0 représente la vitesse maximum. La vitesse par défaut est 3.

```{codeplay}
from turtle import *

print('speed =', speed())

for s in range(2, 10):
    reset()
    speed(s)
    write(f'speed({s})  ', font=(None, 18), align='right')
    for i in range(4):
        forward(100)
        left(90)
```

## Fonction `heading()`

Voici une visualisation de la direction de la tortue, angle exprimé par la fonction `heading()`

```{codeplay}
from turtle import *

for i in range(12):
    down()
    forward(100)
    stamp()
    up()
    forward(10)
    write(heading(), align='center')
    backward(110)
    left(30)

hideturtle()
```

## Animer un point

Animation en utilisant la fonction `tracer(0)` et `update()`.

```{codeplay}
from turtle import *
hideturtle()
tracer(0)
up()

for x in range(-300, 300, 10):
    clear()
    setx(x)
    dot(40, 'red')
    update()
```

## Le Zen de Python

Le Zen de Python est un ensemble de 19 principes qui influencent la conception du langage de programmation Python, et sont utiles pour comprendre et utiliser le langage.

Il est aussi inclus comme **Easter egg** dans Python, et apparait quand on tape la commande `import this`.

```{codeplay}
import this
```

## Mots-clés

Ce module contient la liste de tous des mots-clés de Python. Le nombre des mots-clés est relativement limité. Nous en avons seulement une trentaine. Ces mots-clés concernent :

- les opérateurs logiques : `and`, `or`, `not`
- les boucles : `for`, `in`, `while`, `break`, `continue`
- l'exécution conditionnelle : `if`, `elif`, `else`
- les fonctions : `def`, `return`, `lambda`
- l'importation : `import`, `from`
- les classes : `class`
- les variables : `global`

Les mots-clés que nous n’avons pas encore vus sont :  
`as`, `assert`, `del`, `except`, `exec`, `finally`, `is`, `pass`, `raise`, `try`, `with`, `yield`

```{codeplay}
import keyword
a = keyword.kwlist
print(a)
print(len(a)) 
```

## Expression rationnelle

Une expression rationnelle (regular expression ou RE) spécifie un ensemble de chaînes de caractères qui lui correspondent ; les fonctions de ce module vous permettent de vérifier si une chaîne particulière correspond à une expression rationnelle donnée (ou si une expression rationnelle donnée correspond à une chaîne particulière, ce qui revient à la même chose).

```{codeplay}
import re
print(dir(re))
```

## Chercher un élément

Ce programme crée une liste avec 100 entiers aléatoires.

```{codeplay}
from random import *
 
a = []
for i in range(100):
    x = randint(1, 999)
    a.append(x)

print(a)
a.sort()
print(a)
```

L'expression `x in liste` retourne une valeur booléenne qui indique si x fait partie de la liste.

```{codeplay}
a = [121, 939, 19, 143, 471, 273, 480, 852, 672, 321, 885, 628, 648, 374, 376, 555, 156, 239, 741, 348, 139, 665, 600, 801, 500, 320, 216, 396, 81, 965, 568, 45, 494, 723, 392, 704, 413, 879, 529, 468, 683, 479, 720, 959, 57, 207, 302, 931, 878, 681, 145, 462, 180, 318, 417, 337, 159, 800, 237, 898, 964, 907, 295, 669, 570, 474, 30, 111, 159, 777, 615, 516, 429, 973, 696, 209, 872, 147, 180, 142, 905, 415, 573, 512, 816, 814, 329, 598, 216, 131, 830, 134, 478, 313, 832, 470, 244, 480, 662, 855]

print(855 in a)
print(856 in a)
```

Ce programme vérifie si une valeur `x` se trouve dans la liste `a`.

```{codeplay}
a = [121, 939, 19, 143, 471, 273, 480, 852, 672, 321, 885, 628, 648, 374, 376, 555, 156, 239, 741, 348, 139, 665, 600, 801, 500, 320, 216, 396, 81, 965, 568, 45, 494, 723, 392, 704, 413, 879, 529, 468, 683, 479, 720, 959, 57, 207, 302, 931, 878, 681, 145, 462, 180, 318, 417, 337, 159, 800, 237, 898, 964, 907, 295, 669, 570, 474, 30, 111, 159, 777, 615, 516, 429, 973, 696, 209, 872, 147, 180, 142, 905, 415, 573, 512, 816, 814, 329, 598, 216, 131, 830, 134, 478, 313, 832, 470, 244, 480, 662, 855]
===
x = 855
print(x)
for val in a:
    if x == val:
        print(True)
        break

x = 856
print(x)
for val in a:
    if x == val:
        print('True')
        break
print(False)
from turtle import *
n = len(a)
speed(0)

x = -300
for y in a:
    goto(x, y/5)
    dot()
    x += 6
    
color('red')
a.sort()
x = -300
for y in a:
    goto(x, y/5)
    dot()
    x += 6         
```

## Trié ou pas ?

La fonction `is_sorted()` vérifie si une liste est triée.

```{codeplay}
a = [570, 562, 87, 609, 411, 833, 825, 852, 390, 892, 417, 55, 632, 496, 902, 893, 222, 796, 179, 766, 793, 354, 793, 186, 254, 72, 995, 45, 362, 762, 118, 650, 19, 429, 504, 763, 111, 474, 167, 754, 344, 299, 13, 404, 703, 684, 760, 621, 674, 327, 836, 930, 390, 821, 51, 990, 416, 297, 553, 183, 307, 221, 350, 841, 762, 728, 341, 548, 798, 432, 103, 759, 525, 972, 174, 844, 566, 199, 76, 164, 383, 929, 480, 49, 798, 23, 976, 991, 570, 833, 336, 117, 953, 345, 635, 798, 510, 69, 725, 171]
b = [13, 19, 23, 45, 49, 51, 55, 69, 72, 76, 87, 103, 111, 117, 118, 164, 167, 171, 174, 179, 183, 186, 199, 221, 222, 254, 297, 299, 307, 327, 336, 341, 344, 345, 350, 354, 362, 383, 390, 390, 404, 411, 416, 417, 429, 432, 474, 480, 496, 504, 510, 525, 548, 553, 562, 566, 570, 570, 609, 621, 632, 635, 650, 674, 684, 703, 725, 728, 754, 759, 760, 762, 762, 763, 766, 793, 793, 796, 798, 798, 798, 821, 825, 833, 833, 836, 841, 844, 852, 892, 893, 902, 929, 930, 953, 972, 976, 990, 991, 995]

def is_sorted(a):
    n = len(a)
    for i in range(1, n):
        if a[i-1] > a[i]:
            return False
    return True

print(is_sorted(a))
print(is_sorted(b))
```

## Recherche binaire

Voici comment faire une recherche binaire dans une liste triée.

```{codeplay}
liste = [13, 19, 23, 45, 49, 51, 55, 69, 72, 76, 87, 103, 111, 117, 118, 164, 167, 171, 174, 179, 183, 186, 199, 221, 222, 254, 297, 299, 307, 327, 336, 341, 344, 345, 350, 354, 362, 383, 390, 390, 404, 411, 416, 417, 429, 432, 474, 480, 496, 504, 510, 525, 548, 553, 562, 566, 570, 570, 609, 621, 632, 635, 650, 674, 684, 703, 725, 728, 754, 759, 760, 762, 762, 763, 766, 793, 793, 796, 798, 798, 798, 821, 825, 833, 833, 836, 841, 844, 852, 892, 893, 902, 929, 930, 953, 972, 976, 990, 991, 995]

a = 0
b = len(liste)
x = 995

while b - a > 0:
    m = (a + b) // 2
    print(a, m, b, liste[m])
    
    if x == liste[m]:
        break
    elif x < liste[m]:
        b = m
    else:
        a = m + 1
    
print(liste[m] == x)
```

## Ordre du tri

Quel est la somme de 1 + 2 + 3 + ... n ?  
Graphiquement ceci nous donne la surface d'un triangle.
Si nous affichons

- `x` sur la première ligne
- `xx` sur la deuxième ligne
- n fois `x` sur la dernière ligne

la réponse à la formule est la somme des x.
Nous pouvons ajouter un triangle identique (cette fois dessiné avec des traits (`-`)), ce qui nous donne un rectangle de taille `(n) * (n+1)`.
La taille du triangle est donc  `(n) * (n+1) / 2`.

```{codeplay}
n = 10
for i in range(n+1):
    print('x' * i + '-' * (n-i))

print(n * (n+1) // 2)
```

## Snow Crash

Le [Samouraï virtuel](https://fr.wikipedia.org/wiki/Le_Samouraï_virtuel) (titre anglais : Snow Crash) est un roman de Neal Stephenson, paru en 1992, se déroulant dans un univers futuriste parfois qualifié de cyberpunk ou, plus précisément, de postcyberpunk.

Snow crash est un virus transmis de façon visuelle et qui s'attaquerait directement au « système opératoire » du cerveau des programmeurs par affichage sur écran de symboles apparemment indéchiffrables (d'où le titre original Snow crash).

```{warning}
Ne cliquez pas sur **Exécuter** ! Ce code sert uniquement d'illustration ! Les risques pour votre cerveau seront imprévisibles.
```

```{codeplay}
from turtle import *
from random import *
up()
tracer(0)

d = 20
x0 = 300 - d//2
y0 = 200 - d//2

while True:
    for y in range(y0, -y0-d, -d):
        for x in range(-x0, x0+d, d):
            goto(x, y)
            r = random()
            dot(d, (r, r, r))
    update()
```

```{danger}
Ne cliquez pas sur **Exécuter** ! Ce code sert uniquement d'illustration ! Ce code illustre une version du **virus Snow crash** avec des pixels en couleurs.
```

```{codeplay}
from turtle import *
from random import *
up()
tracer(0)

d = 20
x0 = 300 - d//2
y0 = 200 - d//2

while True:
    for y in range(y0, -y0-d, -d):
        for x in range(-x0, x0+d, d):
            goto(x, y)
            r = random()
            g = random()
            b = random()
            dot(d, (r, g, b))
    update()
```

## Tortue par pixel

Est-ce que le programme est beaucoup ralenti si nous créons une nouvelle tortue pour chaque pixel ?

Effectivement avec 600 tortues, nous occupons beaucoup plus d'espace en mémoire, avec les paramètre propre à chaque tortue (`shape`, `color`, `width`, `speed`, etc.)

```{codeplay}
from turtle import *
from time import *
from random import *

tracer(0)
t0 = time()
d = 20
x0 = 300 - d//2
y0 = 200 - d//2
tortues = []

for y in range(y0, -y0-d, -d):
    for x in range(-x0, x0+d, d):
        t = Turtle()
        t.up()
        t.hideturtle()
        t.goto(x, y)
        r = random()
        t.dot(d, (r, r, r))
        tortues.append(t)

update()
print('time =', time() - t0)
print('objets =', len(tortues))
```

## Hypnose

```{codeplay}
from turtle import *
tracer(0)
width(10)
color('blue')

def star(n=7, a=400):
    for i in range(n):
        forward(a)
        backward(a)
        left(360/n)

while True:
    clear()
    star(13)
    left(1)
    update()
```

## Spiral

```{codeplay}
from turtle import *
tracer(0)
width(5)

a = 0
b = 0

def spiral(n=10):
    goto(0, 0)
    for i in range(200):
        forward(i)
        left(360/n)

while True:
    clear()
    seth(a)
    a += 1
    color('red')
    spiral()
    
    seth(b)
    b += -1
    color('blue')
    spiral(-10)
    update()
```

## Le coronavirus

Le nom « coronavirus » vient du latin et signifie « virus à couronne ». Son apparence sous un microscope électronique montre une frange de grandes projections bulbeuses qui évoquent une couronne solaire.

Dans la fonction `corona()` les paramètres sont :

- la distance entre projections `a`
- la longueur de la projection `d`
- le nombre de projections `n`

```{exercise}
Ajoutez 3 autres virus avec d'autres valeurs pour `a`, `d` et `n`.
```

```{codeplay}
:file: def10.py
from turtle import *
getscreen().bgcolor('azure')
up()

def corona(a=10, d=20, n=24):
    down()
    for i in range(n):
        left(90  - 180/n)
        forward(d)
        dot()
        backward(d)
        right(90 + 180/n)
        forward(a)
    up()

corona()
```

## Squid Game logo

Squid Game, ou Le Jeu du calmar, est une série télévisée dramatique de survie sud-coréenne de 9 épisodes, diffusée dans le monde entier en 2021 sur Netflix.
La série raconte l'histoire d'un groupe de personnes, fortement endettées, voire ruinées, qui risquent leur vie dans un jeu de survie mystérieux avec comme récompense une somme énorme.

Nous définissons une fonction `polygone(a, n)` pour dessiner le cercle, le triangle et le carré du logo.

```{exercise}
Ajoutez votre nom et vos coordonnées à la carte de visite en utilisant la fonction `write()`.
```

```{codeplay}
:file: def11.py
from turtle import *
getscreen().bgcolor('peru')
width(5)
up()

def polygone(a, n):
    down()
    for i in range(n):
        forward(a)
        left(360/n)
    up()
    
backward(150)
polygone(10, 36)
forward(100)
polygone(120, 3)
forward(170)
polygone(100, 4)
```

## Directives

```{tip}
This is a **tip**
```

```{warning}
This is a **warning**
```

```{note}
This is a **note**
```

```{attention}
This is **attention**
```

```{important}
This is **important**
```

```{exercise}
This is **exercise**.  
```

```{exercise}
This is an exercise.  
This is an exercise.  
```

```{exercise}
This is an exercise.  
This is an exercise.  
This is an exercise.  
```

```{admonition} Exercice
This is an exercice.  
```

```{admonition} Exercice
:class: tip
This is an exercice of class tip.  
```

```{admonition} Exercice
:class: note
This is an exercice of class note.  
```
