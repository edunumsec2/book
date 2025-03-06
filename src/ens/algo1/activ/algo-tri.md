# Les algorithmes de tri

Activité de dévolution pour découvrir les algorithmes de tri.
Un dispositif physique ainsi qu'un catalogue d'opérations sont définis afin de forcer un cadrage algorithmique et rendre plus concrète la procédure de tri.  

----

```{admonition} Les algorithmes de tri 
:class: hint
* Thème : Algorithmique
* Niveau : `facile`
* Durée : 2 périodes consécutives
* Objectifs pédagogique : Découvrir quelques algorithmes de tri et leur pertinence sociétale
* Modalité : Débranché
* Matériel : plusieurs set de cartes numérotées (p.ex. jeu de Uno), papier, feuille comparateur (une feuille sur laquelles sont dessinés deux rectangle pour poser les deux cartes que l'on veut comparer), un peu d'espace pour se mouvoir dans la classse
* Prérequis: aucun
* Notions fondamentales : instruction, algorithme, tri, éventuellement complexité
* Taille du groupe : classe entière ou demi-classe (plus facile à gérer)

```



## Déroulement

|     Etape                             | Durée  | Phase de l'activité   | 
|---------------------------------------|------- |-----------------------|
|{ref}`Introduction<algo-tri.situation>`  autour du concept de l'archivage traditionnel, son histoire, son utilité, son organisation, ce qu'il a permis comme pratiques, et la fonction fondamentale du tri dans cette technique | 5-10 min | Mise en situation|
| {ref}`Essais<algo-tri.exploration>`  en groupe au cours de laquelle les élèves explorent des procédures de tri induites par un dispositif physique | 20-25 min | Exploration |
| {ref}`Mise en commun<algo-tri.miseencommun>` au cours de laquelle les élèves discutent et présentent les résultats de leurs recherches | 15 min | Objectivation / Apprentissage |
| {ref}`Formalisation<algo-tri.formalisation>`  des divers algorithmes de tri. | 20 min | Institutionnalisation |
| {ref}`Exercices<algo-tri.exercices>`  d'application des algorithmes.| 10-15 min | Application |
| {ref}`Conclusion<algo-tri.conclusion>`  en bouclant la boucle sur l'archivage informatisé et les pratiques (positives et négatives) qu'il permet. |5-10 min| Disussion|


(algo-tri.situation)=
### Introduction 

*Durée : 5-10 mn*

