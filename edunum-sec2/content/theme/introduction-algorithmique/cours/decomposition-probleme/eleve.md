Décomposition d'un problème en étapes
=====================================

## Algorithme ou la décomposition d’un problème

Un **algorithme** est en quelque sorte « une recette » que l’on suit pour **résoudre un problème**. Voici quelques exemples de problèmes que l’on arrive à résoudre numériquement : calculer le trajet le plus rapide entre deux lieux, gérer les livres d’une bibliothèque, détecter des visages dans une photographie ou recommander des produits. ***L’algorithme n’est donc pas un programme***. Un algorithme ne se code pas, il ne s’exécute pas et il ne donne pas de solution concrète. L’algorithme décrit plutôt un « mode d’emploi » que l’on peut suivre pour créer un programme. C’est le programme qui sera exécuté par un système informatique pour concrètement résoudre le problème.

Un mode d’emploi ou une recette décrivent **des étapes** à suivre. La préparation des ingrédients, la cuisson ou le service sont différentes étapes d’une recette de cuisine qu’une personne peut suivre pour réaliser un plat. Prenons un cas précis : ***réaliser une omelette***. Pour chaque étape de la préparation de l’omelette, il faut prévoir une marche à suivre suffisamment détaillée, afin que la personne qui suit la recette arrive au même résultat. Dans le cas de l’omelette, les opérations pourraient être (voir figure ci-dessous) : 

1. Casser les oeufs dans un bol. 
2. Mélanger les œufs jusqu’à obtenir un mélange homogène.
3. Cuire le mélange d’oeufs dans une poêle à température moyenne.
4. Lorsque cuite, glisser l’omelette dans une assiette.

:::{figure} 

<img src="media/Omelette_1.png" width="80%">

Les opérations à suivre pour la réalisation d’une omelette.

:::

Il en est de même pour l’algorithme qui **décompose le problème en sous-problèmes**. La solution de chaque sous-problème donne lieu à une étape que le système informatique peut suivre pour résoudre le sous-problème. L’algorithme décrit toutes les opérations qu'il faut effectuer pour arriver à un résultat. L’algorithme est donc **une suite d’opérations** qui permettent de résoudre un problème.  Le langage utilisé dans un algorithme est plus libre que celui utilisé dans un programme, comme le montre cet exemple :

```
Tableau Nombres : numérique
Variable i : numérique
Variable Résultat : numérique
Variable Résultat ← 0
Répéter Pour i = 1 à longueur(Nombres) # par pas de 1
    Résultat ← Résultat + Nombres[i]
Fin Pour
```

::::{admonition,note} Exercice 1

Que contient la variable résultat à la fin de l'algorithme ci-dessus ? Quel  problème cet algorithme permet-il de résoudre ?

::::

« Chaque étape d’un algorithme doit être définie précisément » (Knuth, D. E., 2011). En effet, si on ne décompose pas suffisemment la solution du problème, on peut se retrouver face à une recette inutile, par exemple : prendre des oeufs et réaliser une omelette. Cette recette ne nous dit pas vraiment comment procéder pour arriver à faire une omelette.

### Les ingrédients d’un algorithme

L’objectif d’un algorithme est de trouver la solution à un problème donné. Concrètement l’algorithme va utiliser des **données** qu’il reçoit ***en entrée*** et va retourner un **résultat** ***en sortie*** (la solution du problème). Un algorithme qui détecte les visages peut recevoir une image en entrée (les données) et peut répondre "oui" si l’image contient un visage ou "non" si l’image ne contient pas de visage (le résultat). Les données en entrée d’un algorithme qui traduit pourraient être un texte à traduire et un dictionnaire. L’algorithme traite ces données pour retourner en sortie un texte traduit dans une autre langue, dont le sens correspond au texte original.

Entre l’entrée et la sortie, l’algorithme précise quelles **opérations** exécuter. Les opérations que l’on peut demander à un humain sont très différentes de celles d’un ordinateur. On peut demander à un humain de casser des oeufs, mais un ordinateur ne peut comprendre et réaliser cette opération. Par contre on peut demander à un ordinateur de stocker une valeur dans une variable, de comparer les valeurs de plusieurs variables, de parcourir de longues listes de données. Une fois l’algorithme conçu, les opérations qu’il décrit sont retranscrites en une suite d’instructions élémentaires, c’est-à-dire un programme exécutable par un ordinateur.

Le dernier ingrédient d’un algorithme, mais tout aussi important, est l’**ordre des opérations**. Dans l’exemple de l’omelette, on ne peut cuire les œufs avant de les avoir cassés, sans quoi on obtiendrait des oeufs durs. L’ordinateur a besoin de recevoir les instructions élémentaires à exécuter dans le bon ordre. Pour résumer, les ingrédients pour concevoir un algorithme sont les suivants : 

1. Des données en entrée
2. Des opérations, dans un ordre précis
3. Un résultat en sortie

:::{figure} 

<img src="media/Diagramme_algorithme.png" width="60%">

Schéma des ingrédients d'un algorithme.

:::

Notez que les opérations d’un algorithme doivent être précises et ***non ambigües***. Il doit y avoir une seule interprétation possible de l’algorithme. Une recette de cuisine ne serait pas assez précise pour un ordinateur : il faudrait indiquer précisément ce que température moyenne et mélange homogène veulent dire. Les êtres humains peuvent interpréter, deviner et supposer, mais pas les ordinateurs.

