# 3. Algorithmes de tri

Nous venons de voir que pour rechercher de manière efficace, les données doivent être triées. Mais quelle est la complexité de l'algorithme du Tri par sélection vu dans le chapitre <a href="../algo1/cours/2_trie_cherche_trouve/eleve.html#tri-selection">Trie, cherche et trouve</a> ? C'est sa complexité qui nous donnera une indication sur sa rapidité.

## 3.0. Tri par sélection

Pour rappel, l'{glo}`algo|algorithme` du <a href="../algo1/cours/2_trie_cherche_trouve/eleve.html#tri-selection">**<span style="color:rgb(89, 51, 209)">Tri par sélection</span>**</a> parcourt le tableau à la recherche des plus petits éléments. Afin de trouver le plus petit élément du tableau, il faut commencer par parcourir tous les éléments du tableau. Cette opération prend `cn` {glo}`instruction|instructions` : `c` instructions pour l’accès et la comparaison des éléments du tableau, multiplié par le nombre d’éléments `n`. Il faut ensuite trouver le plus petit élément des éléments restants `n-1`, et ainsi de suite. Concrètement, on va parcourir jusqu'à `n` éléments, `n` fois (pour chacun des éléments). La complexité du Tri par sélection est donc proportionnelle à `n * n` (`n`<sup>`2`</sup>), on parle de complexité **<span style="color:rgb(89, 51, 209)">quadratique</span>**. 

`````{admonition} Pour aller plus loin
:class: note


````{dropdown} <span style="color:grey">Si vous souhaitez connaître les détails du calcul de complexité, cliquez pour lire ce qui suit.</span>
:animate: fade-in-slide-down

Pour calculer la somme totale d'instructions nécessaires, il faut additionner les termes qui permettent de retrouver le plus petit élément. La première fois que l'on recherche le plus petit élément il faut parcourir `n` éléments. La deuxième fois, il reste à parcourir  `n-1` éléments. La troisième fois, il faut parcourir les `n-2` éléments restants. Et ainsi de suite, jusqu'à ce qu'il ne reste plus qu'un élément. 

Par exemple, si le tableau contient les éléments [5, 2, 3, 6, 1, 4], pour trouver le plus petit élément 1 à la première itération on doit parcourir tout le tableau, ou 6 éléments. A la deuxième itération, on met l'élément 1 de côté et on parcourt le tableau [5, 2, 3, 6, 4], ce qui fait 5 éléments. On met le plus petit élément 2 de côté et dans la troisième itération on parcourt le tableau [5, 3, 4, 6], ce qui fait 4 éléments. On met 3 de côté et on parcourt encore le tableau [5, 4, 6], ce qui fait 3 éléments. Finalement on se retrouve avec les tableaux [5, 6] à 2 éléments et [5] à 1 élément. La somme totale d'éléments parcourus est 6 + 5 + 4 + 3 + 2 + 1 = 21. 

Si on généralise on obtient :

&nbsp;&nbsp;&nbsp;&nbsp; n + (n-1) + (n-2) + ... + (n/2 + 1) + n/2 + ... + 3 + 2 + 1

En réarrangeant les termes deux par deux de l'extérieur vers l'intérieur on obtient plusieurs fois le même terme :

&nbsp;&nbsp;&nbsp;&nbsp; (n + 1) + ((n-1) + 2) + ((n-2) + 3) + .... + ((n/2 + 1) + n/2) 

&nbsp;&nbsp;&nbsp;&nbsp; (n + 1) + (n + 1) + (n + 1) + .... + (n + 1) =

&nbsp;&nbsp;&nbsp;&nbsp; (n + 1) * n/2 =

&nbsp;&nbsp;&nbsp;&nbsp; n * n/2 + n/2 =

&nbsp;&nbsp;&nbsp;&nbsp; n<sup>2</sup>/2 + n/2

Si on reprend l'exemple ci-dessus, on aurait :

&nbsp;&nbsp;&nbsp;&nbsp; 6 + 5 + 4 + 3 + 2 + 1 =

&nbsp;&nbsp;&nbsp;&nbsp; (6 + 1) + (5 + 2) (4 + 3) = 

&nbsp;&nbsp;&nbsp;&nbsp; 7 *(6/2) = 7 * 3 = 21 &nbsp;&nbsp;&nbsp;&nbsp; ou

&nbsp;&nbsp;&nbsp;&nbsp; 6<sup>2</sup>/2 + 6/2 = 36/2 + 3 = 18 + 3 = 21

Le terme dominant dans la somme n<sup>2</sup>/2 + n/2 est n<sup>2</sup>/2, plus n grandit plus n/2 est insignifiant par rapport à n<sup>2</sup>/2. Par exemple, pour n = 1000, n<sup>2</sup>/2 vaut 500000, alors que n/2 vaut seulement 500. 

Cette somme nous donne le nombre d'éléments parcourus. Mais pour chacun de ces éléments, plusieurs instructions sont exécutées, comme l'accès aux éléments et leur comparaison. Ces instructions et le terme qui divise par 2 peuvent être absorbés dans une {glo}`constante|constante` c qui multuplie le terme quadratique `n`<sup>`2`</sup>. En ajoutant une constante a pour prendre en compte le nombre d'instructions qui ne dépendent pas de la taille des données (comme les initialisations au début de l’algorithme), on obtient l'ordre de grandeur `cn`<sup>`2`</sup>` + a`. L'ordre de grandeur est donc **<span style="color:rgb(89, 51, 209)">quadratique</span>**.

````

`````

Si on compare les complexités vues jusqu'ici pour un tableau de 1000 éléments on obtient :

