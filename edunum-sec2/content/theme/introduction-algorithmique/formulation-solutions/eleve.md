Formulation de solutions algorithmiques à des problèmes simples
===============================================================

::::{admonition,note} Matière à réfléchir II

Pensez à un lieu en proximité. Décrivez les étapes qu’il faut suivre pour s’y rendre. Demandez à un camarade de classe de suivre ces instructions. Est-ce que votre camarade arrive à deviner à quel endroit il s’est rendu ?

**Si non :** recommencez l’opération en essayant de comprendre à quel moment il s’est perdu, suivez-le pas à pas. **Si oui :** reformulez vos instructions en utilisant uniquement des verbes, des distances et les mots-clés **si (if)**, **sinon (else)**, **tant que (while)**.

Imaginez que votre camarade peut uniquement exécuter l’instruction *marcher 1m tout droit* et *tourner de 5 degrés*. Reformulez votre solution en utilisant le mot clé **pendant (for)**.

::::

## De l’algorithme au programme

Une fois que l’on a determiné l’algorithme le plus adapté à utiliser, il faut le transcrire dans un programme qu’une machine peut comprendre. Nous allons détailler ce processus pour l’algorithme  du **tri par sélection**. 

Cet algorithme consiste à parcourir la liste plusieurs fois et à déterminer l’élément le plus petit. Comment pourrait-on traduire ceci en Python ? Comment représenter ces rectangles dans un langage de programmation. Ce qui nous intéresse est leur taille. On peut donc stocker les tailles de la configuration initiale de ces rectangles dans une liste :

```
rectangles = [3,4,1,2,6,5]
```

On doit ensuite trouver l’indice du rectangle le plus petit. Pour faire cela il faut parcourir la liste et comparer les différents éléments. On va stocker l’indice de l’élément le plus petit dans la variable que l’on va nommer rectangle_min. On commence par initialiser cette variable.

```
rectangle_min = 0
# trouve le rectangle le plus petit de la liste
for i in range(1:len(rectangles)):
	if rectangles[i] < rectangles[i-1] :
		rectangle_min = i
```

A la fin de cette boucle rectangle_min contient l’indice de l’élément le plus petit de la liste. On doit à ce stade, échanger cet élément et le premier élément. Comme nous avons pu le voir dans l’exercice II, il faut une variable temporaire pour échanger les valeurs de deux variables. Si on met la valeur du plus petit élément directement à la position 0, nous perdons la valeur contenue à la position 0. Il faut donc la stocker temporairement dans une autre variable :

```
# échange l’élément le plus petit et le premier élément
rectangle_temp = rectangles[0]
rectangles[0]	 = rectangles[rectangle_min]
rectangles[rectangle_min] = rectangle_temp 
```

On doit ensuite rechercher le plus petit élément de la liste en excluant le premier élément, et l’échanger avec le deuxième élément de la liste. On reprend le même code que précédemment, mais on commence à le parcours de la liste et la comparaison des éléments à 2 au lieu de 1.

```
rectangle_min = 1
# trouve le rectangle le plus petit de la liste rectangles[1:]
for i in range(2:len(rectangles)):
	if rectangles[i] < rectangles[i-1] :
		rectangle_min = i
# échange l’élément le plus petit et le deuxième élément
rectangle_temp = rectangles[1]
rectangles[1]	 = rectangles[rectangle_min]
rectangles[rectangle_min] = rectangle_temp
```

La suite de l’algorithme consiste à rechercher ensuite le plus petit élément de la liste restante, en excluant le premier et deuxième éléments et l’échanger avec le troisième élément. A nouveau on peut reprendre le même code, mais on fait incrémenter tous les indices de 1. On parcourt la liste à partir du troisième élément, donc l’élément avec un index 2. 


```
rectangle_min = 2
# trouve le rectangle le plus petit de la liste rectangles[2:]
for i in range(3:len(rectangles)):
	if rectangles[i] < rectangles[i-1] :
		rectangle_min = i
# échange l’élément le plus petit et le troisième élément
rectangle_temp = rectangles[2]
rectangles[2]	 = rectangles[rectangle_min]
rectangles[rectangle_min] = rectangle_temp
```

