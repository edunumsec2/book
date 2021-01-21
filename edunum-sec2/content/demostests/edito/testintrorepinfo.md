````{image} images/introduction/data.jpeg
:name: data
:height: 200px
:width: 1000px
:alt: Data
:align: center
`````

# Intro : Représentation de l'information


*Note : ceci est un test*

Dans ce chapitre nous allons nous concentrer sur la représentation de l'information de façon à ce qu'un ordinateur puisse la traiter automatiquement.  

````{admonition}
:class: note
Le mot **informatique** et la concaténation de **information** et **automatique**.
````

En informatique, l'information est un élément de connaissance (donnée numérique ou textuelle, image, son, etc.) susceptible d'être conservé, traité ou transmis à l'aide d'un support et d'un mode de codification normalisé.

Une des questions centrale est d'identifier les caractéristiques des représentations qui permettent une représentation suffisamment précise pour permettre aux ordinateurs de les traiter de manière fiable.

%![Hmm](images/introduction/hmm.gif)

## Objectifs

- Comprendre le système et l’arithmétique binaire.  
- Découvrir la représentation des nombres entiers, des caractères, des images et des sons.
- Comprendre le stockage et la manipulation des données.
- Appréhender l’importance de la redondance.

## Introduction

L’histoire de l’humanité est marquée par la création de multiples systèmes pour communiquer. Depuis les sumériens qui utilisaient des pictogrammes et l’écriture cunéiforme, en passant par les égyptiens et leurs hiéroglyphes, l’écriture crétoise, les chinois et leurs idéogrammes pour arriver aux symboles de nos alphabets actuels, l’homme n’a eu de cesse de mettre au point des système pour représenter l’information et la transmettre.

````{tabbed} Sumérien
```{image} images/introduction/cuneiform.jpg
:height: 350px
:width: 500px
```
````

````{tabbed} Égyptien
```{image} images/introduction/hieroglyphs.jpg
:height: 350px
:width: 500px
```
````

````{tabbed} Crétois
```{image} images/introduction/cretois.png
:height: 350px
:width: 500px
```
````

````{tabbed} Chinois
```{image} images/introduction/chinois.gif
:height: 350px
:width: 500px
```
````

````{tabbed} Évolution
```{image} images/introduction/evolution.jpg
:height: 350px
:width: 500px
```
````



````{panels}
:column: col-lg

Activité
^^^
Trouvez différentes représentations de la même information

```{toggle} 
- Nombres en chiffres classique, romain, lettres
- Mot en différentes langues, morse, idéogramme
- Symbole danger, stop, paix
```
````

Ce qu'il faut comprendre c'est que pour créer une communication efficace il existe toujours un compromis entre plusieurs paramètres : le nombre de symboles qu'on se donne au départ, le nombre de mots que l'on veut être capable d'exprimer, la longueur de la transmission du message, sa lisibilité, la possibilité technique de la transmission, etc.

On trouve des exemples célèbres et bien documentés depuis l'antiquité grecque.

### Le carré de Polybe

Utilisé dans l'antiquité grecque pour transmettre des messages entre cités voisines, ce système utilise des torches enflammées en guise de signaux. 

Cinq torches "à gauche", cinq torches "à droite" séparées par un espace suffisamment grand pour être identifiable à longue distance. Une torche peut être soit allumée, soit éteinte. Le nombre de torches allumées à gauche, de 1 à 5, représente les colonnes, le nombre de torches allumées à droite représente les lignes. 

````{image} images/introduction/polybe.png
:height: 500px
:width: 350px
````

````{admonition}
:class: note
Dans cet exemple, on utilise les lettres de l'alphabet, mais il est bien plus probable qu'à l'époque les cités voisines utilisaient des expressions toutes faites dans chacune des cases, comme "l'ennemi est à nos portes" ou "envoyez de l'aide".
````

### Le télégraphe de Chappe

Grâce à l'invention du téléscope au XVIIème siècle, les distances avec lesquelles les villes pouvaient communiquer entre elles ont largement diminué. L'information a commencé à circuler à une vitesse étonnante. 

Claude Chappe, inventeur français, développe en 1794 un télégraphe capable de relier des villes entre elles sur plusieurs dizaines de kilomètres grâce à un système de bras mobiles, qui ressemblent aux signaux que pourrait faire un être humain sur le tarmac d'un aéroport. 

````{image} images/introduction/chappe.jpeg
:height: 500px
:width: 350px
````

````{admonition} Piratage du télégraphe Chappe
:class: warning
[Le piratage du télégraphe Chappe](https://fr.wikipedia.org/wiki/Piratage_du_t%C3%A9l%C3%A9graphe_Chappe) est un détournement du réseau de télégraphie optique français entrepris par deux hommes d'affaires bordelais, Louis et François Blanc, entre 1834 et 1836, afin de connaître avant tout le monde la clôture des cours de la rente à la Bourse de Paris.

Le piratage a été rendu possible par la corruption d'un agent télégraphique de Tours, qui ajoutait discrètement le chiffre du cours aux messages envoyés par l'État.
````


### Le morse

Grâce à la découverte de l'électricité au début du XIXème siècle, et les améliorations techniques faites pour la capturer et la transmettre, on a pu utiliser le réseau électrique pour envoyer des messages. En 1832, nait le code Morse, qui s'impose rapidement comme un standard de communication. 
Bien sûr, le morse peut être utilisé aussi avec des signaux lumineux, ou sonores, mais la plupart du temps il est utilisé sur les lignes électriques qui se développent à cet époque. 

`````{sidebar} Raccourcis en morse
À l'époque où les transmissions télégraphiques en code morse sont payées à l'unité d'information, donc la lettre, des *codex* spécifiques sont développés par les utilisateurs pour utiliser le moins de caractères possibles. C'est exactement la même situation qui s'est produite avec l'arrivée des sms dans les années 2000, où les utilisateurs payaient au caractère. Aujourd'hui, même s'il est rare de payer à l'unité d'information, ce genre de raccourcis existent encore, mais surtout pour un avantage de vitesse. 
````{toggle}
```{image} images/introduction/morsecodeshort.png
:height: 500px
:width: 350px
```
Le désavantage de ces **codex d'abbréviations** est leur *transférabilité*. Comment savoir quel codex est utilisé ? Et surtout : comment faire pour que tout le monde s'accorde sur le codex ? 

