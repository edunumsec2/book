# Algorithmique II

## 2. Trie, cherche et trouve

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

````{exercise} L'algorithme de votre journée

Réfléchissez à votre journée : y a-t-il des actions qui se retrouvent chaque jour ouvrable ? Arrivez-vous à esquisser un algorithme que vous suivez sans que vous en ayez conscience ?

````

`````{solution} 

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

````{exercise} Trois algorithmes de tri

Trier la liste [2,5,3,4,7,1,6] en utilisant les trois algorithmes de tri vus adans le cours. Représenter l’état de la liste après chaque étape.

````

`````{solution} 

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


````{exercise} Vérificateur de tri

Ecrivez un algorithme qui vérifie si une liste est triée. 

Que prend l’algorithme en entrée et que retourne-t-il en sortie ?

Demandez ensuite à un autre élève de suivre les opérations décrites par votre algorithme. Est-ce que votre algorithme est correct ?

Comparer vos algorithmes. Sont-ils différents ?

````



`````{solution} 

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


````{exercise} Mondrian

Analysez les œuvres cubistes de Piet Mondrian. Trouvez un algorithme qui permet de créer une œuvre qui pourrait être attribuée à Mondrian.

````



`````{solution} 

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

