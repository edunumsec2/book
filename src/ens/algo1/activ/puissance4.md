# Minimax / Puissance 4

---- 

Découvrir l'algorithme minimax en programmant un jeu de puissance 4

Attention : cette activité a comme prérequis que les élèves aient déjà une certaine maitrise de la programmation, en particulier qu'ils soient à l'aise avec l'utilisation des fonctions et les types composés (dictionnaires, listes, tuples, etc.)

----

```{admonition} Caractéristiques
:class: hint

* Nom : Découvrir l'algorithme minimax en programmant un jeu de puissance 4
* Durée : 4 périodes au total: 2 période consécutives pour lancer le projet, éventuellement à finir à la maison. Puis 2 périodes pour la stratégie (algorithme minimax) et pour présenter le résultat. 
* Thème : Algorithmique
* Objectifs d’apprentissage : Découvrir comment on conceptualise et implémente un jeu de stratégie en utilisant la stratégie minimax. Bonus : Découvrir l'utilité des API. 
* Notions fondamentales : `à compléter`
* Approche pédagogique : Une partie conceptualisation en débranché, suivie d'une réalisation sur ordinateur.
* Matériel : Eventuellement un puissance 4.
* Niveau : `à compléter`
* Mots-clés : `à compléter`
* Dynamique (groupe / individuel) : `à compléter`
* Taille du groupe : `à compléter`
```

```{dropdown} **Déroulement**

**Séance 1**

1. {ref}`Mise en situation<puissance4.miseensituation>` (10 mn) au cours de laquelle les élèves se familiarisent avec le jeu du puissance 4.

1. {ref}`Conceptualisation<puissance4.conceptualisation>` (10mn) au cours de laquelle les élèves prennent conscience des éléments nécessaires à la programmation d'un tel jeu, notamment:

1. {ref}`Discussion<puissance4.discussion>` (10 mn) par groupe.

1. {ref}`Synthèse des discussions<puissance4.synthese>` (10 mn) par l'enseignant·e.

1. {ref}`Programmation<puissance4.programmation>`(30 mn) par deux avec le soutien de l'enseignant·e.

1. {ref}`Compétition<puissance4.competition>`(15 mn) durant laquelle l'enseignant·e montre comment deux groupes peuvent faire jouer leur programme l'un contre l'autre. 

**Séance 2**

1. {ref}`Mise en situation<puissance4.miseensituation2>` (5-10 mn), où les équipes peuvent présenter leur stratégie.

1. {ref}`Présentation théorique<puissance4.presentation>`(10 mn) de l'algorithme minimax. 

1. {ref}`Exercices<puissance4.exercices>` (10 mn) d'application de l'algorithme minimax.

1. {ref}`Présentation théorique<puissance4.presentation2>` (5 mn) des différentes manière d'implémenter minimax

1. {ref}`Programmation<puissance4.programmation2>` (30 mn) de l'algorithme minimax.

1. {ref}`Finalisation<puissance4.finalisation>` (15 mn) avec présentation des résultats, éventuellement en faisant jouer les programmes les uns contre les autres. 

```

**Séance 1**

(puissance4.miseensituation)=
## Mise en situation 

*Durée : 10 mn*

Afin de faire rentrer les élèves dans cette activité et de s'assurer que tous les élèves connaissent le jeu du puissance 4, il est proposé de commencer la leçon en faisant jouer les élèves au puissance 4. 

Plusieurs dispositifs sont envisageables. Par exemples, on peut faire jouer deux équipes d'élèves avec un puissance 4 dessiné au tableau. Une autre option est de faire jouer les élèves contre l'enseignant·e, ce qui lui donne un certain contrôle sur la durée de la partie (potentiellement au détriment de son prestige...). Idéalement il faudrait s'assurer que tous les élèves participent à la réflexion, par exemple en faisant désignant à chaque tour l'élève qui va proposer un coup à son équipe qui en discutera. 

Afin de pouvoir désigner sans ambiguïté les position du jeu, il sera utile de numéroter les coordonnées de la matrice du jeu, de façon analogue au langage utiliser (par exemple en commençant à 0

(puissance4.conceptualisation)=
## Conceptualisation

*Durée : 10 mn*

Une fois la partie terminée, l'enseignant·e annonce aux élèves qu'il va falloir programmer un tel jeu de puissance 4. La plupart des élèves n'auront
sans doute aucune idée de comment commencer et le but de cette discussion sera de déterminer quels sont les différents éléments à programmer. En faisant participer les élèves et en les orientant un peu, les éléments suivants devraient émerger:
1. l'affichage du jeu (l'interface)
1. la stratégie de jeu (savoir quel coup jouer)
1. le déroulement du jeu (tour de rôle et déclaration du vainqueur)
1. la représentation de l'état du jeu (comment savoir quelle est l'état ou la situation du jeu)

