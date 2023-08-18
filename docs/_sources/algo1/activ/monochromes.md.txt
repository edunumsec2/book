# Monochromes ou l'importance d'une « bonne » représentation 

---- 

Cette activité amène progressivement l'élève à simuler un « variateur de lampe LED », construit de manière incrémentale. L'objectif est de créer une prise de conscience qu'une « bonne » représentation est à la base de la résolution d'une tâche.


----

```{admonition} Monochromes ou l'importance d'une « bonne » représentation
:class: hint

* Thème : Algorithmique et programmation (lors du dernier chapitre d'*Algorithmique I*)
* Niveau : `moyen`
* Durée : 2 période ou 90 minutes
* Objectifs pédagogiques : Résoudre un problème donné de manière incrémentale, tout en versionnant son code. Choisir la bonne représentation de l'information pour résoudre un problème.
* Modalité : `branché`
* Matériel : fichier de départ *monochromes_1_0.py* (téléchargeable en haut de cette page)
* Prérequis : bases de la programmation

```


## Déroulement


| Étape                                   | Durée  | Phase de l'activité   | 
|---------------------------------------|------ |---------------------|
| {ref}`0. Analyse de code<apprentissage.analyse>`  | 10 min  | Apprentissage           |
| {ref}`1. Parcours de couleurs<apprentissage.augmentation>`           | 15 min  | Exploration |
| {ref}`2. Double parcours<apprentissage.plus>`  | 10 min   | Exploration          |
| {ref}`3. Optimisation. Un parcours unique<apprentissage.optimisation>`  | 10 min   | Exploration              |
| {ref}`4. Alternative. Un parcours unique<apprentissage.alternative>`    | 15 min   | Exploration et institutionnalisation    |
| {ref}`5. Variateur de lampe LED<apprentissage.variateur>`    | 15 min   | Enseignement et institutionnalisation  |
| {ref}`6. Système HSV<apprentissage.hsv>`          | 15 min   | Institutionnalisation            |





(apprentissage.analyse)=
### 0. Analyse de code

*Durée : 10 min*

Télécharger le fichier de base *monochromes_1_0.py* qui permet d'afficher une fenêtre « écran noir » en utilisant le module *pygame*. Prendre le temps d'analyser le code du fichier. 

Conseil : le raccourci *ctrl+c* permet de quitter le programme plus rapidement qu'en fermant la fenêtre.


(apprentissage.augmentation)=
### 1. Parcours de couleurs

*Durée : 15 min*

Dupliquer le fichier. Changer le 0 dans le nom du fichier en 1. Modifier le code pour rajouter un écran blanc après  l'écran noir. 

"A votre avis pourquoi l'écran blanc s'affiche à nouveau ?*


(apprentissage.plus)=
### 2. Double parcours

*Durée : 10 min*

Dupliquer le fichier. Changer le 1 dans le nom du fichier en 2. Rajouter un parcours de couleurs dans l'autre sens, afin d'éviter la transition brusque entre la couleur blanche à noire.


(apprentissage.optimisation)=
### 3. Optimisation. Un parcours unique

*Durée : 10 min*

[Optionnel] Dupliquer le fichier. Changer le 2 dans le nom du fichier en 3. Plutôt que d’avoir deux parcours de couleurs (noir à blanc, suivi de blanc à noir), essayer d’avoir un parcours unique qui se base sur la valeur d'une variable qui paramètre le sens du parcours dans la fonction *range()*. Changer de sens après un parcours.

(apprentissage.alternative)=
### 4. Alternative. Un parcours unique

*Durée : 15 min*

[Optionnel] Dupliquer le fichier. Changer le 3 dans le nom du fichier en 4. Plutôt que d’avoir deux parcours de couleurs (noir à blanc, suivi de blanc à noir), essayer d’avoir un parcours unique qui se base sur la valeur d'une variable qui change le sens du parcours en changeant *background_color*. Changer de sens après un parcours.


(apprentissage.variateur)=
### 5. Variateur de lampe LED

*Durée : 15 min*

