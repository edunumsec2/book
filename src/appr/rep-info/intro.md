(appr:repinfo:intro)=
# Introduction

Dans ce chapitre, on s’intéresse à la manière dont un {glo}`ordinateur|ordinateur` représente l’information afin de pouvoir la traiter automatiquement. En informatique, l’information est un élément de connaissance — texte, image, son, etc. — pouvant être {glo}numerisation|numérisée, {glo}stockage|stockée et/ou {glo}transmission|transmise au moyen d’un support et d’un mode de codification normalisé.


````{didyouknow} 

Le mot **informatique** est la concaténation de «&nbsp;information&nbsp;» et «&nbsp;automatique&nbsp;».
````

Une des questions centrales de ce chapitre est d’identifier les caractéristiques de la transformation du réel qui donnent une représentation assez précise pour que les ordinateurs puissent la {glo}traitement|traiter de manière fiable.

Mais avant de découvrir le code choisi pour représenter l’information à l’intérieur d’un ordinateur, passons en revue plusieurs alphabets et systèmes de représentation de l’information qui ont été utilisés au cours de l’histoire.

## Alphabets anciens et traditionnels

Depuis qu'elle existe, l'espèce humaine a créé de nombreux alphabets, ainsi que de nombreux {glo}`sysco|systèmes de communication`. Depuis les [sumériens](https://fr.wikipedia.org/wiki/Sum%C3%A9rien) qui utilisaient des {glo}`picto|pictogrammes` et [l’écriture cunéiforme](https://fr.wikipedia.org/wiki/Cun%C3%A9iforme), en passant par les égyptiens et leurs [hiéroglyphes](https://fr.wikipedia.org/wiki/%C3%89criture_hi%C3%A9roglyphique_%C3%A9gyptienne), les chinois et leurs [idéogrammes](https://fr.wikipedia.org/wiki/Caract%C3%A8res_chinois) pour arriver aux symboles de nos alphabets actuels (voir le synoptique ci&#8209;dessous), l'espèce humaine n’a eu de cesse de mettre au point des systèmes pour représenter l’information et la {glo}`transmission|transmettre`.

::::{tab-set}
:::{tab-item} Sumérien
```{image} media/cuneiform.jpg
:height: 300px
align: center
```
:::

:::{tab-item} Égyptien
```{image} media/hieroglyphs.jpg
:height: 300px
align: center
```
:::

:::{tab-item} Chinois
```{image} media/chinois.png
:height: 300px
align: center
```
:::

:::{tab-item} Synoptique
```{image} media/synoptique.png
:height: 300px
align: center
name:fig-synoptique
```
:::
::::


Ainsi, il existe différentes manières de représenter une même information : par exemple, un *nombre* peut s’écrire en chiffres classiques, en chiffres romains ou même avec des lettres, tandis qu’un *mot* peut être exprimé dans différentes langues, en code Morse ou à l’aide d’idéogrammes. On trouve des exemples célèbres et bien documentés de {glo}`sysco|systèmes de communication` depuis l'Antiquité grecque.

## Le carré de Polybe

Utilisé en Grèce Antique pour transmettre des messages entre cités voisines, le carré de Polybe utilisait des torches enflammées en guise de signaux. 

Cinq torches «&nbsp;à gauche&nbsp;», cinq torches «&nbsp;à droite&nbsp;», étaient séparées par un espace suffisamment grand pour être identifiables à longue distance. Une torche pouvait être soit allumée, soit éteinte. Le nombre de torches allumées à gauche, de 1 à 5, représentait la ligne d'un tableau de décodage (voir la [figure ci&#8209;dessous](#fig-polybe)), le nombre de torches allumées à droite représentait la colonne de ce même tableau.


````{figure} media/Polybe.png
---
height: 300px
name: fig-polybe
align: center
---
Dans le carré de Polybe, la lettre «&nbsp;s&nbsp;» se code avec quatre torches à gauche et trois torches à droite.
````

````{note} 

Dans l'exemple ci&#8209;dessus, on utilise les lettres de l'alphabet, mais il est plus probable qu'à l'époque les cités voisines utilisaient des expressions toutes faites dans chacune des cases, comme «&nbsp;l'ennemi est à nos portes&nbsp;» ou «&nbsp;envoyez-nous de l'aide&nbsp;». 
````

## Le télégraphe de Chappe

Grâce à l'invention du [télescope](https://fr.wikipedia.org/wiki/T%C3%A9lescope) au XVII<sup>e</sup> siècle, les distances avec lesquelles les villes pouvaient communiquer entre elles ont largement augmenté. L'information a commencé à circuler à une vitesse étonnante. Des messages pouvaient être transmis sur une longue distance par l'intermédiaire de relais espacés d'une dizaine de kilomètres et situés sur des hauteurs. 

[Claude Chappe](https://fr.wikipedia.org/wiki/Claude_Chappe), inventeur français, développe en 1794 un {glo}`telegraphe|télégraphe` capable de relier des villes entre elles sur plusieurs dizaines de kilomètres grâce à un système de bras mobiles (voir la [figure ci&#8209;dessous](#fig-chappe)), qui ressemblent aux signaux que pourrait faire un être humain sur le tarmac d'un aéroport. 


````{figure} media/Chappe.png
---
height: 400px
name: fig-chappe
---
Le télégraphe de Chappe émet des signaux ressemblant aux bras d'un être humain. 
````



````{didyouknow}
[Le piratage du télégraphe Chappe](https://fr.wikipedia.org/wiki/Piratage_du_t%C3%A9l%C3%A9graphe_Chappe) est un détournement du réseau de télégraphie optique français entrepris par deux hommes d'affaires bordelais, Louis et François Blanc, entre 1834 et 1836, afin de connaître avant tout le monde le prix de certaines actions à la Bourse de Paris.

Le piratage a été rendu possible par la corruption d'un agent télégraphique de Tours, qui ajoutait discrètement le prix actuel des actions aux messages envoyés par l'État.
````

## Le Morse

Grâce à la découverte de l’électricité au début du XIX<sup>e</sup> siècle, puis aux progrès techniques qui ont permis de la capter et de la transmettre, il est devenu possible d’utiliser le réseau électrique pour envoyer des messages. En 1832 nait le [code Morse](https://fr.wikipedia.org/wiki/Code_Morse_international), illustré dans la [figure ci&#8209;dessous](#fig-morse), qui s'impose rapidement comme un standard de communication. 

Bien sûr, le Morse peut être utilisé aussi avec des signaux lumineux, ou sonores, mais la plupart du temps il est utilisé sur les lignes électriques qui se développent à l'époque. 

[Vous trouverez ici](https://morsedecoder.com/) un traducteur du langage naturel vers le Morse.

````{micro}
Amusez-vous avec votre assistant vocal en lui demandant par exemple : «&nbsp;Salut Siri. Quel est le code Morse pour *j'ai envie de dormir* ?&nbsp;».
````

````{figure} media/morse.png
---
height: 600px
name: fig-morse
align: center
---
Le code Morse est le système de représentation de l'information qui se rapproche le plus du langage binaire de l'informatique moderne. 
````

Si vous observez le [code Morse](https://fr.wikipedia.org/wiki/Code_Morse_international) sur la [figure ci&#8209;dessus](#fig-morse), Si vous observez le code Morse sur la figure ci&#8209;dessous, vous remarquerez que les signaux utilisés pour représenter les lettres ne suivent pas simplement l’ordre de l’alphabet, car il est plus économique de coder les lettres les plus fréquentes avec des codes plus courts (voir [figure ci&#8209;dessous)](#fig-distribution).

```{figure} media/letterdistribution.png
---
height: 420px
name: fig-distribution
align: center
---
Fréquences moyennes des lettres dans la langue anglaise.
```


````{didyouknow}

À l'époque où les transmissions télégraphiques en code Morse sont payées à l'unité d'information, donc la lettre, des codex spécifiques sont développés par les utilisateurs pour utiliser le moins de caractères possibles. C'est exactement la même situation qui s'est produite avec l'arrivée des [SMS](https://fr.wikipedia.org/wiki/Short_Message_Service) dans les années 1990, où les utilisateurs payaient au caractère. Aujourd'hui, même s'il est rare de payer à l'unité d'information, ce genre de raccourcis existent encore, mais surtout pour un avantage de vitesse. 

```{image} media/morsecodeshort.png
:height: 500px
:width: 500px
```

Le désavantage de ces codex d'abréviations est leur faible degré de standardisation. Comment savoir quel codex est utilisé ? Et surtout : comment faire pour que tout le monde s'accorde sur le codex ? 

La réponse à cette question est l'apport le plus essentiel de l'introduction du code binaire, et des standards de représentation de l'information qui l'ont suivi : un langage pour les contrôler tous. 
````


## Le binaire

À partir du moment où le [Morse](https://fr.wikipedia.org/wiki/Code_Morse_international) a été inventé comme système de {glo}`codage|codage` et de {glo}`transmission|transmission` de l'information par l'électricité, il ne manquait plus que quelques éléments pour commencer à construire les {glo}`ordinateur|ordinateurs`.

;nb une pièce technologique, qui permettrait de {glo}`transmission|transmettre` pour ainsi dire cette information : le {glo}`transistor|transistor` (voir {ref}`architecture des ordinateurs <archi>`).

Ensuite un {glo}`codage|code` plus élaboré que le Morse pour pouvoir représenter tous les types d'informations possibles à partor d'une alternative entre deux états : courant ou pas de courant ; allumé ou éteint ; vrai ou faux ; 1&nbsp;ou&nbsp;0.

Ce {glo}`codage|code` est le {glo}`codebinaire|code binaire`. Il permet, en utilisant uniquement des 0 et des 1, de représenter n'importe quel type d'information : des chiffres, du texte, des images, du son, des vidéos, etc. 

```{question} Question 1
Pourquoi la lettre «&nbsp;e&nbsp;», en Morse, est-elle représentée par un seul point ? 
* {v}`Parce que c'est la lettre la plus utilisée en anglais.`
* {f}`Par hasard.`
* {f}`Parce que c'est la lettre la plus rare en anglais.`
* {f}`Parce que c'était la lettre préférée de l'inventeur du Morse.`
```

```{question} Question 2
Que signifie informatique ? 
* {f}`Information + quantique.`
* {f}`Information + technique.`
* {v}`Information + automatique.`
* {f}`Information + pratique`
```