(puissance4.discussion)=
## Discussion en groupe

*Durée : 10 mn*

Par groupe de deux ou trois élèves, ils doivent discuter et proposer dans cet ordre:
1. Une représentation de l'état du jeu en utilisant les structures de données qu'ils connaissent 
1. Une ébauche de stratégie, c'est à dire comment choisir le prochain coup

Pendant ce temps, l'enseignant·e passe dans les rangs afin de comprendre et d'orienter les propositions des élèves. A la fin, les élèves résument leur proposition sur papier.

(puissance4.synthese)=
## Synthèse des discussions par l'enseignant·e

*Durée : 10 mn*

L'enseignant·e reprend et présente les propositions des élèves pour la représentation de l'état du jeu (sous leur contrôle afin de ne pas dévoyer leur pensée) et les commente en terme de
1. Complétude (toutes les informations nécessaires sont-elles présentes)
1. Accessibilité (est-ce simple d'accéder à toutes ces informations)
1. Concision (combien de place cela prend-il en mémoire)

L'enseignant·e propose ensuite une représentation adéquate, soit une proposée par les élèves, soit une autre représentation.

L'enseignant·e commente ensuite les propositions de stratégie et propose, pour commencer une stratégie toute simple qui consiste à essayer tous les coups possibles. Si un des coups est gagnant, le jouer, sinon en choisir un autre au hasard. 

(puissance4.programmation)=
## Programmation

*Durée : 30 mn*

L'enseignant·e distribue ensuite un canevas de code contenant déjà la partie déroulement et affichage (de manière encapsulée) et les élèves doivent coder,
par groupe ou individuellement la représentation du jeu, les fonctions d'initialisation, d'accès, et de modification de l'état du jeu. Les API sont déjà
définies par l'enseignant·e.

Les élèves doivent ensuite coder la fonction de stratégie, ce qui leur permettra de tester le jeu. Iels se rendront vite compte de la faiblesse de la stratégie. L'étape suivante consiste à améliorer la stratégie, en excluant les coups qui permettent à l'adversaire de gagner en utilisant testant toutes ses possibilité. Il est ensuite possible d'améliorer la stratégie en regardant un coup en avance, puis deux, puis trois, etc. L'enseignant·e tentera d'orienter les élèves afin de
leur faire découvrir par eux-même la stratégie du minimax. 

(puissance4.competition)=
## Compétition

*Durée : 15 mn*

L'enseignant·e montre comment deux groupes peuvent faire jouer leur programme l'un contre l'autre à l'aide d'un programme ad-hoc utilisant les API. 

Les groupes qui le veulent peuvent se confronter les uns les autres et continuer à développer leur stratégie. Ils peuvent avancer/finir à la maison. 

**Séance 2**

```{admonition} Remarque
Les plus rapides auront déjà eu le temps d'implémenter une stratégie, alors que les plus lent-e-s n'auront que la stratégie de base
```

(puissance4.miseensituation2)=
## Mise en situation

*Durée : 5-10 mn*

Certaines équipes peuvent venir présenter leur jeu et parler de leur stratégie. 

(puissance4.presentation)=
## Présentation théorique

*Durée : 10 mn*

L'enseignant·e récapitule pour tout le monde la stratégie du minimax, en indiquant qu'elle peut aussi être utilisée avec une fonction d'évaluation à plus de trois états comme ici (perdu, gagné, non-décidé). 

Eventuellement, l'enseignant·e peut aussi présenter la stratégie du alpha-beta pruning. 

(puissance4.exercices)=
## Exercices

*Durée : 10 mn*

Les élèves font individuellement sur papier un exercice d'application de la stratégie minimax, suivi immédiatement d'une correction en commun. 

(puissance4.presentation2)=
## Présentation théorique

*Durée : 5 mn*

L'enseignant·e parle des différentes manière d'implémenter minimax (in place, en copie, éventuellement en récursion si cela a déjà été abordé). 

(puissance4.programmation2)=
## Programmation

*Durée : 30 mn*

Les élèves continuent à programmer leur stratégie et peuvent tenter d'implémenter une fonction d'évaluation de l'état du jeu, par exemple en comptant le nombre de rangée ouverte. Optionnellement, en fonction du niveau des élèves, le développement de l'interface graphique peut être considéré. 

(puissance4.finalisation)=
## Finalisation 

*Durée : 15 mn*

Les élèves présentent leur jeu et leur stratégie et on organise un petit tournoi entre les différents programmes. 


