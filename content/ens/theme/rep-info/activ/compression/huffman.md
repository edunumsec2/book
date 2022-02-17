# Compression et codage de Huffman

## Informations

Durée : 1 période de cours en classe

Mode : Débranché

Chapitre : Représentation de l'information

Objectifs : Faire comprendre aux élèves le principe de base derrière la compression de données

Matériel (optionnel) : Quelques dés pour tirer une lettre (uniformément) au hasard parmi 16

## Accroche

Aussi étrange que cela puisse paraître, il est très souvent possible d'enregistrer un fichier de données d'une certaine taille en utilisant moins de place en mémoire que la taille initiale du fichier, et ceci sans perdre aucune information ! Ce sont les techniques de compression de données qui permettent de réaliser ça : l'activité qui suit permet de comprendre le principe de base de la compression de données à travers un jeu interactif avec les élèves.

## Déroulement

### Premier jeu

Ecrire au tableau la séquence de lettres : ABCDEFGHIJKLMNOP, choisir une lettre (éventuellement au hasard, mais ce n'est pas nécessaire), la noter sur une feuille de papier, et demander à un·e volontaire de participer au jeu. Expliquer ensuite la règle du jeu :

L'élève doit deviner quelle lettre a été choisie, ceci en ne posant que des questions binaires, c'est-à-dire des questions auxquelles on ne peut répondre que par oui ou par non. Et le but pour l'élève est de poser le moins de questions possible pour deviner la lettre.

Une fois que l'élève a trouvé la lettre, poser la question aux autres : est-ce que la séquence de questions posées par l'élève était optimale ? Aurait-on pu faire mieux ?

La stratégie optimale consiste à poser des questions qui divisent chaque fois en deux parties égales le nombre de possibilités. Ainsi, en supposant que la lettre choisie soit le D, une séquence possible de questions optimales est :

1. Est-ce une lettre entre A et H ? oui
2. Est-ce une lettre entre A et D ? oui
3. Est-ce une lettre entre A et B ? non
4. Est-ce un C ? non

Et donc, la réponse est D dans ce cas : au total, 4 questions suffisent pour deviner de quelle lettre il s'agit. Et cette conclusion reste identique, quelle que soit la lettre choisie au départ.

````{admonition} Remarque

Ce premier jeu sert d'introduction au sujet et ne traite pas directement de compression en tant que telle, mais c'est une étape nécessaire pour comprendre le jeu qui suit.

Il peut être également utile de mentionner que la séquence de questions optimales à poser n'est rien d'autre qu'une mise en oeuvre de l'algorithme de dichotomie. Pour donner une idée de son efficacité, on peut ajouter que ce même algorithme trouverait en 10 questions une lettre choisie au hasard parmi mille et en 20 questions une lettre choisie au hasard parmi un million. En comparaison, un algorithme consistant à essayer à chaque fois de deviner la lettre choisie ("Est-ce un A ?", "Est-ce un B ?", etc.) serait bien moins performant, à moins d'un heureux hasard !
````

### Second jeu

TBD

## Développements

TBD

## Conclusion

TBD