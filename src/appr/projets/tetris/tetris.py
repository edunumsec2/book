from turtle import *
from random import *
from time import *

d = 20
w = 10
h = 22
x0 = w * d // 2
y0 = h * d // 2
delay = 0.1

pieces = {
'L' : ((1, 0), (1, 0), (1, 1)), 
'J' : ((0, 1), (0, 1), (1, 1)),
'T' : ((1, 0), (1, 1), (1, 0)),
'I' : ((1,), (1,), (1,), (1,)), 
'S' : ((0, 1, 1), (1, 1, 0)),
'Z' : ((1, 1, 0), (0, 1, 1)),
'O' : ((1, 1), (1, 1)),
}

for x in pieces:
    print(x)
    print(x, len(pieces[x]), len(pieces[x][0]))
    for line in pieces[x]:
        print(line)

def line(p, q):
    goto(p)
    down()
    goto(q)
    up()

def draw_grid():
    for x in range(-x0, x0+1, d):
        line((x, -y0), (x, y0))
        
    for y in range(-y0, y0+1, d):
        line((-x0, y), (x0, y))

def fill_cell(x, y):
    goto(-x0+x*d, -y0+y*d)
    begin_fill()
    for side in range(4):
        forward(d)
        right(90)
    end_fill()
    
def draw_piece(piece, x, y):
    blocks = pieces[piece]
    cell_x = x
    cell_y = y
    for row in pieces[piece]:
        for cell in row:
            if cell == 0:
                cell_x += 1
            if cell == 1:
                fill_cell(cell_x, cell_y)
                cell_x += 1
        cell_x = x
        cell_y -= 1

def moveLeft():
    global piece_x
    piece_x = max(0, piece_x-1)

def moveRight():
    global piece_x
    piece_x = min(piece_x + 1, w-2)

def moveDown():
    global piece_y
    piece_y -= 1
    if piece_y + piece_h < 1:
        piece_y = h 

# Turtles setup
s = Screen()
s.tracer(1000)
s.screensize(600, 600)

piece = choice(list(pieces))
piece_x = 4
piece_y = 20
piece_h = len(pieces[piece])
print(piece, piece_h)

s.onkey(moveLeft, 'Left')
s.onkey(moveRight, 'Right')
s.onkey(moveDown, 'Down')
s.listen()

while True:
    clear()
    draw_grid()
    draw_piece(piece, piece_x, piece_y)
    sleep(delay)

    piece_y -= 1
    if piece_y - piece_h < 0:
        piece_y = 22
        piece = choice(list(pieces))
        piece_h = len(pieces[piece])
        
    s.update()
 
s.exitonclick()