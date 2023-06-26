from turtle import *

a = 80
palette = ('pink', 'lightblue', 'orange', 'white', 'yellow', 'lightgreen')
cube = (((0, 1, 2), (3, 4, 0), (1, 3, 5)),
        ((1, 5, 4), (5, 0, 2), (2, 4, 5)),
        ((3, 0, 3), (2, 5, 0), (4, 3, 1)))

cube2 = (((0, 0, 0), (1, 1, 1), (2, 2, 2)),
        ((4, 4, 4), (4, 4, 4), (4, 4, 4)),
        ((3, 0, 3), (2, 5, 0), (4, 3, 1)))


def losange():
    begin_fill()
    for angle in (120, 60, 120, 60):
        forward(a)
        left(angle)
    end_fill()
    forward(a)

def next_line():
    backward(3*a)
    left(120)
    forward(a)
    right(120)
    
def next_surface():
    left(120)
    backward(3*a)
    
speed(0)
left(30)
for surface in cube:
    for line in surface: 
        for i in line:
            fillcolor(palette[i])
            losange()
        next_line()
    next_surface()
done()
