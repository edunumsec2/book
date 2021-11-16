````{admonition} Matière à réfléchir
:class: attention

Pensez à un lieu connu à proximité. Ecrivez les étapes à suivre pour s’y rendre, sans mentionner le lieu. Vous ne pouvez utiliser que les instructions : **<span style="color:rgb(89, 51, 209)">avancer, tourner (à gauche ou à droite).</span>**

Demandez à un.e camarade de classe de suivre ces instructions. Est-ce que votre camarade arrive à deviner à quel endroit il/elle s’est rendu.e ?

**<span style="color:rgb(89, 51, 209)">Si non</span>** : essayez de comprendre à quel moment il/elle s’est perdu.e. Adaptez votre algorithme en fonction. 

**<span style="color:rgb(89, 51, 209)">Si oui</span>** : reformulez vos instructions en utilisant les mots-clés **<span style="color:rgb(89, 51, 209)">si (if), sinon (else), tant que (while)</span>**.

[Optionnel] Imaginez que votre camarade peut uniquement **<span style="color:rgb(89, 51, 209)">avancer de 1m tout droit</span>** et **<span style="color:rgb(89, 51, 209)">tourner de 30 degrés</span>**. Reformulez votre solution en utilisant le mot clé **<span style="color:rgb(89, 51, 209)">répéter</span>**.

````

## 3. Formalisation et implémentation de solutions algorithmiques

Une fois que l’on a déterminé le meilleur {glo}`algo|algorithme` à utiliser, il faut le retranscrire dans un programme qu’une machine peut comprendre. Nous allons détailler ce processus pour l’{glo}`algo|algorithme` du **<span style="color:rgb(89, 51, 209)">tri par sélection</span>**. 

Cet {glo}`algo|algorithme` consiste à parcourir la liste à trier plusieurs fois. A chaque {glo}`iteration|itération`, on sélectionne le plus petit élément et on l’échange avec le premier élément de la liste non triée. Comment pourrait-on traduire ceci en Python ? Comment représenter ces rectangles dans un langage de programmation ? 

Tout d’abord, il faut représenter la taille des rectangles numériquement. On peut par exemple représenter l’ordre des rectangles de la première ligne de la <a href="../algorithmes-classiques/eleve.html#fig-trier">Figure **Trier**</a>, en fonction de leur taille, dans une liste nommée `rect` :

```
rect = [3,4,1,2,6,5]
```

On doit ensuite trouver le plus petit élément de la liste (le rectangle le plus court). Nous allons commencer par supposer que l’élément le plus petit est le premier élément, et nous initialisons une {glo}`variable|variable` nommée indice_min à 0. Cette {glo}`variable|variable` va stocker l’indice du plus petit élément de la liste (la position de l’élément à l’intérieur de la liste). Nous allons ensuite parcourir la liste à partir du deuxième élément. Pour chaque élément nous allons tester s’il est plus petit ou plus grand que le plus petit élément connu jusqu’alors :

```
# trouve le rectangle le plus petit de la liste
indice_min = 0 
for i in range(1,len(rect)):  # len(rect) donne la longueur de rect
    if rect[i] < rect[indice_min] :
        indice_min = i
```

Pour faire plus simple, nous pouvons également utiliser la {glo}`fonction|fonction` min() qui retourne directement le plus petit élément d’une liste. Nous avons aussi besoin de la {glo}`fonction|fonction` index() afin d’accéder à la position du plus petit élément.

```
indice_min = rect.index(min(rect))
```

Après cette opération, `indice_min` contient l’indice de l’élément le plus petit de la liste. On doit à ce stade, échanger cet élément et le premier élément. Comme nous avons pu le voir précédemment, il faut une {glo}`variable|variable` temporaire pour échanger les valeurs de deux {glo}`variable|variables` . Si on met la valeur du plus petit élément directement à la position 0, nous perdons la valeur contenue à ce moment-là à la position 0. Il faut donc la stocker temporairement dans une autre {glo}`variable|variable`  :

```
# échange l’élément le plus petit et le premier élément
rect_temp = rect[0]
rect[0] = rect[indice_min]
rect[indice_min] = rect_temp
```

Là encore, il est possible d’écrire de manière plus compacte en Python. En affectant les deux {glo}`variable|variables` simultanément, c’est Python qui se charge de créer la {glo}`variable|variable` temporaire :


```
rect[0], rect[indice_min] = rect[indice_min], rect[0]
```

On doit ensuite refaire exactement les mêmes opérations, mais en excluant le premier élément qui est bien trié. Donc on va rechercher le plus petit élément de la liste restante, et l’échanger cette fois-ci avec le deuxième élément de la liste (position 1). On adapte le code :


```
# trouve le rectangle le plus petit de la liste rect[1:]
indice_min = rect.index(min(rect[1:]))

# échange le plus petit élément avec le deuxième élément
rect[1], rect[indice_min] = rect[indice_min], rect[1]
```

La suite de l’{glo}`algo|algorithme` consiste à nouveau à rechercher le plus petit élément de la liste restante (en excluant le premier et deuxième élément) et l’échanger avec le troisième élément (premier élément non trié). À nouveau on peut reprendre le même code, mais on incrémente tous les indices de 1 :

```
# trouve le rectangle le plus petit de la liste rect[2:]
indice_min = rect.index(min(rect[2:]))

# échange le plus petit élément avec le troisième élément
rect[2], rect[indice_min] = rect[indice_min], rect[2]
```

