
Focus sur la récursivité
========================

Nous allons maintenant programmer l’algorithme du tri par fusion. Pour rappel, dans sa première phase l’algorithme divise le tableau par deux, comme illustré dans les figures du tri à fusion :

```{code-block} python
def tri_fusion(elements):

	# phase de division
	milieu = len(elements)//2	
	elements_gauche = elements[:milieu]
	elements_droite = elements[milieu:]
```

Vous pouvez imprimer l’état des variables pour une meilleure visibilité. Notez que l’on utilise une division entière, car les indices pour accéder aux éléments du tableau doivent être des entiers. Par exemple, si le tableau contient 5 éléments, cela n’aurait pas de sens de prendre les premiers 2.5 éléments.

Ce qui suit est très intéressant. Dans l’étape d’après, on procède exactement de la même manière pour les nouveaux tableaux obtenus (elements_gauche et elements_droite) - on les divise à nouveau en deux :

```{code-block} python
	# phase de division
	milieu = len(elements)//2	
	elements_gauche = tri_fusion(elements[:milieu])
	elements_droite = tri_fusion(elements[milieu:])
```

Regardez bien ce qui se passe. Nous avons fait appel à la même fonction `tri_fusion` que l’on est en train de définir ! Pour l’instant cette fonction ne fait que diviser un tableau en deux, elle va donc diviser chaque partie d’elements à nouveau en deux. La fonction `tri_fusion` appelle la fonction `tri_fusion` (donc elle-même), qui appelle aussi `tri_fusion` et ainsi de suite.

Le problème ici est que l’appel à `tri_fusion` ne s’arrête jamais. En réalité, il faut arrêter de diviser lorsque les tableaux obtenus ont au moins un élément ou lorsque les tableaux sont vides :

```{code-block} python
# phase de division (récursive) de l’algorithme de tri 
def tri_fusion(elements):

	# condition qui arrête la récursion
   if len(elements) <= 1:
		return elements
	
	# phase de division
	milieu = len(elements)//2	
	elements_gauche = tri_fusion(elements[:milieu])
	elements_droite = tri_fusion(elements[milieu:])
	return fusion(elements_gauche, elements_droite)
```

