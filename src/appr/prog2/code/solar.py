from turtle import *
from math import *

# Solar system

getscreen().bgcolor('black')

dot(50, 'gold')
hideturtle()

AU = 200
terre = Turtle()
terre.color('lightblue')
terre.shape('circle')
terre.up()

mars = Turtle()
mars.color('red')
mars.shape('circle')
mars.up()

t = 0  # temps en jours

while True:
    x = AU * sin(t / 360 * 2 * pi)
    y = 0.5 * AU * cos(t / 360 * 2 * pi)
    terre.goto(x, y)
    terre.down()
    
    x_m = 1.5 * AU * sin(t / 450 * 2 * pi)
    y_m = 0.5 * 1.5 * AU * cos(t / 450 * 2 * pi)
    mars.goto(x_m, y_m)
    mars.down()

    t += 1

done()
