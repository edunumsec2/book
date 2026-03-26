from turtle import *

shape('classic')
speed(1)
up()

x = -280
y = 180
d = 20
sep = ' '
end = '\t'
f = ('Courier', d)

def _print(*args):
    global x, y, d
    goto(x, y)
    for s in args:
        write(s, font=f, move=True)
        write(sep, font=f, move=True)
    y -= d
    
_print('hello', 123)
_print('world')
_print("c'est \"bon\"")
_print(r"c'est \"bon\"")

done()

    