La réponse à cette question est l'apport le plus essentiel de l'introduction du code binaire, et des standards de représentation de l'information qui l'ont suivi. 
````
`````

````{image} images/introduction/morse.png
:height: 500px
:width: 350px
````

```{question} Question
Pourquoi la lettre "e" est-elle représentée par un seul point ? 
* {v}`Parce que c'est la lettre la plus utilisée en anglais.`
* {f}`Par hasard.`
* {f}`Parce que c'est la lettre la plus rare en anglais.`
* {f}`Parce que c'était la lettre préférée de l'inventeur du Morse.`
```

`````{admonition} Note
Si vous observez le code Morse, vous remarquerez que les signaux utilisés pour représenter les lettres ne suivent pas simplement l'ordre de l'alphabet. 
````{toggle} 
Ceci est une extension de la réponse à la question ci-dessus, puisqu'il est logique de coder les lettres les plus fréquentes avec les signaux les plus courts. 
```{image} images/introduction/letterdistribution.png
:height: 500px
:width: 350px
```
`````

### Le binaire

À partir du moment où le Morse a été inventé comme système de codage et de transmission de l'information par l'électricité, il ne manquait plus que quelques éléments pour commencer à construire les ordinateurs.

Une pièce technologique, qui permettrait de "stocker" pour ainsi dire cette information : le transistor (cf : chapitre "architecture des ordinateurs").

Un *vocabulaire* plus élaboré que le Morse pour pouvoir représenter tous les types d'informations possibles à partir d'une alternative entre deux états : courant ou pas courant ; allumé ou éteint ; vrai ou faux ; 1 ou 0.  

Ce *vocabulaire* est le **code binaire**. Il permet, en utilisant uniquement des 0 et des 1, de représenter n'importe quel type d'information : des chiffres, du texte, des images, du son, des vidéos, etc. 

````{image} images/introduction/binary.gif
:height: 500px
:width: 350px
````

`````{admonition} Note
Ce principe est si puissant que c'est devenu le *langage des ordinateurs*. Comme votre smartphone est en fait un ordinateur, tout ce que vous y voyez quotidiennement, vos discussions, l'image d'un chaton, votre série préférée, ou encore la dernière chanson que vous écoutez, ne sont en réalité qu'une suite de 0 et de 1.
````{toggle}
```{image} images/introduction/hmm.gif
```
Même lui... Oui. 
````
``````

<!---
Au milieu du XIXe siècle, les fragments d’un papyrus vieux de plus 4000 ans découvert sur le site de Thèbes sont rassemblés par l’égyptologue écossais Henry Rhind. Aujourd’hui exposés au British Museum de Londres, les cinq mètres du document montrent que les égyptiens utilisaient une représentation binaire des nombres pour effectuer les opérations arithmétiques de base – addition, soustraction, multiplication et division – pour résoudre des problèmes d’algèbre et de géométrie.

Au milieu du XXe siècle, les difficultés liées à l’utilisation du système décimal dans les premiers calculateurs amène les chercheurs à exploiter cette ancienne notion que les multiplications et les divisions dans le système binaire se réalisent au moyen de simples additions et soustractions. L’informatique digitale, basée sur le système binaire, s’est imposée jusqu’à ce jour.
-->
