

# Trie, cherche et trouve

````{thinkingmatter} Bibliothèque inutile

Imaginez une bibliothèque scolaire un peu spéciale : les livres n’y sont pas rangés par ordre alphabétique ! Ils sont bien rangés sur des étagères, mais sans aucune logique particulière. Vous entrez dans cette bibliothèque un peu spéciale et vous vous mettez à chercher l’ouvrage ***<span style="color:rgb(13, 204, 166)">Le&nbsp;Guide&nbsp;du&nbsp;voyageur&nbsp;galactique.</span>***

Pensez&#8209;vous pouvoir retrouver ce livre ? Combien de temps cela vous prendra-t-il ? 

Y a-t-il des objets chez vous, que vous rangez dans un ordre bien particulier ?

Y a-t-il des objets chez vous, que vous feriez mieux de ranger dans un ordre bien particulier, parce que vous passez beaucoup de temps à les chercher ?

````

Pour l'instant il faut nous croire sur parole, mais si l'on veut pouvoir trouver une information parmi une avalanche d'informations, il faut que ces informations soient bien rangées. L'exemple de la bibliothèque ci&#8209;dessus illustre ce besoin de manière intuitive, mais vous allez pouvoir l'expérimenter concrètement dans le chapitre Algorithmique II. 

Saviez&#8209;vous que le succès fulgurant de *Google* est surtout dû à sa capacité à bien ranger l'information disponible sur le Web ? Au moment où vous avez besoin d'une information particulière, leurs algorithmes sont capables de la retrouver parce qu'elle est bien rangée. Ce problème qui consiste à ranger les données a un nom, il s'agit du **<span style="color:rgb(89, 51, 209)">problème&nbsp;du&nbsp;Tri</span>**. Il est si important qu'il est un des problèmes les plus étudiés en algorithmique.


## Algorithmes de tri

<span id=fig-trier></span>Un **<span style="color:rgb(89, 51, 209)">algorithme de tri</span>** est un algorithme qui permet de résoudre le problème du tri des données, donc d'organiser les données selon ***<span style="color:rgb(13, 204, 166)">une relation d’ordre</span>***. Dans la figure ci&#8209;dessous, les objets sont organisés soit par la luminosité de leur couleur (ligne du haut), soit par leur taille (lignes du bas), dans un **ordre croissant**.


```{figure} media/Tris_base.png
---
alt: Problème du tri.
width: 33%
align : left
---

**Problème du tri.** Des objets sont triés selon une relation d’ordre, en lien avec une propriété. Sur&nbsp;la ligne du haut, les rectangles sont organisés selon leur couleur (de la plus sombre à la plus claire), alors&nbsp;que sur la ligne du bas, ils sont triés selon leur taille (du plus petit au plus grand). 

```


`````{htmlonly}
````{exercise} Problème du tri

Trier les rectangles de la ligne du haut de la <a href="#fig&#8209;trier">figure ci&#8209;dessus</a> en fonction de leur taille, pour arriver à la disposition de la ligne du bas. Noter toutes les étapes intermédiaires de vos actions et la disposition des rectangles avant d’arriver à la solution finale. Conseil : remplacer les rectangles par un nombre qui représente leur taille.

En lien avec les ingrédients d’un algorithme, déterminer les données en entrée et le résultat en sortie de l’algorithme.

Quels types d'opérations avez&#8209;vous effectuées ? 
````
`````
`````{latexonly}
````{exercise} Problème du tri

Trier les rectangles de la ligne du haut de la figure précédente en fonction de leur taille, pour arriver à la disposition de la ligne du bas. Noter toutes les étapes intermédiaires de vos actions et la disposition des rectangles avant d’arriver à la solution finale. Conseil : remplacer les rectangles par un nombre qui représente leur taille.

En lien avec les ingrédients d’un algorithme, déterminer les données en entrée et le résultat en sortie de l’algorithme.

Quels types d'opérations avez&#8209;vous effectuées ? 
````

`````{htmlonly} 
````{solution} 
```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Si&nbsp;on remplace les rectangles de la ligne du haut par un nombre qui représente leur taille, on obtient la liste&nbsp;`[3, 4, 1, 2, 6, 5]`. Le plus important est que l'ordre des nombres conserve l'ordre de la taille des rectangles. Après le tri, si l'algorithme est correct, vous devriez vous retrouver avec la&nbsp;liste&nbsp;`[1, 2, 3, 4, 5, 6]`. Les opérations et les dispositions intermédiaires exactes dépendent de l'algorithme que vous avez utilisé. 

Les données en entrée sont les rectangles sur la ligne du haut : leur taille et l'ordre de leur taille, ici &nbsp;`[3, 4, 1, 2, 6, 5]`. Le résultat en sortie correspond aux rectangles sur la ligne du bas : l'ordre croissant de leur taille, ici&nbsp;`[1, 2, 3, 4, 5, 6]`. 

Les types d'opérations que vous avez effectuées sont des comparaisons de la taille de deux rectangles et des déplacements de rectangles.

```
````
`````
````{latexonly} 
```{solution} 

