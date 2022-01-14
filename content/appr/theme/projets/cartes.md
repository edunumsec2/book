# Poker

Le poker est une famille de jeux de cartes comprenant de nombreuses formules et variantes. Il se pratique à plusieurs joueurs avec un jeu généralement de cinquante-deux cartes et des jetons représentant les sommes misées.

## Les cartes

```{codeplay}
from turtle import *
up()
getscreen().bgcolor('teal')
speed(0)

class Card:
    couleurs = '♣♦♥♠'
    valeurs = 'A23456789XJQK'

    def __init__(self, couleur=0, val=1, pos=(0, 0), size=(50, 100), r=10, fill='white'):
        self.pos = pos
        self.size = size
        self.r = r
        self.fill = fill
        self.couleur = Card.couleurs[couleur]
        self.valeur = Card.valeurs[val]
        self.show()
        
    def outline(self):
        down()
        for d in self.size * 2:
            forward(d)
            circle(self.r, 90)
        up()
        
    def show(self):
        goto(self.pos)
        fillcolor(self.fill)
        begin_fill()
        self.outline()
        end_fill()
        sety(ycor() + 10)
        color('red')
        write(self.couleur, font=(None, 24))
        goto(self.pos[0] + self.size[0]/2, self.pos[1]+ 40)
        write(self.valeur, font=(None, 40), align='center')
        
Card()
Card(0, 1, (50, 20), fill='pink')

for i in range(13):
    Card(2, i, (-280 + i * 40, -190 + i * 5))
    
hideturtle()
```
