# Algorithmique II

## 3. Algorithmes de tri [complément]

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


```{exercise} Une question à un million

Si une instruction prend 10<sup>-6</sup> secondes, combien de temps faut-il pour trier un tableau d’un million d’éléments avec le tri à sélection comparé au tri rapide (sans tenir compte de la constante) ?

```

````{solution} 

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

Pour trier 1 million d’éléments, le tri par sélection prend 10<sup>6</sup>*10<sup>6</sup> *10<sup>-6</sup> secondes ou 1 million de secondes (équivalent à plus de 11 jours), alors que le tri rapide a besoin de log2(10<sup>6</sup>)*10<sup>6</sup> *10<sup>-6</sup> ou ~20 secondes. 

Cette différence de temps est suffisante pour rendre rédhibitoire l’utilisation du tri par sélection. Pensez au nombre de clients qu’un réseau social possède, ou au nombre de produits qu’un supermarché doit gérer.
```
````


```{exercise} Une question de pivot

Trier le tableau suivant avec l’algorithme de tri rapide : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main, en prenant le dernier élément comme pivot. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

Est-ce que le choix du pivot est important ?

```

````{solution} 

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




```{exercise} Une question de sélection

Trier le tableau suivant avec l’algorithme de tri par sélection : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```

````{solution} 

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


```{exercise} Une question d'insertion

Trier le tableau suivant avec l’algorithme de tri par insertion : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```

````{solution} 

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



```{exercise} Une question de bulles


Trier le tableau suivant avec l’algorithme de tri à bulles : [3, 6, 8, 7, 1, 9, 4, 2, 5] à la main. Représenter l’état du tableau lors de toutes les étapes intermédiaires.

```


````{solution} 

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


````{exercise} Une question de chronomètre 🔌


Créer une liste qui contient les valeurs de 1 à n dans un ordre aléatoire, où n prend la valeur 100, par exemple. Indice : utiliser la fonction `shuffle()` du module `random`.

Implémenter au moins deux des trois algorithmes de tri vu au cours.
A l’aide du module `time` et de sa fonction `time()`, chronométrer le temps prend le tri d'une liste de 100, 500, 1000, 10000, 20000, 30000, 40000 puis 50000 nombres. 

Noter les temps obtenus et les afficher sous forme de courbe dans un tableur. Ce graphique permet de visualiser le temps d’exécution du tri en fonction de la taille de la liste. Que peut-on constater ?

Sur la base de ces mesures, peut-on estimer le temps que prendrait le tri de 100000 éléments ?

Lancer votre programme avec 100000 éléments et comparer le temps obtenu avec votre estimation.

````

**Solution à compléter**

