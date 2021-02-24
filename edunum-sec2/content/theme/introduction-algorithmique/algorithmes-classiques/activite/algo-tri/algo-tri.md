# Les algorithmes de tri

TODO: compléter

## Informations:

Durée: 2 périodes consécutives

Mode: Débranché

Chapitre: Algorithmique

Objectifs: Découvrir les algorithmes de tri et leur pertinence sociétale

Matériel: plusieurs set de cartes numérotées (p.ex. jeu de Uno), papier, feuille comparateur, un peu d'espace pour se mouvoir dans la classe

## Introduction

Ceci est une activité de dévolution pour découvrir les algorithmes de tri.
Un dispositif physique ainsi qu'un catalogues d'opération sont définis afin de forcer un cadrage algorithmique et rendre plus concrète la procédure de tri  


## Déroulement

Cette activité les phases suivantes:

1. Une mise en situation générale autour du concept de l'archivage traditionnel,
son histoire, son utilité, son organisation, ce qu'il a permis comme pratique, et la fonction
fondamentale du tri dans cette technique

1. Une phase d'exploration en groupe au cours de laquelle les élèves explorent des procédures de tri
induites par un dispositif physique

1. Une phase de mise en commune au cours de laquelle les élèves discute et présentent les résultats de
leurs recherche

1. Une phase de formalisation (et institutionnalisation) des divers algorithmes de tri. 

1. Une phase d'exercices (ou exemples) d'application des algorithmes.

1. Une phase de conclusion en bouclant la boucle sur l'archivage informatisé et les pratiques (positives et négatives) qu'il permet.

## 1 Mise en situation (5-10 min)
L'enseignant-e introduit la notion d'archivage de dossiers par l'état en en retraçant un bref historique. En particulier, le besoin pour les
états naissants d'avoir un registres des habitants à taxer ou à enrôler dans l'armée, registres qui vont se développer avec l'apparition de
l'état social (pour déterminer le droits aux prestations) ou qui vont parfois tourner à la surveillance généralisée comme en RDA ou avec l'affaire
des fiches en Suisse. Cette introduction peut se faire avec des images historiques ou des vidéos, par exemple https://www.rts.ch/info/suisse/10886146-le-scandale-des-fiches-eclatait-en-suisse-il-y-a-tout-juste-trente-ans.html. L'idéal serait que les élèves visualisent bien les armoires contenants des miliers de dossiers afin de bien saisir l'importance du classement.

Ensuite l'enseignant-e insiste sur l'importance du classement afin de rendre ceci opérationnel, tout ce système fonctionne grâce à des personnes (souvent des secrétaires) capables de classer les dossiers selon un ordre donnée (alphabétique, numérique, etc.). Dans ce contexte, la digitalisation
des administrations publiques va nécessiter, entre autres, de transférer à l'ordinateur la capacité de tri des humains. C'est ce qu'on va voir pendant cette activité.  

Enfin l'enseignant-e demande à un-e élève de venir devant et de trier un tas de cartes, ce qu'il devrait pouvoir faire sans problème.
L'enseignant-e demande ensuite à l'élève comment iel a fait. L'élève sera probablement en peine de donner une méthode précise, iel l'aura
fait "naturellement". L'enseignant-e indique que cette méthode fonctionne bien pour des humains, mais pas pour des ordinateurs qui ont besoin
d'instructions beaucoup plus précises (ce qui sera clair pour ceux qui ont déjà fait de la programmation) et que c'est à cela que la classe va
s'atteller: quelle procédure donner à un ordinateur pour le rendre capable de trier des nombres (ou des mots). 

## 2 Exploration (20-30 min)

Pour ceci, on va s'aider d'un dispositif matériel constitué d'un paquet de cartes numérotée, d'un "comparateur" c'est-à-dire une feuille de papier
sur laquelle on peut disposer exactement deux cartes à comparer et d'une table. Le tas de cartes ne dois pas contenir uniquement des nombres consécutifs, ce qui permettrait de classer directement la carte à la bonne position. Il peut contenir des doublons. 

Ensuite, l'enseignant-e décrit et affiche ou projette au tableau
les opérations disponibles qui sont:

1. mettre(haut/bas, courant/gauche/droite): Mettre la carte du haut/bas du tas courant/de gauche/de droite dans le comparateur
1. disposer (grande/petite, au-dessus/en-dessous, courant/gauche/droite): Prendre la plus grande/petite carte du comparateur et la disposer au-dessus/en-dessous du tas courant/de gauche/de droite.
1. séparer(gauche/droite): Séparer le tas courant de carte en deux parties égales (ou presque) et disposer la moitié supérieure à gauche/droite du tas courant
1. initier(gauche/droite): Initier un nouveau tas courant à gauche/droite du tas courant actuel
1. déplacer(gauche/droite): Déplacer le marqueur du tas courante d'un tas à gauche/droite
1. vide(courante/gauche/droite) condition 1: le tas courant/de gauche/de droite est vide
1. unique() condition 2: il n'y a qu'un seul tas
1. répéter jusqu'à : Répéter jusqu'à ce que condition 1/2
1. si: Si condition 1/2

Dans la situation initiale, il n'y a qu'un seul tas mélangé sur la table.


Par groupe de deux ou trois, les élèves reçoivent un dispositif matériel et doivent tenter de trouver une procédure, un algorithme utilisant les opérations ci-dessus et permettant de trier le tas de carte. Ils doivent rédiger cet algorithme en ordonnçant les opérations ci-dessus.

En guise d'exemple, la classe résoud ensemble un problème plus simple qui consiste à insérer une nouvelle carte dans un tas de carte déjà ordonné. Dans la situation initiale, la carte se trouve dans le comparateur. 
Une solution possible est la suivante:
```
répeter jusqu'à courant.vide():
    courant.mettre()
    droite.disposer(petite,au-dessous)
droite.courant()
```
Cette on peut appler cette fonction courant.classer() et l'ajouter à notre répertoire de fonctions 

S'ils pensent avoir trouvé un algorithme qui fonctionne, ils doivent réessayer en remélangeant les cartes pour voir si la procédure fonctionne encore. Si c'est le cas, ils doivent essayer encore une fois, mais cette fois un-e élève fait les manipulations avec les cartes faces cachées
(cet élève ne peut pas voir les nombres sur les cartes et l'autre élève prend le rôle du comparateur et ne fait qu'indiquer quelle carte du comparateur est plus grande ou plus petite. De cette manière les élèves peuvent être certain-e-s que l'algorithme fonctionne sans jugement humain.

Pendant cette phase, l'enseigant-e passe dans les groupes, clarifie au besoin, oriente la recherche des élèves, propose éventuellement des
simplifications potentielle, et valide les méthodes trouvées.


## 3 Mise en commun (15 min)

Chaque groupe va décrire sa méthode au reste de la classe, et l'illustrer en triant les élèves des autres groupes. Chaque élève prend une feuille
de papier est écrit un nombre dessus. Les élève se disposent ensuite en file, ce qui représente l'équivalent du tas de carte. L'enseigant-e indique au sol (par exemple avec du scotch carrossier) la position du comparateur. Le groupe qui présente sa méthode trie ainsi les élèves selon le numéros qu'ils ont indiqué sur leur feuille. Pendant ce temps les élèves essaient de comprendre la méthode exposée. L'enseignant peut ensuite présenter
les algorithmes qu'il souhaite également aborder. 


## 4 Formalisation (20 min)
Les élèves rejoignent leur place et l'enseignant récapitule (au tableau) avec un exemple les méthodes présentées et indique leur nom. Il peut
à ce moment également en donner une représentation plus standard, qui s'abstrait du dispositif matériel en s'appuyer sur le
document de théorie. Cette partie peut être entrelacée avec la partie précédente.

### Tri à bullles
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
### Tri par insertion
```
répéter jusqu'à courant.vide():
    courant.mettre(haut)
    gauche.classer()
gauche.courant()
```

### Tri par sélection (pas vraiment)
 Non adapté à ce dispositif...
 

## 5 Application (10-15 min)
Exercices d'application au cours desquels les élèves doivent trier des listes selon divers algorithmes.

TODO: rédiger les exercices.  


## 6 Conclusion (5-10 min)
Une présentation des dérapage de la surveillance de masse à l'heure du numérique avec l'affaire Snowden

TODO: faire le lien avec les fiches et ressources d'enjeux sociétaux proposés
