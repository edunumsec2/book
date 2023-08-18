(ens:repinfo:imagesnumeriques)=
# Images numériques

```{admonition} Notebook Jupyter
:class: warning
Attention, cette activité est à effectuer dans un notebook Jupyter. Les instructions dans les cellules codeplay ne sont pas exécutables en l'état. Une version .ipynb est disponible ci-dessous
```

[Version .ipynb](https://github.com/edunumsec2/book/blob/2e886527094630cbe0259d4c0849b92077aa0a00/src/ens/rep-info/activ/EncoderImages.ipynb)

La grotte de Lascaux est témoin d'une des premières tentatives de
l'humanité de figer des images sur un support matériel.

En termes de science informatique, il s'agit de **l'encodage d'une
image** sur un substrat rocheux à l'aide de peinture.

![lascaux](media/lascaux.jpg)

Les images, de nos jours, sont utilisées énormément pour les jeux vidéo,
la télévision, la réalité virtuelle.

Comment est‐ce qu'on fait pour les afficher concrètement sur un écran
?

## Comment coder une image

Une image peut être représentée sous la forme d'une grille de carrés,
ces carrés sont appelés des **pixels**.

Les pixels, ce sont des assemblages de petits points de différentes
couleurs, du vert, du bleu et du rouge, qu'on va allumer pour faire
croire à l'œil qu'il s'agit d'une couleur particulière.

Ils sont tellement petits que l'œil ne peut pas distinguer les trois
composantes de chaque couleur :

-   le rouge,
-   le vert,
-   le bleu.

Une image est donc un tableau en deux dimensions composé de points
élémentaires, des pixels.

Pour créer des tableaux et les transformer en image, il faut utiliser
des modules aditionnels, *des sortes d'extensions au langage* .
Nous allons utiliser 2 modules en particulier :

-   `numpy`
-   `matplotlib`

Numpy est une librairie destinée à manipuler des matrices ou tableaux
multidimensionnels ainsi que des fonctions mathématiques opérant sur ces
tableaux. Le module matplotlib regroupe un grand nombre de fonctions qui
servent à créer des graphiques et les personnaliser, elles sont
rassemblées dans le sous-module `pyplot`.

Les 2 lignes de code suivante servent à charger ces modules afin de
pouvoir utiliser leurs fonctionnalités.

**Vous devez impérativement exécuter la cellule suivante avant d'aller
plus loin**, sinon les instructions de ce Notebook ne fonctionneront
pas.

```{codeplay} 
import numpy as np
import matplotlib.pyplot as plt
```

## Trois types de «couleurs»

### Images en noir et blanc

Une image noir et blanc est une image ou chaque pixel peut avoir deux
valeurs:

-   0 = noir
-   1 = blanc

Pour créer des images dans la suite de ce notebook, nous allons
systématiquement procéder de la même manière, en 2 étapes :

1.  Créer une variable et lui affecter les données de notre image sous
    forme de tableau à 2 dimensions
2.  Afficher l'image

```{codeplay} 
# Créer une variable et lui affecter les données
twopixel = [[0,1]]

# Afficher l'image
img = plt.imshow(twopixel, cmap='gray')
```

Notre tableau est défini par une paire de crochets [] à l'intérieur
duquel chaque ligne de pixel est séparé par des virgules.
Chaque ligne est elle aussi définie par une paire de crochets [] à l'intérieur de laquelle les pixels sont également séparés par des virgules.

**Attention toutes les lignes doivent contenir le même nombre de
pixel.**

Si on souhaite ajouter une seconde ligne de pixel à l'exemple
précédent, il suffit d'écrire :

```{codeplay} 
# Créer une variable et lui affecter les données
twopixel = [[0,1],[1,0]]

# Afficher l'image
img = plt.imshow(twopixel, cmap='gray')
```

Voici un exemple un tout petit peu plus compliqué d'une image de 11 x 8 pixels : 

```{codeplay} 
# On crée la matrice de pixel représentant notre image et on la stocke dans une variable
alien = [[1,1,0,1,1,1,1,1,0,1,1],
       [1,1,1,0,1,1,1,0,1,1,1],
       [1,1,0,0,0,0,0,0,0,1,1],
       [1,0,0,1,0,0,0,1,0,0,1],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,1,0,0,0,0,0,0,0,1,0],
       [0,1,0,1,1,1,1,1,0,1,0],
       [1,1,1,0,0,1,0,0,1,1,1]]
# On affiche ensuite notre image avec la fonction imshow en lui donnant en paramètre la variable contenant l'image
img = plt.imshow(alien, cmap='gray')
```

#### Exercice

Reproduisez le code ci-dessus et modifiez-le afin d'obtenir l'alien
ci-dessous

![Alien Up](media/alien_up.png)

```{codeplay} 
#Votre code ici
```

### Images en niveau de gris

Si on veut avoir une image en niveaux de gris, on va pouvoir utiliser
par exemple huit bits (1 octet) pour chacun des pixels.

Huit bits, ça nous donne 256 valeurs possibles (2 puissance 8).

On va avoir le **zéro qui va être du noir**, **255 le maximum qui sera
du blanc**, et les valeurs intermédiaires qui seront des gris plus ou
moins foncés.

*On pourrait aussi utiliser un nombre de bits différents pour augmenter
ou diminuer le nombre de niveaux de gris possibles.
Une alternative serait également d'utiliser une valeur décimale entre 0
(= noir) et 1 (= blanc)*

```{codeplay} 
# On crée la matrice de pixel représentant notre image et on la stocke dans une variable
ndg = [[0,0.2,0.4,0.6,0.8,1]]

#On affiche ensuite notre image avec la fonction imshow en lui donnant en paramètre la variable contenant l'image
img = plt.imshow(ndg, cmap='gray')
```

#### Exercice

En utilisant le même principe que l'exercice précédent, créez le cœur
de Link

![LinkHeart](media/heart.png)

```{codeplay} 
#Votre code ici
```

### Images en couleur 

Enfin, on va pouvoir faire de la couleur en combinant du rouge, du vert
et du bleu.

#### Couleur de base

Une couleur **primaire** est une couleur qui ne peut pas être reproduite
par un mélange d'autres couleurs.

Toutes les couleurs peuvent donc être créées avec les couleurs de base
rouge, vert et bleu.

![](https://upload.wikimedia.org/wikipedia/commons/1/14/AdditiveColorMixing.png)

Le mélange des trois couleurs de base donne la couleur blanche.

#### Système RGB

Le système RGB (Red, Green, Blue) définit une couleur par ces 3
composantes **Rouge, Vert, Bleu**. Une couleur est donc un tuple
(collection ordonnée de plusieurs éléments), et nous pouvons définir les
3 couleurs de base comme ceci:

```{codeplay} 
#On défini une couleur comme un tuple RGB stocké dans une variable
rouge = np.array([255, 0, 0]) 
vert = np.array([0, 255, 0]) 
bleu = np.array([0, 0, 255])
```

Ce qui nous permet de créer une image avec 3 pixels: rouge, vert, bleu

```{codeplay} 
rgb = [[rouge, vert, bleu]]
img = plt.imshow(rgb);
```

#### Exercice

Definissez la couleur blanche et créez une image du drapeau d'Italie
(vert, blanc, rouge) puis de France (bleu, blanc, rouge).

```{codeplay} 
#Votre code ici
```

## Mélanger des couleurs 


### Additivité des couleurs

Les couleurs sont additives.

-   rouge + bleu donne **magenta**
-   rouge + vert donne **jaune**
-   vert + bleu donne **cyan**

```{codeplay} 
magenta = rouge + bleu
jaune  = rouge  + vert
cyan   = bleu   + vert
```

Vérifions les codes RGB de nos mélanges de couleurs


```{codeplay} 
print(jaune, 'jaune')
print(cyan, 'cyan')
print(magenta, 'magenta')
```

```{codeplay} 
cmj = np.array([[cyan, magenta, jaune]])
img = plt.imshow(cmj);
```

#### Exercice

Créez une image de taille 3x3 ou la colonne du milieu représente le
mélange des deux couleurs à gauche et droite.

    rouge magenta bleu
    vert  jaune   rouge
    bleu  cyan    vert

```{codeplay} 
#Votre code ici
```

### Noir et blanc

Toutes les couleurs mélangées donnent le blanc. L'absence de toute
couleur donne le noir.

```{codeplay} 
blanc = rouge + vert + bleu
noir = [0, 0, 0]
```

```{codeplay} 
cmjn = np.array([[cyan, magenta, jaune, noir, blanc]])
img  = plt.imshow(cmjn);
```

#### Exercice

Nous pouvons maintenant créer des simples icones, comme par exemple le
drapeau Suisse.

[SwissFlag]{.image}

```{codeplay} 
#Votre code ici
```

## Création d'icones

Afin de créer votre icone personalisée, vous devez commencer par créer
une image.
Cette image devra ensuite être déclinée en plusieurs tailles. Toutes ces
images devront être rassemblée dans un dossier qui sera ensuite
transformé en un jeu d'icones utilisables.

### Première étape - Création de l'image

Créez une image de taille 32x32 représentant ce que vous souhaitez.

```{codeplay} 
#Votre code ici
```

### Enregistrez votre image

Pour enregistrer votre image, nous allons rendre les axes invisibles et
choisir le nom de fichier, par exemple `toto.png` .
Le code ci-dessous va s'occuper de faire cela pour vous, il vous faut
juste remplacer `monImage` par la variable qui contient votre image et
choisir un nom pour votre image à la place de `toto.png`, puis
d'executer la cellule.

```{codeplay} 
#Mettez le le nom de la variable contenant votre image à la place de monImage
icn = np.array(monImage)

imgName = 'toto.png'

img = plt.imshow(icn)
img.axes.get_xaxis().set_visible(False)
img.axes.get_yaxis().set_visible(False)
plt.imsave(imgName, icn/255)
```

### Générez le jeu d'icones 

Pour générer un jeu d'icones pour OSX, il faut créer l'icone à
différentes taille, typiquement 16x16, 32x32, 128x128, 256x256 et
512x512.

La commande pour transformer votre image en icon 32x32 pour iconset est
:

> sips -z 32 32 monImage.png --out icon_32x32.png

Une fois les différentes tailles générées, on les met dans un dossier
FolderName.iconset sur lequel on applique la commande :

> iconutil -c icns FolderName.iconset

En attendant que vous ayez les compétences pour coder ces instructions
par vous même, la cellule ci-dessous va le faire pour vous.
Après son exécution, vous devriez avoir un nouveau fichier `myIcon.icns`
que vous pourrez utiliser pour remplacer l'icone de n'importequel
fichier ou dossier en le faisant glisser à la place de l'icone actuelle
dans la fenêtre d'information (cmd + i).

```{codeplay} 
import os
os.system("mkdir myIcon.iconset")
for s in [16, 32, 128, 256, 512]:
    os.system(f"sips -z {s} {s} toto.png --out icon_{s}x{s}.png")
os.system("mv icon_*.png myIcon.iconset")
os.system("iconutil -c icns myIcon.iconset")
```