<table style="margin-left: auto; margin-right: auto;">
    <thead>
        <tr>
            <th style="border: 1px solid black; border-collapse: collapse; padding: 15px">Complexité</th>
            <th style="border: 1px solid black; border-collapse: collapse; padding: 15px">Instructions élémentaires pour 1000 éléments</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid black; border-collapse: collapse; padding: 15px">Linéaire</td>
            <td style="border: 1px solid black; border-collapse: collapse; padding: 15px; text-align: center">1000</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; border-collapse: collapse; padding: 15px">Logarithmique</td>
            <td style="border: 1px solid black; border-collapse: collapse; padding: 15px; text-align: center">10</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; border-collapse: collapse; padding: 15px">Quadratique</td>
            <td style="border: 1px solid black; border-collapse: collapse; padding: 15px; text-align: center">1000000</td>
        </tr>
    </tbody>
</table>
<br>

Avec une complexité quadratique, le Tri par sélection est un algorithme relativement lent.



```{admonition} Exercice 3.0. Complexité du Tri par insertion
:class: note

Quelle est la complexité de l’algorithme de <a href="../algo1/cours/2_trie_cherche_trouve/eleve.html#tri-insertion">**<span style="color:rgb(89, 51, 209)">Tri par insertion</span>**</a> ? En d’autres termes, si le tableau contient n éléments, combien faut-il d’instructions pour trier ce tableau ? Pour rappel, le Tri par insertion parcourt le tableau dans l'ordre et pour chaque nouvel élément, l'insère à l'emplacement correct des éléments déjà parcourus.

<!--
Est-ce que la complexité du Tri par insertion est la même si les éléments du tableau sont déjà triés ?
-->

```

````{admonition} Solution 3.0. Complexité du Tri par insertion
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Dans le pire cas, lorsque les éléments sont dans l'ordre inverse, on doit comparer chacun des `n` éléments avec `1` à `n` éléments. La complexité de l'algorithme du Tri par insertion est donc `n * n = n`<sup>`2`</sup> ou **quadratique**. 

<!--
Dans le meilleur cas, lorsque les éléments sont déjà dans le bon ordre, on doit comparer chacun des n éléments avec 1 élément, l'élément précédent. La complexité du Tri par insertion est donc `n * 1 = n` ou **linéaire**. 
-->

```
````

```{admonition} Exercice 3.1. Complexité du Tri à bulles
:class: note

Quelle est la complexité de l’algorithme de <a href="../algo1/cours/2_trie_cherche_trouve/eleve.html#tri-bulles">**<span style="color:rgb(89, 51, 209)">Tri à bulles</span>**</a> ? En d’autres termes, si le tableau contient n éléments, combien faut-il d’instructions pour trier ce tableau ? Pour rappel, le Tri à bulles compare les éléments deux par deux en les réarrangeant dans le bon ordre, afin que l'élément le plus grand remonte vers la fin du tableau tel une bulle d'air dans de l'eau. Cette opération est répétée n fois, pour chaque élément du tableau.

```

````{admonition} Solution 3.1. Complexité du Tri à bulles
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Dans le cas du Tri à bulles, pour chacun des n éléments on parcourt jusqu'à n éléments de la liste, ce qui nous donne une complexité `n * n = n`<sup>`2`</sup> ou une complexité quadratique.

```
````

## Tri rapide

Les trois {glo}`algo|algorithmes` de tri vus dans le chapitre précédent – le Tri par sélection, le Tri par insertion et le Tri à bulles – sont des algorithmes de complexité quadratique. Si on devait utiliser ces tris dans les systèmes numériques en place, on passerait beaucoup de notre temps à attendre. Il existe d’autres algorithmes de tri qui sont bien plus rapides. Nous allons voir un {glo}`algo|algorithme` de tri tellement rapide, qu’on lui a donné le nom **<span style="color:rgb(89, 51, 209)">Tri rapide</span>**.

On commence par prendre un élément du tableau que l'on définit comme ***<span style="color:rgb(13, 204, 166)">élément pivot</span>***. Cet élément pivot est en général soit le premier ou le dernier élément du tableau, soit l’élément du milieu du tableau ou encore un élément pris au hasard. On compare ensuite tous les autres éléments du tableau à cet élément pivot. Tous les éléments qui sont plus petits que le pivot seront mis à sa gauche et tous les éléments qui sont plus grands que le pivot seront mis à sa droite, tout en conservant leur ordre (voir la deuxième ligne de la figure ci-dessous). 


<span id="tri-rapide"></span>
```{figure} media/Tri_rapide.png
---
alt: tri rapide
width: 420px
name : fig-tri-rapide
---
**Tri rapide**. Illustration du tri rapide sur les mêmes données que celles utilisées pour illustrer les algorithmes de tri du chapitre précédent. On choisit comme élément pivot le dernier élément des tableaux à trier. Tous les éléments qui sont plus petits que le pivot se retrouvent à sa gauche, tous les éléments plus grands que le pivot se retrouvent à sa droite. L'ordre est conservé.
```


<!--
```{image} media/Tri_rapide.png
:width: 400px
:height: 300px
```
**Tri rapide**. Illustration du tri rapide sur le même set de données que celui utilisé pour illustrer les algorithmes de tri vus au chapitre précédent. L’élément pivot est le dernier élément des tableaux à trier
<br>
-->

Après la répartition des éléments autour de l’élément pivot en fonction de leur taille, on se retrouve avec deux tableaux non triés, un sous-tableau à chaque côté de l’élément pivot. On répète les mêmes opérations que pour le tableau initial. Pour chaque sous-tableau, celui de gauche et celui de droite du pivot, on détermine un nouvel élément pivot (le dernier élément du sous-tableau). Pour chaque nouvel élément pivot, on met à gauche les éléments du sous-tableau qui sont plus petits que le pivot et on met à droite les éléments du sous-tableau qui sont plus grands que le pivot. **<span style="color:rgb(89, 51, 209)">On répète</span>** ces mêmes opérations jusqu’à ce qu’il ne reste plus que des tableaux à 1 élément (plus que des pivots). A ce stade, le tableau est trié.

