(prog1.parametrer)=

# Paramétrer - `rect(d, d2)`

Dans ce chapitre, nous revenons sur le concept de la fonction. Dans le chapitre 2 nous avons vu la fonction comme une façon de donner un nom à une séquence d'instructions. Ici nous allons voir comment nous pouvons ajouter un ou plusieurs paramètres à une fonction. Nous allons voir que :

- l'expression `def rect(d, d2):` permet de définir une fonction avec deux paramètres,
- les paramètres `d, d2` sont des variables locales valides uniqument à l'intérieur de la définition de fonction,
- ces paramètres prennent une valeur au moment de l'appel  de la fonction avec `rect(50, 30)`.

```{question}
En Python, `def` est un raccourci pour

{f}`défoncé`  
{f}`défilé`  
{v}`définition`  
{f}`défavorisé`
```

## Paramétrer une fonction

Jusqu'à maintenant, notre rectangle était d'une taille fixe. La fonction `rectangle()` du chapitre 2 dessine toujours un rectangle de 160 x 100 pixels. Il faudrait faire une nouvelle fonction `rectangle2()` si on voudrait dessiner une taille différente.

Il serait très utile de disposer d'une fonction de la forme `rectangle(d, d2)` qui puisse dessiner des rectangles de largeur et hauteur variable.
C'est possible en spécifiant des **paramètres** pour la fonction.
Un paramètre de fonction est une variable locale qui peut être utilisée dans sa définition.

Lors de l'appel de la fonction, nous donnons des valeurs à la fonction.
Ces valeurs sont les **arguments** de la fonction.

```{codeplay}
from turtle import *

def rectangle(d, d2):    # paramètres (d, d2)
    for i in range(2):
        forward(d/2)
        write(d)
        forward(d/2)
        left(90)

        forward(d2/2)
        write(d2)
        forward(d2/2)
        left(90)
        
rectangle(160, 100)      # largeur=160, hauteur=100 
rectangle(200, 140)      # largeur=200, hauteur=140 
```

La fonction `losange(a, angle)` a comme paramètre la longueur et le premier angle. Le deuxième anlge du losange est calculé.

```{codeplay}
from turtle import *

def losange(d, a):      # paramètres (d=distance, a=angle)
    for i in range(2):
        forward(d)
        left(a)
        write(a)
        
        forward(d)
        left(180-a)
        write(180-a)

losange(100, 60)            # distance=100, angle=60
losange(140, 100)           # distance=140, angle=100
```

La fonction `polygone(d, n)` a comme paramètre la distance du côté et le nombre de sommets.

```{codeplay}
from turtle import *

def polygone(d, n):     # paramètres (d, n)
    for i in range(n):
        forward(d)
        left(360/n)
        write(360/n)

polygone(100, 3)    # triangle
polygone(100, 4)    # carré    
polygone(100, 5)    # pentagon
```

## Dessiner une maison

Nous revenons à notre fonction pour dessiner une maison.

```{codeplay}
from turtle import *

def maison(d):
    forward (1.41*d)  # sol
    left(90)
    forward(d)  # mur droit
    left(45)
    forward(d)  # toit droit
    left(90)
    forward(d)  # toit gauche
    left(45)
    forward(d)  # mur gauche
    left(90)

backward(200)        
maison(50)      # maison de taille 50
forward(100)
maison(70)      # maison de taille 70
```

## Couleur de la maison

Maintenant nous modifions la fonction pour inclure non seulement la position, la taille, mais également la couleur de la maison comme paramètres.

```{codeplay}
from turtle import *
getscreen().bgcolor('lightgreen')
up()

def maison(d, c):
    down()
    fillcolor(c)
    begin_fill()
    forward (1.41*d)  # sol
    left(90)
    forward(d)  # mur droit
    left(45)
    forward(d)  # toit droit
    left(90)
    forward(d)  # toit gauche
    left(45)
    forward(d)  # mur gauche
    left(90)
    end_fill()
    up()

maison(70, 'lightblue')
forward(150)
maison(50, 'yellow')
```

## Arbre

Pour dessiner un arbre simple, nous utilisons un segment droit pour le tronc et un disque (dot) pour le feuillage.
C'est une fonction qui a 3 paramètres

- `d` -- longueur du tronc
- `c` -- couleur du tronc
- `c2` -- couleur du feuillage

