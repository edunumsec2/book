from turtle import *
from math import *

def point(p, d=10):
    goto(p)
    dot(d)

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

def rectangle(p, taille):
    goto(p)
    down()
    for x in taille * 2:
        forward(x)
        left(90)
    up()

def ellipse(p, taille):
    for i in range(37):
        x = p[0] + taille[0]/2 * sin(pi * i / 18)
        y = p[1] + taille[1]/2 * cos(pi * i / 18)
        goto(x, y)
        down()
    up()

if __name__ == '__main__':
    up()
    p = (-200, 0)
    point(p)
    ligne((-100, -100), (-100, 100))
    left(10)
    rectangle((0, 0), (80, 100))
    ellipse((200, 0), (80, 100))
    
    
    
    