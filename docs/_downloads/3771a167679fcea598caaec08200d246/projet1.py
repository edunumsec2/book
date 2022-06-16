# Niveau d'un jeu vidéo
from turtle import *
from random import *
from tkinter import *
import io

def Exporter():
    #Exporte en format EPS et PS, le format PS est ensuite converti en PNG et JPG
    Screen().getcanvas().postscript(file='file.eps')
    Screen().getcanvas().postscript(file='outputname.ps')
    
def Niveau():
    #Ecriture du niveau en bas à gauche de l'image
    color("black")
    write("Niveau 1", font=("Times",20, "bold"))
    Exporter()
    
def RepositionnementFin():
    #Repositionnement de la tortue pour régler les derniers détails
    left(90)
    forward(250)
    right(90)
    forward(670)
    Niveau()
    
def PlateformePiques():
    #Plateformes qui se trouvent au-dessus des piques
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
    RepositionnementFin()
    
def TriangleDrapeau():
    #drap du drapeau
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
    
def BatonDrapeau():
    #Baton du drapeau
    forward(250)
    right(90)
    forward(75)
    left(90)
    width(3)
    forward(100)
    
def drapeau():
    #Création du drapeau à atteindre
    BatonDrapeau()
    TriangleDrapeau()
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
    PlateformePiques()
    
def ReplacementPiques():
    #Repositionne la tortue à la fin des placements de piques 
    left(90)
    forward(250)
    right(90)

def piques():
    #Dessine les piques
    fillcolor("gray")
    for i in range(6):
        begin_fill()
        for x in (60, 240, 240):
            left(x)
            forward(70)
        end_fill()
        backward(70)
        right(180)
    ReplacementPiques()
    Mur()
    left(90)
    drapeau()
    
def jambes():
    #Dessine les jambes du joueur
    left(45)
    width(5)
    forward(50)
    right(45)
    forward(50)
    backward(50)
    
def torse():
    #Dessine le torse du joueur
    left(90)
    width(10)
    forward(40)
    
def bras():
    #Dessine les bras du joueur
    width(3)
    right(135)
    forward(50)
    backward(50)
    left(270)
    forward(50)
    backward(50)
    right(45)
    
def tete():
    #Dessine la tête du joueur
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
    
def Player():
    #Dessine le joueur
    jambes()
    torse()
    bras()
    tete()
    color("black")
    
def Brique():
    #Composition du mur (voir fonction Mur() ci-dessous)
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

def Mur():
    #Mur de Brique qui forme la plateforme où le joueur peut se déplacer
    for i in range(5):
        Brique()

def ReplacementMur():
    #Remets la tortue en haut du mur de briques
    left(90)
    forward(250)
    right(90)
    forward(150)
    
def Plateforme():
    #Création de la plateforme de jeu pour le joueur
    Mur()
    ReplacementMur()
    Player()
    forward(150)
    down()
    Mur()
    ReplacementMur()
    Mur()
    ReplacementMur()
    right(90)
    forward(250)
    left(90)
    piques()
    

def DeplacementPlateforme():
    #déplace la tortue au début de la plateforme 
    up()
    backward(440)
    right(90)
    backward(1190)
    right(90)
    backward(245)
    left(90)
    down()
    width(5)
    Plateforme()
    
def ColorierMontagnePP():
    #Fait le contour des montagnes pour les colorier
    right(3)
    forward(435)
    left(90)
    forward(1183)
    left(90)
    forward(440)
    end_fill()
    DeplacementPlateforme()
    
def feuillage():
    #Crée le feuillage des arbres du premier plan
    color("green")
    up()
    left(90)
    forward(7)
    for i in range(8) :
        right(45)
        dot(40)
        forward(15)
    right(90)
        
def arbrePP(angle):
    #Dessine les arbres du premier plan
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
    
def montagnePP():
    #Dessine les montagnes en premier plan
    color("silver")
    down()
    width(10)
    left(38)
    for x in (80, 110, 62, 97):
        circle(x,90)
        arbrePP(128)
        forward(50)
        circle(-x,90)
        if x == 97:
            left(145)
        else:
            arbrePP(38)
    ColorierMontagnePP()
    
def ColorierMontagneAP():
    #Fais les contours des montagnes en arrière-plan pour pouvoir les colorier
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
    montagnePP()
    
    
def ReplacementMontagneAP():
    #Replacement sur les bordures avant de créer les montagnes d'arrière-plan
    up()
    left(45)
    forward(93)
    right(90)
    forward(300)
    right(180)
    begin_fill()
    montagneAP()
    
def arbreAP(angle):
    #Dessine les arbres d'arrière-plan(=AP)
    color("sienna")
    right(angle)
    forward(30)
    dot(20, "green")
    up()
    backward(30)
    left(angle)
    color("limegreen")
    down()
    
def montagneAP():
    #Dessine les montagnes d'arrière-plan 
    color("limegreen")
    down()
    width(5)
    left(38)
    for x in (100, 45, 150, 72):
        circle(x,90)
        arbreAP(128)
        forward(50)
        arbreAP(128)
        circle(-x,90)
        if x == 72:
            left(145)
        else:
            arbreAP(38)
    ColorierMontagneAP()
    
    
def nuage(taille):
    #Dessine un nuage avec une taille aléatoire
    for x in ("darkgray", "darkgray","lightgray") :
        taille = randint(2,4)
        dot(26*taille, x)
        forward(50)
    left(90)
    forward(30)
    left(90)
    forward(50)
    for i in range(3):
        taille = randint(2,4)
        dot(30*taille, "lightgray")
        forward(50)

nuage(200)
done()
        
def soleil():
    #Dessine un soleil à 3 rayons
    fillcolor("yellow")
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
        
def nuages(espacement):
    #Dessine les nuages avec un espacement aléatoire entre eux
    #La taille des nuages est aléatoire aussi
    backward(800)
    left(90)
    forward(150)
    for i in range(3):
        espacement = 0*random()
        nuage(random())
        right(180)
        forward(400+espacement)
    backward(100)
    soleil()
    ReplacementMontagneAP()
    
def begin():
    #dessine les bordures du Niveau
    down()
    fillcolor("cyan")
    begin_fill()
    width(10)
    for x in (1200,1000,1200,1000):
        left(90)
        forward(x)
    end_fill()
    width(1)
    up()
    print(pos(), heading())
    done()
    nuages(randint(1,2))
    
def main():
    #Mets la tortue au bon endroit, permet de lancer le reste du code et fixe la couleur de fond
    getscreen().bgcolor('black')
    seed(2)
    speed("fastest")
    up()
    backward(600)
    right(90)
    forward(500)
    begin()
    
main()