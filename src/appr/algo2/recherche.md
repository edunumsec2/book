# Algorithmes de recherche

Les ordinateurs passent la majorité de leur temps à chercher : ils cherchent des fichiers, ils cherchent des sites Web, ils cherchent des informations dans un site Web, ils cherchent votre compte lorsque vous vous loguez sur un site Web, ils cherchent des *posts* à vous montrer et des personnes à qui vous connecter. Nous allons commencer par estimer la complexité de deux algorithmes de recherche importants. 

La complexité ne reflète pas la difficulté à implémenter un algorithme, comme on pourrait le croire, mais à quel point l’algorithme se complexifie au fur et à mesure que le nombre des entrées augmente. La complexité mesure le temps d’exécution d’un algorithme (ou sa rapidité) en termes du nombre d’instructions élémentaires exécutées en fonction de la taille des données. 


## Recherche linéaire 

La manière la plus simple pour rechercher un élément dans un tableau (une liste en Python) consiste à parcourir le tableau et à comparer l’élément recherché à tous les éléments du tableau :

```{code-block} 

# Algorithme de recherche&nbsp;linéaire

Tableau Eléments            # données stockées dans un tableau (une liste en Python)
n ← longueur(Eléments)      # la variable n contient le nombre d'éléments 
elément_recherché ← entrée  # l'élément recherché est un paramètre de l'algorithme
i ← 1                       # index pour parcourir la liste

Répéter Pour i = 1 à n
    si Eléments[i] == élément_recherché
        Retourner « Oui »
Fin Répéter

Retourner « Non »

```

Quelle est la complexité de cet {glo}`algo|algorithme` de **<span style="color:rgb(89, 51, 209)">recherche&nbsp;linéaire</span>** ? Pour répondre à cette question, il faut estimer le nombre d’{glo}`instruction|instructions` élémentaires nécessaires pour rechercher un élément dans un tableau. Ce nombre dépend naturellement de la taille du tableau $n$ : plus le nombre d'éléments dans le tableau est grand, plus on a besoin d'instructions pour retrouver un élément.

Supposons que le tableau contienne $10$ éléments. Pour trouver l’élément recherché, il faut au moins deux {glo}`instruction|instructions` par élément du tableau : une instruction pour accéder à l'élément du tableau (ou `Elements[i]`) et une autre instruction pour le comparer à `élément_recherché`. Dans le cas du tableau à $10$ éléments, cet algorithme prendrait $20$ instructions élémentaires, $2$ (instructions) multiplié par le nombre d'éléments dans le tableau. Mais&nbsp;si le tableau contient $100$ éléments, le nombre d’instructions élémentaires monte à $200$. De manière  générale, si le nombre d’éléments dans le tableau est $n$, cela prend $2n$ instructions pour le parcourir et pour comparer ses éléments. 

Cette estimation n’est pas exacte. Nous n’avons pas pris en compte les instructions élémentaires qui permettent d’incrémenter `i` et de vérifier si `i == longueur(Nombres)`. Lorsqu’on prend en compte ces 2 instructions supplémentaires liées à l'utilisation de `i`, le nombre d’instructions passe de $200$ à $400$ (ce qui correspond à $4n$). Il faut également y ajouter les $4$ instructions d’initialisation avant la {glo}`bouclewhile|boucle`, plus l’instruction de retour à la fin de l'algorithme, ce qui fait monter le nombre d'instructions de $400$ à&nbsp;$405$ ou&nbsp;$(4n + 5)$. Attention, le nombre exact peut être différent, car il dépend de l'implémentation sur la machine. Mais,&nbsp;ce&nbsp;qui nous intéresse ici n’est pas tant le nombre exact d’instructions, si c'est $205$ ou $410$ ou $815$. Ce qui nous intéresse ici est plutôt l'**<span style="color:rgb(89, 51, 209)">ordre de grandeur</span>** de l'algorithme ou comment le nombre d’instructions élémentaires grandit avec la taille du tableau $n$. 

