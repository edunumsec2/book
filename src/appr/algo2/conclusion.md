# Conclusion



````{admonition} Pourquoi est-ce important ?
:class: warning

L’analyse de complexité des algorithmes nous permet de sélectionner les meilleurs algorithmes pour un problème donné et nous permet de comprendre pourquoi certains problèmes ne peuvent pas être (à ce stade) résolus dans un temps raisonnable.

L’algorithmique a permis de mettre en place des stratégies intelligentes de résolution de problèmes comme les principes de « diviser pour régner » ou encore la récursivité. Ces stratégies ont rendu possibles les avancées technologiques fulgurantes du dernier demi-siècle. 

Pour des problèmes difficiles, s’il est impossible de trouver la solution exacte, on peut souvent trouver une solution approchée. L’étude formelle de l’algorithmique nous permet d’estimer la qualité de notre solution approchée.

````

```{admonition} À retenir
:class: danger

Dans la pratique, il est important de garantir qu’un algorithme va se **<span style="color:rgb(89, 51, 209)">terminer</span>**.

L'algorithme de tri rapide (et du tri par fusion) est plus efficace que les algorithmes de tri vus dans les chapitres précédents. Ceci est possible grâce à la stratégie algorithmique **<span style="color:rgb(89, 51, 209)">« diviser pour régner »</span>**, qui divise un grand problème difficile à résoudre en plein de petits sous-problèmes plus faciles à résoudre. La solution au grand problème s’obtient en combinant les solutions des petits problèmes. 

L’**<span style="color:rgb(89, 51, 209)">ordre de complexité</span>** d'un algorithme nous dit si l'algorithme est lent ou rapide. Un algorithme avec un ordre de complexité logarithmique est plus rapide qu’un algorithme avec complexité linéaire, qui à son tour est plus rapide qu’un algorithme de complexité quadratique, ou pire, exponentielle.

Un algorithme **<span style="color:rgb(89, 51, 209)">récursif</span>** est un algorithme qui fait appel à lui-même. Une condition d’arrêt est nécessaire pour que l’algorithme se termine.

Un algorithme avec une **<span style="color:rgb(89, 51, 209)">complexité exponentielle</span>** implique que le temps nécessaire pour résoudre problème est trop long en pratique. Dans ce cas, on ne va pas pouvoir trouver une solution exacte, mais seulement une solution approchée en utilisant des méthodes heuristiques.

```

```{admonition} Ai-je compris ?
:class: hint

<ol>
<li>Je sais appliquer l'algorithme de recherche binaire.</li>

<li>Je comprends comment fonctionne la stratégie algorithmique « diviser pour régner ».</li>

<li>Je sais appliquer l'algorithme de tri rapide.</li>

<li>Je sais calculer la complexité temporelle d'un algorithme.</li>

<li>[En option] Je comprends comment fonctionne la récursivité.</li>

<li>Je sais pourquoi un algorithme de complexité exponentielle est lent.</li>

<li>Je comprends ce qu'est une solution heuristique.</li>



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