::::{admonition,hint} Le saviez-vous ? I

Le jeu d’instructions élémentaires dépend du système informatique. Un algorithme spécifie des opérations à suivre dans un ordre donné. Ces opérations sont transcrites à travers un programme en instructions élémentaires exécutables par la machine, qui peuvent être très différentes d’un système informatique à l’autre. L’algorithmique permet d’aborder la résolution de problème de manière générale, sans se préoccuper des détails de l’implémentation sur différents systèmes. 

::::

::::{admonition,note} Exercice 2

A quoi correspondent les ingrédients d’un algorithme dans l’exemple de la recette de l’omelette ?

::::

::::{admonition,note} Exercice 3

Ecrire un algorithme qui échange les valeurs de 2 variables. Représenter les deux variables par deux cases. Chaque case a une étiquette (le nom de la variable) et un contenu (la valeur de la variable). Représenter le contenu de chaque variable après chaque opération de votre algorithme.

::::




## Exercices supplémentaires

::::{admonition,note} Exercice 4 

L’algorithme suivant contrôle un crayon. Quelle forme dessine-t-il ?
```
Répéter 8 fois :
    Avance de 5 cm
    Tourne à droite de 60°
```
::::

::::{admonition,note} Exercice 5

Ecrire un algorithme qui permet de déterminer le plus petit nombre d’une liste. Penser à décomposer la solution en différentes étapes.

Appliquer l’algorithme à la liste [3,6,2,8,1,9,7,5].

Avez-vous trouvé la bonne solution ? Si non, modifier votre algorithme afin qu’il permette de trouver la bonne solution.

::::

::::{admonition,note} Exercice 6

On souhaite déterminer l’élève dont la date d’anniversaire est la plus proche de la date d’aujourd’hui dans le futur. Ecrire un algorithme qui permet de trouver cet élève (utiliser un langage familier). Penser à décomposer le problème en sous-problèmes. 

Comparer votre solution à celle d’un autre élèves : avez-vous procédé de la même manière ? Si non, expliquez vos raisonnements.

Un ordinateur peut-il réaliser les opérations décrites par votre algorithme ?

::::

::::{admonition,note} Exercice 7

Écrire un algorithme qui effectue la permutation circulaire des variables X, Y et Z: à la fin de l’algorithme : X contient la valeur de Z, Y la valeur de X et Z la valeur de Y. Conseil : penser à chaque variable comme un tiroir avec une étiquette X, Y ou Z qui contient une valeur. Ce tiroir ne peut stocker qu’une valeur à un moment donné. 

Une fois l’algorithme écrit, représenter les variables par une case qui contient des valeurs de votre choix. Suivre les opérations de l’algorithme une après l’autre et dessiner leur impact sur le contenu des variables. Est-ce que votre algorithme donne le résultat attendu ? Si non, modifier votre algorithme afin qu’il permette de résoudre le problème correctement.

::::

::::{admonition,note} Exercice 4

Quel est le résultat de la suite des trois affectations suivantes ? Vérifier votre solution en dessinant une case par variable et en y mettant des valeurs fictives. Suivre les opérations dans l’ordre et dessiner le contenu des variables après chaque étape.

```
X ← X + Y
Y ← X – Y
X ← X – Y
```

::::




::::{admonition,hint} Ai-je compris ?

1. Je connais la différence entre un algorithme et un programme.

2. Je sais formuler un algorithme : je décompose le problème en sous-problèmes et je décris les opérations qui permettent de résoudre chaque sous-problème.

::::




## Solutions des exercices de la théorie 

::::{admonition,note} Solution de l'exercice 1

L’algorithme permet de calculer la somme des nombres contenus dans la liste Nombres.

::::

::::{admonition,note} Solution de l'exercice 2

Les oeufs sont les données en entrée, les opérations correspondent aux instructions numérotées de 1 à 4 dans la recette et finalement le résultat en sortie est l’omelette. On peut considérer le matériel culinaire (bol, fourchette, poêle, spatule) comme du matériel informatique à notre disposition, capable de traiter les données. En effet on peut cuire plein d’autres aliments dans une poêle.

::::

::::{admonition,note} Solution de l'exercice 3

Soient les variables X et Y qui contiennent les valeurs 1 et 2. Une solution naïve consisterait à écrire l’algorithme suivant :

```
X ← Y
Y ← X
```

Nous allons représenter ces deux variables par des cases étiquetées. La première case contient 1 et s’appelle X, la deuxième contient la valeur 2 et est étiquetée Y : 

<img src="media/Algo1Ex3_1.png" width="20%">

Après la première opération où on met la valeur de Y dans la variable X on se retrouve avec cette situation, où la valeur contenue dans Y écrase la valeur qui était contenue dans X :

<img src="media/Algo1Ex3_2.png" width="20%">

On n’a plus accès à la valeur qui était stockée dans la variable X. Pour remédier à ce problème, il faut utiliser une variable temporaire Z qui va se souvenir de la valeur précédente de X. Un algorithme correct pour échanger les valeurs de deux variables est :

```
Z ← X
X ← Y
Y ← Z
```

Si on dessine l’état des variables après chacune de ces opérations dans des cases, voici ce qu’on obtient :

<img src="media/Algo1Ex3_3.png" width="20%">

::::


