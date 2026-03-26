""" Grid

"""
from turtle import *
from game import *


def line(p, q):
    """Draws a ligne from point p to point q."""
    goto(p)
    down()
    goto(q)
    up()


class Matrix:
    """Represents 2D data."""
    def __init__(self, n, m):
        self.data = []
        for i in range(n):
            self.data.append([0] * m)
        self.dict = {}
        for i in range(n):
            for j in range(m):
                self.dict[i, j] = None
        print(self.dict)

    def print(self):
        for line in self.data:
            print(line)

m = Matrix(3, 6)
m.print()

class Cell:
    def __init__(self, pos, num, text, color=None):
        self.num = num
        self.text = text
        self.color = color

class Grid:
    """Defines a n x m grid"""
    def __init__(self, pos=(0, 0), n=4, m=6, d=40):
        self.pos = pos
        self.n = n
        self.m = m
        self.d = d
        print(self)


    def draw(self):
        """Draw the grid."""
        x0, y0 = self.pos
        x1 = x0 + self.m * self.d
        y1 = y0 + self.n * self.d

        for x in range(x0, x1+1, self.d):
            line((x, y0), (x, y1))

        for y in range(y0, y1+1, self.d):
            line((x0, y), (x1, y))

    def inside(self, x, y):
        """True if (x, y) is inside the grid."""
        x0, y0 = self.pos
        x1 = x0 + self.m * self.d
        y1 = y0 + self.n * self.d

        return x0 < x < x1 and y0 < y < y1
        
    def index(self, x, y):
        """Return the index (i, j) of the cell."""
        x0, y0 = self.pos
        y1 = y0 + self.n * self.d
        if self.inside(x, y):
            j = int((x - x0) // self.d)
            i = int((y1 - y) // self.d)
            return i, j
        else:
            return None
        
    def __str__(self):
        """Return a string description of the grid."""
        return f'Grid({self.n}, {self.m})'



if __name__ == '__main__':
    setup(600, 400)
    s = Screen()
    tracer(0)
    up()

    status = Text((-280, -180), 'status')

    grid = Grid((-200, -100))
    grid.draw()

    grid2 = Grid((100, -100), 1, 4)
    grid2.draw()

    def click(x, y):
        if grid.inside(x, y):
            s = str(grid.index(x, y))
        if grid2.inside(x, y):
            s = str(grid2.index(x, y))

        status.text = s
        clear()
        status.draw()
        grid.draw()
        grid2.draw()

    s.onclick(click)
    listen()
    done()
    
