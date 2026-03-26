# ===
from turtle import *
hideturtle()
tracer(0)
fillcolor('pink')

points = []
settings = {}
settings['show_dots'] = True
settings['show_fill'] = True
settings['show_line'] = True
settings['show_index'] = False
settings['show_pos'] = False
settings['close_poly'] = False

def draw():
    clear()
    up()
    _col = color()
    if points:
        goto(points[0])
        if settings['show_fill']:
            begin_fill()
        if settings['show_line']:
            down()
    for i, p in enumerate(points):
        goto(p)
        if settings['show_dots']:
            dot()
        if settings['show_index']:
            color('black')
            write(i)
        if settings['show_pos']:
            color('black')
            p = int(xcor()), int(ycor())
            write(p)
        color(*_col)
    if settings['close_poly']:
            goto(points[0])
    if settings['show_fill']:
        end_fill()
    up()
    update()

def toggle(key):
    settings[key] = not settings[key]
    draw()

def click(x, y):
    points.append((x, y))       # add the point
    draw()

screen = getscreen()
screen.onclick(click)
screen.onkey(lambda: toggle('close_poly'), 'c')
screen.onkey(lambda: toggle('show_dots'), 'd')
screen.onkey(lambda: toggle('show_fill'), 'f')
screen.onkey(lambda: toggle('show_index'), 'i')
screen.onkey(lambda: toggle('show_line'), 'l')
screen.onkey(lambda: toggle('show_pos'), 'p')
screen.listen()
# ===
if 'Pen' in globals():      # it's not codeplay
    screen.setup(width=600, height=400, startx=0, starty=0)
    done()