
````{admonition} Matière à réfléchir. Bibliothèque inutile
:class: hint

Imaginez une bibliothèque scolaire un peu spéciale : les livres n’y sont pas rangés par ordre alphabétique ! Ils sont bien rangés sur des étagères, mais sans aucune logique particulière. Vous entrez dans cette bibliothèque un peu spéciale et vous vous mettez à chercher l’ouvrage ***<span style="color:rgb(13, 204, 166)">Le Guide du voyageur galactique.</span>***

Pensez-vous pouvoir retrouver ce livre ? Combien de temps cela vous prendra-t-il ? 

Y a-t-il des objets chez vous, que vous rangez dans un ordre bien particulier ?

Y a-t-il des objets chez vous, que vous feriez mieux de ranger dans un ordre bien particulier, parce que vous passez beaucoup de temps à les chercher ?

````

# 2. Trie, cherche et trouve

Pour l'instant il faut nous croire sur parole, mais si l'on veut pouvoir trouver une information parmi une avalanche d'informations, il faut que ces informations soient bien rangées. L'exemple de la bibliothèque ci-dessus illustre ce besoin de manière intuitive, mais vous allez pouvoir l'expérimenter concrètement dans le chapitre Algorithmique II. 

Saviez-vous que le succès fulgurant de *Google* est surtout dû à sa capacité à bien ranger l'information disponible sur le Web ? Au moment où vous avez besoin d'une information particulière, leurs algorithmes sont capables de la retrouver parce qu'elle est bien rangée. Ce problème qui consiste à ranger les données a un nom, il s'agit du **<span style="color:rgb(89, 51, 209)">problème du Tri</span>**. Il est si important qu'il est un des problèmes les plus étudiés en algorithmique.

## 2.1. Algorithmes de tri

<span id=fig-trier></span>

Un **<span style="color:rgb(89, 51, 209)">algorithme de tri</span>** est un algorithme qui permet de résoudre le problème du tri des données, donc d'organiser les données selon ***<span style="color:rgb(13, 204, 166)">une relation d’ordre</span>***. Dans la figure ci-dessous, les objets sont organisés soit par la luminosité de leur couleur (ligne du haut), soit par leur taille (lignes du bas), dans **un ordre croissant**.


```{figure} media/Tris_base.png
---
alt: Problème du tri.
width: 50%
align : left
---

**Problème du tri.** Des objets sont triés selon une relation d’ordre, en lien avec une propriété. Sur la ligne du haut, les rectangles sont organisés selon leur couleur (de la plus sombre à la plus claire), alors que sur la ligne du bas, ils sont triés selon leur taille (du plus petit au plus grand).

```

<!-- ```{image} media/Tris_base.png
:width: 600
:height: 300
```
**Problème du tri.** Des objets peuvent être triés selon une relation d’ordre, en lien avec une propriété. Sur la ligne du haut, les rectangles sont organisés selon leur couleur (de la plus sombre à la plus claire), alors que sur la ligne du bas, ils sont triés selon leur taille (du plus petit au plus grand). -->

<!-- Pour apprendre à cuisiner, on commence par suivre des recettes classiques. -->
<!-- Pour apprendre à cuisiner, on commence par suivre des recettes classiques. Ainsi, pour appréhender l’{glo}`algorithmique|algorithmique`, nous étudierons une classe d’{glo}`algo|algorithmes` classiques : les **<span style="color:rgb(89, 51, 209)">algorithmes de tri</span>**.  -->

 


````{admonition} Exercice 0 : problème du tri
:class: note

Trier les rectangles de la ligne du haut de la <a href="#fig-trier">Figure ci-dessus</a> en fonction de leur taille, pour arriver à la disposition de la ligne du bas. Noter toutes les étapes intermédiaires de vos actions et la disposition des rectangles avant d’arriver à la solution finale. Conseil : remplacer les rectangles par un nombre qui représente leur taille.

