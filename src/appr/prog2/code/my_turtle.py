from turtle import *

def line(p, q):
    goto(p)
    down()
    goto(q)
    up()


from random import *
tracer(0)

class Vec2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vec2d(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)
    
    def __mul__(self, k):
        return Vec2d(self.x * k, self.y * k)

    def __str__(self):
        return f'Vec2d({self.x}, {self.y})'

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def normalize(self):
        d = abs(self)
        self.x /= d
        self.y /= d

class Ball:
    def __init__(self, d=50, col='pink'):
        self.p = Vec2d(randint(-300, 300), randint(-200, 200))
        self.v = Vec2d(randint(-1, 1), randint(-1, 1))
        self.d = d
        self.col = col
        
    def move(self):
        acc = q - self.p
        acc.normalize()
        self.v += acc * 0.01
        
        
        self.p = self.p + self.v
        
        if not -300 < self.p.x < 300:
            self.v.x *= -1
        
        if not -200 < self.p.y < 200:
            self.v.y *= -1
        
    def draw(self):
        goto(self.p.x, self.p.y)
        dot(self.d, self.col)
        
    def __str__(self):
        return f'Ball({self.p})'
      
up()
q = Vec2d()
hideturtle()
balls = []
for i in range(10):
    b = Ball()
    balls.append(b)
 
def f(x, y):
    global q
    q = Vec2d(x, y)

s = getscreen()
s.onclick(f)
s.listen()
 
while True:
    clear()
    for b in balls:
        b.move()
        b.draw()
    goto(q.x, q.y)
    dot()
    update()

done()

if __name__ == '__main__':
    p = (20, 30)
    q = (200, 200)
    line(p, q)
    done()