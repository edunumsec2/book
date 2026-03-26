"""Template for a game

This script implements general classes for your game.
Put your description of the game as a doc-string at the beginning.
A doc-string is a mult-line string enclosed with three double-quotes.

Your game must define at a minimum these 5 classes :

- Rectangle
- Text
- Button (composed of class Rectangle and Button)
- Grid
- Game (composed of class Grid, Text and Button)

You can modify these classes.
You can add more classes (ex. Player, Enemy, Score, Room, Level, etc.)
The last command to be called must be Game()

Author: Raphael Holzer
Date: 11 May 2022
"""

from turtle import *

def ligne(p, q):
    """Draws a ligne from point p to point q."""

    goto(p)
    down()
    goto(q)
    up()


class Rectangle:
    """Draw a filled rectangle."""
    
    def __init__(self, pos, size, color='gray'):
        """Initialize the rectangle and draw it."""
        self.pos = pos
        self.size = size
        self.color = color
        self.draw()
    
    def outline(self):
        """Draw just the outline of the rectangle."""
        goto(self.pos)
        down()
        for x in self.size * 2:
            forward(x)
            left(90)
        up()
        
    def draw(self):
        """Draw the outline of the rectangle and fill it a color is defined."""
        if self.color:
            fillcolor(self.color)
            begin_fill()
            self.outline()
            end_fill()
        else:
            self.outline()
            
    def inside(self, p):
        """Check if the point p is inside the rectangle."""
        x, y = self.pos
        w, h = self.size
        
        return 0 < p[0]-x < w and 0 < p[1]-y < h
        

class Text:
    """Draw a text at a given position."""
    
    def __init__(self, pos, text, size=16, align='left'):
        """Initilizes the text"""
        self.pos = pos
        self.text = text
        self.size = size
        self.align = align
        self.draw()
        
    def draw(self):
        """Draw the text."""
        goto(self.pos)
        write(self.text, font=('Arial', self.size), align=self.align)
     
class Button:
    def __init__(self, pos, text, size=(80, 30), color='lightgray', align='center'):
        self.rect = Rectangle(pos, size, color)
        x, y = pos
        w, h = size
        self.label = Text((x + w//2, y + h//4), text, h//2, 'center')
        
    def draw(self):
        self.rect.draw()
        self.label.draw()
    
    def inside(self, p):
        return self.rect.inside(p)

class Grid:
    """Define a grid class with the size (n x m).

    n is the number of lignes,
    m the number of columns.
    """

    def __init__(self, n=8, m=8, d=40, ongrid=True):
        """Create a new Grid instance"""
        self.n = n        # vertical (y)
        self.m = m        # horizontal (x)
        self.d = d        # distance
        self.ongrid = ongrid
        self.x0 = m * d // 2
        self.y0 = n * d // 2
        
        self.draw()
        print(self)
        
    def draw(self):
        """Draw the grid."""
        for x in range(-self.x0, self.x0+1, self.d):
            ligne((x, -self.y0), (x, self.y0))

        for y in range(-self.y0, self.y0+1, self.d):
            ligne((-self.x0, y), (self.x0, y))
    
    def inside(self, x, y):
        """Check if (x, y) is inside the grid."""
        x0 = self.x0
        y0 = self.y0
        if self.ongrid:
            x0 += self.d // 2
            y0 += self.d // 2    
        return -x0 < x < x0 and -y0 < y < y0
            
    def get_cell(self, x, y):
        """Returns the coordinates of center or intersection."""
        
        x += self.x0
        y += self.y0
        if self.ongrid:
            x += self.d // 2
            y += self.d // 2
            
        i = int(y // self.d)
        j = int(x // self.d)
        
        print(i, j)
               
    def __str__(self):
        return f'Grid({self.n}, {self.m})'


class Game:
    """This is a general Game class.
    It contains all the game variables and attributes.
    """
    
    def __init__(self):
        """Set up the game window and the turtle attributes.
        Initilize all the attributes.
        Setup the callback functions.
        """
        
        setup(600, 400)
        hideturtle()
        tracer(0)
        up()
   
        self.score = 0
        self.history = []
        self.grid = Grid()
        self.title = Text((0,  170), 'Title of your Game', 24, 'center')
        self.status = Text((-280, -190), 'status line')
        self.bt_clear = Button((200, 100), 'Clear')
        self.bt_new = Button((200, 50), 'New')
        
        s = getscreen()
        s.onclick(self.click)
        s.onkey(up, 'u')
        s.onkey(down, 'd')
        s.onkey(clear, 'BackSpace')
        s.onkey(self.draw, ' ')  
        s.listen()
        done()
        
    def click(self, x, y):
        """Reacts to mouse clicks."""
        if self.grid.inside(x, y):
            goto(x, y)
            dot()
            write(x, y)
        
        p = x, y
        if self.bt_clear.inside(p):
            clear()
            self.bt_new.draw()
            self.bt_clear.draw()
        
        if self.bt_new.inside(p):
            self.draw()
        
    def draw(self):
        """Draws all the game objects."""
        self.grid.draw()
        self.title.draw()
        self.status.draw()
        self.bt_clear.draw()
        self.bt_new.draw()
        down()

if __name__ == '__main__':
    game = Game()