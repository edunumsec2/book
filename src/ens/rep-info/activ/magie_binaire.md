(ens:repinfo:magiebinaire)=
# Magie Binaire

---- 

*Vous allez faire un tour de magie !*

Une introduction au binaire de manière ludique en misant sur la curiosité à comprendre le fonctionnement d’un tour de magie.

----


```{admonition} Notice
:class: hint

* **Thème** : Représentation de l'information (avant 1. Entiers)
* **Niveau** : Facile 
* **Durée** : 2 périodes
* **Objectifs pédagogiques** : Motiver la compréhension des nombres binaires
* **Notions fondamentales** : Représentation binaire des nombres entiers
* **Modalité** : Débranchée
* **Matériel** : Les 6 cartes pour faire le tour de magie. Disponible ici : {download}`fichier MagieBinaire.png<media/MagieBinaire.png>` 
* **Prérequis** : Aucun
```

| Étapes                                   | Durée          | Phase de l'activité   | 
|---------------------------------------|------|---------------------|
| {ref}`Présentation du tour de magie<magiebinaire.presentation>`| 15 min  | Mise en situation    |
| {ref}`Compter en binaire<magiebinaire.compter>`| 15 min  | Enseignement / Apprentissage |
| {ref}`Retour en base 10<magiebinaire.retour>`| 15 min   |   Enseignement / Apprentissage     |
| {ref}`Encodage de l'information<magiebinaire.encodage>`| 15 min   |   Enseignement / Apprentissage    |
| {ref}`Explication du tour<magiebinaire.explication>`| 15 min   | Objectivation           |
| {ref}`Pour aller plus loin<magiebinaire.plusloin>` | 10 min   | Réinvestissement              |


(magiebinaire.presentation)=
## Présentation du tour de magie

*Durée : 10-15 min*

*Objectif : attiser la curiosité*

Faire le tour de magie suivant à différents élèves. Il est possible que certains d’entre eux le connaissent, soient peut-être capable de le réaliser mais il est très peu probable qu’ils puissent expliquer pourquoi ça marche. Interrogez-les au préalable et concentrez-vous sur ceux qui ne le connaissent pas.

### Tour de magie

Demandez à un élève de choisir un nombre entre 1 et 63 et de le mémoriser sans vous le révéler. A l’aide des cartes vous allez lui révéler le nombre qu’il a secrètement choisi.

Variante 1
: Montrez les cartes une à une à l’élève en lui demandant simplement de vous indiquer si oui ou non son nombre apparaît sur la carte.

Variante 2
: Demandez à l’élève de séparer les cartes en 2 paquets, le premier avec les cartes ou son nombre est présent, le second avec les autres.

Le secret du tour est simple, il suffit d'additionner le nombre en haut à gauche de chaque carte où son nombre est présent.


(magiebinaire.compter)=
## Compter en binaire

*Durée : 15-20 min*

*Objectif : Comprendre comment représenter des nombres entiers positifs à l'aide de la numération de position avec seulement deux chiffres : le 0 et le 1.*

Commencez par expliquer le fonctionnement en base 10.

Pour compter, on commence par 0 et on ajoute 1 pour passer au chiffre suivant et on recommence. Après l’utilisation de tous les chiffres (0...9) on en rajoute 1 devant et on recommence...

Faire la même démonstration en base 2.

### Exercice 1

Faire compter les élèves de 0 à 20 (ou plus) en binaire sur papier, ils peuvent écrire le nombre correspondant en base 10 à côté.


(magiebinaire.retour)=
## Retour de base 2 à base 10

*Durée : 15-20 min*

Revenez ensuite sur la numérotation en base 10 pour présenter la forme canonique.  
Dans un système de position, comme le nôtre, pour connaître la valeur de chaque chiffre qui compose un nombre, il faut décomposer ce nombre pour identifier chaque chiffre et son coefficient.  
En effet, le 2 de 1924 et celui de 2004 n'ont pas la même valeur : Le premier vaut 20, alors que le second vaut 2000.

````{panels}
:columin: col-sd

Base 10
^^^
```{list-table}
:header-rows: 1
:name: example-table-1

* - Niveau
  - Nom
  - Coefficient
* - 0
  - Unités
  - $10^{0} = 1$
* - 1
  - Dizaines
  - $10^{1} = 10$
* - 2
  - Centaines
  - $10^{2} = 100$
* - 3
  - Milliers
  - $10^{3} = 1000$
```
````

