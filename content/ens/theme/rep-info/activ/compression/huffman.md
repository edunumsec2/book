# Compression et codage de Huffman

## Informations

Durée : 1 période de cours en classe

Mode : Débranché

Chapitre : Représentation de l'information

Objectifs : Faire comprendre aux élèves le principe de base derrière la compression de données

Matériel (optionnel) : Quelques dés pour tirer une lettre (uniformément) au hasard parmi 16

## Accroche(s)

Aussi étrange que cela puisse paraître, il est très souvent possible d'enregistrer un fichier de données d'une certaine taille en utilisant moins de place en mémoire que la taille initiale du fichier, et ceci sans perdre aucune information ! Ce sont les techniques de compression de données qui permettent de réaliser ça : l'activité qui suit permet de comprendre le principe de base de la compression de données à travers un jeu interactif avec les élèves.

Pour introduire le sujet, on peut parler également de manière générale du fait que dans la vie courante, on utilise des algorithmes de compression sans s'en rendre compte, comme Mr Jourdain faisait de la prose : par exemple, quand on écrit "slt" ou "tqt" dans un SMS, ou quand on utilise des acronymes. Le principe consiste à abréger des éléments qui reviennent souvent dans la conversation pour gagner de la place ou du temps.

Une autre accroche possible est de parler du code Morse qui utilise un seul point pour la lettre E qui revient très souvent en français ou en anglais, tandis que la lettre X, beaucoup moins fréquente, est encodée par un trait, deux points, un trait.

## Déroulement

### Premier jeu

Ecrire au tableau la séquence de lettres : "ABCDEFGHIJKLMNOP", choisir une lettre (éventuellement au hasard, mais ce n'est pas nécessaire), la noter sur une feuille de papier, et demander à un·e volontaire de participer au jeu. Expliquer ensuite la règle du jeu :

L'élève doit deviner quelle lettre a été choisie, ceci en ne posant que des questions binaires, c'est-à-dire des questions auxquelles on ne peut répondre que par oui ou par non. Et le but pour l'élève est de poser le moins de questions possible pour deviner la lettre.

Une fois que l'élève a trouvé la lettre, poser la question aux autres : est-ce que la séquence de questions posées par l'élève était optimale ? Aurait-on pu faire mieux ?

La stratégie optimale consiste à poser des questions qui divisent chaque fois en deux parties égales le nombre de possibilités. Ainsi, en supposant que la lettre choisie soit le D, une séquence possible de questions optimales est :

1. Est-ce une lettre entre A et H ? oui
2. Est-ce une lettre entre A et D ? oui
3. Est-ce une lettre entre A et B ? non
4. Est-ce un C ? non

Et donc, la réponse est D dans ce cas : au total, 4 questions suffisent pour deviner de quelle lettre il s'agit. Et cette conclusion reste identique, quelle que soit la lettre choisie au départ.

```{admonition} Remarque

Ce premier jeu sert d'introduction au sujet et ne traite pas directement de compression en tant que telle, mais c'est une étape nécessaire pour comprendre le jeu qui suit.

Il peut être également utile de mentionner que la séquence de questions optimales à poser n'est rien d'autre qu'une mise en oeuvre de l'algorithme de dichotomie. Pour donner une idée de son efficacité, on peut ajouter que ce même algorithme trouverait en 10 questions une lettre choisie au hasard parmi mille et en 20 questions une lettre choisie au hasard parmi un million. En comparaison, un algorithme consistant à essayer à chaque fois de deviner la lettre choisie ("Est-ce un A ?", "Est-ce un B ?", etc.) serait bien moins performant, à moins d'un heureux hasard !
```

### Second jeu

Demander ensuite à un·e autre volontaire de participer à un second jeu, et écrire la phrase "SINGING IN THE RAIN" au tableau, composée de 16 lettres (sans les espaces, qu'on laisse de côté). Puis choisir une de ces 16 lettres (éventuellement au hasard, mais ça n'est pas absolument nécessaire) et la noter sur un bout de papier. Expliquer enfin que la règle du jeu reste la même: l'élève doit trouver la lettre choisie en posant un nombre minimum de questions binaires, mais noter qu'ici plusieurs lettres se répètent, et qu'il n'y a pas besoin de deviner la position précise de la lettre, mais juste la valeur de celle-ci, c'est-à-dire "S", "I", "N", etc.

Une fois que l'élève a trouvé la lettre, poser à nouveau la question aux autres : est-ce que la séquence de questions posées par l'élève était optimale ? Aurait-on pu faire mieux ?

Pour ce second jeu, la stratégie optimale consiste à nouveau à diviser chaque fois l'ensemble des possibilités en deux parties égales, mais du fait que des lettres se répètent, on peut optimiser les questions en regroupant les possibilités. Faisons d'abord le compte du nombre d'apparitions de chaque lettre, en prenant soin de les ordonner par ordre décroissant de ce nombre d'apparitions :

lettre               | I | N | G | S | T | H | E | R | A |
---------------------|---|---|---|---|---|---|---|---|---|
nombre d'apparitions | 4 | 4 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |

On voit ainsi que les deux premières lettres I et N apparaissent en tout 8 fois, et qu'il en va de même pour le reste des lettres G, S, T, H, E, R et A. La bonne première question à poser est donc : "Est-ce un I ou un N ?". Si d'aventure la réponse à cette première question est oui, alors il ne reste plus que deux choix, avec chacun le même nombre de possibilités, et donc la deuxième question à poser est : "Est-ce un I ?" Que la réponse à cette question soit un oui ou un non, l'élève aura trouvé la lettre choisie en ne posant que deux questions au total.

Quelle deuxième question poser maintenant si la réponse à la première question est un non ? Dans ce cas, il reste les 8 possibilités suivantes :

lettre               | G | S | T | H | E | R | A |
---------------------|---|---|---|---|---|---|---|
nombre d'apparitions | 2 | 1 | 1 | 1 | 1 | 1 | 1 |

Pour séparer cet ensemble de possibilités en deux parties égales, la bonne deuxième question à poser est : "Est-ce un G, un S ou un T ?" Et ainsi de suite : si la réponse à cette deuxième question est oui, alors la troisième question à poser est : "Est-ce un G ?" Si la réponse à cette troisième question est oui, alors on a trouvé la lettre, sinon, il faut encore poser une quatrième question pour départager les deux dernières possibilités S et T.

Et finalement, si la réponse aux deux premières questions est non, alors il reste 4 possibilités H, E, R et A. Dans ce cas, deux questions supplémentaires sont nécessaires pour trouver la lettre choisie, comme lors du premier jeu, où toutes les lettres apparaissent exactement une fois chacune.

Le tableau ci-dessous résume le nombre optimal de questions qu'il faut poser pour deviner chaque lettre :

lettre               | I | N | G | S | T | H | E | R | A |
---------------------|---|---|---|---|---|---|---|---|---|
nombre d'apparitions | 4 | 4 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |
nombre de questions  | 2 | 2 | 3 | 4 | 4 | 4 | 4 | 4 | 4 |

On voit que plus une lettre est fréquente, moins elle nécessite de questions.

### Et la compression, dans tout ça?

TBD

## Développements

TBD

## Conclusion

TBD