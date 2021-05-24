Microprocesseur
===============

Dans ce chapitre, nous allons comprendre comment fonctionne un microprocesseur en détaillant les différents mécanismes qui sont opérés pour assurer le fonctionnement de base d'un microprocesseur. Appelé 

# L'horloge
Un processeur est un dispositif synchrone, ce qui signifie que les opérations à l'intérieur du processeur se déroulent de manière synchrone à un temps donné. Pour assurer cette simultanéité, il faut comme pour un orchestre, donner le tempo. Cette fonction de métronome est assurée par une horloge, ou un signal d'horloge. Cette horloge est constituée d'un simple signal carré dont la fréquence atteint aujourd'hui plusieurs giga Herz, c'est-à-dire plusieurs milliards de cycles par seconde.

# L'accès à la mémoire
Comme on l'a vu dans l'architecture de von Neumann, l'Unité Centrale de Traitement (UCT ou CPU en anglais pour Central Processing Unit) doit accéder à la mémoire. On parle de mémoire RAM pour Random Access Memory.
Le processeur peut accéder à la mémoire en lecture ou en écriture. Les deux mécanismes sont très similaires, mais avant de regarder plus en détail comment cela fonctionne, il faut d'abord définir comment la mémoire est structurée. La mémoire RAM permet, comme son nom l'indique, d'accéder à tout moment à n'importe quel emplacement.

TODO: illustration

 Pour y accéder, le processeur envoie d'abord l'adresse au module mémoire, puis lis ou écrit la valeur. Pour cela le processeur dispose d'un **bus d'adressage**. Il s'agit physiquement de câbles parallèles qui relient le processeur à la mémoire. La taille de ce bus ou sa largeur définit le nombre de connexions parallèles et dépend des caractéristiques du processeur et de la RAM. Chaque connexion transporte un bit, un bus de largeur 32 bit transporte 32 bits ce qui permet d'adresser 2<sup>32</sup> adresses mémoire (env. 4 Go). Le bus de données lui transporte les données entre le processeur et la mémoire (dans les deux sens). Ces deux bus, adresses et données, ne sont pas forcément de largeur identique.

 TODO: illustration

 Il nous manque encore un élément : lorsque la mémoire voit une adresse apparaître elle doit pouvoir déterminer s'il s'agit d'une lecture ou d'une écriture. Pour cela deux connexions supplémentaires relie le processeur à la mémoire: une ligne *enable* et une ligne *set*. Lorsque la ligne *enable* est à 1, alors le processeur accède à la mémoire en lecture et sur le bus de donnée doit apparaître les données qui sont stockées dans la mémoire à l'adresse indiquée sur le bus d'adressage. Lorsque c'est la ligne *set* qui est à 1, alors la mémoire doit enregistrer les données à l'adresse indiquée.

 ### Exercice

```{question} Question 1
Avec un bus d'adressage de 24 bits, quelle est la taille maximum de la mémoire ? 
* {f}`32ko`
* {v}`16Mo`
* {f}`16Go`
```


# Exemple: le 6502


## Pour aller plus loin
Les microprocesseurs modernes ajoutent quelques éléments de complexité que nous n'avons pas exposés ici. Il s'agit notamment des éléments suivants.
### Les multi-coeurs
Alors que dans le processeur que nous avons présenté, il n'y avait qu'une seule unité arithmétique et logique, ce qui limitait notre processeur à une opération par cycle d'horloge, l'industrie fournit aujourd'hui des microprocesseurs qui sont capables d'effectuer plusieurs opérations simultanément. Pour cela, ces derniers sont dotés de plusieurs coeurs capable d'effectuer chacun une opération. Mais cette mise en parallèle des opérations ne se fait pas sans difficultés. De la même manière qu'il serait extrêmement difficile pour plusieurs personnes d'écrire un texte en tenant le même stylo, il est compliqué de partager un calcul entre plusieurs unités de traitement.
### Le pipeline
Comme nous l'avons vu, l'exécution d'une instruction par le microprocesseur implique plusieurs opérations : accès à la mémoire en lecture et en écriture, accès aux registres en lecture et en écriture, opération logique. Pour optimiser la vitesse d'exécution, les processeurs modernes effectue en série ces opérations. Ainsi alors que les opérations logiques d'une instruction sont effectuées, l'instruction précédente est déjà chargée en mémoire. La difficulté de ce type d'optimisation réside dans le fait que des branchements conditionnels provoquent l'annulation des instructions déjà chargées. Pour optimiser encore ce genre de procédé, les processeur font de la prédiction dans l'exécution. Ces optimisations sont extrêmement compliquées à gérer.