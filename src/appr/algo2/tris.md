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

## 3.1. Tri rapide

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