Intéressons‑nous maintenant à la complexité de cet algorithme. A chaque étape (à chaque ligne de la figure ci-dessus), on compare tout au plus `n` éléments avec les éléments pivots, ce qui nous fait un multiple de `n` {glo}`instruction|instructions` élémentaires. Mais combien d’étapes faut-il pour que l'algorithme se termine ? 

Dans le meilleur cas, à chaque étape de l'algorithme, l’espace de recherche est divisé par 2. Nous avons vu dans le chapitre <a href="../algo2/recherche.html#rech-bin">Recherche binaire</a> que lorsqu’on divise l’espace de recherche par deux, on obtient une complexité logarithmique. Le nombre d'étapes nécessaires est donc un multple de `log(n)`. 

Pour obtenir le nombre total d'instructions élémentaires on multiplie le nombre d'instructions par étape avec le nombre d'étapes. La complexité que l'obtient est une fonction de `nlog(n)`, il s'agit d'une complexité **<span style="color:rgb(89, 51, 209)">linéarithmique</span>**. Un algorithme avec une complexité linéarithmique est plus lent qu'un algorithme de complexité linéaire (la recherche linéaire) ou de complexité logarithmique (la recherche binaire). Par contre, il est bien plus rapide qu'un algorithme de complexité quadratique (le tri par sélection). La figure ci-dessous permet de comparer la vitesse de croissance des complexités étudiées jusqu'ici. Le tri rapide est donc vraiment l'algorithme de tri le plus  rapide vu jusqu'ici et la complexité nous permet de comprendre pourquoi c'est le cas.


```{figure} media/graph_comp.png
---
alt: comparaison des complexités vues jusqu'ici
width: 420px
name : fig-compl-4
---
**Comparaison de complexités**. La vitesse de croissance en fonction de la taille du tableau n est montrée pour toutes les complexités vues jusqu'ici. Plus le nombre d’instructions élémentaires est grand en fonction de la taille des données, plus l’algorithme est lent. 
```

La première question que l’on se pose lorsqu’on analyse un algorithme est son ordre de complexité temporelle. Si l’algorithme est trop lent, il ne sera pas utilisable dans la vie réelle. Pour le problème du Tri, la stratégie **<span style="color:rgb(89, 51, 209)">« diviser pour régner »</span>** vient à nouveau à la rescousse.




```{admonition} Le saviez-vous ? Compliqué = complexe ?
:class: hint

Est-ce que *<span style="color:rgb(89, 51, 209)">complexe</span>* veut dire la même chose que *<span style="color:rgb(89, 51, 209)">compliqué</span>* ? Une chose compliquée est difficile à saisir ou à faire, alors qu’une chose complexe est composée d’éléments avec de nombreuses interactions imbriquées. 

```

```{admonition} Exercice 3.2. Le pire du Tri rapide
:class: note

Que se passe-t-il si on essaie de trier un tableau déjà trié avec l'algorithme du **<span style="color:rgb(89, 51, 209)">Tri rapide</span>**, en prenant toujours comme pivot le dernier élément ? Essayer par exemple avec le tableau [1, 2, 3, 4, 5, 6, 7]. 

Combien d'étapes sont nécessaires pour que l'algorithme se termine ? Quelle est la complexité dans ce cas ?

Est-ce qu'un autre choix de pivot aurait été plus judicieux ?

```

````{admonition} Solution 3.2. Le pire du Tri rapide
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Si on simule l'algorithme de Tri rapide pour le tableau [1, 2, 3, 4, 5, 6, 7] avec comme pivot le dernier élément on se retrouve avec les sous-tableaux suivants (le pivot est affiché en gras, les éléments déjà triés sont affichés en italique) :

[1, 2, 3, 4, 5, 6, **7**]

&nbsp;&nbsp;&nbsp;&nbsp; [1, 2, 3, 4, 5, **6**] [*7*] []

&nbsp;&nbsp;&nbsp;&nbsp; [1, 2, 3, 4, **5**] [*6*] [] [*7*] []

&nbsp;&nbsp;&nbsp;&nbsp; [1, 2, 3, **4**] [*5*] [] [*6*] [] [*7*] []

&nbsp;&nbsp;&nbsp;&nbsp; [1, 2, **3**] [*4*][] [*5*] [] [*6*] [] [*7*] []

&nbsp;&nbsp;&nbsp;&nbsp; [1, **2**] [*3*] [] [*4*][] [*5*] [] [*6*] [] [*7*] []

&nbsp;&nbsp;&nbsp;&nbsp; [**1**] [*2*] [] [*3*] [] [*4*][] [*5*] [] [*6*] [] [*7*] []

&nbsp;&nbsp;&nbsp;&nbsp; [] [*1*] [] [*2*], [*3*] [*4*][] [*5*] [] [*6*] [] [*7*] []

[1] [2] [3] [4] [5] [6] [7] 

Lorsque les éléments du tableau sont déjà triés, l'espace de recherche n'est plus divisé par deux. On se retrouve avec des sous-tableaux déséquilibrés, vides d'un côté et pleins de l'autre. Le nombre d'étapes n'est donc plus log(n), mais vaut `n` (7 étapes de traitement). Lorsqu'on multiple le nombre d'étapes (lignes) au nombre d'éléments à comparer par ligne, on est plutôt dans une complexité `n*n` (ou `n`<sup>`2`</sup>), donc quadratique. Dans ce scénario, le tri rapide n'est donc plus si rapide. Le choix du pivot est alors crucial et dépend du contenu du tableau.

Si on prend comme pivot l'élément du milieu du tableau, on se retrouve avec des sous-tableaux équilibrés, qui contiennent un nombre similaire d'éléments. Dans ce cas l'algorithme a besoin de moins d'étapes pour trouver la solution, de l'ordre de `log(n)`, ici 3 lignes et équivalent à `log`<sub>`2`</sub>`(7)`, de traitement au lieu de 7 auparavant : 

[1, 2, 3, **4**, 5, 6, 7]

