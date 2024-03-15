(ens:repinfo:imagesnumeriquesvar)=
# Images Numériques 

La partie théorique consiste à visionner en premier la vidéo suivante qui a pour but de donner les bases de la repérsentation des images en binaire.

```{youtube} I4Fg58jO5Mg
```


Cette activité est une variante qui n'utilise pas de langage de programmation (Python, numpy, matplotlib, etc.). Elle se base sur les formats de fichiers textes suivant:

- *.pbm* - images en noir et blanc
- *.pgm* - images en niveaux de gris
- *.ppm* - images en couleur

Les fichiers créés sont immédiatement visibles en tant qu'icônes sur les systèmes d'exploitation Mac OS. Pour bien les visualiser, il faut passer en représentation par icône et augmenter suffisamment leur taille.

<center> 

```{image} media/E.png
:height: 300px
```
```{image} media/logo.png
:height: 300px
```
```{image} media/degrade_gris.png
:height: 300px
```
```{image} media/degrade_bleu.png
:height: 300px
```
</center>

----

```{admonition} Notice
:class: hint

* **Thème** : Représentation de l'information (images et pixels)
* **Niveau** : `Facile à moyen`
* **Durée** : 2 périodes
* **Objectifs pédagogiques** : Manipuler des images pixel par pixel
* **Notions fondamentales** : modes de représentation des pixels par des nombres entiers
* Modalité : `branché`
* **Matériel** : un éditeur de fichiers
* **Prérequis** : Aucun
```

## Principe

Les fichiers .pbm, .pgm et .ppm permettent de coder facilement des pixels individuels en mode texte. Chacun de ces fichiers comporte une en-tête suivie des données. Les éléments sont simplement séparés par des espaces ou des tabulations. Les retours à la ligne n'ont pas d'importance. Par contre, il faut ajouter un espace après le dernier élément pour qu'il soit pris en compte. 

### En-tête

1. le mode:
    - "P1" pour des fichiers noir-blanc (.pbm)
    - "P2" pour des fichiers en niveau de gris (.pgm)
    - "P3" pour des fichiers en couleurs (.ppm)

2. la taille de la grille en pixels (h x l)
3. le nombre de niveaux de valeur des pixels

### Données

Chaque pixel est codé de 0 à la valeur maximale choisie. Les pixels sont séparés par un espace. Il faut simplement s'assurer d'avoir un nombre de pixels au moins égal à la taille de la grille (h x l)

## Exemples

</br>
<center> 

```{image} media/exemple1.png
:height: 300px
```
</center>
</br>
Attention, pour le mode noir-blanc le codage utilise 1 pour le noir et 0 pour le blanc! 
<p style="margin-bottom:3cm;">Ici l'image est définie sur une grille 4 x 5. </p>

<center> 

```{image} media/exemple2.png
:height: 300px
```
</center>
</br>
<p style="margin-bottom:3cm;">Ici l'image est définie sur une grille 3 x 6. Les niveaux de gris vont de 0 à 4 (5 valeurs) 0: noir 4: blanc. Avec ce codage, il est facile de définir des dégradés</p>
<center> 

```{image} media/exemple3.png
:height: 300px
```
</center>
</br>
Ici l'image est définie sur une grille 4 x 4. Les valeurs sont définies de 0 à 255 (256 valeurs). Chaque pixel est codé sur 3 valeurs pour RVB. Les valeurs dans le texte ont été colorées pour correspondre à la couleur des pixels.

<p style="margin-bottom:3cm;">Il est parfaitement possible de définir les valeurs de 0 à 100 pour correspondre à un pourcentage. </p>




## Déroulement


| Étape                                   | Durée  | Phase de l'activité   | 
|---------------------------------------|------ |---------------------|
| {ref}`0. Visionnement de la vidéo<ens:repinfo:imagesnumeriquesvideo>`  | 10 min  | Apprentissage           |
| {ref}`1. La pixelisation<ens:repinfo:imagesnumeriquesvar:pixel>`           | 15 min  | Exploration |
| {ref}`2. Lettres au format bitmap<ens:repinfo:imagesnumeriquesvar:lettres>`  | 15 min   | Exploration          |
| {ref}`3. Les dégradés (niveau de gris)<ens:repinfo:imagesnumeriquesvar:degrades>`  | 15 min   | Exploration et institutionnalisation               |
| {ref}`4. Les drapeaux <ens:repinfo:imagesnumeriquesvar:drapeaux>`    | 15 min   | Exploration et institutionnalisation    |
| {ref}`5. Les dégradés (couleur)<ens:repinfo:imagesnumeriquesvar:degrades-col>`    | 15 min   | Exploration et institutionnalisation   |

