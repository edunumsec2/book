from button import *

x0, y0, d = 160, 160, 40
history = []

class Board:
    def __init__(self, n=8, m=8):
        self.board = []
        for i in range (n):
            self.board.append([0] * m)
            
    def print(self):
        for line in self.board:
            print(*line)
            
board = Board()
board.print()


def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

def grid():
    for x in range(-x0, x0+1, d):
        ligne((x, -y0), (x, y0))

    for y in range(-y0, y0+1, d):
        ligne((-x0, y), (x0, y))

def f(x, y):
    if -x0 < x < x0 and -y0 < y < y0:
        x = x//d * d + d//2
        y = y//d * d + d//2
        goto(x, y)
        dot(d)
        
        i = (int(y)+y0) // d
        j = (int(x)+x0) // d
        if (i, j) not in history:
            history.append((i, j))
            print(history)
        
    if button0.inside((x, y)):
        clear()
        button0.draw()
        button1.draw()
        button2.draw()
        grid()
        
    if button2.inside((x, y)):
        print('quit')
        bye()

button0 = Button((200, 30), 'New')
button1 = Button((200, 0), 'Undo')
button2 = Button((200, -30), 'Quit')


grid()

s.onclick(f)
s.listen()
done()