# 1. Les entiers

La plupart des civilisations humaines utilise le système décimal.
Pourquoi ? Tout simplement parce que nous avons 10 doigts !

L'ordinateur, lui, n'a pas de doigts mais utilise l'électricité. Par
conséquent, il ne connaît que deux types d'informations : il y a du
courant, il n'y a pas de courant ; allumé, éteint ; vrai, faux ; 1 ou 0.

**On dit qu'il travaille dans un système binaire, ou en base deux.**

## 1.1. Les systèmes de numération

### Le système décimal

Ce système est composé de 10 symboles qui sont les chiffres :

0, 1, 2, 3, 4, 5, 6, 7, 8, 9

Ainsi, tout nombre écrit dans la base 10 est composé de ces chiffres.

La valeur de chaque chiffre dépend alors du chiffre lui-même et de sa
place. Ainsi, le 3 de 1934 et celui de 3008 n'ont pas la même valeur :
Le premier vaut 30, alors que le second vaut 3000.  
On parle alors de **représentation positionnelle en base 10**.

Dans ce système, pour connaître la valeur de chaque chiffre qui compose
un nombre, il faut décomposer ce nombre pour identifier chaque chiffre
et son coefficient, c'est la **forme canonique**.

``` {panels}
:column: col-sm

Décomposition du nombre 3528 :
^^^
* 8 unités
* 2 dizaines
* 5 centaines
* 3 milliers
+++
Sa forme canonique est : $3 \cdot 10^3 + 5 \cdot 10^2 + 2 \cdot 10^1 + 8 \cdot 10^0$ 
```

On peut alors vérifier que le nombre 3528 est bien dans la base 10, car
tous ces chiffres appartiennent à la base 10. Les nombres de la base 10
ou du système décimal sont des nombres décimaux.

### Le système binaire

Le système binaire, ou numération positionnelle en base 2, est
représenté à l'aide d'uniquement 2 symboles : 0 et 1.  
Cette représentation et la représentation décimale sont deux
représentations, parmi d'autres, d'un même concept.

Un élément binaire se nomme un *bit* et un ensemble de *bits* peut
représenter un entier en utilisant le même principe que pour le système
décimal.

La valeur de chaque chiffre dépend toujours de sa place qui représente,
cette fois, une puissance de 2.

La forme canonique du nombre binaire $1101_{(2)}$ est : $1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0$

```{admonition} Le saviez-vous ? 
:class: hint
vient de la terminologie anglo-saxonne de *binary digit*. Un ensemble
de 8 bits et appelé un **octet**. Un *kilo-octet* (ko) correspond à
$10^3$ octets soit $1000$ octets, donc $8000$ bits. Attention à ne pas
confondre les préfixes binaires ($2^{10}$, $2^{20}$, $2^{30}$, etc.) et
les préfixes décimaux ($10^3$, $10^6$, $10^9$, etc.). On appelle
*kibioctet*, pour kilo binaire, une quantité de $2^{10} = 1024$ octets.
On peut remarquer que cette notation, quoique rigoureuse, peine à
s'imposer dans le vocabulaire courant des ingénieurs eux-même...
```

#### Compter en binaire

On compte en binaire de la même manière que l'on compte en base 10 en
ajoutant 1 aux unités (position la plus à droite). Lorsqu'on arrive au
dernier chiffre (i.e. 9 en base 10 et 1 en base 2), on le remet à 0 et
on augmente de 1 le chiffre à sa gauche.

On répète ces opérations pour tous les chiffres, quelle que soit leur
position. Ainsi, en base 10 :

$$\begin{equation}
0;-;1;-;2;-;3;-;...;-;9;-;10;-;11;-;...;-;99;-;100;-;101;-;...
\end{equation}$$

En binaire, on obtient : $\begin{equation}0;-;1;-;10;-;11;-;100;-;101;-;110;-;111;-;1000;-;...\end{equation}$

```{admonition} Micro-activité ✏️📒 
:class: note 
Comptez jusqu'à 40 en binaire. Que pouvez vous observer au sujet de la parité des nombres
binaires ? Pourquoi ?
```

#### Conversion du binaire vers le décimal

La conversion d'un nombre binaire en nombre décimal se fait aisément
grâce à la forme canonique.

En effet, il suffit de calculer le résultat de la somme pondérée par les
puissances de 2.