```{codeplay}
from turtle import *

def arbre(d, c, c2):
    down()
    left(90)
    width(d/6)      # tronc
    pencolor(c)
    forward(d)
    dot(d, c2)      # feuillage
    up()
    backward(d)     # retourner à la position de départ
    right(90)
    
    
arbre(100, 'brown', 'lime')
forward(70)
arbre(90, 'brown', 'green')
```

## Bus

Pour dessiner un bus, une voiture ou un camion simple, nous pouvons utiliser des rectangles pour le chassis, et un disque (dot) pour les rous.
C'est une fonction qui a a paramètres

- `d` -- longueur du bus
- `c` -- couleur du bus

```{codeplay}
from turtle import *

def rectangle(d, d2):
    for i in range(2):
        forward(d)
        left(90)
        forward(d2)
        left(90)
        
def bus(d, c):
    down()
    fillcolor(c)        # chassis
    begin_fill()
    rectangle(d, d/3)
    end_fill()
    forward(d/4)
    dot(d/5)            # roue arrière
    dot(d/10, 'white')
    forward(d/2)
    dot(d/5)            # roue avant
    dot(d/10, 'white')
    up()
    
backward(200)
bus(200, 'red')
forward(100)
bus(150, 'lightblue')
```

## Coeur

```{codeplay}
from turtle import *

def coeur(r, c):
    fillcolor(c)
    begin_fill()
    left(90)
    circle(r, 225)
    forward(2.4*r)
    left(90)
    forward(2.4*r)
    circle(r, 225)
    left(90)
    end_fill()

coeur(50, 'red')
coeur(30, 'pink')
```

## Escalier

- `d` -- longueur de marche
- `d2` -- hauteur de marche
- `n` -- nombre de marches

```{codeplay}
from turtle import *

def escalier(d, d2, n):
    for i in range(n):
        forward(d)
        left(90)
        forward(d2)
        right(90)

escalier(20, 10, 5)
escalier(10, -20, 5)
escalier(30, 10, 4)
```

## Maison avec porte

Maintenant nous modifions la fonction pour inclure non seulement la position, la taille, la couleur de la maison comme paramètres, mais nous y ajoutons aussi une porte.

```{codeplay}
:file: def8.py
from turtle import *
getscreen().bgcolor('lightgreen')
up()

def porte(d):
    for x in (1, 1.6, 1, 1.6):
        forward(d * x)
        left(90)

def mur(d):
    forward (1.4 * d)
    for a in (90, 45, 90, 45):
        left(a)
        forward(d)
    left(90)

def maison(p, d, col1, col2):
    goto(p)
    down()
    fillcolor(col1)
    begin_fill()
    mur(d)
    end_fill()

    forward(d/3)
    fillcolor(col2)
    begin_fill()
    porte(d/3)
    end_fill()
    up()

maison((-20, -80), 70, 'lightblue', 'red')
maison((-200, 20), 50, 'yellow', 'blue')
maison((120, 40), 40, 'pink', 'violet')
```

## Valeurs par défaut

Nous pouvons spécifier des valeurs par défaut. Pour ceci nous ajoutons la valeur par défaut dans la liste de paramètres.

    def maison(p, d=50, col1='yellow', col2='blue'):

Il a maintenant différentes façons à appeler la fonction. Tous les paramètres qui ont une valeur par défaut sont optionnels. Au minimum nous devons spécifier les paramètres sans valeur par défaut.

    maison((-20, -80))

```{codeplay}
:file: def9.py
from turtle import *
getscreen().bgcolor('lightgreen')
up()

def porte(d):
    for x in (1, 1.6, 1, 1.6):
        forward(d * x)
        left(90)

def mur(d):
    forward (1.4 * d)
    for a in (90, 45, 90, 45):
        left(a)
        forward(d)
    left(90)

def maison(p, d=50, col1='yellow', col2='blue'):
    goto(p)
    down()
    fillcolor(col1)
    begin_fill()
    mur(d)
    end_fill()

    forward(d/3)
    fillcolor(col2)
    begin_fill()
    porte(d/3)
    end_fill()
    up()

maison((-20, -80))
maison((-200, 20), col1='lime')
maison((120, 40), col2='red')
maison((-170, -140), d=80)
```

## Rectangle

La fonction `rectangle(a, b, w=1, pen='black', fill=None)` dessine un rectangle a x b.
Elle possède les 3 paramètres optionnels (valeur par défaut en parenthèse):

- `w` -- épaisseur de ligne (`1`)
- `pen` -- couleur de ligne (`'black'`)
- `fill` -- couleur de remplissage (`'white'`)

