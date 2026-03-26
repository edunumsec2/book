
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


(algo)=
# Algorithmique

```{toctree}
:maxdepth: 2
:hidden:
:numbered: 2
algorithmes
tri
algo-progs

principes
recherche
heuristiques
tris
recursivite
conclusion
```

## Quoi ? 

Un **<span style="color:rgb(89, 51, 209)">{glo}`algo|algorithme`</span>**  permet de décrire la solution d'un problème étape par étape, afin qu'elle soit intelligible par une machine. Pour résoudre un problème informatique, il faut commencer par le décomposer en sous&#8209;problèmes. Et pour chacun de ces sous&#8209;problèmes, il faut décrire précisément les opérations à réaliser pour le résoudre.

Il existe de nombreux algorithmes qui permettent de résoudre un problème, mais ils ne se valent pas tous. L’**<span style="color:rgb(89, 51, 209)">algorithmique</span>** étudie les propriétés des algorithmes, afin de nous aider à décider quel est le meilleur algorithme à utiliser. 

<!--
Nous avons tous entendu parler des algorithmes dans les médias. Normal, c’est le mot à la mode et que tout le monde utilise sans vraiment le comprendre. Ils sont partout, ils font toutes sortes de choses, même nous manipuler. Pourquoi en parle&#8209;t&#8209;on de la même manière que des extraterrestres ? Dans ce cours, nous allons tenter de revenir sur terre, parce que les algorithmes ce n’est pas si compliqué que ça. On apprendra à les définir, à les faire marcher et surtout à reconnaître la différence entre un programme et un algorithme, ainsi qu'entre un « bon » et un « mauvais » algorithme. 

Il y a de fortes chances que vous ayez déjà entendu parler {glo}`algo|d'algorithmes` dans les médias. Il y a aussi de fortes chances que ce mot évoque pour vous des notions bien différentes de celles de votre voisin. L'objectif de ce chapitre est de vous éclairer sur la notion d'algorithme et la distinction avec la notion de programme informatique.
-->

```{figure} media/Shadok.jpeg
---
alt: devise shadok
width: 300px

```

## Pourquoi ? 

Les algorithmes sont partout. Ils analysent vos photos, vos déplacements et votre activité sur des plateformes informatiques. Ils vous proposent des contenus à regarder et composent votre fil d'actualité. Il est important de comprendre ce qu'il y a derrière.

<!--
Les algorithmes existent depuis des millénaires. On doit le nom d'algorithme à Al&#8209;Khwârizmî, mathématicien perse né en l'an 780 dont les ouvrages ont contribué à la popularisation des chiffres arabes en Europe, ainsi que la classification de plusieurs algorithmes connus à ce moment. D'ailleurs l'algorithme le plus connu, l'algorithme d'Euclide, date environ de l'an 300 av J.&#8209;C. et permet de calculer le plus grand diviseur commun de deux nombres. Si Euclide a bien laissé des traces écrites de cet algorithme, il est vraisemblable qu'il ait puisé cette connaissance auprès de disciples de Pythagore lui&#8209;même. 

Les algorithmes sont devenus très populaires aujourd'hui grâce à la machine qui a permis de les automatiser. Que ce soit dans votre smartphone, sur un ordinateur ou dans un système embarqué, ils permettent de résoudre une quantité de problèmes, facilement et avec une rapidité impressionnante.

-->

## Comment ?

Dans un premier temps nous allons nous intéresser à la notion même d'**<span style="color:rgb(89, 51, 209)">algorithme</span>** : comment décomposer la solution d'un problème en étapes ? 

Dans un deuxième temps, nous allons aborder la notion de **<span style="color:rgb(89, 51, 209)">complexité</span>** qui permet de comparer différents algorithmes entre eux. Si plusieurs solutions existent, alors il faut choisir la plus rapide. Mais comment déterminer la vitesse d’un algorithme ? Et sera‑t‑elle la solution la plus rapide dans tous les cas ? 

Finalement, si vous le souhaitez, vous pouvez ouvrir la porte merveilleuse de la **<span style="color:rgb(89, 51, 209)">récursivité</span>**, à la manière des *Infinity Mirror Room* de Yayoi Kusama.

```{figure} media/Kusama.jpeg
---
alt: Infinity Mirror Room de Yayoi Kusama
width: 600px
```


## Objectifs d'apprentissage

À la fin de ce chapitre, vous saurez ce qu'est un algorithme et vous serez capable de transcrire des algorithmes en programmes. Vous saurez résoudre des problèmes, en décomposant leur solution en étapes à suivre. Vous verrez également que pour un même problème, on peut avoir plusieurs solutions avec des propriétés, avantages et désavantages différents. 
<br>

* Se familiariser avec la notion d’algorithme.

* Savoir résoudre des problèmes, en décomposant leur solution en étapes à suivre.

* Savoir que pour un même problème, on peut avoir plusieurs solutions avec différents propriétés, avantages et désavantages.

* Être capable de transcrire un algorithme dans un programme.

* Pouvoir déterminer quelle est la meilleure solution pour un problème donné, en fonction de critères objectifs.  

* Comprendre pourquoi certains problème simples n'ont pas de solution exacte.

* [Optionnel] Créer des fonctions récursives, qui s'appellent elles&#8209;mêmes.  




`````{htmlonly}

## Personnages clés


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
:img-top: media/Margaret.jpg


Margaret Hamilton 🇺🇸
^^^^^
***1902&#8209;1985***

L'informaticienne [**Margaret Hamilton**](https://fr.wikipedia.org/wiki/Margaret_Hamilton_(informaticienne)) a permis le succès de la mission Apollo 11, la première mission «humaine» sur la Lune. Elle a inventé le terme de **software engineering** (génie logiciel), qui vise à appliquer les principes de l’ingénierie à la création de logiciels.
:::
::::
:::::

<!-- ::::{grid-item}
:::{card}
:img-top: media/Dijkstra.jpg


Edsger Dijkstra 🇳🇱
^^^^^
***1930&#8209;2002***

[**Edsger Wybe Dijkstra**](https://fr.wikipedia.org/wiki/Edsger_Dijkstra) est un mathématicien et informaticien néerlandais du XX$^{e}$ siècle. Il reçoit en 1972 le prix Turing pour ses contributions sur la science et l’art des langages de programmation et au langage Algol. Il est le concepteur de l'algorithme éponyme de recherche du plus court chemin. 
:::
::::
::::: -->

`````

