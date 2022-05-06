# Conclusion


```{admonition} Ai-je compris ?
:class: hint

<ol>
<li>Je sais appliquer un algorithme de recherche et un algorithme de tri rapide.</li>

<li>Je sais calculer la complexité temporelle des algorithmes.</li>

<li>Je sais pourquoi un algorithme d’ordre de complexité exponentielle est lent.</li>

<li>Je comprends la différence entre une solution exacte et une solution heuristique.</li>

<li>[Pour aller plus loin] Je comprends comment fonctionne la récursivité.</li>

```




````{admonition} Pourquoi est-ce important ?
:class: warning

L’analyse de complexité des algorithmes nous permet de sélectionner les meilleurs algorithmes pour un problème donné et nous permet de comprendre pourquoi certains problèmes ne peuvent être résolus dans un temps raisonnable (à ce stade).

L’algorithmique a permis de mettre en place des stratégies intelligentes de résolution de problèmes comme les principes de « diviser pour régner » ou encore la récursivité. Ces stratégies ont rendu possibles les avancées technologiques fulgurantes du dernier demi-siècle. 

Pour des problèmes difficiles, s’il est impossible de trouver la solution exacte, on peut toujours trouver une solution approchée. L’étude formelle de l’algorithmique nous permet d’estimer la qualité de notre solution approchée.

````

```{admonition} À retenir
:class: danger

Il est important de garantir qu’un algorithme va se **<span style="color:rgb(89, 51, 209)">terminer</span>** pour être utile en pratique.

Les algorithmes de tri rapide et de tri par fusion sont plus efficaces que les algorithmes de tri vus précédemment. Ceci est possible grâce à la stratégie algorithmique **<span style="color:rgb(89, 51, 209)">« diviser pour régner »</span>**, qui divise un grand problème difficile à résoudre en plein de petits sous-problèmes plus faciles à résoudre. La solution au grand problème s’obtient en combinant les solutions des petits problèmes. 

L’**<span style="color:rgb(89, 51, 209)">ordre de complexité des algorithmes</span>** nous dit si un algorithme est lent ou rapide. Un algorithme  avec un ordre de complexité logarithmique est plus rapide qu’un algorithme avec complexité linéaire, qui en retour est plus rapide qu’un algorithme de complexité quadratique, ou pire exponentielle.

Une **<span style="color:rgb(89, 51, 209)">fonction récursive</span>** est une fonction qui fait appel à elle-même. Une condition d’arrêt est nécessaire pour que l’algorithme se termine.

Un algorithme avec un ordre de **<span style="color:rgb(89, 51, 209)">complexité exponentiel</span>** implique que le temps nécessaire pour résoudre un problème est trop long en pratique. Dans ce cas, on ne va pas pouvoir trouver une solution exacte, mais seulement une solution approchée en utilisant des méthodes heuristiques.

```

```{admonition} Je veux en savoir plus
:class: hint

<br>

**<span style="color:rgb(13, 204, 166)">Visualisation de problèmes</span>** 

https://visualgo.net/en

https://interstices.info/le-probleme-du-sac-a-dos/

https://clementmihailescu.github.io/Pathfinding-Visualizer/

**<span style="color:rgb(13, 204, 166)">Problèmes difficiles</span>**

https://www.franceculture.fr/emissions/le-journal-des-sciences/le-journal-des-sciences-du-mardi-01-decembre-2020

https://www.bfmtv.com/sciences/ou-est-charlie-l-algorithme-pour-le-detecter-du-premier-coup_AN-201502100004.html

https://www.lebigdata.fr/algorithme-definition-tout-savoir

**<span style="color:rgb(13, 204, 166)">P = NP ?</span>**

https://www.youtube.com/watch?v=AgtOCNCejQ

```
