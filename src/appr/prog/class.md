# Créer - `class`

La programmation orientée objet met au centre de la programmation la notion d'objet. Des objets individuels sont créés à partir d'un modèle qu'on appelle classe.

Un objet est caractérisé par ses **attributs** (variables) et **méthodes** (fonctions). La programmation orientée objet attache les attributs et méthodes à l'objet même et permet de cette façon un code très structuré et facilement extensible.  Nous allons voir que :

- le mot-clé `class` permet de définir un modèle pour créer des objets,
- l'expression `point = Point()` crée un nouvel objet à partir d'une classe,
- un objet possède des  **attributs** et des **méthodes**.

```{question}
En programmation orientée objet une classe est

{f}`un objet`  
{v}`un modèle pour faire des objets`  
{f}`quelque chose de très chic`  
{f}`une classification`
```

## Définir une classe

Le mot-clé `class` permet de définir une classe, ici la classe `Point`.
C'est une convention en Python, que le nom de classe soit écrit avec une majuscule. Pour définir une classe, nous écrivons :

1. le mot-clé `class`
1. le nom de la class (avec une majuscule)
1. des parenthèses optionnelles (classe parent)
1. un deux-points `:`
1. un bloc en indentation

```{exercise}
Créez une deuxième classe `Rectangle` et affichez son type.
```

```{codeplay}
class Point:
    "Définition d'un point géométrique"

print(Point)
print(Point.__name__)
```

## Créer des objets

À partir d'une class, nous pouvons créer autant d'objets que nous voulons. L'expression `Point()` crée un objet de type `Point`. On dit aussi qu'on crée une **instance** de la classe `Point`.

Pour créer une instance, on utilise le nom de la classe suivi de parenthèses. Plus tard nous verrons qu'il peut y avoir des arguments entre ces parenthèses.

Une classe est comme un moule qui nous permet de créer des copies, à partir d'une définition de classe.

```{exercise}
Créez encore d'autres instances de la classe `Point`.
```

```{codeplay}
:file: class1.py
class Point():
    "Définition d'un point géométrique"

p = Point()
q = Point()

print(p, q)
```

## Définir des attributs

La notation dotée permet de définir des attributs à un objet.
Par exemple le point peut avoir un attribut `x` et `y`.
Il pourrait avoir une couleur, une épaisseur, etc.

La fonction `dir()` affiche les attributs d'un objet.

```{codeplay}
:file: class2.py
class Point():
    pass

p = Point()
p.x = 20
p.y = 30

print(p.x)
print(p.y)
print(dir(p))
```

## La méthode `__init__()`

Chaque classe possède une méthode spéciale `__init__()` que nous appelons **constructeur**. Cette méthode est appelée lors de la création de l'objet. Son premier paramètre est toujours `self`, qui représente l'objet lui-même. Cette fonction est utilisée pour initialiser les attributs avec les valeurs initiales.

```{codeplay}
:file: class3.py
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p = Point(20, 30)

print(p.x, p.y)
print(p)
```

## La méthode `__str__()`

Toutes les classes possèdent aussi une méthode spéciale `__str__()` qui retourne une chaîne de caractères. Cette chaîne est un descripteur de l'objet. Il est utilisé quand on affiche l'objet avec la fonction `print()`.

Souvent la représentation d'un objet sous forme de texte ressemble à son constructeur, et affiche le nom de la classe et quelques attributs essentiels.

```{codeplay}
:file: class4.py
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

p = Point()
q = Point(20, 30)
print(p)
print(q)
```

## Définir une méthode

Dans la définition de classe, nous pouvons définir des méthodes supplémentaires. Le premier paramètre de toute méthode est `self`, la variable qui représente l'objet lui-même.

```{codeplay}
:file: class5.py
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def norme(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

p = Point(20, 30)

print('p.norme() =', p.norme())
print('p =', p)
```

## Classe `Dot`

Essayons maintenant de créer une classe pour un objet graphique. Définissons la classe `Dot` avec les attributs:

- position
- diamètre
- couleur

et les méthodes

- `__init__()` du constructeur
- `__str__()` du descripteur
- `draw()` pour dessiner l'objet

```{codeplay}
:file: class6.py
from turtle import *
hideturtle()
speed(0)
up()

class Dot():
    def __init__(self, pos=(0, 0), d=40, color='red'):
        self.pos = pos
        self.d = d
        self.color = color
        self.draw()
        
    def draw(self):
        color(self.color)
        goto(self.pos)
        dot(self.d)
        color('black')
        write(self.__str__())
       
    def __str__(self):
        return f'Dot({self.pos}, {self.d}, {self.color})'
        
d0 = Dot()
d1 = Dot((-100, 100))
d2 = Dot((-200, -100), 60, 'lime')
d3 = Dot((100, 100), 100, 'yellow')
```

## Objet cliquable

Nous ajoutons maintenant une fonction de rappel pour basculer la couleur du disque entre rouge et vert quand on y clique avec la souris.

