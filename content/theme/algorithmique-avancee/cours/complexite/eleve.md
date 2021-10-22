<span style="color:rgb(13, 204, 166);font-weight:600; font-size:1.2em">Version du 16 juin 2021</span>

# 2. Complexité des algorithmes


````{admonition} Matière à réfléchir III
:class: attention
On souhaite comparer deux algorithmes qui permettent de résoudre le même problème, afin d’utiliser l’algorithme qui permet de résoudre le problème plus rapidement. Mais comment pourrait‑on calculer la vitesse d’un algorithme ?
````

## Principe de complexité

Nous avons vu dans la section <a href="../introduction-algorithmique/algorithmes-classiques/eleve.html">Algorithmes de tri</a> que certains {glo}`algo|algorithmes` de tri étaient plus rapides que d’autres. Il est important lorsqu’on utilise un {glo}`algo|algorithme` de nous préoccuper de son {glo}`efficacite|efficacité`. Mais comment pourrait-on calculer la vitesse d’un {glo}`algo|algorithme` ?

Est-ce qu’on peut utiliser la taille de l’{glo}`algo|algorithme` pour prédire le temps qu’il va prendre à s’exécuter ? En d’autres termes, est-ce qu’un {glo}`algo|algorithme` de 10 lignes est toujours plus lent qu’un {glo}`algo|algorithme` de 5 lignes ? Nous avons vu que l’{glo}`algo|algorithme` infini du chapitre précédent est très court (seulement 5 lignes), mais en théorie il ne s’arrête jamais. Une {glo}`bouclewhile|boucle` rallonge le code de seulement 2 lignes, mais rallonge le temps d’exécution de manière bien plus significative. 

On pourrait croire qu’il suffit de programmer un {glo}`algo|algorithme` et de chronométrer le temps que ce programme prend à s’exécuter. Cette métrique est problématique, car elle ne permet pas de comparer différents {glo}`algo|algorithmes` entre eux lorsqu’ils sont exécutés sur différentes machines. Un {glo}`algo|algorithme` lent {glo}`implementation|implémenté` sur une machine dernière génération pourrait prendre moins de temps à s’exécuter qu’un {glo}`algo|algorithme` rapide {glo}`implementation|implémenté` sur une machine datant d’une dizaine d’années. 

Pour mesurer le temps d’exécution (ou la vitesse) d’un {glo}`algo|algorithme`, il nous faut un critère plus objectif : **<span style="color:rgb(89, 51, 209)">le nombre d’instructions élémentaires</span>**.  De manière formelle et rigoureuse, on ne parle pas d’efficacité, mais plutôt de la **<span style="color:rgb(89, 51, 209)">complexité d’un algorithme</span>**, qui est en fait contraire à son efficacité. L’analyse de la complexité d’un algorithme étudie la quantité de ressources (par exemple de temps) nécessaires à l’exécution de cet {glo}`algo|algorithme`.

```{admonition} Le saviez-vous ?
:class: hint
Nous allons surtout étudier la complexité des algorithmes en rapport avec le temps. Mais la complexité d’un algorithme peut également être calculée en rapport avec toutes les ressources qu’il utilise, par exemple des ressources d’espace en mémoire ou de consommation d’énergie. 
```

## Recherche linéaire 

Nous allons tenter ici d’estimer le nombre d’{glo}`instruction|instructions` élémentaires nécessaire pour rechercher un élément dans un tableau (liste en Python). La manière la plus simple pour rechercher un élément dans un tableau consiste à parcourir le tableau et à comparer tous ses éléments avec l’élément recherché :

```{code-block} python

# Algorithme de recherche linéaire
Tableau Eléments : numérique
Variable n : longueur(Eléments)
Variable élément_recherché : numérique
Variable i : numérique

Répéter Pour i = 1 à n
    si Eléments[i] == élément_recherché
        Retourner « Oui »
Fin Pour
Retourner « Non »

```

Supposons que le tableau contient 10 éléments. Pour trouver l’élément recherché, il faut au moins deux {glo}`instruction|instructions` : une {glo}`instruction|instruction` qui accède un élément du tableau ou **Elements[i]** et une autre {glo}`instruction|instruction` qui le compare à **élément_recherché**. Dans le cas du tableau à 10 éléments, cet algorithme prendrait 20 {glo}`instruction|instructions` élémentaires. Mais si le tableau contient 100 éléments, le nombre d’{glo}`instruction|instructions` élémentaires monte à environ 200. De manière  générale, si le nombre d’éléments dans le tableau est n, et cela prend 2*n {glo}`instruction|instructions` pour parcourir et comparer ses éléments. 

