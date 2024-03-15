(simulateur)=
Simulateur logique
==================

Cette fiche ne décrit pas une activité précise en soi, mais fournit un guide de prise en main rapide pour utiliser le simulateur logique dans différentes circonstances.

Pour le chapitre traitant l'architecture des ordinateur, un éditeur et simulateur de circuits logiques (appelé plus bas simplement «simulateur») a été conçu. Il est utilisé dans les pages de Modulo à l'intention des élèves pour afficher des schémas logiques, mais il peut être mis en œuvre indépendamment de plusieurs façon et a été conçu pour offrir une grande flexbilité d'intégration.

Bien que le simulateur puisse bien sûr être utilisé pour construire des circuits logiques à partir de zéro, il est recommandé, à l'instar de ce qui est fait dans les pages de Modulo, de commencer par fournir aux élèves des circuit logiques complets à essayer, à modifier ou à compléter avant de leur proposer de les construire intégralement. Les paragraphes ci-dessous décrivent comment.

<!-- Use – Modify – Create

PRIMM -->

_**Note:** le simulateur logique fonctionne avec des technologies mises à disposition par des navigateurs web récents. Des navigateurs obsolètes ou pas mis à jour peuvent causer des problèmes d'affichage ou d'interaction. En particulier, Internet Explorer n'est pas pris en charge._


## Types de mises en œuvre

Le simulateur logique peut être utilisé:

  1. Dans les cadres des exemples et exercices prépréparés dans les pages existantes de Modulo 
  1. En tant que plateforme indépendante à part entière, via l'URL <https://logic.modulo-info.ch>
  1. Sur des pages web tierces que vous contrôlez:
     * … en ajoutant incluant un script JavaScript et un élément HTML à votre page (la méthode recommandée); ou
     * … en incluant une page de <https://logic.modulo-info.ch> via une `<iframe>`.

Dans cas d'une mise en œuvre via les pages de Modulo, aucune instruction d'utilisation supplémentaire n'est nécessaire: les élèves accèdent simplement aux pages de Modulo et les exemples et exercices préparés sont disponibles.

À noter qu'aucune sauvegarde n'est faite du travail réalisés sur ces pages. Avant de quitter la page, si les élèves souhaitent conserver leur travail de conception d'un circuit, ils devront le télécharger explicitement. Un bouton «Télécharger» est mis à disposition lorsqu'il s'agit de concevoir un circuit ou de connecter des composants; le fichier ainsi téléchargé peut être ensuite glissé dans une fenêtre de <https://logic.modulo-info.ch> pour afficher le circuit.

Dans ce cas d'une utilisation directe de la plateforme ou d'inclusion du simulateur dans d'autres pages web, il est souvent souhaitable de diffuser un circuit logique de départ, complet ou partiel et, si jugé opportun, de restreindre les types interactions possibles avec le circuit. La section suivante explique comment.


## Diffusion de circuits logiques

Le simulateur ne stocke pas de données de circuit côté serveur, mais facilite la distribution de circuit en les encodant directement comme paramètre d'URL. L'URL suivante, via le paramètre `data`, ouvre le simulateur avec un circuit prédéfini — ici, une simple porte **ET**.

    https://logic.modulo-info.ch/?data=N4KABGBEBukFxgEwBpxQJYDt5gNrEgAcB7AZx1wFYAGZMGgXTsnQBMdapoBDAGw4C+dAiXIJcANk4BGAMzUmGdgmnMe-BNQFM0kAObcALgFMxeAoYCehYzkgBBAHIARSM1EVpAdk4BOBcxYFChgsoqQxACuhjgALNqoEBHRFCJkwT50-uFsOJQJugDu6ABOphS4sXSUiriciLWqoQwMIAJAA

Ces URL étant longues, il est recommandé de les cacher derrière un lien. En HTML, une balise de type `<a href="...">voici une porte ET</a>`) donnera ceci, founissant en un clic l'accès à ce circuit: [voici une porte ET](https://logic.modulo-info.ch/?mode=full&data=N4KABGBEBukFxgEwBpxQJYDt5gNrEgAcB7AZx1wFYAGZMGgXTsnQBMdapoBDAGw4C+dAiXIJcANk4BGAMzUmGdgmnMe-BNQFM0kAObcALgFMxeAoYCehYzkgBBAHIARSM1EVpAdk4BOBcxYFChgsoqQxACuhjgALNqoEBHRFCJkwT50-uFsOJQJugDu6ABOphS4sXSUiriciLWqoQwMIAJAA).


### Génération d'un lien de diffusion

 1. Se rendre sur <https://logic.modulo-info.ch> et préparer le circuit à diffuser
 1. Cliquer sur le bouton de partage avec l'icône de lien en haut à droite (voir figure ci-dessous)
 1. Copier l'URL qui apparaît
    * Si l'URL est imprimée, on peut choisir sa représentation sous forme de QR code


```{figure} media/LogicShare.png
Petit circuit logique d'exemple avec, entouré, le bouton menant aux liens de partage.
```


### Mode d'interaction avec le simulateur