Si&nbsp;on remplace les rectangles de la ligne du haut par un nombre qui représente leur taille, on obtient la liste&nbsp;`[3, 4, 1, 2, 6, 5]`. Le plus important est que l'ordre des nombres conserve l'ordre de la taille des rectangles. Après le tri, si l'algorithme est correct, vous devriez vous retrouver avec la&nbsp;liste&nbsp;`[1, 2, 3, 4, 5, 6]`. Les opérations et les dispositions intermédiaires exactes dépendent de l'algorithme que vous avez utilisé. 

Les données en entrée sont les rectangles sur la ligne du haut : leur taille et l'ordre de leur taille, ici &nbsp;`[3, 4, 1, 2, 6, 5]`. Le résultat en sortie correspond aux rectangles sur la ligne du bas : l'ordre croissant de leur taille, ici&nbsp;`[1, 2, 3, 4, 5, 6]`. 

Les types d'opérations que vous avez effectuées sont des comparaisons de la taille de deux rectangles et des déplacements de rectangles.

```
````



<br>

Nous allons exposer ici **trois algorithmes de tri simple**, que l'on pourrait utiliser pour trier des objets dans la vie de tous les jours.

## Tri&nbsp;par&nbsp;insertion

L’{glo}`algo|algorithme` du **<span style="color:rgb(89, 51, 209)">tri&nbsp;par&nbsp;insertion</span>** parcourt la liste d’éléments à trier du deuxième au dernier élément. Pour&nbsp;chaque nouvel élément considéré, il l'insère à l'emplacement correct dans la liste déjà parcourue. A&nbsp;tout&nbsp;moment, la liste d'éléments déjà parcourus (jusqu’à l’élément que l'on considère à un moment donné) est toujours bien triée.
```{htmlonly}
<span id=tri-selection></span>
```

## Tri&nbsp;par&nbsp;sélection

L’{glo}`algo|algorithme` du **<span style="color:rgb(89, 51, 209)">tri&nbsp;par&nbsp;sélection</span>** commence par rechercher le plus petit élément de la liste et l’échange avec le premier élément de la liste. Il&nbsp;recherche ensuite le plus petit élément de la liste restante (sans le premier plus petit élément). Il&nbsp;sélectionne ainsi le deuxième plus petit élément de la liste et l’échange avec le deuxième élément de la liste. Et&nbsp;ainsi de&nbsp;suite : il recherche le plus petit élément de la liste restante, en excluant les éléments déjà triés, et échange ce plus petit élément avec le premier élément pas encore trié. Il&nbsp;continue de la sorte jusqu’à arriver au dernier élément de la liste. 

## Tri&nbsp;à&nbsp;bulles

L’{glo}`algo|algorithme` du **<span style="color:rgb(89, 51, 209)">tri&nbsp;à&nbsp;bulles</span>** compare les éléments voisins, deux&nbsp;par&nbsp;deux. Il&nbsp;commence par comparer les deux premiers éléments de la liste et les met dans le bon ordre (le plus petit des deux éléments précède le plus grand des&nbsp;deux). Il&nbsp;compare ensuite les deux éléments suivants (le nouveau deuxième et le troisième élément de la liste) et les met dans le bon ordre. Il&nbsp;continue de la sorte jusqu’à la fin de la liste. Après&nbsp;ce premier&nbsp;parcours de la liste, le plus grand élément se retrouve en dernière position de la liste. L'algorithme parcourt à nouveau la liste, en comparant et en déplaçant les éléments voisins deux par deux (en excluant également le dernier élément qui est déjà bien trié). Après&nbsp;le deuxième&nbsp;parcours de la liste, le deuxième plus grand élément se retrouve en avant&#8209;dernière position de la liste. L'algorithme parcourt la liste de la sorte, autant de fois qu’elle possède d’éléments, en excluant les éléments bien triés en fin de la liste.


````{exercise} Algorithme de tri 

Il est fortement recommandé de résoudre cet exercice avant d’avancer dans le chapitre. 

Appliquer au&nbsp;moins&nbsp;un des trois algorithmes ci-dessus (tri&nbsp;par&nbsp;insertion, tri&nbsp;par&nbsp;sélection et tri&nbsp;à&nbsp;bulles) pour trier les rectangles de la ligne du haut de la <a href="#fig-trier">figure **Problème du tri**</a> en fonction de leur taille (le résultat est illustré dans la ligne du bas). 

Noter l’ordre des éléments à&nbsp;chaque fois qu’il change. Vous aurez besoin d’une grande feuille de papier. Vous pouvez aussi représenter la taille des rectangles par un nombre, cela permet de gagner de la place. Si&nbsp;cela vous aide, vous pouvez découper les rectangles ci-dessous et les manipuler. 

<img src="media/Tris_decoupe.png" width="60%"> &nbsp;  

````

`````{htmlonly} 
````{solution} 
```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

La solution est donnée dans la suite du chapitre et est illustrée dans la figure **Algorithmes&nbsp;de&nbsp;tri** ci&#8209;dessous.

```
````
`````
````{latexonly} 
```{solution} 

