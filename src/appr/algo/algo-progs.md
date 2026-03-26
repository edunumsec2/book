# Des algorithmes aux programmes

````{thinkingmatter} Lieu mystère

Pensez à un lieu connu, qui se trouve à proximité. Ecrivez les étapes à suivre pour s’y rendre, sans mentionner le lieu. Vous ne pouvez utiliser que les instructions : **<span style="color:rgb(89, 51, 209)">avancer</span>**, **<span style="color:rgb(89, 51, 209)">tourner à gauche</span>** et **<span style="color:rgb(89, 51, 209)">tourner à droite</span>**.

Demandez à vos camarades de classe de suivre ces instructions. Sont&#8209;ils arrivés à deviner à quel lieu ils se sont rendus ?

**<span style="color:rgb(89, 51, 209)">Si&nbsp;non</span>** : essayez de comprendre à quel moment ils se sont perdus. Adaptez votre algorithme en fonction. 

**<span style="color:rgb(89, 51, 209)">Si&nbsp;oui</span>** : reformulez vos instructions en utilisant les mots&#8209;clés **<span style="color:rgb(89, 51, 209)">si&nbsp;(if)</span>**, **<span style="color:rgb(89, 51, 209)">sinon&nbsp;(else)</span>** ou **<span style="color:rgb(89, 51, 209)">tant&nbsp;que (while)</span>**.

[Optionnel] Imaginez que votre camarade peut uniquement **<span style="color:rgb(89, 51, 209)">avancer de 1m tout droit</span>** et **<span style="color:rgb(89, 51, 209)">tourner de 15 degrés</span>**. Reformulez votre solution en utilisant en plus le mot clé **<span style="color:rgb(89, 51, 209)">répéter&nbsp;(for)</span>**.

````

Une fois que l’on a déterminé le meilleur {glo}`algo|algorithme` à utiliser, pour l'automatiser, il faut le retranscrire dans un {glo}`programme|programme` qu’une machine peut comprendre. Nous allons détailler ce processus pour l’algorithme du <a href="../algorithmes-classiques/eleve.html#tri-selection">**<span style="color:rgb(89, 51, 209)">tri&nbsp;par&nbsp;sélection</span>**</a>. 

Cet algorithme consiste à parcourir la liste à trier plusieurs fois. A&nbsp;chaque {glo}`iteration|itération`, on sélectionne le plus petit élément et on l’échange avec le premier élément de la liste non triée. Comment pourrait&#8209;on traduire ceci en Python ? Comment représenter les rectangles dans un langage de programmation ? 

Tout d’abord, il faut représenter la taille des rectangles par des nombres. On peut par exemple représenter l’ordre des rectangles de la première ligne de la <a href="../algorithmes-classiques/eleve.html#fig-trier">figure **Trier**</a> en fonction de leur taille, dans une liste nommée `rect` :

```
rect = [3, 4, 1, 2, 6, 5]
```

On doit ensuite ***<span style="color:rgb(13, 204, 166)">parcourir la liste</span>*** pour trouver le plus petit élément de la liste, qui correspond au rectangle le plus court. Nous allons commencer par  ***<span style="color:rgb(13, 204, 166)">déclarer une {glo}`variable|variable`</span>***, nommée `indice_min`, qui va se souvenir de la position du plus petit élément de la liste (équivalent à l'indice de l'élément à l’intérieur de la liste). Pour commencer, nous supposons que le plus petit élément de la liste est le premier élément, et nous initialisons la variable nommée `indice_min` à `0`. 

```
# initialise une variable qui va se souvenir du plus petit rectangle de la liste
indice_min = 0 
```

Nous allons ensuite parcourir la liste à partir du deuxième élément. Pour chaque nouvel élément, nous allons tester s’il est plus petit ou plus grand que le plus petit élément connu jusqu’alors. Si&nbsp;le nouvel élément est plus petit que l'élément désigné par `indice_min`, c'est l'indice du nouvel élément qui sera stocké dans `indice_min` à la place de l'ancien :

```
# for permet de parcourir la liste rect
for i in range(1,len(rect)):  # len(rect) donne la longueur de la liste rect

    # identifie l'indice du plus petit élément de la liste
    if rect[i] < rect[indice_min] :
        indice_min = i
```

