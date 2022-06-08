

## Solutions des exercices

### 1. Les algorithmes

````{admonition} Exercice 4. Forme mystère
:class: note

L’algorithme suivant contrôle un crayon. Quelle forme dessine-t-il ?
```
Répéter 8 fois :
    Avance de 2 cm
    Tourne à droite de 60°
```
````

`````{admonition} Solution 4. Forme mystère
:class: hint

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


````{admonition} Exercice 5. Nombre minimum
:class: note

Ecrire un algorithme qui permet de trouver le plus petit nombre d’une liste. Penser à décomposer la solution en différentes étapes.

Appliquer votre algorithme à la liste [3, 6, 2, 8, 1, 9, 7, 5].

L'algorithme trouve-t-il la bonne solution ? Sinon, modifier votre algorithme afin qu’il trouve la bonne solution.

````

`````{admonition} Solution 5. Nombre minimum
:class: hint

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



````{admonition} Exercice 6. Le prochain anniversaire
:class: note

On souhaite déterminer l’élève dont la date d’anniversaire est la plus proche de la date d’aujourd’hui, dans le futur. Ecrire un algorithme qui permet de trouver cet élève (utiliser un langage familier). Penser à décomposer le problème en sous-problèmes. 

Comparer votre solution à celle de la personne à côté de vous. Avez-vous procédé de la même manière ? Si non, expliquer vos raisonnements.

Un ordinateur peut-il réaliser les opérations décrites par votre algorithme ?

````

`````{admonition} Solution 6. Le prochain anniversaire
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Voici une solution possible. La première étape de l'algorithme consiste à demander à chaque élève sa date de naissance.

Une autre étape de l'algorithme consiste à calculer la distance du mois de la date d'anniversaire par rapport au mois courant.

Ensuite, pour tous les élèves qui ont une distance 0 par rapport au mois courant (ils sont nés ce mois-ci), on calcule la distance du jour de leur naissance par rapport à la date d'aujourd'hui. Si cette distance est négative, leur anniversaire vient de passer et ils ne sont pas retenus. Pour les autres, on choisit l'élève avec la plus petite distance jour.

Si on se retrouve face à une liste vide (par exemple pas d'élèves nés ce mois-ci), on passe au mois d'après et on choisit l'élève avec la plus petite valeur du jour de naissance. Si on se retrouve à nouveau face à une liste vide (pas d'élèves nés le mois d'après), on passe à nouveau au mois d'après t on choisit l'élève avec la plus petite valeur du jour de naissance, et ainsi de suite.

Oui, un ordinateur peut exécuter ces opérations, mais elles doivent être décomposées davantage.

````
`````



````{admonition} Exercice 7. Echange de trois variables
:class: note

Écrire un algorithme qui effectue la permutation circulaire des variables X, Y et Z : à la fin de l’algorithme, X contient la valeur de Z, Y la valeur de X et Z la valeur de Y. Pour rappel, une variable ne peut contenir qu'une valeur à la fois.

Conseil : mettez-vous à la place de la machine et représentez le contenu de chaque variable sous la forme d'un tiroir, dessinez le tiroir avec l'étiquette et son contenu *après chaque opération de votre algorithme*. Est-ce que l'algorithme donne le résultat attendu ? Si non, modifiez votre algorithme pour qu’il résolve le problème correctement.

````

`````{admonition} Solution 7. Echange de trois variables
:class: hint

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



````{admonition} Exercice 8. Affectations
:class: note

Quel est le résultat de la suite des trois affectations suivantes ? 

Vérifier votre solution en représentant chaque variable et en y mettant des valeurs fictives. Suivre les opérations dans l’ordre et dessiner le contenu des variables après chaque étape.

```
X ← X + Y
Y ← X – Y
X ← X – Y
```
````


`````{admonition} Solution 8. Affectations
:class: hint

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


### 2. Trie, cherche et trouve


````{admonition} Exercice 4. L'algorithme de votre journée
:class: note

Réfléchissez à votre journée : y a-t-il des actions qui se retrouvent chaque jour ouvrable ? Arrivez-vous à esquisser un algorithme que vous suivez sans que vous en ayez conscience ?

````

`````{admonition} Solution 4. L'algorithme de votre journée
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Cela pourrait ressembler à ça :

```
Se lever
Répéter pour i = 1 à 3
    Faire des étirements
Fin Pour
Prendre une douche
Prendre un petit-déjener
Se brosser les dents
Aller au Gymnase
Répéter pour i = 1 à 5
    Suivre un cours
Fin Pour
Déjeuner
Répéter pour i = 1 à 5
    Suivre un cours
Fin Pour
Rentrer à la maison
Dîner
Lire un livre
Se brosser les dents
Se coucher
```
````
`````

````{admonition} Exercice 5. Trois algorithmes de tri
:class: note


Trier la liste [2,5,3,4,7,1,6] en utilisant les trois algorithmes de tri vus adans le cours. Représenter l’état de la liste après chaque étape.

````