La solution est donnée dans la suite du chapitre et est illustrée dans la figure **Algorithmes&nbsp;de&nbsp;tri**.

```
````


````{note} Quand on cherche on trouve. Vraiment ?

Vous passez trop de temps à chercher vos affaires ? Pensez à mieux les trier. Le temps perdu à ranger vos affaires sera bien inférieur à celui que vous passerez à les chercher plus tard.

````

<span id=fig-algos-tri></span>


```{figure} media/Tris_algorithmes.png
---
alt: Algorithmes de tri
width: 100%
align: center
---

**Algorithmes de tri**. Etapes intermédiaires lors de l’application des différents algorithmes de tri. La flèche rouge montre les mouvements des éléments suite à une opération. Si&nbsp;l’élément ne bouge pas, la flèche rouge est remplacée par un point rouge. **A&nbsp;gauche**, le tri&nbsp;par&nbsp;insertion. L’étoile dénote l’élément considéré à un moment donné. **Au&nbsp;milieu**, le tri&nbsp;par&nbsp;sélection. L’étoile désigne le plus petit élément de la liste non triée. **A&nbsp;droite**, le tri&nbsp;à&nbsp;bulles. Ici le point rouge signale les éléments triés.
```



La figure ci&#8209;dessus détaille les étapes intermédiaires des trois {glo}`algo|algorithmes` de tri vus précédemment. Dans le **<span style="color:rgb(89, 51, 209)">tri&nbsp;par&nbsp;insertion</span>** à gauche, on parcourt la liste dans l’ordre, un élément après l’autre (dénoté par une étoile). A&nbsp;chaque étape, on cherche à ***<span style="color:rgb(13, 204, 166)">insérer</span>*** le rectangle considéré à la bonne place dans la liste précédemment triée. La flèche rouge montre la position à laquelle le rectangle sera inséré après comparaison avec l'élément précédent. Si l’élément est déjà bien trié, aucune action n’est requise dans ce cas et la flèche est remplacée par un point rouge. Notez que la liste qui précède le rectangle considéré (celui avec l’étoile) est toujours bien triée. 


Dans le **<span style="color:rgb(89, 51, 209)">tri&nbsp;par&nbsp;sélection</span>** au milieu, on parcourt la liste pour ***<span style="color:rgb(13, 204, 166)">sélectionner</span>*** son plus petit élément, et on le met à la bonne position. La ligne noire au&#8209;dessous des rectangles montre la liste parcourue pour rechercher le plus petit élément. Le plus petit élément de cette liste est désigné par l’étoile. Finalement, la flèche rouge montre les éléments échangés : le premier élément de la liste non triée et le plus petit élément. Ainsi, le plus petit élément sélectionné (avec étoile) se retrouve à la fin de la liste déjà triée (liste non soulignée). Si&nbsp;l’élément est déjà bien trié et qu’aucune action n’est requise, la flèche bidirectionnelle est remplacée par un point rouge.

Dans **<span style="color:rgb(89, 51, 209)">le tri&nbsp;à&nbsp;bulles</span>** à droite, les lignes en dessous des rectangles montrent les éléments voisins qui sont comparés à&nbsp;chaque étape. Lorsque cette ligne est grise, les éléments sont déjà bien ordonnés et aucune action n’est requise. Lorsque la ligne est noire, les éléments ne sont pas dans le bon ordre et doivent être intervertis (flèche rouge). Après un passage complet de la liste, l’élément le plus grand se retrouve en dernière position, il remonte comme une ***<span style="color:rgb(13, 204, 166)">bulle</span>*** (voir la 4e ligne). Le point rouge ici indique les éléments triés. Dans ce cas, la liste est triée après deux parcours complets de la liste.



Notez que même si tous les {glo}`algo|algorithmes` arrivent à la même solution finale, ils y arrivent de manière très différente et avec plus ou moins de calculs. 



````{exercise} Votre algorithme de tri

Rappelez&#8209;vous quelle méthode vous avez utilisée pour résoudre le premier exercice. De quel algorithme de tri se rapproche-t-elle le plus ? 
````

`````{htmlonly} 
````{solution} 
```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Cela dépend de votre solution du premier exercice. Vous avez probablement utilisé la méthode du tri&nbsp;par&nbsp;sélection ou du tri&nbsp;à&nbsp;bulles.
```
````
`````
````{solution} 
```{latexonly}

