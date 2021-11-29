
````{admonition} Matière à réfléchir
:class: attention

Imaginez une bibliothèque scolaire un peu spéciale : les livres n’y sont pas rangés par ordre alphabétique ! Ils sont bien rangés sur des étagères, mais sans aucune logique particulière. Vous entrez dans cette bibliothèque un peu spéciale et vous vous mettez à chercher l’ouvrage ***<span style="color:rgb(13, 204, 166)">Le Guide du voyageur galactique.</span>***

Pensez-vous pouvoir retrouver ce livre ?

Combien de temps cela vous prendra-t-il ? 

Y a-t-il des objets chez vous, que vous rangez dans un ordre bien particulier ?

Y a-t-il des objets chez vous, que vous feriez mieux de ranger dans un ordre bien particulier, parce que vous passez beaucoup de temps à les chercher ?

````

# 2. Trie, cherche et trouve

Pour l'instant il faut nous croire sur parole, mais si on veut pouvoir trouver une information parmi une avalanche d'informations, il faut que ces informations soient bien rangées. L'exemple de la bibliothèque ci-dessus illustre ce besoin de manière intuitive, mais vous aller pouvoir l'expérimenter de première main dans le chapitre Algorithmique II. 

Saviez-vous que le succès fulgurant de *Google* est surtout dû à sa capacité à bien ranger l'information disponible sur le Web ? Au moment où vous avez besoin d'une information particulière, leurs algorithmes sont capables de la retrouver parce qu'elle est bien rangée. Ce problème qui consiste à ranger les données a un nom, il s'agit du **<span style="color:rgb(89, 51, 209)">problème du Tri</span>**. Il est si important qu'il est un des problèmes les plus étudiés en algorithmique.

## Algorithmes de tri

<span id=fig-trier></span>

Un **<span style="color:rgb(89, 51, 209)">algorithme de tri</span>** est un algorithme qui permet de résoudre le problème du tri des données, donc d'organiser les données selon ***<span style="color:rgb(13, 204, 166)">une relation d’ordre</span>***. Dans la figure ci-dessous, les objets sont organisés soit par la luminosité de leur couleur (ligne du haut), soit par leur taille (lignes du bas), dans **un ordre croissant**.

```{figure} media/Tris_base.png
---
alt: Problème du tri.
width: 50%
---

**Problème du tri.** Des objets peuvent être triés selon une relation d’ordre, en lien avec une propriété. Sur la ligne du haut, les rectangles sont organisés selon leur couleur (de la plus sombre à la plus claire), alors que sur la ligne du bas, ils sont triés selon leur taille (du plus petit au plus grand).

```


<!-- Pour apprendre à cuisiner, on commence par suivre des recettes classiques. -->
<!-- Pour apprendre à cuisiner, on commence par suivre des recettes classiques. Ainsi, pour appréhender l’{glo}`algorithmique|algorithmique`, nous étudierons une classe d’{glo}`algo|algorithmes` classiques : les **<span style="color:rgb(89, 51, 209)">algorithmes de tri</span>**.  -->




````{admonition} Exercice 0. Tri de rectangles
:class: note

Trier les rectangles de la ligne du haut de la <a href="#fig-trier">Figure ci-dessus</a> en fonction de leur taille, pour arriver à la disposition de la ligne du bas. Noter toutes les étapes intermédiaires de vos actions et la disposition des rectangles avant d’arriver à la solution finale. Conseil : remplacer les rectangles par un nombre qui représente leur taille.

En lien avec les ingrédients d’un algorithme, déterminer les données en entrée et le résultat en sortie de l’algorithme.

Quels types d'opérations avez-vous effectuées ? 

````

````{admonition} Solution 0. Tri de rectangles
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Si on remplace les rectangles de la ligne du haut par un nombre qui représente leur taille, on obtient la liste [3, 4, 1, 2, 6, 5]. Le plus important est que l'ordre des nombres conserve l'ordre de la taille des rectangles. Après le tri, si l'algorithme est correct, vous devriez vous retrouver avec la liste [1, 2, 3, 4, 5, 6]. Les opérations et les dispositions intermédiaires exactes dépendent de l'algorithme que vous avez utilisé. 

