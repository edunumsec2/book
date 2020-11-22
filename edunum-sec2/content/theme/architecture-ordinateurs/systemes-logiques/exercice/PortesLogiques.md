# Exercices avec des portes logiques
>**Contenus abordés** : Portes logiques, loi de De Morgan, systèmes logiques simples, demi-additionneur, additionneur

## Introduction

Dans cette série d'exercices nous allons survoler quelques éléments des systèmes logiques. Les exercices sont organisés de manière progressive, les premiers ne devraient occuper l'élève que quelques minutes, alors que les derniers constitue de véritables mini-projets.

:::{admonition,hint} Rappel
Dans la suite, nous représentons fréquemment Vrai et Faux par **0** et **1** et vice versa sans autre formalisme.

L'avantage des systèmes logiques et que l'on peut souvent énumérer tous les états possibles avec des tables de vérité. La conception de circuits peut donc se faire soit en établissant de telles tables et l'implémentant avec des portes logiques, soit en analysant un cirtuit et retrouvant la table correspondante.

:::


## Outils
Voici quelques outils *interactifs* pour simuler des systèmes logiques. Ils sont en principe équivalents. Si dans les exercices qui suivent nous vous recommandons l'usage de l'un ou l'autre, c'est surtout par commodité et pour rendre la réalisation de l'exercice plus facile.


:::{admonition,seealso} Logic.ly
Ce site vous propose un simulateur en ligne très facile à utiliser avec l'essentiel des portes logiques de base.
Il suffit de rendre sur le site [logic.ly](https://logic.ly/demo) pour accéder directement à l'application. 
:::

:::{admonition,seealso} Logidules et simulateur de logidues
Les logidules ont été développés dès 1968 par J.-D. Nicoud. Ils ont beaucoup été utilisés pour des exercices et le prototypage de systèmes logiques. Un simulateur a même créé qui nous permet d'expérimenter ces briques qui ont quasiment disparu.

![logidules](media/Logidules/logidules_registres.jpg)

**Installation**

Pour installer le logiciel, il suffit de le [télécharger](media/Logidules/simul.jar) et de double clicker sur le fichier .jar

Il faut alors un peu réarranger l'environnement (tirer le diagramme de temps que nous n'utiliserons pas à droite)

:::


## Exercices de base

::::{admonition,attention} Exercice 1 : un binary digit (*bit*)
Construisons notre premier cirtuit le plus simple dans logic.ly. Ce dernier représente une unité d'information, en anglais *binary digit* abrégé bit.

:::{figure} simple_bit
<img src="media/Ex1_PortesLogiques.png">

Un simple bit
:::

::::

:::::{admonition,attention} Exercice 2 : un demi-octet
Un octet est un ensemble de huit bits. Pour simplifier, nous allons ici construire un demi-octet avec sa représentation binaire et sa représentation hexadécimale[^hexa].

::::{admonition,note}Avec logic.ly

:::{figure} demi_octet
<img src="media/Ex2_PortesLogiques.png">

Un demi-octet
:::

A réaliser:
1. Essayer quelques configuration et observer.
2. Tester la division et la multiplication par deux en décalant à droite et à gauche un nombre binaire.
::::

::::{admonition,note}Avec des logidules
Les logidules ont l'avantage de permettre des montages rapides de portes logiques en parallèle. Nous allons ici réaliser le même montage avec un demi-octet.

:::{figure} logidule_representation
<img src="media/Logidules/Ex2_RepresentationBinaire/AffichageBinaire.jpg"  width="200px">

Avec des logidules
:::

:::{figure} simulateur_representation
<img src="media/Logidules/Ex2_RepresentationBinaire/AffichageBinaireS.png"  width="200px">

Dans le simulateur
:::

A réaliser: 
1. Effectuer les même tests que précédemment.
2. Etendre le circuit à un octet complet ([figure](simulateur_representation)).
::::

:::::

## Portes logiques
::::{admonition,attention} Exercice 3 : portes logiques élémentaires

:::{figure} porte_ET
<img src="media/Ex3_PortesLogiques.png">

Porte logique ET
:::

Complter les tables de vérité suivantes pour les portes logiques ET, OU, NON et XOR

**ET (AND)**

Nous avons la fonction A et B que nous notons : $A·B$

|  A  |  B  |  $S=A·B$  |
|:---:|:---:|:---:|
|  0  |  0  |     |
|  0  |  1  |     |
|  1  |  0  |     |
|  1  |  1  |     |

**OU (OR)**

Nous avons la fonction A OU B que nous notons : $A+B$

|  A  |  B  |  $S=A+B$  |
|:---:|:---:|:---:|
|  0  |  0  |     |
|  0  |  1  |     |
|  1  |  0  |     |
|  1  |  1  |     |

**OU EXCLUSIF (XOR)**

Nous avons la fonction A ou B que nous notons : $A \oplus B$

|  A  |  B  |  $S=A \oplus B$  |
|:---:|:---:|:---:|
|  0  |  0  |     |
|  0  |  1  |     |
|  1  |  0  |     |
|  1  |  1  |     |

**NON (NOT)**

Nous avons la fonction non A que nous notons : $S= \overline{A}$

|  A  |  B  |  $S= \overline{A}$  |
|:---:|:---:|:---:|
|  0  |  0  |     |
|  0  |  1  |     |

::::

::::{admonition,attention} Exercice 4 : comparateur

Il peut être intéressant de disposer d'un moyen de comparer deux nombres. Une telle fonction retourne ***vrai*** (càd. ***1***) lorsque les deux nombres sont identiques.

