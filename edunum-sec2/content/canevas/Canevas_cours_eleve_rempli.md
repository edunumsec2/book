# Introduction à l'algorithmique

# Une définition des algorithmes

## Pré-requis

Doit être vu après le chapitre sur la programmation.

## Objectifs pédagogiques

* Familiarisation avec la notion d’algorithme
* Transcription d'un algorithme dans un programme
* Résolution de problème par décomposition en étapes. 
* Compréhension des avantages et désavantages des algorithmes utilisés pour résoudre un problème. 
* Connaissances concernant les critères à prendre en considération pour choisir le meilleur algorithme.

## Accroche (historique, culturelle, technique, etc.)

> Le mot algorithme vient du nom d'un mathématicien perse du IXe siècle, Al-Khwârizmî (en arabe : الخوارزمي). 

Aujourd'hui, les algorithmes nous accompagnent au quotidien. Ce sont eux qui nous suggèrent des contenus à regarder sur nos applications préférées. Ce sont eux qui choisissent les pages qui s'afficheront lorsqu'on utilise un moteur de recherches. 

## Introduction

Un algorithme est en quelque sorte « une recette » que le système informatique suit pour résoudre un problème. Lorsqu'on conçoit une recette de cuisine, on commence par déterminer les grandes étapes, comme la préparation des ingrédients, la cuisson, le service... On décompose ensuite chacune de ces étapes en instructions qu’une personne peut suivre.

Prenons un cas précis : réaliser une omelette. Pour chacune des étapes il faut prévoit une marche à suivre suffisamment détaillée, afin que la personne qui suit la recette arrive au même résultat. Dans le cas de l’omelette, les instructions pourraient être :

1. Prendre des oeufs.
2. Casser et mélanger les œufs dans un bol.
3. Frire les œufs dans une poêle.
4. Glisser l’omelette dans une assiette.

< image : omelette >

L’objectif d’un algorithme est de résoudre un problème, concrètement l’algorithme va donner un résultat en sortie. Pour trouver ce résultat, l’algorithme va se baser sur des données qu’il reçoit en entrée. Par exemple, un algorithme qui détecte les visages va recevoir en entrée une image et donnera en sortie le résultat oui si l’image contient un visage et non si l’image ne contient pas de visages. Un algorithme qui traduit prend en entrée un texte dans une langue et un dictionnaire. C’est tout ce dont il a besoin pour rendre en sortie un texte dans une autre langue dont le sens correspond au premier texte.

Entre l’entrée et la sortie, l’algorithme précise quelles opérations exécuter. Les opérations que l’on peut attendre d’un humain sont très différentes de celle d’un ordinateur. On peut donner l’instruction à un humain de casser des oeufs, mais un ce n’est pas une instruction qu’un programme peut exécuter. Par contre on peut demander à un programme de stocker une valeur dans une variable, de comparer les valeurs de plusieurs variables, de parcourir des longues listes de données. Il le fera sans se plandre... Une opération cache une multitude d’instructions élémentaires. Lorsque l’ordinateur exécute l’opération comparer les valeurs de deux variables, il doit d’abord accéder chacune des variables là où elles sont stockées. Seulement après les avoir accédées, l’ordinateur peut les soustraire afin de déterminer quelle variable contient la plus grande valeur.

::::{admonition,note} Ordre des opérations

Notez que l’ordre des opérations est très important. Dans l’exemple de l’omelette, il est impossible de mélanger les œufs avant de les avoir cassés. L’ordinateur a non seulement besoin de recevoir les instructions dans le bon ordre, il a également besoin que tout lui soit précisé, et ce de manière non‑ambigüe. Il doit y avoir une seule lecture possible des opérations indiquées par un algorithme.

::::

Ainsi, les ingrédients d’un algorithme sont donc les suivants :

1. Des données en entrée
2. Des instructions élémentaires sous la forme d’opérations
3. Ordre d’exécution des opérations
4. Un résultat en sortie

## Exercices introductifs

### Exercice 1

A quoi correspondent les ingrédients d’un algorithme dans l’exemple de la recette de l’omelette ?

### Prolongements 1

**Le saviez-vous ?** 

Le jeu d’instructions élémentaires va dépendre du système informatique. Un algorithme spécifie des opérations à suivre dans un ordre donné. Ces opérations seront transcrites à travers un programme en instructions exécutables par la machine. La manière dont ces instructions éxecutables seront décomposées en instructions élementaires, puis exécutées, peut être très différente d’un système à l’autre. L’algorithmique ne se préoccupe pas des détails de l’implémentation, ou comment le programme s’executera.

## Blocs théoriques (ici : Algorithmes de tri)

* ### Notion abordée

Algorithmes de tri

* ### Théorie

Pour apprendre à cuisiner, on commence par suivre des recettes éprouvées, on ne s’improvise pas chef de cuisine moléculaire. Ainsi, pour introduire l’algorithmique, nous nous appuierons sur une classe d’algorithmes classiques : les algorithmes de tri.