Les données en entrée sont les rectangles sur la ligne du haut : leur taille et l'ordre de leur taille, ici [3, 4, 1, 2, 6, 5]. Le résultat en sortie correspond aux rectangles sur la ligne du bas : l'ordre croissant de leur taille, ici [1, 2, 3, 4, 5, 6]. 

Les types d'opérations que vous avez effectuées sont des comparaisons de la taille de deux rectangles et des déplacements de rectangles.

```
````

<br>

Nous allons exposer ici trois algorithmes de tri simple, que l'on pourrait utiliser pour trier des objets dans la vie de tous les jours.

## Tri par insertion

L’{glo}`algo|algorithme` du **<span style="color:rgb(89, 51, 209)">tri par insertion</span>** parcourt la liste d’éléments à trier du deuxième au dernier élément. Pour chaque nouvel élément considéré, il l'insère à l'emplacement correct dans la liste déjà parcourue. A tout moment, la liste d'éléments déjà parcourus (jusqu’à l’élément que l'on considère à un moment donné) est toujours bien triée.

## Tri par sélection

L’{glo}`algo|algorithme` du **<span style="color:rgb(89, 51, 209)">tri par sélection</span>** commence par rechercher le plus petit élément de la liste et l’échange avec le premier élément de la liste. Il recherche ensuite le plus petit élément de la liste restante (sans le premier plus petit élément). Il sélectionne ainsi le deuxième plus petit élément de la liste et l’échange avec le deuxième élément de la liste. Et ainsi de suite : il recherche le plus petit élément de la liste restante, en excluant les éléments déjà triés, et échange ce plus petit élément avec le premier élément pas encore trié. Il continue de la sorte jusqu’à arriver au dernier élément de la liste. 

## Tri à bulles

L’{glo}`algo|algorithme` du **<span style="color:rgb(89, 51, 209)">tri à bulles</span>** compare les éléments voisins, deux par deux. Il commence par comparer les deux premiers éléments de la liste et les met dans le bon ordre (le plus petit des deux éléments précède le plus grand des deux). Il compare ensuite les deux éléments suivants (le nouveau deuxième et le troisième élément de la liste) et les met dans le bon ordre. Il continue de la sorte jusqu’à la fin de la liste. Après ce premier parcours de la liste, le plus grand élément se retrouve en dernière position de la liste. L'algorithme parcourt à nouveau la liste, en comparant et en déplaçant les éléments voisins deux par deux (en excluant également le dernier élément qui est déjà bien trié). Après le deuxième parcours de la liste, le deuxième plus grand élément se retrouve en avant-dernière position de la liste. L'algorithme parcourt la liste de la sorte, autant de fois qu’elle possède d’éléments, en excluant les éléments bien triés en fin de la liste.


````{admonition} Exercice 1. Algorithme de tri
:class: note

Il est fortement recommandé de résoudre cet exercice avant d’avancer dans le chapitre. 

Appliquer au moins un des trois algorithmes ci-dessus (tri par insertion, tri par sélection et tri à bulles) pour trier les rectangles de la ligne du haut de la <a href="#fig-trier">Figure **Problème du tri**</a> en fonction de leur taille (le résultat est illustré dans la ligne du bas). Noter l’ordre des éléments à chaque fois qu’il change. Vous aurez besoin d’une grande feuille de papier. Vous pouvez aussi représenter la taille des rectangles par un nombre, cela permet de gagner de la place. 

````

````{admonition} Solution 1. Algorithme de tri
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


La figure ci-dessous détaille les étapes intermédiaires des trois {glo}`algo|algorithmes` de tri vus précédemment. Dans le **<span style="color:rgb(89, 51, 209)">tri par insertion</span>** à gauche, on parcourt la liste dans l’ordre, un élément après l’autre (dénoté par une étoile). A chaque étape, on cherche à ***<span style="color:rgb(13, 204, 166)">insérer</span>*** le rectangle considéré à la bonne place dans la liste précédemment triée. La flèche rouge montre la position à laquelle le rectangle sera inséré. Si l’élément est déjà bien trié, aucune action n’est requise dans ce cas et la flèche est remplacée par un point rouge. Notez que la liste qui précède le rectangle considéré (celui avec l’étoile) est toujours bien triée. 








Dans le **<span style="color:rgb(89, 51, 209)">tri par sélection</span>** au milieu, on parcourt la liste pour ***<span style="color:rgb(13, 204, 166)">sélectionner</span>*** son plus petit élément, et on le met à la bonne position. La ligne noire au‑dessous des rectangles montre la liste parcourue pour rechercher le plus petit élément. Le plus petit élément de cette liste est désigné par l’étoile. Finalement, la flèche rouge montre les éléments échangés : le premier élément de la liste non triée et le plus petit élément. Ainsi, le plus petit élément sélectionné (avec étoile) se retrouve à la fin de la liste déjà triée (liste non soulignée). Si l’élément est déjà bien trié et qu’aucune action n’est requise, la flèche bidirectionnelle est remplacée par un point rouge.

Dans **<span style="color:rgb(89, 51, 209)">le tri à bulles</span>** à droite, les lignes en dessous des rectangles montrent les éléments voisins qui sont comparés à chaque étape. Lorsque cette ligne est grise, les éléments sont déjà bien ordonnés et aucune action n’est requise. Lorsque la ligne est noire, les éléments ne sont pas dans le bon ordre et doivent être intervertis (flèche rouge). Après un passage complet de la liste, l’élément le plus grand se retrouve en dernière position, il remonte comme une ***<span style="color:rgb(13, 204, 166)">bulle</span>*** (voir la 4e ligne). Le point rouge ici indique les éléments triés. Dans ce cas, la liste est triée après deux parcours complets de la liste.



Notez que même si tous les {glo}`algo|algorithmes` arrivent à la même solution finale, ils y arrivent de manière très différente et avec plus ou moins de calculs. 

<span id=fig-algos-tri></span>



```{figure} media/Tris_algorithmes.png
---
alt: Algorithmes de tri
width: 100%
---

