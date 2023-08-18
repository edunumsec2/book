# Modéliser une épidémie

```{toctree}
:maxdepth: 2
:hidden:
Marche à suivre <m_a_s>
Corrigé <solution>
```

----

Une activité consistant à adopter, de manière guidée et collaborative une démarche de modélisation, en l'occurence la propagation d'une épidémie.


```{admonition} Modéliser une épidémie
:class: hint
* Thème : Algorithmique et programmation (lors du dernier chapitre d'*Algorithmique I*)
* Niveau : `moyen`
* Durée : 2 période ou 90 minutes
* Objectifs pédagogiques : Comprendre la démarche de modélisation d'un phénomène naturel
* Modalité : `branché`
* Matériel : aucun
* Prérequis : bases de la programmation
* Dynamique (groupe / individuel) : activité coopérative
* Notions fondamentales: modélisation, modèle SIR,  
```

## Préambule
Cette activité consiste à modéliser la propagation d'une épidémie dans une population dans le but de prévoir son évolution et les effets potentiels de mesures sanitaires. C'est l'occasion d'introduire les élèves à la modélisation et à la simulation. Le but est de guider les élèves vers une démarche de modélisation en se basant sur leurs propres idées. 

Là où cela peut être un peu déroutant pour les élèves, c'est qu'on fait quelque chose qui ressemble à des calculs (et donc des mathématiques), mais il n'y a pas de juste ou faux, mais des modèles qui représentent plus ou moins bien la réalité d'un phénomène. L'objectif de cette activité est de faire réfléchir les élèves sur ce phénomène et les orienter vers une modélisation possible. On peut ensuite réfléchir sur ce qui fait la cohérence, la force ou la faiblessse d'un modèle et effectuer une analyse critique de ce modèle. C'est pourquoi il est préférable de modéliser un phénomène familier afin de pouvoir plus facilement le comparer à son modèle. 


