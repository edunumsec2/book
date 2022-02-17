# Compression et codage de Huffman

## Informations

Durée: 1 période de cours en classe

Mode: Débranché

Chapitre: Représentation de l'information

Objectifs: Faire comprendre le principe de base derrière la compression de données aux élèves

Matériel (optionnel): un dé ou une pièce de monnaie pour tirer une lettre au hasard

## Accroche

Aussi étrange que cela puisse paraître, il est possible d'enregistrer un fichier de données d'une certaine taille en utilisant moins de place en mémoire que la taille initiale du fichier, et ceci sans perdre aucune information! Ce sont les techniques de compression de données qui permettent de réaliser ça: l'activité qui suit permet de comprendre le principe de base de la compression de données à travers un jeu interactif avec les élèves

## Déroulement

### Premier jeu

Ecrire au tableau la séquence de lettres: ABCDEFGHIJKLMNOP, choisir une lettre, la noter sur une feuille de papier, et demander à un·e volontaire de participer au jeu. Expliquer ensuite la règle du jeu:

L'élève doit deviner quelle lettre a été choisie, ceci en ne posant que des questions binaires, c'est-à-dire des questions auxquelles on ne peut répondre que par oui ou par non. Et le but pour l'élève est de poser le moins de questions possibles pour deviner la lettre.

Une fois que l'élève a trouvé la lettre, poser la question aux autres: est-ce que la séquence de questions posées par l'élève était optimale ? Aurait-on pu faire mieux ?

La stratégie optimale ici est de poser des questions qui divisent chaque fois en deux le nombre de possibilités. Ainsi, en supposant que la lettre choisie soit le D, une séquence possible de questions optimales est:

1. Est-ce une lettre entre A et H? oui
2. Est-ce une lettre entre A et D? oui
3. Est-ce une lettre entre A et B? non
4. Est-ce un C? non

Et donc, la réponse est D dans ce cas (note: il n'y a pas besoin d'obtenir un oui pour la dernière question): 4 questions suffisent donc pour deviner la lettre.

### Second jeu
