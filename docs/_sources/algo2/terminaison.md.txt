
# 1. Terminaison des algorithmes


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

La **<span style="color:rgb(89, 51, 209)">terminaison</span>** est une propriété essentielle des {glo}`algo|algorithmes`, qui garantit que les calculs de l’{glo}`algo|algorithme` finiront par s’arrêter. Lorsque l’on conçoit un {glo}`algo|algorithme`, il est important de faire en sorte que les calculs s’arrêtent à un moment donné. Cette garantie doit tenir pour toutes les entrées possibles. 
Voici un exemple d’{glo}`algo|algorithme` qui compte et ne se termine pas :

```{code-block} 
 # Algorithme qui compte infini 
 Variable i : numérique
 i ← nombre donné par l’utilisateur
 Tant que i > 0 
	i  ← i + 1 
 	Afficher i   
 Fin Tant que
```

Si on exécute cet {glo}`algo|algorithme`, le {glo}`programme|programme` ne s’arrête jamais : `i` est {glo}`incrementation|incrémenté` de `1` indéfiniment.  En pratique, si on retranscrit cet {glo}`algo|algorithme` en {glo}`programme|programme` et que l’on exécute le {glo}`programme|programme`, le {glo}`programme|programme` finira par s’arrêter lorsque les nombres représentés seront trop grands pour être représentés.

```{admonition} Exercice 1 : infini programmé ✏️📒
:class: note

Retranscrire l’algorithme infini en programme. Après combien de boucles le programme s’arrête‑t‑il ?

```

````{admonition} Solution
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

La solution de l'exercice est donnée directement dans le texte qui suit.

```
````

Pour être certains que le {glo}`programme|programme` finit par s’arrêter, nous pouvons le modifier ainsi :

```{code-block} 
 # Algorithme qui compte toujours infini 
 Variable i : numérique
 i ← nombre donné par l’utilisateur
 Tant que i != 10000 
	i  ← i + 1 
 	Afficher i   
 Fin Tant que
 ```

 ```{admonition} Exercice 2 : infini... toujours ✏️📒
:class: note

L’algorithme ci-dessus est appelé « Algorithme qui compte toujours infini ». Pourquoi est-il toujours infini ? Dans quel cas cet algorithme ne s’arrête jamais ?

```

````{admonition} Solution
:class: hint

```{dropdown} <span style="color:grey">Cliquer ici pour voir la réponse</span>
:animate: fade-in-slide-down

La solution de l'exercice est donnée directement dans le texte qui suit.

```
````

Dans la version ci-dessus, si l’utilisateur entre une valeur plus grande que 10000, ou encore une valeur à virgule, l’{glo}`algo|algorithme` ne s’arrête jamais. Pour le programmeur il peut être implicite qu’un décompte se fait toujours avec des nombres entiers, mais il doit prendre des précautions face à l’utilisateur. Voici une version d’un {glo}`algo|algorithme` de décompte qui s’arrête :  

```{code-block} 
 # Algorithme qui compte et qui s’arrête 
 Variable i : numérique
 i ← nombre donné par l’utilisateur
 Tant que i < 10000 
	i  ← i + 1 
 	Afficher i   
 Fin Tant que
 ```

C’est au programmeur de s’assurer que le {glo}`programme|programme` s’arrête dans tous les cas. Il ne peut pas compter sur la bienveillance de l’utilisateur. 

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