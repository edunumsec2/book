#  Niveau d'un jeu vidéo
from turtle import *
from random import *
from tkinter import *


def exporter():
    # Exporte en format EPS
    Screen().getcanvas().postscript(file='file.eps')


def niveau(n):
    # Affiche le niveau en bas à gauche de l'image
    goto(-580, -380)
    color('black')
    write('Niveau ' + str(n), font=('Times', 20, 'bold'))
    exporter()


def plateforme(col='red', a=100, w=5):
    # Dessine une plateforme en couleur
    seth(0)
    down()
    width(w)
    color(col)
    forward(a)
    up()


def drapeau(h=100, a=50, colour='red', text='WIN'):
    # Dessine un dreapeau avec un texte
    seth(90)
    down()
    forward(h)
    fillcolor(colour)
    triangle(-a)
    backward(a/2)
    color('black')
    write('  '+ text)
    up()


def triangle(a):
    # Dessine un triangle de taille a
    begin_fill()
    for i in range(3):
        forward(a)
        left(120)
    end_fill()


def piques(n=6, a=70):
    # Dessine n piques (triangles de taille a)
    down()
    fillcolor('gray')
    for i in range(n):
        triangle(a)
        forward(a)
    up()


def member(angle, a):
    # dessine une jambe ou un bras avec un angle et une longueur a
    seth(270 - angle)
    width(a/10)
    forward(a)
    backward(a)


def player(a=50, bras=(45, 45), jambes=(45, 90), col='black'):
    # Dessine le joueur avec tête, torse, 2 bras et 2 jambes
    color(col)
    down()
    seth(-90)
    width(a/5)
    dot(0.8 * a)
    forward(a/2)
    member(+bras[0], a)
    member(-bras[1], a)
    width(a/5)
    sety(ycor() - 0.8 * a)
    member(+jambes[0], a)
    member(-jambes[1], a)
    up()


def rectangle(a, b, col='darkgoldenrod'):
    # Dessine un rectangle
    fillcolor(col)
    begin_fill()
    for x in (a, b, a, b):
        forward(x)
        left(90)
    end_fill()


def mur(h=5, w=1, a=150, b=50):
    # Dessine un mur avec h x w briques
    width(1)
    pencolor('black')
    down()
    for j in range(w):
        for i in range(h):
            rectangle(a, b)
            sety(ycor()+b)
        sety(ycor() - h*b)
        forward(a)
    up()


def arbre(h):
    # Dessiner un abre de hauteur h
    color("sienna")
    down()
    width(0.2 * h)
    sety(ycor() + h)
    dot(1.0 * h, "green")
    up()
    sety(ycor() - h)


def montagne(h, rayons, col='lime'):
    # Dessine une montagne donné par une liste de rayons
    p = pos()       # mémoriser la position de départ
    arbre_pos = []  # liste des positions des arbres
    color(col)
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
    # Dessine un nuage avec une taille aléatoire
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
    # Dessine 3 nuages
    for i in range(3):
        nuage(30)
        setx(xcor() + 400)


def soleil(d=100, a=100, angle=45, n=3, col='yellow'):
    # Dessine un soleil avec n rayons dle longeurs a
    color(col)
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
    # Dessine les éléments du jeu videau
    getscreen().bgcolor('black')
    getscreen().setup(width=1200, height=800, startx=0, starty=0)

    seed(2)
    speed("fastest")
    #hideturtle()
    up()

    goto(-600, -400)
    rectangle(1200, 800, 'cyan')

    goto(500, 350)
    soleil()

    goto(-500, 300)
    nuages()

    goto(-600, 200)
    montagne(30, (80, 50, 150, 90))
    goto(-600, 50)
    montagne(50, (80, 155, 150, 72), 'silver')

    goto(-600, -400)
    seth(0)
    mur()

    goto(-450, -50)
    player()
    
    goto(-300, -400)
    mur(5, 2)

    goto(0, -400)
    piques()
    mur()

    goto(500, -150)
    drapeau()
    
    goto(100, -100)
    plateforme()
    goto(250, -50)
    plateforme('blue')

    niveau(1)
    exporter()
    print('done')
    
main()
done()
