# Stroboscope ou le *random* fait bien les choses 

---- 

Cette activité amène progressivement l'élève à simuler un « stroboscope », construit de manière incrémentale. L'objectif est de créer une prise de conscience sur les possibilités de l'utilisation du hasard dans la programmation.


----

```{admonition} Stroboscope ou le *random* fait bien les choses
:class: hint

* Thème : Algorithmique et programmation (lors du dernier chapitre d'*Algorithmique I*)
* Niveau : `moyen`
* Durée : 2 période ou 90 minutes
* Objectifs pédagogiques : Résoudre un problème donné de manière incrémentale, tout en versionnant son code. Utiliser le hasard pour résoudre un problème.
* Modalité : `branché`
* Matériel : fichier de départ *stroboscope_1_0.py* (téléchargeable en haut de cette page)
* Prérequis : bases de la programmation

```


## Déroulement


| Étape                                   | Durée  | Phase de l'activité   | 
|---------------------------------------|------ |---------------------|
| {ref}`0. Analyse de code<apprentissage.analyse>`  | 10 min  | Apprentissage           |
| {ref}`1. Deuxième écran<apprentissage.augmentation>`           | 10 min  | Exploration |
| {ref}`2. Un intervalle<apprentissage.plus>`  | 15 min   | Exploration          |
| {ref}`3. Différents intervalles<apprentissage.optimisation>`  | 10 min   | Exploration              |
| {ref}`4. Stroboscope fixe<apprentissage.alternative>`    | 15 min   | Exploration et institutionnalisation    |
| {ref}`5. Stroboscope aléatoire<apprentissage.variateur>`    | 15 min   | Enseignement et institutionnalisation  |
| {ref}`6. Stroboscope paramétré<apprentissage.hsv>`          | 15 min   | Institutionnalisation            |




(apprentissage.analyse)=
### 0. Analyse de code

*Durée : 10 min*

Télécharger le fichier de base *monochromes_1_0.py* qui permet d'afficher une fenêtre « écran noir » en utilisant le module *pygame*. Prendre le temps d'analyser le code du fichier. 

Conseil : le raccourci *ctrl+c* permet de quitter le programme plus rapidement qu'en fermant la fenêtre.


(apprentissage.augmentation)=
### 1. Deuxième écran

*Durée : 10 min*

Dupliquer le fichier. Changer le 0 dans le nom du fichier en 1. Modifier le code pour passer progressivement d'un écran blanc à un écran noir. 

*A votre avis pourquoi l'écran blanc s'affiche à nouveau ?* 


(apprentissage.plus)=
### 2. Un intervalle

*Durée : 15 min*

Dupliquer le fichier. Changer le 1 dans le nom du fichier en 2. Contrôler l'alternance entre les deux écrans en changeant de couleur toutes les secondes, grâce à la fonction *sleep()* du module *time*.


(apprentissage.optimisation)=
### 3. Différents intervalles

*Durée : 10 min*

[Optionnel] Dupliquer le fichier. Changer le 3 dans le nom du fichier en 4. Essayer différents temps d’attente entre deux écrans. 

*Attention à ne pas descendre en-dessous de 0.5 si vous êtes épileptique.*

(apprentissage.alternative)=
### 4. Stroboscope fixe

*Durée : 15 min*

[Optionnel] Dupliquer le fichier. Changer le 3 dans le nom du fichier en 4. Mettre le temps d’attente entre deux écrans à une valeur qui permette d’avoir une fréquence de 5Hz, ce qui correspond à un stroboscope. 

*Attention à ne pas descendre en-dessous de 0.5 si vous êtes épileptique.*

(apprentissage.variateur)=
### 5. Stroboscope aléatoire

*Durée : 15 min*

5.	Créer une séquence imprévisible, en utilisant la fonction *random()* du module *random*.


*Avez-vous pensé à dupliquer le fichier et changer le numéro 4 en 5 dans le nom ?*


(apprentissage.hsv)=
### 6. Stroboscope paramétré

*Durée : 15 min*

Ajouter un paramètre pour contrôler la fréquence d’affichage de la séquence imprévisible. [Pour les avancés] Ajouter une interface (boutons ou *scroll bar*) pour contrôler la durée maximale de l'intervalle temporel, ou la variation de l'intervalle temporel.


## Considérations didactiques

### Modalité de travail

Si le niveau de la classe est faible, répartir les élèves en équipes de développement qui travaillent ensemble.

### Institutionnalisation n° 1

**[A faire après l'étape 2]** Si on ajoute un temps d’attente uniquement après le premier affichage, la fenêtre reste blanche, il faut à ce stade comprendre que le code de la fenêtre noire s’exécute aussi, mais trop rapidement pour être visible à l’œil nu.

### Institutionnalisation n° 2

**[A faire après l'étape 3]** Insister sur l'importance d'introduire à ce stade une variable (ici *time_interval*), pour éviter de devoir changer la valeur à deux endroits.

*Principe de modularité : je ne duplique pas un bout de code, je le définis.*



### Institutionnalisation n° 3

**[A faire à la fin]** Il est trop difficile de résoudre un problème du premier coup. Il faut procéder de manière incrémentale, par petits paliers. Si l'on souhaite créer un variateur de couleurs, il faut définir des objectifs intermédiaires plus facilement atteignables, ici le parcours de luminosité ou un variateur noir et blanc.

*Pour résoudre un problème il faut le « découper », et le résoudre un bout à la fois. Il vaut mieux viser de multiples objectifs atteignables, qu'un seul objectif géant.*


### Institutionnalisation n° 4

**[A faire à la fin]** Le *versionnage* consiste à garder toutes les versions d'un même code. Le versionnage permet de se souvenir de la progression dans la résolution d'un problème et de ne pas "tout casser" lorsqu'on modifie le programme (on peut toujours revenir à une version qui marche). 

*Dans le cas d'un problème difficile à résoudre, le versionnage est essentiel. Il existe des outils de versionnage très aboutis, par exemple  « GitHub ».*



## Liens avec les autres thématiques

Possibilité de faire référence au hasard dans l'algorithmique, par exemple choix du pivot dans le tri rapide ou certaines heuristiques comme les *méthodes de Monte-Carlo*.


<!--
## Ressources complémentaires

[https://download.tuxfamily.org/linuxgraphic/archives/grokking/node51.html](https://download.tuxfamily.org/linuxgraphic/archives/grokking/node51.html)-->

