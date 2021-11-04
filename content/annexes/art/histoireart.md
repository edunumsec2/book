# Histoire de l'art numérique

## Introduction

Établir une histoire de l'art *numérique* est problématique. Il est difficile, dans ce contexte, de donner une définition satisfaisante du concept *numérique*. Une définition trop large incluerait toute création artistique utilisant une forme de calcul comme paramètre fondamental de la réalisation de l'œuvre. Alors qu'une définition trop restreinte, du type "œuvre ayant été réalisée par un ordinateur" excluerait une part importante de la production du XX<sup>e</sup> siècle qui utilisait, par exemple, des instructions données à des imprimantes pour produire des œuvres *numériques*. 

Dans ce chapitre, nous appelons donc "art numérique" plus spécifiquement des productions utilisant un ordinateur, un programme, un algorithme, comme outil principal de création. 

Néanmoins, nous commencerons par une courte présentation de l'utilisation d'algorithmes de dessin dans des œuvres datant de plusieurs siècles. 

## Zellige 

"Le zellige (de l'arabe "petite pierre polie") est une mosaïque dont les éléments, appelés tesselles, sont des morceaux de carreaux de faïence colorés. Ces morceaux de terre cuite émaillée sont découpés un à un et assemblés sur un lit de mortier pour former un assemblage géométrique. Le zellige, utilisé principalement pour orner des murs ou des fontaines, est un composant caractéristique de l'architecture mauresque, originaire du Maroc 1,2,3, présent en Andalousie et dans de rares cas en Algérie et en Tunisie. Au Maroc, toutes les maisons traditionnelles en sont munies en signe décoratif 4,5, mais c'est aussi devenu le cas pour les maisons modernes." (*https://fr.wikipedia.org/wiki/Zellige*)

```{image} media/zellige.jpeg
:alt: By إيان - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=88836894
:align: center
```
Les artisans qui découpent les faïences connaissent par cœur un grand nombre de ces puzzles, ce qui leur permet de travailler directement sur la pierre sans passer par l'étape du dessin. Néanmoins, il existe sur Youtube un grand nombre de tutoriels qui expliquent étape par étape comment réaliser ce genre de dessins à l'aide d'un compas, d'une équerre, et d'un crayon. 

```{youtube} dLtV_GTCM6I
```
Le code Python ci-dessous, permet de créer un Zellige simplifié à partir d'hexagones, de carrés et de triangles imbriqués les uns dans les autres, aussi appelé ["pavage de Diane"](https://mathcurve.com/polyedres/pavagedediane/pavagedediane.shtml). 

```{codeplay}
import turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(1000)

def draw_square(size):
    for i in range(4):
        pen.forward(size)
        pen.left(90)

def draw_polygon(size):
    for i in range(6):
        draw_square(size)
        for i in range(2):
            pen.forward(size)
            pen.left(30)

def draw_line(size, count):
    for i in range(count):
        draw_polygon(size)
        pen.forward(size)
        for j in range(2):
            pen.left(30)
            pen.forward(size)
        pen.right(60)

def draw_tile(size, lines, cols):
    draw_line(size, cols)
    for i in range(lines - 1):
        if i % 2 == 0:
            for j in range(2):
                pen.forward(size)
                pen.left(90)
        else:
            pen.left(90)
            pen.forward(size)
            for j in range(3):
                pen.left(30)
                pen.forward(size)
            for j in range(3):
                pen.right(60)
                pen.forward(size)
            pen.left(90)
            pen.forward(size)
            pen.left(90)
        draw_line(size, cols)

pen.up()
pen.setposition(-300, 150)
pen.right(30)
pen.down()
draw_tile(20, 9, 11)
pen.hideturtle()
```

On retrouve ce type de motifs dans de nombreuses œuvres culturelles. Comme, par exemple, au Musée archéologique de Séville. 

```{image} media/pavagediane.jpeg
```

Comme on peut le voir, le programme ci-dessus n'exprime qu'une fraction de la complexité contenue dans les Zellige de la tradition de l'art géométrique arabe. Les compositions traditionnelles impliquent des répétitions périodiques de motifs très complexes, impliquant des entrelacements difficiles à reproduires. 

[Cet article](https://dl.acm.org/doi/pdf/10.1145/3064419?casa_token=alNKFW_UWasAAAAA:KuETyYndEmiMiN_ivaN8UkIAEBrvAlvlwZr8eY6qfZT9CVRK4J1J0EgxgvL7vykdjqPACmPd6MNX-Q) datant de 2017, écrit par deux chercheurs de l'université de Fès au Maroc, donne une idée de la subtilité d'un algorithme capable de générer ce genre de motifs. 

```{image} media/entrelacement2.jpeg
```

## Métier à tisser de Joseph Marie Jacquard 

Le métier à tisser développé par [Joseph Marie Jacquard](https://fr.wikipedia.org/wiki/Joseph_Marie_Jacquard) en 1801 à Lyon est un autre exemple de recoupement entre artisanat et mécanisation. 

L'exemple le plus simple de tissage est le damier. On utilise un fil blanc et un fil noir. Le fil blanc est déroulé verticalement, et à chaque ligne, le fil noir vient s'insérer perpendiculairement en passant dessus, dessous, dessus, dessous, et ainsi de suite. 

<!-- ```{codeplay}
import turtle
 
def draw_box(t,x,y,size,fill_color):
    t.penup() 
    t.goto(x,y)
    t.pendown()
    
    t.fillcolor(fill_color)
    t.begin_fill()
    
    for i in range(0,4):
        board.forward(size)
        board.right(90)
        
    t.end_fill()

    
def draw_chess_board():
    square_color = "black"
    start_x = 0 
    start_y = 0 
    box_size = 30 
    for i in range(0,8): 
        for j in range(0,8):
            draw_box(board,start_x+j*box_size,start_y+i*box_size,box_size,square_color)
            square_color = 'black' if square_color == 'white' else 'white'
        square_color = 'black' if square_color == 'white' else 'white'
        
board = turtle.Turtle()
draw_chess_board()
turtle.done()
``` 
-->

Si on veut accélérer le procédé, on utilise un métier à tisser, qui déroule un certain nombre de fils verticalement, et à chaque "ligne" on vient passer un fil horizontal représenté ci-dessus par le fil noir. 

Durant de nombreux siècles, les motifs qui ornaient les textiles étaient filés à la main à l'aide de métiers à tisser traditionnels. Pour créer des patterns compliqués, les artisans devaient actionner les poulies une par une pour soulever les fils qui allaient former le dessin. 

En 1801, [Joseph Marie Jacquard](https://fr.wikipedia.org/wiki/Joseph_Marie_Jacquard), s'inspirant de technologies déjà existantes, réalise le premier métier à tisser automatique suffisamment robuste pour alimenter une production industrielle. Le système repose sur l'utilisation de cartes perforées pour indiquer les endroits où les fils doivent être levés pour produire des motifs complexes jusqu'ici réalisés à la main. 


### En version "C'est pas Sorcier"

````{youtube} vtHJfb8TbK4
````

### Google Jacquard 

Aujourd'hui, Google développe un projet nommé ["Jacquard"](https://atap.google.com/jacquard/technology/), dont l'objectif est de créer des vêtements dont les fibres contiennent des composants électriques capables de véhiculer de l'information en étant connectés à d'autres appareils. 

````{youtube} qObSFfdfe7I
`````

Plotter drawing (1950's)
Teleprinter art
Adding randomness
Generative art
Input / Output transformations (ex : Kinect)
Augmented reality
Art critique (Paolo Cirio, James Bridle)