L'enseignant-e introduit la notion d'archivage de dossiers par l'état en en retraçant un bref historique. En particulier, le besoin pour les états naissants d'avoir un registres des habitants à taxer ou à enrôler dans l'armée, registres qui vont se développer avec l'apparition de
l'état social (pour déterminer le droits aux prestations) ou qui vont parfois tourner à la surveillance généralisée comme en RDA ou avec l'affaire
des fiches en Suisse. Cette introduction peut se faire avec des images historiques ou des vidéos, par exemple [celle-ci](https://www.rts.ch/play/tv/19h30/video/30-ans-apres-le-scandale-des-fiches?urn=urn:rts:video:10887317). L'idéal serait que les élèves visualisent bien les armoires contenants des miliers de dossiers afin de bien saisir l'importance du classement.

Ensuite l'enseignant-e insiste sur l'importance du classement afin de rendre ceci opérationnel, tout ce système fonctionne grâce à des personnes (souvent des secrétaires) capables de classer les dossiers selon un ordre donnée (alphabétique, numérique, etc.). Dans ce contexte, la digitalisation
des administrations publiques va nécessiter, entre autres, de transférer à l'ordinateur la capacité de tri des humains. C'est ce qu'on va voir pendant cette activité.  

Enfin l'enseignant-e demande à un-e élève de venir devant et de trier un tas de cartes, ce qu'il devrait pouvoir faire sans problème.
L'enseignant-e demande ensuite à l'élève comment iel a fait. L'élève sera probablement en peine de donner une méthode précise, iel l'aura
fait "naturellement". L'enseignant-e indique que cette méthode fonctionne bien pour des humains, mais pas pour des ordinateurs qui ont besoin
d'instructions beaucoup plus précises (ce qui sera clair pour ceux qui ont déjà fait de la programmation) et que c'est à cela que la classe va
s'atteler: quelle procédure donner à un ordinateur pour le rendre capable de trier des nombres (ou des mots). 

(algo-tri.exploration)=
### Essai par groupes

*Durée : 20-30 mn*

Pour ceci, on va s'aider d'un dispositif matériel constitué d'un paquet de cartes numérotées, d'un "comparateur" c'est-à-dire une feuille de papier sur laquelle on peut disposer exactement deux cartes à comparer, un marqueur (par exemple un jeton ou une gomme) et d'une table. Le tas de cartes ne doit pas contenir uniquement des nombres consécutifs, ce qui permettrait de classer directement la carte à la bonne position. Il peut contenir des doublons. 

Ensuite, l'enseignant-e démontre et affiche ou projette au tableau
les opérations disponibles qui sont:

Manipulation des cartes:
1. `mettre(haut/bas)`: Mettre la carte du haut/bas du tas dans le comparateur
1. `disposer (grande/petite, au-dessus/en-dessous)`: Prendre la plus grande/petite carte du comparateur et la disposer au-dessus/en-dessous du tas.

Manipulation des tas:
1. `séparer(gauche/droite)`: Séparer le tas courant de carte en deux parties égales (ou presque) et disposer la moitié supérieure à gauche/droite du tas courant
1. `initier(gauche/droite)`: Initier un nouveau tas courant à gauche/droite du tas.
1. `superposer(gauche/droite, au-dessus/en-dessous)`: Superposer le tas courant sur/sous le tas de gauche/droite

Manipulation du markeur:
1. `déplacer(gauche/droite)`: Déplacer le marqueur du tas courante d'un tas à gauche/droite.

Tests:
1. `vide`: Condition 1, le tas est vide.
1. `unique` Condition 2: il n'y a qu'un seul tas.
1. `plus grand que (G>D ou D>G)`: La carte de de gauche du comparateur est plus grande/petite que la carte de droite

Structures de contrôle:
1. `répéter jusqu'à` : Répéter jusqu'à ce que condition 1/2.
1. `si`: Si condition 1/2.

Toutes ces opérations, à l'exception des quatre dernières sont effectuée sur un tas donné, qui est indiqué en préfix de l'opération, par exemple `droite.mettre(haut)` qui signifie que cette opération s'applique sur le tas de droite. 
Dans la situation initiale, il n'y a qu'un seul tas mélangé sur la table.


Par groupe de deux ou trois, les élèves reçoivent un dispositif matériel (le comparateur et env. 7 cartes) et doivent tenter de trouver une procédure, un algorithme utilisant les opérations ci-dessus et permettant de trier le tas de carte. Ils doivent rédiger cet algorithme en utilisant les opérations ci-dessus. L'idée à ce stade n'est pas de bloquer les élèves avec les aspects formels, mais de les faire réfléchir sur une manière rigoureuse de trier les cartes. 

En guise d'exemple, la classe résout ensemble un problème plus simple qui consiste à insérer une nouvelle carte dans un tas de carte déjà ordonné. Dans la situation initiale, la carte se trouve dans le comparateur. 
Une solution possible est la suivante:
```
répeter jusqu'à courant.vide():
    courant.mettre()
    gauche.disposer(petite,au-dessous)
gauche.courant()
```
Cette on peut appeler cette fonction classer() et l'ajouter à notre répertoire de fonctions 

Si les élèves pensent avoir trouvé un algorithme qui fonctionne, iels doivent le
"rédiger" de manière non ambigüe et réessayer en remélangeant les cartes pour
voir si la procédure fonctionne encore. Si c'est le cas, iels doivent essayer
encore une fois, mais cette fois un-e élève fait les manipulations avec les
cartes faces cachée.
Cet-te élève ne peut pas voir les nombres sur les cartes et l'autre élève prend
le rôle du comparateur et ne fait qu'indiquer quelle carte du comparateur est
plus grande ou plus petite. De cette manière les élèves peuvent être certain-e-s
que l'algorithme fonctionne sans jugement humain.

Pendant cette phase, l'enseigant-e passe dans les groupes, clarifie au besoin,
oriente la recherche des élèves, propose éventuellement des
simplifications potentielle, et valide les méthodes trouvées.

(algo-tri.miseencommun)=
### Mise en commun

*Durée : 15 mn*

Selon le temps à disposition, il est possible de regrouper deux groupes de deux
(ayant chacun un autre algorithme, si possible) et chacun présente son
algorithme à l'autre groupe qui doit essayer de l'exécuter à l'aveugle. 

Chaque groupe va décrire sa méthode au reste de la classe, et l'illustrer en
triant les élèves des autres groupes. Chaque élève prend une feuille
de papier est écrit un nombre dessus. Les élève se disposent ensuite en file,
ce qui représente l'équivalent du tas de carte. L'enseignant-e indique au sol
(par exemple avec du scotch carrossier) la position du comparateur. Le groupe
qui présente sa méthode trie ainsi les élèves selon le numéros qu'ils ont
indiqué sur leur feuille. Pendant ce temps les élèves essaient de comprendre la
méthode exposée. L'enseignant peut ensuite présenter les algorithmes qu'il
souhaite également aborder. 

(algo-tri.formalisation)=
### Formalisation

*Durée : 20 mn*

Les élèves rejoignent leur place et l'enseignant récapitule (au tableau) avec
un exemple les méthodes présentées et indique leur nom. Il peut
à ce moment également en donner une représentation plus standard, qui
s'abstrait du dispositif matériel en s'appuyer sur le
document de théorie. Cette partie peut être entrelacée avec la partie
précédente.

#### Tri à bulles
```
répeter jusqu'à courant.vide():
    courant.mettre(haut)
    répéter jusqu'à courant.vide():
        courant.mettre(haut)
        droite.disposer(petit,au-dessous)
    gauche.disposer(seul,au-dessus)
    droite.courant()
gauche.courant()
```    
#### Tri par insertion
```
répéter jusqu'à courant.vide():
    courant.mettre(haut)
    gauche.classer()
gauche.courant()
```

#### Tri par pivot (quicksort)
````
répéter tant qu'il y des tas avec au moins deux cartes:
    courant.mettre(haut, gauche):
    initier(gauche)
    initier(droite)
    répéter jusqu'à courant.vide():
        courant mettre(haut,droite)
        si plus grand que (G>D):
            disposer(petite, gauche)
        sinon
            disposer(grande, droite)
    disposer(seule,courant)
    déplacer le marqueur vers le tas avec au moins 2 cartes le plus à droite
superposer tous les tas de gauche à droite.
````

```{admonition} Remarque
Le tri par sélection n'est pas vraiment adaptés à ce dispositif physique basé sur les
piles. Une variante de l'activité consisterait à donner au autre dispositif basé sur les tableaux à une partie de la classe afin de faire émerger ces algorithmes. 
```
 
(algo-tri.exercices)=
### Exercices

*Durée : 10-15 mn*

Toujours par groupes, les élèves vérifient que ces algorithmes peuvent être utilisés "à l'aveugle", c'est-à-dire
avec les cartes retournées et un-e élève prenant le rôle du comparateur. 

Ensuite, l'enseignant-e donne une suite de noms non triés et les élèves doivent écrire les différentes étapes du tri en utilisant d'une part le tri à bulles et d'autre part le tri par insertion. 

Une correction commune est ensuite effectuée. 

(algo-tri.conclusion)=
### Conclusion

*Durée : 5-10 mn*

Une présentation des dérapages de la surveillance de masse à l'heure du numérique avec l'affaire Snowden (cf ressources sur les enjeux de société)
