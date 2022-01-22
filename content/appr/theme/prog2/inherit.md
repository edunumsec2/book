# Hériter - `E(P)`

Dans ce chapitre nous découvrons comment une classe peut hériter des attributs et des méthodes d'une classe parents. Nous allons voir que : 

- l'expression `class Enfant(Parent):` implique un héritage de la classe `Parent`,
- avec la fonction `super().__init__()` le constructeur de la classe parent est appelé.

```{question}
La la classe `P` dans `E(P)` est appelé

{v}`la classe parent`  
{f}`la classe enfant`  
{f}`la classe primaire`  
{f}`la classe principale`
```

## Classe Dot, Rect, Text

Dans l'exemple suivant nous définissons une classe parent `Object`. Elle possède les méthodes

- `draw_box()` pour dessiner un contour rectangulaire
- `fill_box()` pour dessiner un rectangle rempli
- `inside(x, y)` pour tester si le point `(x, y)` se trouve dans le rectangle

Les trois fonctions `Dot`, `Rect` et `Text` héritent tous les méthodes de la classe parent `Object`.

```{codeplay}
from turtle import *
up()
speed(0)
hideturtle()
getscreen().bgcolor('lightgray')

class Object:
        
    def draw_box(self):
        goto(self.pos)
        down()
        for d in self.size * 2:
            forward(d)
            left(90)
        up()
        
    def fill_box(self):
        goto(self.pos)
        color(*self.col)
        width(self.width)
        begin_fill()
        self.draw_box()
        end_fill()
        width(1)

    def inside(self, x, y):
        x0, y0 = self.pos
        x1 = x0 + self.size[0]
        y1 = y0 + self.size[1]
        return x0 < x < x1 and y0 < y < y1
        
    def __str__(self):
        return f'{self.__class__.__name__}({self.pos}, {self.size})'

class Dot(Object):
    def __init__(self, pos, d=20, col='red'):
        self.pos = pos
        self.size = d, d
        self.col = col
        self.draw()
        
    def draw(self):
        r = self.size[0] / 2
        goto(self.pos[0]+r, self.pos[1]+r)
        pencolor(self.col)
        dot(self.size[0])
        self.draw_box()
    
class Rect(Object):
    def __init__(self, pos, size, width=1, col=('black', 'white')):
        self.pos = pos
        self.size = size
        self.width = width
        self.col = col
        self.draw()
        
    def draw(self):
        self.fill_box()        
             
class Text(Object):
    def __init__(self, pos, text, col='red', font=(None, 12, 'normal'), align='left'):
        super()
        self.text = text
        self.pos = pos
        self.col = col
        self.font = font
        self.align = align
        self.draw()
        
    def draw(self):
        goto(self.pos)
        color(self.col)
        x0 = xcor()
        write(self.text, font=self.font, align=self.align, move=True)
        self.size = xcor() - x0, self.font[1]
        self.draw_box()
        
d0 = Dot((0, 0))
d1 = Dot((100, 20), 50, 'lime')

t0 = Text((0, 50), 'origin', font=(None, 18, 'bold'))
t1 = Text((0, 100), 'pad', font=(None, 80), col='blue')
t2 = Text((-100, 100), '夢', font=(None, 60), col='blue')
t3 = Text((-200, 100), '📺', font=(None, 60), col='blue')

r0 = Rect((-100, 0), (50, 80))
r1 = Rect((-150, -20), (60, 80), width=5, col=('black', 'pink'))

def f(x, y):
    for obj in (d0, d1, t0, t1, t2, t3, r0, r1):
        if obj.inside(x, y):
            print('clicked in', obj)
    
getscreen().onclick(f)
getscreen().listen()
```

**Exercice** : Clickez dans tout les objets et observez les info affichés dans la console.