```{panels}
:column: col-md

Conversion du nombre 10101
^^^
$$\begin{equation}
10101_{(2)} = 1 \cdot 2^4 + 0 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 21_{(10)}
\end{equation}$$
```

Le {ref}`tableau <conversion-octet>` ci-dessous permet de convertir un
octet en nombre décimal.

``` {list-table}
:header-rows: 1
:align: right
:name: conversion-octet

* - Coefficient
  - $2^7$
  - $2^6$
  - $2^5$
  - $2^4$
  - $2^3$
  - $2^2$
  - $2^1$
  - $2^0$
* - Valeur
  - 128
  - 64
  - 32
  - 16
  - 8
  - 4
  - 2
  - 1
* - Bit
  - 0
  - 0
  - 1
  - 0
  - 1
  - 0
  - 1
  - 0
```

L'exemple utilisé ici est l'octet $(00101010_{(2)})$ dont la valeur
décimale est : $\begin{equation} 00101010\_{(2)} = 0 \cdot 2^7 + 0 \cdot 2^6 + 1 \cdot 2^5 + 0 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0 = 42\_{(10)} \end{equation}$

```{admonition} Important 
:class: caution 
L'utilisation d'un tableau de conversion nécessite d'écrire le nombre binaire de droite à gauche car
le bit de poids faible ($=2^0$) se trouve à droite, de la même façon que
le chiffre de poids faible (=l'unité) se trouve à droite en
représentation décimale.
```

```{admonition} Micro-activité ✏️📒 
:class: note
<!-- <span style="color:green">Niveau débutant</span> -->

Donnez la conversion décimale des nombres binaires suivants :

  - 10101101
  - 01110010
  - 1111
  - 1111111
  - 1
  - 10
  - 100
  - 1000
  - 10000
  - 100000
  - 1000000
  - 10000000

<!-- end list -->

```

#### Conversion du décimal vers le binaire

L'opération de conversion du décimal vers le binaire est moins directe.
Cependant, à l'aide d'un tableau de conversion et des instructions suivantes, il est possible d'obtenir la représentation binaire de n'importe quel entier positif.

**Tableau de conversion**

```{math}
\begin{array}{|l|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\text{Coefficient} & 2^{10} & 2^9 & 2^8 & 2^7 & 2^6 & 2^5 & 2^4 & 2^3 & 2^2 & 2^1 & 2^0  \\ 
\hline
\text{Valeur} & 1024 & 512 & 256 & 128 & 64 & 32 & 16 & 8 & 4 & 2 & 1\\ 
\hline
\text{Bit} &  &  &  &  &  &  &  &  &  &  & \\ 
\hline 
\end{array} 
```

**Instructions de conversion d'un entier décimal en binaire**

1.  Déterminer le coefficient **maximum** dont la valeur est plus petite
    que l'entier à convertir.
2.  Le bit associé à ce coefficient est 1.
3.  Soustraire la valeur de ce coefficient à l'entier à convertir pour
    obtenir le nouveau nombre à convertir.
4.  Recommencer à l'étape 1 tant que le nombre est différent de 0.
5.  En commençant par le plus grand coefficient utilisé, le nombre
    binaire correspondant est composé de la suite des bits où des 0
    représentent les coefficients non utilisés.

Par exemple, la conversion du nombre décimal 666 en binaire s'obtient
avec les étapes suivantes :

```{math}
$$\begin{align}
666 = 512 + 154 \\
154 = 128 + 26 \\
26 = 16 + 10 \\
10 = 8 + 2 \\
2 = 2 + 0
\end{align}$$
```

```{math}
$\begin{array}{|l|c|c|c|c|c|c|c|c|c|c|c|}
%\hline
%\text{Coefficient} & 2^{10} & 2^9 & 2^8 & 2^7 & 2^6 & 2^5 & 2^4 & 2^3 & 2^2 & 2^1 & 2^0  \\ 
\hline
\text{Valeur} & 1024 & 512 & 256 & 128 & 64 & 32 & 16 & 8 & 4 & 2 & 1\\ 
\hline
\text{Bit} &  & 1 & 0 & 1 & 0 & 0 & 1 & 1 & 0 & 1 & 0\\ 
\hline 
\end{array}$
```

Résultat : $(666_{(10)} = 1010011010_{(2)})$

