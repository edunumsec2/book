# Représentation des images


## Les images matricielles

Depuis des siècles les humains gardent des traces de leur environnement sous forme d'images. Plus le temps passe, plus ces traces sont fidèles. On découvre par exemple la perspective autour du 15ème siècle, les progrès en optique et en chimie permettent ensuite la création de la camera obscura et de la photographie argentique. Enfin l'informatique se développe permettant l'invention de la photographie numérique.

```{figure} media/camera_obscura.jpg
---
height: 16em
name: fig-repr-img-obscur
---
La camera obscura
```

### De la camera obscura à la caméra numérique

Mais alors, comment marche une camera numérique ? Elle marche d'une manière très similaire à la camera obscura et aux appareils photographiques analogiques d'un point de vue optique. Imaginez une chambre noire pourvue d'un trou sur l'une de ses parois. La lumière venant de l'extérieur vient se projeter sur le mur opposé. 

Dans un appareil analogique, la paroi illuminée est recouverte d'une pellicule chimique photosensible ce qui permettra de capturer l'image. La différence est que dans un appareil photo numérique cette parois est recouverte d'une grille de capteurs électroniques photosensibles. Dans ce cas, l'image numérique ne sera rien d'autre que la collection des mesures de tous les capteurs à un temps précis. Comme ces mesures sont organisées sous forme de tableau, on parle souvent d'images matricielles. Plus le nombre de capteurs sera grand, plus la résolution de cette image le sera aussi.

### Représentation d'une image monochrome

La plupart des images sont représentées au format matriciel. Une image en niveau de gris sera ainsi généralement représenté comme un tableau de valeurs correspondant à la luminance de chaque sous élément de l'image ou pixel(**pic**ture **el**ement). Les valeurs de luminance sont chacune souvent représentée comme un nombre pouvant aller de 0 à 255, correspondant respectivement au noir et au blanc. 

```{figure} media/image_et_pixels.svg
---
name: fig-repr-img-pixel
---
Images monochrome, pixels et luminance.
```

Pour accéder à un pixel d'une image, il faut en général définir à quelle ligne et à quelle colonne de l'image ce pixel correspond. Le pixel (0,0) est correspondra normalement au pixel de la première ligne et de la première colonne.

```{admonition} Note
Ceci est très semblable au fonctionnement des tableurs pour lesquels il est possible d'accéder à la valeur d'une case en utilisant sa référence. On pourrait d'ailleurs utiliser le formatage conditionnel pour transformer un tableau de valeurs dans un tableur en image matricielle.
```

### Codage des couleurs

En peinture, pour obtenir toutes les couleurs de l'arc-en-ciel, on utilise un mélange de magenta, de cyan et de jaune, c'est ce que l'on appelle le système soustractif (en ajoutant du pigment à une surface, une partie du spectre lumineux est soustrait). Pour faire la même chose en informatique, on utilisera également trois couleurs, mais celle-ci seront le rouge, le vert et le bleu. Cela correspond au système additif (en allumant une LED rouge, j'ajoute de la lumière sur la partie du spectre lumineux correspondant).

```{figure} media/SyntheseAdd_pixels.svg
---
name: fig-repr-img-sys-pixel
---
Système additif et écran au microscope.
```

Chaque pixel d'une image couleur est donc représenté comme un mélange de ces trois couleurs et donc sous forme de trois entiers. Comme pour les images en niveaux de gris, ces entiers sont généralement représentés sur 8 bits.

## Les images vectorielles

Pour dessiner une image sur une feuille A4, on peut la diviser en grille et définir un niveau de gris pour chaque case, mais on peut aussi tout simplement de dessiner n'importe quelle figure, par exemple un trait d'un millimètre d'épaisseur allant d'un point A à un point B. De la même manière, en informatique, il est possible de représenter des images sous forme de grilles de pixels, comme nous l'avons vu, mais pas seulement. Il est en effet également possible de définir une image comme une collection d'objets graphiques (un segment, un carré, une ellipse...) sur un espace 2D, c'est ce que l'on appelle des images vectorielles. 

```{admonition} Exercice 1
Saisissez le texte suivant dans un éditeur de texte et enregistrer le sous forme de fichier *.svg*. Il vous sera ensuite normalement possible d'ouvrir ce fichier avec un logiciel pour afficher les images.

	<svg width="100" height="100"  version="1.1" xmlns="http://www.w3.org/2000/svg">
	<circle cx="50" cy="50" r="40" stroke="black" stroke-width="2" fill="red"/>
	</svg>

Modifier le fichier afin de dessiner 4 carrés différents.
```

```{admonition} Exercice 2
Identifier les avantages et les inconvénients du format véctoriel en comparasion avec le système matriciel.
```

