Décomposition d'un problème en étapes
=====================================

## Algorithme : définition

Un **algorithme** est en quelque sorte « une recette » que le système informatique suit pour résoudre un problème. Lorsque l’on conçoit une recette de cuisine, on commence par déterminer les grandes étapes, comme la préparation des ingrédients, la cuisson, le service... On décompose ensuite chacune de ces étapes en instructions qu’une personne peut suivre.

Prenons un cas précis : ***réaliser une omelette***. Pour chacune des étapes il faut prévoit une marche à suivre suffisamment détaillée, afin que la personne qui suit la recette arrive au même résultat. Dans le cas de l’omelette, les instructions pourraient être (voir figure ci-dessous) : 
1. Prendre des oeufs. 
2. Casser et mélanger les œufs dans un bol.
3. Frire les œufs dans une poêle.
4. Glisser l’omelette dans une assiette.

:::{figure} 

<img src="Omelette.png" width="80%">

Les étapes à suivre pour la réalisation d’une omelette.

:::

Il en est de même pour le système informatique. On doit lui décrire toutes les opérations qu’il doit effectuer afin d’arriver au résultat souhaité. L’algorithme est **une suite d’instructions** que l’on peut suivre pour résoudre un problème.

### Les ingrédients d’un algorithme

L’objectif d’un algorithme est de résoudre un problème, concrètement l’algorithme va donner un résultat en sortie. Pour trouver ce **résultat**, l’algorithme va se baser sur  des **données** qu’il reçoit en entrée. Par exemple, un algorithme qui détecte les visages va recevoir en entrée une image et donnera en sortie le résultat oui si l’image contient un visage et non si l’image ne contient pas de visages. Un algorithme qui traduit prend en entrée un texte dans une langue et un dictionnaire. C’est tout ce dont il a besoin pour rendre en sortie un texte dans une autre langue dont le sens correspond au premier texte.

Entre l’entrée et la sortie, l’algorithme précise quelles **opérations** exécuter. Les opérations que l’on peut attendre d’un humain sont très différentes de celle d’un ordinateur. On peut donner l’instruction à un humain de casser des oeufs, mais un ce n’est pas une instruction qu’un programme peut exécuter. Par contre on peut demander à un programme de stocker une valeur dans une variable, de comparer les valeurs de plusieurs variables, de parcourir de longues listes de données. Il le fera sans se plaindre... Une opération cache une multitude d’**instructions élémentaires**. Lorsque l’ordinateur exécute l’opération comparer les valeurs de deux variables, il doit d’abord accéder chacune des variables là où elles sont stockées. Seulement après les avoir accédées, l’ordinateur peut les soustraire afin de déterminer quelle variable contient la plus grande valeur.

Notez que l’**ordre des opérations** est très important. Dans l’exemple de l’omelette, il est impossible de mélanger les œufs avant de les avoir cassés. L’ordinateur a non seulement besoin de recevoir les instructions dans le bon ordre, il a également besoin que tout lui soit précisé, et ce de manière **non ambigüe**. Il doit y avoir une seule lecture possible des opérations indiquées par un algorithme.

Ainsi, les ingrédients d’un algorithme sont donc  les suivants : 
1. Des données en entrée  
2. Des instructions élémentaires sous la forme d’opérations 
3. Ordre d’exécution des opérations
4. Un résultat en sortie

::::{admonition,attention} Exercice 1

A quoi correspondent les ingrédients d’un algorithme dans l’exemple de la recette de l’omelette ?

::::

::::{admonition,hint} Le saviez-vous ? I

Le jeu d’instructions élémentaires va dépendre du système informatique. Un algorithme  spécifie des opérations à suivre dans un ordre donné. Ces opérations seront transcrites à travers un programme en instructions exécutables par la machine. La manière dont ces instructions exécutables seront décomposées en instructions élémentaires, puis exécutées, peut être très différente d’un système à l’autre. L’algorithmique ne se préoccupe pas des détails de l’implémentation, ou comment le programme s’exécutera. 

::::

::::{admonition,attention} Exercice 2

Écrire un algorithme qui effectue la permutation circulaire de trois nombres X, Y et Z. A la fin de l’algorithme, X contient la valeur de Z, Y la valeur de X et Z la valeur de Y. Conseil : écrire à chaque étape ce que contient chacune des trois variables.

::::

::::{admonition,note} Pour aller plus loin I

Le jeu d’instructions élémentaires va dépendre du système informatique. Un algorithme  spécifie des opérations à suivre dans un ordre donné. Ces opérations seront transcrites à travers un programme en instructions exécutables par la machine. La manière dont ces instructions éxecutables seront décomposées en instructions élementaires, puis exécutées, peut être très différente d’un système à l’autre. L’algorithmique ne se préoccupe pas des détails de l’implémentation, ou comment le programme s’executera. 

::::

::::{admonition,attention} Exercices supplémentaires

**Exercice 1.** L’algorithme suivant contrôle un crayon. Quelle forme est dessinée à la fin de l’algorithme ?
```
    Répéter 8 fois :
    	Avance de 10 pas
         Tourne à droite de 45°
```
::::


