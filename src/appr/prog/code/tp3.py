"""
tp3 - répéter

Nom : 
Classe :
Date :

- nommez ce fichier : tp3_classe_prenom (minuscules, sans accents)
- créez 5+ fonctions qui utilisent la répétion
- utilisez la variable d (distance) pour vos déplacements
- composez une scène de jeu vidéo (pacman, tetris, minecraft, etc.
- utilisez de la couleur
- déposez sur Moodle :
    tp3_classe_prenom.py     (code)
    tp3_classe_prenom.eps    (image vectorielle)
    tp3_classe_preneom.jpg   (image)
"""
from turtle import *
from tkinter import *

d = 20

def pacman():
    down()
    left(45)
    forward(d)
    left(90)
    circle(d, 270)
    left(90)
    forward(d)
    right(135)   
    for i in range(5):
        up()
        forward(d)
        dot(d/5)

# ajoutez vos fonctions ici

pacman()



# remplacer avec tp3_classe_prenom
Screen().getcanvas().postscript(file='tp2.eps')
done()