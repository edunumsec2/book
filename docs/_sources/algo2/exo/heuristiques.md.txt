# Algorithmique II

## 4. Algorithmes heuristiques

### Solutions des exercices

````{exercise} 
Voir partie Apprendre.
````
````{exercise} 
Voir partie Apprendre.
````


```{exercise} L'univers dans un sac à dos 

L’âge estimé de l’univers est de 14 milliards d’années. Si le calcul d’une combinaison d’objets dans le problème du sac&nbsp;à&nbsp;dos prenait une microseconde, pour quel nombre d’objets serait-il possible de trouver une solution exacte sans dépasser l’âge de l’univers ?

```

````{solution} 

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Une microseconde vaut 10<sup>-6</sup> s. La complexité du problème du sac&nbsp;à&nbsp;dos est de 2<sup>n</sup>.

On recherche un `n` pour lequel 2<sup>n</sup>*10<sup>-6</sup> = 14 000 000 000 * 3,154*10<sup>7</sup> (l'âge de l'univers en secondes) 

n = log<sub>2</sub>(1.4 * 3,154*10<sup>17</sup> / 10<sup>-6</sup>) = log<sub>2</sub>(4.42 * 10<sup>23</sup>) = 78 objets seulement.

```
````


```{exercise} Parcours du parcours du parcours de listes

Quelle est la complexité d’un algorithme qui pour chacun des éléments d'une liste de $n$ éléments, doit parcourir tous les éléments d'une autre liste de $n$ éléments, puis pour chacune des combinaisons de deux éléments doit encore parcourir une troisième liste de $n$ éléments ?

Si vous avez besoin de travailler sur un exemple plus concret, quelle est complexité de l'algorithme qui calcule tous les menus possibles à partir d'une liste de $n$ entrées, une liste de $n$ plats et une liste de $n$ desserts ?

```


````{solution} 

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Pour chaque élément de la première liste (premier parcours) on doit parcourir la deuxième liste une fois, ce qui fait une complexité de n * n = n<sup>2</sup>. Pour chacune des combinaisons de deux éléments des deux premières listes, il nous faut parcourir la troisième liste : on a donc une complexité de n * n * n = n<sup>3</sup>, ou une complexité cubique.

```
````