Cet algorithme est de complexité&nbsp;**<span style="color:rgb(89, 51, 209)">linéaire</span>**. Une complexité&nbsp;linéaire implique que le nombre d’instructions élémentaires croît linéairement en fonction du nombre d’éléments des données : $cn + a$, ou $c$ et $a$ sont des {glo}`constante|constantes`. Dans ce cas précis, $c$ vaut $4$ et $a$ vaut $5$. Si le tableau contient $10$ éléments, il faut environ $45$ instructions ; pour $100$ éléments il faut environ $405$ instructions ; pour $1000$ éléments il faut environ $4005$ instructions et ainsi de suite. Le nombre d’instructions grandit de manière linéaire en fonction de la taille des données $n$, et cette relation est représentée par une ligne lorsqu'on la dessine (voir la figure ci&#8209;dessous).

```{figure} media/Complexité_linéaire.png
---
alt: Ordre de grandeur linéaire
width: 500px
name : fig-comp-log
---
**Complexité linéaire**. La complexité de l'algorithme de recherche&nbsp;linéaire, comme son nom l'indique, est linéaire. La relation entre la taille du tableau $n$ et le nombre d'instructions nécessaires pour retrouver un élément dans ce tableau représente une ligne.
```

```{exercise} Compter jusqu'à $n$

Ecrire un algorithme qui affiche tous les nombres de $1$ à $n$. 

Combien d’instructions élémentaires sont nécessaires lorsque $n$ vaut $100$ ? 

Quelle est la complexité de cet algorithme ?  
```



````{solution} 
```{code-block} python
Variable n : numérique
Variable i : numérique

Répéter Pour i = 1 à n
    Afficher(i)
Fin Pour
```

L’initialisation des variables `n` et `i` compte pour $2$ instructions élémentaires. Chaque passage de la boucle correspond à trois instructions élémentaires : $1$ instruction qui affiche `i`, 1 instruction qui incrémente `i` de 1 et finalement une instruction qui compare `i` à `n` (pour savoir si la boucle s’arrête ou si elle continue). Le&nbsp;total d’instructions élémentaires pour le cas où `n` vaut $100$ est $3 * 100 + 2$ ou $302$ instructions élémentaires.

Il faut se rendre compte que cette estimation du nombre d’instructions élémentaires est approximatif, et non pas exact. Par exemple, l’instruction élémentaire `Afficher(i)` englobe certainement plusieurs instructions à l’exécution et prend de plus en plus de temps à mesure que `i` grandit (affiche de plus en plus de caractères).

La complexité (ou l’ordre de grandeur) de cet algorithme est linéaire, comme illustré dans ce graphique : 

```{figure} media/Graphique_rech_lin_22.png
---
alt: recherche&nbsp;linéaire
width: 500px
name : fig-rech-lin2
---
```
````

```{exercise} Compter par pas de 2

Ecrire un algorithme qui affiche tous les nombres *pairs* de $1$ à $n$. 

Combien d’instructions élémentaires sont nécessaires lorsque $n$ vaut $100$ ? 

Quelle est la complexité de cet algorithme ? 
```


````{solution} 
```{code-block} python
Variable n : numérique
Variable i : numérique

Répéter Pour i = 2 à n, par pas de 2
    Afficher(i)
Fin Pour
```

La seule ligne qui change par rapport à la solution de l’exercice précédent est l’incrément de la boucle par pas de $2$. 

L’initialisation des variables `i` et `n` compte pour 2 instructions élémentaires. Chaque passage de la boucle correspond à trois instructions élémentaires : 1 instruction qui affiche `i`, $1$ instruction qui incrémente `i` de $2$ et finalement $1$ instruction qui compare `i` à `n` (pour savoir si la boucle s’arrête ou si elle continue). Pour le cas où `n` vaut 100, la boucle sera parcourue $50$ fois (par pas de $2$). Le&nbsp;total d’instructions élémentaires est donc $3 * 50 + 2$ ou $152$ instructions élémentaires.

La complexité (ou l’ordre de grandeur) de cet algorithme est également linéaire, comme illustré dans le graphique. Il faut noter que l’ordre de grandeur est le même que pour l’exercice précédent, seule la vitesse de croissance change. 