En lien avec les ingrédients d’un algorithme, déterminer les données en entrée et le résultat en sortie de l’algorithme.

Quels types d'opérations avez-vous effectuées ? 

````

````{admonition} Solution 0 : problème du tri
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Si on remplace les rectangles de la ligne du haut par un nombre qui représente leur taille, on obtient la liste [3, 4, 1, 2, 6, 5]. Le plus important est que l'ordre des nombres conserve l'ordre de la taille des rectangles. Après le tri, si l'algorithme est correct, vous devriez vous retrouver avec la liste [1, 2, 3, 4, 5, 6]. Les opérations et les dispositions intermédiaires exactes dépendent de l'algorithme que vous avez utilisé. 

Les données en entrée sont les rectangles sur la ligne du haut : leur taille et l'ordre de leur taille, ici [3, 4, 1, 2, 6, 5]. Le résultat en sortie correspond aux rectangles sur la ligne du bas : l'ordre croissant de leur taille, ici [1, 2, 3, 4, 5, 6]. 

Les types d'opérations que vous avez effectuées sont des comparaisons de la taille de deux rectangles et des déplacements de rectangles.

```
````

<br>

Nous allons exposer ici **trois algorithmes de tri simple**, que l'on pourrait utiliser pour trier des objets dans la vie de tous les jours.

## 2.2. Tri par insertion

L’{glo}`algo|algorithme` du **<span style="color:rgb(89, 51, 209)">tri par insertion</span>** parcourt la liste d’éléments à trier du deuxième au dernier élément. Pour chaque nouvel élément considéré, il l'insère à l'emplacement correct dans la liste déjà parcourue. A tout moment, la liste d'éléments déjà parcourus (jusqu’à l’élément que l'on considère à un moment donné) est toujours bien triée.


<span id=tri-selection></span>
## 2.3. Tri par sélection

L’{glo}`algo|algorithme` du **<span style="color:rgb(89, 51, 209)">tri par sélection</span>** commence par rechercher le plus petit élément de la liste et l’échange avec le premier élément de la liste. Il recherche ensuite le plus petit élément de la liste restante (sans le premier plus petit élément). Il sélectionne ainsi le deuxième plus petit élément de la liste et l’échange avec le deuxième élément de la liste. Et ainsi de suite : il recherche le plus petit élément de la liste restante, en excluant les éléments déjà triés, et échange ce plus petit élément avec le premier élément pas encore trié. Il continue de la sorte jusqu’à arriver au dernier élément de la liste. 

## 2.4. Tri à bulles

L’{glo}`algo|algorithme` du **<span style="color:rgb(89, 51, 209)">tri à bulles</span>** compare les éléments voisins, deux par deux. Il commence par comparer les deux premiers éléments de la liste et les met dans le bon ordre (le plus petit des deux éléments précède le plus grand des deux). Il compare ensuite les deux éléments suivants (le nouveau deuxième et le troisième élément de la liste) et les met dans le bon ordre. Il continue de la sorte jusqu’à la fin de la liste. Après ce premier parcours de la liste, le plus grand élément se retrouve en dernière position de la liste. L'algorithme parcourt à nouveau la liste, en comparant et en déplaçant les éléments voisins deux par deux (en excluant également le dernier élément qui est déjà bien trié). Après le deuxième parcours de la liste, le deuxième plus grand élément se retrouve en avant-dernière position de la liste. L'algorithme parcourt la liste de la sorte, autant de fois qu’elle possède d’éléments, en excluant les éléments bien triés en fin de la liste.


````{admonition} Exercice 2.1. Algorithme de tri 
:class: note

Il est fortement recommandé de résoudre cet exercice avant d’avancer dans le chapitre. 

Appliquer au moins un des trois algorithmes ci-dessus (tri par insertion, tri par sélection et tri à bulles) pour trier les rectangles de la ligne du haut de la <a href="#fig-trier">Figure **Problème du tri**</a> en fonction de leur taille (le résultat est illustré dans la ligne du bas). 

Noter l’ordre des éléments à chaque fois qu’il change. Vous aurez besoin d’une grande feuille de papier. Vous pouvez aussi représenter la taille des rectangles par un nombre, cela permet de gagner de la place. Si cela vous aide, vous pouvez découper les rectangles ci-dessous et les manipuler. 

<img src="media/Tris_decoupe.png" width="60%"> &nbsp;  

````

````{admonition} Solution 2.1. Algorithme de tri
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

La solution est donnée dans la suite du chapitre et est illustrée dans la Figure **Algorithmes de tri** ci-dessous.

```
````