`````{admonition} Solution 5. Trois algorithmes de tri
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Voici le détail de toutes les étapes intermédiaires des trois algorithmes de tri.

**<span style="color:rgb(89, 51, 209)">Tri par insertion</span>** : 

```
[2,5,3,4,7,1,6]  # on considère le 2e élément et on l'ordonne par rapport au premier élément
[2,5,3,4,7,1,6]  # on considère le 3e élément et on l'ordonne par rapport aux deux premiers éléments
[2,3,5,4,7,1,6]  # on considère le 4e élément et on l'insère au bon endroit du tableau déjà trié
[2,3,4,5,7,1,6]  # on considère le 5e élément et on l'insère au bon endroit du tableau déjà trié
[2,3,4,5,7,1,6]  # on considère le 6e élément et on l'insère au bon endroit du tableau déjà trié
[1,2,3,4,5,7,6]  # on considère le 7e élément et on l'insère au bon endroit du tableau déjà trié
[1,2,3,4,5,6,7]
```
**<span style="color:rgb(89, 51, 209)">Tri par sélection</span>** : 

```
[2,5,3,4,7,1,6]  # on sélectionne le plus petit élément et on l'échange avec le premier élément
[1,5,3,4,7,2,6]  # on sélectionne le 2e plus petit élément et on l'échange avec le 2e élément 
[1,2,3,4,7,5,6]  # on sélectionne le 3e plus petit élément et on l'échange avec le 3e élément 
[1,2,3,4,7,5,6]  # on sélectionne le 4e plus petit élément et on l'échange avec le 4e élément 
[1,2,3,4,5,7,6]  # on sélectionne le 5e plus petit élément et on l'échange avec le 5e élément 
[1,2,3,4,5,6,7]  # on sélectionne le 6e plus petit élément et on l'échange avec le 6e élément 
```

**<span style="color:rgb(89, 51, 209)">Tri à bulles</span>** : 

```
[2,5,3,4,7,1,6]  # on compare 2 et 5
[2,5,3,4,7,1,6]  # on compare 5 et 3 et on les déplace
[2,3,5,4,7,1,6]  # on compare 5 et 4 et on les déplace
[2,3,4,5,7,1,6]  # on compare 5 et 7
[2,3,4,5,7,1,6]  # on compare 7 et 1 et on les déplace
[2,3,4,5,1,7,6]  # on compare 7 et 6 et on les déplace, tableau trié [7]
[2,3,4,5,1,6,7]  # on compare 2 et 3
[2,3,4,5,1,6,7]  # on compare 3 et 4
[2,3,4,5,1,6,7]  # on compare 4 et 5
[2,3,4,1,5,6,7]  # on compare 5 et 1 et on les déplace
[2,3,4,1,5,6,7]  # on compare 5 et 6, tableau trié [6, 7]
[2,3,4,1,5,6,7]  # on compare 2 et 3
[2,3,4,1,5,6,7]  # on compare 3 et 4
[2,3,1,4,5,6,7]  # on compare 4 et 1 et on les déplace
[2,3,1,4,5,6,7]  # on compare 4 et 5, tableau trié [5, 6, 7]
[2,3,1,4,5,6,7]  # on compare 2 et 3 
[2,1,3,4,5,6,7]  # on compare 3 et 1 et on les déplace
[2,1,3,4,5,6,7]  # on compare 3 et 4, tableau trié [4, 5, 6, 7]
[1,2,3,4,5,6,7]  # on compare 2 et 1 et on les déplace
[1,2,3,4,5,6,7]  # on compare 2 et 3, tableau trié [3, 4, 5, 6, 7]
[1,2,3,4,5,6,7]  # on compare 1 et 2, tableau trié [2, 3, 4, 5, 6, 7]
```
````

`````


````{admonition} Exercice 6. Vérificateur de tri
:class: note

Ecrivez un algorithme qui vérifie si une liste est triée. 

Que prend l’algorithme en entrée et que retourne-t-il en sortie ?

Demandez ensuite à un autre élève de suivre les opérations décrites par votre algorithme. Est-ce que votre algorithme est correct ?

Comparer vos algorithmes. Sont-ils différents ?

````



`````{admonition} Solution 6. Vérificateur de tri
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Voici un algorithme possible. 

```
Liste Nombres           # la variable Nombres contient une liste de nombres
i = 2                   # la variable i permet de parcourir Nombres

Répéter Pour i = 2 à Longueur(Nombres)
    Si Nombres[i-1] > Nombres[i]  # l'élément précédent est plus grand
        Retourner Faux
    Fin Si
Fin Pour
Retourner Vrai
```

L'algorithme compare les éléments deux par deux et retourne `Faux` (et se termine) si l'élément d'après est plus petit que l'élément d'avant. Si tous les éléments parcourus sont dans le bon ordre, l'algorithme arrive à la dernière ligne et retourne `Vrai`. 

L'algorithme prend une liste (triée ou non triée) en entrée et retourne `Vrai` ou `Faux` en sortie, selon si la liste est triée. L'algorithme pourrait retourner aussi `Oui` et `Non`, mais *par convention* on préfère les valeurs logiques Vrai et Faux, car ces dernières peuvent être utilisées par la suite dans une condition. Par exemple, si l'algorithme retourne Faux, on pourrait demander à un autre algorithme de trier la liste. `Vrai` et `Faux` correspondent également à 0 et 1, ce qui permet de les utiliser pour faire des calculs. 

````
`````