Cette estimation n’est pas exacte. Nous n’avons pas pris en compte les {glo}`instruction|instructions` élémentaires qui permettent d’incrémenter i et de vérifier si **i == longueur(Nombres)**. Lorsqu’on prend en compte ces 2 {glo}`instruction|instructions` liées à **i**, le nombre d’{glo}`instruction|instructions` passe de 200 à 400. Ce qui nous intéresse ici n’est pas le nombre exact d’{glo}`instruction|instructions`, 200 ou 400, mais plutôt son **<span style="color:rgb(89, 51, 209)">ordre de grandeur</span>** ou comment ce nombre d’{glo}`instruction|instructions` élémentaires grandit avec **n**. L’algorithme ici est d’ordre **O(n)** ou linéaire. 

Un ordre de grandeur linéaire implique que le nombre d’{glo}`instruction|instructions` élémentaires de l’{glo}`algo|algorithme` croît linéairement en fonction du nombre d’éléments des données : c*n+a, ou c est une {glo}`constante|constante` . Dans ce cas précis, c vaut 4. La {glo}`constante|constante`  a vaut 5 et correspond aux {glo}`instruction|instructions` d’initialisation avant la {glo}`bouclewhile|boucle` plus l’instruction de retour à la fin. Si le tableau contient 10 éléments, il faut environ 45 {glo}`instruction|instructions` ; pour 100 éléments il faut environ 405 {glo}`instruction|instructions` ; pour 1000 éléments il faut environ 4005 {glo}`instruction|instructions` et ainsi de suite. Le nombre d’{glo}`instruction|instructions` grandit de manière linéaire en fonction de la taille des données **n**.

```{admonition} Exercice 2
:class: note

Ecrire un algorithme qui affiche tous les nombres de **1** à **n**. 

Combien d’instructions élémentaires sont exécutées pour **n=100** ? Quel est l’ordre de grandeur de cet algorithme ?  

```


`````{admonition} Solution de l'exercice 2
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

```{code-block} python
Variable n : numérique
Variable i : numérique

Répéter Pour i = 1 à n
    Afficher(i)