1. Pour un seul bit, quelle porte ou combinaison de portes logiques permet d'assurer une telle fonction.
2. Pour un octet ou un demi-octet comme assurer une telle fonction qui donnerait pour résultat ***vrai*** uniquement si tous les bits sont identiques.

*Cette fonction relativement simple à réaliser est toujours présente dans les microprocesseurs. On peut cependant se représenter la complexité du circuit lorsque l'opération doit être implémentée pour des mots de 64 bits qui est la taille standard pour les microprocesseurs actuels*

::::

::::{admonition,attention} Exercice 5 : lois de *De Morgan*
les lois de De Morgan proposent les égalités suivantes:

$$
    \overline{A·B} = \overline{A} + \overline{B}

    \overline{A+B} = \overline{A} · \overline{B}
$$

Que l'on peut aussi écrire avec un formalisme logique:

$$
    \overline{A \wedge B} = \overline{A} \lor \overline{B}

    \overline{A \lor B} = \overline{A} \wedge \overline{B}
$$

Et qui se formule en Francais:
> La négation de la disjonction de deux propositions est équivalente à la conjonction des négations des deux propositions, ce qui signifie que « non(A ou B) » est identique à « (non A) et (non B) ».

>La négation de la conjonction de deux propositions est équivalente à la disjonction des négations des deux propositions, ce qui signifie que « non(A et B) » est identique à « (non A) ou (non B) ».

On peut enfin en donner une représentation en diagramme de Vennes (fig) ...

:::{figure} DeMorgan
<img src="media/Demorganlaws.svg.png">

Diagrammes de *Venn* (source wikipedia[^2])
:::

**A réaliser :** Concevoir et mettre en place dans l'un ou l'autre des simulateurs un montage qui démontre le plus efficacement possible les lois de De Morgan.

> En életronique digitale, ces lois sont remarquables parce qu'elles garantissent que l'on peut toujours remplacer des portes **OU** avec des portes **ET** (et inversément). Cette équivalence est abondamment utilisée dans la conception de circuits intégrés digitaux.
> Sachant que l'on peut également trouver une combinaison équivalent pour construire une porte **XOR** et que l'on peut, en reliant ensemble les deux entrées d'une porte **NAND** en faire un inverseur (**NOT**), on réalise que n'importe quel système de logique combinatoire peut-être réalisé avec uniquement des portes **NAND**.

::::

## Système logiques

Dans cette partie nous allons réaliser des systèmes logiques qui rentrent dans la conception des microprocesseur tels que ceux utilisés dans votre odrinateur personnel ou votre smartphone.

Nous avons choisi de nous attarder sur l'additionneur et le demi-additionneur parce qu'ils démontrent une fonction facile à comprendre : l'addition en colonnes de nombres binaires.


::::{admonition,attention} Exercice 6 : demi-additionneur

Le demi-additionneur calcule sur une colonne et reporte la retenue, mais ne prend pas la retenue de la colonne précédente. C'est en fait l'additionneur qui est utilisée pour le premier bit ou première colonne.

En considérant le demi-additionneur comme une *une boîte noire*, nous avons donc deux entrées (les opérandes A et B) et deux sorties : la somme des deux entrée et la retenue (ou dépassement, en anglais : *carry*, noté C).

A partir de là, nous pouvons proposer la table de vérité suivante:

|  A  |  B  |  $S=A \oplus B$  | C |
|:---:|:---:|:---:|:---:|
|  0  |  0  |  0  |  0  |
|  0  |  1  |  1  |  0  |
|  1  |  0  |  1  |  0  |
|  1  |  1  |  0  |  1  |

**Consignes :** 
1. Concevoir le circuit logique complet.
2. Réaliser le circuit dans un simulateur et vérifier qu'il produit bien le résultat attendu.

::::

::::{admonition,attention} Exercice 7 : additionneur

Dans le cas d'un additionneur complet, nous devons reporter la retenue à la colonne suivante : $C_{in}$. Chaque colonne prend donc trois entrées et produit 2 sorties : le résultat de l'addition $S$ et la retenue $C_{out}$ qui devient le $C_{in}$ de la colonne suivante.

La table de vérité augmente en conséquence et passe à huit cas à nénumérer. Voici la forme qu'elle prend:

|  A  |  B  | $C_{in}$  | $S=A \oplus B$  | $C_{out}$ |
|:---:|:---:|:---------:|:---------------:|:---------:|
|  0  |  0  |  0        |                 |           |
|  0  |  0  |  1        |                 |           |
|  0  |  1  |  0        |                 |           |
|  0  |  1  |  1        |                 |           |
|  1  |  0  |  0        |                 |           |
|  1  |  0  |  1        |                 |           |
|  1  |  1  |  0        |                 |           |
|  1  |  1  |  1        |                 |           |

**Consignes :** 
1. Compléter la table.
2. Réaliser le circuit complet pour un demi-octet (évtl. un octet complet)


::::

## Système logiques plus avancés

Comme nous l'avons vu dans le cours, pour contruire un ordinateur, il nous manque encore la notion de mémoire. Nous allons donc, dans cette dernière série d'exercices aborder les bascules et la mémorisation.

Ces éléments introduisent la notion de **système synchrone**. Sans entrer dans les détails, il est désormais nécessaire de synchroniser les différents éléments qui *échangent* des informations. Pour cela, de tels système disposent d'un métronome qui donne la mesure. Dans un processeur on parle de signal d'horloge (Clock, abrégé CLK) qui dans les processeurs moderne oscille à une fréquence aux alenteurs de 3GHz.





[^hexa]: La notation hexadécimale se fait en base 16 avec les chiffres suivants: {1,2,3,4,5,6,7,8,9,A,B,C,D,E,F}
[^2]:Par Teknad — Travail personnel, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=36768081