````{admonition} Anecdote
:class: hint

Vous passez trop de temps à chercher vos affaires ? Pensez à mieux les trier. Le temps perdu à ranger vos affaires sera bien inférieur à celui que vous passerez à les chercher plus tard.

````


La figure ci-dessous détaille les étapes intermédiaires des trois {glo}`algo|algorithmes` de tri vus précédemment. Dans le **<span style="color:rgb(89, 51, 209)">tri par insertion</span>** à gauche, on parcourt la liste dans l’ordre, un élément après l’autre (dénoté par une étoile). A chaque étape, on cherche à ***<span style="color:rgb(13, 204, 166)">insérer</span>*** le rectangle considéré à la bonne place dans la liste précédemment triée. La flèche rouge montre la position à laquelle le rectangle sera inséré après comparaison avec l'élément précédent. Si l’élément est déjà bien trié, aucune action n’est requise dans ce cas et la flèche est remplacée par un point rouge. Notez que la liste qui précède le rectangle considéré (celui avec l’étoile) est toujours bien triée. 


Dans le **<span style="color:rgb(89, 51, 209)">tri par sélection</span>** au milieu, on parcourt la liste pour ***<span style="color:rgb(13, 204, 166)">sélectionner</span>*** son plus petit élément, et on le met à la bonne position. La ligne noire au‑dessous des rectangles montre la liste parcourue pour rechercher le plus petit élément. Le plus petit élément de cette liste est désigné par l’étoile. Finalement, la flèche rouge montre les éléments échangés : le premier élément de la liste non triée et le plus petit élément. Ainsi, le plus petit élément sélectionné (avec étoile) se retrouve à la fin de la liste déjà triée (liste non soulignée). Si l’élément est déjà bien trié et qu’aucune action n’est requise, la flèche bidirectionnelle est remplacée par un point rouge.

Dans **<span style="color:rgb(89, 51, 209)">le tri à bulles</span>** à droite, les lignes en dessous des rectangles montrent les éléments voisins qui sont comparés à chaque étape. Lorsque cette ligne est grise, les éléments sont déjà bien ordonnés et aucune action n’est requise. Lorsque la ligne est noire, les éléments ne sont pas dans le bon ordre et doivent être intervertis (flèche rouge). Après un passage complet de la liste, l’élément le plus grand se retrouve en dernière position, il remonte comme une ***<span style="color:rgb(13, 204, 166)">bulle</span>*** (voir la 4e ligne). Le point rouge ici indique les éléments triés. Dans ce cas, la liste est triée après deux parcours complets de la liste.



Notez que même si tous les {glo}`algo|algorithmes` arrivent à la même solution finale, ils y arrivent de manière très différente et avec plus ou moins de calculs. 

<span id=fig-algos-tri></span>


```{figure} media/Tris_algorithmes.png
---
alt: Algorithmes de tri
width: 100%
align: left
---

**Algorithmes de tri**. Etapes intermédiaires lors de l’application des différents algorithmes de tri. La flèche rouge montre les mouvements des éléments suite à une opération. Si l’élément ne bouge pas, la flèche rouge est remplacée par un point rouge. **A gauche**, le tri par insertion. L’étoile dénote l’élément considéré à un moment donné. **Au milieu**, le tri par sélection. L’étoile désigne le plus petit élément de la liste non triée. **A droite**, le tri à bulles. Ici le point rouge signale les éléments triés.
```