```{figure} media/Graphique_rech_lin_23.png
---
alt: recherche&nbsp;linéaire
width: 500px
name : fig-rech-lin3
---
```

La différence de croissance se cache dans la constante $c$ de l’ordre de grandeur $cn + a$. La valeur de $c$ dans l’exercice précédent est supérieure à la valeur de $c$ dans cet exercice. Dans un premier temps, on peut ignorer la valeur de cette constante $c$. Cependant elle peut devenir importante lorsque l’on doit comparer des algorithmes du même ordre entre eux.  

````

```{exercise} Recherche linéaire🔌

Programmer l'algorithme de recherche&nbsp;linéaire en Python. Rechercher une valeur entre 1 et 1000000 dans un tableau qui contient les valeurs allant de $1$ à $1000000$.

Pour quelle valeur l'algorithme est le plus rapide ? Le plus lent ? Indice : utiliser le module `time` pour chronometrer le temps d'exécution.

```



````{solution} 

Voici un programme possible pour l'algorithme de recherche&nbsp;linéaire. Si on chronomètre le temps d'exécution, la valeur $1$ est trouvée très rapidement en comparaison à la valeur 1000000. C'est beaucoup plus lent de rechercher une valeur qui se trouve à la fin du tableau, qu'au début du tableau. 

```{codeplay}

# algorithme de recherche&nbsp;linéaire
def search_lin(search_list, search_element, verbose=0) :
    
    # boucle pour parcourir la liste
    for element in search_list :

        if verbose :
            print("L'élément comparé est : " + str(element) + "\n")

        # l'élément de la liste correspond à l'élément recherché
        if element == search_element :
            return True

    # aucun élément ne correspond
    return False


import time

last = 1000000
ma_liste = list(range(1,last+1)) 

# mettre verbose à 1 pour avoir une vue de ce qui se passe
# attention, cela fausse les temps de calcul (plus temps d'affichage) 
verbose = 0

# chronomètre le temps de recherche de l'élément 1000000
time_start = time.time()
search_lin(ma_liste, last, verbose)
time_1000000= time.time() - time_start
print("Recherche linéaire de 1000000 : "  + str(round(time_1000000,7)) + " secondes.\n")

# chronomètre le temps de recherche de l'élément 1
time_start = time.time()
search_lin(ma_liste, 1, verbose)
time_1 = time.time() - time_start
print("Recherche linéaire de 1 : "  + str(round(time_1,7)) + " secondes.")

```
````

```{exercise} Recherche linéaire (dans le désordre)🔌

On a vu dans l'exercice précédent que cela prend moins de temps pour trouver un élément au début de la liste qu'un élément de la fin de la liste. Qu'est-ce qui arrive si les éléments de la liste ne sont pas dans l'ordre ? Essayer en utilisant la fonction `shuffle()` du module `random`.

```

````{solution} 
Si on mélange l'ordre des éléments, la valeur $1$ pourrait se retrouver en fin de tableau et pourrait prendre très longtemps à retrouver. Au contraire, la valeur 1000000 pourrait se retrouver en début de tableau et pourrait prendre très peu de temps à retrouver. La situation est donc beaucoup moins prévisible.

```{codeplay}

# algorithme de recherche&nbsp;linéaire
def search_lin(search_list, search_element, verbose=0) :
    
    # boucle pour parcourir la liste
    for element in search_list :

        if verbose :
            print("L'élément comparé est : " + str(element) + "\n")

        # l'élément de la liste correspond à l'élément recherché
        if element == search_element :
            return True

    # aucun élément ne correspond
    return False


import time
import random

last = 1000000
ma_liste = list(range(1,last+1)) 

# mettre verbose à 1 pour avoir une vue de ce qui se passe
# attention, verbose à 1 fausse les temps de calcul (rajoute du temps d'affichage) 
verbose = 0

# mélange les éléments du tableau au hasard
random.shuffle(ma_liste);
print("Les éléments ne sont plus dans l'ordre.\n")

# chronomètre le temps de recherche de l'élément 1000000
time_start = time.time()
search_lin(ma_liste, last, verbose)
time_1000000 = time.time() - time_start
print("Recherche linéaire de 1000000 : "  + str(round(time_1000000,7)) + " secondes.\n")

# chronomètre le temps de recherche de l'élément 1
time_start = time.time()
search_lin(ma_liste, 1, verbose)
time_1 = time.time() - time_start
print("Recherche linéaire de 1 : "  + str(round(time_1,7)) + " secondes.")

```
````


