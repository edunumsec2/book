(ens:repinfo:compressionhuffman)=
# Compression sans pertes et codage de Huffman

---- 

Aussi étrange que cela puisse paraître, il est très souvent possible d'enregistrer un fichier de données d'une certaine taille en utilisant moins de place en mémoire que la taille initiale du fichier, et ceci sans perdre aucune information ! Ce sont les techniques de compression de données qui permettent de réaliser ça : l'activité qui suit permet de comprendre le principe de base de la compression de données à travers un jeu interactif avec les élèves.

Pour introduire le sujet, on peut parler également de manière générale du fait que dans la vie courante, on utilise des algorithmes de compression sans s'en rendre compte, comme Mr Jourdain faisait de la prose : par exemple, quand on écrit "slt" ou "tqt" dans un SMS, ou quand on utilise des acronymes. Le principe consiste à abréger des éléments qui reviennent souvent dans la conversation pour gagner de la place ou du temps.

Une autre accroche possible est de parler du code Morse qui utilise un seul point pour la lettre E qui revient très souvent en français ou en anglais, tandis que la lettre X, beaucoup moins fréquente, est encodée par un trait, deux points, un trait.

----

```{admonition} Compression sans pertes et codage de Huffman
:class: hint
* Thème : Représentation de l'information
* Niveau : moyen
* Durée : 1 période
* Objectifs pédagogiques : comprendre le principe de base de la compression sans pertes
* Modalité : débranché
* Matériel : (év.) 4 pièces de monnaies ou 4 dés pour tirer une lettre uniformément au hasard parmi 16
* Prérequis : codage binaire
* Taille du groupe : classe entière
```


```{dropdown} **Déroulement**

1. {ref}`Premier jeu<huffman.premierjeu>` (durée : 10 minutes)

1. {ref}`Second jeu<huffman.secondjeu>` (durée : 15 minutes)

1. {ref}`Et la compression, dans tout ça ?<huffman.compression>` (durée : 15 minutes)

1. {ref}`Développements<huffman.developpements>` (durée : 5 minutes ou ...)

```

(huffman.premierjeu)=
## Premier jeu

*Durée : 10 minutes*

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