````{admonition} Exercice 7. Mondrian
:class: note

Analysez les œuvres cubistes de Piet Mondrian. Trouvez un algorithme qui permet de créer une œuvre qui pourrait être attribuée à Mondrian.

````



`````{admonition} Solution 7. Mondrian
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Voici un algorithme possible. 

```
Répéter Pour i = 1 à 3 
    Séparer espace avec une ligne verticale noire
Fin Pour
Répéter Pour i = 1 à 3 
    [1 fois sur 2] Aller jusque la première ligne verticale 
    Séparer espace avec une ligne horizontale noire
    [1 fois sur 2] Arrêter avant la dernière ligne verticale
Fin Pour

Répéter Pour couleur_choisie dans ([Rouge, Bleu, Jaune] ou [Rouge, Bleu, Jaune, Noir])
    Répéter Pour i = 1 à Nombre allant de 1 à 4
        Choisir un grand carré 
        Répéter Tant que carré à côté est égale à couleur_choisie  
            Choisir un autre carré
        Fin Tant que
        Colorier le carré en couleur_choisie
Fin Pour

```

Cet algorithme est approximatif. Il pourrait être amélioré pour colorier en priorité les grands carrés en rouge et en bleu. Il pourrait aussi donner plus d'indications, sur comment séparer l'espace en précisant les proportions souhaitées.

Si vous avez un niveau de programmation avancé, vous pouvez essayer de coder cet algorithme.
````
`````


### 3. Des algorithmes aux programmes

````{admonition} Exercice 1. Jeu de la devinette 🔌
:class: note

Ecrire le programme suivant : le programme pense à un nombre au hasard. Lorsque vous lui proposez un nombre, il vous dit si «c'est plus» ou «si c'est moins» jusqu'à ce que vous ayez trouvé.
 
````

`````{admonition} Solution 1. Jeu de la devinette 🔌
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Voici un programme possible pour le jeu de la devinette. 

```
import random

# imagine un ombre au hasard
n = random.randint(0,100)

essais = 0
nb = -1

while nb != n:
    try :
        nb = int(input("Devinez le nombre ?"))
    except :
        print("Le nombre indiqué n'est pas valide...")

    essais += 1

    if nb < n :
        print("C'est plus")
    elif nb > n :
        print("C'est moins")
    else :
        print("Super! Vous avez trouvé en", essais, "coups")


```

La stratégie gagnante consiste à toujours viser au milieu de la plage de nombres possibles (sera vu en 2e année).

````
`````





````{admonition} Exercice 2. Plus petit nombre 🔌
:class: note

Transcrire l’algorithme de l’exercice qui permet de déterminer le plus petit nombre d’une liste, en un programme Python.

````

`````{admonition} Solution 2. Plus petit nombre 🔌🔌
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Voici un programme qui trouve le minimum d'une liste. 

```
def trouver_minimum(liste) :

    # se souvient du plus petit élément
    min_indice = 0

    # pour chaque élément de la liste (-1, car compare deux éléments)
    for i in range(1, len(liste)):

        # on ordonne les éléments deux par deux
        if liste[i] < liste[min_indice] :
            min_indice = i

    return liste[min_indice]

# tester la fonction
rect = [3,4,1,2,6,5,9,10,14,7,23,24,21]
print(trouver_minimum(rect))

````
`````




````{admonition} Exercice 3. Programmes de tri 🔌
:class: note

Implémenter le tri à bulles et/ou le tri par insertion vus au cours.

Créer une liste qui contient les valeurs de 1 à n dans un ordre aléatoire, où n prend la valeur 10, par exemple. Vous pouvez utiliser la fonction shuffle() du module random.

*Pour aller plus loin.*

A l’aide du module time et de sa fonction time(), chronométrez le temps prend le tri d'une liste de 100, 500, 1000, 10000, 20000, 30000, 40000 puis 50000 nombres. 

Noter les temps obtenus et affichez-les sous forme de courbe dans un tableur. Ce graphique permet de visualiser le temps d’exécution du tri en fonction de la taille de la liste. Que constatez‑vous ?

Sur la base de ces mesures, pouvez-vous estimer le temps que prendrait le tri de 100000 éléments ?

Lancer votre programme avec 100000 éléments et comparez le temps obtenu avec votre estimation.

````

`````{admonition} Solution 3. Programmes de tri 
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Voici un bout de programme avec les deux algorithmes de tri et leur comparaison. Idéalement, il faudrait calculer le temps moyen basé sur plusieurs listes plutôt que d'afficher les résultats d'un seul *run*.