On détecte un pattern qui se répète. On fait toujours les même actions, mais on commence à une position différente. Plutôt que de ré-écrire le même code autant de fois que d’éléments dans la liste, (moins 1), on peut remplacer l’indice de début par une variable que l’on incrémente. 


```
# pour tous les éléments de la liste non-triée
for j in range(0,len(rectangles)-1):
	rectangle_min = j
	# trouve le rectangle le plus petit de la liste rectangles[j:]
	for i in range(j+1:len(rectangles)):
		if rectangles[i] < rectangles[i-1] :
			rectangle_min = i

# échange l’élément le plus petit et le j-ième élément
	rectangle_temp = rectangles[rectangle_min]
	rectangles[rectangle_min] = rectangles[j]
	rectangles[j] = rectangle_temp
```

Notez que cela rend le programme utilisable pour toutes les longueurs de la liste, on n’a pas besoin de savoir à l’avance combien d’éléments sont contenus dans la liste. Au lieu de répéter le code un nombre prédéterminé de fois, le code s’exécute autaut de fois qu’il y a d’éléments dans la liste (moins 1, car on compare toujours 2 éléments).

Plutôt que de définir le contenu de la liste rectangles, on peut encapsuler tout le code dans une fonction qui reçoit la liste en argument.

```
# Tri par sélection
fonction tri_selection(rectangles) :
	# pour tous les éléments de la liste non-triée
	for j in range(0,len(rectangles)-1):
		rectangle_min = j
		...
```

Finalement le terme rectangles n’est pas assez général, car le tri par sélection peut être utiliser pour trier toute sortes d’éléments. Ainsi on peut renommer les variables qui contiennent le terme rectangle par element.

```
# Tri par sélection
fonction tri_selection(elements) :
	
	# pour tous les éléments de la liste non-triée
	for j in range(0,len(elements)-1):
		element_min = j
		
		# trouve l’élément le plus petit de la liste elements[j:]
		for i in range(j+1:len(elements)):
			if elements[i] < elements[i-1] :
			element_min = i

		# échange l’élément le plus petit et le j-ième élément
		element_temp = rectangles[element_min]
		elements[element_min] = elements[j]
		elements[j] = element_temp
```

::::{admonition,attention} Exercices supplémentaires

**Exercice 1.** ![](../plugged.png) Ecrire un algorithme qui détermine si un nombre donné est positif ou négatif. Transcrire l’algorithme en un programme Python.

**Exercice 2.** ![](../plugged.png) Ecrire un algorithme qui calcule la suite de Fibonacci. Traduire l’algorithme en une fonction Python.

**Exercice 3.** ![](../plugged.png) Créer un tableau (une liste en python) qui contient les valeurs de 1 à n dans un ordre aléatoire, où n prend la valeur 100. Utiliser le module random.

Implémenter au moins deux des autres algorithmes de tri vu au cours.
A l’aide du module time, chronométrer le temps que ça prend pour trier une liste de 10, 100, 1000 et 10000 objets. 

Afficher le résultat sous forme de courbe dans un tableur : noter les temps que ça prend de trier un tableau avec 10, 100, 1000, 10000, 100000 éléments, Ce graphique qui permet de visualiser le temps d’exécution du tri en fonction de la taille de la liste.

**Exercice 4.** ![](../plugged.png) Analyser les oeuvres cubiques de Piet Mondrian. Trouver un algorithme qui permet de créer une peuvre qui pourrait être attribuées à Mondrian.

**Exercice 5.** ![](../plugged.png) Télécharger une liste des mots en français.  Imaginez plusieurs algorithmes qui permettent de parcourir cette liste au hasard (ou pas complètement au hasard) et génèrent des poèmes. Programmez-les et faites un councours de poésie numérique dans votre classe. 
::::