#  Niveau d'un jeu vidéo
from turtle import *
from random import *
from tkinter import *
import io


def exporter():
    # Exporte en format EPS et PS
    # le format PS est ensuite converti en PNG et JPG
    Screen().getcanvas().postscript(file='file.eps')
    Screen().getcanvas().postscript(file='outputname.ps')


def niveau():
    # Ecriture du niveau en bas à gauche de l'image
    color("black")
    write("Niveau 1", font=("Times", 20, "bold"))
    exporter()


def repositionnement_fin():
    # Repositionnement de la tortue pour régler les derniers détails
    left(90)
    forward(250)
    right(90)
    forward(670)
    niveau()


def plateforme_piques():
    # Plateformes qui se trouvent au-dessus des piques
    down()
    width(5)
    color("blue")
    forward(100)
    left(90)
    up()
    forward(70)
    right(90)
    forward(70)
    down()
    color("red")
    forward(100)
    up()
    repositionnement_fin()


def triangle_drapeau():
    # drap du drapeau
    fillcolor("red")
    begin_fill()
    right(120)
    forward(50)
    right(120)
    forward(50)
    right(120)
    forward(50)
    end_fill()
    backward(32)
    up()
    right(90)
    forward(5)
    write("WIN")


def baton_drapeau():
    # Baton du drapeau
    forward(250)
    right(90)
    forward(75)
    left(90)
    width(3)
    forward(100)


def drapeau():
    # Création du drapeau à atteindre
    baton_drapeau()
    triangle_drapeau()
    width(1)
    backward(5)
    right(90)
    forward(68)
    right(90)
    forward(75)
    right(90)
    forward(80)
    left(90)
    forward(50)
    plateforme_piques()


def replacement_piques():
    # Repositionne la tortue à la fin des placements de piques
    left(90)
    forward(250)
    right(90)


def piques():
    # Dessine les piques
    fillcolor("gray")
    for i in range(6):
        begin_fill()
        for x in (60, 240, 240):
            left(x)
            forward(70)
        end_fill()
        backward(70)
        right(180)
    replacement_piques()
    mur()
    left(90)
    drapeau()


def jambes():
    # Dessine les jambes du joueur
    left(45)
    width(5)
    forward(50)
    right(45)
    forward(50)
    backward(50)


def torse():
    # Dessine le torse du joueur
    left(90)
    width(10)
    forward(40)


def bras():
    # Dessine les bras du joueur
    width(3)
    right(135)
    forward(50)
    backward(50)
    left(270)
    forward(50)
    backward(50)
    right(45)


def tete():
    # Dessine la tête du joueur
    fillcolor("black")
    begin_fill()
    left(180)
    circle(20)
    end_fill()
    up()
    left(90)
    backward(40)
    left(135)
    forward(50)
    left(135)


def player():
    # Dessine le joueur
    jambes()
    torse()
    bras()
    tete()
    color("black")

def rectangle(a, b, couleur):
    fillcolor(couleur)
    begin_fill()
    for x in (a, b, a, b):
        forward(x)
        left(90)
    end_fill()

def brique():
    # Composition du mur (voir fonction Mur() ci-dessous)
    width(1)
    color("black")
    fillcolor("darkgoldenrod")
    begin_fill()
    forward(150)
    right(90)
    forward(50)
    right(90)
    forward(150)
    right(90)
    forward(50)
    end_fill()
    backward(50)
    right(90)


def mur():
    # Mur de Brique qui forme la plateforme où le joueur peut se déplacer
    for i in range(5):
        brique()


def replacement_mur():
    # Remets la tortue en haut du mur de briques
    left(90)
    forward(250)
    right(90)
    forward(150)


def plateforme():
    # Création de la plateforme de jeu pour le joueur
    mur()
    replacement_mur()
    player()
    forward(150)
    down()
    mur()
    replacement_mur()
    mur()
    replacement_mur()
    right(90)
    forward(250)
    left(90)
    piques()


def deplacement_plateforme():
    # déplace la tortue au début de la plateforme
    up()
    backward(440)
    right(90)
    backward(1190)
    right(90)
    backward(245)
    left(90)
    down()
    width(5)
    plateforme()


def arbre(h):
    # Dessiner un abre de hauteur h
    color("sienna")
    down()
    width(0.2 * h)
    sety(ycor() + h)
    dot(1.0 * h, "green")
    up()
    sety(ycor() - h)

def montagne(h, rayons, couleur='lime'):
    p = pos()       # mémoriser la position de départ
    arbre_pos = []  # liste des positions des arbres
    color(couleur)
    begin_fill()
    seth(55)
    for r in rayons:
        circle(-r, 90)
        arbre_pos.append(pos())
        forward(2*h)
        arbre_pos.append(pos())
        circle(r, 90)
        arbre_pos.append(pos())
    sety(-500)
    setx(p[0])
    goto(p)
    end_fill()

    for p in arbre_pos[:-1]:
        goto(p)
        arbre(h)

def nuage(taille):
    #Dessine un nuage avec une taille aléatoire
    seth(0)
    for x in ("darkgray", "darkgray","lightgray") :
        dot(taille * randint(2, 4), x)
        forward(1.7 * taille)
    left(90)
    forward(taille)
    left(90)
    forward(taille)
    for i in range(3):
        dot(taille * randint(2, 4), "lightgray")
        forward(1.8 * taille)


def nuages():
    # Dessine les nuages avec un espacement aléatoire entre eux
    # La taille des nuages est aléatoire aussi
    for i in range(3):
        nuage(30)
        setx(xcor() + 400)


def soleil(d=100, a=100, angle=45, n=3, couleur='yellow'):
    color(couleur)
    dot(d)
    seth(180)
    down()
    width(10)
    for i in range(n):
        forward(a)
        backward(a)
        left(angle)
    up()


def main():
    getscreen().bgcolor('black')
    getscreen().setup(width=1200, height=1000, startx=0, starty=0)

    seed(2)
    speed("fastest")
    #hideturtle()
    up()

    goto(-600, -500)
    rectangle(1200, 1000, 'cyan')

    goto(-400, 300)
    nuages()

    goto(400, 400)
    soleil()

    goto(-600, 200)
    montagne(30, (80, 50, 150, 90))
    goto(-600, 50)
    montagne(50, (80, 155, 150, 72), 'silver')

    goto(-600, -150)
    seth(0)
    pencolor('black')
    plateforme()

main()
done()
