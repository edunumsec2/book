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


def colorier_montagne_PP():
    # Fait le contour des montagnes pour les colorier
    right(3)
    forward(435)
    left(90)
    forward(1183)
    left(90)
    forward(440)
    end_fill()
    deplacement_plateforme()


def feuillage():
    # Crée le feuillage des arbres du premier plan
    color("green")
    up()
    left(90)
    forward(7)
    for i in range(8):
        right(45)
        dot(40)
        forward(15)
    right(90)


def arbre_PP(angle):
    # Dessine les arbres du premier plan
    color("sienna")
    right(angle)
    up()
    forward(20)
    down()
    width(30)
    forward(50)
    feuillage()
    up()
    backward(70)
    left(angle)
    color("silver")
    width(10)
    down()


def montagne_PP():
    # Dessine les montagnes en premier plan
    color("silver")
    down()
    width(10)
    left(38)
    for x in (80, 110, 62, 97):
        circle(x, 90)
        arbre_PP(128)
        forward(50)
        circle(-x, 90)
        if x == 97:
            left(145)
        else:
            arbre_PP(38)
    colorier_montagne_PP()


def colorier_montagne_AP():
    # Fais les contours des montagnes en arrière-plan pour pouvoir les colorier
    width(1)
    right(3)
    forward(637)
    left(90)
    forward(1190)
    left(90)
    forward(640)
    end_fill()
    up()
    backward(200)
    begin_fill()
    montagne_PP()


def replacement_montagne_AP():
    # Replacement sur les bordures avant de créer les montagnes d'arrière-plan
    up()
    left(45)
    forward(93)
    right(90)
    forward(300)
    right(180)
    begin_fill()
    montagne_AP()


def arbre_AP(angle):
    # Dessine les arbres d'arrière-plan(=AP)
    color("sienna")
    right(angle)
    forward(30)
    dot(20, "green")
    up()
    backward(30)
    left(angle)
    color("limegreen")
    down()


def montagne_AP():
    # Dessine les montagnes d'arrière-plan
    color("limegreen")
    down()
    width(5)
    left(38)
    for x in (100, 45, 150, 72):
        circle(x, 90)
        arbre_AP(128)
        forward(50)
        arbre_AP(128)
        circle(-x, 90)
        if x == 72:
            left(145)
        else:
            arbre_AP(38)
    colorier_montagne_AP()


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


def soleil():
    # Dessine un soleil à 3 rayons
    seth(0)
    color("yellow")
    begin_fill()
    circle(50)
    end_fill()
    left(90)
    forward(50)
    left(90)
    down()
    width(10)
    for i in range(3):
        forward(100)
        backward(100)
        left(45)


def main():
    # fixe la couleur de fond
    getscreen().bgcolor('black')
    seed(2)
    speed("fastest")
    #hideturtle()
    up()
    # dessine l'arrière-fond du niveau
    goto(-600, -500)
    rectangle(1200, 1000, 'cyan')

    goto(-400, 200)
    nuages()

    goto(300, 200)
    soleil()

    replacement_montagne_AP()


main()
done()