Cela dépend de votre solution du premier exercice. Vous avez probablement utilisé la méthode du tri&nbsp;par&nbsp;sélection ou du tri&nbsp;à&nbsp;bulles.
```
````


````{didyouknow} Tri stupide

Il existe un algorithme, **Tri de Bogo** (ou *Bogosort*), aussi nommé le *tri lent* ou encore le *tri stupide*. C’est un tri qui génère différentes permutations des éléments de la liste et s’arrête lorsque la configuration obtenue par hasard est triée. A&nbsp;votre&nbsp;avis, combien d’opérations prend cet algorithme en moyenne ?

````


````{exercise} Opérations 

Pour chaque algorithme de tri, compter le nombre de ***<span style="color:rgb(13, 204, 166)">comparaisons</span>*** de la taille de deux rectangles, ainsi que le nombre de ***<span style="color:rgb(13, 204, 166)">déplacements</span>*** (le nombre de fois que deux rectangles échangent leur place).

Imaginons que ce qui prend le plus de temps est une ***comparaison***. Dans ce cas précis, quel algorithme de tri parmi les trois algorithmes présentés est le plus lent ? 

Imaginons que ce qui prend le plus de temps est un ***déplacement***. Dans ce cas précis, quel algorithme de tri est le plus lent ? Quel algorithme est le plus rapide ?

````

`````{htmlonly} 
````{solution} 
```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Le décompte des opérations effectuées, en se référant à la <a href="#fig-algos-tri">figure **Algorithmes de tri**</a> est comme suit :

**<span style="color:rgb(89, 51, 209)">Tri&nbsp;par&nbsp;insertion</span>** : 9 comparaisons deux par deux (flèches et points rouges) et 5 déplacements deux par deux (flèches rouges). Notez que pour insérer un élément en première position, il faut tout d'abord l'échanger avec l'élément juste devant, puis avec l'élément avant, et ainsi de suite jusqu'à arriver à la première position.

**<span style="color:rgb(89, 51, 209)">Tri&nbsp;par&nbsp;sélection</span>** : 15 comparaisons deux par deux (lignes en dessous) et 3 déplacements deux par deux (flèches rouges).

**<span style="color:rgb(89, 51, 209)">Tri&nbsp;à&nbsp;bulles</span>** : 9 comparaisons deux par deux (lignes en dessous) et 5 déplacements deux par deux (flèches rouges). 

Si&nbsp;ce qui prend beaucoup de temps est la comparaison de la taille de deux rectangles, il ne faudrait pas utiliser le tri&nbsp;par&nbsp;sélection, car il comporte le plus grand nombre de comparaisons et il serait le plus lent. Si&nbsp;c’est le déplacement de deux rectangles qui coûte beaucoup de temps, cette fois&#8209;ci le tri&nbsp;par&nbsp;sélection serait le plus rapide (avec 3 rectangles qui échangent leur position). Donc, selon l'implémentation sur la machine, le tri&nbsp;par&nbsp;sélection serait le plus lent ou le plus rapide des trois algorithmes.

Ces résultats sont valables pour cette configuration en particulier. Si&nbsp;on trie un autre tableau, la performance des trois algorithmes pourrait changer. Le choix du meilleur algorithme dépend donc de l’implémentation et de la situation initiale. Notez finalement qu’il existe des algorithmes de tri bien plus rapides que les trois algorithmes considérés ici.
```
````
`````
````{latexonly} 
```{solution} 