```{admonition} Micro-activité ✏️📒 
:class: note
<!-- <span style="color:orange">Niveau intermédiaire</span> -->

Donnez la conversion binaire des nombres décimaux suivants :

  - 97
  - 123
  - 256
  - 1000
  - 511

<!-- end list -->
```

```{admonition} Aller plus loin
:class: note

Pouvez-vous penser à une autre façon de convertir un entier décimal en binaire ?
```

```{admonition} Anecdote 
:class: hint

Le 4 juin 1996, le premier vol de la fusée Ariane 5 a explosé 40
secondes après l'allumage. La fusée et son chargement avaient coûté 500
millions de dollars. La commission d'enquête a rendu son rapport au bout
de deux semaines. Il s'agissait d'une erreur de programmation dans le
système inertiel de référence. À un moment donné, un nombre codé en
virgule flottante sur 64 bits (qui représentait la vitesse horizontale
de la fusée par rapport à la plate-forme de tir) était converti en un
entier sur 16 bits. Malheureusement, le nombre en question était plus
grand que 32768 (le plus grand entier que l'on peut coder sur 16 bits)
et la conversion a été incorrecte, induisant un changement de
trajectoire fatal.
```

</div>

<div class="cell markdown">

## 1.2. Représentation des entiers négatifs

Après la représentation des entiers naturels $(\(\mathbb{N}\))$, on
souhaite évidement pouvoir représenter les entiers négatifs afin d'avoir
une représentation des entiers relatifs $(\(\mathbb{Z}\))$.  
Un entier relatif est un entier naturel auquel on a ajoute un signe
positif ou négatif indiquant sa position **relative** par rapport à 0.

### Bit de signe

La première idée pour représenter un entier relatif est d'utiliser un
bit pour représenter le signe. En effet, un bit peut uniquement prendre
deux valeurs, 0 ou 1, comme le signe, + ou -. Les bits restants étant
utilisés pour représenter un entier positif.  
Considérons l'encodage sur un octet (8 bits), nous réservons le bit de
poids fort (la puissance de 2 la plus grande) pour le signe : 0 indique
un nombre positif et 1 un nombre négatif.

Avec cette approche, un entier relatif est représenté par sa valeur
absolue (entier naturel) auquel on associe un signe. Le domaine couvert
se trouve donc divisé par deux, un bit étant utilisé pour le signe.  
Ainsi, avec un octet, 7 bits sont utilisés pour encoder la valeur
absolue, soit $\[0, 127\]$, ce qui permet de représenter les entiers
relatifs dans l'intervalle $\[-127, 127\]$.

```` {panels}
:column: col-sm
La représentation de -21 est :
^^^
```{math}
$$\begin{array}{|l|c|c|c|c|c|c|c|}
\hline
\text{signe} & 2^6 & 2^5 & 2^4 & 2^3 & 2^2 & 2^1 & 2^0  \\
\hline
1 & 0 & 0 & 1 & 0 & 1 & 0 & 1\\ 
\hline 
\end{array}$$ 
```
````

Bien que cette approche soit simple et semble convenir, elle pose deux
problèmes majeurs :

  - le premier est d'avoir deux représentations pour zéro (+0 et -0),
  - le second apparait lorsque l'on additionne un nombre et son opposé.
    Le résultat de cette opération devrait être 0, mais, sans rentrer
    dans le détail de l'arithmétique binaire qui sera abordée plus tard,
    l'addition bit à bit avec cette représentation donne
    $(-2 \lvert x \rvert\)$. En effet, l'addition des bits de signe donne
    toujours 1 et le reste des bits représente l'addition de deux fois
    la valeur absolue.

Pour remédier ces problèmes, une autre représentation des entiers
relatifs a été mise au point, il s'agit de la représentation en
complément à deux.

</div>

<div class="cell markdown">

### Complément à deux

La représentation en complément à deux reprend l'idée du signe encodé
par le bit de poids fort et conserve la représentation des entiers
positifs. Donc tous les entiers positifs ont une représentation en
binaire qui commence par un 0 et le plus grand entier représenté sur un
octet est 127.

Les entiers négatifs sont représentés grâce au complément à deux dont
voici le principe :

1.  Écrire la valeur absolue du nombre en binaire (le bit de poids fort
    est égal à 0).
2.  Inverser tous les bits, les 0 deviennent des 1 et vice-versa. Le
    résultat obtenu s'appelle le complément à 1 du nombre de départ.