Fin Pour
```

L’initialisation des variables `n` et `i` compte pour 2 instructions élémentaires. Chaque passage de la boucle correspond à trois instructions élémentaires : 1 instruction qui affiche `i`, 1 instruction qui incrémente `i` de 1 et finalement une instruction qui compare `i` à `n` (pour savoir si la boucle s’arrête ou si elle continue). Le total d’instructions élémentaires pour le cas où n vaut 100 est 3*100+1 ou 301 instructions élémentaires.

Il faut se rendre compte que ce nombre estimé d’instructions élémentaires est approximatif, et non pas exact. Par exemple, l’instruction élémentaire `Afficher(i)` n’est certainement implémentée avec une seule instruction à l’exécution et prend de plus en plus de temps à mesure que `i` grandit.

L’ordre de grandeur est `O(`n) ou linéaire, comme illustré dans ce graphique : 

```{figure} media/Graphique_rech_lin_22.png
---
alt: recherche linéaire
width: 420px
name : fig-rech-lin2
---
```

````

`````


```{admonition} Exercice 3
:class: note

Ecrire un algorithme qui affiche tous les nombres *pairs* de **1** à **n**. 

Combien d’instructions élémentaires sont exécutées pour **n=100** ? Quel est l’ordre de grandeur de cet algorithme ?  

```

`````{admonition} Solution de l'exercice 3
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

```{code-block} python
Variable n : numérique
Variable i : numérique

Répéter Pour i = 2 à n, par pas de 2
    Afficher(i)
Fin Pour
```

Notez que la seule ligne de code qui change par rapport à la solution de l’exercice précédent est l’incrément de la boucle par pas de 2. 

L’initialisation de la variable `i` compte pour 1 instruction élémentaire. Chaque passage de la boucle correspond à trois instructions élémentaires : 1 instruction qui affiche `i`, 1 instruction qui incrémente `i` de 2 et finalement une instruction qui compare `i` à `n` (pour savoir si la boucle s’arrête ou si elle continue). Pour la cas où `n` vaut 100, la boucle sera parcourue 50 fois. Le total d’instructions élémentaires est donc 3*50+1 ou 151 instructions élémentaires.

L’ordre de grandeur est `O(n)` ou linéaire, comme illustré dans ce graphique :

```{figure} media/Graphique_rech_lin_23.png
---
alt: recherche linéaire
width: 420px
name : fig-rech-lin3
---
```

Notez que l’ordre de grandeur est le même que pour l’exercice précédent, seule la vitesse de croissance change. 

Cette différence de croissance se cache dans la constante c de l’ordre de grandeur `O(cn + a)`. La valeur de `c` dans l’exercice précédent est supérieure à la valeur de c dans cet exercice. Dans un premier lieu, on ne se préoccupe pas de cette constante `c` et on s’intéresse à l’ordre de grandeur général ou tout simplement `O(n)`. Par contre, lorsque l’on doit comparer des algorithmes du même ordre entre eux, il faut s’intéresser à la valeur de cette constante et la calculer.  

````

`````

*******************

```{admonition} Matière à réfléchir IV
:class: attention
Comment faites-vous pour rechercher un mot dans un dictionnaire ? 

Avez-vous utilisé l’algorithme de recherche linéaire qui parcourt tous les éléments un par un ? 

Quelle propriété du dictionnaire nous permet d’utiliser un autre algorithme de recherche que l’algorithme de recherche linéaire ?
```

## Recherche binaire

Si on doit rechercher un élément dans **un tableau déjà trié**, l’{glo}`algo|algorithme` de la recherche linéaire n’est pas optimal. Dans le cas d’un dictionnaire, lorsque l’on recherche un mot, on ne va pas parcourir tous les mots du dictionnaire dans l’ordre. Nous exploitons le fait que les mots du dictionnaire sont triés dans un ordre alphabétique. On commence par ouvrir le dictionnaire sur une page au hasard et on  regarde si le mot recherché se trouve avant ou après cette page. On ouvre ensuite une autre page au hasard dans la partie avant ou après du dictionnaire. On appelle cette méthode la recherche binaire (ou recherche dichotomique), car concrètement elle divise l’espace de recherche par deux à chaque itération (à chaque nouvelle page ouverte, nous éliminons environ la moitié de l’espace de recherche) :

```{code-block} python

# Algorithme de recherche binaire
Tableau Eléments : numérique    # les données du tableau sont triées
Variable n : longueur(Eléments)
Variable elément_recherché : numérique
Variable trouvé : Faux
Variable i : numérique

Tant que trouvé != Vrai et n > 0 :
    indice_milieu = partie_entière(n/2)

    if Eléments[indice_milieu] == elément_recherché :
        trouvé = Vrai
    else :
        if Eléments[indice_milieu] > elément_recherché :
            Eléments = Eléments[:indice_milieu]
        else :
            Eléments = Eléments[indice_milieu+1:]
	n = longueur(Eléments)  
Fin Tant que
Retourner trouvé  

```

Prenez le temps d’étudier cet {glo}`algo|algorithme`. Que fait-il ? La {glo}`bouclewhile|boucle Tant que` permet de rechercher elément_recherché à l’intérieur d’`Eléments` tant qu’il n’est pas trouvé (`trouvé != Vrai`). A chaque itération (à chaque passage dans la {glo}`bouclewhile|boucle`), on vérifie si l’élément au milieu du tableau `Eléments` n’est pas l’`élément recherché`. Si l’ élément au milieu du tableau est plus grand que l’`élément recherché`, cela indique que elément_recherché se trouverait dans la première partie du tableau, les éléments étant triés. Si cet élément du milieu du tableau est plus petit que l’élément recherché, cela indique que l’élément recherché se trouverait au contraire dans la deuxième partie du tableau. 

Dans la recherche linéaire, chaque passage de la {glo}`bouclewhile|boucle` permet de comparer un élément à l’élément recherché et l’espace de recherche diminue seulement de 1. A chaque itération de la recherche binaire, l’espace de recherche est divisé par deux et nous n’avons besoin de parcourir plus qu’une moitié du tableau.



Le nombre d’étapes nécessaires pour rechercher dans un tableau de taille 16 de façon dichotomique est donc le nombre de fois que le tableau peut être divisé en 2 et correspond à 4 (voir la figure ci-dessous) parce que : 


&nbsp;&nbsp;&nbsp;&nbsp;  16 / 2 / 2 / 2 / 2 = 1, donc	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	16 = 2 * 2 * 2 * 2 	 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   ou 16 = 2<sup>4</sup>


```{figure} media/Logn.png
---
alt: le parcours d'un tableau trié est en logn
width: 420px
name : fig-logn
---
Seulement 4 étapes sont suffisantes pour parcourir un tableau trié de 16 éléments à la recherche d’un élément. A chaque étape, l’espace de recherche est divisé par 2.
```


De manière générale, le nombre d’étapes `x` nécessaires pour parcourir un tableau de taille `n` est :

&nbsp;&nbsp;&nbsp;&nbsp; 2 * x = n 

&nbsp;&nbsp;&nbsp;&nbsp; x = log2(n) ~ log(n)   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  # simplification : même ordre de grandeur


L’ordre de croissance de la recherche binaire est donc `O(log(n))`. La figure ci-dessous permet de comparer la croissance de `n` versus `log(n)`. Un {glo}`algo|algorithme` de complexité `O(log(n))` est beaucoup plus rapide qu’un {glo}`algo|algorithme` de complexité linéaire `O(n)`. La lettre O ici est pour « Ordre ».


```{figure} media/Graphique_Complexite_log.png
---
alt: complexité logarithmique
width: 420px
name : fig-comp-log
---
Un algorithme avec un ordre de complexité logarithmique est plus rapide qu’un algorithme de complexité linéaire.
```

## Exercices

```{admonition} Exercice 4 ![](../../../introduction-algorithmique/cours/formulation-solutions/media/plugged.png)
:class: note

Programmer les algorithmes de recherche linéaire et binaire en Python. 

Rechercher une valeur entre 1 et 100 dans un tableau trié qui contient des valeurs de 1 à 100.

Utiliser vos deux programmes pour rechercher un élément : quel algorithme est le plus rapide ? 

Augmenter la taille du tableau à 10000. Rechercher un élément vos deux programmes. Quel algorithme est plus rapide ? Est-ce significatif ? Est-ce que 10000 vous semble être un grand nombre ? 

Est-ce qu’on peut utiliser l’algorithme de recherche binaire si le tableau n’est pas trié ? Essayez.

```

`````{admonition} Solution de l'exercice 4
:class: hint

````{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

```{codeplay}
# algorithme de recherche linéaire
def search_lin(search_list, search_element, verbose=0) :
    
    # boucle pour parcourir la liste
    for element in search_list :

        if verbose :
            print("L'élément comparé est : " + str(element))

        # l'élément de la liste correspond à l'élément recherché
        if element == search_element :
            return True

    # aucun élément ne correspond
    return False


# algorithme de recherche binaire
def search_bin(search_list, search_element, verbose = 0) :
    
    # détermine les limites de la liste considérée
    start = 0
    end = len(search_list)

    # tant que la liste
    while end-start :

        # middle = len(search_list) // 2
        middle = (end-start) // 2 + start

	# compare l'élément au milieu de la liste
        if search_element == search_list[middle] :
            return True

	# l'élément du milieu est plus petit, on cherche dans la fin de la liste
        elif search_element < search_list[middle] :
            end = middle  # search_list = search_list[:middle]
            if verbose :
                print("L'élément se trouve en début de la liste : " + str(search_list))
        
        # l'élément du milieu est plus grand, on cherche dans la fin de la liste
        else :
            start = middle + 1  # search_list = search_list[middle+1:]
            if verbose :
                print("L'élément se trouve en fin de la liste :   " + str(search_list))

	# recalcule la longueur de la liste - condition d'arrêt de la boucle
        # len_search_list = len(search_list)

    # aucun élément ne correspond
    return False


import time
import random

last = 10000
ma_liste = list(range(1,last+1)) 
mon_element = random.randint(1,last)  + last

print("L'élément recherché est : " + str(mon_element))

# mettre verbose à 1 pour avoir une vue de ce qui se passe
# attention, verbose à 1 fausse les temps de calcul
verbose = 0

time_1 = time.time()
search_lin(ma_liste, mon_element, verbose)
time_algo_lin = time.time() - time_1
print("Recherche linéaire : "  + str(time_algo_lin) + " secondes")

time_1 = time.time()
search_bin(ma_liste, mon_element, verbose)
time_algo_bin = time.time() - time_1
print("Recherche binaire : " + str(time_algo_bin) + " secondes")



print("L'algorithme linéaire a été {0:.2f} fois plus lent.".format(time_algo_lin/time_algo_bin))


# Le gain de vitesse est significatif lorsqu'on recherche dans des grandes listes.  Essayez avec last = 1000000

# Les systèmes automatiques traitent des objets plus nombreux que 10000.

# Non, le tableau doit être trié, sinon l'algorithme binaire n'est pas garantit de donner la bonne solution. L'algorithme linéaire va dans ce cas trouver la bonne solution, car il va comparer tous les éléments un par un. Essayer le code ci-dessous en le décommentant.

# random.shuffle(ma_liste)
# print(search_bin(ma_liste, mon_element, verbose))

```

````

`````





````{admonition} Pour aller plus loin
:class: attention

Modifier votre programme  de recherche binaire : au lieu de diviser l’espace de recherche exactement au milieu, le diviser au hasard. Cette recherche avec une composante randomisée s’apparente plus à la recherche que l’on fait lorsque l’on cherche un mot dans le dictionnaire. 

Rechercher une valeur avec les deux versions de recherche binaire. Quel algorithme est plus rapide ?

Rechercher plusieurs valeurs avec les deux versions de recherche binaire. Est-ce que c’est toujours le même algorithme qui est le plus rapide ? 

Quel algorithme est plus rapide en moyenne ?

Rechercher une valeur avec la nouvelle version randomisée de recherche binaire. Exécuter le programme plusieurs fois. Est-ce que ça prend toujours le même temps ? Pourquoi ?

````

## Tri par sélection

Pour rappel, le tri par sélection parcourt le tableau à la recherche du plus petit élément, et ce pour tous les éléments du tableau. Afin de trouver le plus petit élément du tableau, il faut commencer par parcourir toute la liste. Cette opération prend `cn` {glo}`instruction|instructions` : `c` {glo}`instruction|instructions` pour l’accès et la comparaison des éléments du tableau, multiplié par le nombre d’éléments. Il faut ensuite trouver le plus petit élément des éléments restants `n-1`, et ainsi de suite. Concrètement, on se retrouve avec la somme suivante :

&nbsp;&nbsp;&nbsp;&nbsp; cn + c(n-1) + c(n-2) + ... + c(n/2+1) + c(n/2) + ... + 3c + 2c + c

Si on réarrange l’ordre des termes on obtient cette somme d’{glo}`instruction|instructions` :

&nbsp;&nbsp;&nbsp;&nbsp; cn + c + c(n-1) + 2c + c(n-2) + 3c + ... + c(n/2+1) + c(n/2)

On groupe ensuite les termes deux par deux :

&nbsp;&nbsp;&nbsp;&nbsp; (cn + c) + (c(n-1) + 2c) + (c(n-2) + 3c) + ... + (c(n/2+1) + c(n/2))

On obtient ainsi plusieurs fois le même terme :

&nbsp;&nbsp;&nbsp;&nbsp; c(n+1) + c(n+1) + c(n+1) + ... + c(n+1) 

Nous avons commencé par `n` termes, que l’on a combinés deux par deux. On se retrouve donc avec la moitié des termes ou `n/2` :

&nbsp;&nbsp;&nbsp;&nbsp; c(n+1)*n/2	

Le terme qui divise par 2 peut être absorbé dans la {glo}`constante|constante` `c` (la valeur de celle-ci changerait). Finalement, on ajoute une constante a pour prendre en compte le nombre d’{glo}`instruction|instructions` qui ne dépendent pas de la taille des données (p. ex : initialisations au début de l’{glo}`algo|algorithme`) :

&nbsp;&nbsp;&nbsp;&nbsp; c’(n+1)*n + a = c’n2 + c’n + a	ou 	c’= c/2	

Quand `n` est très grand, le terme qui domine cette somme est le `c’n2`. Comme ce qui nous intéresse est l’ordre de grandeur de la croissance, la complexité du tri par sélection est `O(n2)` ou quadratique.

## Exercices

```{admonition} Exercice 5
:class: note

Quelle est la complexité de l’algorithme de tri par insertion ? En d’autres termes, si le tableau contient n éléments, combien faut-il d’instructions pour trier ce tableau ?

```

````{admonition} Solution de l'exercice 5
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

La complexité de l'algorithme par insertion est de n * n = n<sup>2</sup> ou **quadratique**. Il arrive que l'on doive parcourir tous les éléments de la liste n fois, c'est-à-dire pour chaque élément.

```
````

```{admonition} Exercice 6
:class: note

Quelle est la complexité de l’algorithme de tri à bulles ? 

```

````{admonition} Solution des l'exercice 6
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

La complexité de l'algorithme par insertion, par sélection et à bulles est de n * n = n<sup>2</sup> ou **quadratique**. Dans tous ces cas, il arrive que l'on doive parcourir tous les éléments de la liste n fois, c'est-à-dire pour chaque élément.

```
````

## Tri rapide

Tous les {glo}`algo|algorithmes` de tri vus dans le chapitre précédent sont des {glo}`algo|algorithmes`s d’ordre quadratique ou de complexité `O(n2)`. Il existe d’autres {glo}`algo|algorithmes`s de tri qui sont bien plus rapides. Nous allons voir un {glo}`algo|algorithme` de tri tellement rapide, qu’on lui a donné le nom de **<span style="color:rgb(89, 51, 209)">tri rapide</span>**.

On commence par définir un élément pivot : cet élément peut être le premier élément du tableau, l’élément du milieu, le dernier élément ou encore un élément au hasard. Supposons ici que l’élément pivot est le dernier élément du tableau. Une fois que l’on a défini l’élément pivot, on met tous les éléments qui sont plus petits que le pivot à sa gauche et tous les éléments qui sont plus grands que le pivot à droite de celui‑ci (voir la deuxième ligne de la Figure **Tri rapide** ci-dessous). 


<span id="tri-rapide"></span>
```{figure} media/Tri_rapide.png
---
alt: tri rapide
width: 420px
name : fig-tri-rapide
---
**Tri rapide**. Illustration du tri rapide sur le même set de données que celui utilisé pour illustrer les algorithmes de tri vus au chapitre précédent. L’élément pivot est le dernier élément des tableaux à trier.
```

Après la répartition des éléments autour de l’élément pivot en fonction de leur taille, on se retrouve avec deux tableaux non triés, un tableau à chaque côté de l’élément pivot. On continue de traiter ces deux tableaux de la même manière que le tableau initial. On sélectionne pour chaque tableau, celui de gauche et celui de droite, un nouvel élément pivot (le dernier élément du tableau). Pour chaque nouvel élément pivot, on met à gauche les éléments du tableau qui sont plus petits que le pivot. Les éléments qui sont plus grands que le pivot se retrouvent à sa droite. On agit de la sorte jusqu’à ce qu’il ne reste plus que des tableaux à 1 élément.

Intéressons‑nous maintenant à la complexité de cet {glo}`algo|algorithme`. A chaque étape (chaque ligne dans la <a href="#tri-rapide">Figure **Tri rapide**</a> ci-dessus), on compare tout au plus n éléments avec les éléments pivots. Mais combien d’étapes faut-il pour que cet {glo}`algo|algorithme` se termine ? 

A chaque étape de l’{glo}`algo|algorithme`, l’espace de recherche est divisé par 2 (dans le meilleur des cas). Nous avons vu dans l’{glo}`algo|algorithme` de la recherche binaire que lorsqu’on divise l’espace de recherche par deux, on obtient une complexité de `O(log(n))`. Pour obtenir le nombre total d’{glo}`instruction|instructions` élémentaires on multiplie le nombre maximal de comparaisons par étape `n` avec le nombre d’étapes `log(n)`.  Donc l’ordre de complexité du tri rapide est en moyenne `O(nlog(n))`.

Comparons maintenant les différentes croissances des ordres de complexité vus jusqu’ici (voir la Figure ci-dessous). On voit bien que moins d’{glo}`instruction|instructions` élémentaires sont nécessaires pour le tri rapide d’ordre `O(nlog(n))` que pour le tri à sélection d’ordre `O(n2)`. 

```{figure} media/Complexites4.png
---
alt: comparaison de différentes complexités
width: 420px
name : fig-compl-4
---
Comparaison des ordres de complexité vus jusqu’ici. Plus le nombre d’instructions élémentaires grandit avec la taille des données, plus l’algorithme est lent. 
```

````{admonition} Matière à réfléchir V
:class: attention

Appliquer le tri par rapide à un tableau déjà trié. Est-ce que le tri rapide est plus lent ou plus rapide que dans le cas moyen ? 

Quelle est la complexité du tri rapide dans ce cas ? Est-ce que le choix du pivot est important dans ce cas ?

Mêmes questions pour le tri par insertion.

````


## Tri fusion


Un autre {glo}`algo|algorithme` de complexité `O(nlog(n))` est le **<span style="color:rgb(89, 51, 209)">tri fusion</span>**. L’{glo}`algo|algorithme` se base sur l’idée qu’il est difficile de trier beaucoup d’éléments, mais qu’il est très facile de trier deux éléments et de fusionner deux tableaux déjà triés.


<span id="diviser"></span>

L’{glo}`algo|algorithme` commence par une phase de division : on découpe le tableau en deux, jusqu’à arriver à uniquement des tableaux à 1 élément (voir la Figure **Diviser** ci-dessous). Le nombre d’étapes nécessaires pour découper le tableau en tableaux à 1 élément en divisant toujours les tableaux en deux est `log(n)`.



La deuxième phase consiste à fusionner les petits tableaux. On commence par fusionner les éléments 1 à 1, dans un ordre qui dépend de leur taille. Il suffit d’assembler les deux éléments du plus petit au plus grand (voir la 2e ligne de la <a href="#fusionner">Figure **Fusionner**</a> ci-dessous).



```{figure} media/Tri_fusion_diviser.png
---
alt: etape de division dans le tri fusion
width: 360px
name : fig-div-fus
---
**Diviser.** Illustration de la première phase du tri fusion. A chaque étape le tableau est découpé en deux jusqu’à ce qu’il ne reste que des tableaux à 1 élément
```
<span id="fusionner"></span>

```{figure} media/Tri_fusion_fusionner.png
---
alt: etape de fusion dans le tri fusion
width: 360px
name : fig-fus-fus
---
**Fusionner.**Illustration de la deuxième phase du tri fusion. A chaque étape les tableaux sont fusionnés par paires de deux, en faisant attention à respecter l’ordre de tri. On continue ainsi jusqu’à ce qu’il ne reste qu’un tableau unique.
```

Dans les prochaines étapes (lignes 3 et 4 de la Figure **Fusionner** ci-dessus), on continue à fusionner les tableaux par paires de deux. Il est facile de fusionner ces tableaux, car ils sont déjà triés. Tout d’abord, on compare les premiers éléments des deux tableaux et on prend le plus petit des deux. Concrètement, on enlève le plus petit élément des deux tableaux pour commencer un nouveau tableau fusionné. On compare ensuite les premiers éléments des éléments restants dans les tableaux à fusionner et on prend à nouveau le plus petit des deux. On continue de la sorte jusqu’à ce qu’il ne reste pas d’éléments dans les tableaux à fusionner. 

Chaque étape de la phase de fusion consiste à comparer deux éléments `n` fois, autant qu’il y a d’éléments à fusionner dans le tableau. Elle prend donc un temps qui grandit linéairement en fonction de la taille du tableau `n`. En tout il y a besoin de `log(n)` d’étapes ce qui nous donne l’ordre de complexité `O(nlog(n))`.


```{admonition} Le saviez-vous ?
:class: hint

Le tri rapide et le tri fusion se basent sur la stratégie algorithmique de résolution de problèmes **<span style="color:rgb(89, 51, 209)">« diviser pour régner »</span>**. Cette stratégie qui consiste à :

&nbsp;&nbsp;&nbsp;&nbsp; Diviser : décomposer le problème initial en sous-problèmes ;

&nbsp;&nbsp;&nbsp;&nbsp; Régner : résoudre les sous-problèmes ;

&nbsp;&nbsp;&nbsp;&nbsp; Combiner : calculer une solution au problème initial à partir des solutions des sous-problèmes.

Les sous-problèmes étant plus petits, ils sont plus faciles et donc plus rapides à résoudre. Les algorithmes de ce type sont efficaces et se prêtent à la résolution en parallèle (p.ex.  multiprocesseurs).  

```

````{admonition} Pour aller plus loin
:class: attention

La première question que l’on se pose lorsqu’on analyse un algorithme est son ordre de complexité. Si l’algorithme est trop lent, il ne sera pas utilisable dans la vie réelle. Lorsqu’on parle de complexité, on pense en fait à la complexité moyenne, mais on peut également calculer la complexité dans le meilleur et dans le pire cas.

Par exemple, si on trie un tableau qui est en fait déjà trié avec le tri par insertion, la complexité dans ce cas est linéaire ou `O(n)`.  Au contraire, si on trie ce même tableau avec le tri rapide, la complexité dans ce cas est quadratique ou O(n<sup>2</sup>). On voit donc que selon le tableau que l’on trie, le tri rapide peut être bien plus lent que le tri par insertion.

Une analyse complète d’un algorithme consiste à calculer la complexité non seulement dans le **<span style="color:rgb(89, 51, 209)">cas moyen</span>**, mais aussi dans le **<span style="color:rgb(89, 51, 209)">meilleur cas</span>** et dans le **<span style="color:rgb(89, 51, 209)">pire cas</span>**. 

Une analyse complète va également calculer les constantes qui influencent l’ordre de complexité. Ces constantes ne sont pas importantes lors d’une première analyse d’un algorithme. En effet, les constantes n’ont que peu d’effet pour une grande taille des données n, c’est uniquement le terme qui grandit le plus rapidement en fonction de n qui compte, et qui figure dans un premier temps dans l’ordre de complexité. Par contre, lorsque l’on souhaite comparer deux algorithmes de la même complexité, il faut estimer les constantes et prendre celui des deux avec la plus petite constante.

````


```{admonition} Le saviez-vous ?
:class: hint
La complexité ne reflète pas la difficulté à implémenter un algorithme, comme on pourrait le croire, mais à quel point l’algorithme se complexifie au fur et à mesure que le nombre des entrées augmente. La complexité mesure le temps d’exécution d’un algorithme (ou sa rapidité) en termes du nombre d’instructions élémentaires exécutées en fonction de la taille des données. Mais est-ce que *<span style="color:rgb(89, 51, 209)">complexe</span>* veut dire la même chose que *<span style="color:rgb(89, 51, 209)">compliqué</span>* ? Une chose compliquée est difficile à saisir ou à faire, alors qu’une chose complexe est composée d’éléments avec de nombreuses interactions imbriquées. 
```

## Exercices

```{admonition} Exercice 7
:class: note

Si une instruction prend 10<sup>-6</sup> secondes, combien de temps faut-il pour trier un tableau d’1 million d’éléments avec le tri à sélection comparé au tri rapide (sans tenir compte de la constante) ? 
```

````{admonition} Solution de l'exercice 7
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Pour trier 1 million d’éléments, le tri par sélection prend 10<sup>6</sup>*10<sup>6</sup> *10<sup>-6</sup> secondes ou 1 million de secondes (équivalent à plus de 11 jours), alors que le tri rapide a besoin de log2(10<sup>6</sup>)*10<sup>6</sup> *10<sup>-6</sup> ou ~20 secondes. 

Cette différence de temps est suffisante pour rendre rédhibitoire l’utilisation du tri par sélection. Pensez au nombre de clients qu’un réseau social possède, ou au nombre de produits qu’un supermarché doit gérer.
```

````

```{admonition} Exercice 8
:class: note

Trier le tableau suivant avec l’algorithme de tri rapide : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main, en prenant le dernier élément comme pivot. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

Est-ce que le choix du pivot est important ?

```

````{admonition} Solution de l'exercice 8
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

Le choix du pivot est important et à prendre en comptes si on a des indications sur le tableau à trier.

```
````

```{admonition} Exercice 9
:class: note

Trier le tableau suivant avec l’algorithme de tri fusion : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

N’y a-t-il qu’une seule solution ?

```

````{admonition} Solution de l'exercice 9
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Lors de la première étape du tri fusion, on divise le tableau en deux, jusqu’à arriver à des tableaux d’un seul élément :

&nbsp;&nbsp;&nbsp;&nbsp; 	[3, 6, 8, 7]  [1, 9, 4, 2, 5]

&nbsp;&nbsp;&nbsp;&nbsp; 	[3, 6]  [8, 7]  [1, 9]  [4, 2, 5]

&nbsp;&nbsp;&nbsp;&nbsp; 	[3]  [6]  [8]  [7]  [1]  [9]  [4]  [2, 5]

&nbsp;&nbsp;&nbsp;&nbsp; 	[3]  [6]  [8]  [7]  [1]  [9]  [4]  [2]  [5]

Une autre solution consiste par diviser le tableau en deux tableaux de 5 et 4 éléments lors de la première division. Lors de la deuxième étape du tri fusion, on fusionne les tableaux deux à deux, en respectant l’ordre de tri :

&nbsp;&nbsp;&nbsp;&nbsp; 	[3, 6]  [7, 8]  [1, 9]   [2, 4]  [5]

&nbsp;&nbsp;&nbsp;&nbsp; 	[3, 6, 7, 8]  [1, 2, 4, 9]  [5]

&nbsp;&nbsp;&nbsp;&nbsp; 	[1, 2, 3, 4, 6, 7, 8, 9]  [5]

Concrètement, pour fusionner les tableaux [3, 6, 7, 8]  [1, 2, 4, 9], on prend toujours le plus petit des deux premiers éléments des deux tableaux :

&nbsp;&nbsp;&nbsp;&nbsp; [3, 6, 7, 8]  [1, 2, 4, 9]	&nbsp;&nbsp; → &nbsp;&nbsp; 3 > 1  &nbsp;&nbsp; → &nbsp;&nbsp; on prend 1  &nbsp;&nbsp;	→ &nbsp;&nbsp; 	[1]

&nbsp;&nbsp;&nbsp;&nbsp; 		[3, 6, 7, 8]  [2, 4, 9]    &nbsp;&nbsp; → &nbsp;&nbsp;  3 < 2	&nbsp;&nbsp; → &nbsp;&nbsp; on prend 2 	&nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2]