Le décompte des opérations effectuées, en se référant à la <a href="#fig-algos-tri">figure **Algorithmes de tri**</a> est comme suit :

**<span style="color:rgb(89, 51, 209)">Tri&nbsp;par&nbsp;insertion</span>** : 9 comparaisons deux par deux (flèches et points rouges) et 5 déplacements deux par deux (flèches rouges). Notez que pour insérer un élément en première position, il faut tout d'abord l'échanger avec l'élément juste devant, puis avec l'élément avant, et ainsi de suite jusqu'à arriver à la première position.

**<span style="color:rgb(89, 51, 209)">Tri&nbsp;par&nbsp;sélection</span>** : 15 comparaisons deux par deux (lignes en dessous) et 3 déplacements deux par deux (flèches rouges).

**<span style="color:rgb(89, 51, 209)">Tri&nbsp;à&nbsp;bulles</span>** : 9 comparaisons deux par deux (lignes en dessous) et 5 déplacements deux par deux (flèches rouges). 

Si&nbsp;ce qui prend beaucoup de temps est la comparaison de la taille de deux rectangles, il ne faudrait pas utiliser le tri&nbsp;par&nbsp;sélection, car il comporte le plus grand nombre de comparaisons et il serait le plus lent. Si&nbsp;c’est le déplacement de deux rectangles qui coûte beaucoup de temps, cette fois&#8209;ci le tri&nbsp;par&nbsp;sélection serait le plus rapide (avec 3 rectangles qui échangent leur position). Donc, selon l'implémentation sur la machine, le tri&nbsp;par&nbsp;sélection serait le plus lent ou le plus rapide des trois algorithmes.