```

# Fonction tri à bulles
def tri_bulles(liste, verbose=1):

    # pour chaque élément de la liste (-1)
    for j in range(1, len(liste)):

        # pour chaque élément de la liste jusqu'à -j
        for i in range(1, len(liste)):

            # on ordonne les éléments deux par deux
                liste[i-1], liste[i] = liste[i], liste[i-1]
                if verbose :
                    print('Liste modifiée', liste)

        if verbose :
            print('\nBulles : Parcours', j, 'de la liste terminé.\n')

    return liste


# Fonction tri par insertion
def tri_insertion(liste, verbose=1):

    # pour chaque élément de la liste (-1)
    for j in range(1, len(liste)):

        # pour chaque élément de la liste jusqu'à j
        for i in range(j, 0, -1):

            # on initialise le plus petit élément au prochain élément de la liste
            if liste[i-1] > liste[i] :
                liste[i-1], liste[i] = liste[i], liste[i-1]
                if verbose :
                    print('Liste modifiée', liste)
            else :
                break

        if verbose :
            print('\nInsertion : Parcours', j, 'de la liste terminé.\n')

    return liste


import random

#créé une liste non triée
def liste_melangee(n) :
    liste = []
    for i in range(1, n):
        liste.append(i)
    random.shuffle(liste)
    return liste

ma_liste = liste_melangee(11)
ma_liste_non_triee = ma_liste[:]

tri_bulles(ma_liste)

ma_liste = ma_liste_non_triee[:]
tri_insertion(ma_liste)


import time

times_bulles = []
times_insertion = []

for i in [100, 500, 1000, 10000, 20000, 30000, 40000, 50000] : #, 10000, 20000, 30000, 40000, 50000] :
    ma_liste = liste_melangee(i)

    ma_liste_non_triee = ma_liste[:]
    time1 = time.time()
    tri_bulles(ma_liste, 0)
    time2 = time.time()
    times_bulles.append(time2-time1)

    ma_liste = ma_liste_non_triee[:]
    time1 = time.time()
    tri_insertion(ma_liste, 0)
    time2 = time.time()
    times_insertion.append(time2-time1)

print(times_bulles)
print(times_insertion)


## Un exemple de run, idéalement on devrait faire une moyenne sur plusiers listes

import matplotlib.pyplot as plt

# times_bulles = [0.0007197856903076172, 0.021329164505004883, 0.09939980506896973, 11.248387098312378, 57.714684009552, 139.61864519119263, 233.14582777023315, 373.582261800766]
# times_insertion = [0.00029206275939941406, 0.008688211441040039, 0.0382380485534668, 4.295107841491699, 21.795172929763794, 49.34161734580994, 88.14957118034363, 135.34030890464783]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot([100, 500, 1000, 10000, 20000, 30000, 40000, 50000], times_insertion, 'o-', color='tab:blue', label='Tri par insertion')
ax.plot([100, 500, 1000, 10000, 20000, 30000, 40000, 50000], times_bulles, 'o-', color='tab:red', label='Tri à bulles')
plt.legend(fontsize=12)

ax.set_xlabel(r"Nombres d'éléments", fontsize=14)
ax.set_ylabel(r'Secondes', fontsize=14)

ax.set_title('Comparaison du tri à bulles avec le tri par insertion', fontsize=16)

# display the plot
plt.show()

````
`````



````{admonition} Exercice 4. Bogosort 🔌
:class: note

Coder l’algorithme du tri de Bogo en Python (voir chapitre 2 : Le saviez-vous ?). 

Relancer l'algorithme plusieurs fois, en notant le nombre d'itération nécessaires pour qu'il termine.

A partir de quelle taille de liste cet algorithme est-il inutilisable ?
 
````

`````{admonition} Solution 4. Tri de Bogo
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Voici une fonction qui code le tri de Bogo.

```

# module qui permet de mélanger la liste
import random

# retourne vrai si les éléments sont triés, retourne faux sinon
def verifie_tri(elements):
    for i in range(0, len(elements)-1):
        if (elements[i] > elements[i+1] ):
            return False
    return True

# implémente le tri Bogo
def TriBogo(liste):
    n = 0 # se souvient du nombre d'essais
    while (verifie_tri(liste)== False):
        random.shuffle(liste)
        n += 1
        print('Nouvelle configuration', n, ' : ', liste)
    print('La liste', liste, 'est triée après', n, 'essais')

# tester la fonction
rect = [3,4,1,2,6,5]
TriBogo(rect)

``` 

En relançant le programme une dizaine de fois, le minimum d'itérations nécessaires était 7 et le maximum 4531. En théorie, cela peut prendre de 1 à une infinité d'opérations (si on a vraiment pas de chance).

````
`````



````{admonition} Exercice 5. Fibonacci 🔌
:class: note

Ecrire un algorithme qui calcule la suite des nombres de Fibonacci. 

Traduire l’algorithme en une fonction Python. 

Comparer avec les solutions trouvées par vos camarades de classe.
````


`````{admonition} Solution 5. Fibonacci 🔌
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Une version simple de l'algorithme de Fibonnaci pourrait être la suivante (calcule au moins NB_TERMES termes) :

```
N1 ← 0
N2 ← 1
Répéter Pour i  ← 1 à NB_TERMES//2 
    N1 ← N1 + N2
    N2 ← N1 + N2