&nbsp;&nbsp;&nbsp;&nbsp; [1, **2**, 3] [*4*], [5, **6**, 7]

&nbsp;&nbsp;&nbsp;&nbsp; [**1**] [*2*] [**3**] [*4*], [**5**] [*6*] [**7**]

&nbsp;&nbsp;&nbsp;&nbsp; [] [*1*] [] [*2*] [] [*3*] [] [*4*] [] [*5*] [] [*6*] [] [*7*]

[1] [2] [3] [4] [5] [6] [7] ]

```
````


```{admonition} Exercice 3.3. Le meilleur et le pire du Tri par insertion
:class: note

Que se passe-t-il si on essaie de trier un tableau déjà trié avec l'algorithme du **<span style="color:rgb(89, 51, 209)">Tri par insertion</span>** ? Essayer par exemple avec le tableau [1, 2, 3, 4, 5, 6, 7]. 

Combien d'étapes sont nécessaires pour que l'algorithme se termine ? Quelle est la complexité dans ce cas ?

Que se passe-t-il si on essaie de trier un tableau déjà trié, mais dans l'ordre inverse de celui qui est souhaité, avec l'algorithme du Tri par insertion ? Essayer par exemple avec le tableau [4, 3, 2, 1].

```

````{admonition} Solution 3.3. Le meilleur et le pire du Tri par insertion
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Si on simule l'algorithme de Tri par insertion pour le tableau [1, 2, 3, 4, 5, 6, 7] on se retrouve avec la configuration suivante (l'élément inséré est affiché en gras, l'élément auquel on le compare en italique) :

&nbsp;&nbsp;&nbsp;&nbsp; [**1**, 2, 3, 4, 5, 6, 7]

&nbsp;&nbsp;&nbsp;&nbsp; [*1*] [**2**, 3, 4, 5, 6, 7]

&nbsp;&nbsp;&nbsp;&nbsp; [1, *2*] [**3**, 4, 5, 6, 7]

&nbsp;&nbsp;&nbsp;&nbsp; [1, 2, *3*] [**4**, 5, 6, 7]

&nbsp;&nbsp;&nbsp;&nbsp; [1, 2, 3, *4*] [**5**, 6, 7]

&nbsp;&nbsp;&nbsp;&nbsp; [1, 2, 3, 4, *5*] [**6**, 7]

&nbsp;&nbsp;&nbsp;&nbsp; [1, 2, 3, 4, 5, *6*] [**7**]

[1, 2, 3, 4, 5, 6, 7]

On voit qu'il y a besoin de 7 étapes, ou `n` étapes, car autant que d'éléments dans le tableau. Dans chaque étape on n'a besoin de comparer qu'une fois, avec l'élément précédent. La complexité dans ce cas est `n*1 = n` ou linéaire. Pour des données presque triées, le Tri par insertion est encore plus rapide que le Tri rapide.

A premier abord, trier le tableau [5, 4 ,3, 2, 1] avec le Tri par insertion ne présente pas de difficultés. Regardons ce qui se passe :

&nbsp;&nbsp;&nbsp;&nbsp; [**5**, 4, 3, 2, 1]

&nbsp;&nbsp;&nbsp;&nbsp; [*5*] [**4**, 3, 2, 1]

&nbsp;&nbsp;&nbsp;&nbsp; [4, *5*] [**3**, 2, 1]

&nbsp;&nbsp;&nbsp;&nbsp; [*4*, **3**, 5] [2, 1]

&nbsp;&nbsp;&nbsp;&nbsp; [3, 4, *5*] [**2**, 1]

&nbsp;&nbsp;&nbsp;&nbsp; [3, *4*, **2**, 5] [1]

&nbsp;&nbsp;&nbsp;&nbsp; [*3*, **2**, 4, 5] [1]

&nbsp;&nbsp;&nbsp;&nbsp; [2, 3, 4, *5*] [**1**]

&nbsp;&nbsp;&nbsp;&nbsp; [2, 3, *4*, **1**, 5]

&nbsp;&nbsp;&nbsp;&nbsp; [2, *3*, **1**, 4, 5]

&nbsp;&nbsp;&nbsp;&nbsp; [*2*, **1**, 3, 4, 5]

[1, 2, 3, 4, 5]

Cette fois-ci on se retrouve dans la pire configuration pour le Tri par inserstion, où chaque élément doit être comparé à chaque autre élément. Ici nous avons besoin de 11 étapes de traitement pour trier 5 éléments, alors qu'avant 7 étapes suffisaient pour trier 7 éléments. Lorsqu'on doit trier un grand nombre d'éléments, ces différence est significative et peut rendre un algorithme non utilisable.

```
````

Si on trie un tableau qui est en fait déjà trié avec le tri par insertion, la complexité dans ce cas est linéaire.  Au contraire, si on trie ce même tableau avec le tri rapide, la complexité dans ce cas est quadratique. On voit donc que selon le tableau que l’on trie, le tri rapide peut être bien plus lent que le tri par insertion.

Une analyse complète d’un algorithme consiste à calculer la complexité non seulement dans le **<span style="color:rgb(89, 51, 209)">cas moyen</span>**, mais aussi dans le **<span style="color:rgb(89, 51, 209)">meilleur cas</span>** et dans le **<span style="color:rgb(89, 51, 209)">pire cas</span>**. 


````{admonition} Pour aller plus loin
:class: attention

Une analyse complète va également calculer les constantes qui influencent l’ordre de complexité. Ces constantes ne sont pas importantes lors d’une première analyse d’un algorithme. En effet, les constantes n’ont que peu d’effet pour une grande taille des données `n`, c’est uniquement le terme qui grandit le plus rapidement en fonction de `n` qui compte, et qui figure dans un premier temps dans l’ordre de complexité. Par contre, lorsque l’on souhaite comparer deux algorithmes de même complexité, il faut estimer les constantes et choisir l'algorithme avec une constante plus petite.

