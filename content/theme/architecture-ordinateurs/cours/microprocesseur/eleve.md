Microprocesseur
===============

Dans ce chapitre, nous allons comprendre comment fonctionne un microprocesseur en détaillant les différents mécanismes qui sont opérés pour assurer le fonctionnement de base d'un ordinateur. 

# L'horloge

# L'accès à la mémoire


# Exemple: le 6502


## Pour aller plus loin
Les microprocesseurs modernes ajoutent quelques éléments de complexité que nous n'avons pas exposés ici. Il s'agit notamment des éléments suivants.
### Les multi-coeurs
Alors que dans le processeur que nous avons présenté, il n'y avait qu'une seule unité arithmétique et logique, ce qui limitait notre processeur à une opération par cycle d'horloge, l'industrie fournit aujourd'hui des microprocesseurs qui sont capables d'effectuer plusieurs opérations simultanément. Pour cela, ces derniers sont dotés de plusieurs coeurs capable d'effectuer chacun une opération. Mais cette mise en parallèle des opérations ne se fait pas sans difficultés. De la même manière qu'il serait extrêmement difficile pour plusieurs personnes d'écrire un texte en tenant le même stylo, il est compliqué de partager un calcul entre plusieurs unités de traitement.
### Le pipeline
Comme nous l'avons vu, l'exécution d'une instruction par le microprocesseur implique plusieurs opérations : accès à la mémoire en lecture et en écriture, accès aux registres en lecture et en écriture, opération logique. Pour optimiser la vitesse d'exécution, les processeurs modernes effectue en série ces opérations. Ainsi alors que les opérations logiques d'une instruction sont effectuées, l'instruction précédente est déjà chargée en mémoire. La difficulté de ce type d'optimisation réside dans le fait que des branchements conditionnels provoquent l'annulation des instructions déjà chargées. Pour optimiser encore ce genre de procédé, les processeur font de la prédiction dans l'exécution. Ces optimisations sont extrêmement compliquées à gérer.