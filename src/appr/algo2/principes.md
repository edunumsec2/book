
# 1. Terminaison et complexité 


````{admonition} Matière à réfléchir. Compte à rebours
:class: attention

Voici une version naïve du compte à rebours des secondes pour le passage du Nouvel An :

```{codeplay}
# Compte à rebours 
def compte_a_rebours(nb_secondes) :
    while True :
        print(nb_secondes)
    	nb_secondes = nb_secondes - 1 

compte_a_rebours(10)
```
Qu’arrive-t-il lorsqu’on exécute ce {glo}`programme|programme` avec `compte_a_rebours(10)` ?

Corriger le programme pour qu’il s’arrête à 0. 

Qu’arrive-t-il lorsque l’on exécute la nouvelle version du  programme avec  la valeur -10 en entrée ou `compte_a_rebours(-10)` ?

````

## 1.0. Principe de terminaison

La **<span style="color:rgb(89, 51, 209)">terminaison</span>** est une propriété essentielle des {glo}`algo|algorithmes`, qui garantit que les calculs de l’algorithme finiront par s’arrêter. Lorsque l’on conçoit un algorithme, il est important de faire en sorte que les calculs s’arrêtent à un moment donné. Cette garantie doit tenir pour toutes les entrées possibles. Voici un exemple d’algorithme qui compte et qui ne se termine pas :

```{code-block} 
 # Algorithme qui compte infini 
 Variable i : numérique
 i ← nombre donné par l’utilisateur
 Tant que i > 0 
	i  ← i + 1 
 	Afficher i   
 Fin Tant que
```

Si on exécute cet {glo}`algo|algorithme`, le {glo}`programme|programme` ne s’arrête jamais : `i` est {glo}`incrementation|incrémenté` de `1` indéfiniment.  En pratique, si on retranscrit cet algorithme en programme et que l’on exécute le programme, le programme finira par s’arrêter lorsque les nombres représentés seront trop grands pour être représentés.

```{admonition} Exercice 1.0. L'infini en programme
:class: note

Retranscrire l’algorithme infini en programme. Après combien de boucles le programme s’arrête‑t‑il ?

```

````{admonition} Solution 1.0. L'infini en programme
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

La solution de l'exercice est donnée directement dans le texte qui suit.

```
````

Pour faire en sorte que le programme finisse par s’arrêter, nous pouvons le modifier ainsi :

```{code-block} 
 # Algorithme qui compte toujours infini 
 Variable i : numérique
 i ← nombre donné par l’utilisateur
 Tant que i != 10000 
	i  ← i + 1 
 	Afficher i   
 Fin Tant que
 ```

 ```{admonition} Exercice 1.1. L'infini ne finit plus de finir
:class: note

L’algorithme ci-dessus est appelé « Algorithme qui compte toujours infini ». Pourquoi est-il toujours infini ? Dans quel cas cet algorithme ne s’arrête jamais ?

```

````{admonition} Solution 1.1. L'infini ne finit plus de finir
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

La solution de l'exercice est donnée directement dans le texte qui suit.

```
````

Dans la version ci-dessus, si l’utilisateur entre une valeur plus grande que 10000, ou encore une valeur à virgule, l’algorithme ne s’arrête pas. Il peut être implicite pour la personne qui programme qu’un décompte se fait toujours avec des nombres entiers, mais il doit prendre des précautions face aux utilisateurs. Voici une version de l'algorithme de décompte qui s’arrête dans tous les cas :  

```{code-block} 
 # Algorithme qui compte et qui s’arrête 
 Variable i : numérique
 i ← nombre donné par l’utilisateur
 Tant que i < 10000 
	i  ← i + 1 
 	Afficher i   
 Fin Tant que
 ```

En programmant, nous devons nous assurer que nos programmes se terminent dans tous les cas, autrement il ne seront pas utilisables. Il ne suffit pas de compter sur la bienveillance des utilisateurs. 

````{admonition} Le saviez-vous ? Conjecture de Syracuse
:class: hint

De nos jours, on ne sait toujours pas si ce programme termine pour chaque entrée n. Ce problème est connu sous le nom la ***<span style="color:rgb(13, 204, 166)">conjecture de Collatz</span>*** ou ***<span style="color:rgb(13, 204, 166)">la conjecture de Syracuse</span>*** :

```{code-block} python
def Collatz(n) :
    while n > 1 :
        if n % 2 == 0 :
            n = n / 2
        else : 
            n = 3 * n + 2 
```

````



## 1.1. Principe de complexité

````{admonition} Matière à réfléchir. Record de vitesse
:class: attention
On souhaite comparer deux algorithmes qui permettent de résoudre le même problème, afin d’utiliser l’algorithme qui permet de résoudre le problème plus rapidement. Mais comment pourrait‑on calculer la vitesse d’un algorithme ?
````

Il est important lorsqu’on utilise un {glo}`algo|algorithme` de nous préoccuper de son {glo}`efficacite|efficacité`. Mais comment calculer l'efficacité d’un algorithme, comment calculer sa vitesse ? 

Est-ce qu’on peut utiliser la taille de l’algorithme pour prédire le temps qu’il va prendre à s’exécuter ? En d’autres termes, est-ce qu’un algorithme de 10 lignes est toujours plus lent qu’un algorithme de 5 lignes ? Nous avons vu que l’algorithme infini du chapitre précédent est très court (seulement 5 lignes), mais en théorie il ne s’arrête jamais. Une {glo}`bouclewhile|boucle` rallonge le code de seulement 2 lignes, mais rallonge le temps d’exécution de manière importante. 

On pourrait croire qu’il suffit de programmer un algorithme et de chronométrer le temps que ce programme prend à s’exécuter. Cette métrique est problématique, car elle ne permet pas de comparer différents algorithmes entre eux lorsqu’ils sont exécutés sur différentes machines. Un algorithme lent {glo}`implementation|implémenté` sur une machine dernière génération pourrait prendre moins de temps à s’exécuter qu’un algorithme rapide implémenté sur une machine datant d’une dizaine d’années. 

Pour mesurer le temps d’exécution (ou la vitesse) d’un algorithme, il existe un critère plus objectif : le **<span style="color:rgb(89, 51, 209)">nombre d’instructions élémentaires</span>**.  De manière formelle et rigoureuse, on ne parle pas d’efficacité, mais plutôt de la **<span style="color:rgb(89, 51, 209)">complexité d’un algorithme</span>**, qui est en fait contraire à son efficacité. L’analyse de la complexité d’un algorithme étudie la quantité de ressources, par exemple de temps, nécessaires à son exécution.

```{admonition} Le saviez-vous ? Espace-temps et énergie
:class: hint

Nous allons surtout étudier la complexité des algorithmes en rapport avec le temps. Mais la complexité d’un algorithme peut également être calculée en rapport avec toutes les ressources qu’il utilise, par exemple des ressources d’**espace en mémoire** ou de **consommation d’énergie**. 

```

````{admonition} Ai-je compris ?
:class: attention

1. Je sais que l’on doit garantir la terminaison d’un algorithme.

2. Je sais que la complexité d’un algorithme peut nous donner une indication de sa vitesse.

3. Je sais que la complexité est une fonction du nombre d’instructions élémentaires.

````