La notation « Grand O », que l'on utilise pour écrire mathématiquement la complexité, désigne en fait la complexité dans le pire cas. Les différentes complexités vues jusqu'ici seraient notées : `O(n)`, `O(log(n))`, `O(n`<sup>`2`</sup>`)` et `O(nlog(n))`. Arrivez-vous à trouver les adjectifs correspondants ?

````

## 3.2. Exercices

```{admonition} Exercice 3.4. Une question à un million
:class: note

Si une instruction prend 10<sup>-6</sup> secondes, combien de temps faut-il pour trier un tableau d’un million d’éléments avec le tri à sélection comparé au tri rapide (sans tenir compte de la constante) ?

```

```{admonition} Exercice 3.5. Une question de pivot
:class: note

Trier le tableau suivant avec l’algorithme de tri rapide : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main, en prenant le dernier élément comme pivot. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

Est-ce que le choix du pivot est important ?

```

```{admonition} Exercice 3.6. Une question de sélection
:class: note

Trier le tableau suivant avec l’algorithme de tri par sélection : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```

```{admonition} Exercice 3.7. Une question d'insertion
:class: note

Trier le tableau suivant avec l’algorithme de tri par insertion : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```

```{admonition} Exercice 3.8. Une question de bulles
:class: note

Trier le tableau suivant avec l’algorithme de tri à bulles : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```

````{admonition} Exercice 3.9. Une question de chronomètre 🔌
:class: note

Créer une liste qui contient les valeurs de 1 à n dans un ordre aléatoire, où n prend la valeur 100, par exemple. Indice : utiliser la fonction `shuffle()` du module `random`.

Implémenter au moins deux des trois algorithmes de tri vu au cours.
A l’aide du module `time` et de sa fonction `time()`, chronométrer le temps prend le tri d'une liste de 100, 500, 1000, 10000, 20000, 30000, 40000 puis 50000 nombres. 

Noter les temps obtenus et les afficher sous forme de courbe dans un tableur. Ce graphique permet de visualiser le temps d’exécution du tri en fonction de la taille de la liste. Que peut-on constater ?

Sur la base de ces mesures, peut-on estimer le temps que prendrait le tri de 100000 éléments ?

Lancer votre programme avec 100000 éléments et comparer le temps obtenu avec votre estimation.

````


````{admonition} Ai-je compris ?
:class: attention

1. Je sais que grâce à la stratégie algorithmique « diviser pour régner », je ne passe pas mon temps à attendre que l’ordinateur me donne une réponse.

2. Je sais comment trier de manière rapide.

3. Je sais que la complexité temporelle peut changer selon la configuration des données, en plus du cas moyen, il est également utile d’estimer le pire et le meilleur cas.

````




## 3.1. Tri fusion


Un autre {glo}`algo|algorithme` de complexité `O(nlog(n))` est le **<span style="color:rgb(89, 51, 209)">tri fusion</span>**. L’{glo}`algo|algorithme` se base sur l’idée qu’il est difficile de trier beaucoup d’éléments, mais qu’il est très facile de trier deux éléments et de fusionner deux tableaux déjà triés.


<span id="diviser"></span>

L’{glo}`algo|algorithme` commence par une phase de division : on découpe le tableau en deux, jusqu’à arriver à uniquement des tableaux à 1 élément (voir la Figure **Diviser** ci-dessous). Le nombre d’étapes nécessaires pour découper le tableau en tableaux à 1 élément en divisant toujours les tableaux en deux est `log(n)`.



La deuxième phase consiste à fusionner les petits tableaux. On commence par fusionner les éléments 1 à 1, dans un ordre qui dépend de leur taille. Il suffit d’assembler les deux éléments du plus petit au plus grand (voir la 2e ligne de la <a href="#fusionner">Figure **Fusionner**</a> ci-dessous).


<!--
```{figure} media/Tri_fusion_diviser.png
---
alt: etape de division dans le tri fusion
width: 360px
name : fig-div-fus
---
**Diviser.** Illustration de la première phase du tri fusion. A chaque étape le tableau est découpé en deux jusqu’à ce qu’il ne reste que des tableaux à 1 élément
```
-->

```{image} media/Tri_fusion_diviser.png
:width: 400px
:height: 300px
```
**Diviser.** Illustration de la première phase du tri fusion. A chaque étape le tableau est découpé en deux jusqu’à ce qu’il ne reste que des tableaux à 1 élément
<br> <br>


<!--
<span id="fusionner"></span>

```{figure} media/Tri_fusion_fusionner.png
---
alt: etape de fusion dans le tri fusion
width: 360px
name : fig-fus-fus
---
**Fusionner.**Illustration de la deuxième phase du tri fusion. A chaque étape les tableaux sont fusionnés par paires de deux, en faisant attention à respecter l’ordre de tri. On continue ainsi jusqu’à ce qu’il ne reste qu’un tableau unique.
```
-->

```{image} media/Tri_fusion_fusionner.png
:width: 400px
:height: 300px
```
**Fusionner.** Illustration de la deuxième phase du tri fusion. A chaque étape les tableaux sont fusionnés par paires de deux, en faisant attention à respecter l’ordre de tri. On continue ainsi jusqu’à ce qu’il ne reste qu’un tableau unique
<br> <br>


Dans les prochaines étapes (lignes 3 et 4 de la Figure **Fusionner** ci-dessus), on continue à fusionner les tableaux par paires de deux. Il est facile de fusionner ces tableaux, car ils sont déjà triés. Tout d’abord, on compare les premiers éléments des deux tableaux et on prend le plus petit des deux. Concrètement, on enlève le plus petit élément des deux tableaux pour commencer un nouveau tableau fusionné. On compare ensuite les premiers éléments des éléments restants dans les tableaux à fusionner et on prend à nouveau le plus petit des deux. On continue de la sorte jusqu’à ce qu’il ne reste pas d’éléments dans les tableaux à fusionner. 

