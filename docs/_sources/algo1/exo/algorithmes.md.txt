# Algorithmique II

## 1. Les Algorithmes

### Solutions des exercices


````{exercise} 
Voir partie Apprendre.
````
````{exercise} 
Voir partie Apprendre.
````
````{exercise} 
Voir partie Apprendre.
````
````{exercise} 
Voir partie Apprendre.
````

````{exercise} Forme mystère

L’algorithme suivant contrôle un crayon. Quelle forme dessine-t-il ?
```
Répéter 8 fois :
    Avance de 2 cm
    Tourne à droite de 60°
```
````

`````{solution} 

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down


```

# import the turtle modules
import turtle
 
# Start a work Screen
ws = turtle.Screen()
 
# Define a Turtle Instance
crayon = turtle.Turtle()

crayon.speed(1)

for i in range(8):
 
    # Avance d'à peu près 2 cm
    crayon.forward(100) 

    # Tourne à droite de 60°
    crayon.right(60)

``` 

Un hexagone. Pour vérifier, exécuter le code ci-dessus. On pourrait croire que le fait de répéter l'action qui dessine une ligne 8 fois aboutit à un octogone. Cependant, pour trouver la bonne réponse il faut simuler les effets de l'algorithme sur le crayon. La forme que l'on obtient en tournant de 60° est bien un hexagone et les deux dernières lignes sont dessinées par dessus des lignes déja existantes. Si on change la valeur 8 à 6, on obtient exactement le même dessin.

````
`````


````{exercise} Nombre minimum

Ecrire un algorithme qui permet de trouver le plus petit nombre d’une liste. Penser à décomposer la solution en différentes étapes.

Appliquer votre algorithme à la liste [3, 6, 2, 8, 1, 9, 7, 5].

L'algorithme trouve-t-il la bonne solution ? Sinon, modifier votre algorithme afin qu’il trouve la bonne solution.

````

`````{solution}

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Dans un premier temps il faut pouvoir parcourir la liste de nombres.

```
Liste Nombres                               # la variable Nombres contient une liste de nombres
i ← 1

Répéter Pour i ← 1 à longueur(Nombres)      # i prend la valeur de 1, puis 2, puis 3, jusqu'à la fin de la liste  
    afficher Nombres[i]
Fin Répéter
```

Dans un deuxième temps, il nous faut une variable *Nombre_min* qui va stocker le résultat. Il faut lui donner une valeur initiale et on peut supposer que le plus petit élément est le premier élément de *Nombres*.

```
Liste Nombres                               # la variable Nombres contient une liste de nombres
i ← 1                               
Nombre_min ← Nombres[1]

Répéter Pour i ← 1 à longueur(Nombres)      # i prend la valeur de 1, puis 2, puis 3, jusqu'à la fin de la liste  
    afficher Nombres[i]
Fin Répéter
```

Finalement, l'algorithme doit comparer les nombres qu'il parcourt par rapport à la valeur de *Nombre_min*. S'il rencontre une valeur plus petite que celle stockée dans *Nombre_min*, il stocke cette nouvelle plus petite valeur dans *Nombre_min*.

```
Liste Nombres                               # la variable Nombres contient une liste de nombres
i ← 1
Nombre_min ← Nombres[1]

Répéter Pour i ← 1 à longueur(Nombres)      # i prend la valeur de 1, puis 2, puis 3, jusqu'à la fin de la liste  
    Si Nombres[i] < Nombre_min
       Nombre_min ← Nombres[i]
    Fin Si 
Fin Répéter 

Retourner Nombre_min
```

On peut encore améliorer l'algorithme. La première fois que l'algorithme passe dans la boucle *Répéter*, *Nombre_min* contient la même valeur que *Nombres[1]* et nous n'avons pas besoin de les comparer. Voici une version plus optimale de l'algorithme : 

```
Liste Nombres                               # la variable Nombres contient une liste de nombres
i ← 2
Nombre_min ← Nombres[1]

Répéter Pour i ← 2 à longueur(Nombres)      # i prend la valeur de 2, puis 3, jusqu'à la fin de la liste  
    Si Nombres[i] < Nombre_min
       Nombre_min ← Nombres[i]
    Fin Si 
Fin Répéter 

Retourner Nombre_min
```

Il faut encore vérifier que l'algorithme a bien le comportement souhaité. Voici un tableau qui tracke les valeurs des variables après chaque passage dans la boucle *Répéter* :


```{figure} media/AlgoMin.png
---
alt: Valeurs des variables de l'algorithme pour le cas où Nombres contient [3, 6, 2, 8, 1, 9, 7, 5].
width: 70%
---

