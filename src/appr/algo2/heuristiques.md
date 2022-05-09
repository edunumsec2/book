# 5. Algorithmes heuristiques


````{admonition} Matière à réfléchir. Tour du monde
:class: attention

Vous avez décidé de faire le tour du monde. Choisissez cinq pays que vous souhaitez visiter et placez-les sur une carte. Essayez de trouver le meilleur itinéraire pour visiter ces cinq pays. 

Quels critères avez-vous pris en compte pour décider du meilleur itinéraire ? Avez-vous essayé de trouver la plus petite distance à parcourir ?

Vous avez décidé de visiter dix pays. Est-ce qu’il est aussi facile de trouver un itinéraire optimal ?

Imaginez que vous souhaitez visiter tous les pays du monde (un peu moins de 200). Combien y a-t‑il d’itinéraires possibles ?  Comment s’appelle ce nombre ?

Si le calcul d’un itinéraire prenait 1 milliseconde, combien de temps faudrait-il pour trouver la meilleure solution en énumérant toutes les solutions possibles ? Pour comparaison, le nombre d’atomes dans l’univers est d’ordre 10<sup>80</sup>.

````

## 5.0. Complexité exponentielle

Il existe des problèmes difficiles à résoudre. Nous allons nous pencher sur un problème qui s’appelle le **<span style="color:rgb(89, 51, 209)">problème du sac à dos</span>**. Prenons un sac à dos et une multitude d’objets qui ont chacun un poids. Notre objectif est de choisir les objets à mettre dans le sac à dos pour le remplir au maximum, mais sans dépasser sa capacité. Donc la question que l'on se pose est la suivante : quels objets devrions-nous emporter, sans dépasser le poids maximal que le sac à dos peut contenir ?


```{admonition} Exercice 5.0. Le problème du sac à dos
:class: note

Comment procéderiez-vous pour résoudre ce problème du sac à dos ? Prenez le temps d’imaginer un {glo}`algo|algorithme` qui puisse résoudre ce problème ? 

Appliquer cet algorithme pour 5 objets de poids 1, 3, 5 et 7 kg et un sac de capacité de 10 kg.

Est-ce que votre algorithme donne toujours la meilleure solution ? 
```

````{admonition} Solution 5.0. Le problème du sac à dos
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

La solution est donnée dans le texte qui suit.

```
````



L'algorithme le plus simple pour résoudre ce problème est un **<span style="color:rgb(89, 51, 209)">algorithme de force brute</span>** (ou un algorithme exhaustif), qui consiste à énumérer toutes les combinaisons d'objets que pourrait contenir le sac à dos, l’une après l’autre, et de calculer le poids total pour chaque combinaison. Après avoir calculé toutes les combinaisons, il suffit de sélectionner la combinaison dont le poids se rapproche le plus de la capacité du sac à dos, sans la dépasser. Vous trouverez ci-dessous la solution pour l’exemple de l’exercice 5.0 (« oui » signifie que l’on met l’objet dans le sac à dos et « non » signifie que l’on ne met pas l’objet dans le sac à dos). 


<table style="border: 1px solid; border-collapse: collapse;">
    <thead>
        <tr>
            <th style="border: 1px solid; padding:10px; text-align:center">Combinaison</th><th style="border: 1px solid; padding:10px; text-align:center">1 kg</th><th style="border: 1px solid; padding:10px; text-align:center">3 kg</th><th style="border: 1px solid; padding:10px; text-align:center">5 kg</th><th style="border: 1px solid; padding:10px; text-align:center">7 kg</th><th style="border: 1px solid; padding:10px">Poids total</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid; padding:10px">1</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px; text-align:center">0</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">2</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px; text-align:center"">1</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">3</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px; text-align:center"">3</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">4</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px; text-align:center"">4</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">5</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px; text-align:center"">5</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">6</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px; text-align:center"">6</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">7</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px; text-align:center"">8</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">8</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px; text-align:center"">9</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">9</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px; text-align:center"">7</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">10</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px; text-align:center"">8</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">11</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px; text-align:center"">10</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">12</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px; text-align:center"">11</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">13</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px; text-align:center"">12</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">14</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px; text-align:center"">13</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">15</td><td style="border: 1px solid; padding:10px">non</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px; text-align:center"">15</td>
        </tr><tr>
            <td style="border: 1px solid; padding:10px">16</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px">oui</td><td style="border: 1px solid; padding:10px; text-align:center"">16</td>
        </tr>
    </tbody>
</table>

<br>

La meilleure solution se trouve à la 11ème ligne, la capacité du sac à dos (10 kg) est atteinte lorsqu'on y met le deuxième et le quatrième objet.


```{admonition} Exercice 5.1. Le problème du sac à dos avec 10 objets
:class: note