Pour faire plus simple, nous pouvons également utiliser la {glo}`fonction|fonction` Python **<span style="color:rgb(89, 51, 209)">min()</span>** qui retourne directement le plus petit élément d’une liste. Nous avons aussi besoin de la fonction **<span style="color:rgb(89, 51, 209)">index()</span>** afin d’accéder à la position (ou l'indice) du plus petit élément.

```
# identifie l'indice du plus petit élément de la liste
indice_min = rect.index(min(rect))
```

Grâce à ces fonctions Python préexistantes, nous avons remplacé les 3&nbsp;lignes du code au-dessus par une seule ligne de code. Après cette opération, `indice_min` contient l’indice du plus petit élément de la liste. On doit à ce stade, échanger cet élément et le premier élément. Comme nous avons pu le voir <a href="../decomposition-probleme/eleve.html#exercice&#8209;echange">avant</a>, pour échanger les valeurs de deux variables, nous avons besoin d'une ***<span style="color:rgb(13, 204, 166)">variable temporaire</span>***. En&nbsp;effet, si on met la valeur du plus petit élément directement à la position&nbsp;0, nous perdons la valeur contenue à la position&nbsp;0 à ce moment&#8209;là. Il faut donc la stocker temporairement dans une autre variable :

```
# échange le plus petit élément avec le premier élément
rect_temp = rect[0]
rect[0] = rect[indice_min]
rect[indice_min] = rect_temp
```

Là encore, Python permet d’écrire ces trois lignes de manière beaucoup plus compacte. En affectant les deux variables simultanément, c’est Python qui se charge de créer la variable temporaire :


```
# échange le plus petit élément avec le premier élément
rect[0], rect[indice_min] = rect[indice_min], rect[0]
```

On doit ensuite refaire exactement les mêmes opérations (parcourir à nouveau la liste pour trouver le plus petit élément et échanger sa position), mais en excluant le premier élément de la liste qui est maintenant bien trié. Donc on va rechercher le plus petit élément de la liste restante, et l’échanger cette fois&#8209;ci avec le deuxième élément de la liste (attention, il s'agit de la position&nbsp;`1` et non&nbsp;`2` en Python). On adapte le code précédent :


```
# trouve le plus petit rectangle de la liste rect[1:] (à partir du 2e élément)
indice_min = rect.index(min(rect[1:]))

# échange le plus petit élément avec le deuxième élément
rect[1], rect[indice_min] = rect[indice_min], rect[1]
```

La suite de l’algorithme consiste à nouveau à rechercher le plus petit élément de la liste restante (en excluant cette fois&#8209;ci le premier et deuxième élément, qui sont bien triés) et l’échanger avec le troisième élément (premier élément non trié). À nouveau on peut reprendre le même code, mais on incrémente tous les indices de&nbsp;`1` :

```
# trouve le rectangle le plus petit de la liste rect[2:] (à partir du 3e élément)
indice_min = rect.index(min(rect[2:]))

# échange le plus petit élément avec le troisième élément
rect[2], rect[indice_min] = rect[indice_min], rect[2]
```

On détecte un motif qui se répète. On fait toujours les mêmes opérations, mais en commençant à une position différente. On peut réécrire le même code autant de fois que d’éléments dans la liste, mais ce n'est pas optimal si la liste est longue et si on veut pouvoir réutiliser ce code pour une liste de longueur différente. Il vaut mieux remplacer l’indice qui change par une variable que l’on {glo}`incrementation|incrémente` (augmente). Notez que ce code est répété `len(rect)-1` fois et pas autant de fois qu’il y a d'éléments de la liste, car on doit pouvoir comparer et échanger deux éléments. 

```
# pour tous les éléments de la liste non triée
for j in range(0,len(rect)-1):

    # trouve le rectangle le plus petit de la liste rect[j:] (à partir de l'élément j)
    indice_min = rect.index(min(rect[j:]))

    # échange le plus petit élément avec le j-ième élément
    rect[j], rect[indice_min] = rect[indice_min], rect[j]
```

Le principal avantage de cette **<span style="color:rgb(89, 51, 209)">factorisation</span>** (réécriture) est que maintenant notre code fonctionne pour toutes les longueurs de listes. Nous n’avons plus besoin de savoir à l’avance combien d’éléments sont contenus dans la liste (combien de fois répéter les opérations). Au lieu de répéter le code un nombre prédéterminé de fois, le code s’exécute autant de fois qu’il y a d’éléments dans la liste (moins&nbsp;`1`, car on compare toujours 2&nbsp;éléments).

L’étape suivante consiste à encapsuler tout le code dans une **<span style="color:rgb(89, 51, 209)">fonction</span>** qui reçoit la liste comme **<span style="color:rgb(89, 51, 209)">{glo}`parametre|paramètre`</span>**, afin de le rendre utilisable par d'autres programmes sans avoir à copier&#8209;coller le code. Cela permet aussi en cas d’erreur de facilement corriger la fonction, plutôt que de corriger le code partout il a été copié&#8209;collé. Pour que la fonction soit utilisable, il ne faut pas oublier de rajouter le `return` qui retourne le résultat.

```
# Tri par sélection
def tri_selection(rect) :
    
    # pour tous les rectangles de la liste non triée
    for j in range(0,len(rect)-1):
   
        # trouve le rectangle le plus petit de la liste rect[j:] 
        indice_min = rect.index(min(rect[j:]))
 
        # échange le plus petit élément et le j-ième élément
        rect[j], rect[indice_min] = rect[indice_min], rect[j]

    return(rect)
```

Finalement le terme `rect` n’est pas assez général, car le tri&nbsp;par&nbsp;sélection peut être utilisé pour trier toutes sortes d’éléments et pas seulement des rectangles. Ainsi on peut renommer la {glo}`variable|variable` `rect` par le terme plus général `liste`, partout où `rect` apparait dans le code ci&#8209;dessus :


```
# Tri par sélection
def tri_selection(liste) :
    
    # pour tous les éléments de la liste non triée
    for j in range(0,len(liste)-1):
   
        # trouve l’élément le plus petit de liste[j:]
        indice_min = liste.index(min(liste[j:]))
 
        # échange le plus petit élément et le j-ième élément
        liste[j], liste[indice_min] = liste[indice_min], liste[j]

    return(liste)
```

Pour trier la liste `rect` définie au tout début, il suffit d’appeler la fonction `tri_selection` avec la liste `rect` en {glo}`argument|argument`. La fonction **<span style="color:rgb(89, 51, 209)">print()</span>** permet d'afficher la liste triée :

```
# trier la liste de rectangles par sélection
rect = [3,4,1,2,6,5]
print(tri_selection(rect))
```

En traduisant les étapes intermédiaires du tri&nbsp;par&nbsp;sélection en des lignes de code, nous avons automatisé l'algorithme. Nous l'avons transcrit en un programme informatique qui peut être exécuté sur une machine.

## Exercices

````{exercise} Jeu de la devinette 🔌

Ecrire le programme suivant : le programme pense à un nombre au hasard. Lorsque vous lui proposez un nombre, il vous dit si « c'est&nbsp;plus » ou&nbsp;si « c'est&nbsp;moins » jusqu'à ce que vous trouvez le bon nombre. Conseil : utiliser le module Python *random*.

Y a-t-il une stratégie gagnante ?
 
````

````{exercise} Plus petit nombre 🔌

Transcrire l’algorithme de l’exercice qui permet de déterminer le plus petit nombre d’une liste, en un programme Python.

````


````{exercise} Programmes de tri 🔌

Implémenter le tri&nbsp;à&nbsp;bulles et/ou le tri&nbsp;par&nbsp;insertion vus au cours.

Créer une liste qui contient les valeurs de `1` à `n` dans un ordre aléatoire, où `n` prend la valeur 10, par exemple. Vous pouvez utiliser la fonction `shuffle()` du module random.

*Pour aller plus loin.*

A l’aide du module `time` et de sa fonction `time()`, chronométrer le temps prend le tri d'une liste de 100, 500, 1000, 10000, 20000, 30000, 40000 puis 50000 nombres. 

Noter les temps obtenus et les afficher sous forme de courbe dans un tableur. Ce graphique permet de visualiser le temps d’exécution du tri en fonction de la taille de la liste. Que constatez&#8209;vous ?

Sur la base de ces mesures, pouvez&#8209;vous estimer le temps que prendrait le tri de 100000 éléments ?

Lancer le programme avec 100000 éléments et comparer le temps obtenu avec votre estimation.

````


````{exercise} Tri de Bogo🔌

Coder l’algorithme du tri de Bogo en Python (voir chapitre précédent : Le saviez&#8209;vous ?). 

Relancer l'algorithme plusieurs fois, en notant le nombre d'itérations nécessaires pour qu'il termine.

A partir de quelle taille de liste cet algorithme est&#8209;il inutilisable ?
 
````


````{exercise} Fibonacci 🔌

Ecrire un algorithme qui calcule la suite des nombres de Fibonacci. 

Traduire l’algorithme en une fonction Python. 

Comparer avec les solutions trouvées par vos camarades de classe.
````


````{eval} 

Vérifiez votre compréhension :

1. Je sais lire et appliquer un algorithme, c’est&#8209;à&#8209;dire que je peux déduire le résultat que me donnera un algorithme à partir d’un jeu de données particulier.

2. Je sais retranscrire un algorithme en un programme, je sais traduire les opérations d’un algorithme en instructions élémentaires if, else, while et for.

````


