
# *Introduction*

L’algorithmique est une discipline s’intéressant à la construction de processus systématiques de résolution de problèmes, en décrivant précisément les étapes pour le résoudre.


Les premiers algorithmes dont on ait trace se trouvent chez les babyloniens, entre 2000 et 3000 ans av. JC : ils se présentent sous la forme de méthodes de calcul et de résolution d’équations. 
Par exemple une méthode permettant d'extraire la racine carrée d'un nombre :


````{admonition} Exemple 0
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
````