Le modèle proposé se base sur le modèle SIR classique (Kermack & McKendrick, 1927)[lien wikipedia](https://fr.wikipedia.org/wiki/Mod%C3%A8les_compartimentaux_en_%C3%A9pid%C3%A9miologie). Une des difficultés auxquelles il faut faire attention est que la méthode proposée repose implicitement sur une ODE intégrée numériquement avec la méthode d'Euler ce qui peut poser des problèmes de précision et de stabilité qu'il faudra autant que possible "cacher" aux élèves. Cela vaut donc la peine se faire quelques essais à l'avance pour s'assurer qu'on est bien en zone stable avec les paramètres choisis.

Cette activité peut être effectuée dans une éditeur python ou sur un jupyter-notebook. L'avantage du notebook est que les élèves ont tout dans un seul fichier (consignes, codes, graphes, réponses aux questions), le désavantage est qu'il faut une infrastructure informatique plus importante pour faire tourner le code à la maison (jupyter-lab).



## Déroulement 
|			Etape			| Durée | Phase |
|-----------------------------------------------| ------|-------|
|{ref}`Mise en situation<epidemie.misenensituation>`  autour de l'évènement historique de la fermeture des écoles le 13 mars 2020.| 5 min | mise en situation |
| {ref}`Conception du modèle<epidemie.conception>` par groupe de deux ou trois, pendant que l'enseignant passe dans les rangs pour orienter le travail.| 15 min | exploration| 
| {ref}`Évaluation<epidemie.evaluation>` durant laquelle chaque groupe fait un commentaire sur le modèle d'un autre groupe. | 5 min | évaluation| 
| {ref}`Présentation des modèles<epidemie.presentation>`  devant le reste de la classe, et discussions des modèles. |15 min| objectivation |
| {ref}`Gestion des contraintes<epidemie.contraintes>` durant laquelle les étudiant·e·s choisissent un modèle et avancent dans la marche à suivre. | 5 min | Application |
| {ref}`Discussion<epidemie.discussion>`  où les groupes ayant des résultats négatifs viennent expliquer devant la classe pourquoi ils obtiennent ces chiffres et comment l'éviter.|10 min| Discussion|
| {ref}`Visualisation<epidemie.visualisation>` des graphes de courbes épidémiologiques.|15 min| Application |
| {ref}`Recherche des paramètres<epidemie.recherche>`  où les groupes essaient "à la main" de reproduire des courbes semblables à l'une ou à l'autre vague et les affichent en superposition| 15 min | exploration |
| {ref}`Présentation et discussion des résultats<epidemie.resultats>`| 10 min | objectivation/discussion|



(epidemie.misenensituation)=
## Mise en situation

*Durée : 5 mn* 

L'enseignant·e demande aux élèves qui se souvient de l'annonce de la fermeture des écoles le 13 mars 2020. 
Au début de la pandémie de coronavirus, diverses prédictions sur la durée et la gravité de cette épidémie ont alors été publiées. Ces prédictions étaient basées sur des *modèles* faits par des épidémiologistes. Diverses prédictions d'alors peuvent être présentées. 
Le but de la leçon sera de faire et analyser un modèle de propagation d'une épidémie. 

(epidemie.conception)=
## Conception du modèle

*Durée : 15 mn*

Par groupe de deux ou trois, les élèves font les points 1 à 4 de la {ref}`marche à suivre<m_a_s>`, pendant que l'enseignant passe dans les groupes pour les orienter. L'enseignant choisit parmi les modèles des élèves ceux qui sont intéressants à discuter.

(epidemie.evaluation)=
## Évaluation

*Durée : 5 mn*

Chaque groupe fait un commentaire sur le modèle d'un autre groupe, c'est-à-dire si le modèle lui semble logique. Les groupes peuvent adapter leur modèle en fonction. 

(epidemie.presentation)=
## Présentation des modèles

*Durée : 15 mn*

Les groupes sélectionnés par l'enseignant·e présentent leur modèle et la classe les discutent. L'enseignant·e peut présenter le modèle standard (cf corrigé), s'il n'a pas été présenté par un groupe. Pour chaque modèle, l'enseigant·e met en avant les hypothèses principales induites par le modèle, par exemple,
- Brassage homogène de la population
- Population en vase clos, absence d'immigration ou d'émigration
- Absence de période d'incubation
- Absence de réinfection
- Population non structurée (en âge, sexe, etc.) avec des caractèristiques épidémiologiques homogènes. 

(epidemie.contraintes)=
## Gestion des contraintes

*Durée : 5 min*

Les groupes choisissent un modèle validé par l'enseignant·e et font la partie 5 de la {ref}`marche à suivre<m_a_s>` (déroulé sur plusieurs jours). Certains groupes risquent de tomber sur des chiffres négatifs. 

(epidemie.discussion)=
## Discussion

*Durée : 10 min*

Ceux qui ont des chiffres négatifs viennent présenter leur modèles et la classe essaie de déterminer pourquoi ils obtiennent ceci et comment l'éviter (avec l'aide de l'enseignant·e).

(epidemie.visualisation)=
## Visualisation

*Durée : 15 min*

Les groupes produisent des graphes de leur courbe épidémiologique, parties 6 à 11 de la {ref}`marche à suivre<m_a_s>`.

(epidemie.recherche)=
## Recherche des paramètres

*Durée : 15 min*

Les élèves téléchargent les données réelles et les affichent dans un graphique.
Les données pour la suisse sont disponibles sur le site github de [Daniel Probst](https://github.com/daenuprobst/covid19-cases-switzerland). Il est conseillé d'extraire au préalable les données pour le canton de Vaud (p. ex.) de
de fournir un fichier csv déjà bien formaté aux élèves, comme {download}`ici<./data/covid_vd.csv>`.

Les groupes essaient "à la main" de reproduire des courbes semblables à l'une ou à l'autre vague et les affichent en superposition (partie 12 de la {ref}`marche à suivre<m_a_s>`).

(epidemie.resultats)=
## Présentation et discussion des résultats

*Durée : 10 min*

Les groupe viennent présenter leur courbes et la classe discute des limites du modèle, des effets des mesures sanitaires, fiabilité des chiffres, etc. 