Le rectangle est dessiné dans la direction actuelle de la tortue. Cette orientation peut être changée avec `seth()`. La tortue se positionne de l'autre côté du point de départ. Ceci permet d'enchainer à dessiner des rectangles.

```{codeplay}
from turtle import *

def rectangle(a, b, w=1, pen='black', fill='white'):
    down()
    width(w)
    pencolor(pen)
    fillcolor(fill)
    begin_fill()
    for x in (a, b, a, b):
        forward(x)
        left(90)
    end_fill()
    up()
    forward(a)

rectangle(40, 30, 3, 'blue', 'lime')
forward(10)
rectangle(40, 30, 1, 'orange', 'orange')
forward(10)
rectangle(30, 80, fill='yellow')
seth(45)
rectangle(40, 30, 5, 'magenta')
seth(0)
rectangle(80, 40, 1, 'red', 'pink')
```



## Polygone

La fonction `polygone()` dessine un polygone régulier avec n sommets. Les arguments de la fonction sont :

- `d` -- distance du segment
- `n` -- nombre de segments

```{codeplay}
from turtle import *

def polygon(d, n, w=1, pen='black', fill='white'):
    down()
    pencolor(pen)
    width(w)
    fillcolor(fill)
    begin_fill()
    for i in range(n):
        forward(d)
        left(360/n)
    end_fill()
    up()  

up()
backward(280)
for n in range(3, 9):
    polygon(40, n, fill='lime')
    color('black')
    write(n)
    forward(100)
```


## Etoile

En ajoutant un paramètre supplémentaire `m`, la fonction `polygone()` permet également de dessiner un polygone étoilé.  Ce paramètre signifie le nombre de pics sauté pour aller au prochain des `n` points répartis dans un cercle. Pour `m=1` un polygone régulier est dessinée.

es arguments de la fonction sont :

- `d` -- distance du segment
- `n` -- nombre de segments
- `m` -- paramètre pour polygone étoilé (nombre de pics sautés)

```{codeplay}
from turtle import *

def polygon(d, n, m=1, w=1, pen='black', fill='white'):
    down()
    pencolor(pen)
    width(w)
    fillcolor(fill)
    begin_fill()
    for i in range(n):
        forward(d)
        left(m*360/n)
    end_fill()
    up()  
    
up()
backward(250)
for m in range(2, 6):
    polygon(80, 11, m, fill='yellow')
    color('black')
    write(m)
    forward(60)
```

## Nommer une variable

Pour nommer une variable, vous pouvez utiliser :

- lettres (`a...z` et `A...Z`),
- chiffres (`0...9`),
- le tiret bas (`_`).

Le nom de variable :

- est sensible aux majuscules/minuscules,
- ne peut pas commencer avec un chiffre,
- ne doit pas consister d'un mot-clé (`if`, `else`, `for`),

Ces noms de variables sont donc valides : `a2`, `_a`, `speed`, `pos_x`, `POS_X`

```{question}
Lesquels des noms de variable sont valides ?

{f}`var 2`  
{v}`var2`  
{f}`2var`  
{v}`IF`
===
`var 2` contient une espace  
`2var` commence par un chiffre  
`IF` n'est pas un mot-clé  
```

## Exercices

### Pingpong

La fonction `pingpong()` reprend le dessin du chapitre 1 et ajoute trois paramètres

```{codeplay}
:file: pingpong.py
from turtle import *

def pingpong(d, c, c2):
    down()
    left(90)
    color(c)        # poignée
    width(d/8)
    forward(d/2)
    color(c2)       # plaque
    width(d/2)
    forward(d/10)
    up()            # retourner au point de départ
    backward(6/10*d)
    right(90)

pingpong(200, 'brown', 'red')
forward(100)
pingpong(150, 'brown', 'blue')
```

### Stickman

```{codeplay}
from turtle import *
up()


def leg(angle, a):
    left(angle)
    forward(a)
    backward(a)
    right(angle)

def stickman(a, bras=(30, -45), jambes=(10, -30)):
    seth(0)
    down()
    circle(a/2)       # tête
    right(90)
    forward(a/2)    # cou
    
    leg(bras[0], a)
    leg(bras[1], a)
    forward(a)
    
    leg(jambes[0], a)
    leg(jambes[1], a)
    up()

goto(-200, 0)      
stickman(20)

goto(-100, 0)      
stickman(20, (90, -110))

goto(0, 0)      
stickman(30, (90, -110), (110, -24))
hideturtle()
```
