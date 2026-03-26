"""
Dessine une ligne polygonale.

Cette ligne polygonale est définie par un tuple de points.
Les caractéristiques suivantes sont configurables:
- courbe ouverte ou fermée,
- dot, numéro ou coordonnées dans les sommets,
- couleur et épaisseur de ligne,
- couleur de remplissage,
- déplacement de la courbe,
- changement d'echèlle (séparément pour x et y).
"""
from turtle import *


def polyline(points, pos=(0, 0), size=(1, 1), w=1, pen='black', fill=None,
             dots=False, numbered=False, i=0, coords=False, closed=True):
    """Dessine une ligne polygonale définie par un tuple de points.

    Arguments:
    points -- tuple de points (x, y)
    pos -- position de déplacement (0, 0)
    size -- facteur d'échelle (1, 1)
    w -- epaisseur de ligne (1)
    pen -- couleur de ligne ('black')
    fill -- couleur de remplissage (None)
    dots -- ajoute des points dans les sommets (False)
    coords -- ajoute des coordonnées dans les sommets (False)
    numbered -- ajoute un numéro dans les sommets (False)
    i -- numéro de départ (0)
    closed -- referme la ligne polygonale (True)
    """
    
    width(w)
    x = pos[0]+points[0][0]*size[0]
    y = pos[1]+points[0][1]*size[1]
    goto(x, y)        # aller au premier point
    
    if fill:
        begin_fill()  
    if closed:
        points += (points[0],)
    for p in points:
        x = pos[0]+p[0]*size[0]
        y = pos[1]+p[1]*size[1]
        if pen:
            pencolor(pen)
            down()
        goto(x, y)
        if dots:
            dot()
        if numbered:
            color('black')
            write(i)
            i += 1
        if coords:
            color('black')
            write((int(x), int(y)))       
    if fill:
        fillcolor(fill)
        end_fill()
    up()


if __name__ == '__main__':
    w = 600
    h = 400
    Screen().setup(width=w, height=h, startx=0, starty=0)
    tracer(0)
    
    house = ((0, 0), (12, 0), (12, 15), (30, 15), (30, 0),
             (50, 0), (50, 25), (25, 50), (0, 25))
    
    polyline(house, numbered=True, fill='skyblue')
    polyline(house, pos=(0, 60), fill=None, dots=True, pen=False, numbered=True)
    polyline(house, pos=(60, 120), fill='pink', dots=True, closed=False, pen='red')
    polyline(house, (80, -60), size=(3, 3), w=3, pen='lime', closed=False, coords=True)
    polyline(house, (80, -80), size=(3, -2), coords=True, fill='silver')
    polyline(house, (-250, -100), size=(4, 4), numbered=True, fill='gold')
         
    help(__name__)
    Screen().getcanvas().postscript(file='polyline.eps')
    update()