Fin Pour
```

Voici trois programmes de plus en plus sophistiqués qui calculent la suite de Fibonnaci.

```

# gère des entrées non prévues de la part de l'utilisateur
try :
    nb = int(input("Combien de termes calculer pour la suite de Fibonnaci ?"))
except :
    print("Le nombre indiqué n'est pas valide...")


## Version simple sans liste (à quelques termes près)

if nb :

    # initialise deux éléments
    n1 = 0
    n2 = 1

    # affiche le début de la suite
    print(n1)
    print(n2)

    # calcule la suite
    for i in range(nb//2) :
        n1 = n1 + n2
        print(n1)
        n2 = n1 + n2
        print(n2)


## Version sans liste

if nb :

    # initialise deux éléments
    n1 = 0
    n2 = 1

    # affiche le début de la suite
    print(n1)
    print(n2)

    # calcule la suite
    for i in range(1,nb-1) :
        if i%2 == 1 :
            n1 = n1 + n2
            print(n1)
        else :
            n2 = n1 + n2
            print(n2)


## Version avec liste

if nb :

    # initialise la suite
    resultat = [0, 1]

    # calcule la suite
    for i in range(1,nb-1) :
        nouveau_terme = resultat[i-1] + resultat[i]
        resultat.append(nouveau_terme)
    print(resultat)


``` 
````
`````




```{admonition} Exercice 3.4. Une question à un million
:class: note

Si une instruction prend 10<sup>-6</sup> secondes, combien de temps faut-il pour trier un tableau d’un million d’éléments avec le tri à sélection comparé au tri rapide (sans tenir compte de la constante) ?

```

````{admonition} Solution 3.4. Une question à un million
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Pour trier 1 million d’éléments, le tri par sélection prend 10<sup>6</sup>*10<sup>6</sup> *10<sup>-6</sup> secondes ou 1 million de secondes (équivalent à plus de 11 jours), alors que le tri rapide a besoin de log2(10<sup>6</sup>)*10<sup>6</sup> *10<sup>-6</sup> ou ~20 secondes. 

Cette différence de temps est suffisante pour rendre rédhibitoire l’utilisation du tri par sélection. Pensez au nombre de clients qu’un réseau social possède, ou au nombre de produits qu’un supermarché doit gérer.
```
````


```{admonition} Exercice 3.5. Une question de pivot
:class: note

Trier le tableau suivant avec l’algorithme de tri rapide : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main, en prenant le dernier élément comme pivot. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

Est-ce que le choix du pivot est important ?

```

````{admonition} Solution 3.5. Une question de pivot
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Lors de la première étape du tri rapide, l’élément pivot est 5. On se retrouve donc avec les deux tableaux suivants :

&nbsp;&nbsp;&nbsp;&nbsp; [[3, 1, 4, 2], 5, [6, 8, 7, 9]]

Les nouveaux éléments pivots sont les derniers éléments des nouveaux tableaux de gauche [3, 1, 4, 2] et le tableau de droite [6, 8, 7, 9] , donc 2 et 9. On réarrange tous les éléments des tableaux autour des éléments pivots, selon leur taille :

&nbsp;&nbsp;&nbsp;&nbsp; 	[[1], 2, [3, 4], 5, [6, 8, 7], 9 [ ]]

On continue les mêmes opérations pour les tableaux qui contiennent plus d’un élément : [3, 4] et [6, 8, 7]. Les nouveaux pivots sont 4 et 7, car ils sont les derniers éléments des tableaux restants à plus d’un élément :

&nbsp;&nbsp;&nbsp;&nbsp; 	[1, 2, [3], 4, [ ], 5, [6], 7, [8], 9]

Il ne reste plus de tableaux de plus d’un élément, le tableau est donc trié :

&nbsp;&nbsp;&nbsp;&nbsp; 	[1, 2, 3, 4, 5, 6, 7, 8, 9]

Le choix du pivot est important et à prendre en compte si on a des indications sur le tableau à trier.

```
````




```{admonition} Exercice 3.6. Une question de sélection
:class: note

Trier le tableau suivant avec l’algorithme de tri par sélection : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```

````{admonition} Solution 3.6. Une question de sélection
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Lors de la première étape du tri par insertion, on cherche à trouver la bonne position du 2e élément, dans ce cas l’élément 6 reste au même emplacement, car 3 est plus petit que 6 :

&nbsp;&nbsp;&nbsp;&nbsp; [3, **<span style="color:rgb(89, 51, 209)">6</span>**, 8, 7, 1, 9, 4, 2, 5]

Le prochain élément considéré est le 8. Cet élément est également déjà bien placé :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	[**<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, 7, 1, 9, 4, 2, 5]

Comme l’ordre des éléments ne change pas, nous notons cette configuration à droite.

Le prochain élément considéré est le 7. Cet élément n’est pas bien placé au regard du tableau que l’on a déjà trié. Sa place est avant le 8, on va donc l’insérer entre le 6 et le 8 : 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	[**<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">8</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, 1, 9, 4, 2, 5]

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, 1, 9, 4, 2, 5]

Le prochain élément de la liste non triée est le 1 :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, **<span style="color:rgb(13, 204, 166)">8</span>**, **<span style="color:rgb(89, 51, 209)">1</span>**, 9, 4, 2, 5] 