<!-- ```{image} media/Tris_algorithmes.png
:width: 700
:height: 500
```
**Algorithmes de tri**. Etapes intermédiaires lors de l’application des différents algorithmes de tri. La flèche rouge montre les mouvements des éléments suite à une opération. Si l’élément ne bouge pas, la flèche rouge est remplacée par un point rouge. **A gauche**, le tri par insertion. L’étoile dénote l’élément considéré à un moment donné. **Au milieu**, le tri par sélection. L’étoile désigne le plus petit élément de la liste non triée. **A droite**, le tri à bulles. Ici le point rouge signale les éléments triés. -->




````{admonition} Exercice 2.2. Votre algorithme de tri
:class: note

Rappelez-vous quelle méthode vous avez utilisée pour résoudre l’exercice 0. De quel algorithme de tri se rapproche-t-elle le plus ? 
````

````{admonition} Solution 2.2. Votre algorithme de tri
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Cela dépend de votre solution de l’exercice 0. Vous avez probablement utilisé la méthode du tri par sélection ou du tri à bulles.
```
````

````{admonition} Exercice 2.3. Opérations 
:class: note

Pour chaque algorithme de tri, compter le nombre de ***<span style="color:rgb(13, 204, 166)">comparaisons</span>*** de la taille de deux rectangles, ainsi que le nombre de ***<span style="color:rgb(13, 204, 166)">déplacements</span>*** (le nombre de fois que deux rectangles échangent leur place).

Imaginons que ce qui prend le plus de temps est une ***comparaison***. Dans ce cas précis, quel algorithme de tri parmi les trois algorithmes présentés est le plus lent ? 

Imaginons que ce qui prend le plus de temps est un ***déplacement***. Dans ce cas précis, quel algorithme de tri est le plus lent ? Quel algorithme est le plus rapide ?

````

````{admonition} Solution 2.3. Opérations
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Le décompte des opérations effectuées, en se référant à la <a href="#fig-algos-tri">Figure **Algorithmes de tri**</a> est comme suit :

**<span style="color:rgb(89, 51, 209)">Tri par insertion</span>** : 9 comparaisons deux par deux (flèches et points rouges) et 5 déplacements deux par deux (flèches rouges). Notez que pour insérer un élément en première position, il faut tout d'abord l'échanger avec l'élément juste devant, puis avec l'élément avant, et ainsi de suite jusqu'à arriver à la première position.

**<span style="color:rgb(89, 51, 209)">Tri par sélection</span>** : 15 comparaisons deux par deux (lignes en dessous) et 3 déplacements deux par deux (flèches rouges).

**<span style="color:rgb(89, 51, 209)">Tri à bulles</span>** : 9 comparaisons deux par deux (lignes en dessous) et 5 déplacements deux par deux (flèches rouges). 

Si ce qui prend beaucoup de temps est la comparaison de la taille de deux rectangles, il ne faudrait pas utiliser le tri par sélection, car il comporte le plus grand nombre de comparaisons et il serait le plus lent. Si c’est le déplacement de deux rectangles qui coûte beaucoup de temps, cette fois-ci le tri par sélection serait le plus rapide (avec 3 rectangles qui échangent leur position). Donc, selon l'implémentation sur la machine, le tri par sélection serait le plus lent ou le plus rapide des trois algorithmes.

Ces résultats sont valables pour cette configuration en particulier. Si on trie un autre tableau, la performance des trois algorithmes pourrait changer. Le choix du meilleur algorithme dépend donc de l’implémentation et de la situation initiale. Notez finalement qu’il existe des algorithmes de tri bien plus rapides que les trois algorithmes considérés ici.
```

````


````{admonition} Le saviez-vous ? Tri stupide
:class: hint

Il existe un algorithme, **Tri de Bogo** (ou *Bogosort*), aussi nommé le *tri lent* ou encore le *tri stupide*. C’est un tri qui génère différentes permutations des éléments de la liste et s’arrête lorsque la configuration obtenue par hasard est triée. A votre avis, combien d’opérations prend cet algorithme en moyenne ?