Chaque étape de la phase de fusion consiste à comparer deux éléments `n` fois, autant qu’il y a d’éléments à fusionner dans le tableau. Elle prend donc un temps qui grandit linéairement en fonction de la taille du tableau `n`. En tout il y a besoin de `log(n)` d’étapes ce qui nous donne l’ordre de complexité `O(nlog(n))`.


```{admonition} Le saviez-vous ?
:class: hint

Le tri rapide et le tri fusion se basent sur la stratégie algorithmique de résolution de problèmes **<span style="color:rgb(89, 51, 209)">« diviser pour régner »</span>**. Cette stratégie qui consiste à :

&nbsp;&nbsp;&nbsp;&nbsp; Diviser : décomposer le problème initial en sous-problèmes ;

&nbsp;&nbsp;&nbsp;&nbsp; Régner : résoudre les sous-problèmes ;

&nbsp;&nbsp;&nbsp;&nbsp; Combiner : calculer une solution au problème initial à partir des solutions des sous-problèmes.

Les sous-problèmes étant plus petits, ils sont plus faciles et donc plus rapides à résoudre. Les algorithmes de ce type sont efficaces et se prêtent à la résolution en parallèle (p.ex.  multiprocesseurs).  

```

````{admonition} Pour aller plus loin
:class: attention

La première question que l’on se pose lorsqu’on analyse un algorithme est son ordre de complexité. Si l’algorithme est trop lent, il ne sera pas utilisable dans la vie réelle. Lorsqu’on parle de complexité, on pense en fait à la complexité moyenne, mais on peut également calculer la complexité dans le meilleur et dans le pire cas.

Par exemple, si on trie un tableau qui est en fait déjà trié avec le tri par insertion, la complexité dans ce cas est linéaire ou `O(n)`.  Au contraire, si on trie ce même tableau avec le tri rapide, la complexité dans ce cas est quadratique ou O(n<sup>2</sup>). On voit donc que selon le tableau que l’on trie, le tri rapide peut être bien plus lent que le tri par insertion.

Une analyse complète d’un algorithme consiste à calculer la complexité non seulement dans le **<span style="color:rgb(89, 51, 209)">cas moyen</span>**, mais aussi dans le **<span style="color:rgb(89, 51, 209)">meilleur cas</span>** et dans le **<span style="color:rgb(89, 51, 209)">pire cas</span>**. 

Une analyse complète va également calculer les constantes qui influencent l’ordre de complexité. Ces constantes ne sont pas importantes lors d’une première analyse d’un algorithme. En effet, les constantes n’ont que peu d’effet pour une grande taille des données n, c’est uniquement le terme qui grandit le plus rapidement en fonction de n qui compte, et qui figure dans un premier temps dans l’ordre de complexité. Par contre, lorsque l’on souhaite comparer deux algorithmes de la même complexité, il faut estimer les constantes et prendre celui des deux avec la plus petite constante.

````





```{admonition} Exercice 6 : comparaison de tris ✏️📒
:class: note

Si une instruction prend 10<sup>-6</sup> secondes, combien de temps faut-il pour trier un tableau d’1 million d’éléments avec le tri à sélection comparé au tri rapide (sans tenir compte de la constante) ? 
```

````{admonition} Solution
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Pour trier 1 million d’éléments, le tri par sélection prend 10<sup>6</sup>*10<sup>6</sup> *10<sup>-6</sup> secondes ou 1 million de secondes (équivalent à plus de 11 jours), alors que le tri rapide a besoin de log2(10<sup>6</sup>)*10<sup>6</sup> *10<sup>-6</sup> ou ~20 secondes. 

Cette différence de temps est suffisante pour rendre rédhibitoire l’utilisation du tri par sélection. Pensez au nombre de clients qu’un réseau social possède, ou au nombre de produits qu’un supermarché doit gérer.
```

````

```{admonition} Exercice 7 : tri rapide et pivot ✏️📒
:class: note

Trier le tableau suivant avec l’algorithme de tri rapide : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main, en prenant le dernier élément comme pivot. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

Est-ce que le choix du pivot est important ?

```

````{admonition} Solution
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Lors de la première étape du tri rapide, l’élément pivot est 5. On se retrouve donc avec les deux tableaux suivants :

&nbsp;&nbsp;&nbsp;&nbsp; [[3, 1, 4, 2], 5, [6, 8, 7, 9]]

Les nouveaux éléments pivots sont les derniers éléments des nouveaux tableaux de gauche [3, 1, 4, 2] et le tableau de droite [6, 8, 7, 9] , donc 2 et 9. On réarrange tous les éléments des tableaux autour des éléments pivots, selon leur taille :

&nbsp;&nbsp;&nbsp;&nbsp; 	[[1], 2, [3, 4], 5, [6, 8, 7], 9 [ ]]

On continue les mêmes opérations pour les tableaux qui contiennent plus d’un élément : [3, 4] et [6, 8, 7]. Les nouveaux pivots sont 4 et 7, car ils sont les derniers éléments des tableaux restants à plus d’un élément :

&nbsp;&nbsp;&nbsp;&nbsp; 	[1, 2, [3], 4, [ ], 5, [6], 7, [8], 9]

Il ne reste plus de tableaux de plus d’un élément, le tableau est donc trié :

&nbsp;&nbsp;&nbsp;&nbsp; 	[1, 2, 3, 4, 5, 6, 7, 8, 9]

Le choix du pivot est important et à prendre en comptes si on a des indications sur le tableau à trier.

```
````

```{admonition} Exercice 8 : tri fusion ✏️📒
:class: note

Trier le tableau suivant avec l’algorithme de tri fusion : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

N’y a-t-il qu’une seule solution ?

```

````{admonition} Solution
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Lors de la première étape du tri fusion, on divise le tableau en deux, jusqu’à arriver à des tableaux d’un seul élément :

&nbsp;&nbsp;&nbsp;&nbsp; 	[3, 6, 8, 7]  [1, 9, 4, 2, 5]

