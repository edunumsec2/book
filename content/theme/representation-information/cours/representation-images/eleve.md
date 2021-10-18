# Représentation des images


<!-- ````{role} prof
```{admonition} Suggestion de déroulé
:class: danger
Voilà un déroulé de cours pour cette section représentation des images : 
1. Activité image Bitmap
2. Activité Kirby
3. Présentation des images matricielles
4. Exercice sur les résolutions
5. Questionnaire d'auto-contrôle
```
```` 
-->

<!-- ## Les images matricielles

Depuis des siècles les humains gardent des traces de leur environnement sous forme d'images. Plus le temps passe, plus ces traces sont fidèles. On découvre par exemple la perspective autour du XV<sup>e</sup> siècle, les progrès en optique et en chimie permettent ensuite la création de la camera obscura et de la photographie argentique. Enfin l'informatique se développe permettant l'invention de la photographie numérique.

```{figure} media/camera_obscura.jpg
---
height: 16em
name: fig-repr-img-obscur
---
La camera obscura
```

### De la camera obscura à la caméra numérique

Mais alors, comment marche une caméra numérique ? Elle marche d'une manière très similaire à la camera obscura et aux appareils photographiques analogiques d'un point de vue optique. Imaginez une chambre noire pourvue d'un trou sur l'une de ses parois. La lumière venant de l'extérieur vient se projeter sur le mur opposé. 

Dans un appareil analogique, la paroi illuminée est recouverte d'une pellicule chimique photosensible qui permet de capturer l'image. La différence est que dans un appareil photo numérique cette paroi est recouverte d'une grille de capteurs électroniques photosensibles. Dans ce cas, l'image numérique ne sera rien d'autre que la collection des mesures de tous les capteurs à un temps précis. Comme ces mesures sont organisées sous forme de tableau, on parle souvent d'images matricielles. Plus le nombre de capteurs est grand, plus la résolution de cette image le sera aussi. -->

## Représentation d'une image noir et blanc

````{tabbed} Image
```{image} media/thuglife.png
:width: 300px
```
````
````{tabbed} Code
```{image} media/thuglife2.png
:width: 300px
```
````

Un bit est l'unité minimale d'information qu'un ordintaeur comprend : 1 ou 0, allumé ou éteint. L'image la plus simple qu'un ordinateur puisse afficher est constituée uniquement de noir et blanc. Ainsi, un bit pourrait être soit noir, soit blanc. 

````{role} prof
```{admonition} Suggestion d'activité
:class: caution
Voilà une [activité débranchée](https://maitre.edunumsec2.ch/content/theme/representation-information/activites/representation-images/bitmap/bitmap.html) faciitant l'introduction des notions de bits noirs et blancs pour représenter une image.
```
````

```{figure} media/bitmap1.png
---
name: fig-bitmap-1
height: 250px
width: 250px
---
Tous les pixels marqués d'un 1 s'affichent en blanc, tous ceux marqués d'un zéro s'affichent en noir. 
```

Ceci nous permet de construire des images simples, et d'une {glo}`resolution|résolution` très faible.