Nous allons l’insérer à la bonne position du tableau déjà trié, c’est-à-dire tout au début :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">1</span>**, **<span style="color:rgb(89, 51, 209)">3</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, 9, 4, 2, 5]

Tous les éléments qui ont changé de position dans l’étape précédente sont désignés en rouge. Le prochain élément à considérer est le 9. Il est déjà bien placé par rapport à la partie triée du tableau :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, **<span style="color:rgb(13, 204, 166)">8</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**, 4, 2, 5]

On continue de la sorte jusqu’à ce que tous les éléments du tableau soient parcourus :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, **<span style="color:rgb(13, 204, 166)">8</span>**, **<span style="color:rgb(13, 204, 166)">9</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, 2, 5]

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**,  2, 5]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, **<span style="color:rgb(13, 204, 166)">8</span>**, **<span style="color:rgb(13, 204, 166)">9</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, 5]

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, **<span style="color:rgb(89, 51, 209)">3</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**, 5]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, **<span style="color:rgb(13, 204, 166)">8</span>**, **<span style="color:rgb(13, 204, 166)">9</span>**, **<span style="color:rgb(89, 51, 209)">5</span>**]

Lorsque le dernier élément du tableau est inséré à la bonne position, tout le tableau est trié :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(89, 51, 209)">5</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**]

```
````


```{admonition} Exercice 3.7. Une question d'insertion
:class: note

Trier le tableau suivant avec l’algorithme de tri par insertion : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```

````{admonition} Solution 3.7. Une question d'insertion
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Lors de la première étape du tri par sélection, on cherche le plus petit élément :

&nbsp;&nbsp;&nbsp;&nbsp; [3, 6, 8, 7, **<span style="color:rgb(89, 51, 209)">1</span>**, 9, 4, 2, 5]

On échange les positions du premier et du plus petit élément :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">1</span>**, 6, 8, 7, **<span style="color:rgb(89, 51, 209)">3</span>**, 9, 4, 2, 5]

On cherche le plus petit élément dans le tableau, en excluant l’élément que l’on vient de trier :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, 6, 8, 7, 3, 9, 4, **<span style="color:rgb(89, 51, 209)">2</span>**, 5]

On échange sa position avec le 2e élément du tableau :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, 8, 7, 3, 9, 4, **<span style="color:rgb(89, 51, 209)">6</span>**, 5]

Notez que les étapes qui changent l’ordre des éléments du tableau sont disposées à gauche. On cherche le plus petit élément du tableau non trié et on l’échange avec le troisième élément :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, 8, 7, **<span style="color:rgb(89, 51, 209)">3</span>**, 9, 4, 6, 5]	

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(89, 51, 209)">3</span>**, 7, **<span style="color:rgb(89, 51, 209)">8</span>**, 9, 4, 6, 5] 

On continue de la sorte jusqu’à ce que tous les éléments soient triés (les éléments triés sont en vert) :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, 7, 8, 9, **<span style="color:rgb(89, 51, 209)">4</span>**, 6, 5]

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, 8, 9, **<span style="color:rgb(89, 51, 209)">7</span>**, 6, 5]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, 8, 9, 7, 6, **<span style="color:rgb(89, 51, 209)">5</span>**]

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(89, 51, 209)">5</span>**, 9, 7, 6, **<span style="color:rgb(89, 51, 209)">8</span>**]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">5</span>**, 9, 7, **<span style="color:rgb(89, 51, 209)">6</span>**, 8]

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">5</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, 7, **<span style="color:rgb(89, 51, 209)">9</span>**, 8]

Le septième élément du tableau est déjà à la bonne position, donc il n’y a pas besoin d’échanger la position de deux éléments. Le tableau est trié lorsque tous les éléments sont parcourus.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">5</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, 9, 8]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">5</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, 9, **<span style="color:rgb(89, 51, 209)">8</span>**]


&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(13, 204, 166)">1</span>**, **<span style="color:rgb(13, 204, 166)">2</span>**, **<span style="color:rgb(13, 204, 166)">3</span>**,  **<span style="color:rgb(13, 204, 166)">4</span>**, **<span style="color:rgb(13, 204, 166)">5</span>**, **<span style="color:rgb(13, 204, 166)">6</span>**, **<span style="color:rgb(13, 204, 166)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**]

```
````



```{admonition} Exercice 3.8. Une question de bulles
:class: note

Trier le tableau suivant avec l’algorithme de tri à bulles : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```