````


## 2.5. Comparaison d’algorithmes

Toutes les recettes de cuisine ne se valent pas, de la même manière, un {glo}`algo|algorithme` peut aussi être ***<span style="color:rgb(13, 204, 166)">plus approprié</span>*** qu’un autre algorithme pour résoudre le même problème. Il existe des dizaines d’{glo}`algo|algorithmes` qui trient avec des approches différentes (nous en verrons encore quelques-uns). Certains algorithmes sont plus rapides, d’autres plus économes en mémoire ou encore plus simples à coder. Ainsi, selon la situation, il faut choisir le « bon » {glo}`algo|algorithme`.

La qualité d’un {glo}`algo|algorithme` dépend de la propriété que l’on souhaite optimiser (maximiser ou minimiser). Cela pourrait être de maximiser la **<span style="color:rgb(89, 51, 209)">vitesse d’exécution</span>** (mesurée par le nombre d’{glo}`instruction|instructions` élémentaires exécutées), de minimiser la place occupée en **<span style="color:rgb(89, 51, 209)">mémoire</span>**, de minimiser la **<span style="color:rgb(89, 51, 209)">consommation d'énergie</span>** ou de maximiser la **<span style="color:rgb(89, 51, 209)">précision de la solution</span>**. L'{glo}`algo|algorithme` utilisé devrait être choisi en fonction de ce qui est important.

***<span style="color:rgb(13, 204, 166)">La vitesse d’un {glo}`algo|algorithme` dépend également des {glo}`data|données` en {glo}`input|entrée`</span>***. Selon la configuration initiale des {glo}`data|données` en {glo}`input|entrée` (correspond à la ligne du haut de la <a href="#fig-algos-tri">Figure **Algorithmes de tri**</a>), un {glo}`algo|algorithme` « rapide » peut devenir « lent » et *vice versa*. Il faut savoir que les {glo}`algo|algorithmes` vus jusqu’ici sont tous des {glo}`algo|algorithmes` lents (nous verrons un {glo}`algo|algorithme` de tri rapide ultérieurement).

````{admonition} Le saviez-vous ? Tri trop lent
:class: hint

Pour trier 1 million d’éléments, selon l’algorithme choisi, cela peut prendre de 20 millions à 1 billion d’opérations. Si chaque opération prenait 1 microseconde (10<sup>-6</sup> s) à s’exécuter, il faudrait 20 secondes pour trier 1 million d’éléments si l'algorithme est efficace. Par contre, pour un des algorithmes ci-dessus, cela pourrait prendre 11 jours !  

````


````{admonition} Pour aller plus loin
:class: note

Imaginer que les quatre éléments d’une liste sont triés dans le sens inverse de ce que l’on souhaite (ils sont placés du plus grand au plus petit). Trier la liste selon les trois algorithmes de tri vus précédemment : le tri par insertion, le tri par sélection et le tri à bulles. 

Dans cette configuration précise, quel algorithme est le plus rapide  (présente le moins d’étapes intermédiaires) ? Quel algorithme est le plus lent ?


````



## 2.6. Exercices



````{admonition} Exercice 2.6.1. L'algorithme de votre journée
:class: note

Réfléchir à votre journée : y a-t-il des actions qui se retrouvent chaque jour ouvrable ? Arrivez-vous à esquisser un algorithme que vous suivez sans que vous en ayez conscience ?

````

````{admonition} Exercice 2.6.2. Trois algorithmes de tri
:class: note


Trier la liste [2, 5, 3, 4, 7, 1, 6] en utilisant les trois algorithmes de tri vus dans le cours. Représenter l’état de la liste après chaque étape.

````

<!-- 
`````{admonition} Solution 4. L'algorithme de votre journée
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Cela pourrait ressembler à ça :

```
Se lever
Répéter pour i = 1 à 3
    Faire des étirements