```{codeplay}
import turtle

ATuin = turtle.Turtle()
ATuin.hideturtle()
ATuin.speed(0)

def drawSquare(size, color=(1,1,1)):
    #ATuin.pencolor(color)
    ATuin.fillcolor(color)
    ATuin.begin_fill()
    for i in range(4):
        ATuin.forward(size)
        ATuin.right(90)
    ATuin.end_fill()
    ATuin.forward(size)

divtpl = lambda tpl : tuple(round(x/255.,2) for x in tpl)

def setColor(col):
    if isinstance(col,tuple) and len(col) == 3 :
        return divtpl(col)
    elif isinstance(col, (int, float)):
        if col > 1 and col < 255:
            grey = int(col)
            return divtpl((grey,)*3)
        elif col == 1 or col == 0:
            bw = 255 - int(col)*255
            return divtpl((bw,)*3)
        else:
            return divtpl((1,1,1))
    else:
        return divtpl((1,1,1))



def drawImg(mtrx, imgSize = 300):
    nb = max(len(mtrx), max([len(line) for line in mtrx]))
    pixSize = imgSize // nb
    ATuin.up()
    ATuin.setpos(-nb*pixSize//2,nb*pixSize//2)
    ATuin.down()
    for line in mtrx :
        for elmt in line:
            drawSquare(pixSize, setColor(elmt))
        ATuin.up()
        pos = ATuin.pos()
        ATuin.setpos(pos[0]-pixSize*len(line), pos[1]-pixSize)
        ATuin.down()

thuglife=[
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],      
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
      [0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,0],
      [0,0,0,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0],
      [0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   
]


mario=[
    [1,1,(255,0,0),(255,0,0),(255,0,0), (255,0,0),1,1],
    [1,1,(255,0,0),(255,0,0),(255,0,0),0,(255,0,0),1],
    [1,1,(252, 233, 142),(0,26,122),(252, 233,142),(0,26,122),1,1],
    [1,1,(252, 233, 142),(252, 233, 142),(118,55,18),(118,55,18),1,1],
    [(252, 233, 142),(255,0,0),(0,26,122),(255,0,0),(255,0,0),(0,26,122),(255,0,0),(252, 233, 142)],
    [1,1,(0,26,122),(0,26,122),(0,26,122),(0,26,122),1,1],
    [1,1,(0,26,122),(0,26,122),(0,26,122),(0,26,122),1,1],  
    [1,1,(118,55,18),1,1,(118,55,18),1,1]
]

luigi=[
    [1,1,(55,124,38),(55,124,38),(55,124,38), (55,124,38),1,1],
    [1,1,(55,124,38),(55,124,38),(55,124,38),0,(55,124,38),1],
    [1,1,(252, 233, 142),(0,26,122),(252, 233,142),(0,26,122),1,1],
    [1,1,(252, 233, 142),(252, 233, 142),(118,55,18),(118,55,18),1,1],
    [(252, 233, 142),(55,124,38),(0,26,122),(55,124,38),(55,124,38),(0,26,122),(55,124,38),(252, 233, 142)],
    [1,1,(0,26,122),(0,26,122),(0,26,122),(0,26,122),1,1],
    [1,1,(0,26,122),(0,26,122),(0,26,122),(0,26,122),1,1],  
    [1,1,(118,55,18),1,1,(118,55,18),1,1]
]

link=[
    [1,(55,124,38),(55,124,38),(55,124,38),(55,124,38),1,1,(128,128,128)],
    [1,1,(55,124,38),(55,124,38),(55,124,38),(55,124,38),1,(128,128,128)],
    [1,1,(250, 215, 73),1,(252, 233,142),1,1,(128,128,128)],
    [1,1,(252, 233, 142),(252, 233, 142),(240,134,131),(252, 233, 142),1,(128,128,128)],
    [(252, 233, 142),(55,124,38),(55,124,38),(55,124,38),(55,124,38),(55,124,38),(55,124,38),(252, 233, 142)],
    [1,1,(55,124,38),(55,124,38),(55,124,38),(55,124,38),1,(0,26,122)],
    [1,1,(121,91,67),(121,91,67),(121,91,67),(121,91,67),1,1],  
    [1,1,(118,55,18),1,1,(118,55,18),1,1]
]

guerrier=[
        [(190,190,190),0,0,0,0,0,0,0],
        [(190,190,190),0,0,(190,190,190),(190,190,190),0,0,0],
        [(192,95,38),0,(190,190,190),(190,190,190),(190,190,190),(190,190,190),0,0],
        [(192,95,38),0,(8,5,7),(190,190,190),(8,5,7),(8,5,7),0,0],
        [(8,5,7),(8,5,7),(8,5,7),(8,5,7),(8,5,7),(192,95,38),(192,95,38),0],
        [(192,95,38),0,(8,5,7),(8,5,7),(8,5,7),(192,95,38),(192,95,38),0],
        [(192,95,38),0,(8,5,7),(8,5,7),(8,5,7),(8,5,7),0,0],
        [(192,95,38),0,(8,5,7),0,0,(8,5,7),0,0],
]

tortuesninja1=[
    [1,1,1,(105,226,105),(105,226,105),(105,226,105),(59,132,86),1],
    [1,(31,44,80),(83,173,248),(83,173,248),1,(83,173,248),1,1],
    [1,(105,226,105),(105,226,105),(105,226,105),(105,226,105),(105,226,105),(105,226,105),(59,132,86)],
    [1,(160,86,61),(105,226,105),(105,226,105),(105,226,105),(238,128,167),(105,226,105),(59,132,86)],
    [(160,86,61),(160,86,61),(59,132,86),(160,86,61),(160,86,61),(160,86,61),1,1],
    [(160,86,61),(105,226,105),(59,132,86),(255,253,92),(243,166,59),(255,253,92),(59,132,86),1],
    [1,(160,86,61),(105,226,105),(243,166,59),(243,166,59),(243,166,59),1,1],
    [1,1,(105,226,105),1,1,(59,132,86),1,1]
]

tortuesninja2=[
    [1,1,1,(105,226,105),(105,226,105),(105,226,105),(59,132,86),1],
    [1,(116,45,82),(235,52,82),(235,52,82),1,(235,52,82),1,1],
    [1,(105,226,105),(105,226,105),(105,226,105),(105,226,105),(105,226,105),(105,226,105),(59,132,86)],
    [1,(160,86,61),(105,226,105),(105,226,105),(59,132,86),(59,132,86),(105,226,105),(59,132,86)],
    [(160,86,61),(160,86,61),(59,132,86),(160,86,61),(160,86,61),(160,86,61),1,1],
    [(160,86,61),(105,226,105),(59,132,86),(255,253,92),(243,166,59),(255,253,92),(59,132,86),1],
    [1,(160,86,61),(105,226,105),(243,166,59),(243,166,59),(243,166,59),1,1],
    [1,1,(105,226,105),1,1,(59,132,86),1,1]
]

homer=[
    [1,1,1,(255,253,92),(255,253,92),(255,253,92),1,1],
    [1,1,(255,253,92),(255,253,92),(255,253,92),(255,253,92),(255,253,92),1],    
    [1,1,(255,253,92),(255,253,92),1,(255,253,92),1,1],
    [1,1,(255,253,92),(247,205,175),(247,205,175),(247,205,175),(247,205,175),1],
    [1,1,(255,253,92),(247,205,175),(247,205,175),(247,205,175),(160,86,61),1],
    [1,0,0,0,0,0,(247,205,175),1],
    [(255,253,92),(255,253,92),(83,173,248),(83,173,248),(83,173,248),(83,173,248),(31,44,80),(243,166,59)],
    [1,1,(83,173,248),(83,173,248),1,(31,44,80),(31,44,80),1]
]


pikachu=[
      [0,60,60,0,0,0,0,60],
      [0,0,(252, 230, 84),(242,165,59),0,0,0, (242,165,59)],
      [0,0,0,(252, 230, 84),(252, 230, 84),(252, 230, 84),(252, 230, 84),(242,165,59)],
      [(242,165,59),(242,165,59),0,(252, 230, 84),1,(252, 230, 84),(252, 230, 84),1],
      [(242,165,59),(242,165,59),0,(234,52,79),(252, 230, 84),(252, 230, 84),(252, 230, 84),(242,165,59)],
      [0,(163,87,58),0,(252, 230, 84),(242,165,59),(242,165,59),(242,165,59),0],
      [0,(163,87,58),(252, 230, 84),(242,165,59),(252, 230, 84),(242,165,59),(252, 230, 84),0],
      [0,0,(252, 230, 84),(242,165,59),(163,87,58),(163,87,58),(242,165,59),0]
]     

kirby=[

      [0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0],
      [1,150,150,1,150,0,0,0,0,150,1,150,0,150,1,0],
      [1,0,1,150,0,0,0,0,0,0,150,0,0,0,150,1],
      [1,0,150,0,0,0,0,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,1,0,1,0,0,0,0,0,0,0,150,1],
      [1,150,0,0,1,0,1,0,0,0,0,0,0,150,1,0],
      [0,1,0,0,1,0,1,0,0,0,0,0,150,1,1,0],
      [0,1,150,0,0,0,0,0,150,150,0,0,0,150,1,0],
      [0,1,0,0,0,0,0,0,0,0,0,0,0,150,1,0],
      [0,1,150,0,0,1,0,0,0,0,0,0,0,1,0,0],
      [0,0,1,0,0,0,0,0,0,0,0,0,150,1,0,0],
      [0,0,1,150,0,0,0,0,0,0,0,150,1,150,1,0],
      [0,0,0,1,150,150,0,0,0,150,1,1,150,150,1,0],
      [0,0,0,0,1,1,1,1,1,1,1,150,150,150,1,0],
      [0,0,0,0,0,0,1,150,150,1,0,1,150,150,1,0],
      [0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0],

]

kirbycouleur=[

      [0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0],
      [1,(238,116,155),(238,116,155),1,(238,116,155),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(238,116,155),1,(238,116,155),(243,178,200),(238,116,155),1,0],
      [1,(243,178,200),1,(238,116,155),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(238,116,155),(243,178,200),(243,178,200),(243,178,200),(238,116,155),1],
      [1,(243,178,200),(238,116,155),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),1],
      [1,(243,178,200),(243,178,200),(243,178,200),1,(243,178,200),1,(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(238,116,155),1],
      [1,(238,116,155),(243,178,200),(243,178,200),1,(243,178,200),1,(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(238,116,155),1,0],
      [0,1,(243,178,200),(243,178,200),1,(243,178,200),1,(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(238,116,155),1,1,0],
      [0,1,(238,116,155),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(238,116,155),(238,116,155),(243,178,200),(243,178,200),(243,178,200),(238,116,155),1,0],
      [0,1,(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(238,116,155),1,0],
      [0,1,(238,116,155),(243,178,200),(243,178,200),1,(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),1,0,0],
      [0,0,1,(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(238,116,155),1,0,0],
      [0,0,1,(238,116,155),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(243,178,200),(238,116,155),1,(255,0,0),1,0],
      [0,0,0,1,(238,116,155),(238,116,155),(243,178,200),(243,178,200),(243,178,200),(238,116,155),1,1,(255,0,0),(255,0,0),1,0],
      [0,0,0,0,1,1,1,1,1,1,1,(255,0,0),(255,0,0),(255,0,0),1,0],
      [0,0,0,0,0,0,1,(255,0,0),(255,0,0),1,0,1,(255,0,0),(255,0,0),1,0],
      [0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0],

]

## source illustrations : https://johanvinet.tumblr.com/

===
alien=[
    
      [0,0,0,0,0,0,0,0,0,0,0],
      [0,0,1,0,0,0,0,0,1,0,0],
      [0,0,0,1,0,0,0,1,0,0,0],
      [0,0,1,1,1,1,1,1,1,0,0],
      [0,1,1,0,1,1,1,0,1,1,0],
      [1,1,1,1,1,1,1,1,1,1,1],
      [1,0,1,1,1,1,1,1,1,0,1],
      [1,0,1,0,0,0,0,0,1,0,1],
      [0,0,0,1,1,0,1,1,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0]
      ]


drawImg(alien)
```
*Conseil : à la place de alien, essayez mario, luigi, link, guerrier, tortueninja1, tortueninja2, homer, pikachu, kirby, kirbycouleur*