````{togofurther} 

Pour décrire mathématiquement les ordres de complexité, on utilise la notation « Grand O ». Pour dire qu'un ordre de complexité est linéaire, on écrit par exemple qu'il est $O(n)$.

````


## Recherche binaire


```{thinkingmatter} Le dictionnaire

Comment faites&#8209;vous pour rechercher un mot dans un dictionnaire ? 

Utilisez&#8209;vous l’algorithme de recherche&nbsp;linéaire, parcourez&#8209;vous tous les éléments un à un ? 

Quelle propriété du dictionnaire nous permet d’utiliser un autre algorithme de recherche que l’algorithme de recherche&nbsp;linéaire ?
```

<span id=rech-bin></span> Si on doit rechercher un élément dans un tableau qui est **déjà trié**, l’{glo}`algo|algorithme` de recherche&nbsp;linéaire n’est pas optimal. Dans le cas de la recherche d'un mot dans un dictionnaire, la recherche&nbsp;linéaire implique que l'on va parcourir tous les mots du dictionnaire dans l’ordre, jusqu'à trouver le mot recherché. Mais&nbsp;nous ne recherchons pas les mots dans un dictionnaire de la sorte. Nous exploitons le fait que les mots du dictionnaire sont triés dans un ordre alphabétique. On commence par ouvrir le dictionnaire sur une page au hasard et on  regarde si le mot recherché se trouve avant ou après cette page. On ouvre ensuite une autre page au hasard dans la partie retenue du dictionnaire. On appelle cette méthode la **<span style="color:rgb(89, 51, 209)">recherche&nbsp;binaire</span>** (ou&nbsp;la&nbsp;recherche&nbsp;dichotomique), car à&nbsp;chaque itération elle ***<span style="color:rgb(13, 204, 166)">divise l’espace de recherche en deux</span>***. En&nbsp;effet, à&nbsp;chaque nouvelle page ouverte, nous éliminons environ la moitié du dictionnaire qui nous restait à parcourir. Voici une description de l'algorithme de recherche&nbsp;binaire :

```{code-block}

# Algorithme de recherche&nbsp;binaire

Tableau Eléments            # les données du tableau (liste en Python) sont triées
n ← longueur(Eléments)      # la variable n contient le nombre d'éléments 
elément_recherché ← entrée  # l'élément recherché est un paramètre de l'algorithme
trouvé ← Faux               # indique si l'élément à été retrouvé 
index_début ← 0             # au début on cherche dans tout le tableau 
index_fin ← n               # au début on cherche dans tout le tableau 

# tant que l'élément n'est pas trouvé et que le sous-tableau retenu n'est pas vide
Tant que trouvé != Vrai et n > 0 :

    # on identifie le milieu du sous-tableau retenu
    index_milieu = (index_fin - index_début)/2 + index_début

    # si l'élément recherché correspond à l'élément du milieu du sous-tableau retenu
    if Eléments[index_milieu] == elément_recherché :
        trouvé = Vrai
    else :
        
        # si l'élément du milieu est plus grand que l'élément recherché
        # on retient la première moitié comme sous-tableau 
        if Eléments[index_milieu] > elément_recherché :
            index_fin = index_milieu
        
        # si l'élément du milieu est plus petit que l'élément recherché
        # on retient la deuxième moitié comme sous-tableau  
        else :
            index_début = index_milieu+1

    # calcule le nombre d'éléments du sous-tableau retenu
    n = index_fin - index_début

Fin Tant que

Retourner trouvé  

```

