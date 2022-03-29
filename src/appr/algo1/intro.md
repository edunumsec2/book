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
    <a href="http://files.edunumsec2.ch/algo.pdf" target="_blank" class="round-button">
         <font color=white id="demo">Voir <br>dossier</font>
    </a>
</div>

# Introduction

## Quoi ?

Il y a de fortes chances que vous ayez déjà entendu parler {glo}`algo|d'algorithmes` dans les médias. Il y a aussi de fortes chances que ce mot évoque pour vous des notions bien différentes de celles de votre voisin. L'objectif de ce chapitre est de vous éclairer sur la notion d'algorithme et la distinction avec la notion de programme informatique.

## Pourquoi ?

Les algorithmes existent depuis des millénaires. On doit le nom d'algorithme à Al-Khwârizmî, mathématicien perse né en l'an 780 dont les ouvrages ont contribué à la popularisation des chiffres arabes en Europe, ainsi que la classification de plusieurs algorithmes connus à ce moment. D'ailleurs l'algorithme le plus connu, l'algorithme d'Euclide, date environ de l'an 300 av J.-C. et permet de calculer le plus grand diviseur commun de deux nombres. Si Euclide a bien laissé des traces écrites de cet algorithme, il est vraisemblable qu'il ait puisé cette connaissance auprès de disciples de Pythagore lui-même. 

Les algorithmes sont devenus très populaires aujourd'hui grâce à la machine qui a permis de les automatiser. Que ce soit dans votre smartphone, sur un ordinateur ou dans un système embarqué, ils permettent de résoudre une quantité de problèmes, facilement et avec une rapidité impressionnante.

## Comment ?

Dans un premier temps nous allons nous intéresser à la notion même d'algorithme : qu'est-ce qui caractérise un algorithme et comment le faire exécuter par une machine ? Nous allons voir que pour un problème donné il existe de nombreuses solutions, mais que toutes ces solutions ne sont pas de *bonnes* solutions, selon le contexte dans lequel on tente de résoudre le problème. Dans un deuxième temps nous chercherons à départager ces différentes solutions.


<!-- 
L’algorithmique est une discipline s’intéressant à la construction de processus systématiques de résolution de problèmes, en décrivant précisément les étapes pour le résoudre.


Les premiers algorithmes dont on ait trace se trouvent chez les babyloniens, entre 2000 et 3000 ans av. JC : ils se présentent sous la forme de méthodes de calcul et de résolution d’équations. 
Par exemple une méthode permettant d'extraire la racine carrée d'un nombre : -->


<!-- ````{admonition} Exemple 0
:class: note


Soit N le nombre dont on cherche la racine carrée.
1. On choisit au hasard un nombre D inférieur à N.
2. On divise le nombre N par le nombre choisi, soit N/D.
3. On fait la moyenne de N/D et de N, soit (N/D + N)/2.
4. On fait successivement les mêmes opérations (2 et 3), le dernier résultat jouant le rôle du nombre choisi.
Soit à extraire la racine carrée de 663. On choisit 15. On convient de retenir seulement les deux premières décimales et d’arrondir au besoin. Le tableau suivant présente les calculs.

|  Quotient    |   Moyenne |
| :------------ | -------------: |
| 663/15 = 44,2 | (44,2 + 15)/2 = 29,6 |
| 663/29,6 = 22,39 | (29,6+22,39)/2 = 25,99 |
| (663/25,99 = 25,5 | (25,99 + 25,5)/2 = 25,74 |

````

</br>

Par cet algorithme, après avoir fait la moyenne trois fois, on obtient 25,74 qui 
est très proche du résultat donné par une calculatrice, soit 25,7487. 
</br>
</br>

Le plus célèbre algorithme est sans doute celui d’Euclide (*Livre 7 des Eléments*), 
permettant de déterminer le Plus Grand Commun Diviseur de deux nombres (PGCD).
</br>
</br>
Le mot algorithme vient d'Al-Khwârizmî (son nom a été latinisé au Moyen Âge en *Algoritmi*), mathématicien persan du IXe siècle qui a rédigé le premier véritable ouvrage décrivant des méthodes de résolution systématiques pour les équations linéaires et quadratiques. Il a repris la méthodologie des babyloniens, mais est allé au-delà du modèle des exemples en proposant justement une systématisation.

Cette notion de systématisation est illustrée par des fonctionnalités 
spécifiques communément retrouvées au sein des algorithmes : itérativité, 
récursivité, parallélisme.
</br>
</br>
L'algorithmique s'est considérablement développée au cours de la 
deuxième moitié du XXe siècle, suivant l’essort technique et technologique 
du début du siècle amené par l’électricité et le machinisme au XIXe siècle. 

La science algorithmique s’est ainsi affirmée comme le support conceptuel 
de la programmation des ordinateurs, dans le cadre du développement 
de l'informatique pendant cette période. Donald Knuth, auteur du 
traité *The Art of Computer Programming*, ouvrage de référence, a contribué, 
avec Edsger Dijkstra en particulier, à poser les fondements mathématiques 
de la discipline.

````{panels}

:img-top: media/knuth.jpg

Donald Knuth
^^^^^
* **Naissance** 10 janvier 1938

[Donald Knuth](https://fr.wikipedia.org/wiki/Donald_Knuth) est un 
informaticien et mathématicien américain de renom, professeur émérite 
en informatique à l'université Stanford, pionnier de l'algorithmique et de l'informatique 
théorique.
```` -->