Un {glo}`pixel|pixel`, de l'anglais : **pic**ture **el**ement, est le composant minimal d'une image. C'est à dire que c'est la plus petite brique avec laquelle on construit une image sur un écran d'ordinateur, et donc dans sa mémoire. Dans notre exemple minimaliste, chaque pixel peut être soit noir, soit blanc, ce qui nous permet de construire une image.

````{admonition} Anecdote
:class: hint
[The Million Dollar Homepage](https://fr.wikipedia.org/wiki/The_Million_Dollar_Homepage) est un site web conçu en 2005 par Alex Tew, un étudiant anglais, dans le but de financer ses études supérieures. La page d'accueil est une grille de 1000 X 1000 pixels. Chaque pixel était vendu 1$ en tant qu'espace publicitaire. Ils ont tous été vendus...

```{figure} media/milliondollarhomepage.png
```
````

## Représentation d'une image en niveaux de gris

````{tabbed} Image
```{image} media/kirbygrey.png
:width: 300px
```
````
````{tabbed} Code
```{image} media/kirbygrey2.png
:width: 300px
```
````

La plupart des images sont représentées au format {glo}`matrice|matriciel`. Une image en niveau de gris sera ainsi généralement codée comme un tableau de valeurs correspondant à la {glo}`luminance|luminance` de chaque pixel. Les valeurs de luminance sont chacune déclarées comme un nombre allant de 0 à 255, correspondant respectivement au noir et au blanc. Pour encoder une image en niveaux de gris, chaque pixel nécessite dont 8 bits. 

```{figure} media/image_et_pixels.svg
---
name: fig-repr-img-pixel
---
Images monochrome, pixels et luminance.
```

Pour accéder à un pixel particulier, il faut en général définir à quelle ligne et à quelle colonne de l'image ce pixel correspond. Le pixel (0,0) correspondra normalement au pixel de la première ligne et de la première colonne.

```{admonition} Le saviez-vous ? 
:class: hint
Ce mode de fonctionnement est similaire à celui des tableurs pour lesquels il est possible d'accéder à la valeur d'une case en utilisant sa référence. On pourrait d'ailleurs utiliser le formatage conditionnel pour transformer un tableau de valeurs dans un tableur en image matricielle.
```

## Codage des couleurs

````{tabbed} Image
```{image} media/kirbycolor.png
:width: 300px
```
````
````{tabbed} Code
```{image} media/kirbycolor2.png
:width: 500px
```
````

En peinture, pour obtenir toutes les couleurs de l'arc-en-ciel, on utilise un mélange de magenta, de cyan et de jaune, c'est ce que l'on appelle la {glo}`synthsoustractive|synthèse soustractive` : en ajoutant du pigment à une surface, une partie du spectre lumineux est soustrait. Pour faire la même chose en informatique, on utilisera également trois couleurs, mais celles-ci seront le rouge, le vert et le bleu. Cela correspond à la {glo}`synthadditive|synthèse additive additif` : en allumant une LED rouge, j'ajoute de la lumière sur la partie du spectre lumineux correspondant.

```{figure} media/SyntheseAdd_pixels.svg
---
name: fig-repr-img-sys-pixel
---
Système additif et écran au microscope.
```

Chaque pixel d'une image couleur est donc représenté comme un mélange de ces trois couleurs et donc sous forme de trois entiers. Comme pour les images en niveaux de gris, ces entiers sont généralement représentés sur 8 bits. Pour représenter une image en couleur il faut donc 8 bits pour le niveau de rouge, 8 bits pour le niveau de vert, et 8 bits pour le niveau de bleu, donc 24 bits. 

[Dans cette animation](https://www.csfieldguide.org.nz/en/interactives/pixel-viewer/) vous pouvez zoomer sur chacun des pixels qui constituent l'image totale. Chaque pixel possède trois valeurs allant de 0 à 255. RGB signifie en anglais Red, Green, Blue. 

[Dans cette autre animation](https://csfieldguide.org.nz/en/interactives/colour-matcher/) vous pouvez jouer avec la valeur de Rouge, Vert, Bleu, pour créer une couleur finale. L'outil vous permet d'abord de jouer avec des couleurs codées en 24 bits, puis en 8 bits, ce qui illustre bien la précision qu'on arrive à atteindre avec 24 bits. 

## Les images vectorielles

<!-- TODO #13 @dasilvadds : Modifier le paragraphe suivant en changeant blablabla
 -->
Pour dessiner une image sur une feuille A4, on peut la diviser en grille et définir un niveau de gris pour chaque case, mais on peut aussi tout simplement de dessiner n'importe quelle figure, par exemple un trait d'un millimètre d'épaisseur allant d'un point A à un point B. De la même manière, en informatique, il est possible de représenter des images sous forme de grilles de pixels, comme nous l'avons vu, mais pas seulement. Il est en effet également possible de définir une image comme une collection d'objets graphiques (un segment, un carré, une ellipse...) sur un espace 2D, c'est ce que l'on appelle des images vectorielles. 

```{admonition} Micro-activité
:class: note
Saisissez le texte suivant dans un éditeur de texte et enregistrer le sous forme de fichier *.svg*. Il vous sera ensuite normalement possible d'ouvrir ce fichier avec un logiciel pour afficher les images.

	<svg width="100" height="100"  version="1.1" xmlns="http://www.w3.org/2000/svg">
	<circle cx="50" cy="50" r="40" stroke="black" stroke-width="2" fill="red"/>
	</svg>

Modifier le fichier afin de dessiner 4 carrés différents.
```

```{admonition} Aller plus loin
:class: note
Identifiez et listez les avantages et les inconvénients du format vectoriel en comparaison avec le système matriciel.
```

## Bonus

Une œuvre d'art numérique signée Andreas Gysin : 

https://play.ertdfgcvb.xyz/#/src/demos/doom_flame_full_color

<!-- ## Auto-contrôle

### Texte à trous

La résolution d'une image se calcule en {bl}`centimètres|>pixels|niveaux de gris`. La plupart des {bl}`courroies|>images|bananes` sont représentées au format {bl}`matrix|magique|>matriciel`. 

### Questions

```{question} Question
S'il faut 8 bits pour coder un chiffre entre 0 et 255, combien faut-il de bits pour coder un seul pixel d'une image couleur ? 
* {v}`24, car il y a trois fois 8 bits.`
* {f}`3, car il y a trois couleurs qui se mélangent.`
* {f}`765, car il faut multiplier 255 par 3.`
``` -->