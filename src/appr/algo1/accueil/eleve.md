
 <!DOCTYPE html>
<html>
<head>
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
</head>
</html>

<div align="right"> 
    <a href="http://files.edunumsec2.ch/algo.pdf" target="_blank" class="round-button">
         <font color=white id="demo">Voir <br>dossier</font>
    </a>
</div>


(algorithmique)=
Algorithmique I
==============================

Nous avons tous entendu parler des ALGORITHMES. Normal, c’est le mot à la mode et que tout le monde utilise sans vraiment le comprendre. Ils sont partout, ils font toutes sortes de choses, ils nous manipulent : pourquoi en parle-t-on de la même manière que des extraterrestres ? Dans ce cours, nous allons tenter de revenir sur terre, parce que les algorithmes ce n’est pas si compliqué que ça. On apprendra à les définir, à les faire fonctionner et surtout à reconnaître la différence entre un « bon » et un « mauvais » algorithme…



<!-- Le terme d'algorithme s'est progressivement diffusé dans toutes les facettes de la société actuelle, pour dépasser le cadre de l'utilisation par les seuls experts en informatique. Ils sont partout, de la plus petite application pour smartphone au système d'intelligence artificielle le plus complexe et ont largement investi la sphère médiatique et nos espaces de communication. Ils font toutes sortes de choses... Mais, qu'est ce qu'un algorithme réellement ? Comment ça marche ? Comment faire la différence entre un bon et un mauvais algorithme ? Quelles sont ses spécificités, ses caractéristiques ? Tant de questions qui tenteront de s'éclaircir au cours des chapitres qui suivent.

Bienvenue dans le monde fascinant des algorithmes... -->

<!-- 
## Contenu de la thématique

```{tableofcontents}
``` 
-->

## Objectifs de la thématique

A la fin de ce chapitre, vous saurez ce qu'est un algorithme et vous serez capable de transcrire des algorithmes en programmes. Vous saurez résoudre des problèmes, en décomposant leur solution en étapes à suivre. Vous verrez également que pour un même problème, on peut avoir plusieurs solutions avec des propriétés, avantages et désavantages différents. 

{fa}`check, text-success mr-1`Se familiariser avec la notion d’algorithme.

{fa}`check, text-success mr-1`Savoir résoudre des problèmes, en décomposant leur solution en étapes à suivre.

{fa}`check, text-success mr-1`Savoir que pour un même problème, on peut avoir plusieurs solutions avec différents propriétés, avantages et désavantages.

{fa}`check, text-success mr-1`Être capable de transcrire un algorithme dans un programme.

Bienvenue dans le monde fascinant des algorithmes...


## Personnages-clés


````{panels}

:img-top: media/Al-Khwarizmi.png

Al-Khwarizmi 🇺🇿
^^^^^
***780-850***

Considéré comme le père de l’algèbre [**Al-Khwarizmi**](https://fr.wikipedia.org/wiki/Al-Khw%C3%A2rizm%C3%AE) a vécu au VIII<sup>e</sup> siècle dans le Moyen-Orient. Il est l'auteur de plusieurs ouvrages de mathématiques, d’astronomie et de géographie. Son nom est à l’origine du mot **algorithme**.

----
:img-top: media/Dijkstra.jpg

Edsger Dijkstra 🇳🇱
^^^^^
***1930-2002***

[Edsger Wybe Dijkstra](https://fr.wikipedia.org/wiki/Edsger_Dijkstra) est un mathématicien et informaticien néerlandais du XX<sup>e</sup> siècle. Il reçoit en 1972 le prix Turing pour ses contributions sur la science et l’art des langages de programmation et au langage Algol. Il est le concepteur de l'algorithme éponyme de recherche du plus court chemin. 
````






