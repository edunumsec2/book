# (Second) théorème de Shannon

Le but de cette section est de présenter de manière abordable une partie du travail important accompli par Claude Shannon dans les années 50 sur la "communication en présence de bruit". Elle peut être vue comme une extension au chapitre sur la représentation de l'information.

## Mise en situation : Bob est perdu au milieu de la forêt

Supposons que deux personnes, disons Alice et Bob, désirent communiquer, et imaginons le scénario où Bob est perdu au milieu d'une forêt ; Alice, qui connaît la position GPS de Bob et qui a aussi la carte de la forêt devant elle, voit dans quelle direction (N, S E ou W) Bob devrait aller pour en sortir au plus vite.

Supposons maintenant que pour communiquer avec Bob, Alice ne puisse envoyer que des suites de 0 et de 1. On voit ici que 2 bits suffisent à Alice pour transmettre l'information requise, en utilisant le dictionnaire suivant (sur lequel elle se sera mise d'accord au préalable avec Bob) :

direction   | N | S | E | W |
------------|---|---|---|---|
mot de code |11 |10 |01 |00 |

Disons qu'elle lui transmette justement le message "va au nord!" en envoyant le mot de code 11. Il se peut qu'à cause du "bruit sur la ligne", un des deux bits transmis ne parvienne pas correctement à Bob (on dit alors qu'il est "effacé") : par exemple, si le deuxième bit est effacé, Bob recevra la séquence "1?" (le point d'interrogation symbolisant l'effacement) et ne saura donc pas s'il faut aller au nord ou au sud pour sortir rapidement de la forêt.

Pour remédier à ce problème, Alice pourrait utiliser plutôt le dictionnaire suivant, où chaque bit est doublé, ce qui ajoute de la *redondance* au mot de code transmis :

direction   | N | S | E | W |
------------|---|---|---|---|
mot de code |1111 |1100 |0011 |0000 |

Ainsi, si un bit est effacé au cours de la transmission, disons le 3e, Bob reçoit le mot de code "11?1", et par identification avec le tableau ci-dessus, il voit bien qu'Alice lui dit d'aller au nord ; l'erreur de transmission a donc pu être corrigée.

Fondamentalement, ce qui se passe ici est que les mots de codes potentiellement envoyés par Alice sont plus *distants* les uns des autres que dans le premier cas : en effet, il y a toujours au moins deux bits de différence entre chaque paire de mots de code (entre 1111 et 1100, par exemple), ce qui permet de corriger un effacement.

## Généralisation

Supposons maintenant qu'Alice désire envoyer un message non pas parmi 4 possibilités différentes, mais parmi $M$. Pour simplifier l'exposition de ce qui suit, supposons également que $M$ soit une puissance de 2, c'est-à-dire que $M=2^k$ pour un nombre entier positif $k$ donné. Dans ce cas, $k$ bits suffisent a priori pour cette transmission (avec $k=3$ bits, par exemple, Alice pourrait envoyer un des 8 messages suivants: N, NE, E, SE, S, SW, W, NW ; avec $k=4$ bits, elle pourrait envoyer une information encore plus précise parmi 16 possibilités: N, NNE, NE, ENE, E, etc.).

Mais  supposons encore qu'en moyenne, une proportion $\varepsilon$ des bits envoyés par Alice soient effacés lors de la transmission, et que ces effacements surviennent de façon aléatoire. Ceci veut dire concrètement que si Alice envoie $n$ bits, alors seuls $n \, (1-\varepsilon)$ d'entre eux parviennent à Bob ; de plus, il n'y a aucun moyen de savoir à l'avance lesquels seront effacés.

```{admonition} Remarque
La lettre grecque $\varepsilon$ utilisée ici ne fait pas référence au $\varepsilon$ infinitésimal en mathématiques ! Ici, la lettre $\varepsilon$ veut juste faire penser au "e" de "erreur" ou "effacement".
```

Comment s'assurer dans cette situation que Bob puisse toujours retrouver le message envoyé par Alice ? Clairement, si Alice envoie le message "tel quel" en l'encodant sur $k$ bits, ça ne fonctionnera pas. Il faut donc qu'Alice ajoute ici de la redondance pour protéger son message des effacements qui surviennent, en envoyant plus de $k$ bits.