< image : colonnes >

Un algorithme de tri permet de trier ou plus précisément d’organiser une liste d’objets selon une relation d’ordre déterminée. Dans la figure ci-dessus, les objets sont organisés soit par la luminosité croissante de leur couleur, soit par leur taille croissante.

Toutes les recettes de cuisine ne se valent pas, de même en algorithmique, selon le problème précis sous la main, un algorithme est plus adéquat qu’un autre. Il existe des dizaines d’algorithmes qui trient de manière différente, nous en verrons quelques uns juste après. Certains sont plus rapides, d’autres utilisent moins de mémoire ou bien sont plus simples à comprendre. Ainsi, selon la situation, il faut choisir le bon algorithme à utiliser.

* ### Exemples

**Tri par insertion** 

Parcourir la liste d’éléments à trier (par exemple, les rectangles de la Figure 2). Pour chaque nouvel élément, l’insérer au bon emplacement de la liste déjà parcourue. La liste déjà parcourue est ainsi triée à tout moment.

**Tri par sélection**

Rechercher le plus petit élément de la liste et l’échanger avec le premier élément de la liste. Rechercher ensuite le plus petit élément de la liste en excluant le premier élément, et l’échanger avec le deuxième élément de la liste. Rechercher ensuite le plus petit élément de la liste restante, en excluant le premier et deuxième éléments et l’échanger avec le troisième élément. Continuer de la sorte jusqu’à ce que toute la liste soit triée.

**Tri à bulles**

Comparer les deux premiers éléments de la liste et les mettre dans le bon ordre (l’lélment qui est plus petit précède celui qui est plus grand). Comparer ensuite le deuxième et troisième éléments de la liste et les mettre dans le bon ordre. Continuer de la sorte jusqu’à la fin de la liste. Après ce premier parcours de la liste, le plus grand élément se retrouve en dernière position de la liste. Parcourir à nouveau la liste, en excluant le dernier élément qui est bien trié. Parcourir ainsi la liste autant de fois qu’il y a d’éléments, en excluant les éléments bien triés en fin de liste.

* ### Prolongements

**Pour aller plus loin II**

Imaginez que les objets sont triés dans le sens inverse de ce que l’on souhaite. Trier les objets selon les trois algorithmes de tri : tri par insertion, tri par sélection et tri à bulles. Intuitivement, quel algorithme est le plus rapide dans cette configuration précise ? Quel algorithme est le plus lent ?

* ### Exercices

**Exercice VI**

Imaginons que le changement de position d’un rectangle prenne beaucoup de temps, bien plus que la comparaison de la taille de 2 rectangles. Dans ce cas, lequel des trois algorithmes serait le plus rapide ? Quel serait l’algorithme le plus lent ? Imaginons que la comparaison de la taille de 2 rectangles prenne beaucoup de temps, bien plus que le changement de position d’un rectangle. Dans ce cas, lequel des trois algorithmes serait le plus rapide ? Quel serait l’algorithme le plus lent ? Imaginons que le meilleur algorithme est celui qui propose le plus de rectangles qui sont déjà à la bonne position (leur position finale une fois triés) toutes étapes confondues. Cela peut être
le cas si l’on a pas le temps d’attendre que l’algorithme converge et on souhaite que les étapes intermédiares nous donnent une réponse aussi proche de la solution que possible. Dans ce cas, lequel des trois algorithmes serait le plus rapide ? Quel serait l’algorithme le plus lent ?

## Conclusion

### Liens et perspectives pour aller plus loin (références à d'autres chapitres, etc.)

**A retenir**
Un algorithme est une suite d’instructions dans un ordre bien précis qui permet de résoudre un problème. L’algorithme va donner un résultat en fonction des données reçues en entrée. Afin de pouvoir rechercher de manière efficace, les données doivent impérativement être triées. Il existe de multiples manières de résoudre un problème. Toutes ces manières ne se valent pas. Il faut choisir l’algorithme en fonction de ce qui doit être optimisé : le temps de résolution, l’espace de stockage, la précision de la solution, ... 

La complexité d’un algorithme se mesure en nombre d’opérations. Plus ce nombre est grand, plus l’algorithme est lent. Il existe des problème que l’on peut toujours pas résoudre de nos jours.

## Validation grâce à auto-contrôle

**Ai-je compris ?**

1. Je sais lire et appliquer un algorithme. Je sais quel résultat l’algorithme donnera à partir
d’un jeu de données.
2. Je sais écrire un algorithme. Je sais décomposer la solution d’un problème en opérations
qui suivent un certain ordre.
3. Je sais retranscrire un algorithme en un programme. Je sais traduire les opérations d’un
algorithme en instructions élémentaires if, else, while et for.
4. Je comprends ce qu’est la complexité d’un algorithme, comment on la calcule et à quoi
elle sert.
5. Je sais choisir le bon algorithme en fonction de ce qu’il faut optimiser.