&nbsp;&nbsp;&nbsp;&nbsp; 		[3, 6, 7, 8]  [4, 9]	&nbsp;&nbsp; → &nbsp;&nbsp;  3 < 4  	&nbsp;&nbsp; → &nbsp;&nbsp; on prend 3  	&nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2, 3]

&nbsp;&nbsp;&nbsp;&nbsp; 		[6, 7, 8]  [4, 9]    	&nbsp;&nbsp; → &nbsp;&nbsp;  6 > 4	&nbsp;&nbsp; → &nbsp;&nbsp;on prend 4 &nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2, 3, 4]

&nbsp;&nbsp;&nbsp;&nbsp; 		[6, 7, 8]  [9]    		&nbsp;&nbsp; → &nbsp;&nbsp;  6 < 9	&nbsp;&nbsp; → &nbsp;&nbsp; on prend 6 	&nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2, 3, 4, 6]

&nbsp;&nbsp;&nbsp;&nbsp; 		[7, 8]  [9]    		&nbsp;&nbsp; → &nbsp;&nbsp;  7 < 9	&nbsp;&nbsp; → &nbsp;&nbsp; on prend 7 	&nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2, 3, 4, 6, 7]

&nbsp;&nbsp;&nbsp;&nbsp; 		[8]  [9]    		&nbsp;&nbsp; → &nbsp;&nbsp;  8 < 9	&nbsp;&nbsp; → &nbsp;&nbsp; on prend 8 	&nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2, 3, 4, 6, 7, 8]

&nbsp;&nbsp;&nbsp;&nbsp; 		[  ]  [9]    		  		&nbsp;&nbsp; → &nbsp;&nbsp; on prend 9 &nbsp;&nbsp; → &nbsp;&nbsp; 	[1, 2, 3, 4, 6, 7, 8, 9]

On procède de la même manière pour fusionner le tableau contenant le chiffre et on arrive ainsi à la solution du tableau trié : 

&nbsp;&nbsp;&nbsp;&nbsp; 	[1, 2, 3, 4, 5, 6, 7, 8, 9]

````

```{admonition} Exercice 10
:class: note

Trier le tableau suivant avec l’algorithme de tri par sélection : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```

````{admonition} Solution de l'exercice 10
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

```{admonition} Exercice 11
:class: note

Trier le tableau suivant avec l’algorithme de tri par insertion : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```

````{admonition} Solution de l'exercice 11
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

```{admonition} Exercice 12
:class: note

Trier le tableau suivant avec l’algorithme de tri à bulles : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```


