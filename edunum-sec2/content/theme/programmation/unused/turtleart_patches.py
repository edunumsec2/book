# book 2 - patches
from turtle import *
from colorsys import hls_to_rgb
from random import randint, uniform

bgcolor('black')
up()
speed(0)
hue = 0

def patch(x0, y0):
    for i in range(30):
        x = x0 + randint(0, 30)
        y = y0 + randint(0, 90)
        goto(x, y)
        setheading(randint(-5, 5))
        
        color = hls_to_rgb(hue, uniform(0.4, 0.9), 1)
        pencolor(color)
        pensize(randint(10, 15))
        
        down()
        forward(randint(80, 90))
        up()
        
def star():
    setheading(0)
    pensize(7)
    pencolor('black')
    for i in range(5):
        forward(80)
        right(2*360/5)
    pensize(5)
    color = hls_to_rgb(hue, 0.5, 1)
    pencolor(color)
    for i in range(5):
        forward(80)
        right(2*360/5)
    up()

for x in range(-320, 250, 130):
    for y in range(-270, 200, 110):
        patch(x, y)
        up()
        goto(x+20, y+60)
        down()
        hue = hue + 0.2
        star()
        hue = hue + 0.1