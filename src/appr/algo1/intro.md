
```{htmlonly}

<style>
.button {
  background-color: white;
  border: 1px solid;
  border-color: black;
  font-family:"Lato",sans-serif;
  font-weight:350;
  color: black!important;
  padding: 10px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
.button:hover {
  text-decoration:none;
  background-color: black; 
  color: white!important;
}
.round-button {
    display:block;
    width:100px;
    height:100px;
    line-height:17px;
    border:0px ;
    border-radius: 50%;
    color:#6069db;
    text-align:center;
    text-decoration:none;
    display: table-cell;
    vertical-align: middle;
    background: #6069db;
    box-shadow: 0 0 0px gray;
    font-size:14px;
    font-weight:bold;
    }
</style>

<div align="right"> 
    <a href="https://files.modulo-info.ch/Algorithmique_20220322_I.pdf" target="_blank" class="round-button">
         <font color=white id="demo">Cliquer ici pour <br>dossier</font>
    </a>
</div>

```



# Introduction

## Quoi ? 

Nous avons tous entendu parler des algorithmes dans les médias. Normal, c’est le mot à la mode et que tout le monde utilise sans vraiment le comprendre. Ils sont partout, ils font toutes sortes de choses, même nous manipuler. Pourquoi en parle&#8209;t&#8209;on de la même manière que des extraterrestres ? Dans ce cours, nous allons tenter de revenir sur terre, parce que les algorithmes ce n’est pas si compliqué que ça. On apprendra à les définir, à les faire marcher et surtout à reconnaître la différence entre un programme et un algorithme, ainsi qu'entre un « bon » et un « mauvais » algorithme. 

<!--
Il y a de fortes chances que vous ayez déjà entendu parler {glo}`algo|d'algorithmes` dans les médias. Il y a aussi de fortes chances que ce mot évoque pour vous des notions bien différentes de celles de votre voisin. L'objectif de ce chapitre est de vous éclairer sur la notion d'algorithme et la distinction avec la notion de programme informatique.
-->

## Pourquoi ? 

Les algorithmes existent depuis des millénaires. On doit le nom d'algorithme à Al&#8209;Khwârizmî, mathématicien perse né en l'an 780 dont les ouvrages ont contribué à la popularisation des chiffres arabes en Europe, ainsi que la classification de plusieurs algorithmes connus à ce moment. D'ailleurs l'algorithme le plus connu, l'algorithme d'Euclide, date environ de l'an 300 av J.&#8209;C. et permet de calculer le plus grand diviseur commun de deux nombres. Si Euclide a bien laissé des traces écrites de cet algorithme, il est vraisemblable qu'il ait puisé cette connaissance auprès de disciples de Pythagore lui&#8209;même. 

Les algorithmes sont devenus très populaires aujourd'hui grâce à la machine qui a permis de les automatiser. Que ce soit dans votre smartphone, sur un ordinateur ou dans un système embarqué, ils permettent de résoudre une quantité de problèmes, facilement et avec une rapidité impressionnante.

## Comment ?

Dans un premier temps nous allons nous intéresser à la notion même d'algorithme : qu'est&#8209;ce qui caractérise un algorithme et comment le faire exécuter par une machine ? Nous allons voir que pour un problème donné il existe de nombreuses solutions, mais que toutes ces solutions ne sont pas de *bonnes* solutions, selon le contexte dans lequel on tente de résoudre le problème. 


## Objectifs d'apprentissage

À la fin de ce chapitre, vous saurez ce qu'est un algorithme et vous serez capable de transcrire des algorithmes en programmes. Vous saurez résoudre des problèmes, en décomposant leur solution en étapes à suivre. Vous verrez également que pour un même problème, on peut avoir plusieurs solutions avec des propriétés, avantages et désavantages différents. 
<br>

* Se familiariser avec la notion d’algorithme.

* Savoir résoudre des problèmes, en décomposant leur solution en étapes à suivre.

* Savoir que pour un même problème, on peut avoir plusieurs solutions avec différents propriétés, avantages et désavantages.

* Être capable de transcrire un algorithme dans un programme.
<br>

Bienvenue dans le monde fascinant des algorithmes.


`````{htmlonly}

## Personnages&#8209;clés


:::::{grid} 1 2 2 2
:gutter: 2

::::{grid-item}
:::{card}
:img-top: media/Al-Khwarizmi.png


Al&#8209;Khwârizmî 🇺🇿
^^^^^
***780&#8209;850***

Considéré comme le père de l’algèbre [**Al&#8209;Khwârizmî**](https://fr.wikipedia.org/wiki/Al-Khw%C3%A2rizm%C3%AE) a vécu au VIII$^{e}$ siècle dans le Moyen&#8209;Orient. Il est l'auteur de plusieurs ouvrages de mathématiques, d’astronomie et de géographie. Son nom est à l’origine du mot **algorithme**.
:::
::::

::::{grid-item}
:::{card}
:img-top: media/Dijkstra.jpg


Edsger Dijkstra 🇳🇱
^^^^^
***1930&#8209;2002***

[**Edsger Wybe Dijkstra**](https://fr.wikipedia.org/wiki/Edsger_Dijkstra) est un mathématicien et informaticien néerlandais du XX$^{e}$ siècle. Il reçoit en 1972 le prix Turing pour ses contributions sur la science et l’art des langages de programmation et au langage Algol. Il est le concepteur de l'algorithme éponyme de recherche du plus court chemin. 
:::
::::
:::::

`````