Prenons le temps d’étudier cet {glo}`algo|algorithme`. Que fait&#8209;il ? La {glo}`bouclewhile|boucle Tant que` permet de parcourir le tableau `Eléments` et d'y rechercher `elément_recherché` tant qu’il n’est pas trouvé (tant que `trouvé != Vrai`). A&nbsp;la première itération (au premier passage dans la {glo}`bouclewhile|boucle`, on vérifie si l’élément au milieu du tableau `Eléments` n’est justement pas l'élément recherché. Les éléments de la liste étant triés, si l’élément au milieu du tableau est plus grand que l’élément recherché, cela indique que `elément_recherché` se trouve dans la première partie du tableau. Si l'élément au milieu du tableau est plus petit que l’élément recherché, cela indique que l’élément recherché se trouve au contraire dans la deuxième moitié du tableau. Pour la suite de la recherche, on retient soit la première, soit la deuxième moitié du tableau, selon si l'élément recherché est plus grand ou plus petit que l'élément du milieu. A&nbsp;chaque prochaine itération (à chaque passage dans la {glo}`bouclewhile|boucle`), on vérifie si l’élément au milieu du nouveau sous&#8209;tableau retenu n’est pas l’élément recherché. 

Dans la **<span style="color:rgb(89, 51, 209)">recherche linéaire</span>**, chaque passage de la {glo}`bouclewhile|boucle` permettait de comparer un élément à l’élément recherché et l’espace de recherche diminuait seulement de $1$ (l'espace de recherche correspond aux nombre d'emplacements encore possibles). Dans la **<span style="color:rgb(89, 51, 209)">recherche binaire</span>**, chaque passage de la {glo}`bouclewhile|boucle` divise l’espace de recherche par deux et nous n’avons besoin de parcourir plus qu’une moitié (de la moitié, de la moitié, de la moitié, etc.) du tableau.

