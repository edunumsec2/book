
# La recette de l'univers

>**Contenus abordés** : Algorithmique, ordre topologique d'un graphe, circuit dans un graphe


***


## Introduction

Activité ludique d'élaboration d'une recette de cuisine infinie. 

## Objectifs du cours

1. Comprendre la notion d'algorithme. 
2. Comprendre la notion d'ordre topologique.
3. Comprendre la notion de circuit dans les graphes.

## Accroche

Si vous deviez expliquer à quelqu'un comment se faire cuire un oeuf, par où commenceriez-vous ? Casser l'oeuf dans la poêle ? Mais pour avoir une poêle, il faut l'acheter, pour l'acheter, il faut travailler, et pour travailler, il faut avoir mangé l'omelette... Comment faire ? 


## Matériel requis

**papier, stylos** 


## Marche à suivre

* Les élèves commencent par écrire une recette de cuisine pour se faire une omelette. 
* On leur explique la notion de graphe orienté. 
* On leur explique que chaque instruction peut être représentée comme le sommet d'un graphe. 
* On présente la notion d'ordre d'exécution des tâches comme une `liste ordonnée de sommets tel que y ne peut être entamée tant que x n'a pas été exécuté`. 
* Les élèves représentent leur recette sous forme d'un graphe et inscrivent les arrêtes correspondant à l'ordre d'exécution des tâches. 
* On présente l'algorithme pour créer un ordre topologique : `à chaque étape, chercher le sommet qui n'a pas d'axe entrant. Si plusieurs possibilités, choisir une au hasard`.
* Les élèves appliquent l'algorithme et créent un ordre topologique de leur recette. 
* Après ce premier round, on les fait écrire une recette telle qu'elle comporte un circuit. 

## Prolongements


1. On peut aller plus loin en expliquant en profondeur la notion de graphe avec circuit, ainsi que les problèmes que ces derniers posent en termes d'optimisation d'un parcours (problèmes pour l'algorithme de Dijkstra notamment, si ce dernier a déjà été abordé). 
2. On peut demander une mise en commun des recettes de départ, et entamer à partir de leurs différences une discussion quant à la précision relative des instructions données. 
3. On peut complexifier les choses en abordant la question du niveau de détail des instructions en rapport à la notion de librairie en programmation. Certaines instructions, comme "prendre une poêle" pourraient être décomposées en une infinité de micro-instructions plus précises. À moins que l'on ne possède une librairie comprenant une méthode `ustensiles.take(poêleàfrire)`

## Labels 

* **Nom (libre)** : La recette de l'univers
* **Genre (contraint)** : unplugged
* **Type (contraint)** : activité
* **Durée (libre)** : en moyenne 90mn (2 périodes)
* **Thème (contraint / selon plan d'études)** : introduction à l'algorithmique
* **Sujet (contraint / selon plan d'études)** : découpage d'un problème en étapes
* **Outils de mise en place (libre)** : feuilles de papier / stylos
* **Pédagogie (contraint)** : ? 
* **Niveau (contraint)** : facile
* **Objectifs info (libre)** : comprendre la notion d'algorithme / comprendre la notion d'ordre topologique / comprendre la notion de graphe avec ou sans circuit. 
* **Objectifs socio (libre)** :  ?
* **Compétences visées (libre)** : analyse, réflexion, découpage d'un problème en étapes. 
* **Mots-clefs (libre)** : ? 
* **Applications célèbres liées à la ressource (libre)** : ? 
* **Centres d'intérêts (libre)** : ? 
* **Auteur(s)**
* **Relecteur(s)**
* **Testeur(s)**