Pour les élèves, les interactions avec un circuit peuvent se faire selon plusieurs modalités, suivant l'exercice à réaliser. En allant directement sur la plateforme, il est possible de choisir le mode d'interaction à adopter via le sélecteur de droite.

Ces modes sont les suivants:

 * Le mode **statique** affiche uniquement le circuit logique sans permettre d'interaction avec. On ne peut ainsi ni le modifier, ni changer les valeurs des entrées. Cela équivaut presque à partager une image du circuit. Le menu montrant la liste des composants disponibles est masqué.
 * Le mode **test** permet en plus de changer les valeurs d'entrées et d'observer le résultat de la propagation des valeurs. On peut ainsi interagir avec le circuit sans pour autant en modifier la structure.
 * Le mode **connexion** permet en plus de connecter des composants existants et de les réarranger. On ne peut toujours pas ajouter de nouveaux composants.
 * Le mode **complet** affiche la liste des composants et est le premier qui permet de créer des circuits à partir d'un canevas vide.
 * Finalement, le mode **admin** donne des outils supplémentaires pour régler d'autres paramètres du circuit logique ainsi que d'autres outils comme la création de circuits volontairement défecteux à des fins pédagogiques ou l'affichage d'une porte logique différente de la fonction logique vraiment réalisée. Ces fonctionnalités supplémentaires sont décrites plus bas.

Ainsi, avant de copier un lien de partage, on peut choisir un de ces modes d'interaction, qui sera également transmis via l'URL. Voici par exemple le même petit circuit que ci-dessous, partagé selon ces modes:

[Statique](https://logic.modulo-info.ch/?mode=static&data=N4KABGBEBukFxgEwBpxQJYDt5gNrEgAcB7AZx1wFYAGZMGgXTsnQBMdapoBDAGw4C+dAiXIJcANk4BGAMzUmGdgmnMe-BNQFM0kYgFcALhRFkKiAOycAnAuZsclbagiQA5t0MBTMXgKGAT0IvHEgAQQA5ABFIZlEKaSs6W0UWbHEUMFlUg2MEABZnXQB3dAAnHwpcfLpKRVxORHrVLIYGEAEgA) | [Test](https://logic.modulo-info.ch/?mode=tryout&data=N4KABGBEBukFxgEwBpxQJYDt5gNrEgAcB7AZx1wFYAGZMGgXTsnQBMdapoBDAGw4C+dAiXIJcANk4BGAMzUmGdgmnMe-BNQFM0kYgFcALhRFkKiAOycAnAuZsclbagiQA5t0MBTMXgKGAT0IvHEgAQQA5ABFIZlEKaSs6W0UWbHEUMFlUg2MEABZnXQB3dAAnHwpcfLpKRVxORHrVLIYGEAEgA) | [Connexion](https://logic.modulo-info.ch/?mode=connect&data=N4KABGBEBukFxgEwBpxQJYDt5gNrEgAcB7AZx1wFYAGZMGgXTsnQBMdapoBDAGw4C+dAiXIJcANk4BGAMzUmGdgmnMe-BNQFM0kYgFcALhRFkKiAOycAnAuZsclbagiQA5t0MBTMXgKGAT0IvHEgAQQA5ABFIZlEKaSs6W0UWbHEUMFlUg2MEABZnXQB3dAAnHwpcfLpKRVxORHrVLIYGEAEgA) | [Complet](https://logic.modulo-info.ch/?mode=design&data=N4KABGBEBukFxgEwBpxQJYDt5gNrEgAcB7AZx1wFYAGZMGgXTsnQBMdapoBDAGw4C+dAiXIJcANk4BGAMzUmGdgmnMe-BNQFM0kYgFcALhRFkKiAOycAnAuZsclbagiQA5t0MBTMXgKGAT0IvHEgAQQA5ABFIZlEKaSs6W0UWbHEUMFlUg2MEABZnXQB3dAAnHwpcfLpKRVxORHrVLIYGEAEgA) | [Admin](https://logic.modulo-info.ch/?mode=full&data=N4KABGBEBukFxgEwBpxQJYDt5gNrEgAcB7AZx1wFYAGZMGgXTsnQBMdapoBDAGw4C+dAiXIJcANk4BGAMzUmGdgmnMe-BNQFM0kYgFcALhRFkKiAOycAnAuZsclbagiQA5t0MBTMXgKGAT0IvHEgAQQA5ABFIZlEKaSs6W0UWbHEUMFlUg2MEABZnXQB3dAAnHwpcfLpKRVxORHrVLIYGEAEgA)

Attention, tous ces liens contiennent l'intégralité de la structure de circuit et ne sont pas une référence vers un circuit existant (à la différence des liens vers, par exemple, Google Docs, qui sont une référence fixe vers un document modifiable). Cela signifie qu'une modification du circuit _après_ le partage du lien ne sera pas prise en compte: il faudra générer un nouveau lien pour récupérer le circuit modifié.

Notons que la longueur d'une URL est limitée et que des liens avec de gros circuits risquent de ne pas être reconnus. Dans ce cas, il faut passer par la diffusion de fichiers JSON comme décrit ci-dessous ou par l'inclusion dans un site tiers avec le système des web components.


### Affichage de certains composants uniquement

Lorsqu'un circuit est partagé en mode complet, il est possible de ne pas afficher l'intégralité des composants dans le menu de droite. On peut par exemple afficher un simulateur «épuré» et ne proposer que des entrées et sorties 1 bit et une sélection resteinte de portes.

Ceci se fait «à la main» en rajoutant le paramètre d'URL `showonly`. Par exemple, [ce lien](https://logic.modulo-info.ch/?showonly=in,out,and,or,xor) affiche quelques portes uniquement et est formé ainsi:

    https://logic.modulo-info.ch/?showonly=in,out,and,or,xor


## Sauvergarde et chargement de circuits

Si le partage de circuit via un lien ne convient pas, il est possible de partager des fichiers JSON contenant la structure du circuit.

Lorsque l'éditeur est dans un mode qui permet la modification de circuits, les boutons de contrôle apparaissent à droite (voir la figure ci-dessus). Le bouton **Télécharger** permet de sauvegarder en local un fichier qui contient la structure du circuit. Les possibilités d'accès aux fichiers depuis un navigateur étant restreintes, il n'est pas possible de choisir un autre emplacement de téléchargement que ce que votre navigateur décidera.

Pour charger un circuit, on utilisera le bouton **Ouvrir**. Il faut choisir un fichier JSON précédemment téléchargé. C'est aussi possible de direcement glisser dans la zone de l'éditeur un fichier JSON au lieu de cliquer sur le bouton.

Le bouton **Screenshot** télécharge une image du circuit actuel au format PNG. Comme la description du circuit est incluse dans les métadonnées du fichier PNG, il est aussi possible de charger un circuit depuis un tel fichier PNG. (Il n'est naturellement pas possible de charger un circuit depuis un fichier PNG qui ne contiendrait pas ou plus les métadonnées appropriées.)



## Fonctionnalités du simulateur

Le simulateur logique permet de glisser des componsants logiques depuis la liste de gauche sur le canevas princpal et de des connecter en cliquant et glissant depuis un nœud de sortie vers un nœud d'entrée (ou inversement).

Les connexions véhiculant la valeur logique 1 sont affichées de façon colorée et celles qui véhiculent la valeur logique 0 sont affichées en noir. Dès qu'une entrée change, sa valeur est propagée aux composants connectés, puis au suivant, et ainsi de suite, mettant ainsi à jour l'état du circuit.

Plusieurs réglages sont disponibles pour le simulateur, détaillés ci-dessous avec chaque fois comme illustration d'un circuit directement inclus dans la page en plus du lien l'ouvrant directement sur <https://logic.modulo-info.ch>.


### Délai de propagation

Les changements de valeur mettent un peu de temps pour se propager à l'autre bout d'une connexion (par défaut, 100 ms). Les changements sont animés le long des connexions. Le délai de propagation ne dépend pas de la longueur des connexions.

Exemple avec un délai de propagation de 100 ms ([lien](https://logic.modulo-info.ch/?mode=full&data=N4KABGBEBukFxgEwBpxQJYDt5gNrEgAcB7AZx1wA4AGZMANmoF07J0ATHWqaAQwBsuAXzoES5BFW4BGac1Ycc01n0EJpIsGLIUadaYxYZOCFDwFKhLNJADmvAC4BTCXgIOAnoSc5IAQQA5ABFIVnEKRERuGiM2bEkAZjoAFljiAFcHHABWTXcvHwR-YNCocMTsmWp5DHi8ejoAdjTMnEorVAhIDKzJbVdcZL0wORq2EzAATg6bAHd0ACcXClxuBKNcZTBUulxsunoNs2bdyjpJpiYQISA)) — commutez la première entrée pour voir le signal se propager:

```{logic}
:height: 220
:mode: tryout

{
  "v": 3,
  "in": [{"pos": [80, 60], "id": 0, "val": 0}, {"pos": [80, 110], "id": 1, "val": 1}, {"pos": [80, 160], "id": 2, "val": 1}],
  "gates": [{"type": "AND", "pos": [220, 80], "in": [3, 4], "out": 5}, {"type": "AND", "pos": [350, 100], "in": [6, 7], "out": 8}],
  "out": [{"pos": [480, 100], "id": 9}],
  "wires": [[0, 3], [1, 4], [5, 6], [2, 7], [8, 9]]
}
```

Même exemple, avec un délai de propagation de 1000 ms ([lien](https://logic.modulo-info.ch/?mode=full&data=N4KABGBEBukFxgEwBpxQPYAcAuBneYwkmATlgIYDm52AlugHYAiApgDbkCeBAjAAwCAvqgiRaDAgG0imdPgSSAHH2RgAbHwC6qsQBMCKqNHJsDwwsTlTlqnv21Ra+hDx3HTL8zKsKbYHhoOegQoRia8gtpokNTYLPJg0pDYnJgsBJAAggByTJA6sgmSiIiGykHiUgDMqgAsQegArtgEAKxeyanpCFm5+VCF1a2G-Fo6lQpqqgDsDc0EipEiGPMK3kW1fqMVzmAAnEvRAO60JPFSkoZVDpKuYPWqkq2qajehs4+KqnuamiCCQA)):

```{logic}
:height: 220
:mode: tryout

{
  "v": 3,
  "opts": {"propagationDelay": 1000},
  "in": [{"pos": [80, 60], "id": 0, "val": 0}, {"pos": [80, 110], "id": 1, "val": 1}, {"pos": [80, 160], "id": 2, "val": 1}],
  "gates": [{"type": "AND", "pos": [220, 80], "in": [3, 4], "out": 5}, {"type": "AND", "pos": [350, 100], "in": [6, 7], "out": 8}],
  "out": [{"pos": [480, 100], "id": 9}],
  "wires": [[0, 3], [1, 4], [5, 6], [2, 7], [8, 9]]
}
```

Sur cet exemple, on voit que le délai de propatation s'applique, pour simplifier et faciliter la visualisation, aux connexions, et non aux composants.

Le délai de propagation se règle dans la petite palette des réglages, qui s'affiche en cliquant sur la petite roue dentée à côté du mode Admin:

```{figure} media/LogicSettings.png
La palette de réglages applicables à un circuit logique dans son ensemble, avec les valeurs par défaut.
```


### Connexions affichées de manière neutres

D'habitude, les circuits, même statiques, montrent les valeurs véhiculées ([lien](https://logic.modulo-info.ch/?mode=full&data=N4KABGBEBukFxgEwBpxQJYDt5gNpomEgAcB7AZx1wFYAGZMATloF0HJ0ATHAZncwCGAWwCmOSAA1I7aAIA2OAIwBfVBEIkKVOg0UAOVuy44ALP2FiEkAJrSoshQlqqCYImUoIa9JADZDGNwIiormouIAWnYw8krKaGxokKQArgAuVO5aXiYGDHRsUKQATugimBlW2EZBYNRhllAASiJp5Sliqm6annjU-vkByaXllVDVgTiMDeIAyqRC4cqJEJAA5gJtvfjq3WkAnsSNkACCAHIAItEeVIoA7D6KtENYVI+Fyek4iC67RAdHcQSADyTWu2Tw90eDw+ry8vgYdw+qTGel+6n+h2O5yu7BuXh4z10Blh2C8ihQYEUPGRX2CJnRGgBxxBYLxENwhJ8iAKRjJkPqVN8tLG90Zeyx4lB4O2JiJVKepNuel0jBF32cCTUUAA7uhiiJtpyGAFcGYqYVjWBhQwzYjLSqqYgHbpqJaQroabaPUL3XcGGrvebFIG8JT9JbED43SwQMogA)):

```{logic}
:height: 310
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 90], "id": 3, "name": "X", "val": 1},
    {"pos": [50, 180], "id": 4, "name": "Y", "val": 0},
    {"pos": [50, 260], "id": 11, "name": "Z", "val": 1}
  ],
  "out": [{"pos": [480, 50], "orient": "n", "id": 5, "name": "Retenue"}, {"pos": [560, 50], "orient": "n", "id": 9, "name": "Somme"}],
  "gates": [
    {"type": "AND", "pos": [170, 100], "in": [0, 1], "out": 2},
    {"type": "XOR", "pos": [170, 170], "in": [6, 7], "out": 8},
    {"type": "AND", "pos": [300, 180], "in": [12, 13], "out": 14},
    {"type": "XOR", "pos": [300, 250], "in": [15, 16], "out": 17},
    {"type": "OR", "pos": [400, 110], "in": [18, 19], "out": 20}
  ],
  "wires": [[3, 0], [4, 1], [3, 6], [4, 7], [8, 12], [8, 15], [11, 13], [11, 16], [17, 9], [14, 19], [2, 18], [20, 5]]
}
```

Via les mêmes réglages du circuit que décrit plus haut, on peut les afficher de manière neutre et demander aux élèves de les déterminer ([lien](https://logic.modulo-info.ch/?mode=full&data=N4KABGBEBukFxgEwBpxQPYAcAuBneYwkAFgJYAmApgOqkBOlAwugDbp34LZ0CulyUMlQDyPbJjHM2HAtz4BfVBEikAdgQDaaCEUzpOYDQFYADAICcJgLoCV5AgGZbqgIYBbSgUgANSLeguLAQAjIrahJB6BsZmYMEAHNa2FAQALM7ungiQAJp+UAFBCCZhEDqR+pqmAogAbElQKQjBwRkeXgBa+TCBIfJoNmiQ6GKaupUIGqmJAqY2GHSklKrYXurJ9ghGbVlQAEqU2Mt8kIoRUVX1sw3Di8ur2euNm2DmO14Ayuhu7fKDygBzFxHaLhIjYACemF2kAAggA5AAi3Quk2CAHZYsETDc1JosfNhqMEIhSmVwVCYd5hHsURNDBisZjCXjJrUBOjCSMHmB4mTypDoV4EcjbKjDA4cQIErj1GiUHEHFziXFUvyIoKqTS6dFJbFEHNknKGds4rVlTyMeqKULstqxfSplK4tiWcaNAlpeYLQRECUBkooAB3eiUaIaJxgBpTaXzCMCc0CGNgTlJ+LSxBx9NxIxxlrSpVJ-NmvPoix59Jxb1JhUJON+2ZWKwgeRAA)):

```{logic}
:height: 310
:mode: tryout

{
  "v": 3,
  "opts": {"hideWireColors": true, "hideOutputColors": true},
  "in": [
    {"pos": [50, 90], "id": 3, "name": "X", "val": 1},
    {"pos": [50, 180], "id": 4, "name": "Y", "val": 0},
    {"pos": [50, 260], "id": 11, "name": "Z", "val": 1}
  ],
  "out": [{"pos": [480, 50], "orient": "n", "id": 5, "name": "Retenue"}, {"pos": [560, 50], "orient": "n", "id": 9, "name": "Somme"}],
  "gates": [
    {"type": "AND", "pos": [170, 100], "in": [0, 1], "out": 2},
    {"type": "XOR", "pos": [170, 170], "in": [6, 7], "out": 8},
    {"type": "AND", "pos": [300, 180], "in": [12, 13], "out": 14},
    {"type": "XOR", "pos": [300, 250], "in": [15, 16], "out": 17},
    {"type": "OR", "pos": [400, 110], "in": [18, 19], "out": 20}
  ],
  "wires": [[3, 0], [4, 1], [3, 6], [4, 7], [8, 12], [8, 15], [11, 13], [11, 16], [17, 9], [14, 19], [2, 18], [20, 5]]
}
```

Toujours via ces réglages, on peut également afficher le type des portes pour proposer une aide à l'interprétation d'un circuit ([lien](https://logic.modulo-info.ch/?mode=full&data=N4KABGBEBukFxgEwBpxQPYAcAuBneYwkuAFugO4DiAhtgKYAqAnpnfgtgE4CudyUJAJYATOgHVBnOgGF0AG3Sd2YLr36QhogPLdsmXbIVKCqugF9UESIIB2BANpoIRTOmX2ArAAZ+ATi8AuuoiBADM6jbUALZ0BJAAGpDq0NRyBACMFk6EkK7u3vzpAByBwcIEACwR0bEIkACaSVApaQheWRDOuW4OBUgAbKVQIQjp6dUxcQBaTTCpGWZoQWiQ6LoOLj0I9hUl-N5BGJyCdDbYcXZlBB4TtVAASnT0NryQFjl5vYP7Q6vHp+c6pdhuUEL5bnEAMroKKTMzLKwAc1obAc2SI2BYd0gAEEAHIAEVmn226QA7D4wOkvL9bA5KelDqt1ghEB1OhisXF4lp7sStmB7OSGRSmXTtv1+GSmWtAWAiuyupjWHF8UT1CTBaEaYUSmK7KSUFTQjKWVSKoqcsrsTy+RqBfZtZTEAdggbBekblT+qa5eTLZyVXVefz3BUdVTqfqHMVCr5fQREO0lpYoORJKjto7+EMdoVDtmwD7+HmwNKS0VCogC5WqR4C2NCiaS43vQ2yX4G1UqfGS0bigWk-sAgEQGYgA)):

```{logic}
:height: 310
:mode: tryout

{
  "v": 3,
  "opts": {"showGateTypes": true, "hideWireColors": true, "hideOutputColors": true},
  "in": [
    {"pos": [50, 90], "id": 3, "name": "X", "val": 1},
    {"pos": [50, 180], "id": 4, "name": "Y", "val": 0},
    {"pos": [50, 260], "id": 11, "name": "Z", "val": 1}
  ],
  "out": [{"pos": [480, 50], "orient": "n", "id": 5, "name": "Retenue"}, {"pos": [560, 50], "orient": "n", "id": 9, "name": "Somme"}],
  "gates": [
    {"type": "AND", "pos": [170, 100], "in": [0, 1], "out": 2},
    {"type": "XOR", "pos": [170, 170], "in": [6, 7], "out": 8},
    {"type": "AND", "pos": [300, 180], "in": [12, 13], "out": 14},
    {"type": "XOR", "pos": [300, 250], "in": [15, 16], "out": 17},
    {"type": "OR", "pos": [400, 110], "in": [18, 19], "out": 20}
  ],
  "wires": [[3, 0], [4, 1], [3, 6], [4, 7], [8, 12], [8, 15], [11, 13], [11, 16], [17, 9], [14, 19], [2, 18], [20, 5]]
}
```

Notons qu'ici, commuter les entrées n'a aucun effet visible. Ces trois circuits, qui ont été partagés en mode test, auraient très bien pu être partagés en mode statique.

Inversément, on peut décider de masquer une porte, dont la fonction doit être retrouvée en testant le circuit. Par exemple, ici, la porte cachée réalise un OU-X à 3 entrées ([lien](https://logic.modulo-info.ch/?mode=full&data=N4KABGBEBukFxgEwBpxQJYDt5gNrEgAcB7AZx1wFYAGZMAFmoF07J0ATHWqaAQwBsuAXzoES5BFW4AOZqw44AjKz6CE1EWDFkKNOosRyMnBCh4DhLNJGIBXAC4VtEvIll1ZLYzgDsQqxCQAOa89gCmLviQ9gCehGE4kAAaAPIASgDMkKziFIruYJ7y2JIZdPR0lF42DjgAbKykABbEAO4AgqQAqpgA1phtJWD2AE62Yf6oga3oIxEUuNwZXrjKDCtmVXS4DWA+TEwgQkA)):

```{logic}
:height: 160
:mode: tryout

{
  "v": 3,
  "in": [{"pos": [50, 40], "id": 0, "val": 0}, {"pos": [50, 80], "id": 1, "val": 0}, {"pos": [50, 120], "id": 2, "val": 0}],
  "out": [{"pos": [280, 80], "id": 7}],
  "gates": [{"type": "XOR3", "pos": [180, 80], "in": [3, 4, 5], "out": 6, "showAsUnknown": true}],
  "wires": [[0, 3], [1, 4], [2, 5], [6, 7]]
}
```

Pour afficher une porte ainsi, faites un clic droit en mode admin et choisissez «Porte inconnue» via le sous-menu «Afficher comme».


### Circuits défectueux

On peut faire en sorte qu’une porte s’affiche en fait comme une autre porte. La {logicref}`faultygate.faulty|porte de droite` de ce circuit réalise la fonction **OU**, mais s'affiche comme une porte **ET**:

```{logic}
:ref: faultygate
:height: 140
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [50, 30], "id": 3, "name": "X", "val": 0},
    {"pos": [50, 70], "id": 4, "name": "Y", "val": 0},
    {"pos": [50, 110], "id": 6, "name": "W", "val": 0}
  ],
  "out": [{"pos": [320, 70], "id": 5, "name": "Z"}],
  "gates": [
    {"type": "AND", "pos": [150, 50], "in": [0, 1], "out": 2},
    {"type": "OR", "pos": [260, 70], "ref": "faulty", "in": [7, 8], "out": 9, "poseAs": "AND"}
  ],
  "wires": [[3, 0], [4, 1], [6, 8], [2, 7], [9, 5]]
}
```

En mode admin, une telle porte s'affiche en rouge pour indiquer qu'elle est trompeuse. Vérifiez-le en ouvrant ce circuit avec [ce lien](https://logic.modulo-info.ch/?mode=full&data=N4KABGBEBukFxgEwBpxQJYDt5gNpomEgAcB7AZx1wFYAGZMAZloF0HJ0ATHR9zAQwC2AUxyQAGpHbR+AGxy0AvqgiESFKnQYB2Vuy44ALHyGiEkAJpSoM+QiUrVRMpQQ16YAIye9GbggA2ExExAHVrGDkFRTQ2NEhSAFcAFypnDTdGRA9dNj8camCzKAAtSEU4iEgAc35k4Vc8AjAiZIBPYmLIAEEAOQARCJcqTy0wOjyObDcPT0mk1IREZWbWjq6AeQAlIYy8RACc30gAJ2EAMzFz-kTZdoisKm0GAA55lJwATnYXYW7GnoDcqxRyQADu6DOjVwuF4YF8uGMXjyuCCYDeDFwKDA2hR33GLBYIEUQA
).

Pour changer l'affichage d'une porte, faites un clic droit en mode admin et choisissez une autre apparence via le sous-menu «Afficher comme».

On peut aussi forcer une sortie à avoir une valeur autre que sa valeur normale, par exemple dans cet enchaînement d'additionneurs, où {logicref}`faultyadder.faulty|la sortie de retenue (_carry out_) du deuxième additionneur` a été «bloquée» à 0 ([lien](https://logic.modulo-info.ch/?mode=full&data=N4KABGBEBukFxgEwBpxQJYDt5gNpomEgAcB7AZx1wEYAGW5MAFloF1HJSAndAU0wAuOSJQ7oAJjgDMHTAEMAtr2EBBKZA7Q5AGxzUAvqgiESFKonqMW7KNz6DhojJIQMo8pasQaoW3a8MCMCIySgRcKUtmNg47fiEEER9ICT1ZRWVElWpkvz1A42DTMLwWN2tYnnjHZNSEFHcM1VpcnXyjYxCzcOoWRmoADhjbKodEpxSXMGoAVnTPRIAhdU02gI6TUPM+6aGbTlGEqAm66aZ5zKhF71X-MFoCzuKqKR3B4YP7I6SxKeoZRoLK45W44B4bIpbcJMN57SpfGq-PQNSAeS6QRYtUEIAxodhoTgAVyO+EKXRKEXKMw+cTGx1qUykAHYLsIAGqQR6bbp4agWKzU-a074nRkANlZiQAyuouZCebhEPzmIL4dVxgzpANJVApd45eSXsqmKqRgiNUiEFIAJw6yBSnIG57Q42mz7q+mW6J2qUtJ0CACexHRmHQACMw9plBwoXgZpF+vR9qdcOcwHMwBKwEz9mjVJyIURA8HhKGI1HkrHcPG3IgKs4qNqwLbpm5qNRc00lgWgkWgyHw5Ho1AqzXGDaPimmNQrA0mACYZ2gfbOXiOpAAMakBRkTDxCm9yDF9FycTiXhcSsKpjKqQWZPYHpZ6gs3ZC4lUagt+-+-vCU-npeMYKnebigQ+5gzkgDSIFI74knWjBEKciAZpAABm3AbpcDysL+JaJABF5XhSSpgfeYiPngiBZogr6IAM8HmC2kR4YWR5-oRZ7EcBFJ8uRk5UREUF3uOcGxB+4SvOOMx4WuBIAO7oFwvAHoUNANIxEI0AC1r4upvSJvpxg0Bm7bGRAipWBZvKMLJ2luGKNkRIwObacqsHOahjAMUhkAqehwjoXIhLaIGnLOQmYBSOJQRWdMTnaXy-RuXFUGIB2SUAkqzm1olaVpnRkXjplaUZnezlflYpXqYhzCIF5LbzpFaaLtpUjlal6nSdF+W1SxWlxXVNqVU1bB4iA+hAA)):

```{logic}
:ref: faultyadder
:height: 490
:mode: tryout

{
  "v": 3,
  "in": [
    {"pos": [100, 40], "orient": "s", "id": 3, "name": "A3", "val": 1},
    {"pos": [200, 40], "orient": "s", "id": 0, "name": "A2", "val": 0},
    {"pos": [300, 40], "orient": "s", "id": 1, "name": "A1", "val": 1},
    {"pos": [400, 40], "orient": "s", "id": 2, "name": "A0", "val": 1},
    {"pos": [140, 180], "orient": "s", "id": 15, "name": "B3", "val": 0},
    {"pos": [240, 180], "orient": "s", "id": 14, "name": "B2", "val": 0},
    {"pos": [340, 180], "orient": "s", "id": 13, "name": "B1", "val": 0},
    {"pos": [440, 180], "orient": "s", "id": 12, "name": "B0", "val": 1}
  ],
  "out": [
    {"pos": [30, 450], "orient": "s", "id": 37, "name": "V"},
    {"pos": [120, 450], "orient": "s", "id": 36, "name": "S3"},
    {"pos": [220, 450], "orient": "s", "id": 38, "name": "S2"},
    {"pos": [320, 450], "orient": "s", "id": 39, "name": "S1"},
    {"pos": [420, 450], "orient": "s", "id": 40, "name": "S0"},
    {"type": "nibble", "pos": [530, 100], "id": [4, 5, 6, 7], "name": "A"},
    {"type": "nibble", "pos": [530, 240], "id": [8, 9, 10, 11], "name": "B"},
    {"type": "nibble", "pos": [530, 390], "id": [41, 42, 43, 44], "name": "S"}
  ],
  "components": [
    {"type": "adder", "pos": [420, 320], "in": [16, 17, 18], "out": [19, 20]},
    {"type": "adder", "pos": [320, 320], "in": [21, 22, 23], "out": [24, {"id": 25, "force": 0}]},
    {"type": "adder", "pos": [220, 320], "in": [26, 27, 28], "out": [29, 30]},
    {"type": "adder", "pos": [120, 320], "in": [31, 32, 33], "out": [34, 35]}
  ],
  "wires": [
    [12, 8],
    [13, 9],
    [14, 10],
    [15, 11],
    [2, 4],
    [1, 5],
    [0, 6],
    [3, 7],
    [20, 23],
    [25, 28, {"ref": "faulty"}],
    [30, 33],
    [2, 16],
    [12, 17],
    [1, 21],
    [13, 22],
    [0, 26],
    [14, 27],
    [3, 31],
    [15, 32],
    [19, 41],
    [24, 42],
    [29, 43],
    [34, 44],
    [35, 37],
    [34, 36],
    [29, 38],
    [24, 39],
    [19, 40]
  ]
}
```

Ceci se fait avec un clic droit sur un composant, puis via le sous-menu «Forcer une sortie».


### Tables de vérité

À partir du mode connexion, un _mouseover_ sur une porte affiche sa table de vérité ([lien](https://logic.modulo-info.ch/?mode=full&data=N4KABGBEBukFxgEwBpxQJYDt5gNrEgAcB7AZx1wE4AGZMARmuoF07J0ATHWqaAQwA23AL50CJcgio96AFhZtOOem35CE1UWHFkKNOvQAcCjFwQpegkazSRiAVwAuFHZLwBmRDPmtTOAOzCNhCQAOZ8jgCmbviQjgCehJE4kAAaAPIASu6QbBIUiF4GPorYUu50snQArL52TjgAbEGoIQDu6ABO0RS4PO6+uCpgsoMWtXS4jXT+zMwgwkA)):

```{logic}
:height: 280
:mode: connect

{
  "v": 3,
  "in": [{"pos": [90, 100], "id": 0, "val": 0}, {"pos": [90, 140], "id": 1, "val": 0}, {"pos": [90, 180], "id": 2, "val": 0}],
  "out": [{"pos": [320, 140], "id": 7}],
  "gates": [{"type": "XOR3", "pos": [220, 140], "in": [3, 4, 5], "out": 6}],
  "wires": [[0, 3], [1, 4], [2, 5], [6, 7]]
}
```

D'autres composants montrent d'autres informations sur leur fonction ou leur état interne.

Ceci est désactivable en cochant «Désactiver les tooltips» dans les réglages du circuit (voir figure ci-dessus).


### Autres fonctions en vrac

  * Les cellules mémoires (verrous, bascules, registres, compteur, RAM, etc.) peuvent explictement montrer la ou les valeurs qu'elles stockent
  * Dans les circuits contenant des horloges, on peut «mettre pause» et procéder pas à pas dans les transitions d'états
  * Le nom par défaut du fichier téléchargé («circuit») peut être modifié dans les réglages
  * Des données des élèves (par exemple, identifiant ou pseudonyme) peuvent être passées en tant que paramètres (par exemple, en étant automatiquemet remplies via Moodle) et sont exportées dans les fichiers JSON téléchargés
  * _(liste non exhaustive)_



## Composants disponibles

  * **Entrées**
    * 1 bit (commutateur par défaut, transformable en bouton poussoir)
    * 4 bits (_dip switches_)
    * Horloge
    * Aléatoire 1 bit (sur coup d'horloge)
  * **Sorties**
    * 1 bit (standard ou «bande lumineuse»)
    * 4 bits (hexa, décimal signé ou non)
    * 7 bits (ASCII)
    * Afficheur 7 segments, 16 segments
  * **Portes**
    * Portes standard: ET, OU, OU-X, inverseur
    * Portes universelles: NON-ET, NON-OU
    * Portes moins standard: IMPLIQUE, NON-IMPLIQUE
    * Buffer à trois états (1, 0 et haute impédance [Z])
    * 2, 3 ou 4 entrées 
  * **Composants combinatoires**
    * Additionneur complet
    * ALU (addition, soustration, ET, OU)
    * Multiplexeurs (8/4/2 vers 4/2/1)
    * Décodeurs 7 segments, 16 segments, BCD
  * **Composants séquentiels**
    * Verrou SR
    * Bascules: JK, T, D
    * Registre 4 bits
    * RAM de 16 × 4 bits
    * Compteur 4 bits (chaînable)
  * _Pas encore disponible_
    * Registre à décalage, bus, ROM, composants personnalisés


## Inclusion du simulateur sur des pages tierces

Plutôt que de diffuser des liens, on peut vouloir inclure directement des circuits logiques dans des pages tierces (site du cours, forum, questionnaire Moodle, etc.).

Il est possible d'inclure une ou plusieurs occurrences du simulateur ainsi:

 1. Ajouter une référence vers le code JavaScript du simulateur dans la page web: \
 `<script src="https://logic.modulo-info.ch/simulator/lib/bundle.js"></script>`
 2. Insérer dans la page un ou plusieurs éléments de type `<logic-editor></logic-editor>`

Pour faire un sorte qu'un simulateur affiche déjà un circuit donnée, on peut copier-coller le code HTML de partage proposé via le même bouton que décrit ci-dessous pour partager une URL. Les données à l'intérieur du bloc `<script type="application/json">` représentent le circuit au format JSON.

    <div style="width: 100%; height: 180px">
      <logic-editor>
        <script type="application/json">
          {
            "v": 3,
            "in": [
              {"pos": [50, 50], "id": 0, "val": 0},
              {"pos": [60, 130], "id": 1, "val": 0}
            ],
            "out": [
              {"pos": [270, 90], "id": 5}
            ],
            "gates": [
              {"type": "AND", "pos": [170, 90], "in": [2, 3], "out": 4}
            ],
            "wires": [
              [4, 5], [0, 2], [1, 3]
            ]
          }
        </script>
      </logic-editor>
    </div>

Comme pour les URL, on peut rajouter un attribut `showonly` à l'élément `<logic-editor>` pour afficher uniquement certain composants dans la liste de gauche. Exemple:

    <logic-editor showonly="in,out,and,or,xor">...</logic-editor>

Il est possible d'interagir en JavaScript avec une instance d'un simulateur, notamment via les méthodes `save()`, `load()`, `highlight()`, etc. Contactez l'équipe Modulo en cas d'intérêt.

Dans certains environnements, il n'est pas possible d'ajouter de fichiers JavaScript externes. Dans ce cas, il est toujours possible d'inclure le simulateur logique via une `<iframe>`, dont le code HTML est également proposé via le lien de partage.

    <iframe style="width: 100%; height: 180px; border: 0" src="https://logic.modulo-info.ch/?mode=full&data=N4KABGBEBukFxgEwBpxQJYDt5gNrEgAcB7AZx1wFYAGZMGgXTsnQBMdapoBDAGw4C+dAiXIJcANk4BGAMzUmGdgmnMe-BNQFM0kYgFcALhRFkKiAOycAnAuZsclbagiQA5t0MBTMXgKGAT0IvHEgAQQA5ABFIZlEKaSs6W0UWbHEUMFlUg2MEABZnXQB3dAAnHwpcfLpKRVxORHrVLIYGEAEgA"></iframe>
