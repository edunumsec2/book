"""
Titre : polygon.py
Nom : Raphael Holzer
Date : 15 mars 2023

Editeur de polygone
- un clic de souris ajouten un point
- cliquer sur un point le selectionne
- un point séléctionné peut être bougé (clic) ou supprimés (BACK)
- TAB permet de parcourir les points sélectionnées

L'éditeur peut affchier
- une grille (grid)
- des points (dots)
- l'aide (help)
- la numérotation des points (index)
- les coordonnées des points (pos)

La grille peut être aimanté.

SPACE permet le mode transformation
- scale
- rotate
- shear
touches DIRECTION pour transformer
ESC pour arrêter le mode transformation

Features do add : 
- move by pixel/grid
- change grid size
"""
from turtle import *
from math import sin, cos, radians

d = 10

# polygon which can be edited
points = []
objects = []

# selected point
p_index = -1

# polygon bounding box, used for transforms (scale, rotate, shear)
box = []
box_index = 0

settings = {}
settings['screen_size'] = 600, 400
settings['show_box'] = False
settings['show_dots'] = True
settings['show_grid'] = True
settings['show_help'] = True
settings['show_index'] = False
settings['show_pos'] = False
settings['is_magnetic'] = True

settings['box_color'] = 'red'
settings['box_size'] = 2
settings['grid_d'] = 20
settings['grid_color'] = 'gray'
settings['grid_size'] = 1
settings['font_size'] = 12

settings['fill_colors'] = ('pink', 'yellow', 'lime', 'orange', 'cyan', 'beige')
settings['fill_color'] = 'pink'
settings['pen_colors'] = ('black', 'gray', 'red', 'green', 'blue', 'brown', 'navy')
settings['pen_color'] = 'black'
settings['pen_sizes'] = (1, 2, 5, 10)
settings['pen_size'] = 1
settings['edit_modes'] = ('scale', 'rotate', 'shear')
settings['edit_mode'] = 'scale'

screen = getscreen()
screen.setup(width=settings['screen_size'][0],
             height=settings['screen_size'][1],
             startx=0, starty=0)
text = Turtle()
text.up()
text.hideturtle()
hideturtle()
tracer(0)
up()

settings['help'] = """
Help menu

a - align with grid
d - duplicate object
e - save EPS file
c - choose pen color
f - choose fill color
s - choose pen size
g - show grid
h - show help
i - show index
o - show dots
p - show position
m - toggle magnetic
k - erase all
x - erase

Space - transform mode (box)
Arrows - scale/rotate/shear
Clic - move box
Return - add new object
Tab - next dot
BackSpace - remove dot/box
Shift_R - close polygon
"""


def write_text(lines, p=None, d=14):
    """Writes multiple lines at position p."""
    if p:
        text.goto(p)
    for line in lines:
        text.write(line, font=(None, d))
        text.sety(text.ycor() - d)


def draw_help():
    """Displays the help text."""
    w, h = settings['screen_size']
    p = -w / 2 + 25, h / 2 - 30
    lines = settings['help'].split('\n')
    write_text(lines, p)


def help():
    """Displays the help screen."""
    if settings['show_help']:
        draw_help()
    else:
        text.clear()
    settings['show_help'] = not settings['show_help']


def draw_grid():
    """Draws the grid."""
    pencolor(settings['grid_color'])
    pensize(settings['grid_size'])
    d = settings['grid_d']
    w, h = settings['screen_size']
    x0 = w // 2 // d * d
    y0 = h // 2 // d * d

    for x in range(-x0, x0+1, d):
        draw_line((x, -h/2), (x, h/2))

    for y in range(-y0, y0+1, d):
        draw_line((-w/2, y), (w/2, y))
    up()


def grid_point(x, y):
    """Returns the closest grid point to (x, y)."""
    d = settings['grid_d']
    x0 = (x + d/2) // d * d
    y0 = (y + d/2) // d * d
    return x0, y0


def align_dots():
    """Aligns the points to the grid."""
    for i in range(len(points)):
        points[i] = grid_point(*points[i])
    draw()


def distance(p, q):
    """Returns the distance between points p and q."""
    d = (p[0]-q[0])**2 + (p[1]-q[1])**2
    return d ** 0.5