Fin Pour
Prendre une douche
Prendre un petit-déjener
Se brosser les dents
Aller au Gymnase
Répéter pour i = 1 à 5
    Suivre un cours
Fin Pour
Déjeuner
Répéter pour i = 1 à 5
    Suivre un cours
Fin Pour
Rentrer à la maison
Dîner
Lire un livre
Se brosser les dents
Se coucher
```
````
````` -->





<!-- 
`````{admonition} Solution 5. Trois algorithmes de tri
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Voici le détail de toutes les étapes intermédiaires des trois algorithmes de tri.

**<span style="color:rgb(89, 51, 209)">Tri par insertion</span>** : 

```
[2,5,3,4,7,1,6]  # on considère le 2e élément et on l'ordonne par rapport au premier élément
[2,5,3,4,7,1,6]  # on considère le 3e élément et on l'ordonne par rapport aux deux premiers éléments
[2,3,5,4,7,1,6]  # on considère le 4e élément et on l'insère au bon endroit du tableau déjà trié
[2,3,4,5,7,1,6]  # on considère le 5e élément et on l'insère au bon endroit du tableau déjà trié
[2,3,4,5,7,1,6]  # on considère le 6e élément et on l'insère au bon endroit du tableau déjà trié
[1,2,3,4,5,7,6]  # on considère le 7e élément et on l'insère au bon endroit du tableau déjà trié
[1,2,3,4,5,6,7]
```
**<span style="color:rgb(89, 51, 209)">Tri par sélection</span>** : 

```
[2,5,3,4,7,1,6]  # on sélectionne le plus petit élément et on l'échange avec le premier élément
[1,5,3,4,7,2,6]  # on sélectionne le 2e plus petit élément et on l'échange avec le 2e élément 
[1,2,3,4,7,5,6]  # on sélectionne le 3e plus petit élément et on l'échange avec le 3e élément 
[1,2,3,4,7,5,6]  # on sélectionne le 4e plus petit élément et on l'échange avec le 4e élément 
[1,2,3,4,5,7,6]  # on sélectionne le 5e plus petit élément et on l'échange avec le 5e élément 
[1,2,3,4,5,6,7]  # on sélectionne le 6e plus petit élément et on l'échange avec le 6e élément 
```

**<span style="color:rgb(89, 51, 209)">Tri à bulles</span>** : 

```
[2,5,3,4,7,1,6]  # on compare 2 et 5 et
[2,5,3,4,7,1,6]  # on compare 5 et 3 et on les déplace
[2,3,5,4,7,1,6]  # on compare 5 et 4 et on les déplace
[2,3,4,5,7,1,6]  # on compare 5 et 7
[2,3,4,5,7,1,6]  # on compare 7 et 1 et on les déplace
[2,3,4,5,1,7,6]  # on compare 7 et 6 et on les déplace, tableau trié [7]
[2,3,4,5,1,6,7]  # on compare 2 et 3
[2,3,4,5,1,6,7]  # on compare 3 et 4
[2,3,4,5,1,6,7]  # on compare 4 et 5
[2,3,4,1,5,6,7]  # on compare 5 et 1 et on les déplace
[2,3,4,1,5,6,7]  # on compare 5 et 6, tableau trié [6, 7]
[2,3,4,1,5,6,7]  # on compare 2 et 3
[2,3,4,1,5,6,7]  # on compare 3 et 4
[2,3,1,4,5,6,7]  # on compare 4 et 1 et on les déplace
[2,3,1,4,5,6,7]  # on compare 4 et 5, tableau trié [5, 6, 7]
[2,3,1,4,5,6,7]  # on compare 2 et 3 
[2,1,3,4,5,6,7]  # on compare 3 et 1 et on les déplace
[2,1,3,4,5,6,7]  # on compare 3 et 4, tableau trié [4, 5, 6, 7]
[1,2,3,4,5,6,7]  # on compare 2 et 1 et on les déplace
[1,2,3,4,5,6,7]  # on compare 2 et 3, tableau trié [3, 4, 5, 6, 7]
[1,2,3,4,5,6,7]  # on compare 1 et 2, tableau trié [2, 3, 4, 5, 6, 7]
```
````

`````
 -->