La forme canonique de 3528 est : $3 \cdot 10^3 + 5 \cdot 10^2 + 2 \cdot 10^1 + 8 \cdot 10^0$.

En binaire c’est la même chose sauf qu’il n’y a que 2 chiffres qui composent la base, le 0 et le 1.

````{panels}
:columin: col-sd

Base 2
^^^
```{list-table}
:header-rows: 1
:name: example-table

* - Niveau
  - Nom[^0]
  - Coefficient
* - 0
  - Unité
  - $2^{0} = 1$
* - 1
  - *Deuzaine*
  - $2^{1} = 2$
* - 2
  - *Quatraine*
  - $2^{2} = 4$
* - 3
  - *Huitaine*
  - $2^{3} = 8$
* - 4
  - *Seizaine*
  - $2^{4} = 16$
* - 5
  - ...
  - $2^{5} = 32$
* - 6
  - ...
  - $2^{6} = 64$
* - 7
  - ...
  - $2^{7} = 128$
```
````

[^0]: Les noms sont au singulier car il ne peut pas y en avoir plus que 1 par niveau...

La forme canonique du nombre binaire $10101_{(2)}$ est : $1 \cdot 2^4 + 0 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0$

````{panels}
:columin: col-md

La forme canonique nous permet de faire facilement le passage de la base 2 à la base 10 :
^^^
\begin{equation*}
10101_{(2)} = 1.2^4 + 0.2^3 + 1.2^2 + 0.2^1 + 1.2^0 = 21_{(10)}
\end{equation*}
````
### Exercice 2

Réalisation d'un tableau de conversion des 11 premières puissances de 2.

```{math}
\begin{array}{|l|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\text{Coefficient} & 2^{10} & 2^9 & 2^8 & 2^7 & 2^6 & 2^5 & 2^4 & 2^3 & 2^2 & 2^1 & 2^0  \\ 
\hline
\text{Valeur} & 1024 & 512 & 256 & 128 & 64 & 32 & 16 & 8 & 4 & 2 & 1\\ 
\hline
\end{array} 
```

### Exercice 3

Faire les conversions décimales de plusieurs nombres binaires

* $10101101_{(2)}$
* $01110010_{(2)}$
* $1111_{(2)}$
* $1111111_{(2)}$

### Exercice 4

Faire les conversions décimales de nombres binaires spécifiques

* $1_{(2)}$
* $10_{(2)}$
* $100_{(2)}$
* $1000_{(2)}$
* $10000_{(2)}$
* $100000_{(2)}$
* $1000000_{(2)}$
* $10000000_{(2)}$

````{tip}
La dernière conversion de l'exercice 3 peut être obtenue rapidement si on remarque qu'il s'agit de 
\begin{equation*}
10000000000_{(2)} - 1 = 2^{10} - 1 = 1023_{(10)}
\end{equation*}
````

### Exercice 5

À l'aide du tableau de l'exercice 2, comment peut-on passer de la base 10 à la base 2 ?  
Faire les conversions binaires de différents nombres décimaux.

*Durée : 10-15 min*

(algo-tri.conclusion)=
## Conclusion

*Durée : 5-10 min*

(magiebinaire.encodage)=
## Encodage de l'information

*Durée : 10-15 min*

A l’instar du morse (0 = . ; 1 = - ), on peut utiliser le binaire pour (en)coder autre chose que des nombres. Introduire la notion du nombre de “mots” différents en fonction du nombre de bits.

```{math}
\begin{array}{|l|c|c|c|c|c|c|c|c|c|c|}
\hline
\text{Nombre de bits} & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
\hline
\text{Nombre} & 2^1 & 2^2 & 2^3 & 2^4 & 2^5 & 2^6 & 2^7 & 2^8 & 2^9 & 2^{10}  \\ 
 \text{de mots} & 2 & 4 & 8 & 16 & 32 & 64 & 128 & 256 & 512 & 1024\\ 
\hline
\end{array} 
```
### Exercice 6

Quelques questions pour ancrer l’idée. Au début l’encodage par l’intermédiaire des nombres rassure puis on essaye de s’en éloigner.

Combien de bits faut-il pour représenter :

* les mois de l’année ?
* les lettres de l’alphabet (préciser lequel) ? 
* le nombre d’élèves du gymnase ?
* la présence/absence des élèves étant donnée la liste de présence ?
* ...

