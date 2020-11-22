# Exercices avec des portes logiques
>**Contenus abordés** : Portes logiques, loi de De Morgan, systèmes logiques simples, demi-additionneur, additionneur

## Introduction

... a compléter ...
:::{admonition,hint} Rappel
Dans la suite, nous représentons fréquemment Vrai et Faux par **0** et **1** et vice versa sans autre formalisme.
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

Pour installer le logiciel, il suffit de le [télécharger](./media/Logidules/simul.jar) et de double clicker sur le fichier .jar

Il faut alors un peu réarranger l'environnement (tirer le diagramme de temps que nous n'utiliserons pas à droite)

:::


## Exercices de base

:::{admonition,attention} Exercice 1 : un binary digit (*bit*)
Construisons notre premier cirtuit le plus simple dans logic.ly. Ce dernier représente une unité d'information, en anglais *binary digit* abrégé bit.

![Un simple bit](media/PortesLogiques_Ex1.png)
:::

:::::{admonition,attention} Exercice 2 : un demi octet
Un octet est un ensemble de huit bits. Pour simplifier, nous allons ici construire un demi-octet avec sa représentation binaire et sa représentation hexadécimale[^hexa].

::::{admonition,note}Avec logic.ly
![Un simple bit](media/PortesLogiques_Ex2.png)

A réaliser:
1. Essayer quelques configuration et observer.
2. Tester la division et la multiplication par deux en décalant à droite et à gauche un nombre binaire.
::::

::::{admonition,note}Avec des logidules
Les logidules ont l'avantage de permettre des montages rapides de portes logiques en parallèle. Nous allons ici réaliser le même montage avec un demi-octet.

:::{figure} fig-target
<img src="media/Logidules/1-RepresentationBinaire/AffichageBinaire.jpg"  width="200px">

Avec des logidules
:::
:::{figure} fig-target
<img src="media/Logidules/1-RepresentationBinaire/AffichageBinaireS.png"  width="200px">

Dans le simulateur
:::

A réaliser: 
1. Effectuer les même tests que précédemment.
2. Etendre le circuit à un octet complet.
::::

:::::

## Portes logiques
::::{admonition,attention} Exercice 3 : portes logiques élémentaires
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

::::

::::{admonition,attention} Exercice 5 : loi de *De Morgan*

::::

## Système logiques

::::{admonition,attention} Exercice 5 : demi-additionneur

::::

::::{admonition,attention} Exercice 6 : additionneur

::::

[^hexa]: La notation hexadécimale se fait en base 16 avec les chiffres suivants: {1,2,3,4,5,6,7,8,9,A,B,C,D,E,F}