from turtle import *
s = getscreen()
hideturtle()
tracer(0)
up()

class Button:
    def __init__(self, pos, text, size=(80, 40), color='lightgray', align='center'):
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

texts = ('AC', '+/-', '%', '÷', '7', '8', '9', '×', '4', '5',
         '6', '–', '1', '2', '3', '+', '0', '.', '=', '')

display = Button((-160, 80), '0', size=(320, 100), color='white', align='right')
    
buttons = []
for i in range(len(texts)):
    x = -160 + i%4 * 80
    y = 40 - i//4 * 40
    button = Button((x, y), texts[i])
    buttons.append(button)

number = 0
number1 = 0
op = ''

def f(x, y):
    global number, number2, op
    p = (x, y)
    for b in buttons:  
        if b.inside(p):
            if b.text in '0123456789':
                if number == 0:
                    number = int(b.text)
                else:
                    number = 10 * number + int(b.text)
                    
            elif b.text == 'AC':
                number = 0
            
            elif b.text == '+/-':
                number *= -1
            
            elif b.text in '÷×–+':
                number2 = number
                number = 0
                op = b.text
                
            elif b.text == '=':
                if op == '–':    
                    number = number2 - number
                elif op == '+':    
                    number = number2 + number
                elif op == '×':    
                    number = number2 * number
                elif op == '÷':    
                    number = number2 / number    
            
            display.text = str(number)
            display.draw()

s.onclick(f)
s.listen()
done()