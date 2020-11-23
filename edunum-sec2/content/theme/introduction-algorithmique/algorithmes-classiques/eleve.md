Algorithmes classiques
======================

::::{admonition,note} Matière à réfléchir I

Imaginez une bibliothèque scolaire un peu spéciale : les livres n’y sont pas rangés. Ils sont bien posés sur des rayons, mais sans aucune logique particulière. Vous entrez dans cette bibliothèque un peu spéciale et vous recherchez ***Le Guide du voyageur galactique***. 

Est-il possible de retrouver ce livre ? 

Si oui, en combien de temps ? 

Quelles sont les choses que vous rangez chez vous ?

::::

## Algorithmes de tris

Pour apprendre à cuisiner, on commence par suivre des recettes éprouvées, on ne s’improvise pas chef de cuisine moléculaire. Ainsi, pour introduire l’algorithmique, nous nous appuierons sur une classe d’algorithmes classiques : les **algorithmes de tri**. 

:::{figure} 

<img src="Tris_base.png" width="40%">

Des objets peuvent être triés ou organisés selon une relation d’ordre en lien avec une de leurs propriétés. Sur la ligne du haut, les rectangles sont placés selon leur couleur, de la plus sombre à la plus lumineuse. Sur la ligne du bas, les rectangles sont triés selon leur taille, du plus petit au plus grand. 

:::

Un algorithme de tri permet de trier ou plus précisément d’organiser une liste d’objets selon une **relation d’ordre** déterminée. Dans la figure ci-dessus, les objets sont organisés soit par la luminosité croissante de leur couleur, soit  par leur taille croissante.

Toutes les recettes de cuisine ne se valent pas, de même en algorithmique, selon le problème précis sous la main, un algorithme est ***plus adéquat qu’un autre***. Il existe des dizaines d’algorithmes qui trient de manière différente, nous en verrons quelques-uns juste après. Certains sont plus rapides, d’autres utilisent moins de mémoire ou bien sont plus simples à comprendre. Ainsi, selon la situation, il faut choisir le bon algorithme à utiliser.  

::::{admonition,hint} Le saviez-vous ? II

Pour trier un million d’objets, selon l’algorithme choisi cela peut prendre de l’ordre de 20 millions à 1 billion d’opérations. Si chaque opération prend 1 microseconde (10^<sup>-6</sup> s), cela pourrait prendre de 20 secondes à 11 jours. 

::::

::::{admonition,attention} Exercice 3

Trier les rectangles de la ligne du haut de la Figure 2 en fonction de leur taille. Dessiner toutes les étapes intermédiaires avant d’arriver à la solution finale.

Quelles opérations avez-vous effectuées ? En lien avec les ingrédients d’un algorithme, déterminer les données en entrée et le résultat en sortie de l’algorithme.

::::

### Tri par insertion

Parcourir la liste d’éléments à trier (par exemple, les rectangles de la Figure 2). Pour chaque nouvel élément, l’insérer au bon emplacement de la liste déjà parcourue. La liste déjà parcourue est ainsi triée à tout moment.

### Tri par sélection

Rechercher le plus petit élément de la liste et l’échanger avec le premier élément de la liste. Rechercher ensuite le plus petit élément de la liste en excluant le premier élément, et l’échanger avec le deuxième élément de la liste. Rechercher ensuite le plus petit élément de la liste restante, en excluant le premier et deuxième élément, et l’échanger avec le troisième élément. Continuer de la sorte jusqu’à ce que toute la liste soit triée.

### Tri à bulles

Comparer les deux premiers éléments de la liste et les mettre dans le bon ordre (l’élément qui est plus petit précède celui qui est plus grand). Comparer ensuite le deuxième et le troisième élément de la liste et les mettre dans le bon ordre. Continuer de la sorte jusqu’à la fin de la liste. Après ce premier parcours de la liste, le plus grand élément se retrouve en dernière position de la liste. Parcourir à nouveau la liste, en excluant le dernier élément qui est bien trié. Parcourir ainsi la liste autant de fois qu’il y a d’éléments, en excluant les éléments bien triés en fin de liste.

::::{admonition,attention} Exercice 4

Appliquer les trois algorithmes ci-dessus à l’exemple de la Figure 2. Il faut partir de la ligne du haut pour trier les rectangles en fonction de leur taille et arriver au résultat de la ligne du bas. Dessiner toutes les étapes intermédiaires.