3.  On ajoute 1, la dernière retenue est ignorée le cas échéant.

<!-- end list -->

```{panels}
:column: col-sm

La représentation de -21 en complément à 2 :
^^^
1. Valeur absolue en binaire : 00010101
2. Complément à 1 : 11101010
3. Ajouter 1 : 11101011
+++
La représentation de -21 est 11101011, qui additionné à 21, soit 00010101 donne bien zéro : 00000000.
```

```{figure} media/4bitsIntegers.jpg 
alt: Représentation des entiers
avec 4 bits width: 600px align: left --- Représentation des entiers
avec 4 bits. </br> Cette figure illustre la différence du domaine
couvert avec 4 bits pour la représentation des entiers naturels ou des
entiers relatifs. Ainsi, avec 4 bits le domaine couvert pour les entiers
naturels est : \[0, 15\], et pour les entiers relatif : \[-8, -7\].
```

<!--
```{figure} media/4bitsIntegers.jpg
:width: 550
:height: 300
```
Représentation des entiers avec 4 bits.
La figure ci-dessus illustre la différence du domaine couvert avec 4 bits pour la représentation des entiers naturels ou des entiers relatifs.
Ainsi, avec 4 bits le domaine couvert pour les entiers naturels est : \[0, 15\], et pour les entiers relatif : \[-8, -7\].  
-->

```{admonition} A retenir 
:class: attention

Puisque le nombre d'entiers relatifs représentés est forcément pair et
que le 0 en fait partie, il y a une asymétrie entre les nombres positifs
et négatifs représentés. Par exemple, avec 4 bits on peut représenter
-8, **mais pas 8**
```

```{dropdown} Quel est le domaine couvert en utilisant la représentation en complément à deux sur un octet ?
$[-128, 127\]$
```

```{admonition} Micro-activité ✏️📒
:class: note
<!-- <span style="color:green">Niveau débutant</span> -->

Encodez les entiers relatifs suivants sur un octet :

* -99
* -1
* 127
* -128
```

````{panels}
:column: col-sm

Vous pouvez maintenant comprendre ce comic d'un robot comptant des moutons pour s'endormir... d'ailleurs, combien de bits utilise-t-il pour compter ??
^^^
```{figure} media/cant_sleep.png
```
+++
Source : [xkcd](https://xkcd.com/571/)
````

</div>


`````{admonition} Activité : pour aller plus loin ... ✏️📒 
:class: note

<!-- <span style="color:red">Niveau avancé</span> -->

Le code binaire réfléchi, ou code Gray, est un type de codage binaire ne
modifiant qu’un seul bit à la fois quand un nombre est augmenté d’une
unité. Ce type de codage est utilisé pour les codeurs rotatifs absolus
calibrés et initialisés une seule fois **qui doivent conserver leur
valeur** lors de l'arrêt de l'appareil, comme les compteurs
kilométriques des automobiles (à la différence du compteur journalier
qui peut être remis a zéro par l'utilisateur).

<br>

Voici le début de la table de correspondance décimal-binaire-Gray sur
quatre bits (huit premières valeurs) :

| Codage décimal | Codage binaire | Codage binaire réfléchi |
| :------------- | -------------- | ----------------------: |
| 0              | 0000           |                    0000 |
| 1              | 0001           |                    0001 |
| 2              | 0010           |                    0011 |
| 3              | 0011           |                    0010 |
| 4              | 0100           |                    0110 |
| 5              | 0101           |                    0111 |
| 6              | 0110           |                    0101 |
| 7              | 0111           |                    0100 |

Chaque encodage peut être représenté sur un disque divisé en huit
secteurs identiques :

```{image} media/bin.png
:width: 200
:height: 200
```

```{image} media/gray.png 
:width: 200 
:height: 200 
```

<br>

1 - Etablir la correspondance entre la table binaire et la figure de
l'encodage binaire, puis entre la table Gray et la figure
correspondante.

2 - En comprenant la construction des huit valeurs données dans la table
de correspondance (correspondant donc aux huit secteurs des disques),
tenter d'écrire la table complète sur quatre bits.

3 - Combien de secteurs angulaires les disques vont-ils comprendre pour
un codage sur quatre bits ? Représenter alors le disque binaire puis
Gray sur quatre bits.

`````
