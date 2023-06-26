"""
lib

"""
from turtle import *

def line(p, q):
    """Dessine une ligne entre les points p et q."""
    goto(p)
    down()
    goto(q)
    up()
    
def dist(p, q):
    """Retourne la distance entre les points p et q."""
    d = (p[0]-q[0])**2 + (p[1]-q[1])**2
    return d ** 0.5

def cross(p, q):
    ...

    
if __name__ == '__main__':
    p = 0, 0
    q = 200, 100
    line(p, q)
    print(dist(p, q))