**Algorithmes de tri**. Etapes intermédiaires lors de l’application des différents algorithmes de tri. La flèche rouge montre les mouvements des éléments suite à une opération. Si l’élément ne bouge pas, la flèche rouge est remplacée par un point rouge. **A gauche**, le tri par insertion. L’étoile dénote l’élément considéré à un moment donné. **Au milieu**, le tri par sélection. L’étoile désigne le plus petit élément de la liste non triée. **A droite**, le tri à bulles. Ici le point rouge signale les éléments triés.




````{admonition} Exercice - application 2 : tri ✏️📒
:class: note

Rappelez-vous la méthode que vous avez utilisée pour résoudre l’exercice 8. De quel algorithme de tri se rapproche-t-elle le plus ? 

````

````{admonition} Solution
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

La solution dépend de votre solution de l’exercice 8. 

```

````

````{admonition} Exercice - application 3 : comparaison et mouvements ✏️📒
:class: note

Pour chaque algorithme, comptez le nombre de comparaisons de la taille de deux éléments et le nombre de mouvements (rectangles déplacés).

Imaginons que ce qui prend le plus de temps est la comparaison. Dans ce cas précis, lequel des trois algorithmes faudrait-il utiliser ? 

Imaginons que ce qui prend le plus de temps est le mouvement d’un élément. Dans ce cas précis, lequel des trois algorithmes serait le plus rapide ? Quel serait l’algorithme le plus lent ?

````

````{admonition} Solution
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Le décompte des opérations effectuées est comme suit :

Tri par insertion : 9 comparaisons (flèches rouges) et 8 changements de position (flèches rouges).

Tri par sélection : 15 comparaisons (lignes en dessous) et 6 changementes de position (flèches rouges). 

Tri à bulles : 9 comparaisons (lignes en dessous) et 10 changements de position (flèches rouges). 

Si c’est le changement de position d’un élément qui coûte beaucoup de temps, l’algorithme le plus rapide serait le tri par sélection (3 éléments intervertis ou 6 éléments changés de place). Le tri à bulles serait le plus lent avec 10 changements de position. 

Il faut savoir que ces résultats sont valides pour cette configuration en particulier ; si on triait un autre tableau, la comparaison de la performance de chacun de ces algorithmes pourrait changer.  Pour ces trois algorithmes, le choix du meilleur algorithme dépend donc de l’implémentation et de la situation initiale. Notez finalement qu’il existe des algorithmes de tri bien plus rapides que les trois algorithmes considérés ici.
```

````


````{admonition} Le saviez-vous ?
:class: hint

Il existe un algorithme, Bogosort, aussi nommé le tri lent ou encore le tri stupide. C’est un tri qui génère différentes permutations des éléments de la liste et s’arrête lorsque la configuration obtenue est par hasard triée. Combien d’opérations prend cet algorithme en moyenne ?

