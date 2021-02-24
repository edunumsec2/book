<!-- ````{image} 02_media/accueil/ASCII.png
:name: information
:height: 200px
:width: 1000px
:alt: Information
:align: center
```` 
 -->


Représentation de l'information
==================================

Le monde numérique est extrêmement vaste. Au moyen d’applications dédiées, il est possible d’y travailler sur une certaine représentation du réel. Des textes, des images, des sons ou des données financières peuvent tout aussi bien y être manipulées.

Pourtant, il faut avoir conscience qu’aussi “réelles” que ces représentations peuvent paraître, elles n’en sont pas moins des représentations.

Dans cette section, nous allons comprendre comment les ordinateurs parviennent à représenter le monde et les sacrifices qui doivent être faits pour simplifier le réel jusqu’à ce que sa représentation puisse être manipulée automatiquement au moyen de calculs élémentaires.

## Contenus du chapitre

````{panels}

```{link-button} content/theme/representation-information/representation-entiers/eleve.ipynb
:text: Représentation des entiers
:type: ref
:classes: stretched-link
```
---

```{link-button} content/demostests/edito/syntaxemyst.md
:text: Représentation des caractères
:type: ref
:classes: stretched-link
```
---

```{link-button} content/demostests/edito/syntaxemyst.md
:text: Représentation des images
:classes: stretched-link
```
---
````

## Objectifs du chapitre

{fa}`check, text-success mr-1`Découvrir la **représentation** des nombres entiers, des caractères, des images et des sons.

{fa}`check, text-success mr-1`Comprendre le **stockage** et la **manipulation** des données.

{fa}`check, text-success mr-1`Appréhender l’importance de la **redondance**.

## Personnages-clés

````{tabbed} Grace Hopper
```{image} 02_media/accueil/gracehopper.jpeg
:alt: Grace Hopper
:height: 500px
:width: 350px
```
[**Grace Hopper**](https://fr.wikipedia.org/wiki/Grace_Hopper) est une informaticienne d'origine américaine. À partir de 1957, elle travaille pour IBM, où elle défend l'idée qu'un programme devrait pouvoir être écrit dans un langage proche de l'anglais plutôt que d'être calqué sur le langage machine, comme l'assembleur. De cette idée naît le langage COBOL en 1959.
````

````{tabbed} Claude Shannon
```{image} 02_media/accueil/claudeshannon.jpg
:alt: Claude Shannon
:height: 500px
:width: 350px
```
Pendant la Seconde Guerre mondiale, [**Claude Shannon**](https://fr.wikipedia.org/wiki/Claude_Shannon) travaille pour les services secrets de l'armée américaine, en cryptographie. Il est chargé de localiser de manière automatique dans le code ennemi les parties signifiantes cachées au milieu du brouillage. C'est ce qui le mènera par la suite à développer une mesure mathématique de la quantité d'information contenue dans un message. 
````

```{panels} 
:column: col-lg
☕ Tous les livres du monde VS Tik Tok
^^^
[Le projet Gutenberg](https://www.gutenberg.org/) est une immense bibliothèque en ligne qui rassemble une grande partie des livres ayant été écrits à toutes les époques. Sa taille est de 60GB. 1mn de vidéo smartphone HD pèse environ 100MB. Ce qui signifie que la quasi totalité des livres écrits par l'espère humaine correspond à 100 vidéos smartphones. Quand on sait que Tik Tok possède 500 millions d'utilisateurs actifs, cela devient abyssal.
```