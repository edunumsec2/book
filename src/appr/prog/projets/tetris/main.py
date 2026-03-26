import turtle
import math
import time
import random
from var_dic import * # import variables and dictionaries

# Add some functions to make program concise
def set_speed(a_turtle, speed):
  a_turtle.speed(speed)
def hide(a_turtle):
  a_turtle.hideturtle()

# Put all functions at top
def draw_screen():
    #fin.showturtle()
    fin.up()
    fin.home()
    fin.sety(inset)
    fin.left(90)
    fin.fd(70)
    fin.right(90)
    fin.fd(50)
    fin.fillcolor(colors["screen"])
    fin.begin_fill()
    fin.down()
    for i in range(4):
        fin.left(90)
        fin.fd(150)
    fin.end_fill()

def draw_grid():
    fin.up()
    fin.home()
    fin.sety(inset)
    fin.left(90)
    fin.fd(70)
    fin.right(90)
    fin.fd(50)
    fin.pencolor(colors["pixel"])
    
    for x in range(w+1):
        fin.goto(left+x*grid, top)
        fin.down()
        fin.goto(left+x*grid, top+h*grid)
        fin.up()
        
    for y in range(h+1):
        fin.goto(left, top+y*grid)
        fin.down()
        fin.goto(left+w*grid, top+y*grid)
        fin.up()

def fill_cell(x, y):
    fin.up()
    fin.home()
    fin.goto(left+x*grid, top+y*grid)
    fin.fillcolor(colors["pixel"])
    fin.begin_fill()
    fin.setheading(0)
    for side in range(4):
        fin.fd(grid)
        fin.rt(90)
    fin.end_fill()
    
def draw_piece(piece, x, y):
    blocks = pieces[piece]
    cell_x = x
    cell_y = y
    for row in blocks.split("\n"):
        for cell in row:
            if cell == " ":
                cell_x += 1
            if cell == "*":
                fill_cell(cell_x, cell_y)
                cell_x += 1
        cell_x = x
        cell_y -= 1



def moveLeft():
    global piece_x
    piece_x -= 1
    if piece_x < 0:
        piece_x = 0

def moveRight():
    global piece_x
    piece_x += 1
    if piece_x + 2 > w:
        piece_x = w-2

def moveDown():
    global piece_y
    piece_y -= 1
    if piece_y + piece_h < 1:
        piece_y = h 

# Turtles setup
disp = turtle.Screen()
disp.tracer(1000)
# disp.screensize(600, 600)

jay = turtle.Turtle()
sam = turtle.Turtle()
fin = turtle.Turtle()
but = turtle.Turtle()
key = turtle.Turtle()
speak = turtle.Turtle()

turtle_list = [jay,sam,fin,but,key,speak]
for i in range(len(turtle_list)):
  set_speed(turtle_list[i],9)
# Reset speak's speed as it is different from other turtles
set_speed(speak,5)

for i in range(len(turtle_list)):
  hide(turtle_list[i])



#Draw body
jay.fillcolor(colors["body"])
jay.up()
jay.sety(inset)
jay.right(180)
jay.fd(150)
jay.right(90)
jay.fd(250)
jay.right(90)
jay.down()
jay.begin_fill()
jay.fd(250)
jay.right(90)
jay.fd(350)
jay.circle(-50, 70)
jay.right(20)
jay.fd(218)
jay.right(90)
jay.fd(397)
jay.end_fill()


#sam.showturtle()
sam.fillcolor(colors["bezel"])
sam.up()
sam.sety(inset)
sam.left(90)
sam.forward(60)
sam.right(90)
sam.fd(70)
sam.begin_fill()
for i in range(2):
    sam.down()
    sam.circle(20, 70)
    sam.left(20)
    sam.fd(140)
    sam.circle(20, 70)
    sam.left(20)
    sam.forward(200)
sam.end_fill()

sam.up()
sam.goto(left-grid*12, top+grid*12)
sam.fillcolor("#e86060")
sam.begin_fill()
sam.circle(4)
sam.end_fill()
sam.goto(left-grid*12, top+grid*12+2)
sam.fillcolor("#ffe608")
sam.begin_fill()
sam.circle(2)
sam.end_fill()

#Draw buttons
#but.showturtle()
but.fillcolor(colors["button"])
but.up()
but.sety(inset)
but.right(90)
but.fd(50)
but.left(90)
but.fd(30)
but.down()
but.begin_fill()
but.circle(15)
but.end_fill()
but.up()
but.left(30)
but.fd(50)
but.down()
but.begin_fill()
but.circle(15)
but.end_fill()

#Draw keypad
#key.showturtle()
key.up()
key.sety(inset)
key.bk(100)
key.down()
key.fillcolor(colors["dpad"])
key.begin_fill()
for i in range(4):
    key.fd(17)
    key.right(90)
    key.fd(17)
    key.left(90)
    key.fd(17)
    key.right(90)
key.end_fill()
    
#Draw Speaker
speaker_x = 40
speaker_y = -130 + inset
speak.fillcolor(colors["speaker"])
for i in range(6):
    speak.penup()
    speak.goto(speaker_x + i*10, speaker_y + i*10)
    speak.down()
    speak.begin_fill()
    speak.setheading(135)
    speak.fd(40)
    speak.circle(5, 180)
    speak.fd(40)
    speak.circle(5, 180)
    speak.end_fill()
    speak.up()



for p in pieces:
    pieces[p] = pieces[p][1:-1]
piece = random.choice(list(pieces))
piece_x = 4
piece_y = 20
piece_h = len(pieces[piece].split("\n"))


disp.onkey(moveLeft, "Left")
disp.onkey(moveRight, "Right")
disp.onkey(moveDown, "Down")
disp.listen()

while True:
    draw_screen()
    draw_grid()
    draw_piece(piece, piece_x, piece_y)
    time.sleep(delay)

    piece_y -= 1
    if piece_y - piece_h < 0:
        piece_y = 22
        piece = random.choice(list(pieces))
        piece_h = len(pieces[piece].split("\n"))
        
    disp.update()

    
disp.exitonclick()
