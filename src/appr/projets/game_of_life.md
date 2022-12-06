# Game of Life

Le Jeu de la vie est un automate cellulaire imaginé par John Horton Conway en 1970. Malgré des règles très simples, il est Turing-complet. C'est un jeu de simulation au sens mathématique.

```{codeplay}
import turtle
import random
import copy

screen=turtle.Screen()
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0,0)

lifeturtle = turtle.Turtle() # turtle for drawing life
lifeturtle.up()
lifeturtle.hideturtle()
lifeturtle.speed(0)
lifeturtle.color('black')

n = 25 # nxn grid
def draw_line(x1,y1,x2,y2): # this function draw a line between x1,y1 and x2,y2
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    turtle.goto(x2,y2)
    
def draw_grid(): # this function draws nxn grid
    turtle.pencolor('gray')
    turtle.pensize(3)
    x = -200
    for i in range(n+1):
        draw_line(x,-200,x,200)
        x += 400/n
    y = -200
    for i in range(n+1):
        draw_line(-200,y,200,y)
        y += 400/n

life = list() # create an empty list
def init_lives():
    for i in range(n):
        liferow = [] # a row of lives
        for j in range(n):
            if random.randint(0,7) == 0: # 1/7 probability of life
                liferow.append(1) # 1 means life
            else:
                liferow.append(0) # 0 means no life
        life.append(liferow) # add a row to the life list -> life is a list of list

def draw_square(x,y,size): # draws a filled square 
    lifeturtle.up()
    lifeturtle.goto(x,y)
    lifeturtle.down()
    lifeturtle.seth(0)
    lifeturtle.begin_fill()
    for i in range(4):
        lifeturtle.fd(size)
        lifeturtle.left(90)
    lifeturtle.end_fill()

def draw_life(x,y): # draws life in (x,y)
    lx = 400/n*x - 200 # converts x,y to screen coordinate 
    ly = 400/n*y - 200
    draw_square(lx+1,ly+1,400/n-2)

def draw_all_life(): # draws all life
    global life
    for i in range(n):
        for j in range(n):
            if life[i][j] == 1: draw_life(i,j) # draw live cells

def num_neighbors(x,y): # computes the number of life neighbours for cell[x,y]
    sum = 0
    for i in range(max(x-1,0),min(x+1,n-1)+1):
        for j in range(max(y-1,0),min(y+1,n-1)+1):
            sum += life[i][j]
    return sum - life[x][y]
        
def update_life(): # update life for each cycle
    global life
    newlife = copy.deepcopy(life) # make a copy of life
    for i in range(n):
        for j in range(n):
            k = num_neighbors(i,j)
            if k < 2 or k > 3:
                newlife[i][j] = 0
            elif k == 3:
                newlife[i][j] = 1
    life = copy.deepcopy(newlife) # copy back to life
    lifeturtle.clear() # clears life in previous cycle
    draw_all_life()
    screen.update() 
    screen.ontimer(update_life,200) # update life every 0.2 second

draw_grid()
init_lives()
update_life()
```

## Program 2

```{codeplay}
from random import choice
from turtle import *


s = Screen()
cells = {}
shape('square')
d = 10
up()
n = 10

def initialize():
    """Randomly initialize the cells."""
    for x in range(-n, n):
        for y in range(-n, n):
            cells[x, y] = False

    for x in range(-5, 5):
        for y in range(-5, 5):
            cells[x, y] = choice([True, False])


def step():
    """Compute one step in the Game of Life."""
    neighbors = {}

    for x in range(-(n-1), n-1):
        for y in range(-(n-1), n-1):
            count = -cells[x, y]
            for h in [-1, 0, 1]:
                for v in [-1, 0, 1]:
                    count += cells[x + h, y + v]
            neighbors[x, y] = count

    for cell, count in neighbors.items():
        if cells[cell]:
            if count < 2 or count > 3:
                cells[cell] = False
        elif count == 3:
            cells[cell] = True
    
def draw():
    """Draw all the squares."""
    step()
    clear()
    for (x, y), alive in cells.items():
        color('green' if alive else 'black')
        goto(x*d, y*d)
        stamp()
    update()
    s.ontimer(draw, 100)
    

s.setup(600, 400)
hideturtle()
tracer(0)
initialize()
draw()
s.onkey(initialize, ' ')
s.listen()
done()
```