````


## Comparaison d’algorithmes

Toutes les recettes de cuisine ne se valent pas, de la même manière, un {glo}`algo|algorithme` peut aussi être ***<span style="color:rgb(13, 204, 166)">plus approprié</span>*** qu’un autre algorithme pour résoudre le même problème. Il existe des dizaines d’{glo}`algo|algorithmes` qui trient avec des approches différentes (nous en verrons quelques-uns). Certains algorithmes sont plus rapides, d’autres plus économes en mémoire ou encore plus simples à coder. Ainsi, selon la situation, il faut choisir le « bon » {glo}`algo|algorithme`.

La qualité d’un {glo}`algo|algorithme` dépend de l’aspect que l’on souhaite optimiser (ou minimiser). Cela peut être la vitesse d’exécution (mesurée par le nombre d’{glo}`instruction|instructions` élémentaires exécutées), la place occupée en mémoire, ou encore le coût de certaines opérations comme le déplacement d’un élément. L'{glo}`algo|algorithme` utilisé devrait être choisi en fonction de la situation.

La vitesse d’un {glo}`algo|algorithme` dépend également des {glo}`data|données` en {glo}`input|entrée`. Selon la situation initiale des {glo}`data|données` en {glo}`input|entrée` (correspond à la ligne du haut de la <a href="#fig-algos-tri">Figure **Algorithmes de tri**</a>), un {glo}`algo|algorithme` « rapide » peut devenir « lent ». Il faut savoir que les {glo}`algo|algorithmes` vus jusqu’ici sont des {glo}`algo|algorithmes` lents, nous verrons un {glo}`algo|algorithme` de tri rapide ultérieurement.

````{admonition} Le saviez-vous ?
:class: hint

Pour trier 1 million d’éléments, cela peut prendre 20 millions à 1 milliard d’opérations, selon l’algorithme choisi. Si chaque opération prenait 1 microseconde (10<sup>-6</sup> s) à s’exécuter, il faudrait 20 secondes pour trier 1 million d’éléments si l'algorithme est efficace. Par contre, pour un des algorithmes ci-dessus, il faudrait prévoir 11 jours !  

````


````{admonition} Aller plus loin
:class: note

Imaginer que les quatre éléments d’une liste sont triés dans le sens inverse de ce que l’on souhaite (ils sont placés du plus grand au plus petit). Trier la liste selon les trois algorithmes de tri vus précédemment : le tri par insertion, le tri par sélection et le tri à bulles. 

Dans cette configuration précise, quel algorithme est le plus rapide  (présente le moins d’étapes intermédiaires) ? Quel algorithme est le plus lent ?


````






````{admonition} Exercice 1. L'algorithme de votre journée
:class: note

Réfléchir à votre journée : y a-t-il des actions qui se retrouvent chaque jour ouvrable ? Arrivez-vous à esquisser un algorithme que vous suivez sans que vous en ayez conscience ?

````

````{admonition} Exercice 2. Trois algorithmes de tri
:class: note


Trier la liste [2,5,3,4,7,1,6] en utilisant les trois algorithmes de tri vus adans le cours. Représenter l’état de la liste après chaque étape qui change l’ordre des éléments.

````

````{admonition} Exercice 3. Vérificateur de tri
:class: note

Ecrire un algorithme qui vérifie si une liste est triée. 

Que prend l’algorithme en entrée et qu’est-ce qu’il retourne en sortie ?

Demander ensuite à un autre élève de suivre les opérations décrites par votre algorithme. Est-ce que votre algorithme est correct ?

Comparer vos algorithmes. Sont-ils différents ?

````

````{admonition} Exercice 4. Mondrian
:class: note

Analyser les œuvres cubistes de Piet Mondrian. Trouver un algorithme qui permet de créer une œuvre qui pourrait être attribuée à Mondrian.

````

````{admonition} Ai-je compris ?
:class: attention

1. Je sais qu’il existe plusieurs manières différentes de résoudre un problème.

2. Je sais qu’il faut choisir le meilleur algorithme en fonction de critères objectifs : vitesse de l’algorithme, qualité de la solution,  espace utilisé en mémoire ou encore consommation d’énergie.

3. Je sais appliquer les trois algorithmes de tri vus dans le cours.

````