&nbsp;&nbsp;&nbsp;&nbsp; 	[3, 6]  [8, 7]  [1, 9]  [4, 2, 5]

&nbsp;&nbsp;&nbsp;&nbsp; 	[3]  [6]  [8]  [7]  [1]  [9]  [4]  [2, 5]

&nbsp;&nbsp;&nbsp;&nbsp; 	[3]  [6]  [8]  [7]  [1]  [9]  [4]  [2]  [5]

Une autre solution consiste par diviser le tableau en deux tableaux de 5 et 4 éléments lors de la première division. Lors de la deuxième étape du tri fusion, on fusionne les tableaux deux à deux, en respectant l’ordre de tri :

&nbsp;&nbsp;&nbsp;&nbsp; 	[3, 6]  [7, 8]  [1, 9]   [2, 4]  [5]

&nbsp;&nbsp;&nbsp;&nbsp; 	[3, 6, 7, 8]  [1, 2, 4, 9]  [5]

&nbsp;&nbsp;&nbsp;&nbsp; 	[1, 2, 3, 4, 6, 7, 8, 9]  [5]

Concrètement, pour fusionner les tableaux [3, 6, 7, 8]  [1, 2, 4, 9], on prend toujours le plus petit des deux premiers éléments des deux tableaux :

&nbsp;&nbsp;&nbsp;&nbsp; [3, 6, 7, 8]  [1, 2, 4, 9]	&nbsp;&nbsp; → &nbsp;&nbsp; 3 > 1  &nbsp;&nbsp; → &nbsp;&nbsp; on prend 1  &nbsp;&nbsp;	→ &nbsp;&nbsp; 	[1]

&nbsp;&nbsp;&nbsp;&nbsp; 		[3, 6, 7, 8]  [2, 4, 9]    &nbsp;&nbsp; → &nbsp;&nbsp;  3 < 2	&nbsp;&nbsp; → &nbsp;&nbsp; on prend 2 	&nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2]

&nbsp;&nbsp;&nbsp;&nbsp; 		[3, 6, 7, 8]  [4, 9]	&nbsp;&nbsp; → &nbsp;&nbsp;  3 < 4  	&nbsp;&nbsp; → &nbsp;&nbsp; on prend 3  	&nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2, 3]

&nbsp;&nbsp;&nbsp;&nbsp; 		[6, 7, 8]  [4, 9]    	&nbsp;&nbsp; → &nbsp;&nbsp;  6 > 4	&nbsp;&nbsp; → &nbsp;&nbsp;on prend 4 &nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2, 3, 4]

&nbsp;&nbsp;&nbsp;&nbsp; 		[6, 7, 8]  [9]    		&nbsp;&nbsp; → &nbsp;&nbsp;  6 < 9	&nbsp;&nbsp; → &nbsp;&nbsp; on prend 6 	&nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2, 3, 4, 6]

&nbsp;&nbsp;&nbsp;&nbsp; 		[7, 8]  [9]    		&nbsp;&nbsp; → &nbsp;&nbsp;  7 < 9	&nbsp;&nbsp; → &nbsp;&nbsp; on prend 7 	&nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2, 3, 4, 6, 7]

&nbsp;&nbsp;&nbsp;&nbsp; 		[8]  [9]    		&nbsp;&nbsp; → &nbsp;&nbsp;  8 < 9	&nbsp;&nbsp; → &nbsp;&nbsp; on prend 8 	&nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2, 3, 4, 6, 7, 8]

&nbsp;&nbsp;&nbsp;&nbsp; 		[  ]  [9]    		  		&nbsp;&nbsp; → &nbsp;&nbsp; on prend 9 &nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2, 3, 4, 6, 7, 8, 9]

On procède de la même manière pour fusionner le tableau contenant le chiffre et on arrive ainsi à la solution du tableau trié : 

&nbsp;&nbsp;&nbsp;&nbsp; 	[1, 2, 3, 4, 5, 6, 7, 8, 9]

````

```{admonition} Exercice 9 : tri par selection ✏️📒
:class: note

Trier le tableau suivant avec l’algorithme de tri par sélection : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```

````{admonition} Solution
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Lors de la première étape du tri par sélection, on cherche le plus petit élément :

&nbsp;&nbsp;&nbsp;&nbsp; [3, 6, 8, 7, **<span style="color:rgb(89, 51, 209)">1</span>**, 9, 4, 2, 5]

On échange les positions du premier et du plus petit élément :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">1</span>**, 6, 8, 7, **<span style="color:rgb(89, 51, 209)">3</span>**, 9, 4, 2, 5]

On cherche le plus petit élément dans le tableau, en excluant l’élément que l’on vient de trier :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, 6, 8, 7, 3, 9, 4, **<span style="color:rgb(89, 51, 209)">2</span>**, 5]

On échange sa position avec le 2e élément du tableau :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, 8, 7, 3, 9, 4, **<span style="color:rgb(89, 51, 209)">6</span>**, 5]

Notez que les étapes qui changent l’ordre des éléments du tableau sont disposées à gauche. On cherche le plus petit élément du tableau non trié et on l’échange avec le troisième élément :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, 8, 7, **<span style="color:rgb(89, 51, 209)">3</span>**, 9, 4, 6, 5]	

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(89, 51, 209)">3</span>**, 7, **<span style="color:rgb(89, 51, 209)">8</span>**, 9, 4, 6, 5] 

On continue de la sorte jusqu’à ce que tous les éléments soient triés (les éléments triés sont en vert) :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, 7, 8, 9, **<span style="color:rgb(89, 51, 209)">4</span>**, 6, 5]

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, 8, 9, **<span style="color:rgb(89, 51, 209)">7</span>**, 6, 5]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, 8, 9, 7, 6, **<span style="color:rgb(89, 51, 209)">5</span>**]

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(89, 51, 209)">5</span>**, 9, 7, 6, **<span style="color:rgb(89, 51, 209)">8</span>**]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">5</span>**, 9, 7, **<span style="color:rgb(89, 51, 209)">6</span>**, 8]

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">5</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, 7, **<span style="color:rgb(89, 51, 209)">9</span>**, 8]

