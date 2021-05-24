Microprocesseur
===============

````{panels}

:img-top: media/Gordon_Moore.jpeg


^^^^^
* **Naissance** 3 janvier 1929 / San Francisco 🇺🇸 
```{dropdown} Bio
:animate: fade-in-slide-down
Gordon Earle Moore est le cofondateur d'Intel en 1968. Intel est le premier fabricant mondial de microprocesseurs. Gordon Moore est célèbre pour avoir formulé en 1965 une loi empirique portant son nom: **loi de Moore**. Cette lois prédit un doublement de la complexité, et donc du nombre de transistors présents dans les microprocesseurs tous les deux ans. Bien que nous ayons atteint certaines limites physique au niveau atomique et des effets de bruits parasites liés aux effets quantique et à la désintégration alpha, la loi est toujours vérifiée aujourd'hui malgré un ralentissement de la progression pour certaines caractéristiques. Ces limites sont aujourd'hui compensées par des puces intégrant de plus en plus de composants de plus en plus complexes.
```

````

Dans ce chapitre, nous allons comprendre comment fonctionne un microprocesseur en détaillant les différents mécanismes qui sont opérés pour assurer le fonctionnement de base d'un microprocesseur. Appelé 

# L'horloge
Un processeur est un dispositif synchrone, ce qui signifie que les opérations à l'intérieur du processeur se déroulent de manière synchrone à un temps donné. Pour assurer cette simultanéité, il faut comme pour un orchestre, donner le tempo. Cette fonction de métronome est assurée par une horloge, ou un signal d'horloge. Cette horloge est constituée d'un simple signal carré dont la fréquence atteint aujourd'hui plusieurs giga Herz, c'est-à-dire plusieurs milliards de cycles par seconde.

# L'accès à la mémoire

```{admonition} Rappel
:class: danger
Comme on l'a vu dans l'architecture de vonNeumman, la mémoire contient le programme et les données du programme. Un programme peut donc se modifier lui-même en se modifiant dans la mémoire (c'est rarement un effet souhaité).
```

L'Unité Centrale de Traitement (UCT ou CPU en anglais pour Central Processing Unit) doit accéder à la mémoire. On parle de mémoire RAM pour Random Access Memory. Le processeur peut accéder à la mémoire en lecture ou en écriture. Les deux mécanismes sont très similaires, mais avant de regarder plus en détail comment cela fonctionne, il faut d'abord définir comment la mémoire est structurée. La mémoire RAM permet, comme son nom l'indique, d'accéder à tout moment à n'importe quel emplacement.

TODO: illustration

 Pour y accéder, le processeur envoie d'abord l'adresse au module mémoire, puis lis ou écrit la valeur. Pour cela le processeur dispose d'un **bus d'adressage**. Il s'agit physiquement de câbles parallèles qui relient le processeur à la mémoire. La taille de ce bus ou sa largeur définit le nombre de connexions parallèles et dépend des caractéristiques du processeur et de la RAM. Chaque connexion transporte un bit, un bus de largeur 32 bit transporte 32 bits ce qui permet d'adresser 2<sup>32</sup> adresses mémoire (env. 4 Go). Le bus de données lui transporte les données entre le processeur et la mémoire (dans les deux sens). Ces deux bus, adresses et données, ne sont pas forcément de largeur identique.

 TODO: illustration

 ```{admonition} Anecdote
:class: attention
Le processeur Intel 80286 (ancêtre des processeurs Pentium),  sorti en 1982, présentait un bus de données de 16 bits et un bus d'adresses de 24 bits. De plus l'adressage par segments (relativement compliqué) réduisait l'adressage physique à un adressage sur 20 bits.
```

 Il nous manque encore un élément : lorsque la mémoire voit une adresse apparaître elle doit pouvoir déterminer s'il s'agit d'une lecture ou d'une écriture. Pour cela deux connexions supplémentaires relie le processeur à la mémoire: une ligne *enable* et une ligne *set*. Lorsque la ligne *enable* est à 1, alors le processeur accède à la mémoire en lecture et sur le bus de donnée doit apparaître les données qui sont stockées dans la mémoire à l'adresse indiquée sur le bus d'adressage. Lorsque c'est la ligne *set* qui est à 1, alors la mémoire doit enregistrer les données à l'adresse indiquée.

```{admonition} Le contenu de la mémoire
:class: hint

**Les instructions** : 
La mémoire contient le programme sous-forme de codes qui représentent des instructions à exécuter par le processeur. Ces codes correspondent à un jeu d'instruction propre à chaque modèle de proceseur. On parle de langage machine. Pour écrire de tels programme, on utilise un logiciel de type assembleur qui traduit les codes dans une représentation plus lisible.

**Les données** : 
Les données stockées dans la mémoire peuvent être des nombres, des lettres, des chaînes de caractères ainsi que des adresses d'autres emplacement en mémoire. On trouvera plus de détails à ce sujet dans le chapitre [Représentation de l'information](/content/theme/representation-information/accueil/eleve.html "Représentation de l'information").


```

 ### Exercice

```{question} Question 1
Avec un bus d'adressage de 24 bits, quelle est la taille maximum de la mémoire ? 
* {f}`32ko`
* {v}`16Mo`
* {f}`16Go`
```

```{question} Question 2
Quelle est la taille maximale de la mémoire pour un processeur 80286, sachant que l'adressage physique est finalement réduit à 20 bits ? 
* {f}`32ko`
* {f}`16Mo`
* {v}`1Mo`
```





# Exemple: le 6502

image

réf: visual 6502.org 

## Pour aller plus loin
Les microprocesseurs modernes ajoutent quelques éléments de complexité que nous n'avons pas exposés ici. Il s'agit notamment des éléments suivants.
### Les multi-coeurs
Alors que dans le processeur que nous avons présenté, il n'y avait qu'une seule unité arithmétique et logique, ce qui limitait notre processeur à une opération par cycle d'horloge, l'industrie fournit aujourd'hui des microprocesseurs qui sont capables d'effectuer plusieurs opérations simultanément. Pour cela, ces derniers sont dotés de plusieurs coeurs capable d'effectuer chacun une opération. Mais cette mise en parallèle des opérations ne se fait pas sans difficultés. De la même manière qu'il serait extrêmement difficile pour plusieurs personnes d'écrire un texte en tenant le même stylo, il est compliqué de partager un calcul entre plusieurs unités de traitement.
### Le pipeline
Comme nous l'avons vu, l'exécution d'une instruction par le microprocesseur implique plusieurs opérations : accès à la mémoire en lecture et en écriture, accès aux registres en lecture et en écriture, opération logique. Pour optimiser la vitesse d'exécution, les processeurs modernes effectue en série ces opérations. Ainsi alors que les opérations logiques d'une instruction sont effectuées, l'instruction précédente est déjà chargée en mémoire. La difficulté de ce type d'optimisation réside dans le fait que des branchements conditionnels provoquent l'annulation des instructions déjà chargées. Pour optimiser encore ce genre de procédé, les processeur font de la prédiction dans l'exécution. Ces optimisations sont extrêmement compliquées à gérer.