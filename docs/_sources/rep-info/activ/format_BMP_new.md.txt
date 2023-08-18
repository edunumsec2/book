(ens:repinfo:conceptionimages)=
# Conception d'images dans un éditeur hexadécimal

---- 

Cette activité, prévue pour deux périodes de 45 minutes en salle d'informatique, tourne autour de la conception d'images au format `BMP`.

La manipulation des images se fait au travers d'un éditeur hexadécimal et ne demande pas de connaissances en programmation.

----

```{admonition} Caractéristiques
:class: hint

* Nom : Conception d'images dans un éditeur hexadécimal
* Durée : 
* Thème : Représentation de l'information
* Objectifs d’apprentissage : L'objectif général de la leçon est que les élèves soient capables de concevoir des fichiers au travers d'un éditeur hexadécimal et en suivant un format de données spécifié. Voir {ref}`ci-dessous<formatbmp.objectifs>`pour des objectifs détaillés. 
* Notions fondamentales : 
* Approche pédagogique : Débranchée, mais pourrait aussi être faite en Python avec une librairie comme [Pillow](https://pillow.readthedocs.io/en/stable/)
* Matériel : voir {ref}`ci-dessous<formatbmp.materiel>`
* Niveau : `à compléter`
* Mots-clés : `à compléter`
* Dynamique (groupe / individuel) : `à compléter`
* Taille du groupe : `à compléter`
* Pré-requis : La notion de bit et d'octet / Les fichiers en tant que séquences d'octets.
```

(formatbmp.objectifs)=
### Objectifs détaillés

Les objectifs spécifiques sont les suivants:
- Les élèves sont capables d'expliquer que les fichiers, peu importe leur type, sont constitués de séquences de bits regroupés en octets.
- Les élèves sont capables de lire et d'écrire des octets en notation hexadécimale.
- Les élèves sont capables de concevoir des images au format `BMP` étant donné un fichier modèle.
- Les élèves sont capables de déchiffrer des couleurs exprimées au format `BGR` / `RGB`.
- Les élèves sont capables d'expliquer les principes généraux de la compression de données sans pertes.
- Les élèves sont capables de concevoir des images au format `BMP` utilisant une palette de couleur étant donné un fichier modèle. 

(formatbmp.materiel)= 
### Matériel

#### Éditeur