Faire parcourir les couleurs dans l’ordre de l’image ci-dessous, ce qui correspond aux teintes saturées du cercle chromatique. 

```{figure} media/hsv_saturated.png
---
alt: couleurs hsv saturées
width: 420px
name : hsv_saturated
---
```

*Avez-vous pensé à dupliquer le fichier et changer le numéro 4 en 5 dans le nom ?*


(apprentissage.hsv)=
### 6. Système HSV

*Durée : 15 min*

[Difficile, pour les avancés] Afficher les valeurs RGB de chaque teinte HSV afin de comprendre la relation qui existe entre ces deux systèmes de représentation numérique des couleurs (utiliser *matplotlib.pyplot*).


## Considérations didactiques

### Modalité de travail

Si le niveau de la classe est faible, répartir les élèves en équipes de développement qui travaillent ensemble.

### Institutionnalisation n° 1

**[A faire après l'étape 4]** La première, ainsi que la deuxième, idée d’implémentation n’est pas la plus compacte. Un même algorithme (objectif) peut être implémenté de plusieurs manières différents, et cela vaut la peine de réfléchir à l’implémentation en amont. 

Pour gagner du temps, il est possible de présenter les 3 manières de résoudre le même problème et de demander aux élèves comment ils ont procéder, et quelle est la meilleure solution d'après eux.

*La première idée qu'on a est souvent la plus simple, mais c'est rarement la meilleure idée*.

### Institutionnalisation n° 2

**[A faire après l'étape 5]** Cet exercice est beaucoup plus facile à résoudre lorsqu’on passe en représentation HSV au lieu de RVB, une seule boucle au lieu de 3 boucles imbriquées. La *représentation de couleur* que l’on choisit a un impact fort sur la résolution de l’exercice. Il faut probablement donner cette solution aux élèves, une fois qu’ils ont suffisamment essayé de résoudre l’exercice en utilisant le système RGB, car elle est difficile à trouver.

```{code-block} 
color_hsva = pygame.Color(0)

# parcourir les 360 teintes (les limites "se rejoignent")
for color_value in range(0,360) :

    # passer en représentation HSL pour parcourir les teintes
    color_hsva.hsva = (color_value,100,100,100)
```

*Avant de coder, il faut vous poser la question de comment représenter l'information dont vous avez besoin pour résoudre le problème.*


### Institutionnalisation n° 3

**[A faire après l'étape 6]** La relation entre HSV et RGB est visible dans la figure ci-dessous.

```{figure} media/HSV_to_RGB.png
---
alt: couleurs hsv saturées
width: 420px
name : hsv_saturated
---
```

*Dans le système HSV on fait varier les couleurs RGB une à la fois, dans un ordre bien précis. H représente la teinte, S la saturation et V la luminosité.*

### Institutionnalisation n° 4

**[A faire à la fin]** Il est trop difficile de résoudre un problème du premier coup. Il faut procéder de manière progressive, par petits paliers. Si l'on souhaite créer un variateur de couleurs, il faut définir des objectifs intermédiaires plus facilement atteignables, ici le parcours de luminosité ou un variateur noir et blanc.

*Pour résoudre un problème il faut le « découper », et le résoudre un bout à la fois. Il vaut mieux viser de multiples objectifs atteignables, qu'un seul objectif géant.*


### Institutionnalisation n° 5

**[A faire à la fin]** Le *versionnage* consiste à garder toutes les versions d'un même code. Le versionnage permet de se souvenir de la progression dans la résolution d'un problème et de ne pas "tout casser" lorsqu'on modifie le programme (on peut toujours revenir à une version qui marche). 

*Dans le cas d'un problème difficile à résoudre, le versionnage est essentiel. Il existe des outils de versionnage très aboutis, par exemple  « GitHub ».*



## Liens avec les autres thématiques

Les images dans *Représentation de l'information*.


## Ressources complémentaires

[https://download.tuxfamily.org/linuxgraphic/archives/grokking/node51.html](https://download.tuxfamily.org/linuxgraphic/archives/grokking/node51.html)
