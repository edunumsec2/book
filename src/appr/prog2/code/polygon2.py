from turtle import *
hideturtle()
tracer(0)
fillcolor('pink')
screen = getscreen()

points = []
settings = {}
settings['show_dots'] = True
settings['show_fill'] = False
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
    if p_index >=0:
        goto(points[p_index])
        dot(d, 'red')
    update()

def toggle(key):
    settings[key] = not settings[key]
    draw()
# ===
def click(x, y):
    if select_point(x, y):          # selectionner un point
        ...
    elif p_index >= 0:
        points[p_index] = x, y      # repositionner le point
    else:
        points.append((x, y))       # ajouter le point
    draw()

def distance(p, q):
    d = (p[0]-q[0])**2 + (p[1]-q[1])**2
    return d ** 0.5

p_index = -1
d = 10

def select_point(x, y):
    global p_index
    for i, p in enumerate(points):
        if distance(p, (x, y)) < d:
            p_index = i
            return True         # on a cliqué sur un point
        
def unselect_dot():
    global p_index
    p_index = -1
    draw()

def next_dot():
    global p_index
    p_index = (p_index + 1) % len(points)
    draw()

def remove_dot():
    global p_index
    if points:
        points.pop(p_index)
    p_index = min(len(points)-1, p_index)
    draw()

screen.onkey(unselect_dot, 'Escape')
screen.onkey(next_dot, 'Tab')
screen.onkey(remove_dot, 'BackSpace')
# ===
screen.onclick(click)
screen.onkey(lambda: toggle('close_poly'), 'c')
screen.onkey(lambda: toggle('show_dots'), 'd')
screen.onkey(lambda: toggle('show_fill'), 'f')
screen.onkey(lambda: toggle('show_index'), 'i')
screen.onkey(lambda: toggle('show_line'), 'l')
screen.onkey(lambda: toggle('show_pos'), 'p')
screen.listen()

if 'Pen' in globals():      # it's not codeplay
    screen.setup(width=600, height=400, startx=0, starty=0)
    done()