Cette activité nécessite l'usage par les élèves d'un éditeur hexadécimal.
Dans ce document, nous conseillons l'utilisation de l'éditeur [Hexed.it](https://hexed.it), une application web qui ne nécessite aucune installation.

Il existe d'autres solutions, notamment l'éditeur [Hex Fiend](https://hexfiend.com/) sur Mac OS X, qui offre une interface minimaliste suffisante pour le travail des élèves.

#### Fichiers

- Fichier modèle 4 pixels par 4 pixels: [files.modulo-info.ch/bmp/petit.bmp](https://files.modulo-info.ch/bmp/petit.bmp)
- Fichier modèle 8 pixels par 8 pixels: [files.modulo-info.ch/bmp/grand.bmp](https://files.modulo-info.ch/bmp/grand.bmp)
- Fichier modèle 8 pixels par 8 pixels, avec palette de couleurs: [files.modulo-info.ch/bmp/palette.bmp](https://files.modulo-info.ch/bmp/palette.bmp)

#### Resources

- Sélectionneur de couleurs BGR: [files.modulo-info.ch/bmp/couleurs.html](https://files.modulo-info.ch/bmp/couleurs.html)

#### Références théoriques pour l'enseignant·e

L'activité nécessite l'utilisation d'un éditeur hexadécimal par les élèves, ce qui suppose une introduction à la notation hexadécimale. L'[article Wikipédia](https://fr.wikipedia.org/wiki/Syst%C3%A8me_hexad%C3%A9cimal) sur le sujet est très complet.

Le format d'image utilisé dans le cadre de cette activité est le format `BMP`.
Une bonne introduction au format est [disponible sur Wikipédia](https://fr.wikipedia.org/wiki/Windows_bitmap).

Au besoin, la [version anglaise de l'article](https://en.wikipedia.org/wiki/BMP_file_format) entre dans plus de détails du format au travers d'exemples.



```{dropdown} **Déroulement**

1. {ref}`Double lecture des fichiers<formatbmp.doublelecture>` (5 mn) où il s'agit de faire comprendre qu'une image peut être affichée en tant qu'image ou lue en tant que séquence d'octets. 

1. {ref}`Introduction à la notation hexadécimale<formatbmp.introduction>` (10 mn) où l'enseignant·e explique la notation hexadécimale utilisée dans l'éditeur.

1. {ref}`Prise en main de l'éditeur et découverte du format BMP<formatbmp.formatbmp>` (10 mn).

1. {ref}`Formalisation<algo-tri.formalisation>` (20 mn) des divers algorithmes de tri. 

1. {ref}`Exercices<algo-tri.exercices>` (10-15 mn) d'application des algorithmes.

1. {ref}`Conclusion<algo-tri.conclusion>` (5-10 mn) en bouclant la boucle sur l'archivage informatisé et les pratiques (positives et négatives) qu'il permet.

```

(formatbmp.doublelecture)=
## Double lecture des fichiers

*Durée : 5 mn*

L'enseignant·e invite les élèves à télécharger le premier fichier utilisé à l'adresse:
[files.modulo-info.ch/bmp/petit.bmp](https://files.modulo-info.ch/bmp/petit.bmp).

Puis, l'enseignant·e invite les élèves à ouvrir le fichier à l'aide d'une visionneuse d'image (par exemple `Aperçu` sur Mac OS X).

Il est à noter qu'il faut bien zoomer pour voir l'image étant donné sa petite taille.

L'enseignant·e montre qu'il s'agit d'une image de 4 par 4 pixels, tous de couleur blanche.
Il ou elle en profite pour donner une définition du terme "pixel".

> Le pixel est plus petit élément qui compose une image.
> Chaque pixel d'une image est un carré de couleur qui occupe une place dans la grille de l'image.
> Le terme provient de l'anglais ***pic**ture **el**ement*.

Après cela, l'enseignant·e invite les élèves à ouvrir l'image dans un éditeur hexadécimal (par exemple [Hexed.it](https://hexed.it)).
L'enseignant·e explique aux élèves ce qu'ils ont sous les yeux: la séquence d'octets qui représente l'image.
L'enseignant·e souligne deux façons différentes de visualiser le même fichier:
- Son interprétation en tant qu'image dans la visionneuse d'image, et
- Son interprétation en tant que séquence d'octets dans l'éditeur hexadécimal.

S'il est possible de le faire dans l'éditeur, l'enseignant·e montre les bits qui se cachent sous la notation hexadécimale des octets. Dans [Hexed.it](https://hexed.it), les bits d'un octet sont affichés dans la colonne de gauche de l'éditeur.

## Introduction à la notation hexadécimale

*Durée : 10 mn*

L'enseignant explique la notation hexadécimale utilisée dans l'éditeur.
Alors que la notation binaire est basée sur la base 2, la notation hexadécimale est basée sur la base 16.
Les symboles utilisés pour représenter les 10 premiers chiffres sont les mêmes qu'en base 10: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` et `9`.
Pour représenter les chiffres suivants, la notation fait appel à des lettres: `A`, `B`, `C`, `D`, `E` et `F`.

La lecture et l'édition d'octets dans cette notation est en effet bien plus rapide qu'en notation binaire.
À la place d'une série de 8 symboles en notation binaire, il suffit de 2 chiffres.
De plus, chacun de ces chiffres correspond exactement à 4 bits, ce qui fait que chaque symbole peut-être converti en bits de manière indépendante.

| Symbole | Valeur | Séquence de bits |
|:-------:|:------:|:----------------:|
|   `0`   |   0    |      `0000`      |
|   `1`   |   1    |      `0001`      |
|   `2`   |   2    |      `0010`      |
|   `3`   |   3    |      `0011`      |
|   `4`   |   4    |      `0100`      |
|   `5`   |   5    |      `0101`      |
|   `6`   |   6    |      `0110`      |
|   `7`   |   7    |      `0111`      |
|   `8`   |   8    |      `1000`      |
|   `9`   |   9    |      `1001`      |
|   `A`   |   10   |      `1010`      |
|   `B`   |   11   |      `1011`      |
|   `C`   |   12   |      `1100`      |
|   `D`   |   13   |      `1101`      |
|   `E`   |   14   |      `1110`      |
|   `F`   |   15   |      `1111`      |

L'enseignant peut proposer aux élèves un exercice de conversion entre base 2 et base 16.
Par exemple :

- Convertir `00` depuis la notation héxadécimale au binaire en binaire
- Convertir `11111111` en hexadécimal
- Convertir `3C` en binaire
- Convertir `00010010` en hexadécimal


## Prise en main de l'éditeur et découverte du format BMP

*Durée : 10 minutes*

L'enseignant·e présente ensuite une introduction au format BMP au travers du petit fichier d'exemple (`petit.bmp`) sur l'éditeur.

L'enseignant·e indique que les 54 premiers octets du fichier constituent l'entête du fichier.
Cette entête contient notamment des informations sur les dimensions du fichiers, les couleurs utilisées, et ainsi de suite.

Les 48 octets suivants représentent les pixels de l'images.
Chacun des 16 pixels est encodé sur 3 octets (au format `Bleu-Vert-Rouge`).
Initialement, tous les octets sont à `FF`, et donc tous les pixels sont blancs.

L'enseignant·e indique que l'on utilise `FFFFFF` pour dénoter un pixel blanc, et indique 
aux élèves de remplacer les octets du premier pixel par `000000` puis de télécharger le fichier et de l'ouvrir dans la visionneuse afin d'observer les changements.
Le résultat attendu est le suivant.

<img src="https://files.modulo-info.ch/bmp/petit-step.bmp" class="pixels" />

### Exercice

L'enseignant·e présente l'ordre dans lequel apparaissent les pixels: de gauche à droite et de bas en haut.
Les élèves sont ensuite amenés à reproduire un damier noir et blanc, tel que présenté sur l'image suivante.

<img src="https://files.modulo-info.ch/bmp/damier.bmp" class="pixels" />

### Points d'attention

- S'ils ne sont pas attentifs, les élèves peuvent se retrouver avec une images constituée de deux colonnes noires et deux colonnes blanches intercalées. En effet, il s'agit de l'image obtenue en alternant pixels noirs et blancs.
- Les élèves peuvent se retrouver à ne plus pouvoir lire les fichiers qu'ils génèrent. En effet, une erreur dans le format peut amener à un fichier illisible. Pour résoudre ce problème, il s'agit simplement de vérifier que le fichier a bien le nombre attendu d'octets, et que les octets d'entête ne sont pas modifiés.
- Les élèves peuvent obtenir des pixels aux couleurs inattendues suite à un décalage d'un ou deux octets dans l'encodage des pixels. Dans ce genre de cas, après l'erreur traitée, les élèves peuvent être amenés à documenter ce qui s'est passé: Quelle était la couleur obtenue, quel était son code ?

### Étape 4 : Représentation des couleurs [5 minutes]

### Étape 5 : Reproduction d'une image [20 minutes]

### Étape 6 : Utilisation d'une palette de couleurs [10 minutes]

### Étape 7 : Conception libre d'une image avec palette de couleur [30 minutes]

## Pistes pour aller plus loin

Stéganographie: Utiliser les bits de poids faible des canaux de couleurs des pixels pour y cacher un message.

Compression avec codage par plage, qui est aussi supportée au format BMP.

Compression avec pertes et le format JPEG.

Images vectorielles.