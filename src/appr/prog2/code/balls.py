from turtle import *
from vec import *
from random import *
from time import *
tracer(0)

class Ball:
    def __init__(self, d=50, col='pink', mass=1):
        self.p = Vec(randint(-300, 300), randint(-200, 200))
        self.v = Vec(randint(-100, 100), randint(-100, 100))
        self.d = d
        self.mass = mass
        self.col = col
        self.t0 = time()

    def move(self):
        t = time()
        dt = t - self.t0
        self.t0 = t
        
        acc = q - self.p
        acc.normalize()
        self.v += acc * 0.5
        
        self.p += self.v * dt
        
        if not -300 < self.p.x < 300:
            self.v.x *= -1
        
        if not -200 < self.p.y < 200:
            self.v.y *= -1
        
    def draw(self):
        goto(self.p.x, self.p.y)
        dot(self.d, self.col)
        down()
        goto(q.x, q.y)
        up()
        
    def __str__(self):
        return f'Ball({self.p})'
      
up()
q = Vec()
hideturtle()
balls = []
for i in range(10):
    b = Ball()
    balls.append(b)
 
def f(x, y):
    global q
    q = Vec(x, y)

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