Le nombre d’étapes nécessaires pour rechercher un élément dans un tableau de taille $16$ de façon dichotomique correspond donc au nombre de fois que le tableau peut être divisé en $2$ et correspond à $4$ (comme on peut le voir sur la figure ci&#8209;dessous), parce que : 


&nbsp;&nbsp;&nbsp;&nbsp;  $16 / 2 / 2 / 2 / 2 = 1$ &nbsp;&nbsp;  donc	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	

&nbsp;&nbsp;&nbsp;&nbsp; $2 * 2 * 2 * 2 = 16$ &nbsp;&nbsp;    ou 


&nbsp;&nbsp;&nbsp;&nbsp; $ 2^{4} = 16$


```{figure} media/Logn.png
---
alt: le parcours d'un tableau trié de 16 éléments
width: 500px
name : fig-logn
---
**Exemple de parcours d'un tableau trié.** Seulement $4$&nbsp;étapes sont suffisantes pour parcourir un tableau trié de $16$&nbsp;éléments à la recherche d’un élément qui se trouve à la onzième position. A&nbsp;chaque&nbsp;étape, l’espace de recherche est divisé par&nbsp;$2$. Si le tableau n'était pas trié, $11$&nbsp;étapes seraient nécessaires (on doit vérifier chaque élément dans l'ordre). 

```


Si on généralise, le nombre d’étapes $x$ nécessaires pour parcourir un tableau de taille $n$ est :


&nbsp;&nbsp;&nbsp;&nbsp; $2^{x}$ = n &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; par conséquent


&nbsp;&nbsp;&nbsp;&nbsp; $x = log_{2}(n) \sim log(n)$   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  la simplification peut être faite car l’ordre de grandeur est le même

La complexité de l'algorithme de recherche&nbsp;binaire est donc **<span style="color:rgb(89, 51, 209)">logarithmique</span>**, lorsque $n$ grandit nous avons besoin de $log(n)$ opérations. La figure ci&#8209;dessous permet de comparer les ordres de grandeur logarithmique et linéaire. On remarque qu'un algorithme de complexité&nbsp;logarithmique est beaucoup plus rapide qu’un algorithme de complexité&nbsp;linéaire, car il a besoin de beaucoup moins d'instructions élémentaires pour trouver une solution.


```{figure} media/Graphique_lin_log.png
---
alt: comparaison de complexités logarithmique et linéaire
width: 500px
name : fig-graph-log
---
**Comparaison de complexités logarithmique et linéaire**. Un algorithme de complexité&nbsp;logarithmique est plus rapide qu’un algorithme de complexité&nbsp;linéaire.
```


L'algorithme de la recherche&nbsp;binaire se base sur une stratégie algorithmique de résolution de problèmes très efficace, que l'on appelle la stratégie **<span style="color:rgb(89, 51, 209)">« diviser&nbsp;pour&nbsp;régner »</span>**. Cette stratégie qui consiste à :

&nbsp;&nbsp;&nbsp;&nbsp; **<span style="color:rgb(89, 51, 209)">Diviser :</span>** décomposer le problème initial en sous&#8209;problèmes ;

&nbsp;&nbsp;&nbsp;&nbsp; **<span style="color:rgb(89, 51, 209)">Régner :</span>** résoudre les sous&#8209;problèmes ;

&nbsp;&nbsp;&nbsp;&nbsp; **<span style="color:rgb(89, 51, 209)">Combiner :</span>** calculer une solution au problème initial à partir des solutions des sous&#8209;problèmes.

Les sous&#8209;problèmes étant plus petits, ils sont plus faciles et donc plus rapides à résoudre. Les algorithmes de ce type en plus d'être efficaces, se prêtent à la résolution en parallèle (par exemple sur des multiprocesseurs).  



<!-- 
```{image} media/Graphique_Complexite_log.png
:width: 400px
:height: 300px
```
Un algorithme avec un ordre de complexité logarithmique est plus rapide qu’un algorithme de complexité linéaire
<br>
-->


```{exercise} Recherche binaire 🔌

Programmer l'algorithme de recherche&nbsp;binaire en Python. Rechercher une valeur entre 0 et 100 dans un tableau qui contient les valeurs allant de $1$ à $99$.

Pour quelle valeur l'algorithme est le plus rapide ? Pour quelle valeur l'algorithme est le plus lent ? Indice : mettre un mode verbose pour afficher ce que fait l’algorithme. 

```

````{solution} 
Voici un programme possible pour l'algorithme de recherche&nbsp;binaire. L'algorithme est le plus rapide si on recherche la valeur qui se trouve au milieu du tableau (la valeur $50$) et il est le plus lent lorsque l'on recherche la première ou dernière valeur du tableau (la valeur $1$ ou $99$). 

```{codeplay}
# algorithme de recherche&nbsp;binaire
def search_bin(search_list, search_element, verbose = 0) :
    
    # détermine les limites de la liste considérée
    start = 0
    end = len(search_list)
    
    # tant que la liste
    while end-start :
    
        # accède l'élément du milieu, division entière, il faut un index
        middle = (end-start) // 2 + start 
        if verbose :
            print("Elément comparé : " + str(search_list[middle]) +"\n")
    
        # compare l'élément au milieu de la liste
        if search_element == search_list[middle] :
            if verbose :
                print("Elément retrouvé !\n")
            return True      
    
        # l'élément est plus petit que l'élément du milieu
        elif search_element < search_list[middle] :
            # search_list devient dans la première moitié de search_list
            end = middle 
    
            if verbose :
                print("1ère moitié de la liste : " + str(search_list[start:end]) + "\n")
    
        # l'élément est plus grand que l'élément du milieu
        else :
            # search_list devient la deuxième moitié de search_list
            start = middle + 1  

            if verbose :
                print("2ème moitié de la liste : " + str(search_list[start:end]) + "\n")

    # aucun élément ne correspond
    if verbose :
        print("L'élément " + str(search_list[middle]) + " n'a pas été retrouvé...\n")
    return False


ma_liste = list(range(1,100)) 
mon_element = 25

# recherche de l’élément mon_element
search_bin(ma_liste, mon_element, 1)

```
````

```{exercise} Recherche binaire (dans le désordre) 🔌

Est&#8209;ce qu’on peut utiliser l’algorithme de recherche&nbsp;binaire si le tableau n’est pas trié ? Essayer avec la fonction `shuffle()` du module `random`.

```


````{solution} 
Si le tableau n'est pas trié, l'algorithme n'est pas garanti de trouver l'élément recherché, car il peut facilement passer à côté. 

```{codeplay}
# algorithme de recherche&nbsp;binaire
def search_bin(search_list, search_element, verbose = 0) :
    
    # détermine les limites de la liste considérée
    start = 0
    end = len(search_list)
    
    # tant que la liste
    while end-start :
    
        # accède l'élément du milieu, division entière, il faut un index
        middle = (end-start) // 2 + start 
        if verbose :
            print("Elément comparé : " + str(search_list[middle]) +"\n")
    
        # compare l'élément au milieu de la liste
        if search_element == search_list[middle] :
            if verbose :
                print("Elément retrouvé !\n")
            return True      
    
        # l'élément est plus petit que l'élément du milieu
        elif search_element < search_list[middle] :
            # search_list devient dans la première moitié de search_list
            end = middle 
    
            if verbose :
                print("1ère moitié de la liste : " + str(search_list[start:end]) + "\n")
    
        # l'élément est plus grand que l'élément du milieu
        else :
            # search_list devient la deuxième moitié de search_list
            start = middle + 1  

            if verbose :
                print("2ème moitié de la liste : " + str(search_list[start:end]) + "\n")

    # aucun élément ne correspond
    if verbose :
        print("L'élément " + str(search_list[middle]) + " n'a pas été retrouvé...\n")
    return False


import random

last = 99
ma_liste = list(range(1,last+1)) 

mon_element = random.randint(1,last) 
print("L'élément recherché est : " + str(mon_element) + "\n")

# recherche de l’élément mon_element
search_bin(ma_liste, mon_element, 1)

random.shuffle(ma_liste)
print("Tableau mélangé... : " + str(ma_liste) + "\n")
search_bin(ma_liste, mon_element, 1)

```
````




```{exercise} Recherche linéaire versus binaire 🔌

Reprendre les programmes de recherche&nbsp;linéaire et recherche&nbsp;binaire en Python et les utiliser pour rechercher un élément dans un tableau à $100$ éléments : quel algorithme est le plus rapide ? 

Augmenter la taille du tableau à $1000$, $10000$, $100000$, $1000000$ et $10000000$. Rechercher un élément avec vos deux programmes. Quel algorithme est plus rapide ? Est&#8209;ce significatif ? 

Est&#8209;ce que **un million** vous semble être un grand nombre pour une taille de données ? 

```


````{solution} 
Comme prévu par les estimations de complexité, avec sa complexité&nbsp;logarithmique, c'est l'algorithme de la recherche&nbsp;binaire qui est plus rapide. Le gain de temps devient de plus en plus important au fur et à mesure que le nombre d'éléments dans le tableau grandit. Pour $100$&nbsp;éléments, la recherche&nbsp;binaire est environ ***<span style="color:rgb(13, 204, 166)">$2$&nbsp;fois</span>*** plus rapide que la recherche&nbsp;linéaire, alors que pour un million d'éléments, elle est plus de ***<span style="color:rgb(13, 204, 166)">1000 fois</span>*** plus rapide.

On peut remarquer que le temps pris par la recherche&nbsp;binaire change peu avec la taille du tableau, ce qui n'est pas le cas de la recherche&nbsp;linéaire. Il faut environ ***<span style="color:rgb(13, 204, 166)">10 secondes</span>*** pour trier un million d'éléments avec l'algorithme linéaire, alors que moins de ***<span style="color:rgb(13, 204, 166)">10 millisecondes</span>*** suffisent à l'algorithme binaire. Les systèmes actuels traitent des données bien plus volumineuses qu'un million, pensez à toutes les vidéos sur le Web ou tous les utilisateurs d'un réseau social. Tout serait très lent, trop lent si on n'avait pas pensé à diviser&nbsp;pour&nbsp;régner.


```{codeplay}
# algorithme de recherche&nbsp;linéaire
def search_lin(search_list, search_element, verbose=0) :
    
    # boucle pour parcourir la liste
    for element in search_list :

        if verbose :
            print("L'élément comparé est : " + str(element) + "\n")

        # l'élément de la liste correspond à l'élément recherché
        if element == search_element :
            return True

    # aucun élément ne correspond
    return False


# algorithme de recherche&nbsp;binaire
def search_bin(search_list, search_element, verbose = 0) :
    
    # détermine les limites de la liste considérée
    start = 0
    end = len(search_list)

    # tant que la liste
    while end-start :

        # accède à l'élément du milieu 
        # la division est entière, car on doit obtenir un index de liste
        middle = (end-start) // 2 + start 
        
        if verbose :
            print("L'élément comparé est : " + str(search_list[middle]) + "\n")

	    # compare l'élément au milieu de la liste
        if search_element == search_list[middle] :
            if verbose :
                print("L'élément " + str(search_list[middle]) + " a été retrouvé !\n")
            return True

	    # l'élément du milieu est plus petit, on cherche dans la fin de la liste
        elif search_element < search_list[middle] :
            # search_list devient dans la première moitié de search_list
            end = middle 
            
            if verbose :
                print("L'élément se trouve au début de la liste : " + str(search_list[start:end]) + "\n")
        
        # l'élément du milieu est plus grand, on cherche dans la fin de la liste
        else :
            # search_list devient la deuxième moitié de search_list
            start = middle + 1  
            
            if verbose :
                print("L'élément se trouve dans la deuxième moitié de la liste : " + str(search_list[start:end]) + "\n")

    # aucun élément ne correspond
    if verbose :
        print("L'élément " + str(search_list[middle]) + " n'a pas été retrouvé...\n")
    return False


import time
import random

# stocke les résultats
resultat_lin, resultat_bin  = [], []

# longueurs des listes
nb = [100, 1000, 10000, 100000, 1000000, 10000000]

# pour toute les longueurs des listes
for last in nb :
    
    # créer la liste
    ma_liste = list(range(1,last+1)) 

    # rechercher un élément au hasard
    mon_element = random.randint(1,last) 
    print("L'élément recherché est : " + str(mon_element))

    # recherche&nbsp;linéaire
    time_1 = time.time()
    search_lin(ma_liste, mon_element, 0)
    time_algo_lin = round(time.time() - time_1, 7)
    resultat_lin.append(time_algo_lin)

    # recherche&nbsp;binaire
    time_1 = time.time()
    search_bin(ma_liste, mon_element, 0)
    # des fois, c'est tellement rapide que le temps pris vaut 0
    time_algo_bin = round(max(time.time() - time_1, 0.000001), 7)
    resultat_bin.append(time_algo_bin)

print("Linéaire (secondes) : " + str(resultat_lin))
print("Binaire (secondes) : " + str(resultat_bin))



```
````

```{didyouknow} Espace&#8209;temps et énergie

Nous allons surtout étudier la complexité des algorithmes en rapport avec le temps. Mais&nbsp;la&nbsp;complexité d’un algorithme peut également être calculée en rapport avec toutes les ressources qu’il utilise, par exemple des ressources d’**espace en mémoire** ou de **consommation d’énergie**. 

```

## Exercices

```{exercise} Recherche binaire aléatoire 🔌

Modifier votre programme  de recherche&nbsp;binaire : au lieu de diviser l’espace de recherche exactement au milieu, le diviser au hasard. Cette recherche avec une composante aléatoire s’apparente plus à la recherche que l’on fait lorsque l’on cherche un mot dans le dictionnaire.  

```


````{eval}

Vérifiez votre compréhension :

1. Je sais que la complexité&nbsp;temporelle donne une indication sur la vitesse d’un algorithme, en mesurant le nombre d’instructions élémentaires.

2. Je sais qu’un algorithme de complexité&nbsp;linéaire est plus lent qu’un algorithme de complexité&nbsp;logarithmique.

3. Je peux utiliser la stratégie « diviser&nbsp;pour&nbsp;régner » pour rechercher rapidement avec l’algorithme de recherche&nbsp;binaire.

````