```{codeplay}
:file: class7.py
from turtle import *
hideturtle()
speed(0)
up()

class Dot(): 
    def __init__(self, pos, d=100):
        self.pos = pos
        self.d = d
        self.state = False
        self.color = 'red'
        self.draw()
        
    def draw(self):
        color(self.color)
        goto(self.pos)
        dot(self.d)

    def inside(self, x, y):
        dx = self.pos[0] - x
        dy = self.pos[1] - y
        r = self.d / 2 
        return dx*dx + dy*dy < r*r
    
    def toggle(self):
        self.color = 'lime' if self.color == 'red' else 'red'
        self.draw()
        
d0 = Dot((-100, 0))
d1 = Dot((100, 0))

def f(x, y):
    for d in (d0, d1):
        if d.inside(x, y):
            d.toggle()
          
getscreen().onclick(f)
getscreen().listen()
```

## Dot cliquable

Dans l'exemple suivant nous avons deux points `p0` et `p1` qui

- basculent d'état quand on y clique.
- montrent leur état 0 ou 1,
- changent de couleur entre gris et jaune.

Le troisième point `p2` tient son état à partir de la relation logique
`p0 and p1`.

```{codeplay}
:file: class8.py
from turtle import *
hideturtle()
speed(0)
up()

class Dot(): 
    def __init__(self, pos):
        self.pos = pos
        self.state = False
        self.draw()

    def draw(self):
        goto(self.pos)
        dot(40, 'yellow' if self.state else 'lightgray')
        sety(self.pos[1] - 10)
        write(int(self.state), font=(None, 18), align='center')

    def inside(self, x, y):
        return (x - self.pos[0]) ** 2 + (y - self.pos[1]) ** 2 < (20 ** 2)

    def set(self, state):
        self.state = state
        self.draw()

    def toggle(self):
        self.set(not self.state)    

d0 = Dot((-100, 100))
d1 = Dot((-100, -100))
d2 = Dot((100, 0))

def f(x, y):
    for d in (d0, d1):
        if d.inside(x, y):
            d.toggle()   
    d2.set(d0.state and d1.state)

getscreen().onclick(f)
getscreen().listen()
```

## Classe Rectangle

Par la suite nous allons voir comment nous pouvons transformer une programmation procédurale en programmation orientée objet. Prenons le cas d'un rectangle.

Dessinons un rectangle de taille (a, b) à la position (x, y).

```{codeplay}
from turtle import *
up()

def rectangle(x, y, a, b):
    goto(x, y)
    down()
    for x in (a, b, a, b):
        forward(x)
        left(90)
    up()

rectangle(-20, 100, 150, 50)
rectangle(0, 0, 100, 50)
rectangle(20, -100, 100, 50)
```

Maintenant implémentons une class `Rectangle`. Nous allons ajouter plusieurs options :

- angle d'inclinaison
- couleur du trait
- épaisseur du trait
- couleur de remplissage

Nous utilisons `None` si il n'y a pas de remplissage ou pas de trait.

```{codeplay}
from turtle import *
up()

class Rectangle:

    def __init__(self, pos, size, angle=0, pen=1, color=('black', 'white')):
        self.pos = pos
        self.size = size
        self.angle = angle
        self.pen = pen
        self.color = color
        self.draw()

    def draw(self):
        color(*self.color)
        width(self.pen)
        goto(self.pos)
        setheading(self.angle)

        if self.color[0] == None:
            self.draw_box()
        else:
            begin_fill()
            self.draw_box()
            end_fill()

    def draw_box(self):
        down()
        for x in (self.size) * 2:
            forward(x)
            left(90)
        up()

p = (-50, 20)
size = (100, 50)
Rectangle(p, size)
Rectangle(p, size, angle=45)
Rectangle((-150, 30), (150, 70), -30, 5, ('red', 'yellow'))
```

## Classe Ellipse

Commençons de nouveau avec une fonction procédurale pour dessiner une ellipse.

```{codeplay}
from turtle import *
from math import *

speed(0)
up()

def ellipse(x0, y0, a, b):
    for i in range(37):
        x = x0 + a/2 * sin(pi * i / 18)
        y = y0 + b/2 * cos(pi * i / 18)
        goto(x, y)
        down()
    up()

ellipse(-20, 100, 150, 50)
ellipse(0, 0, 100, 250)
ellipse(20, -100, 100, 50)
```

Et maintenant la même chose en programmation orientée objet.

```{codeplay}
from turtle import *
from math import *
speed(0)
up()

class Ellipse:

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.draw()

    def draw(self):
        for i in range(37):
            x = self.pos[0] + self.size[0]/2 * sin(pi * i / 18)
            y = self.pos[1] + self.size[1]/2 * cos(pi * i / 18)
            goto(x, y)
            down()
        up()

p = (100, 0)
Ellipse(p, (100, 50))
Ellipse(p, (50, 100))
Ellipse((-100, 30), (150, 270))
```

## Classe Card

Les cartes de jeux sont représentées avec un rectangle arrondi et un des 4 symboles (cœur, pique, carreau, trèfle).

