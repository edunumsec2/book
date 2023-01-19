# Réutiliser -  `import`

Le mot-clé `import` permet d'importer un module déjà prêt à utiliser.
Vous pouvez vous-même créer des modules avec des fonctions utiles que vous pouvez réutiliser dans vos projets, ou partager avec d'autres personnes.

Pour qu'un module soit utile il faut :

- bien le documenter
- bien le tester
- le rendre le plus général possible

## Le nom d'un module

Dans Python, la variable spéciale `__name__` designe le nom du module (fichier code) actuel.

- si le module est executé comme programme principale, cette variable est égale à `'__main__'`
- si le module est importé par un autre programe, cette variable est égale au nom du module.

```{exercise}
Téléchargez les deux fichiers et exécutez les. Que constatez-vous ?
```

```{codeplay}
:file: mymodule.py
# Ce fichier s'appele mymodule.py
print(__name__)

if __name__ == '__main__':
    print('test de mymodule')
```

```{codeplay}
:file: main.py
# Ce fichier s'appele main.py
import mymodule
print(__name__)

if __name__ == '__main__':
    print('test de main')
```

Quand vous executé `mymodule` vous devrez obtenir

``` text
__main__
test de mymodule
```

Quand vous executé `main`  qui importe `mymodule` vous devrez obtenir

``` text
mymodule
__main__
test de main
```

Vous constatez que :

- la partie test est seulement executé quand le fichier est exécuté comme principal
- le nom du module est alors `'__main__'`
- quand le module est importé, `__name__` est égale au nom du fichier
- la partie test n'est pas exécuté

## PixelArt

Le module `pixelart` definit deux fonctions. La structure du fichier est:

- docstring qui explique le module
- définition des fonctions
- test des fonctions

Vous constaterez que:

- seulement 25% des lignes constitutent du code util
- 25% (autant que le code) constitue de la documentation
- 50% (la moitié) sert à tester le code

```{codeplay}
:file: pixelart.py
"""
Dessine des images PixelArt

Ce module definit les fonctions:
- pixel(d, w, pen, fill)
- pixelart(image, palette, d, w, pen):
"""
from turtle import *


def pixel(d, w=1, pen='black', fill=None):
    """Dessine un carré de taille d.

    Arguments:
    d -- dimension d'un pixel
    w -- epaisseur de ligne (1)
    pen -- couleur de ligne (black)
    fill -- couleur de remplissage (None)
    """
    if pen:
        down()
        width(w)
        pencolor(pen)
    if fill:
        fillcolor(fill)
        begin_fill()
    for i in range(4):
        forward(d)
        right(90)
    if fill:
        end_fill()
    up()
    forward(d)


def pixelart(image, palette, d=20, w=1, pen='black'):
    """Dessine une image avec des pixels.

    Arguments:
    image -- tableau 2D avec les indices des couleurs
    palette -- table contenant les couleurs
    d -- dimension d'un pixel
    w -- épaisseur de ligne (1)
    pen -- couleur de ligne ('black')
    """    
    for line in image:
        for i in line:
            pixel(d, w=w, pen=pen, fill=palette[i])
        backward(len(line)*d)
        right(90)
        forward(d)
        left(90)
        
if __name__ == '__main__':
    w = 600
    h = 400
    #Screen().setup(width=w, height=h, startx=0, starty=0)
    tracer(0)
    up()

    palette = (None, 'black', 'yellow', 'white', 'red', )
    pikachu = ((1, 2, 2, 1),
               (3, 4, 2, 3),
               (2, 2, 2, 2),
               (2, 2, 2, 3))
    
    invader = ( (0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0),
                (0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0),
                (0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0),
                (0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0),
                (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
                (1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1),
                (1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1),
                (0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0))
    
    dot()
    pixelart(invader, ('white', 'black'))
    goto(-250, 150)
    pixelart(invader, ('white', 'red'), d=10)
    goto(-100, 150)
    pixelart(invader, ('red', 'blue'), d=10, pen=None)
    
    goto(100, 100)
    seth(45)
    pixelart(invader, ('yellow', 'green'), d=10)
    seth(0)
    
    goto(-250, 0)
    pixelart(pikachu, palette)
    
    goto(-150, 0)
    pixelart(pikachu, palette, d=30, w=0)
    
    #help(__name__)    
    #Screen().getcanvas().postscript(file='pixelart.eps')
    update()
```

## Docstring

Le **docstring** au début du module et dans chaque fonction est utilisé par Python pour produire la documetation help. Un docstring est une chaîne de caractères multiligne, entourés de triples guillemets doubles (`"""`).

### Documenter un module

La documentation pour un module est le premier élément du fichier code. Il a la forme suivante:

