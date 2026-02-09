# Algorithme de coloration de graphe

```{toctree}
:maxdepth: 2
:hidden:
Théorie <theorie>
Exercices <exercices>
```

Activité sur table pour introduire le problème de la coloration des graphes et l'algorithme de Welch-Powell, avec 
quelques applications possibles de ce problème. 

```{admonition} Notice
:class: hint

* **Thème** : `Algorithmes dans les graphes`
* **Niveau** : `facile`
* **Durée** : 2 x 45 minutes
* **Objectifs pédagogiques** : Découvrir les notions de graphe, de coloration et d'algorithme glouton
* **Modalité** : `débranché`
* **Matériel** : [carte des cantons suisses](media/cantons.pdf), [support de théorie](theorie),[exercices](exercices), 
* **Prérequis** : aucun
* **Notions fondamentales** : graphes, coloration, algorithme glouton, modélisation
* **Taille du groupe** : `classe entière`

```

## Déroulement


|                                       | Durée  | Phase de l'activité   | 
|---------------------------------------|------ |---------------------|
| {ref}`Introduction<coloration.intro>`| 5 min  | Mise en situation     |
| {ref}`Travail en groupe <coloration.groupe>`| 15 min  | Exploration |
| {ref}`Mise en commun <coloration.commun>`| 10 min   | Objectivation          |
| {ref}`Théorie <coloration.thgraphe>`| 15 min   | Institutionnalisation           |
| {ref}`Exercices d'application <coloration.exercices>`| 15 min   | Apprentissage          |
| {ref}`Optimalité <coloration.opt>`| 10 min   | Exploration           |
| {ref}`Correction et discussion <coloration.discussion>`| 15 min   | Institutionnalisation|



(coloration.intro)=
## Introduction

*Durée : 5 min*

On distribue la {download}`carte des cantons suisses<./media/cantons.pdf>` aux élèves en leur demandant d'essayer de la colorier avec le moins de
couleurs possibles, sachant que deux cantons adjacents ne peuvent pas avoir la même couleur. Les élèves indiquent sur leur feuille combien de couleurs
ont été utilisées.

Première mise en commun, où les élèves partagent leur coloriage et surtout le nombre de couleurs utilisées. L'enseignant peut alors évoquer avec le
[théorème des quatre couleurs.](https://accromath.uqam.ca/2019/01/le-theoreme-des-quatre-couleurs/). 

(coloration.groupe)=
## Travail en groupe 

*Durée : 15  min*

### Formalisation
Par deux, les élèves doivent ensuite formaliser un algorithme de coloration en le décrivant, sous forme de texte ou de logigramme,
sur une feuille de papier. 

### Evaluation
Chaque groupe évalue l'algorithme d'un autre groupe en essayant de l'appliquer pour obtenir une coloration à plus de quatre couleurs sur la même
carte des cantons. Les plus rapides peuvent essayer de trouver des graphes pour lesquels l'algorithme ne permets pas une coloration avec un nombre
minimal de couleurs. 

(coloration.commun)=
## Mise en commun

*Durée : 10  min*

L'enseignant.e propose à certains groupes de présenter leur algorithme. Attention à bien préciser qu'un algorithme peut produire une coloration avec un
nombre minimal de couleurs pour une carte, mais pas pour une autre. 

(coloration.thgraphe)=
### Théorie

*Durée : 10-20 min*

Au besoin l'enseignant-e introduit les termes suivants : graphe, sommet, arrête, sommet adjacent et degré d'un sommet, en illustrant avec le graphe
des cantons suisses. 

L'enseignant-e propose ensuite une définition formelle de la coloration d'un graphe et présente l'algorithme de Welch-Powell en faisant le lien avec
les algorithmes proposés par les élèves. Un exemple simple d'application est démontré en classe. Un [support theorique](theorie) est utilisé
(par exemple en imprimant la page web). 


<!-- Introduire la notion de (sous-)graphe complet avec l'exemple LU-BE-OW-NW. -->


(coloration.exercices)=
### Exercices d'application

*Durée : 15 min*

Les élèves travaillent par groupe de 2 et tentent de résoudre les [exercices d'application](exercices) distribués par l'enseignant ou l'enseignante. Le corrigé est disponible {download}`ici<./data/coloration_corrige.docx>`


(coloration.opt)=
### Optimalité

*Durée : 10 min*

Les élèves doivent déterminer si l'algorithme de Welch-Powel trouve toujours une coloration minimale. Pour ceci, ils et elles essayent de
trouver des graphes pour lesquels l'algorithme de Welch-Powel ne trouve pas une coloration minimale.

Cet algorithme fait partie de la famille des algorithmes gloutons. Cela signifie que l'algorithme ne donne par forcément la solution optimale. Essai de l'algorithme sur un graphe simple et discussion avec les élèves pour savoir si la solution obtenue est optimale ou pas. Possible d'aborder la notion de problèmes NP-complet avec les élèves les plus avancés. 


(coloration.discussion)=
### Discussion des résultats

*Durée : 15 min*

Discussion avec les élèves des résultats obtenus. Introduction du concept d'algorithme glouton. 


### Prolongements possibles
* Théorème des 4 couleurs
* Problèmes NP-complets
* Algorithmes heuristiques
* Algorithme de coloration DSATUR (Daniel Brélaz)