def get_box():
    """Returns a bounding box around the polygone."""
    global box
    x_list = [x for (x, y) in points]
    y_list = [y for (x, y) in points]
    x0 = min(x_list)
    x2 = max(x_list)
    x1 = (x2 + x0) / 2

    y0 = min(y_list)
    y2 = max(y_list)
    y1 = (y2 + y0) / 2

    box = [(x0, y0), (x1, y0), (x2, y0), (x2, y1), (x2, y2),
           (x1, y2), (x0, y2), (x0, y1), (x1, y1)]


def draw_box():
    """Draws a bounding box around the polygone."""
    pencolor(settings['box_color'])
    pensize(settings['box_size'])
    up()
    for p in box[:-1] + [box[0]]:
        goto(p)
        down()
        dot()
    up()
    goto(box[-1])           # center point
    dot()
    goto(box[box_index])    # index point
    dot(d)
    write(settings['edit_mode'], font=(None, settings['font_size']))


def draw_line(p, q):
    """Draws a line from point p to point q."""
    goto(p)
    down()
    goto(q)
    up()


def draw_polygon():
    """Draws the polygon."""
    pensize(settings['pen_size'])
    pencolor(settings['pen_color'])
    fillcolor(settings['fill_color'])

    up()
    if points:
        goto(points[0])
        begin_fill()
    for i, p in enumerate(points):
        goto(p)
        down()
        if i == p_index:
            dot(d, 'red')
        if settings['show_dots']:
            dot()
        if settings['show_index']:
            write(i, font=(None, settings['font_size']))
        if settings['show_pos']:
            p = int(xcor()), int(ycor())
            write(p, font=(None, settings['font_size']))
    up()
    end_fill()


def draw_objects():
    """Draws the previously saved objects."""
    for (w, pen, fill, points) in objects:
        width(w)
        color(pen, fill)
        if points:
            goto(points[0])
            begin_fill()
        for p in points:
            goto(p)
            down()
        up()
        end_fill()


def draw(update_box=True):
    """Draws everything"""
    clear()
    if settings['show_grid']:
        draw_grid()
    # if settings['show_help']:
    #     draw_help()
    draw_objects()
    draw_polygon()
    if settings['show_box'] and points:
        if update_box:
            get_box()
        draw_box()


def toggle(key):
    """Toggle boolean value in settings dictionary."""
    settings[key] = not settings[key]
    draw()


def next(key):
    """Increment to next value in settings dictionary"""
    values = settings[key+'s']
    val = settings[key]
    i = values.index(val)
    settings[key] = values[(i + 1) % len(values)]
    draw()


def select_point(x, y):
    """Select a polygon point."""
    global p_index

    for i, p in enumerate(points):
        if distance(p, (x, y)) < d:
            p_index = i
            return True


def select_box_point(x, y):
    """Select a box point."""
    global box_index

    for i, p in enumerate(box):
        if distance(p, (x, y)) < d:
            box_index = i
            return True


def close_polygon():
    """Close the polygone."""
    p0 = points[0]
    points.append(p0)
    draw()


def select_next():
    """Select next dot."""
    global p_index, box_index
    if settings['show_box']:
        box_index = (box_index + 1) % len(box)
    else:
        p_index = (p_index + 1) % len(points)
    draw()


def unselect():
    """Unselect dot and box."""
    global p_index
    p_index = -1
    settings['show_box'] = False
    draw()


def remove_dot():
    """Remove selected dot."""
    global p_index
    if points:
        points.pop(p_index)
        p_index = min(p_index, len(points)-1)
        draw()


def add_object():
    """Save current polygone to the object list."""
    size = settings['pen_size']
    pen = settings['pen_color']
    fill = settings['fill_color']
    objects.append([size, pen, fill, points[:]])


def new_object():
    """Save current polygone and project new one."""
    global points, p_index
    add_object()
    points = []
    p_index = -1
    settings['show_box'] = False 
    draw()


def duplicate_object():
    """Save current object and keep."""
    add_object()
    move(points, 10, 10)
    draw()


def save_eps():
    """Saves an EPS file."""
    screen.getcanvas().postscript(file='polygon.eps')


def erase():
    """Erase the current polygone."""
    global points, p_index
    settings['show_box'] = False
    points = []
    p_index = -1
    draw()


def erase_all():
    """Erase all objects."""
    global objects
    objects = []
    erase()


def move(points, dx, dy):
    """Move the points by the displacement vector (dx, dy)."""
    for i, p in enumerate(points):
        points[i] = p[0] + dx, p[1] + dy


def scale(points, p0, dx, dy):
    """Scale the polygone with reference to p0 by scaling factor (dx, dy)."""
    x0, y0 = p0
    for i, (x, y) in enumerate(points):
        points[i] = x0 + (x - x0) * dx, y0 + (y - y0) * dy


