(repinfo)=
# Représentation de l'information

```{toctree}
:maxdepth: 2
:hidden:
:numbered: 2
intro
entiers
caracteres
images
son
redondance
conclusion
```

`````{htmlonly}
Le monde numérique est extrêmement vaste. Au moyen d’applications dédiées, il est possible d’y travailler sur une certaine représentation du réel. Des textes, des images, des sons ou des données financières peuvent y être manipulées.

Pourtant, il faut avoir conscience qu’aussi «réelles» que ces représentations puissent paraître, elles restent des représentations.

Dans cette section, nous allons comprendre comment les ordinateurs parviennent à représenter le monde et les compromis qui doivent être faits pour simplifier le réel jusqu’à ce que sa représentation puisse être manipulée automatiquement au moyen de calculs élémentaires.


## Objectifs

* Découvrir la **représentation binaire** des nombres entiers, des caractères, des images et des sons.

* Comprendre les notions de **compression** et de **stockage** des données.

* Appréhender l’importance de la **redondance**.


## Personnages-clés

:::::{grid} 1 2 2 2
:gutter: 2

::::{grid-item}
:::{card}
:img-top: media/gracehopper.jpeg

Grace Hopper 🇺🇸
^^^^^
***1906-1992***

[**Grace Hopper**](https://fr.wikipedia.org/wiki/Grace_Hopper) est une informaticienne d'origine américaine. À partir de 1957, elle travaille pour IBM, où elle défend l'idée qu'un programme devrait pouvoir être écrit dans un langage proche de l'anglais plutôt que d'être calqué sur le langage machine, comme l'assembleur. De cette idée naît le langage COBOL en 1959.
:::
::::

::::{grid-item}
:::{card}
:img-top: media/claudeshannon.jpg
Claude Shannon  🇺🇸
^^^^^
***1916-2001***

Pendant la Seconde Guerre mondiale, [**Claude Shannon**](https://fr.wikipedia.org/wiki/Claude_Shannon) travaille pour les services secrets de l'armée américaine, en cryptographie. Il est chargé de localiser de manière automatique dans le code ennemi les parties signifiantes cachées au milieu du brouillage. C'est ce qui le mènera par la suite à développer une mesure mathématique de la quantité d'information contenue dans un message. 
:::
::::
:::::
`````