``` text
"""
Description en une ligne
    (ligne vide)
Explication détaillée du module en plusieurs lignes
"""
```

### Documenter une fonction

Le docstring pour une fonction suit immédiatement la ligne de définition de fonction. Il explique en une ligne l'essentiel de ce que fait la fonction.
Il explique ensuite la signification de chaque argument.
Le nom de l'argument et son explication sont séparé par `--`.

``` text
"""Description en une ligne
    (ligne vide)
Arguments:
d -- explication de l'argument d
e -- explication de ...
"""
```

### Afficher Help

La fonction `help(module)` dans la console permet d'afficher la documentation sur un module

```{exercise}
Téléchargez le module `pixelart` exécutez le code suivant dans la console.
```

``` text
import pixelart
help(pixelart)
```

Vous devriez obtenir ceci.

``` text
Help on module pixelart:

NAME
    pixelart - Dessine des images PixelArt

DESCRIPTION
    Ce module definit les fonctions:
    - pixel(d, w, pen, fill)
    - pixelart(image, palette, d, w, pen):

FUNCTIONS
    pixel(d, w=1, pen='black', fill=None)
        Dessine un carré de taille d.
        
        Arguments:
        d -- dimension d'un pixel
        w -- epaisseur de ligne (1)
        pen -- couleur de ligne (black)
        fill -- couleur de remplissage (None)
    
    pixelart(image, palette, d=20, w=1, pen='black')
        Dessine une image avec des pixels.
        
        Arguments:
        image -- tableau 2D avec les indices des couleurs
        palette -- table contenant les couleurs
        d -- dimension d'un pixel (20)
        w -- épaisseur de ligne (1)
        pen -- couleur de ligne ('black')
```

## Ligne polygonale

Une fonction puissante peut être très compacte, si bien réfléchie.
La fonction `polyline()` comporte 11 paramètres, pourtant la définition de la fonctions contient seulement 28 lignes de code.

```{codeplay}
:file: polyline.py
"""
Dessine une ligne polygonale.

Cette ligne polygonale est définie par un tuple de points.
Les caractéristiques suivantes sont configurables:
- courbe ouverte ou fermée,
- dot, numéro ou coordonnées dans les sommets,
- couleur et épaisseur de ligne,
- couleur de remplissage,
- déplacement de la courbe,
- changement d'echèlle (séparément pour x et y).
"""
from turtle import *


def polyline(points, pos=(0, 0), size=(1, 1), w=1, pen='black', fill=None,
             dots=False, numbered=False, i=0, coords=False, closed=True):
    """Dessine une ligne polygonale définie par un tuple de points.

    Arguments:
    points -- tuple de points (x, y)
    pos -- position de déplacement (0, 0)
    size -- facteur d'échelle (1, 1)
    w -- epaisseur de ligne (1)
    pen -- couleur de ligne ('black')
    fill -- couleur de remplissage (None)
    dots -- ajoute des points dans les sommets (False)
    coords -- ajoute des coordonnées dans les sommets (False)
    numbered -- ajoute un numéro dans les sommets (False)
    i -- numéro de départ (0)
    closed -- referme la ligne polygonale (True)
    """
    
    width(w)
    x = pos[0]+points[0][0]*size[0]
    y = pos[1]+points[0][1]*size[1]
    goto(x, y)        # aller au premier point
    
    if fill:
        begin_fill()  
    if closed:
        points += (points[0],)
    for p in points:
        x = pos[0]+p[0]*size[0]
        y = pos[1]+p[1]*size[1]
        if pen:
            pencolor(pen)
            down()
        goto(x, y)
        if dots:
            dot()
        if numbered:
            color('black')
            write(i)
            i += 1
        if coords:
            color('black')
            write((int(x), int(y)))       
    if fill:
        fillcolor(fill)
        end_fill()
    up()


if __name__ == '__main__':
    w = 600
    h = 400
    #Screen().setup(width=w, height=h, startx=0, starty=0)
    tracer(0)
    
    house = ((0, 0), (12, 0), (12, 15), (30, 15), (30, 0),
             (50, 0), (50, 25), (25, 50), (0, 25))
    
    polyline(house, numbered=True, fill='skyblue')
    polyline(house, pos=(0, 60), fill=None, dots=True, pen=False, numbered=True)
    polyline(house, pos=(60, 120), fill='pink', dots=True, closed=False, pen='red')
    polyline(house, (80, -60), size=(3, 3), w=3, pen='lime', closed=False, coords=True)
    polyline(house, (80, -80), size=(3, -2), coords=True, fill='silver')
    polyline(house, (-250, -100), size=(4, 4), numbered=True, fill='gold')

    #help(__name__)
    #Screen().getcanvas().postscript(file='polyline.eps')
    update()
```

## Formes