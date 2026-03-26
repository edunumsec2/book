from turtle import *

hideturtle()
tracer(0)
d = 50
up()

def f(x):
    return 0.5*x + 2

def g(x):
    return 0.2 * x ** 2 - 3

def axis():
    for x in range(-300//d, 301//d):
        goto(x*d, 0)
        down()
        dot()
        write(x)
    up()
    
def tracer(f, c='red', bars=True, dots=True, value=True):
    color(c)
    for x in range(-300//d, 301//d):
        if bars:
            goto(x*d, 0)
            down()
            goto(x*d, f(x)*d)
            up()
        else:
            goto(x*d, f(x)*d)
            down()
        if dots:
            dot()
        if value:
            write(round(f(x), 1))

    
axis()
tracer(g)
tracer(f, bars=False)
update()
done()