Le septième élément du tableau est déjà à la bonne position, donc il n’y a pas besoin d’échanger la position de deux éléments. Le tableau est trié lorsque tous les éléments sont parcourus.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">5</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, 9, 8]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">5</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, 9, **<span style="color:rgb(89, 51, 209)">8</span>**]


&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">5</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**]

```
````

```{admonition} Exercice 10 : tri par insertion ✏️📒
:class: note

Trier le tableau suivant avec l’algorithme de tri par insertion : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```

````{admonition} Solution
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Lors de la première étape du tri par insertion, on cherche à trouver la bonne position du 2e élément, dans ce cas l’élément 6 reste au même emplacement, car 3 est plus petit que 6 :

&nbsp;&nbsp;&nbsp;&nbsp; [3, **<span style="color:rgb(89, 51, 209)">6</span>**, 8, 7, 1, 9, 4, 2, 5]

Le prochain élément considéré est le 8. Cet élément est également déjà bien placé :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	[**<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, 7, 1, 9, 4, 2, 5]

Comme l’ordre des éléments ne change pas, nous notons cette configuration à droite.

Le prochain élément considéré est le 7. Cet élément n’est pas bien placé au regard du tableau que l’on a déjà trié. Sa place est avant le 8, on va donc l’insérer entre le 6 et le 8 : 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	[**<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">8</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, 1, 9, 4, 2, 5]

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, 1, 9, 4, 2, 5]

Le prochain élément de la liste non triée est le 1 :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, **<span style="color:rgb(13, 204, 166)">8</span>**, **<span style="color:rgb(89, 51, 209)">1</span>**, 9, 4, 2, 5] 

Nous allons l’insérer à la bonne position du tableau déjà trié, c’est-à-dire tout au début :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">1</span>**, **<span style="color:rgb(89, 51, 209)">3</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, 9, 4, 2, 5]

Tous les éléments qui ont changé de position dans l’étape précédente sont désignés en rouge. Le prochain élément à considérer est le 9. Il est déjà bien placé par rapport à la partie triée du tableau :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, **<span style="color:rgb(13, 204, 166)">8</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**, 4, 2, 5]

On continue de la sorte jusqu’à ce que tous les éléments du tableau soient parcourus :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, **<span style="color:rgb(13, 204, 166)">8</span>**, **<span style="color:rgb(13, 204, 166)">9</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, 2, 5]

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**,  2, 5]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, **<span style="color:rgb(13, 204, 166)">8</span>**, **<span style="color:rgb(13, 204, 166)">9</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, 5]

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, **<span style="color:rgb(89, 51, 209)">3</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**, 5]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, **<span style="color:rgb(13, 204, 166)">8</span>**, **<span style="color:rgb(13, 204, 166)">9</span>**, **<span style="color:rgb(89, 51, 209)">5</span>**]

Lorsque le dernier élément du tableau est inséré à la bonne position, tout le tableau est trié :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(89, 51, 209)">5</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**]

```
````

```{admonition} Exercice 11 : tri à bulles ✏️📒
:class: note

Trier le tableau suivant avec l’algorithme de tri à bulles : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```

````{admonition} Exercice 12. Comparaison temporelle des algorithmes de tris 🔌
:class: note

Créer une liste qui contient les valeurs de 1 à n dans un ordre aléatoire, où n prend la valeur 100, par exemple. Vous pouvez utiliser la fonction shuffle() du module random.

Implémenter au moins deux des trois algorithmes de tri vu au cours.
A l’aide du module time et de sa fonction time(), chronométrez le temps prend le tri d'une liste de 100, 500, 1000, 10000, 20000, 30000, 40000 puis 50000 nombres. 

Noter les temps obtenus et affichez-les sous forme de courbe dans un tableur. Ce graphique permet de visualiser le temps d’exécution du tri en fonction de la taille de la liste. Que constatez‑vous ?

Sur la base de ces mesures, pouvez-vous estimer le temps que prendrait le tri de 100000 éléments ?

Lancer votre programme avec 100000 éléments et comparez le temps obtenu avec votre estimation.

````


<!--
&nbsp;&nbsp;&nbsp;&nbsp; cn + c(n-1) + c(n-2) + ... + c(n/2+1) + c(n/2) + ... + 3c + 2c + c

Si on réarrange l’ordre des termes on obtient cette somme d’{glo}`instruction|instructions` :

&nbsp;&nbsp;&nbsp;&nbsp; cn + c + c(n-1) + 2c + c(n-2) + 3c + ... + c(n/2+1) + c(n/2)

On groupe ensuite les termes deux par deux :

&nbsp;&nbsp;&nbsp;&nbsp; (cn + c) + (c(n-1) + 2c) + (c(n-2) + 3c) + ... + (c(n/2+1) + c(n/2))

On obtient ainsi plusieurs fois le même terme :

&nbsp;&nbsp;&nbsp;&nbsp; c(n+1) + c(n+1) + c(n+1) + ... + c(n+1) 

Nous avons commencé par `n` termes, que l’on a combinés deux par deux. On se retrouve donc avec la moitié des termes ou `n/2` :

&nbsp;&nbsp;&nbsp;&nbsp; c(n+1)*n/2	

Le terme qui divise par 2 peut être absorbé dans la {glo}`constante|constante` `c` (la valeur de celle-ci changerait). Finalement, on ajoute une constante a pour prendre en compte le nombre d’{glo}`instruction|instructions` qui ne dépendent pas de la taille des données (p. ex : initialisations au début de l’{glo}`algo|algorithme`) :

&nbsp;&nbsp;&nbsp;&nbsp; c’(n+1)*n + a = c’n2 + c’n + a	ou 	c’= c/2	
-->