````{admonition} Solution 3.8. Une question de bulles
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Lors du tri à bulles, on considère les éléments deux par deux. S’ils sont dans le bon ordre, on ne fait rien, sinon on échange leur position :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">3</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, 8, 7, 1, 9, 4, 2, 5]
&nbsp;&nbsp;&nbsp;&nbsp;[3, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, 7, 1, 9, 4, 2, 5]
&nbsp;&nbsp;&nbsp;&nbsp;[3, 6, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, 1, 9, 4, 2, 5]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3, 6, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, 1, 9, 4, 2, 5]
&nbsp;&nbsp;&nbsp;&nbsp;[3, 6, 7, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">1</span>**, 9, 4, 2, 5]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3, 6, 7, **<span style="color:rgb(89, 51, 209)">1</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, 9, 4, 2, 5]
&nbsp;&nbsp;&nbsp;&nbsp;[3, 6, 7, 1, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**, 4, 2, 5]
&nbsp;&nbsp;&nbsp;&nbsp;[3, 6, 7, 1, 8, **<span style="color:rgb(89, 51, 209)">9</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, 2, 5]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3, 6, 7, 1, 8, **<span style="color:rgb(89, 51, 209)">4</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**, 2, 5]
&nbsp;&nbsp;&nbsp;&nbsp;[3, 6, 7, 1, 8, 4, **<span style="color:rgb(89, 51, 209)">9</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, 5]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3, 6, 7, 1, 8, 4, **<span style="color:rgb(89, 51, 209)">2</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**, 5]
&nbsp;&nbsp;&nbsp;&nbsp;[3, 6, 7, 1, 8, 4, 2, **<span style="color:rgb(89, 51, 209)">9</span>**, **<span style="color:rgb(89, 51, 209)">5</span>**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3, 6, 7, 1, 8, 4, 2, **<span style="color:rgb(89, 51, 209)">5</span>**, **<span style="color:rgb(89, 51, 209)">9</span>**]