(ens:repinfo:imagesnumeriquesvar:pixel)=

### Pixelisation

Cette première partie se fait de manière débranchée. On distribue aux élèves des grilles imprimées (sur papier et sur transparent) et divers logos.
{download}`grilles<media/grilles.pdf>`, {download}`logo 1<media/Logo.pdf>`, {download}`logo 2<media/Logo 2.pdf>` et {download}`logo 3<media/Logo 3.pdf>`.
On superpose les grilles transparentes aux images pour remplir les grilles sur papier.

Lors d'une petite mise en commun, on peut comparer les résultats obtenus par les élèves. Globalement on peut remarquer qu'il faut un grand nombre de pixels (résolution élevée) pour pouvoir identifier un logo même très simple. On va se concentrer sur des objets facilement identifiables même avec un nombre très limité de pixels: les lettres de l'alphabet.

(ens:repinfo:imagesnumeriquesvar:lettres)=

### Lettres au format bitmap

Les lettres sont très faciles à identifier, même sur des grilles de taille réduite (4 x 5 ou 5 x 5). En utilisant l'exemple donné pour la lettre "E", on introduit les fichiers de type *.pbm*. La tâche des élèves est de produire diverses lettres de l'alphabet ou des chiffres.

(ens:repinfo:imagesnumeriquesvar:degrades)=

### Les dégradés

Il est difficile de produire une image en niveau de gris en codant les pixels individuels. Certains logiciels comme *GIMP* permettent d'enregistrer les fichiers directement sous ce format. Par contre, il est intéressants de produire des dégradés en variant progressivement les valeurs dans le tableau comme le montre l'exemple suivant. En fonction du niveau de connaissance des élèves, il est possible d'utiliser *Excel* pour générer facilement des dégradés numériques que l'on peut ensuite copier-coller.


```
# Codage du dégradé
P2
8 8
10
0  1  2  3  4  5  6  7
1  2  3  4  5  6  7  8
2  3  4  5  6  7  8  9
3  4  5  6  7  8  9 10
4  5  6  7  8  9 10 11
5  6  7  8  9 10 11 12
6  7  8  9 10 11 12 13
7  8  9 10 11 12 13 14
```

</br>
<center> 

```{image} media/degrade-diag.png
:height: 300px
```
</center>
</br>

(ens:repinfo:imagesnumeriquesvar:drapeaux)=

### Les drapeaux

Un bon sujet d'activité pour le codage des images en couleur consiste à reproduire des drapeaux. La palette des couleurs nécessaires est limitée et en cas de nécessité, on peut fournir une liste de valeurs au tableau pour aider les élèves. 

<center> 

```{image} media/swiss.png
:height: 150px
```
```{image} media/france.png
:height: 150px
```
```{image} media/ireland.png
:height: 150px
```
```{image} media/germany.png
:height: 150px
```
</center>

``` 
# Codage pour germany.ppm
P3
6 3 255
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
255 0 0 255 0 0 255 0 0 255 0 0 255 0 0 255 0 0 
255 255 0 255 255 0 255 255 0 255 255 0 255 255 0 255 255 0 
```

(ens:repinfo:imagesnumeriquesvar:degrades-col)=

### Les dégradés en couleur

Pour les élèves plus avancés, on peut proposer de coder des dégradés en couleur. C'est une activité plus difficile et il peut être utile de recourir à un tableur pour générer facilement les valeurs. 

```
# Codage pour germany.ppm
P3
6 6
12
12	0	2	11	1	2	10	2	2	9	3	2	8	4	2	7	5	2
11	1	2	10	2	2	9	3	2	8	4	2	7	5	2	6	6	2
10	2	2	9	3	2	8	4	2	7	5	2	6	6	2	5	7	2
9	3	2	8	4	2	7	5	2	6	6	2	5	7	2	4	8	2
8	4	2	7	5	2	6	6	2	5	7	2	4	8	2	3	9	2
7	5	2	6	6	2	5	7	2	4	8	2	3	9	2	2	10	2
6	6	2	5	7	2	4	8	2	3	9	2	2	10	2	1	11	2
5	7	2	4	8	2	3	9	2	2	10	2	1	11	2	0	12	2
```

</br>
<center> 

```{image} media/degrade_diag_2.png
:height: 300px
```
</center>