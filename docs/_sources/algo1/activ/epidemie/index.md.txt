# Modéliser une épidémie

```{toctree}
:maxdepth: 2
:hidden:
Marche à suivre <fiche>
Corrigé <solution>
Modéliser une épidémie <epidemie/index>
```

Cette activité consiste à modéliser la propagation d'une épidémie dans une population dans le but de prévoir son évolution et les effets potentiels de mesures sanitaires. C'est l'occasion d'introduire les élèves à la modélisation et à la simulation. Le but est de guider les élèves vers une démarche de modélisation en se basant sur leurs propres idées. 

Là où cela peut être un peu déroutant pour les élèves, c'est qu'on fait quelque chose qui ressemble à des calculs (et donc des mathématiques), mais il n'y a pas de juste ou faux, mais des modèles qui représentent plus ou moins bien la réalité d'un phénomène. L'objectif de cette activité est de faire réfléchir les élèves sur ce phénomène et les orienter vers une modélisation possible. On peut ensuite réfléchir sur ce qui fait la cohérence, la force ou la faiblessse d'un modèle et effectuer une analyse critique de ce modèle. C'est pourquoi il est préférable de modéliser un phénomène familier afin de pouvoir plus facilement le comparer à son modèle. 


Le modèle proposé se base sur le modèle SIR classique (Kermack & McKendrick, 1927)[lien wikipedia](https://fr.wikipedia.org/wiki/Mod%C3%A8les_compartimentaux_en_%C3%A9pid%C3%A9miologie). Une des difficultés auxquelles il faut faire attention est que la méthode proposée repose implicitement sur une ODE intégrée numériquement avec la méthode d'Euler ce qui peut poser des problèmes de précision et de stabilité qu'il faudra autant que possible "cacher" aux élèves. Cela vaut donc la peine se faire quelques essais à l'avance pour s'assurer qu'on est bien en zone stable avec les paramètre choisis.

Cette activité peut être effectuée dans une éditeur python ou sur un jupyter-notebook. L'avantage du notebook est que les élèves ont tout dans un seul fichier (consignes, codes, graphes, réponses aux questions), le désavantage est qu'il faut une infrastructure informatique plus importante pour faire tourner le code à la maison (jupyter-lab).


## Mise en situation (5 min)
L'enseignant·e demande aux élèves qui se souvient de l'annonce de la fermeture des écoles le 13 mars 2020. 
Au début de la pandémie de coronavirus, diverses prédictions sur la durée et la gravité de cette épidémie ont alors été publiées. Ces prédictions étaient basées sur des *modèles* faits par des épidémiologistes. Diverses prédictions d'alors peuvent être présentées. 
Le but de la leçon sera de faire et analyser un modèle de propagation d'une épidémie. 

## Conception du modèle (15 min)
Par groupe de deux, les élèves font les points 1 à 4 de la fiche, pendant que l'enseignant passe dans les groupes pour les orienter. L'enseignant choisi parmi les modèles des élèves ceux qui sont intéressants à discuter.

## Eventuellement: évaluation (5 min)
Chaque groupe fait un commentaire sur le modèle d'un autre groupe, c'est-à-dire si le modèle lui semble logique. Les groupes peuvent adapter leur modèle en fonction. 

## Présentation des modèles (15 min)
Les groupes sélectionnés par l'enseignant·e présentent leur modèle et la classe les discutent. L'enseignant·e peut présenter le modèle standard (cf corrigé), s'il n'a pas été présenté par un groupe. Pour chaque modèle, l'enseigant·e met en avant les hypothèses principales induites par le modèle, par exemple,
- Brassage homogène de la population
- Population en vase clos, absence d'immigration ou d'émigration
- Absence de période d'incubation
- Absence de réinfection
- Population non structurée (en âge, sexe, etc.) avec des caractèristiques épidémiologiques homogènes. 



## Gestion des contraintes (5 min)
Les groupes choisissent un modèle validé par l'enseignant·e et font la partie 5 (déroulé sur plusieurs jours). Certains groupes risquent de tomber sur des chiffres négatifs. 

## Discussion (10 min)
Ceux qui ont des chiffres négatifs viennent présenter leur modèles et la classe essaie de déterminer pourquoi ils obtiennent ceci et comment l'éviter (avec l'aide de l'enseignant·e).

## Visualisation (15 min)
Les groupes produisent des graphes de leur courbe épidémiologique (parties 6-11).

## Recherche des paramètres (15 min)
Les élèves téléchargent les données réelles et les affichent dans un graphique.
Les données pour la suisse sont disponibles sur le site github de [Daniel Probst] (https://github.com/daenuprobst/covid19-cases-switzerland). Il est conseillé d'extraire au préalable les données pour le canton de Vaud (p. ex.) de
de fournir un fichier csv déjà bien formaté aux élèves, comme [ici](./covid_vd.csv).

Les groupes essaient "à la main" de reproduire des courbes semblables à l'une ou à l'autre vague et les affichent en superposition (partie 12).

## Présentation et discussion des résultats (10 min)
Les groupe viennt présenter leur courbes et la classe discute des limites du modèle, des effets des mesures sanitaires, fiabilité des chiffres, etc. 




