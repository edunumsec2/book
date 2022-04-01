# Démineur

```{codeplay}
"""
  1a   1b   1c   1d   1e   1f   1g   1h

  2a   2b   2c   2d   2e   2f   2g   2h

  3a   3b   3c   3d   3e   3f   3g   3h

  4a   4b   4c   4d   4e   4f   4g   4h

  5a   5b   5c   5d   5e   5f   5g   5h

  6a   6b   6c   6d   6e   6f   6g   6h

  7a   7b   7c   7d   7e   7f   7g   7h

  8a   8b   8c   8d   8e   8f   8g   8h

 """
#Defining / importing stuff
import turtle,random,time
from random import shuffle
clickx = 1
clicky = 1
minesaround = 0
mine = turtle.Turtle()
mine.speed(0)
mine.pu()
screen = turtle.Screen()
turtle.speed(0)
box = turtle.Turtle()
turtle.pu()
turtle.ht()
box.ht()
mine.ht()
box_list = [[209,206],[209,143],[209,80],[209,17],[209,-46],[209,-109],[209,-172],[209,-235],[146,206],[146,143],[146,80],[146,17],[146,-46],[146,-109],[146,-172],[146,-235],[83,206],[83,143],[83,80],[83,17],[83,-46],[83,-109],[83,-172],[83,-235],[20,206],[20,143],[20,80],[20,17],[20,-46],[20,-109],[20,-172],[20,-235],[-43,206],[-43,143],[-43,80],[-43,17],[-43,-46],[-43,-109],[-43,-172],[-43,-235],[-106,206],[-106,143],[-106,80],[-106,17],[-106,-46],[-106,-109],[-106,-172],[-106,-235],[-169,206],[-169,143],[-169,80],[-169,17],[-169,-46],[-169,-109],[-169,-172],[-169,-235],[-232,206],[-232,143],[-232,80],[-232,17],[-232,-46],[-232,-109],[-232,-172],[-232,-235]]
checkfor = []
eee = 0

#Sets the background color to 'Misty Rose'
window=turtle.Screen()
window.bgcolor("misty rose")

#Picks the pen up on sides to fix graphic errors
def grid_side():
  grid.pu()
  grid.forward(63)
  grid.pd()  

#Draws the horizontal / vertical lines
def grid_line():
  for i in range(4):
    grid_side()
    grid.left(90)
    grid.forward(504)
    grid.right(90)
    grid_side()
    grid.right(90)
    grid.forward(504)
    grid.left(90)

#Function for building lines on grid
def gridgrid():
  grid.pu()
  grid.goto(-252,252)
  grid.right(90)
  grid.pd()
  grid_line()
  grid.left(90)
  grid_line()

#Creates the grid
grid = turtle.Turtle()
grid.ht()
grid.speed(0)
grid.penup()
grid.goto(-252,-252)
grid.pendown()
grid.color('gainsboro')
grid.begin_fill()
grid.pensize(7)
for i in range(4):
  grid.forward(504)
  grid.left(90)
grid.forward(10)
grid.pensize(10)
grid.forward(500)
grid.color('silver')
grid.end_fill()
grid.pensize(8)
grid.color('gainsboro')
gridgrid()
grid.pensize(1)
grid.color('black')
gridgrid()
grid.pensize(2)
grid.goto(-252,-252)
for i in range(4):
  grid.forward(504)
  grid.left(90)

#For drawing mines
def minedraw(x,y):
  mine.ht()
  mine.goto(x-5,y+3)
  mine.color("fire brick")
  mine.write('m', move=False, font=("ms sans serif", 30, "normal"))

#Gets 10 mine positions
mines10 = random.sample(box_list, 10)
for i in mines10:
  box_list.remove(i)

#writes game over ontop of screen
def endwritewin():
  scorebox = turtle.Turtle()
  scorenum = turtle.Turtle()
  scorenum.ht()
  scorebox.ht()
  scorebox.pu()
  scorebox.speed(0)
  scorenum.speed(0)
  scorebox.goto(-126,265)
  scorebox.pensize(3)
  scorebox.pd()
  scorebox.begin_fill()
  for i in range(2):
    scorebox.forward(250)
    scorebox.left(90)
    scorebox.forward(50)
    scorebox.left(90)
  scorebox.color('gainsboro')
  scorebox.end_fill()
  scorenum.pu()
  scorenum.goto(scorebox.xcor(),scorebox.ycor())
  scorenum.forward(15)
  scorenum.left(90)
  scorenum.forward(10)
  scorenum.pd()
  scorenum.color('black')
  scorenum.write("   You Win! " , move=False, font=("Arial", 30, "normal"))
  screen.onscreenclick(None)

#writes game over ontop of screen
def endwrite():
  scorebox = turtle.Turtle()
  scorenum = turtle.Turtle()
  scorenum.ht()
  scorebox.ht()
  scorebox.pu()
  scorebox.speed(0)
  scorenum.speed(0)
  scorebox.goto(-126,265)
  scorebox.pensize(3)
  scorebox.pd()
  scorebox.begin_fill()
  for i in range(2):
    scorebox.forward(250)
    scorebox.left(90)
    scorebox.forward(50)
    scorebox.left(90)
  scorebox.color('gainsboro')
  scorebox.end_fill()
  scorenum.pu()
  scorenum.goto(scorebox.xcor(),scorebox.ycor())
  scorenum.forward(15)
  scorenum.left(90)
  scorenum.forward(10)
  scorenum.pd()
  scorenum.color('black')
  scorenum.write("Game Over" , move=False, font=("Arial", 30, "normal"))

#End of game if mine clicked
def endgamedead():
  for i in mines10:
    minedraw(i[0],i[1])
  screen.onscreenclick(None)
  endwrite()

#End of game if you win


#Edit box
def boxedit(x,y,num):
  global box_list
  box_list.remove([x,y])
  box.pu()
  box.ht()
  box.speed(0)
  box.goto(x-18,y-16)
  box.color('gainsboro')
  box.begin_fill()
  for i in range(4):
    box.forward(58)
    box.left(90)
  box.end_fill()
  turtle.goto(x,y)
  turtle.pd
  turtle.color('black')
  turtle.write(num , move=False, font=("ms sans serif", 30, "normal"))
  if len(box_list) == 0:
    print("You won!")
    endwritewin()
  
  return [x,y]

#Checks how many mines are around the box and returns that number.
def numcheck(x,y):
  minesaround = 0
  if [x-63,y] in mines10:
    minesaround += 1
  if [x+63,y] in mines10:
    minesaround += 1
  if [x,y-63] in mines10:
    minesaround += 1
  if [x,y+63] in mines10:
    minesaround += 1
  if [x-63,y-63] in mines10:
    minesaround += 1
  if [x-63,y+63] in mines10:
    minesaround += 1
  if [x+63,y-63] in mines10:
    minesaround += 1
  if [x+63,y+63] in mines10:
    minesaround += 1
  return minesaround

#Checks if boxes surrounding a zero are zero
def zerocheck(x,y):
  global checkfor
  checking=0
  if numcheck(x-63,y) == 0 and x-63 > -250:
    checkfor.append([x-63,y])
    checking=1
  if numcheck(x+63,y) == 0 and x+63 < 250:
    checkfor.append([x+63,y])
    checking=1
  if numcheck(x,y-63) == 0 and y-63 > -250:
    checkfor.append([x,y-63])
    checking=1
  if numcheck(x,y+63) == 0 and y+63 < 250:
    checkfor.append([x,y+63])
    checking=1
  if numcheck(x-63,y-63) == 0 and x-63 > -250 and y-63 > -250:
    checkfor.append([x-63,y-63])
    checking=1
  if numcheck(x+63,y+63) == 0 and x+63 < 250 and y+63 < 250:
    checkfor.append([x+63,y+63])
    checking=1
  if numcheck(x-63,y+63) == 0 and x-63 > -250 and y+63 < 250:
    checkfor.append([x-63,y+63])
    checking=1
  if numcheck(x+63,y-63) == 0 and x+63 < 250 and y-63 > -250:
    checkfor.append([x+63,y-63])
    checking=1
  return checking

def expandZero():
  global checkfor
  checking=1
  while checking == 1:
    for i in range(len(checkfor)):
      x=checkfor[i][0]
      y=checkfor[i][1]
      checking=zerocheck(x,y)
  return checkfor

#Checks if the box contains a mine or a number
def boxcheck(x,y):
  if [x,y] in mines10:
    print("mine clicked")
    endgamedead()
  else:
    if numcheck(x,y) == 0:
      #checks if boxes around were 0 as well and calls boxedit for each one NOT FINISHED
      boxedit(x,y,0)
      zerocheck(x,y)
      print(expandZero())
      for i in checkfor:
        chx = i[0]
        chy = i[1]
        boxedit(chx,chy,0)
    else:
      boxedit(x,y,numcheck(x,y))

#Gets y coords for box clicked
def getboxy(y):
  if y <= 252 and y >= 189:
    return 206
  elif y < 189 and y >= 126:
    return 143
  elif y < 126 and y >= 63:
    return 80
  elif y < 63 and y >= 0:
    return 17
  elif y < 0 and y >= -63:
    return -46
  elif y < -63 and y >= -126:
    return -109
  elif y < -126 and y >= -189:
    return -172
  elif y < -189 and y >= -252:
    return -235

#For getting the box clicked
def getbox(x, y):
  if x <= 252 and x >= 189:
    boxcheck(209, getboxy(y))
    return (209, getboxy(y))
  elif x < 189 and x >= 126:
    boxcheck(146, getboxy(y))
    return (146, getboxy(y))
  elif x < 126 and x >= 63:
    boxcheck(83, getboxy(y))
    return (83, getboxy(y))
  elif x < 63 and x >= 0:
    boxcheck(20, getboxy(y))
    return (20, getboxy(y))
  elif x < 0 and x >= -63:
    boxcheck(-43, getboxy(y))
    return (-43, getboxy(y))
  elif x < -63 and x >= -126:
    boxcheck(-106, getboxy(y))
    return (-106, getboxy(y))
  elif x < -126 and x >= -189:
    boxcheck(-169, getboxy(y))
    return (-169, getboxy(y))
  elif x < -189 and x >= -252:
    boxcheck(-232, getboxy(y))
    return (-232, getboxy(y))

#For getting pos of mouse click to check which box was clicked.
def mouseco(x, y):
  global eee
  if eee == 0:
    now = time.time()
    eee = 1
  print(getbox(x,y))
screen.onscreenclick(mouseco,1,add=None)
```
