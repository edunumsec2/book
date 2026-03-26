"""
tp2 - définir

Nom : 
Classe :
Date :

- nommez ce fichier : tp2_classe_prenom (minuscules, sans accents)
- créez des fonctions pour les lettres de l'abc
- créer une fonction pour écrire votre nom
- récrivez l'abc et votre nom une deuxième fois plus petit    
- déposez sur Moodle :
    tp2_classe_prenom.py     (code)
    tp2_classe_prenom.eps    (image vectorielle)
    tp2_classe_preneom.jpg   (image)
"""
from turtle import *
from tkinter import *

d = 30

def A():
    dot()
    down()
    left(70)        # demi-montée
    forward(d)
    right(70)
    forward(0.6*d)  # trait du milieu
    backward(0.6*d)
    left(70)
    forward(d)      # partie haute
    right(140)
    forward(2*d)    # descente
    left(70)
    up()
    forward(d/2)    # avancer à la prochaine lettre


def ABC():
    A()
    A()
    A()
    
def prenom():
    ...

# afficher l'ABC et votre prénom
backward(280)
ABC()
prenom()

# afficher l'ABC et votre prénom avec une autre taille
d = 10
forward(100)
ABC()
prenom()

Screen().getcanvas().postscript(file='tp2.eps')
done()