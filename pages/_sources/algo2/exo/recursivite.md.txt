# Algorithmique II

## 5. Récursivité [en option]

### Solutions des exercices


````{exercise} 
Voir partie Apprendre.
````
````{exercise} 
Voir partie Apprendre.
````

```{exercise}  Exercice 5.3. Une question de fusion

Trier le tableau suivant avec l’algorithme de tri par fusion : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```


**Solution à compléter**

````{exercise}  Exercice 5.4. Dans l'autre sens 🔌

En Python, proposer une fonction qui inverse l’ordre des lettres dans un mot. Vous pouvez parcourir les lettres du mot directement ou à travers un indice.

Proposer une autre fonction qui inverse l’ordre des lettres dans un mot de manière récursive.

````



`````{solution} 

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

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
`````




````{exercise}  Factorielle 🔌

La fonction factorielle `n!` en mathématiques est le produit de tous les nombres entiers jusqu’à `n`. C’est une des fonctions les plus simples à calculer de manière récursive. Elle peut être définie comme ceci :

	n! = (n-1)! * n

Programmer cette fonction de manière récursive en Python. Proposer également une implémentation itérative de la factorielle où les éléments de 1 à `n` sont traités l’un après l’autre.

````


`````{solution} 

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

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
`````