def shear(points, p0, dx, dy):
    """Shear the points with reference to p0 by the shearing factor (dx, dy)."""
    for i, p in enumerate(points):
        x = p[0] - p0[0]
        y = p[1] - p0[1]
        points[i] = p0[0] + x + dx*y, p0[1] + y + dy * x


def rotate(points, p0, angle):
    """Rotate the points around p0 by the given angle (radians)."""
    x0, y0 = p0
    for i, (x, y) in enumerate(points):
        x1 = x0 + cos(angle) * (x - x0) - sin(angle) * (y - y0)
        y1 = y0 + sin(angle) * (x - x0) + cos(angle) * (y - y0)
        points[i] = x1, y1


def transform():
    """Show edit box: move, rotate, scale, shear."""
    global p_index
    if not settings['show_box']:
        settings['show_box'] = True
        settings['edit_mode'] = 'scale'
        p_index = -1
    else:
        next('edit_mode')
    draw()


def direction(x, y):
    """Edit the polygone with the arrow keys: move, scale, shear, rotate."""
    if settings['show_box']:
        p0 = box[box_index]
        d = settings['grid_d']
        mode = settings['edit_mode']

        if mode == 'scale':
            if x:
                scale(points, p0, 1.2**x, 1)
                scale(box, p0, 1.2**x, 1)
            else:
                scale(points, p0, 1, 1.2**y)
                scale(box, p0, 1, 1.2**y)

        elif mode == 'rotate':
            if x:
                rotate(points, p0, -radians(15)*x)
                rotate(box, p0, -radians(15)*x)
            else:
                scale(points, p0, 1.2**y, 1.2**y)
                scale(box, p0, 1.2**y, 1.2**y)
        else:
            if x:
                shear(points, p0, 0.2 * x, 0)
                shear(box, p0, 0.2 * x, 0)
            else:
                shear(points, p0, 0, 0.2 * y)
                shear(box, p0, 0, 0.2 * y)
        draw(update_box=False)
    else:
        d = settings['grid_d']
        if p_index >= 0:
            move([points[p_index]], x*d, y*d)
        else:
            move(points, x*d, y*d)
        draw()


def click(x, y):
    """Callback function for the mouse-click."""

    if settings['show_box'] and points:
        if select_box_point(x, y):
            ...
        else:
            if settings['is_magnetic']:
                x, y = grid_point(x, y)

            x0, y0 = box[box_index]
            move(points, x-x0, y-y0)
            move(box, x-x0, y-y0)
        draw(update_box=False)
    else:
        select_point(x, y)
        if settings['is_magnetic']:
            x, y = grid_point(x, y)
        if p_index >= 0:
            points[p_index] = (x, y)    # move the point
        else:
            points.append((x, y))       # add the point
        draw()


if settings['show_help']:
    help()
draw()

screen.onclick(click)
screen.onkey(align_dots, 'a')
screen.onkey(duplicate_object, 'd')
screen.onkey(save_eps, 'e')
screen.onkey(lambda: next('pen_color'), 'c')
screen.onkey(lambda: next('fill_color'), 'f')
screen.onkey(lambda: next('pen_size'), 's')
screen.onkey(help, 'h')
screen.onkey(erase_all, 'k')
screen.onkey(lambda: toggle('show_grid'), 'g')
screen.onkey(lambda: toggle('show_index'), 'i')
screen.onkey(lambda: toggle('is_magnetic'), 'm')
screen.onkey(lambda: toggle('show_dots'), 'o')
screen.onkey(lambda: toggle('show_pos'), 'p')
screen.onkey(erase, 'x')

screen.onkey(transform, 'space')
screen.onkey(new_object, 'Return')
screen.onkey(select_next, 'Tab')
screen.onkey(close_polygon, 'Shift_R')
screen.onkey(remove_dot, 'BackSpace')
screen.onkey(lambda: direction(1, 0), 'Right')
screen.onkey(lambda: direction(-1, 0), 'Left')
screen.onkey(lambda: direction(0, 1), 'Up')
screen.onkey(lambda: direction(0, -1), 'Down')
screen.onkey(unselect, 'Escape')
screen.onkey(lambda: print('Shift_L'), 'Shift_L')
screen.onkey(lambda: print('Alt_L'), 'Alt_L')
screen.onkey(lambda: print('F1'), 'F1')

screen.listen()
done()