Combien de combinaisons possibles existent pour le problème du sac à dos avec 10 objets ? 
```

````{admonition} Solution 5.1. Le problème du sac à dos avec 10 objets
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

La solution est donnée dans le texte qui suit.

```
````

Mais, combien y a-t-il de combinaisons possibles si on a 10 objets ? Pour chaque objet, on a deux choix possibles : le mettre dans le sac à dos ou ne pas le mettre dans le sac à dos ***<span style="color:rgb(13, 204, 166)">(to take or not to take, that is the question)</span>***. Comme ces deux possibilités existent pour chacun des 10 objets, le nombre de combinaisons possibles vaut :

&nbsp;&nbsp;&nbsp;&nbsp; 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 = 2<sup>10</sup>

Pour `n` objets, le nombre de solutions possibles est 2<sup>n</sup>. Si on a 2 objets, il y a donc 4 combinaisons différentes d’objets dans le sac à dos (aucun objet, le premier objet, le deuxième objet et les deux objets ensemble). Pour 3 objets, le nombre de combinaisons est 8. Pour 5 objets, nous avons 32 possibilités à explorer. Mais déjà pour 10 objets, ce nombre dépasse les 1000 combinaisons possibles. Pour 100 objets, ce nombre devient prohibitif et vaut 10<sup>30</sup>. Si on doit résoudre ce problème avec 270 objets sous la main, le nombre de combinaisons possibles dépasse le nombre d’atomes dans l’univers, c'est-à-dire 10<sup>80</sup>. Si le calcul du poids d’une combinaison prenait une microseconde, il nous faudrait pour résoudre ce problème bien plus que le temps de l'existence de l’univers, plus de 14 milliards d'années. Ces nombres sont réellement vertigineux. Cela va de soi, nous n’avons pas tout ce temps à disposition... 

L’ordre de complexité de type 2<sup>n</sup> est un ordre de **<span style="color:rgb(89, 51, 209)">complexité exponentielle</span>**. Cela vaut aussi pour d’autres constantes que 2, par exemple 10<sup>n</sup> ou 1.1<sup>n</sup>. Lorsqu’un algorithme est d’ordre de complexité exponentielle, cela veut dire que le temps nécessaire pour résoudre le problème croît exponentiellement en fonction de la taille des données `n` (voir figure ci-dessous). Les problèmes de complexité exponentielle ne peuvent être résolus dans un temps raisonnable, pour des données à partir d’une certaine taille.


```{figure} media/Complexite_exponentielle.png
---
alt: complexité exponentielle
width: 420px
name : fig-comp-exp
---
**Complexité exponentielle.** Comparaison de l’ordre de complexité exponentielle avec les ordres de complexité vus jusqu’ici. Dans un ordre de complexité exponentielle, le nombre d’instructions élémentaires grandit très rapidement avec la taille des données, et l’algorithme est très lent. 
```

Lorsqu’il est trop difficile de trouver une solution exacte à un problème, nous ne devons pas nous avouer vaincus. Dans ce cas, nous pouvons tout de même rechercher une solution inexacte, mais qui se rapproche autant que possible de la solution optimale. Les algorithmes qui aboutissent à des solutions non optimales ou inexactes, sont appelés des **<span style="color:rgb(89, 51, 209)">heuristiques</span>**.