On appelle une fonction qui s’appelle elle-même une [**<span style="color:rgb(13, 204, 166)">fonction récursive</span>**. C’est une sorte de mise en abime ou une définition circulaire. Lorsqu’on entre dans la fonction, des opérations sont exécutées et on fait à nouveau [**<span style="color:rgb(13, 204, 166)">appel à la même fonction</span>**, mais avec d’autres éléments, afin de refaire les mêmes opérations (voir figure ci-dessous). 

```{figure} media/Recursivite.png
---
alt: recursivité
width: 420px
name : fig-rec
---
Schéma d’une fonction récursive
```

Le deuxième ingrédient indispensable à toute fonction récursive est la **<span style="color:rgb(13, 204, 166)">condition d’arrêt</span>** : à quel moment tous ces appels imbriqués les uns dans les autres doivent-ils s’arrêter ? Sans cette condition, le programme ne s’arrête jamais. Il est important que la condition d’arrêt précède l’appel à la fonction récursive. Pourquoi ?

A la fin du programme, nous avons rajouté une ligne de code qui correspond à la deuxième phase de l’algorithme – à la fusion des deux listes triées (voir la 2e figure du tri fusion). Il faut maintenant définir cette fonction `fusion`, que nous allons également définir de manière récursive.

```{code-block} python

# phase de fusion (récursive) de l’algorithme de tri 
def fusion(elements_gauche, elements_droite):
	
	# trouve le plus petit premier élément des deux listes
	if elements_gauche[0] < elements_droite[0]:

		# appelle fusion récursivement avec le reste des listes
		liste_reste = fusion(elements_gauche[1:], elements_droite) 
		liste_fusionnée = [elements_gauche[0]] + liste_reste
      
    else:
		# appelle fusion récursivement avec le reste des listes
		liste_reste = fusion(elements_gauche, elements_droite[1:]) 
		liste_fusionnee = [elements_droite[0]] + liste_reste

	return liste_fusionnee

```

Quelle est la différence entre le code dans la partie `if` de la condition et dans la partie `else` de la condition (relisez le 3e paragraphe de la solution de l’exercice 9) ? Lorsqu’on fusionne deux tableaux triés, on commence par prendre le plus petit des premiers éléments des deux tableaux à fusionner, que l’on met au début de notre tableau fusionné. On refait ensuite la même opération : on sélectionne le plus petit élément des éléments qui restent dans nos tableaux de départ et on le met à la suite de notre tableau fusionné. 

Dans la partie `if` de la fonction `fusion`, c’est le tableau de gauche qui contient le plus petit élément. On met cet élément au début de notre nouvelle liste fusionnée et on appelle la fonction `fusion` sur les éléments restants. Dans la partie `else` on fait la même chose, sauf que l’on commence notre tableau par le premier élément du tableau de droite. Mais qu’est-ce qui manque à cette fonction ?

Oui, vous avez raison, il manque la condition d’arrêt. Comme avant, on peut arrêter la fusion lorsqu’un des deux tableaux à fusionner est vide. Dans ce cas la solution de fusionner un tableau vide avec un autre tableau est triviale : c’est l’autre tableau (non vide).

```{code-block} python

# phase de fusion (récursive) de l’algorithme de tri 
def fusion(elements_gauche, elements_droite):

	# conditions d’arrêt de la récursivité
	if elements_gauche == []:
		return elements_droite
	if elements_droite == []:
		return elements_gauche
	
	# trouve le plus petit premier élément des deux listes
	if elements_gauche[0] < elements_droite[0]:

		# appelle fusion récursivement avec le reste des listes
		liste_reste = fusion(elements_gauche[1:], elements_droite) 
		liste_fusionnée = [elements_gauche[0]] + liste_reste
      
    else:
		# appelle fusion récursivement avec le reste des listes
		liste_reste = fusion(elements_gauche, elements_droite[1:]) 
		liste_fusionnee = [elements_droite[0]] + liste_reste

	return liste_fusionnee

```

Ces deux fonctions implémentent l’algorithme de tri par fusion de manière récursive. La récursivité est un concept difficile à appréhender. Le mieux c’est d’essayer de coder des algorithmes récursifs et d’afficher ce qui se passe au fur et à mesure.

````{admonition}  Exercice 13 ![](media/plugged.png)
:class: note

La fonction factorielle `n!` en mathématiques est le produit de tous les nombres entiers jusqu’à `n`. C’est une des fonctions les plus simples à calculer de manière récursive. Elle peut être définie comme ceci :

	n! = (n-1)! * n

Programmer cette fonction de manière récursive en Python. Proposer également une implémentation itérative de la factorielle où les éléments de 1 à `n` sont traités l’un après l’autre.

````

````{admonition}  Exercice 14 ![](media/plugged.png)

En Python, proposer une fonction qui inverse l’ordre des lettres dans un mot. Vous pouvez parcourir les lettres du mot directement ou à travers un indice.

Proposer une autre fonction qui inverse l’ordre des lettres dans un mot de manière récursive.

````

````{admonition} Exercice 15 ![](media/plugged.png)
:class: note

Les fractales sont des objets géométriques, dont la définition récursive est naturelle. Essayer le code suivant pour différentes valeurs de `n` (augmenter à chaque fois de 1). 

Essayez de comprendre comment le flocon se construit, de manière récursive. Vous pouvez aussi varier la longueur du segment dessiné et la vitesse d’affichage en décommentant la ligne correspondante.


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

turtle.hideturtle() 	# cache la tortue
# turtle.speed(0)	 	# ACCELERE LA TORTUE
turtle.forward(-10) 	# positionne la tortue en haut à gauche
turtle.left(150)
turtle.forward(150)
window = turtle.Screen()
window.bgcolor("black")	# tableau noir
turtle.color("white")	# dessine avec une trace blanche
turtle.setheading(0)     # orientation initiale de la tête : droite

n = 1                   # AUGMENTER ICI
segment = 300           # DIMINUER ICI

flocon(n, segment)

turtle.exitonclick()	 # garde la fenêtre ouverte


```

````


````{admonition} Exercice 16 ![](media/plugged.png)
:class: note


Implémenter l’algorithme du tri rapide de manière récursive, puis comparer sa vitesse à celle de l’algorithme du tri par sélection.

````

## Solutions des exercices

````{admonition} Solutions de l'exercice 13
:class: note

Voici une implémentation en Python de la fonction factorielle où la fonction fait appel à elle-même, sans oublier la condition d’arrêt  :

```{codeplay}
# fonction factorielle (définition récursive)
def factorielle_recursive(nombre):

	if nombre == 1:
		res = 1
	else:
		res = nombre * factorielle_recursive(nombre-1)

	return res

res = factorielle_recursive(5)
print(res)

```

Voici une implémentation en Python de la fonction factorielle qui n’est pas récursive :

```{codeplay}

def factorielle(nombre):
	res = 1
	for n in range(2,nombre+1) :
		res = res * n
	return res

res = factorielle(5)
print(res)

```

````

````{admonition} Solution de l'exercice 14
:class: note

Voici plusieurs implémentations itératives et une récursive de la fonction qui inverse un mot :

```{codeplay}

def inverser_mot_iteratif(mot) :
	mot_inverse = ""
	for lettre in mot :
		mot_inverse = lettre + mot_inverse
	return mot_inverse

def inverser_mot_iteratif_2(mot) :
	mot_inverse = ""
	for indice in range(len(mot)-1,-1,-1) :
		mot_inverse += mot[indice] 
	return mot_inverse

def inverser_mot_recursif(mot) :
	if len(mot) == 1:
		return mot
	else :
		return inverser_mot_recursif(mot[1:]) + mot[0] 

un_mot = "mot"

print(inverser_mot_iteratif(un_mot))
print(inverser_mot_iteratif_2(un_mot))
print(inverser_mot_recursif(un_mot))

```

````

````{admonition} Solution de l'exercice 16
:class: note

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
    


def tri_fusion(elements):
    
    if len(elements)<=1:
        print("4. tri fusion condition d'arret, retourne : ", elements)
        return elements

    print("1. tri fusion appelee pour : ", elements)
    milieu=len(elements)//2
    print("2. tri fusion appelee a gauche avec : ", elements[:milieu], "pour", elements)
    elements_gauche=tri_fusion(elements[:milieu])
    print("3. tri fusion appelee a droite avec : ", elements[milieu:], "pour", elements)
    elements_droite=tri_fusion(elements[milieu:])

    print("5. fonction fusion appelee avec : ", elements_gauche, elements_droite)
    return fusion(elements_gauche, elements_droite)

elements=list(range(10,0,-1))
print(tri_fusion(elements))

```

````



*******************
*******************


````{admonition} Matière à réfléchir VI
:class: attention

Vous avez décidé de faire le tour du monde. Choisissez 5 pays que vous souhaitez visiter et placez-les sur une carte. Essayez de trouver le meilleur itinéraire pour visiter ces 5 pays. Quels critères avez-vous pris en compte pour décider du meilleur itinéraire, c’est-à-dire un itinéraire qui minimise la distance parcourue ?

Vous avez décidé de visiter 10 pays. Est-ce qu’il est aussi facile de trouver un itinéraire optimal ?

Imaginez que vous souhaitez visiter plus de la moitié des pays du monde, environ 100. Combien y a-t‑il d’itinéraires possibles ?  Comment s’appelle ce nombre ?

Si le calcul d’un itinéraire prenait 1 milliseconde, combien de temps faudrait-il pour trouver la meilleure solution en énumérant toutes les solutions possibles ? Pour comparaison, le nombre d’atomes dans l’univers est d’ordre 10<sup>80</sup>.

````