::::

:::{figure} 

<img src="Tris_algorithmes.png" width="80%">

Etapes intermédiaires lors de l’application des différents algorithmes de tri. **A gauche**, le tri par insertion. Pour chaque étape, l’étoile dénote le rectangle que l’on doit insérer dans la liste précédemment triée. La flèche rouge montre la position à laquelle le rectangle sera inséré. Le point rouge indique que l’élément est déjà bien trié et qu’aucune action n’est requise. Noter que la liste qui précède le rectangle avec étoile est toujours déjà triée. **Au milieu**, le tri par sélection. La ligne noire au-dessous des rectangles montre la liste qui sera parcourue à la recherche du plus petit élément. L’étoile désigne le plus petit élément de la liste considérée. Finalement, la flèche rouge montre quels éléments seront échangés, le plus petit élément se retrouve à la fin de la liste déjà triée (sans ligne en dessous). Le point rouge indique que l’élément est déjà bien trié et qu’aucune action n’est requise. **A droite**, les lignes en dessous des rectangles montrent les éléments qui sont comparés. Lorsque la ligne est grise, les éléments sont déjà bien ordonnés et aucune action n’est requise. Lorsque la ligne est noire, les éléments ne sont pas dans le bon ordre est doivent être inversés (flèche rouge). Après un passage complet de la liste, le dernier élément est l’élément le plus grand (4e ligne). Ainsi le point rouge indique lorsque l’élément est à la bonne position. La liste est triée après trois passages. 


:::

La figure ci-dessus détaille les étapes intermédiaires des algorithmes de tri présentés. Notez que même si tous les algorithmes arrivent à la même solution finale, ils y arrivent de manière très différente.

::::{admonition,attention} Exercice 5

Rappelez-vous la méthode que vous avez utilisée pour résoudre l’exercice III. A quel algorithme de tri correspond-elle le plus ? 

::::

::::{admonition,attention} Exercice 6

Imaginons que le changement de position d’un rectangle prenne beaucoup de temps, bien plus que la comparaison de la taille de 2 rectangles. Dans ce cas, lequel des trois algorithmes serait le plus rapide ? Quel serait l’algorithme le plus lent ?

Imaginons que la comparaison de la taille de 2 rectangles prenne beaucoup de temps, bien plus que le changement de position d’un rectangle. Dans ce cas, lequel des trois algorithmes serait le plus rapide ? Quel serait l’algorithme le plus lent ?

Imaginons que le meilleur algorithme est celui qui propose le plus de rectangles qui sont déjà à la bonne position (leur position finale une fois triés) toutes étapes confondues. Cela peut être le cas si l’on n'a pas le temps d’attendre que l’algorithme converge et on souhaite que les étapes intermédiaires nous donnent une réponse aussi proche de la solution que possible. Dans ce cas, lequel des trois algorithmes serait le plus rapide ? Quel serait l’algorithme le plus lent ?

::::

::::{admonition,note} Pour aller plus loin II

Imaginez que les objets sont triés dans le sens inverse de ce que l’on souhaite. Trier les objets selon les trois algorithmes de tri : tri par insertion, tri par sélection et tri à bulles. 

Intuitivement, quel algorithme est le plus rapide dans cette configuration précise ? Quel algorithme est le plus lent ?

::::

## Comparaison d’algorithmes

La qualité d’un algorithme dépend de l’aspect que l’on souhaite optimiser. Cela peut être la vitesse d’exécution (nombre d’étapes nécessaires), la place en mémoire, le coût de certaines opérations comme le changement de position d’un élément. L’algorithme utilisé devrait être choisi en fonction de la situation.

::::{admonition,attention} Exercices supplémentaires

**Exercice 1.** Ecrire un algorithme qui vérifie si une liste est triée.

**Exercice 2.** Pensez à votre journée. Y a-t-il des actions qui se retrouvent chaque jour ouvrable ? Arrivez-vous à esquisser un algorithme que vous suivez sans que vous en ayez conscience ?

**Exercice 3.** Quel est le résultat de la suite des trois affectations suivantes ? 
```
	X <— X + Y
	Y <— X – Y
	X <— X – Y
```

Vérifiez votre solution en mettant des valeurs aux variables. 

::::