```

Le résultat obtenu est bien le résultat attendu, l'algorithme a trouvé la plus petite valeur contenue dans la liste. L'algorithme est correct.

````
`````



````{exercise} Le prochain anniversaire

On souhaite déterminer l’élève dont la date d’anniversaire est la plus proche de la date d’aujourd’hui, dans le futur. Ecrire un algorithme qui permet de trouver cet élève (utiliser un langage familier). Penser à décomposer le problème en sous-problèmes. 

Comparer votre solution à celle de la personne à côté de vous. Avez-vous procédé de la même manière ? Si non, expliquer vos raisonnements.

Un ordinateur peut-il réaliser les opérations décrites par votre algorithme ?

````

`````{solution} 

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Voici une solution possible. La première étape de l'algorithme consiste à demander à chaque élève sa date de naissance.

Une autre étape de l'algorithme consiste à calculer la distance du mois de la date d'anniversaire par rapport au mois courant.

Ensuite, pour tous les élèves qui ont une distance 0 par rapport au mois courant (ils sont nés ce mois-ci), on calcule la distance du jour de leur naissance par rapport à la date d'aujourd'hui. Si cette distance est négative, leur anniversaire vient de passer et ils ne sont pas retenus. Pour les autres, on choisit l'élève avec la plus petite distance jour.

Si on se retrouve face à une liste vide (par exemple pas d'élèves nés ce mois-ci), on passe au mois d'après et on choisit l'élève avec la plus petite valeur du jour de naissance. Si on se retrouve à nouveau face à une liste vide (pas d'élèves nés le mois d'après), on passe à nouveau au mois d'après t on choisit l'élève avec la plus petite valeur du jour de naissance, et ainsi de suite.

Oui, un ordinateur peut exécuter ces opérations, mais elles doivent être décomposées davantage.

````
`````



````{exercise} Echange de trois variables

Écrire un algorithme qui effectue la permutation circulaire des variables X, Y et Z : à la fin de l’algorithme, X contient la valeur de Z, Y la valeur de X et Z la valeur de Y. Pour rappel, une variable ne peut contenir qu'une valeur à la fois.

Conseil : mettez-vous à la place de la machine et représentez le contenu de chaque variable sous la forme d'un tiroir, dessinez le tiroir avec l'étiquette et son contenu *après chaque opération de votre algorithme*. Est-ce que l'algorithme donne le résultat attendu ? Si non, modifiez votre algorithme pour qu’il résolve le problème correctement.

````

`````{solution} 

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Comme pour l'exercice 3 nous avons besoin d'une variable temporaire W pour nous souvenir de la valeur initiale de X avant qu'elle ne soit écrasée par la valeur de Y :

```
W ← X
X ← Y
Y ← Z
Z ← W
```
Supposons que X contient 1, Y contient 2 et Z contient 3. Si on dessine l’état des variables après chacune de ces opérations dans des tiroirs, voici ce que l’on obtient :

<img src="media/Swap4.png" width="45%"> &nbsp;  

Nous avons donc la confirmation que la solution obtenue résout correctement notre problème d'échange des valeurs de trois variables.

````

`````



````{exercise} Affectations

Quel est le résultat de la suite des trois affectations suivantes ? 

Vérifier votre solution en représentant chaque variable et en y mettant des valeurs fictives. Suivre les opérations dans l’ordre et dessiner le contenu des variables après chaque étape.

```
X ← X + Y
Y ← X – Y
X ← X – Y
```
````


`````{solution} 

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Imaginons que X contient 1 et Y contient 2. 

Après la première opération X ← X + Y, X vaut 1 + 2 = 3. 

Après la deuxième opération Y ← X - Y, Y vaut 3 - 2 = 1. Il faut faire attention à bien utiliser la dernière valeur stockée dans X et non sa valeur initiale.

Après la dernière opération X ← X – Y, X vaut 3 - 1 = 2. 

De manière générale, il faut remplacer les variables X et Y avec **les dernières valeurs** qu'elles contiennent :

```
X ← X + Y
Y ← (X + Y) – Y, donc Y ← X
X ← X – Y ou X ← (X + Y) - Y, donc X ← Y
```

Cet algorithme échange les valeurs des deux variables *sans avoir le besoin d'utiliser une variable temporaire*.

````
`````

