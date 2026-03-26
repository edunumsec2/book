"""
tp10 - typographier

Nom : 
Classe :
Date :

- Nommez ce fichier : tp10_classe_prenom (minuscules, sans accents)

Créez une image avec 2 parties : 
- Nuage de mots (10+ mots)
- Poésie (5+ lignes)

- Utilisez différents polices, tailles, couleurs
- Déposez sur Moodle les 3 fichiers (py, eps, jpg)
"""
from turtle import *
from tkinter import *

w, h = 600, 400
Screen().setup(width=w+40, height=h+40)
up()

def rectangle(p, d, e, text):
    goto(p)
    write(text, font=('Arial', 12))
    down()
    for i in range(2):
        forward(d)
        left(90)
        forward(e)
        left(90)
    up()
     
rectangle((-w/2, -h/2), w/2, h, 'Nuage de mots')
rectangle((0, -h/2), w/2, h, 'Poésie')

...

Screen().getcanvas().postscript(file='tp10.eps')
done()