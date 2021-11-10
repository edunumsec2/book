# Découvrir l'algorithme minimax en programmant un jeu de puissance 4.

## Information

Durée: 4 périodes au total: 2 période consécutives pour lancer le projet, éventuellement à finir à la maison. 
Puis 2 périodes pour la stratégie (algorithme minimax) et pour présenter le résultat. 

Mode: Une partie conceptualisation en débranché, suivie d'une réalisation sur ordinateur

Objectif: Découvrir comment on conceptualise et implémente un jeu de stratégie en utilisant la stratégie minimax.
En bonus: Découvrir l'utilité des API. 

Matériel: Eventuellement un puissance 4.

Prérequis: Les élèves ont déjà une certaine maitrise de la programmation, en particulier ils sont à l'aise avec l'utilisation des fonctions et les types composés (dictionnaires, listes, tuples, etc.)


## Déroulement

Cette activité comporte les phases suivante:

Première séance: 
1. Une mise en situation au cours de laquelle les élèves se familiarisent avec le jeu du puissance 4

1. Conceptualisation / discussion au cours de laquelle les élèves prennent conscience des éléments nécessaires à la programmation d'un tel jeu, notamment:

1. Conceptualisation par groupe

1. Présentation des réflexions de chaque groupe

1. Codage par deux avec le soutien de l'enseignant

1. Expérimentation des stratégies

Seconde séance:

1. Mini présentation des stratégies utilisées

1. Présentation de l'algorithme minimax

1. Exercices d'application de l'algorithme minimax

1. Codage de l'algorithme minimax

1. Présentation des résultats, éventuellement en faisant jouer les programmes les uns contre les autres. 

## Séance 1

## Mise en situation (10 min.)
Afin de faire rentrer les élèves dans cette activité et de s'assurer que tous les élèves connaissent le jeu du puissance 4, il est proposé de commencer la leçon en faisant jouer les élèves au puissance 4. 

Plusieurs dispositifs sont envisageables. Par exemples, on peut faire jouer deux équipes d'élèves avec un puissance 4 dessiné au tableau. Une autre option est de faire jouer les élèves contre l'enseignant-e, ce qui lui donne un certain contrôle sur la durée de la partie (potentiellement au détriment de son prestige...). Idéalement il faudrait s'assurer que tous les élèves participent à la réflexion, par exemple en faisant désignant à chaque tour l'élève qui va proposer un coup à son équipe qui en discutera. 

Afin de pouvoir désigner sans ambiguïté les position du jeu, il sera utile de numéroter les coordonnées de la matrice du jeu, de façon analogue au langage utiliser (par exemple en commençant à 0

## Discussion générale / conceptualisation (10 min.)
Une fois la partie terminée, l'enseignant-e annonce aux élèves qu'il va falloir programmer un tel jeu de puissance 4. La plupart des élèves n'auront
sans doute aucune idée de comment commencer et le but de cette discussion sera de déterminer quels sont les différents éléments à programmer. En faisant participer les élèves et en les orientant un peu, les éléments suivants devraient émerger:
1. l'affichage du jeu (l'interface)
1. la stratégie de jeu (savoir quel coup jouer)
1. le déroulement du jeu (tour de rôle et déclaration du vainqueur)
1. la représentation de l'état du jeu (comment savoir quelle est l'état ou la situation du jeu)

## Discussion en groupe (10 min.)

Par groupe de deux ou trois élèves, ils doivent discuter et proposer dans cet ordre:
1. Une représentation de l'état du jeu en utilisant les structures de données qu'ils connaissent 
1. Une ébauche de stratégie, c'est à dire comment choisir le prochain coup

Pendant ce temps, l'enseignant-e passe dans les rangs afin de comprendre et d'orienter les propositions des élèves. A la fin, les élèves résument leur proposition sur papier.

## Synthèse des discussions par l'enseignant-e (10 min.)
L'enseignant-e reprend et présente les propositions des élèves pour la représentation de l'état du jeu (sous leur contrôle afin de ne pas dévoyer leur pensée) et les commente en terme de
1. Complétude (toutes les informations nécessaires sont-elles présentes)
1. Accessibilité (est-ce simple d'accéder à toutes ces informations)
1. Concision (combien de place cela prend-il en mémoire)

L'enseignant-e propose ensuite une représentation adéquate, soit une proposée par les élèves, soit une autre représentation.

L'enseignant commente ensuite les propositions de stratégie et propose, pour commencer une stratégie toute simple qui consiste à essayer tous les coups possibles. Si un des coups est gagnant, le jouer, sinon en choisir un autre au hasard. 

## Programmation (30 min)
L'enseignant distribue ensuite un canevas de code contenant déjà la partie déroulement et affichage (de manière encapsulée) et les élèves doivent coder,
par groupe ou individuellement la représentation du jeu, les fonctions d'initialisation, d'accès, et de modification de l'état du jeu. Les API sont déjà
définies par l'enseignant.

Les élèves doivent ensuite coder la fonction de stratégie, ce qui leur permettra de tester le jeu. Iels se rendront vite compte de la faiblesse de la stratégie. L'étape suivante consiste à améliorer la stratégie, en excluant les coups qui permettent à l'adversaire de gagner en utilisant testant toutes ses possibilité. Il est ensuite possible d'améliorer la stratégie en regardant un coup en avance, puis deux, puis trois, etc. L'enseignant tentera d'orienter les élèves afin de
leur faire découvrir par eux-même la stratégie du minimax. 


## Compétition (5 min)

L'enseignant montre comment deux groupes peuvent faire jouer leur programme l'un contre l'autre à l'aide d'un programme ad-hoc utilisant les API. 

## Stratégies (10 min)
Les groupes qui le veulent peuvent se confronter les uns les autres et continuer à développer leur stratégie. Ils peuvent avancer/finir à la maison. 

## Séance 2
(les plus rapides auront déjà eu le temps d'implémenter une stratégie, alors que les plus lent-e-s n'auront que la stratégie de base)

## Mise en situation (5-10 minutes)

Certaines équipes peuvent venir présenter leur jeu et parler de leur stratégie. 

## Présentation théorique (10 minutes)
L'enseignant-e récapitule pour tout le monde la stratégie du minimax, en indiquant qu'elle peut aussi être utilisée avec une fonction d'évaluation à plus de trois états comme ici (perdu, gagné, non-décidé). 

Eventuellement, l'enseignant peut aussi présenter la stratégie du alpha-beta pruning. 

## Exercice (10 min)

Les élèves font individuellement sur papier un exercice d'application de la stratégie minimax, suivi immédiatement d'une correction en commun. 

## Présentation théorique(5 min.)
L'enseignant parle des différentes manière d'implémenter minimax (in place, en copie, éventuellement en récursion si cela a déjà été abordé). 


## Programmation (30 min)
Les élèves continuent à programmer leur stratégie et peuvent tenter d'implémenter une fonction d'évaluation de l'état du jeu, par exemple en comptant le nombre de rangée ouverte. Optionnellement, en fonction du niveau des élèves, le développement de l'interface graphique peut être considéré. 

## Finalisation (15 minutes)
Les élèves présentent leur jeu et leur stratégie et on organise un petit tournoi entre les différents programmes. 


