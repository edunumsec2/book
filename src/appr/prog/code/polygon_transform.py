from turtle import *
from math import sin, cos, radians
hideturtle()
tracer(0)
screen = getscreen()

points = []
p0 = (0, 0)

def draw():
    clear()
    up()
    for p in points:
        goto(p)
        down()
        dot()
    up()
    goto(p0)
    dot(10, 'red')
    update()

def click(x, y):
    points.append((x, y))       # ajouter le point
    draw()
# ===
def scale(points, p0, dx, dy):
    for i, p in enumerate(points):
        points[i] = p0[0] + (p[0] - p0[0]) * dx, p0[1] + (p[1] - p0[1]) * dy
    draw()

def rotate(points, p0, angle):
    x0, y0 = p0
    for i, (x, y) in enumerate(points):
        x1 = x0 + cos(angle) * (x - x0) - sin(angle) * (y - y0)
        y1 = y0 + sin(angle) * (x - x0) + cos(angle) * (y - y0)
        points[i] = x1, y1
    draw()

screen.onkey(lambda : scale(points, p0, 1.2, 1.2), 'Up')
screen.onkey(lambda : scale(points, p0, 0.8, 0.8), 'Down')
screen.onkey(lambda : rotate(points, p0, radians(30)), 'Left')
screen.onkey(lambda : rotate(points, p0, radians(-30)), 'Right')
# ===
screen.onclick(click)
screen.listen()

if 'Pen' in globals():      # it's not codeplay
    screen.setup(width=600, height=400, startx=0, starty=0)
    done()