<span style="color:rgb(13, 204, 166);font-weight:600; font-size:1.2em">Version du 16 juin 2021</span>

Terminaison des algorithmes
===========================

````{admonition} Matière à réfléchir I
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
Qu’arrive-t-il lorsqu’on exécute ce programme avec `compte_a_rebours(10)` ?

Corriger le programme pour qu’il s’arrête à 0. 

Qu’arrive-t-il lorsque l’on exécute la nouvelle version du  programme avec  la valeur -10 en entrée ou `compte_a_rebours(-10)` ?

````

## Principe de terminaison

La **<span style="color:rgb(89, 51, 209)">terminaison</span>** est une propriété essentielle des algorithmes, qui garantit que les calculs de l’algorithme finiront par s’arrêter. Lorsque l’on conçoit un algorithme, il est important de faire en sorte que les calculs s’arrêtent à un moment donné. Cette garantie doit tenir pour toutes les entrées possibles. 
Voici un exemple d’algorithme qui compte et ne se termine pas :

```{code-block} python
 # Algorithme qui compte infini 
 Variable i : numérique
 i ← nombre donné par l’utilisateur
 Tant que i > 0 
	i  ← i + 1 
 	Afficher i   
 Fin Tant que
```

Si on exécute cet algorithme, le programme ne s’arrête jamais : `i` est incrémenté de `1` indéfiniment.  En pratique, si on retranscrit cet algorithme en programme et que l’on exécute le programme, le programme finira par s’arrêter lorsque les nombres représentés seront trop grands pour être représentés.

```{admonition} Exercice 0
:class: note

Retranscrire l’algorithme infini en programme. Après combien de boucles le programme s’arrête‑t‑il ?

La solution est donnée dans le texte ci-dessous.
```

Pour être certains que le programme finit par s’arrêter, nous pouvons le modifier ainsi :

```{code-block} python
 # Algorithme qui compte toujours infini 
 Variable i : numérique
 i ← nombre donné par l’utilisateur
 Tant que i != 10000 
	i  ← i + 1 
 	Afficher i   
 Fin Tant que
 ```

 ```{admonition} Exercice 1
:class: note

L’algorithme ci-dessus est appelé « Algorithme qui compte toujours infini ». Pourquoi est-il toujours infini ? Dans quel cas cet algorithme ne s’arrête jamais ?

La solution est donnée dans le texte ci-dessous.
```

Dans la version ci-dessus, si l’utilisateur entre une valeur plus grande que 10000, ou encore une valeur à virgule, l’algorithme ne s’arrête jamais. Pour le programmeur il peut être implicite qu’un décompte se fait toujours avec des nombres entiers, mais il doit prendre des précautions face à l’utilisateur. Voici une version d’un algorithme de décompte qui s’arrête :  

```{code-block} python
 # Algorithme qui compte et qui s’arrête 
 Variable i : numérique
 i ← nombre donné par l’utilisateur
 Tant que i < 10000 
	i  ← i + 1 
 	Afficher i   
 Fin Tant que
 ```

C’est au programmeur de s’assurer que le programme s’arrête dans tous les cas. Il ne peut pas compter sur la bienveillance de l’utilisateur. 

````{admonition} Matière à réfléchir II
:class: attention
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