````{admonition} Exercice 2.6.3. Vérificateur de tri
:class: note

Ecrire un algorithme qui vérifie si une liste est triée. 

Que prend l’algorithme en entrée et que retourne-t-il en sortie ?

Demander ensuite à un autre élève de suivre les opérations décrites par votre algorithme. Est-ce que votre algorithme est correct ?

Comparer vos algorithmes. Sont-ils différents ?

````

<!-- 

`````{admonition} Exercice 6 : vérificateur de tri
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Voici un algorithme possible. 

```
Liste Nombres           # la variable Nombres contient une liste de nombres
i = 2                   # la variable i permet de parcourir Nombres

Répéter Pour i = 2 à Longueur(Nombres)
    Si Nombres[i-1] > Nombres[i]  # l'élément précédent est plus grand
        Retourner Faux
    Fin Si
Fin Pour
Retourner Vrai
```

L'algorithme compare les éléments deux par deux et retourne `Faux` (et se termine) si l'élément d'après est plus petit que l'élément d'avant. Si tous les éléments parcourus sont dans le bon ordre, l'algorithme arrive à la dernière ligne et retourne `Vrai`. 

L'algorithme prend une liste (triée ou non triée) en entrée et retourne `Vrai` ou `Faux` en sortie, selon si la liste est triée. L'algorithme pourrait retourner aussi `Oui` et `Non`, mais *par convention* on préfère les valeurs logiques Vrai et Faux, car ces dernières peuvent être utilisées par la suite dans une condition. Par exemple, si l'algorithme retourne Faux, on pourrait demander à un autre algorithme de trier la liste. `Vrai` et `Faux` correspondent également à 0 et 1, ce qui permet de les utiliser pour faire des calculs. 

````
````` 
-->


````{admonition} Exercice 2.6.4. Mondrian
:class: note

Analyser les œuvres cubistes de Piet Mondrian. Trouver un algorithme qui permet de créer une œuvre qui pourrait être attribuée à Mondrian.

````

<!-- 

`````{admonition} Exercice 7 : Mondrian
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Voici un algorithme possible. 

```
Répéter Pour i = 1 à 3 
    Séparer espace avec une ligne verticale noire
Fin Pour
Répéter Pour i = 1 à 3 
    [1 fois sur 2] Aller jusque la première ligne verticale 
    Séparer espace avec une ligne horizontale noire
    [1 fois sur 2] arrêter avant la dernière ligne verticale
Fin Pour

Répéter Pour couleur_choisie dans ([Rouge, Bleu, Jaune] ou [Rouge, Bleu, Jaune, Noir])
    Répéter Pour i = 1 à Nombre allant de 1 à 4
        Choisir un grand carré 
        Répéter Tant que carré à côté est égale à couleur_choisie  
            Choisir un autre carré
        Fin Tant que
        Colorier le carré en couleur_choisie
Fin Pour

```

Cet algorithme est approximatif. Il pourrait être amélioré pour colorier en priorité les grands carrés en rouge et en bleu. Il pourrait aussi donner plus d'indications, sur comment séparer l'espace en précisant les proportions souhaitées.

Si vous avez un niveau de programmation avancé, vous pouvez essayer de coder cet algorithme.
````
`````
 -->


````{admonition} Ai-je compris ?
:class: attention

1. Je sais qu’il existe plusieurs manières différentes de résoudre un problème.

2. Je sais qu’il faut choisir le meilleur algorithme en fonction de critères objectifs : vitesse de l’algorithme, qualité de la solution,  espace utilisé en mémoire ou encore consommation d’énergie.

3. Je sais appliquer les trois algorithmes de tri vus dans le cours.

````











