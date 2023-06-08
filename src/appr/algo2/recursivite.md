
# Récursivité [niveau avancé]

Ce chapitre est prévu en tant que chapitre optionnel. Il présente un autre algorithme de tri célèbre, le **<span style="color:rgb(89, 51, 209)">Tri par fusion</span>**. Cet algorithme utilise la **<span style="color:rgb(89, 51, 209)">récursivité</span>**, une stratégie qui consiste en ce qu'un algorithme s'invoque lui&#8209;même. La récursivité, c'est un peu comme si on essayait de définir le terme « définition » en disant c'est une phrase qui nous donne la définition de quelque chose. C'est certes circonvolu que de vouloir utiliser dans une définition *la chose&#8209;même* que l'on est en train de définir, mais si on respecte quelques conditions, « ça fonctionne » ! 

## Tri par fusion

Un autre {glo}`algo|algorithme` de tri célèbre, inventé par John von Neumann en 1945, est le **<span style="color:rgb(89, 51, 209)">Tri par fusion</span>**. L’algorithme se base sur l’idée qu’il est difficile de trier un tableau avec beaucoup d'éléments, mais qu’il est très facile de trier un tableau avec juste deux éléments. Il suffit ensuite de fusionner les plus petits tableaux déjà triés.

<span id="diviser"></span>L’algorithme commence par une phase de ***<span style="color:rgb(13, 204, 166)">division</span>*** : on divise le tableau en deux, puis on divise *à nouveau* les tableaux ainsi obtenus en deux, et ceci jusqu’à arriver à des tableaux avec un seul élément (voir la figure ci&#8209;dessous). Comme pour la recherche&nbsp;binaire, le nombre d’étapes nécessaires pour arriver à des tableaux de $1$&nbsp;élément, en divisant toujours par deux, est $log(n)$.

```{figure} media/Tri_fusion_diviser.png
---
alt: phase de division dans le Tri par fusion
width: 500px
name : fig-div-fus
---
**Phase de division.** Illustration de la première phase du Tri par fusion : on commence par diviser le tableau en deux, puis à&nbsp;chaque étape on divise à nouveau les tableaux ainsi obtenus par deux, jusqu’à ce qu’il n'y ait plus que des tableaux à $1$&nbsp;élément.
```


La deuxième phase de ***<span style="color:rgb(13, 204, 166)">fusion</span>*** commence par fusionner des paires de tableaux à un élément, dans un ***ordre trié***. Il suffit d’assembler les deux éléments du plus petit au plus grand, comme on peut le voir sur la 2ème ligne de la figure ci&#8209;dessous. Dans les prochaines étapes, on continue à fusionner les tableaux par paires de deux, tout en respectant l'ordre de tri (lignes 3 et 4 de la figure). On continue de la sorte jusqu’à ce qu’il n'y  ait plus de tableaux à fusionner. 



```{figure} media/Tri_fusion_fusionner.png
---
alt: phase de fusion dans le tri fusion
width: 500px
name : fig-fus-fus
---
**Phase de fusion.** Illustration de la deuxième phase du Tri par fusion : on commence par fusionner les tableaux à un élément, en faisant attention à respecter l’ordre de tri (ligne 2) ; puis par fusionner à nouveau les tableaux obtenus à l'étape précédente, toujours en respectant l’ordre de tri (lignes 3 et 4). On continue de la sorte jusqu’à ce qu’il n'y ait plus qu'un tableau unique (ligne 4).
```

<span id="fusionner"></span>La fusion de tableaux **déjà triés**, par rapport à des tableaux non&#8209;triés, est très facile. Il suffit de comparer les premiers éléments des deux tableaux à fusionner et de prendre le plus petit des deux. Concrètement, on enlève le plus petit élément des deux tableaux pour le mettre dans le nouveau tableau fusionné. On compare ensuite les premiers éléments de ceux qui restent dans les tableaux à fusionner et on prend à nouveau le plus petit des deux pour le mettre à la suite dans le tableau fusionné. 

Chaque étape de la phase de fusion consiste à comparer deux éléments $n$&nbsp;fois, autant de fois qu’il y a d’éléments à fusionner. Le temps de calcul grandit donc linéairement en fonction de la taille du tableau n (plus il y a d’éléments dans le tableau, plus la fusion prend du temps). En tout il y a besoin de $log(n)$&nbsp;étapes (fusion deux&nbsp;par&nbsp;deux), dont chacune prend un temps qui dépend de&nbsp;$n$, ce qui nous donne un ordre de complexité&nbsp;linéarithmique.


## Focus sur la récursivité

<span id="recursivite"></span>Nous allons maintenant programmer l’{glo}`algo|algorithme` du Tri par fusion. Pour rappel, la première phase de l’{glo}`algo|algorithme` divise *continuellement* le tableau par deux, comme illustré dans la première <a href="#diviser">figure</a> ci&#8209;dessus. Voici le code qui permet de diviser un tableau en deux une seule fois :

```{code-block} python
# Tri&nbsp;par&nbsp;fusion 
def tri_par_fusion(elements):

	### Phase DIVISION

	# détermine l'indice au milieu du tableau (division entière)
	milieu = len(elements)//2	
	
	# prend tous les éléments depuis le début, jusqu'à (et sans) milieu
	elements_gauche = elements[:milieu]

	# prend tous les éléments depuis le milieu (y compris), jusqu'à la fin
	elements_droite = elements[milieu:]
```

La division utilisée pour déterminer le milieu du tableau est une division entière `//` au lieu de `/`. En effet, on souhaite obtenir un résultat entier et non un nombre à virgule, car les indices pour accéder aux éléments du tableau doivent être des entiers. Par exemple, si le tableau contient `5`&nbsp;éléments, cela n’aurait pas de sens de prendre les premiers `2.5`&nbsp;éléments, et `5//2` nous retournerait `2`.

Ce qui suit est très intéressant. Dans l’étape d’après, on souhaite faire exactement la même chose pour les nouveaux tableaux `elements_gauche` (équivalent à `elements[:milieu]`) et `elements_droite` (équivalent à `elements[milieu:]`), c'est&#8209;à&#8209;dire que l'on souhaite à nouveau les diviser en deux, comme sur la deuxième ligne dans la première <a href="#diviser">figure</a>  ci&#8209;dessus. On va donc appeler la fonction `tri_par_fusion` sur les deux moitiés de tableaux :


```{code-block} python
	# prend tous les éléments depuis le début, jusqu'à (et sans) milieu
	elements_gauche = tri_par_fusion(elements[:milieu])

	# prend tous les éléments depuis le milieu (y compris), jusqu'à la fin
	elements_droite = tri_par_fusion(elements[milieu:])
```

Regardez bien ce qui se passe. Nous avons fait appel à la même {glo}`fonction|fonction` `tri_par_fusion` que l’on est en train de définir ! Pour l’instant cette fonction ne fait que diviser le tableau `elements` en deux, elle va donc diviser le tableau reçu en entrée en deux. Au début le tableau en entrée sera le tableau entier, mais ensuite il s'agira des deux moitiés du tableau, puis des moitiés de la moitié et ainsi de suite. La fonction `tri_par_fusion` appelle la fonction `tri_par_fusion` (elle s'appelle donc elle&#8209;même), qui va à nouveau s'appeler et ainsi de suite...

Si on laisse le programme tel quel, on est face à un problème. La fonction `tri_par_fusion` continue de s'appeler elle&#8209;même et ce processus ne s’arrête jamais. En réalité, il faut arrêter de diviser lorsque les tableaux obtenus ont au moins un élément ou lorsqu'ils sont vides, car dans ces cas on ne peut plus les diviser en deux. On rajoute donc cette **<span style="color:rgb(89, 51, 209)">condition d'arrêt</span>** de la récursion :

```{code-block} python
	# condition d'arrêt la récursion
	if len(elements) <= 1:
		return(elements)
	
	# détermine l'indice au milieu du tableau (division entière)
	milieu = len(elements)//2	
	
	# prend tous les éléments depuis le début, jusqu'à (et sans) milieu
	elements_gauche = tri_par_fusion(elements[:milieu])

	# prend tous les éléments depuis le milieu (y compris), jusqu'à la fin
	elements_droite = tri_par_fusion(elements[milieu:])
```

Voici le programme appliqué sur l'exemple de la figure. Essayez de comprendre dans quel ordre sont appelées les fonctions `tri_par_fusion` et avec quel paramètre en entrée. Pour une meilleure visibilité, nous affichons l’état des {glo}`variable|variables` avec `print`. 


```{codeplay}
# Tri&nbsp;par&nbsp;fusion : phase de division
def division(elements, ligne, side=0):

	# nous dit où on en est
	print("Appel de la fonction division avec ", str(elements), "ligne", ligne, "depuis", side)

	# correspond à la ligne sur la figure division du tri&nbsp;par&nbsp;fusion
	ligne = ligne + 1

	# condition d'arrêt la récursion
	if len(elements) <= 1:
		return(elements)

	# détermine l'indice au milieu du tableau (division entière)
	milieu = len(elements)//2	

	# prend tous les éléments depuis le début, jusqu'à (et sans) milieu
	elements_gauche = division(elements[:milieu], ligne, 'gauche')
	if elements_gauche :
		print('Eléments à gauche : ', elements_gauche, 'de :', elements, "ligne", ligne)

	# prend tous les éléments depuis le milieu (y compris), jusqu'à la fin
	elements_droite = division(elements[milieu:], ligne, 'droite')
	if elements_droite :
		print('Eléments à droite : ', elements_droite, 'de :', elements, "ligne", ligne)

division([3,5,1,2,6,4], 0)
```


<!-- 	return fusion(elements_gauche, elements_droite) -->

Une {glo}`fonction|fonction` qui s’appelle elle&#8209;même est appelée **<span style="color:rgb(89, 51, 209)">{glo}`fonctionrec|fonction récursive`</span>**. Il s'agit d'une *mise en abime*, d'une *définition circulaire*. Lorsqu’on entre dans la fonction, des opérations sont exécutées et on fait à nouveau ***<span style="color:rgb(13, 204, 166)">appel à la même fonction</span>***, mais cette fois&#8209;ci avec  ***<span style="color:rgb(13, 204, 166)">d’autres éléments en entrée</span>***, afin de refaire les mêmes opérations, comme le montre cette figure :

```{figure} media/Recursivite.png
---
alt: recursivité
width: 800px
name : fig-rec
---
**Schéma d’une fonction récursive**. La fonction s'appele elle&#8209;même. toujours avec un autre paramètre en entrée, jusqu'à ce que la condition d'arrêt soit remplie. A&nbsp;ce moment&#8209;là, un résultat est calculé et retourné à la fonction du dessus (celle qui à appelé la fonction). Ainsi tous les résultats sont retournés au fur et à mesure et permettent de calculer la fonction souhaitée.
```

Les deux ingrédients indispensables à toute {glo}`fonctionrec|fonction récursive` sont donc :

1. un **<span style="color:rgb(13, 204, 166)">appel à la fonction elle&#8209;même</span>** à l'intérieur de la définition de la fonction.

2. une **<span style="color:rgb(13, 204, 166)">condition d’arrêt</span>**, qui permet de terminer les appels imbriqués.



```{exercise} Position de la condition d'arrêt

Sans la condition d'arrêt, un programme récursif ne se termine pas, et s'appelle soi&#8209;même indéfiniment. Il est important que cette condition d’arrêt précède l’appel récursif à la fonction. Pourquoi est&#8209;ce le cas ?

```

````{solution} 

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Si la condition d'arrêt est après l'appel à la fonction, la fonction est appelée avant d'avoir pu vérifié si la condition d'arrêt est remplie. Dans ce cas, la condition d'arrêt n'est jamais testée.

```
````


Maintenant que nous avons programmé la première phase de division du Tri par fusion il nous faut programmer la deuxième phase de fusion (voir la deuxième <a href="fusionner">figure</a> du Tri par fusion). Nous allons définir cette phase de fusion de manière récursive :


```{code-block} python

# Phase de fusion du Tri&nbsp;par&nbsp;fusion
def fusion(elements_gauche, elements_droite):
	
	# trouve le plus petit premier élément des deux listes
	if elements_gauche[0] < elements_droite[0]:
		
		# appelle fusion récursivement avec le reste des listes
		elements_reste = fusion(elements_gauche[1:], elements_droite) 
		
		# crée une liste fusionnée avec le résultat
		elements_fusion = [elements_gauche[0]] + elements_reste
		
	else:
		
		# appelle fusion récursivement avec le reste des listes
		elements_reste = fusion(elements_gauche, elements_droite[1:]) 
		
		# crée une liste fusionnée avec le résultat
		elements_fusion = [elements_droite[0]] + elements_reste
		
	return(elements_fusion)
```

Quelle est la différence entre le code dans la partie `if` de la condition et dans la partie `else` de la condition ? Lorsqu’on fusionne deux tableaux qui sont **déjà triés**, le plus petit élément se trouve parmi les premiers éléments des deux tableaux à fusionner. On commence alors par prendre le plus petit des premiers éléments des deux tableaux à fusionner, que l’on met au début de notre tableau fusionné. On refait ensuite la même opération avec le reste des éléments : on sélectionne le plus petit élément des tableaux de départ et on le met à la suite de notre tableau fusionné. On recommence de la sorte tant qu'il n'y ait plus d'éléments dans les tableaux.

Dans la partie `if` de la fonction `fusion`, c’est le tableau de gauche qui contient le plus petit élément. On prend cet élément pour le mettre au début d'un nouveau tableau fusionné et on appelle la fonction `fusion` sur les éléments restants. Dans la partie `else` on fait la même chose, sauf que l’on commence notre tableau fusionné par le premier élément du tableau de droite. 

Mais&nbsp;n'y a&#8209;t&#8209;il pas quelque chose qui manque à cette fonction ? En&nbsp;effet, il manque la condition d’arrêt. Il faut arrêter la fusion lorsqu’un des deux tableaux à fusionner est vide. Dans ce cas la solution de fusionner un tableau vide avec un autre tableau est triviale : c’est l’autre tableau non vide. Mettons ceci sous forme de code :


```{code-block} python

# Phase de fusion du Tri&nbsp;par&nbsp;fusion
def fusion(elements_gauche, elements_droite):

	# conditions d’arrêt de la récursivité
	if elements_gauche == []:
		return(elements_droite)
	if elements_droite == []:
		return(elements_gauche)
	
	# trouve le plus petit premier élément des deux listes
	if elements_gauche[0] < elements_droite[0]:

		# appelle fusion récursivement avec le reste des listes
		elements_reste = fusion(elements_gauche[1:], elements_droite) 
		
		# crée une liste fusionnée avec le résultat
		elements_fusion = [elements_gauche[0]] + elements_reste
		
	else:
		
		# appelle fusion récursivement avec le reste des listes
		elements_reste = fusion(elements_gauche, elements_droite[1:]) 
		
		# crée une liste fusionnée avec le résultat
		elements_fusion = [elements_droite[0]] + elements_reste

	return(elements_fusion)
```

Pour que le programme soit complet, il faut faire appel cette fonction `fusion` dans la fonction `tri_fusion` ci&#8209;dessus :

```{code-block} python

# Phase de division du Tri&nbsp;par&nbsp;fusion
def tri_par_fusion(elements):

	### Phase DIVISION

	# condition d'arrêt la récursion
	if len(elements) <= 1:
		return(elements)
	
	# détermine l'indice au milieu du tableau (division entière)
	milieu = len(elements)//2	
	
	# prend tous les éléments depuis le début, jusqu'à (et sans) milieu
	elements_gauche = tri_par_fusion(elements[:milieu])

	# prend tous les éléments depuis le milieu (y compris), jusqu'à la fin
	elements_droite = tri_par_fusion(elements[milieu:])

	# fusionne les éléments un par un, puis deux par deux, etc..
	resultat = fusion(elements_gauche, elements_droite)

	# retourner le résultat
	return(resultat)
```


Ces deux {glo}`fonction|fonctions` `fusion` et `division` ensemble implémentent l’{glo}`algo|algorithme` du Tri par fusion de manière {glo}`recursivite|récursive`. La {glo}`recursivite|récursivité` est un concept difficile à appréhender. Le mieux est d’essayer de coder différents {glo}`algo|algorithmes` {glo}`recursivite|récursifs` et d’afficher ce qui se passe au fur et à mesure. Voici le programme du tri&nbsp;par&nbsp;fusion :


```{codeplay}
# TRI PAR FUSION

# Phase de fusion 
def fusion(elements_gauche, elements_droite):

	# conditions d’arrêt de la récursivité
	if elements_gauche == []:
		print("\n4. Tableau gauche vide :", elements_droite)
		return(elements_droite)
	if elements_droite == []:
		print("\n5. Tableau droite vide :", elements_droite)
		return(elements_gauche)
	
	# trouve le plus petit premier élément des deux listes
	if elements_gauche[0] < elements_droite[0]:

		# appelle fusion récursivement avec le reste des listes
		elements_reste = fusion(elements_gauche[1:], elements_droite) 
		
		# crée une liste fusionnée avec le résultat
		elements_fusion = [elements_gauche[0]] + elements_reste

		# affiche ce qui se passe
		print("\n6. Retour fusion :", [elements_gauche[0]], '+', elements_reste)
		
	else:
		
		# appelle fusion récursivement avec le reste des listes
		elements_reste = fusion(elements_gauche, elements_droite[1:]) 
		
		# crée une liste fusionnée avec le résultat
		elements_fusion = [elements_droite[0]] + elements_reste

		# affiche ce qui se passe
		print("\n7. Retour fusion :", [elements_droite[0]], '+', elements_reste)

	# retourner le résultat
	return(elements_fusion)
```

La fonction `division` s'appelle aussi elle&#8209;même, mais appelle également la fonction&nbsp;`fusion` précédemment définie : 

```{codeplay}
# TRI PAR FUSION

# Phase de division
def division(elements, ligne, side=0):

	# nous dit où on en est
	print("\n1. Appel de la fonction division avec ", str(elements), "ligne", ligne, "depuis", side)

	# correspond à la ligne sur la figure division du tri&nbsp;par&nbsp;fusion
	ligne = ligne + 1

	# condition d'arrêt la récursion
	if len(elements) <= 1:
		return(elements)

	# détermine l'indice au milieu du tableau (division entière)
	milieu = len(elements)//2	

	# prend tous les éléments depuis le début, jusqu'à (et sans) milieu
	elements_gauche = division(elements[:milieu], ligne, 'gauche')
	if elements_gauche :
		print('\n2. Eléments à gauche : ', elements_gauche, 'de :', elements, "ligne", ligne)

	# prend tous les éléments depuis le milieu (y compris), jusqu'à la fin
	elements_droite = division(elements[milieu:], ligne, 'droite')
	if elements_droite :
		print('\n3. Eléments à droite : ', elements_droite, 'de :', elements, "ligne", ligne)

	# fusionne les éléments un par un, puis deux par deux, etc..
	resultat = fusion(elements_gauche, elements_droite)

	# retourner le résultat
	return(resultat)

resultat = division([3,5,1,2,6,4], 0)

print("\nVoici le tableau trié : ", resultat)
```
## Exercices 

````{exercise} Fractale 🔌

Une fractale est un objet géométrique, dont la définition récursive est naturelle. Essayez le code suivant pour différentes valeurs de $n$ (augmenter à&nbsp;chaque fois de $1$). 

Essayez de comprendre comment le flocon se construit de manière **récursive**. Vous pouvez aussi varier la longueur du segment dessiné et la vitesse d’affichage en décommentant la ligne correspondante.

```{codeplay}
import turtle

def courbeKoch(n, segment) :
	if n == 0 :
		turtle.forward(segment)
	else :
		courbeKoch(n-1, segment/3)
		turtle.left(60)
		courbeKoch(n-1, segment/3)
		turtle.left(-120)
		courbeKoch(n-1, segment/3)
		turtle.left(60)
		courbeKoch(n-1, segment/3)

def flocon(n, segment) :
	for i in range(3) :
		courbeKoch(n, segment)
		turtle.left(-120)

turtle.hideturtle() 		# cache la tortue
# turtle.speed(0)			# ACCELERE LA TORTUE
turtle.forward(-10) 		# positionne la tortue en haut à gauche
turtle.left(150)
turtle.forward(150)
window = turtle.Screen()
window.bgcolor("black")		# tableau noir
turtle.color("white")		# dessine avec une trace blanche
turtle.setheading(0)     	# orientation initiale de la tête : droite

# AUGMENTER ICI
n = 1        
# DIMINUER ICI
segment = 300           
flocon(n, segment)		 # dessine le flocon
turtle.exitonclick()	 # garde la fenêtre ouverte
```
````





```{exercise} Une question de fusion

Trier le tableau suivant avec l’algorithme de tri&nbsp;par&nbsp;fusion : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```


````{exercise} Dans l'autre sens 🔌

En Python, proposer une fonction qui inverse l’ordre des lettres dans un mot. Vous pouvez parcourir les lettres du mot directement ou à travers un indice.

Proposer une autre fonction qui inverse l’ordre des lettres dans un mot de manière récursive.

````




````{exercise} Factorielle 🔌

La fonction factorielle $n!$ en mathématiques est le produit de tous les nombres entiers jusqu’à $n$. C’est une des fonctions les plus simples à calculer de manière récursive. Elle peut être définie comme ceci :

$n! = (n-1)! * n$

Programmer cette fonction de manière récursive en Python. Proposer également une implémentation itérative de la factorielle où les éléments de $1$ à $n$ sont traités l’un après l’autre.

````







<!-- ````{admonition} Exercice 4 : tri rapide récursif 🔌
:class: note


Implémenter l’algorithme du tri rapide de manière récursive, puis comparer sa vitesse à celle de l’algorithme du tri&nbsp;par&nbsp;sélection.

````


`````{admonition} Solution
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

```{codeplay}

def fusion(elements_gauche, elements_droite):
    
    if elements_gauche == []:
        print("8. fusion avec elements a gauche vide, retourne : ", elements_droite)
        return elements_droite
    if elements_droite == []:
        print("9. fusion avec elements a droite vide, retourne ", elements_gauche)
        return elements_gauche

    if elements_gauche[0]<elements_droite[0]:
        print("6. fusion de ", elements_gauche[0], "avec fusion de ", elements_gauche[1:], elements_droite)
        liste_reste=fusion(elements_gauche[1:], elements_droite)
        liste_fusionnee= [elements_gauche[0]]+liste_reste
    else:
        print("7. fusion de ", elements_droite[0], "avec fusion de ", elements_gauche, elements_droite[1:])
        liste_reste=fusion(elements_gauche,elements_droite[1:])
        liste_fusionnee=[elements_droite[0]]+liste_reste
        
    print("10. fusion retourne", liste_fusionnee)
    return liste_fusionnee
    


def tri_par_fusion(elements):
    
    if len(elements)<=1:
        print("4. tri fusion condition d'arret, retourne : ", elements)
        return elements

    print("1. tri fusion appelee pour : ", elements)
    milieu=len(elements)//2
    print("2. tri fusion appelee a gauche avec : ", elements[:milieu], "pour", elements)
    elements_gauche=tri_par_fusion(elements[:milieu])
    print("3. tri fusion appelee a droite avec : ", elements[milieu:], "pour", elements)
    elements_droite=tri_par_fusion(elements[milieu:])

    print("5. fonction fusion appelee avec : ", elements_gauche, elements_droite)
    return fusion(elements_gauche, elements_droite)

elements=list(range(10,0,-1))
print(tri_par_fusion(elements))

```
````
````` -->





