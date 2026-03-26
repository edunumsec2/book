"""
Dessine des images PixelArt

Ce module definit les fonctions:
- pixel(d, w, pen, fill)
- pixelart(image, palette, d, w, pen):
"""
from turtle import *


def pixel(d, w=1, pen='black', fill=None):
    """Dessine un carré de taille d.

    Arguments:
    d -- dimension d'un pixel
    w -- epaisseur de ligne (1)
    pen -- couleur de ligne (black)
    fill -- couleur de remplissage (None)
    """
    if pen:
        down()
        width(w)
        pencolor(pen)
    if fill:
        fillcolor(fill)
        begin_fill()
    for i in range(4):
        forward(d)
        right(90)
    if fill:
        end_fill()
    up()
    forward(d)


def pixelart(image, palette, d=20, w=1, pen='black'):
    """Dessine une image avec des pixels.

    Arguments:
    image -- tableau 2D avec les indices des couleurs
    palette -- table contenant les couleurs
    d -- dimension d'un pixel (20)
    w -- épaisseur de ligne (1)
    pen -- couleur de ligne ('black')
    """    
    for line in image:
        for i in line:
            pixel(d, w=w, pen=pen, fill=palette[i])
        backward(len(line)*d)
        right(90)
        forward(d)
        left(90)
        
if __name__ == '__main__':
    w = 600
    h = 400
    Screen().setup(width=w, height=h, startx=0, starty=0)
    tracer(0)
    up()

    palette = (None, 'black', 'yellow', 'white', 'red', )
    pikachu = ((1, 2, 2, 1),
               (3, 4, 2, 3),
               (2, 2, 2, 2),
               (2, 2, 2, 3))
    
    invader = ( (0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                (1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1),
                (1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1),
                (0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0))
    
    dot()
    pixelart(invader, ('white', 'black'))
    goto(-250, 150)
    pixelart(invader, ('white', 'red'), d=10)
    goto(-100, 150)
    pixelart(invader, ('red', 'blue'), d=10, pen=None)
    
    goto(100, 100)
    seth(45)
    pixelart(invader, ('yellow', 'blue'), d=10)
    seth(0)
    
    goto(-250, 0)
    pixelart(pikachu, palette)
    
    goto(-150, 0)
    pixelart(pikachu, palette, d=30, w=0)
    
    help(__name__)    
    Screen().getcanvas().postscript(file='pixelart.eps')
    update()