(magiebinaire.explication)=
## Explication du tour

*Durée : 10-15 min.*

L’idée ici est d’essayer d’amener les élèves à comprendre en observant les cartes et guidées par des questions telles que :

1. Combien faut-il de bits pour encoder les chiffres de 1 (ou 0) à 63 ?
2. Combien y a-t-il de cartes pour le tour ?
3. Avec 6 bits je peux coder 64 “mots” différents, avec 1 bit de moins, combien ?
4. Combien y a-t-il de nombres sur une carte ?
5. Qu’ont en commun les nombres d’une même carte ?

### La solution

Regardez attentivement la carte qui contient un 2 en haut à gauche.  
Voici comment s'écrivent les nombres de cette carte en binaire:

````{panels}
:columin: col-md

Représentation binaire des chiffres de la carte n°2
^^^
<img src="./Carte2.png" alt="carte2" class="bg-primary" width="600px">
````

Chaque carte représente donc 1 des 6 bits nécessaire à l’encodage des entiers de 0 à 63 et les nombres présents sur la carte sont tous ceux dont ce bit est à 1 dans leur code binaire.  
Par conséquent l’information donnée par l’élève de présence ou non de son nombre sur une carte équivaut à la notion de 0 ou 1 sur un certain bit.  
Une fois toutes les cartes passées en revue il a donné le code binaire de son nombre secret !

(magiebinaire.plusloin)=
## Pour aller plus loin

Si on a du temps pour escalader la pyramide d’Anderson et Krathwohl[^1].

Les élèves doivent créer la version du tour pour le petit frère (ou petite sœur) avec 4 cartes.

1. Quels sont les nombres possibles ?
2. Combien y a-t-il de nombres par carte ?
3. Quels sont ces nombres ?

[^1]: LW, Anderson & DR, Krathwohl Eds. (2001). A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives.

### Ouvertures et questionnements

* Les valeurs des puissances de 2 sont des valeurs qu’ils connaissent déjà ! Capacité de stockage des clés USB, smartphones, SSD, etc.. Pourquoi ?
* Comment peut-on faire pour écrire des nombres négatifs, décimaux en binaire ?
* À compléter...

(magiebinaire.mobiliser)=
### Mobiliser les connaissances

Voici une énigme dont la solution utilise le principe de codage binaire.

#### L’énigme

Vous êtes le seigneur du canton de Vaud, et préparez votre mariage qui a lieu demain. Pour cette occasion, vous avez commandé 1000 bouteilles d’un excellent cru du Valais. Mauvaise idée, on vous apprend qu'une des bouteilles (et une seule) est empoisonnée. Le poison incolore, insipide et inodore, dont les effets sont dévastateurs (vomissements, convulsions, ...), provoque la mort en moins de 24h.  

Pour trouver la bouteille empoisonnée, vous disposez de 10 rats testeurs (vous avez malheureusement aboli l’esclavage et personne ne souhaite faire ce métier). Votre problème, il est midi et les bouteilles doivent être servies demain à 14h. Comment allez-vous procéder pour pouvoir servir les 999 bouteilles non empoisonnées à votre mariage ?

#### La solution

Le fait qu'un rat meurt ou non nous donne de l'information. Ce qu'on doit trouver, c'est comment cette information peut nous permettre d'identifier la bouteille empoisonnée. 

Il suffit d’identifier chaque bouteille par un nombre binaire unique, et chaque rat par un numéro (non binaire celui-ci).  

Ce nombre binaire comportera autant de bits que de rats, et la position d'un bit dans le nombre  correspondra à un numéro de rat (avec 10 rats on a 1024 possibilités donc un peu de marge). Si ce bit est à 1, alors cela signifie que ce rat aura gouté cette bouteille.  

Par exemple la bouteille 3 sera codée 0110 (si on code sur 4 bits, c'est à dire 4 rats), ce qui signifie que les rats 2 et 3 l’auront gouté.

Une fois que toutes les bouteilles ont été goutées, on regarde les numéros des rats décédés. Tous ont leur bit à 1 dans la bouteille empoisonnée, leur mort nous apporte l'information nécessaire.  

Si par exemple on avait le rat 1 et le 3 de mort, alors la bouteille correspondante serait (0101), c'est à dire la numéro 5 !