Il faut procéder à nouveau par un parcours de la liste depuis son début, où on compare et on réarrange les éléments deux par deux :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">3</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, 7, 1, 8, 4, 2, 5, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [3, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, 1, 8, 4, 2, 5, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [3, 6, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">1</span>**, 8, 4, 2, 5, **9**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [3, 6, **<span style="color:rgb(89, 51, 209)">1</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, 8, 4, 2, 5, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [3, 6, 1, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, 4, 2, 5, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [3, 6, 1, 7, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, 2, 5, **9**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [3, 6, 1, 7, **<span style="color:rgb(89, 51, 209)">4</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, 2, 5, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [3, 6, 1, 7, 4, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, 5, **9**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [3, 6, 1, 7, 4, **<span style="color:rgb(89, 51, 209)">2</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, 5, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [3, 6, 1, 7, 4, 2, **<span style="color:rgb(89, 51, 209)">8</span>**, **<span style="color:rgb(89, 51, 209)">5</span>**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; [3, 6, 1, 7, 4, 2, **<span style="color:rgb(89, 51, 209)">5</span>**, **<span style="color:rgb(89, 51, 209)">8</span>**, **9**]

Une deuxième « bulle » remonte, le deuxième élément le plus grand. On refait à nouveau un parcours du tableau (les éléments bien triés sont en gras) : 

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">3</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, 1, 7, 4, 2, 5, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [3, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">1</span>**, 1, 7, 4, 2, 5, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [3, **<span style="color:rgb(89, 51, 209)">1</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, 7, 4, 2, 5, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [3, 1, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, 4, 2, 5, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [3, 1, 6, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, 2, 5, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [3, 1, 6, **<span style="color:rgb(89, 51, 209)">4</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, 2, 5, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [3, 1, 6, 4, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, 5, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [3, 1, 6, 4, **<span style="color:rgb(89, 51, 209)">2</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, 5, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [3, 1, 6, 4, 2, **<span style="color:rgb(89, 51, 209)">7</span>**, **<span style="color:rgb(89, 51, 209)">5</span>**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [3, 1, 6, 4, 2, **<span style="color:rgb(89, 51, 209)">5</span>**, **<span style="color:rgb(89, 51, 209)">7</span>**, **8**, **9**]

Lorsqu’on atteint la partie déjà triée du tableau (éléments en gras), on recommence depuis le début du tableau :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">3</span>**, **<span style="color:rgb(89, 51, 209)">1</span>**, 6, 4, 2, 5, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">1</span>**, **<span style="color:rgb(89, 51, 209)">3</span>**, 6, 4, 2, 5, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [1, **<span style="color:rgb(89, 51, 209)">3</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, 4, 2, 5, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [1, 3, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, 2, 5, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [1, 3, **<span style="color:rgb(89, 51, 209)">4</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, 2, 5, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [1, 3, 4, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, 5, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [1, 3, 4, **<span style="color:rgb(89, 51, 209)">2</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, 5, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [1, 3, 4, 2, **<span style="color:rgb(89, 51, 209)">6</span>**, **<span style="color:rgb(89, 51, 209)">5</span>**, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [1, 3, 4, 2, **<span style="color:rgb(89, 51, 209)">5</span>**, **<span style="color:rgb(89, 51, 209)">6</span>**, **7**, **8**, **9**]

On a atteint la partie triée du tableau, on recommence depuis le début :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">1</span>**, **<span style="color:rgb(89, 51, 209)">3</span>**, 4, 2, 5, **6**, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [1, **<span style="color:rgb(89, 51, 209)">3</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, 2, 5, **6**, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [1, 3, **<span style="color:rgb(89, 51, 209)">4</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, 5, **6**, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [1, 3, **<span style="color:rgb(89, 51, 209)">2</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, 5, **6**, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [1, 3, 2, **<span style="color:rgb(89, 51, 209)">4</span>**, **<span style="color:rgb(89, 51, 209)">5</span>**, **6**, **7**, **8**, **9**]

Les bulles (les plus grands nombres) continuent à remonter : 

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">1</span>**, **<span style="color:rgb(89, 51, 209)">3</span>**, 2, 4, 5, **6**, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [1, **<span style="color:rgb(89, 51, 209)">3</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, 4, 5, **6**, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [1, **<span style="color:rgb(89, 51, 209)">2</span>**, **<span style="color:rgb(89, 51, 209)">3</span>**, 4, 5, **6**, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [1, 2, **<span style="color:rgb(89, 51, 209)">3</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, 5, **6**, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [1, 2, 3, **<span style="color:rgb(89, 51, 209)">4</span>**, **<span style="color:rgb(89, 51, 209)">5</span>**, **6**, **7**, **8**, **9**]

On recommence à nouveau à comparer les éléments depuis le début du tableau : 

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">1</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, 3, 4, **5**, **6**, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [1, **<span style="color:rgb(89, 51, 209)">2</span>**, **<span style="color:rgb(89, 51, 209)">3</span>**, 4, **5**, **6**, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [1, 2, **<span style="color:rgb(89, 51, 209)">3</span>**, **<span style="color:rgb(89, 51, 209)">4</span>**, 4, **5**, **6**, **7**, **8**, **9**]

Même si nous n'avons pas du intervertir la position de deux éléments, il faut à nouveau parcourir le tableau depuis le début :

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">1</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, 3, **4**, **5**, **6**, **7**, **8**, **9**]
&nbsp;&nbsp;&nbsp;&nbsp; [1, **<span style="color:rgb(89, 51, 209)">2</span>**, **<span style="color:rgb(89, 51, 209)">3</span>**, **4**, **5**, **6**, **7**, **8**, **9**]

Et on fait une dernière comparaison : 

&nbsp;&nbsp;&nbsp;&nbsp; [**<span style="color:rgb(89, 51, 209)">1</span>**, **<span style="color:rgb(89, 51, 209)">2</span>**, **3**, **4**, **5**, **6**, **7**, **8**, **9**]

Le tableau est désormais trié : 

&nbsp;&nbsp;&nbsp;&nbsp; [1, **2**, **3**, **4**, **5**, **6**, **7**, **8**, **9**]


```
````


````{admonition} Exercice 3.9. Une question de chronomètre 🔌
:class: note

Créer une liste qui contient les valeurs de 1 à n dans un ordre aléatoire, où n prend la valeur 100, par exemple. Indice : utiliser la fonction `shuffle()` du module `random`.

Implémenter au moins deux des trois algorithmes de tri vu au cours.
A l’aide du module `time` et de sa fonction `time()`, chronométrer le temps prend le tri d'une liste de 100, 500, 1000, 10000, 20000, 30000, 40000 puis 50000 nombres. 

Noter les temps obtenus et les afficher sous forme de courbe dans un tableur. Ce graphique permet de visualiser le temps d’exécution du tri en fonction de la taille de la liste. Que peut-on constater ?

Sur la base de ces mesures, peut-on estimer le temps que prendrait le tri de 100000 éléments ?

Lancer votre programme avec 100000 éléments et comparer le temps obtenu avec votre estimation.

````

**Solution à compléter**



```{admonition} Exercice 4.2. Une question de fusion
:class: note

Trier le tableau suivant avec l’algorithme de tri par fusion : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```


**Solution à compléter**

````{admonition}  Exercice 4.3. Dans l'autre sens 🔌
:class: note

En Python, proposer une fonction qui inverse l’ordre des lettres dans un mot. Vous pouvez parcourir les lettres du mot directement ou à travers un indice.

Proposer une autre fonction qui inverse l’ordre des lettres dans un mot de manière récursive.

````



`````{admonition} Solution 4.3. Dans l'autre sens 🔌
:class: hint

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




````{admonition}  Exercice 4.4. Factorielle 🔌
:class: note

La fonction factorielle `n!` en mathématiques est le produit de tous les nombres entiers jusqu’à `n`. C’est une des fonctions les plus simples à calculer de manière récursive. Elle peut être définie comme ceci :

	n! = (n-1)! * n

Programmer cette fonction de manière récursive en Python. Proposer également une implémentation itérative de la factorielle où les éléments de 1 à `n` sont traités l’un après l’autre.

````


`````{admonition} Solution 4.4. Factorielle 🔌
:class: hint

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