On détecte un motif qui se répète. On fait toujours les mêmes opérations, mais en commençant à une position différente. Plutôt que de réécrire le même code autant de fois que d’éléments dans la liste, on peut remplacer l’indice de début par une {glo}`variable|variable` que l’on {glo}`incrementation|incrémente`. Notez que ce code est répété len(rect)-1 fois et pas autant de fois qu’il y a d'éléments de la liste, car on doit pouvoir comparer et échanger deux éléments. 

```
# pour tous les éléments de la liste non triée
for j in range(0,len(rect)-1):

	# trouve le rectangle le plus petit de la liste rect[j:]
	indice_min = rect.index(min(rect[j:]))

    # échange le plus petit élément et le j-ième élément
    rect[j], rect[indice_min] = rect[indice_min], rect[j]
```

Le principal avantage de cette ***<span style="color:rgb(13, 204, 166)">factorisation</span>*** (réécriture) est que maintenant notre code fonctionne pour toutes les longueurs de listes. Nous n’avons plus besoin de savoir à l’avance combien d’éléments sont contenus dans la liste (combien de fois répéter les opérations). Au lieu de répéter le code un nombre prédéterminé de fois, le code s’exécute autant de fois qu’il y a d’éléments dans la liste (moins 1, car on compare toujours 2 éléments).

L’étape suivante consiste à encapsuler tout le code dans une {glo}`fonction|fonction` qui reçoit la liste comme {glo}`parametre|paramètre`, afin de le rendre utilisable par différents {glo}`programme|programmes` sans avoir à copier-coller le code. Cela permet aussi en cas d’erreur de facilement corriger la {glo}`fonction|fonction`, sans avoir à savoir où elle a été utilisée.

```
# Tri par sélection
def fonction tri_selection(rect) :
    
    # pour tous les rectangles de la liste non triée
    for j in range(0,len(rect)-1):
   
        # trouve le rectangle le plus petit de la liste rect[j:] 
        indice_min = rect.index(min(rect[j:]))
 
        # échange le plus petit élément et le j-ième élément
        rect[j], rect[indice_min] = rect[indice_min], rect[j]
```

Finalement le terme `rect` n’est pas assez général, car le tri par sélection peut être utilisé pour trier toutes sortes d’éléments et pas seulement des rectangles. Ainsi on peut renommer la {glo}`variable|variable` `rect` par liste :


```
# Tri par sélection
def fonction tri_selection(liste) :
    
    # pour tous les éléments de la liste non triée
    for j in range(0,len(liste)-1):
   
        # trouve l’élément le plus petit de liste[j:]
	    indice_min = liste.index(min(liste[j:]))
 
        # échange le plus petit élément et le j-ième élément
        liste[j], liste[indice_min] = liste[indice_min], liste[j]
```

Pour trier la liste rect définie au tout début, il suffit d’appeler la {glo}`fonction|fonction` tri_selection avec la liste en {glo}`argument|argument`. Pour afficher la liste triée :

```
rect = [3,4,1,2,6,5]
print(tri_selection(rect))
```

<!-- ````{admonition} Question philosophique

:class: note

Tout algorithme peut être exprimé sous forme de programme. 

Mais est-ce que derrière chaque programme se cache un algorithme ?

```` 
-->






````{admonition} Exercice 1 : jeu de la devinette 🔌
:class: note

Ecrire le programme suivant : le programme pense à un nombre au hasard. Lorsque vous lui proposez un nombre, il vous dit si «c'est plus» ou «si c'est moins» jusqu'à ce que vous ayez trouvé.
 
````

````{admonition} Exercice 2 : plus petit nombre 🔌
:class: note

Transcrire l’algorithme de l’exercice qui permet de déterminer le plus petit nombre d’une liste, en un programme Python.

````

````{admonition} Exercice 3 : tris 🔌
:class: note

Créez une liste qui contient les valeurs de 1 à n dans un ordre aléatoire, où n prend la valeur 100, par exemple. Vous pouvez utiliser la fonction shuffle() du module random.

Implémentez au moins deux des trois algorithmes de tri vu au cours.
A l’aide du module time et de sa fonction time(), chronométrez le temps prend le tri d'une liste de 100, 500, 1000, 10000, 20000, 30000, 40000 puis 50000 nombres. 

Notez les temps obtenus et affichez-les sous forme de courbe dans un tableur. Ce graphique permet de visualiser le temps d’exécution du tri en fonction de la taille de la liste. Que constatez‑vous ?

Sur la base de ces mesures, pouvez-vous estimer le temps que prendrait le tri de 100000 éléments ?

Lancez votre programme avec 100000 éléments et comparez le temps obtenu avec votre estimation.

````


````{admonition} Exercice 4 : Bogosort 🔌
:class: note

Codez l’algorithme Bogosort en Python (voir chapitre 2 : Le saviez-vous ?). 

A partir de quelle taille de liste cet algorithme est-il inutilisable ?
 
````


````{admonition} Exercice 5 : Fibonacci 🔌
:class: note

Ecrivez un algorithme qui calcule la suite des nombres de Fibonacci. 

Traduisez l’algorithme en une fonction Python. 

Comparez avec les solutions trouvées par vos camarades de classe.
````


````{admonition} Ai-je compris ?
:class: attention

1. Je sais lire et appliquer un algorithme, c’est-à dire que je peux déduire le résultat que me donnera un algorithme à partir d’un jeu de données particulier.

2. Je sais retranscrire un algorithme en un programme, je sais traduire les opérations d’un algorithme en instructions élémentaires if, else, while et for.

````


