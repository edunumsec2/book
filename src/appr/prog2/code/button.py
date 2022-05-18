from turtle import *
hideturtle()
tracer(0)
up()
s = getscreen()
setup(600, 400)

# Documenting Python code
# https://realpython.com/documenting-python-code/

class Button:
    def __init__(self, pos, text, size=(80, 30), color='lightgray', align='center'):
        self.pos = pos
        self.size = size
        self.text = text
        self.color = color
        self.align = align
        self.draw()
        
    def draw(self):
        goto(self.pos)
        fillcolor(self.color)
        begin_fill()
        down()
        for x in self.size * 2:     # parcourir 2 fois longeur et hauteur
            forward(x)
            left(90)
        up()
        end_fill()
        x, y = self.pos
        w, h = self.size
        if self.align == 'center':
            goto(x+w/2, y+h/4)
        elif self.align == 'right':
            goto(x+w-h/4, y+h/4)
        else:
            goto(x+h/4, y+h/4)
        color('black')    
        write(self.text, font=('Arial', h//2), align=self.align)
        update()
        
    def __str__(self):
        return f'Button({self.text})'
    
    def inside(self, p):
        x, y = self.pos
        w, h = self.size
        
        return 0 < p[0]-x < w and 0 < p[1]-y < h
    
    
if __name__ == '__main__':
    
    b0 = Button((0,100), 'Play')
    b1 = Button((0, 50), 'Undo')
    b2 = Button((0,  0), 'Quit')

    def f(x, y):
        p = x, y
        for b in b0, b1:  
            if b.inside(p):
                print(b)
                if b.text == 'Quit':
                    bye()   
    
    s.onclick(f)
    s.listen()
    done()