Un algorithme heuristique pour le problème du sac à dos pourrait être l'algorithme suivant : prendre les objets du plus petit au plus grand poids jusqu’à remplir le sac à dos, ce qui nous permettrait de mettre le plus d'objets possible. En suivant cet algorithme heuristique, dans l'exemple de l'exercice 5.0, on prendrait les trois premiers objets et on aurait un sac à dos rempli à 9 kgs au lieu des 10 kg de capacité maximale du sac à dos. Cette solution est suffisamment proche de la meilleure solution, mais elle n'est pas la meilleure solution.



Une solution heuristique est donc une solution intuitive, qui se base sur une ***<span style="color:rgb(13, 204, 166)">stratégie d'essais et d'erreurs</span>***, qui en quelque sorte repose sur la chance. Un algorithme heuristique est plus rapide que l'algorithme de force brute qui énumérerait toutes les solutions possibles afin de trouver la meilleure solution, mais on paie le prix de cette efficacité par de la précision. Un algorithme heuristique aboutit à une solution moins précise et moins complète, à une solution sans garantie. Quand un problème est trop complexe, il ne peut être résolu que par des algorithmes heuristiques, aboutissant dans certains cas à des mauvaises solutions. 


```{admonition} Le saviez-vous ? Que veut dire heuristique ?
:class: hint

Le mot **heuristique** nous vient du grec ancien, plus précisément du terme *heuriskêin*, qui veut dire trouver, inventer, découvrir. 

Ce même terme a donné un autre mot bien connu *eurêka*.

```


L'algorithme heuristique qu'on vient de voir est en fait un **<span style="color:rgb(89, 51, 209)">algorithme glouton</span>**, un algorithme qui choisit une solution *localement optimale* (qui choisit la meilleure solution en apparence à un moment donné) sans se préoccuper de toutes les solutions possibles. On espère ainsi que toutes ces décisions localement optimales mènent vers une très bonne solution. C'est un peu comme si on cherchait à atteindre le plus haut sommet d'une montagne, entourés de brouillard, et qu'on prenait une décision sur le chemin à emprunter uniquement en fonction de ce que l’on peut voir juste autour de nous. On pourrait prendre le chemin le plus pentu en espérant qu’il nous mène à un sommet très haut, mais une fois arrivés en haut d'un sommet, on ne peut savoir si notre sommet est bien le plus haut. On l’espère…




Il n’y a pas que des {glo}`heuristique|heuristiques` gloutonnes. Un autre exemple de solution heuristique, très utilisée dans les jeux vidéos, est le calcul de distance entre deux objets. Ce calcul est très important par exemple lorsque l'on souhaite détecter si deux objets sont en collision. Pythagore nous dit que cette distance vaut la racine carrée de la somme de `a` et `b` au carré. Mais ce calcul est difficile, et même si on peut le calculer de manière exacte, il prend beaucoup de temps à calculer s’il y a beaucoup d’objets affichés à l’écran. On préfère ainsi estimer cette distance par un calcul bien plus simple `a+b`, que l'on sait faux, mais qui est suffisamment proche lorsque les objets sont alignés (voir la figure ci-dessous).

```{figure} media/Distance.png
---
alt: exemple d'heuristique
width: 420px
name : heuristique
---
**Exemple d'heuristique.** Dans les jeux vidéos, on préfère estimer la distance `d` entre deux objets `A` et `B` par la somme des longueurs des côtés de l'angle droit `a+b`, plutôt que de calculer la racine carrée de la somme des carrés des longueurs des côtés de l'angle droit `d`<sup>`2`</sup> `=` `a`<sup>`2`</sup> `+` `b`<sup>`2`</sup> (théorème de Pythagore). Même si ce calcul est inexact, il est beaucoup plus rapide à calculer quand il y a beaucoup d’objets à afficher à l’écran, et il est suffisemment précis lorsque les deux objets sont alignés.
```