Il peut être également utile de mentionner que la séquence de questions optimales à poser n'est rien d'autre qu'une mise en œuvre de l'algorithme de dichotomie. Pour donner une idée de son efficacité, on peut ajouter que ce même algorithme trouverait en 10 questions une lettre choisie au hasard parmi mille et en 20 questions une lettre choisie au hasard parmi un million. En comparaison, un algorithme consistant à essayer à chaque fois de deviner la lettre choisie ("Est-ce un A ?", "Est-ce un B ?", etc.) serait bien moins performant, à moins d'un heureux hasard !
```

(huffman.secondjeu)=
## Second jeu

*Durée : 15 minutes*

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

On voit notamment que plus une lettre est fréquente, moins elle nécessite de questions.

(huffman.compression)=
## Et la compression, dans tout ça?

*Durée : 15 minutes*

Tout ceci semble a priori quelque peu éloigné du sujet, mais en fait, le lien avec l'algorithme de compression de Huffman est presque immédiat ! Voici plus précisément comment établir ce lien.

Pour encoder les 16 lettres ABCDEFGHIJKLMNOP du premier jeu sous la forme d'une séquence de bits, il n'y a pas d'autre choix que d'utiliser 4 bits par lettre, vu que celles-ci sont toutes différentes. Ainsi, on encode par exemple A par 0000, B par 0001, C par 0010, etc., et le nombre total de bits nécessaires pour encoder la séquence  ABCDEFGHIJKLMNOP vaut donc $16 \times 4=64$.

Il est bien sûr possible de refaire exactement la même chose pour encoder la séquence SINGING IN THE RAIN (en oubliant encore une fois les espaces), mais ce serait ignorer le fait que certaines lettres se répètent. Pour être plus précis, il n'y a que... 9 lettres différentes dans cette séquence ; malheureusement une de trop pour pouvoir représenter chaque lettre avec 3 bits ! Donc il semble a priori qu'on ne gagne rien ici. Cependant, si on utilise l'information additionnelle liée au nombre d'apparitions de chaque lettre, alors on peut faire mieux ! Et c'est là que le second jeu vient en aide pour définir un schéma d'encodage efficace, suivant les deux règles suivantes :

1. Chaque lettre est encodée avec un nombre de bits égal au nombre de questions binaires nécessaires pour deviner la lettre.
2. Le mot de code associé à chaque lettre est la séquence de bits correspondant à la séquence de réponses obtenues lors du jeu (avec la correspondance oui=1 et non=0, par exemple).

Ainsi, les mots de code suivants sont obtenus pour la séquence SINGING IN THE RAIN :

lettre                    | I | N | G | S | T | H | E | R | A |
--------------------------|---|---|---|---|---|---|---|---|---|
nombre d'apparitions      | 4 | 4 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |
nombre de questions/bits  | 2 | 2 | 3 | 4 | 4 | 4 | 4 | 4 | 4 |
mot de code correspondant | 11 | 10 | 011 | 0101 | 0100 | 0011 | 0010 | 0001 | 0000 |

Ce système d'encodage, ou *dictionnaire*, est clairement plus économe en bits que le système d'encodage classique décrit plus haut, utilisant 4 bits par lettre. Faisons le compte du nombre total de bits utilisés avec ce nouvel encodage : 

$8 \times 2 + 2 \times 3 + 6 \times 4 = 16 + 6 + 24 = 46$ bits

L'économie de place réalisée est donc de l'ordre de $\frac{64-46}{64} = \frac{18}{64} \simeq 28\%$ ; un taux de compression à peu près équivalent à celui obtenu lors de la compression de fichiers de données informatiques avec le format ZIP.

Pour autant, une question importante reste en suspens : quand on encode chaque lettre avec le même nombre de bits, il est trivial de décoder la séquence de bits pour retrouver la séquence de lettres correspondante, en lisant simplement les bits 4 par 4 dans l'exemple vu plus haut. Mais qu'en est-il ici où des lettres d'une même séquence sont encodées avec des nombres de bits différents ? Avec l'encodage ci-dessus, la séquence SINGING IN THE RAIN s'écrit :

010111100111110011...

A priori, il peut sembler sans espoir de retrouver le message d'origine... Mais il se trouve que si on lit cette séquence *de gauche à droite*, alors muni du dictionnaire ci-dessus, le décodage de la séquence est très facile: il suffit de rechercher à quelle lettre peuvent correspondre les premiers bits de la séquence : en essayant avec les deux premiers, on voit que le mot de code 01 n'est pas listé dans le dictionnaire ; en essayant avec les trois premiers, on voit que 010 ne fait pas non plus partie du dictionnaire ; donc la première lettre est forcément celle encodée par les quatre premiers bits 0101, à savoir un S. Puis on refait la même chose avec le reste de la séquence de bits 11100111110011... : ici, on voit que les deux premiers bits forment le mot de code 11 correspondant à la lettre I ; et ainsi de suite... Le message d'origine peut ainsi être entièrement décodé ; il est donc bien vrai qu'aucune information n'est perdue !

(huffman.developpements)=
## Développements

*Durée : 5 minutes de conclusion, ou un autre cours entier!*

Plusieurs remarques méritent d'être faites ici pour compléter la description de cette activité.

### Utilisation du hasard dans le jeu

Si on tire uniformément la lettre à deviner parmi les 16 lettres qui composent la séquence (ce qui peut se faire en combinant les résultats de deux dés à 4 faces, par exemple), alors on peut estimer le *nombre moyen* de questions que posera l'élève suivant une stratégie optimale :

$\frac{8}{16} \times 2 + \frac{2}{16} \times 3 + \frac{6}{16} \times 4 = \frac{16+6+24}{16} = \frac{46}{16} = 2,875$

Par définition, ce nombre est aussi égal au nombre moyen de bits utilisés par lettre par le codage de Huffman, et dans cet exemple précis, il correspond aussi à l'*entropie* de la séquence SINGING IN THE RAIN. Le premier théorème de Shannon stipule que pour n'importe quel système d'encodage qui permet un décodage sans ambiguïté (comme vu ci-dessus), le nombre moyen de bits utilisés par lettre ne peut jamais descendre en dessous de l'entropie de la séquence de lettres (noter cependant que la définition générale de l'entropie d'une séquence de lettres fait intervenir la notion de logarithme et dépasse donc les connaissances des élèves en première année de gymnase).

### Dictionnaire sans préfixe

La magie qui permet de lire la séquence de gauche à droite vient du fait que par construction, aucun mot du dictionnaire construit avec ce système n'est le *préfixe* d'un autre. Par exemple, on trouve dans le dictionnaire les mots de code 110 et 0101, mais pas 110 et 1101, ni encore 010 et 0101. De cette façon, il n'y a aucune ambiguïté
à décoder la séquence de gauche à droite.

### Faut-il toujours recalculer un dictionnaire pour compresser chaque nouvelle séquence de lettres ?

Clairement, non. Si on a affaire à un texte écrit en français, par exemple, on peut se baser sur un dictionnaire établi une fois par toutes pour un texte "standard" (tel que la déclaration des droits de l'homme), en supposant souvent à raison que les fréquences d'apparition des lettres restent similaires d'un texte à l'autre.

### Compresser des fichiers binaires ?

Si la séquence qu'on désire compresser est elle-même une séquence de 0 et de 1 (c'est-à-dire, n'importe fichier de données numériques), que faire ? Dans ce cas, on peut simplement regrouper par 8 les bits de la séquence pour former des séquences de symboles (avec le code ASCII, par exemple), puis appliquer la méthode décrite ci-dessus.

### Codages de Huffman de de Shannon-Fano

Le système d'encodage présenté ci-dessus n'est à proprement parler pas exactement le codage de Huffman, mais plutôt le codage de Shannon-Fano. Ceci dit, dans l'exemple de la séquence SINGING IN THE RAIN, les deux systèmes d'encodage coïncident parfaitement. On observe par contre des différences mineures de performance entre les deux systèmes d'encodage (avec un avantage systématique à Huffman) dans des situations moins idéales où les nombres d'apparitions des lettres dans la séquence sont plus irréguliers.

Pour plus d'informations sur le sujet, voici des liens vers des vidéos expliquant la notion d'entropie, ainsi que les codages de Shannon-Fano et de Huffman :

entropie : https://www.youtube.com/watch?v=nAA7UyiCIOE

codage de Shannon-Fano : https://www.youtube.com/watch?v=DSdTiFc3Aws

codage de Huffman : https://www.youtube.com/watch?v=UAY-wpHZCs4

## Autres algorithmes de compression

### Compression sans pertes

Les codages de Huffman ou de Shannon-Fano ne sont de loin pas les seuls systèmes permettant de faire de la compression sans perte d'information, dite aussi plus simplement "compression sans pertes". Un défaut important de l'approche évoquée ici est qu'il est nécessaire de connaître (ou au moins estimer) à l'avance les fréquences d'apparition de chaque lettre dans la séquence à compresser, ce qui s'avère trop lent lors de la compression de grands fichiers de données. Dans ce cas, il vaut mieux recourir à des algorithmes de compression dits *universels*, tels que l'algorithme de Lempel-Ziv, qui "apprend" en quelque sorte les fréquences d'apparition des lettres dans la séquence au fur et à mesure qu'il lit (et compresse) celle-ci.

### Compression avec pertes

Finalement, il importe de remarquer qu'il existe une pléthore d'autres algorithmes de compression dite "avec pertes", absolument pas évoqués ici, et permettant d'atteindre des taux de compression beaucoup plus élevés que ceux mentionnés plus haut, ceci au prix de la perte d'une partie de l'information contenue dans le signal d'origine. Tout l'art de la compression avec pertes consiste à se débarrasser de l'information qu'on ne perçoit pas ou peu (telle des fréquences inaudibles dans un son, des variations subtiles de bleu dans une photo du ciel, etc.) et à encoder proprement celle qui est nécessaire à une bonne reconstitution du signal. Citons notamment les formats de fichiers MP3, JPEG et MP4 qui utilisent de tels algorithmes de compression avec pertes pour le son, les images et la vidéo, respectivement.

## Conclusion

Cette activité donne un aperçu du fonctionnement des algorithmes de compression de données, qui sont utilisés en permanence par les systèmes informatiques modernes. Il est à espérer que le côté ludique et interactif de l'activité permette de faire passer quelques idées sur un sujet qui reste quand-même techniquement un peu plus difficile que les autres vus dans ce chapitre. 