Ces résultats sont valables pour cette configuration en particulier. Si&nbsp;on trie un autre tableau, la performance des trois algorithmes pourrait changer. Le choix du meilleur algorithme dépend donc de l’implémentation et de la situation initiale. Notez finalement qu’il existe des algorithmes de tri bien plus rapides que les trois algorithmes considérés ici.
```
````





## Comparaison d’algorithmes

Toutes les recettes de cuisine ne se valent pas, de la même manière, un {glo}`algo|algorithme` peut aussi être ***<span style="color:rgb(13, 204, 166)">plus&nbsp;approprié</span>*** qu’un autre algorithme pour résoudre le même problème. Il existe des dizaines d’{glo}`algo|algorithmes` qui trient avec des approches différentes (nous en verrons encore quelques&#8209;uns). Certains algorithmes sont plus rapides, d’autres plus économes en mémoire ou encore plus simples à coder. Ainsi, selon la situation, il faut choisir le « bon » {glo}`algo|algorithme`.

La qualité d’un {glo}`algo|algorithme` dépend de la propriété que l’on souhaite optimiser (maximiser ou minimiser). Cela pourrait être de maximiser la **<span style="color:rgb(89, 51, 209)">vitesse&nbsp;d’exécution</span>** (mesurée par le nombre d’{glo}`instruction|instructions` élémentaires exécutées), de minimiser la place occupée en **<span style="color:rgb(89, 51, 209)">mémoire</span>**, de minimiser la **<span style="color:rgb(89, 51, 209)">consommation&nbsp;d'énergie</span>** ou de maximiser la **<span style="color:rgb(89, 51, 209)">précision&nbsp;de la&nbsp;solution</span>**. L'{glo}`algo|algorithme` utilisé devrait être choisi en fonction de ce qui est important.

***<span style="color:rgb(13, 204, 166)">La&nbsp;vitesse&nbsp;d’un {glo}`algo|algorithme` dépend&nbsp;également des&nbsp;{glo}`data|données` en {glo}`input|entrée`</span>***. Selon la configuration initiale des {glo}`data|données` en {glo}`input|entrée` (correspond à la ligne du haut de la <a href="#fig-algos-tri">figure **Algorithmes de tri**</a>), un {glo}`algo|algorithme` « rapide » peut devenir « lent » et *vice versa*. Il faut savoir que les {glo}`algo|algorithmes` vus jusqu’ici sont tous des {glo}`algo|algorithmes` lents (nous verrons un {glo}`algo|algorithme` de tri&nbsp;rapide ultérieurement).


````{didyouknow} Tri trop lent

Pour trier 1&nbsp;million d’éléments, selon l’algorithme choisi, cela peut prendre de 20&nbsp;millions à 1&nbsp;billion d’opérations. Si&nbsp;chaque opération prenait 1 microseconde ($10^{-6} s$) à s’exécuter, il faudrait $20$&nbsp;secondes pour trier 1&nbsp;million d’éléments si l'algorithme est efficace. Par contre, pour un des algorithmes ci-dessus, cela pourrait prendre 11&nbsp;jours !  

````


````{togofurther}

Imaginer que les quatre éléments d’une liste sont triés dans le sens inverse de ce que l’on souhaite (ils sont placés du plus grand au plus petit). Trier la liste selon les trois algorithmes de tri vus précédemment : le tri&nbsp;par&nbsp;insertion, le tri&nbsp;par&nbsp;sélection et le tri à bulles. 

Dans cette configuration précise, quel algorithme est le plus rapide  (présente le moins d’étapes intermédiaires) ? 

Et quel algorithme est le plus lent ?

````


## Exercices


````{exercise} L'algorithme de votre journée

Réfléchir à votre journée : y a-t-il des actions qui se retrouvent chaque jour ouvrable ? Arrivez&#8209;vous à esquisser un algorithme que vous suivez sans que vous en ayez conscience ?

````


````{exercise} Trois algorithmes de tri

Trier la liste [2, 5, 3, 4, 7, 1, 6] en utilisant les trois algorithmes de tri vus dans le cours. Représenter l’état de la liste après chaque étape.

````


````{exercise} Vérificateur de tri

Ecrire un algorithme qui vérifie si une liste est triée. 

Que prend l’algorithme en entrée et que retourne-t-il en sortie ?

Demander ensuite à un autre élève de suivre les opérations décrites par votre algorithme. Est&#8209;ce que votre algorithme est correct ?

Comparer vos algorithmes. Sont&#8209;ils différents ?

````


````{exercise} Mondrian

Analyser les œuvres cubistes de Piet Mondrian. Trouver un algorithme qui permet de créer une œuvre qui pourrait être attribuée à Mondrian.

````


````{eval}

Vérifiez votre compréhension :

1. Je sais qu’il existe plusieurs manières différentes de résoudre un problème.

2. Je sais qu’il faut choisir le meilleur algorithme en fonction de critères objectifs : vitesse de l’algorithme, qualité de la solution,  espace utilisé en mémoire ou encore consommation d’énergie.

3. Je sais appliquer les trois algorithmes de tri vus dans le cours.

````