Il existe encore d’autres types d’algorithmes {glo}`heuristique|heuristiques`, plus lents, mais qui permettent de s’approcher davantage de la solution optimale. Ils utilisent par exemple des stratégies de résolution statistiques, génétiques ou neuronales. L'apprentissage automatique à qui l'on doit les succès récents de l'intelligence artificielle repose sur des algorithmes heuristiques. La majorité des problèmes que l’on tente de résoudre aujourd’hui sont difficiles et leurs algorithmes de résolution ne trouvent pas la meilleure solution.


```{admonition} Exercice 5.2. L'univers dans un sac à dos 
:class: note

L’âge estimé de l’univers est de 14 milliards d’années. Si le calcul d’une combinaison d’objets dans le problème du sac à dos prenait une microseconde, pour quel nombre d’objets serait-il possible de trouver une solution exacte sans dépasser l’âge de l’univers ?

```

````{admonition} Solution 5.2. L'univers dans un sac à dos 
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Une microseconde vaut 10<sup>-6</sup> s. La complexité du problème du sac à dos est de 2<sup>n</sup>.

On recherche un `n` pour lequel 2<sup>n</sup>*10<sup>-6</sup> = 14 000 000 000 * 3,154*10<sup>7</sup> (l'âge de l'univers en secondes) 

n = log<sub>2</sub>(1.4 * 10<sup>10</sup> / 10<sup>-6</sup>) = log<sub>2</sub>(1.4 * 10<sup>16</sup>) = 88 objets seulement.

```
````


```{admonition} Exercice 5.3. Parcours du parcours du parcours d'un tableau
:class: note

Quelle est la complexité d’un algorithme qui pour chacun de ses éléments doit parcourir le tableau, puis pour chaque combinaison de deux de ses élements doit encore parcourir le tableau ?

```


````{admonition} Solution 5.3. Parcours du parcours du parcours d'un tableau
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

<!-- TODO #21 @edunum-sec2 : Clarification de la consigne car telle que je la comprend, 2 fois un parcours pour chaque élément fais 2 * n * n = O(n^2) -->

Pour chaque élément (premier parcours) on doit parcourir le tableau une fois, et pour chacune des combinaisons de deux éléments du tableau, il nous faut parcourir le tableau une troisième fois : on a donc une complexité de n * n * n = n<sup>3</sup>, ou une complexité cubique.

```
````

````{admonition} Pour aller plus loin
:class: attention

Voici un problème à un million de dollars, un parmi les sept problèmes mathématiques du prix du millénaire qui rapporteront de l’argent à la personne qui les résoudra.

On appelle la classe des problèmes qui sont faciles à résoudre la classe des problèmes P. Ces algorithmes peuvent être résolus en un temps polynomial en fonction de la taille des données n, ou O(n<sup>a</sup>). 

Une autre classe de problèmes sont les problèmes difficiles à résoudre qui sont d’ordre de complexité exponentielle. Lorsqu'on arrive à vérifier rapidement (en temps polynomial) si une solution proposée permet de résoudre le problème, il s'agit d'une classe de problèmes appellée NP ou « non déterministe polynomial ».

On souhaite savoir si les problèmes NP peuvent être résolus en un temps P ou non, ou en d’autres termes : est-ce que **P = NP** ? 

S’il s’avérait que c’est bien le cas (ce qui est tout de même peu probable), beaucoup de problèmes difficiles à résoudre deviendraient d’un seul coup plus faciles à résoudre. Un des ces problèmes est le **problème de repliement des protéines** en biologie qui cherche de nouveaux médicaments. Cela pourrait également signifier la fin de la cryptographie telle qu’elle existe actuellement.

````

````{admonition} Ai-je compris ?
:class: attention

1. Je sais reconnaître un algorithme de force brute.

2. Je sais reconnaître un algorithme heuristique.

3. Je sais reconnaître un algorithme glouton.

4. Je comprends pourquoi un algorithme de complexité exponentielle est lent.

````
