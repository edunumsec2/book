from turtle import *
from vec import *
from form import *
from random import *
from time import *
tracer(0)



class Ball:
    def __init__(self, d=50, col='pink'):
        self.p = Vec(randint(-300, 300), randint(-200, 200))
        self.v = Vec(randint(-100, 100), randint(-100, 100))
        self.d = d
        self.col = col
        self.t0 = time()
        self.g = Vec(0, -200)
        self.wind = Vec(20, 0)
        
    def move(self):
        t = time()
        self.dt = t - self.t0
#         write(f'{dt:.3}', font=('Arial', 24))
        self.t0 = t
        
#         acc = Vec(0, 2)
#         acc.normalize()
#         self.v += acc * 0.01
        
        self.v += (self.g + self.wind) * self.dt
        self.p += self.v * self.dt
        
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
hideturtle()
b = Ball()
q = Vec()
 
def f(x, y):
    global b
    b.p = Vec(x, y)

s = getscreen()
s.onclick(f)
s.listen()
 
while True:
    clear()
    b.move()
    b.draw()
    goto(q.x, q.y)
    dot()
    rectangle((-300, -200), (600, 400))
    write(b.dt, font=('Arial', 12))
    update()

done()

if __name__ == '__main__':
    print(123)

    