```{codeplay}
:file: class12.py
from turtle import *
up()

class Card:
    couleur = '♥♦'

    def __init__(self, pos=(0, 0), size=(50, 80), r=10, fill='white'):
        self.pos = pos
        self.size = size
        self.r = r
        self.fill = fill
        self.show()

    def outline(self):
        down()
        for d in self.size * 2:
            forward(d)
            circle(self.r, 90)
        up()

    def show(self):
        goto(self.pos)
        fillcolor(self.fill)
        begin_fill()
        self.outline()
        end_fill()
        color('red')
        sety(self.pos[1]+5)
        write('♥', font=(None, 30))

Card()
Card((50, 20), fill='pink')
Card((100, -120), fill='azure')
```

## Exercices

Les exercices ci-dessous utilisent la classe `Button`. C'est une classe extrêmement important pour une interface graphique. Toute interface graphique, et encore plus les smartphones et tablettes utilisent des boutons pour interagir avec l'utilisateur.

### Jeu avec boutons

Retournez au jeux de Go dans les exercices du chapitre **Cliquer** intégrez des boutons pour 

- recommencer une nouvelle partie
- quitter le jeu

```{codeplay}
from turtle import *
s = getscreen()
hideturtle()
speed(0)
up()

x0, y0, d = 160, 160, 40

class Button:
    def __init__(self, pos, text, size=(80, 30), color='lightgray'):
        self.pos = pos
        self.size = size
        self.text = text
        self.color = color
        self.draw()
        
    def draw(self):
        goto(self.pos)
        fillcolor(self.color)
        begin_fill()
        down()
        for x in self.size * 2:     # parcourir 2 fois longeur et hauteur
            forward(x)
            left(90)
        up()
        end_fill()
        x, y = self.pos
        w, h = self.size
        goto(x+w/2, y+h/4)
        color('black')
        write(self.text, font=('Arial', h//2), align='center')
        
    def __str__(self):
        return f'Button({self.pos}, {self.text})'
    
    def inside(self, p):
        x, y = self.pos
        w, h = self.size
        
        return 0 < p[0]-x < w and 0 < p[1]-y < h    

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

def grid():
    for x in range(-x0, x0+1, d):
        ligne((x, -y0), (x, y0))

    for y in range(-y0, y0+1, d):
        ligne((-x0, y), (x0, y))

def f(x, y):
    if -x0 < x < x0 and -y0 < y < y0:
        x = x//d * d + d//2
        y = y//d * d + d//2
        goto(x, y)
        dot(d)
        
    if button0.inside((x, y)):
        clear()
        button0.draw()
        button1.draw()
        grid()
        
    if button1.inside((x, y)):
        bye()

button0 = Button((200, 30), 'New')
button1 = Button((200, -60), 'Quit')
grid()

s.onclick(f)
s.listen()
done()
```

### Calculatrice

Ci-dessous vous avez le début du code pour une calculatrice.
La classe `Button` est utilisée également pour afficher le résultat.
Dans l'objet `display` nous changeons donc la taille, la couleur et l'alignement.

Votre tâche est d'ajouter le code pour faire fonctionner la calculatrice.
Pour vous donner une idée, le bouton `1` a été implémenté. Vous devez ajouter le code pour les 18 autres boutons.

```{codeplay}
from turtle import *
s = getscreen()
hideturtle()
tracer(0)
up()

class Button:
    def __init__(self, pos, text, size=(80, 40), color='lightgray', align='center'):
        self.pos = pos
        self.size = size
        self.text = text
        self.color = color
        self.align = align
        self.draw()
        
    def draw(self):
        goto(self.pos)
        fillcolor(self.color)
        begin_fill()
        down()
        for x in self.size * 2:     # parcourir 2 fois longeur et hauteur
            forward(x)
            left(90)
        up()
        end_fill()
        x, y = self.pos
        w, h = self.size
        if self.align == 'center':
            goto(x+w/2, y+h/4)
        elif self.align == 'right':
            goto(x+w-h/4, y+h/4)
        else:
            goto(x+h/4, y+h/4)
        color('black')
        write(self.text, font=('Arial', h//2), align=self.align)
        update()
        
    def __str__(self):
        return f'Button({self.text})'
    
    def inside(self, p):
        x, y = self.pos
        w, h = self.size
        
        return 0 < p[0]-x < w and 0 < p[1]-y < h

texts = ('AC', '+/-', '%', '÷', '7', '8', '9', '×', '4', '5',
         '6', '–', '1', '2', '3', '+', '0', '.', '=', '')

display = Button((-160, 40), '0', size=(320, 100), color='white', align='right')
    
buttons = []
for i in range(len(texts)):
    x = -160 + i%4 * 80
    y = 0 - i//4 * 40
    button = Button((x, y), texts[i])
    buttons.append(button)

number = 0

def f(x, y):
    global number
    p = (x, y)
    for b in buttons:  
        if b.inside(p):
            print(b)
            if b.text == '1':
                if number == 0:
                    number = 1
                else:
                    number = 10 * number + 1
                display.text = str(number)
                display.draw()

s.onclick(f)
s.listen()
done()
```

**Challenge** : Transformer le code en calculatrice scientifique avec les fonctions trigonométriques et autres.
