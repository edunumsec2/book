# Algorithmique I

## 3. Des algorithmes aux programmes

### Solution des exercices 

````{exercise} Jeu de la devinette 🔌

Ecrire le programme suivant : le programme pense à un nombre au hasard. Lorsque vous lui proposez un nombre, il vous dit si «c'est plus» ou «si c'est moins» jusqu'à ce que vous ayez trouvé.
 
````

`````{solution}

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





````{exercise} Plus petit nombre 🔌

Transcrire l’algorithme de l’exercice qui permet de déterminer le plus petit nombre d’une liste, en un programme Python.

````

`````{solution} 

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




````{exercise} Programmes de tri 🔌

Implémenter le tri à bulles et/ou le tri par insertion vus au cours.

Créer une liste qui contient les valeurs de 1 à n dans un ordre aléatoire, où n prend la valeur 10, par exemple. Vous pouvez utiliser la fonction shuffle() du module random.

*Pour aller plus loin.*

A l’aide du module time et de sa fonction time(), chronométrez le temps prend le tri d'une liste de 100, 500, 1000, 10000, 20000, 30000, 40000 puis 50000 nombres. 

Noter les temps obtenus et affichez-les sous forme de courbe dans un tableur. Ce graphique permet de visualiser le temps d’exécution du tri en fonction de la taille de la liste. Que constatez‑vous ?

Sur la base de ces mesures, pouvez-vous estimer le temps que prendrait le tri de 100000 éléments ?

Lancer votre programme avec 100000 éléments et comparez le temps obtenu avec votre estimation.

````

`````{solution} 

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
            if liste[i-1] > liste[i] :
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



````{exercise} Bogosort 🔌

Coder l’algorithme du tri de Bogo en Python (voir chapitre 2 : Le saviez-vous ?). 

Relancer l'algorithme plusieurs fois, en notant le nombre d'itération nécessaires pour qu'il termine.

A partir de quelle taille de liste cet algorithme est-il inutilisable ?
 
````

`````{solution} 

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



````{exercise} Fibonacci 🔌

Ecrire un algorithme qui calcule la suite des nombres de Fibonacci. 

Traduire l’algorithme en une fonction Python. 

Comparer avec les solutions trouvées par vos camarades de classe.
````


`````{solution} 

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





