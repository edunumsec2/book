# L'algorithme du plus court chemin de Dijkstra

## Informations

Durée: 2 périodes consécutives avec une suite optionnelle qui porte sur les enjeux de société.

Mode: Débranché

Chapitre: Algorithmique

Objectifs: Découvrir l'algorithme de Dijkstra, à quoi il sert, et pourquoi il fonctionne.  

Matériel: Une connection internet pour la mise en situation. 

## Introduction

Ceci est une activité collaborative et débranchée pour introduire l'algorithme
du plus court de chemin de Dijkstra.


## Déroulement

Cette activité comporte sept phases:

1. Une mise en situation générale pour comprendre un contexte de la vie quotidienne dans lequel cet algorithme
est utilisé et qui constituera un fil rouge concret tout au long de l'activité.  

1. Une mise en situation plus spécifique pour passer à un niveau d'abstraction et de généralisation plus élévé. 

1. Une phase pour formaliser le problème, mieux en cerner l'objectif, et comprendre pourquoi il n'est pas trivial.

1. Une phase de découverte (potentiellement tâtonnante) de l'algorithme et de sa justification par simulation humaine

1. Une phase de formalisation (et institutionnalisation) de l'algorithme.

1. Une phase d'exercices (ou exemples) d'application de l'algorithme et puis de modélisation

1. Une phase de réflexion plus approfondie sur l'algorithme (pour les plus avancés)


## 1. Mise en situation générale (5 min)

L'enseignant va sur une page de navigation (p.ex OpenStreetMap) et on montre un exemple
de requête de chemin pour relier deux points.

**Questions:**
 - Comment le site web a-t-il déterminé le chemin qu'il nous indique?
 - Quelles données a-t-il à sa disposition pour déterminer ce chemin? 

**Réponses:**
 - Tout le réseau routier est représenté sous forme d'un graphe
 - Les croisements et embranchements sont représentés par les *sommets* du graphe et les
 routes qui les relient sont représentées par les *arêtes* du graphe. La *longueur* de


## 2. Mise en situation spécifique (15 min)

### Exemple 1
L'enseignant distribue à chaque élève un graphe suffisamment compliqué dans lequels la longueur des
arêtes est indiquée. Ils doivent trouver, individuellement, le plus court chemin reliant deux points.
Le graphe est tel qu'il y a plusieurs plus courts chemins. 

![graphe 1](figs/graph1.png)

**Mise en commun:**

- Qui a trouvé le plus court chemin?
- Etes-vous sûr qu'il s'agit du plus court chemin? Le cas échéant, comment le savez-vous?
- Chacun donne son plus court chemin. 
- Y a-t-il des chemins plus courts que ça?

### Exemple 2
Dans un voyage en voiture, on ne veut pas forcément le plus court chemin, mais souvent le plus rapide.
Par exemple, on va prendre l'autoroute de contournement de Lausanne qui est plus longue, mais plus rapide que
de traverser la ville.
On retrouve le même graphe qu'avant, mais cette fois on a le temps de parcours entre chaque point qui est
indiqué et on ne peut plus se baser sur les aspects géométriques pour trouver le plus courts chemin.

![graphe 2](figs/graph2.png)

**Mise en commun:**

- Qui a trouvé le plus court chemin?
- Etes-vous sûr qu'il s'agit du plus court chemin? Le cas échéant, comment le savez-vous?
- Chacun-e donne son plus court chemin. 
- Y a-t-il des chemins plus courts que ça?
- Que faut-il faire pour être sûr-e que ce soit vraiment le plus court? (Essayer tous les chemins?). 


## 3 Formalisation (5 min)

Le problème est donc donnée sous forme d'un graphe constitué de *sommets* reliés par des *arêtes* qui
ont une certaine *longueur*. Dans le cas ci-desssus, les sommets représentent des villes, les arêtes les
routes, et les longueurs la durée du trajet. La *longueur totale* est donnée par la somme des longueurs
des arêtes empruntée.

## 4 Découverte (15 min)

Pour déterminer le plus court chemin dans ce graphe, la classe va le faire tous ensemble. Chaque élèves
représente un sommet et reçoit le sous-graphe constitué de son sommet et ses voisin directs (autrement dit
une liste de ses voisins et les distances correspondantes). Chaque élève prend en outre une feuille avec un
crayon et une gomme.

L'enseignant délimite la classe en trois zones:
1. La zone contenant les sommets qui ont trouvé la longueur du chemin le plus court depuis le sommet de départ.
1. La zone contenant les sommets qui ont trouvé une longueur de chemin depuis le sommet de départ, mais pas forcément la plus petite.
1. La zone contenant les sommets qui n'ont pas trouvé de longueur depuis le sommet de départ.

Les instructions pour les élèves sont les suivantes:
1. Les élèves commencent tous dans la zone 3.
1. Lorsqu'une élève se rend compte qu'elle peut calculer la longueur d'un chemin depuis le sommet de départ, elle écrit sur sa
feuille par quel voisin ce chemin passe ainsi que la distance correspondante, et se place dans la zone 2.
1. Les élèves de la zone 2 peuvent se voir mutuellement leur feuille
1. Lorsqu'une élève de la zone 2 se rend compte qu'il existe un chemin plus court que la longueur indiquée sur sa feuille, elle
met sa feuille à jour. 
1. Lorsqu'une élève se rend compte que le chemin indiqué sur sa feuille est le plus court, elle passe dans la zone 1.
1. Dans la zone 1, toutes les feuilles sont clairement visibles. 

Si tout se passe bien, les élèves vont se déplacer dans les zones 2 et 3 en commençant par le sommet de départ. Idéalement, elles
doivent se rendre compte des principes de base de l'alogrithme de Dijkstra:

1. Si un de leur voisin direct a trouvé une longueur de chemin, il ont également une longueur de chemin en ajoutant la distance qui
les sépare.
1. Si une élève a le chemin de plus court de la zone 2 et que personne ne s'y ajoute (i.e. tous les voisin des personnes dans la zones 1 sont soit dans la zone 1 soit dans la zone 2), elle peut passer en zone 1.
1. A la fin, en suivant les relations de voisinage, on peut reconstituer le chemin le plus court. 

### Remarque
Cette activité implémente dans les faits une version distribuée de l'algorithme où les sommets peuvent changer de zone en parallèle. Il est conseillé de bien marqué la transition à l'algorithme séquentiel.

## 5 Formalisation (10 min)
L'enseignant formalise l'algorithme au tableau avec l'aide des élèves. Pour aider à la compréhension et à la représentation, il peut utiliser des couleurs pour dénommer les zones et ainsi pouvoir changer les sommets de zone en modifiant la couleur (ou en utilisant un autre moyen graphique). Ici la zone 1 est "rouge", la zone 2 est "verte" et la zone 3 est "blanche" (non marquée). La formalisation se fait en français de manière à rendre la compréhension la plus intuitive possible, par exemple ainsi:

1. Mettre le sommet de départ (S) en rouge, sa distance au sommet de départ est 0. 
1. Mettre en vert tous les sommets voisins de ce sommet S qui sont en blanc et indiquer en vert leur distance au sommet de départ en passant par ce sommet S et indiquer le chemin à ce sommet S par une flèche verte.
1. Vérifier tous les voisins de ce sommet (S) qui sont en vert si leur distance au sommet de départ est plus petite en passant par ce sommet. Si c'est le cas ajuster leur distance au sommet de départ et leur flèche pour qu'elle pointe vers le sommet S.
1. Prendre le sommet vert avec la plus petite distance au sommet de départ et le mettre en rouge avec sa distance et sa flèche. Ce sommet est le nouveau sommet S.
1. Si ce sommet S est le sommet d'arrivée, le plus court chemin est obtenu en suivant les flèches, sinon retourner au point 2.



## 6 Exemples et exercices d'application et de modélisation (15 min)

L'enseignant fait un exemple au tableau avec les élèves et leur propose ensuite d'essayer seuls ou par deux sur des graphes donnés. 

### Jeu: De VERSE à LITRE 
Ce jeu consiste à trouver une manière de relier deux mots ayant le même nombre de lettres (par exemple VERSE et LITRE) avec une série
de mots existants dont chaque mot ne diffère du précédent que d'une seule lettre. Dans notre exemple, une solution est donnée par:

VERSE - VERRE - SERRE - SEVRE - LEVRE - LIVRE - LITRE

On suppose disposer d'une liste de tous les mots de la langue française.
Comment l'algorithme du plus cours chemin peut-il être utilisé pour trouver une solution à ce jeu? En particulier,
quel graphe serait-il nécessaire de construire, à quoi correspondrait ses nœuds et ses arêtes et ses distances?

Selon le niveau atteint en programmation, une petite application proposant ce jeu et les solutions correspondantes pourrait être
programmée par exemple en utilisant une libraire de graphe telle que igraph ou networkX en python.

### Réseautage
L'autre jour, vous avez flashé sur quelqu'un que vous ne connaissez pas mais dont vous avez réussi à obtenir
le nom. Après avoir passé beaucoup de temps sur son profil dans votre réseau social préféré, vous recevez
une notification vous indiquant quel ami-e pourra sans doute vous aider à vous rapprocher de cette personne.
Comme ce réseau social a-t-il pu utiliser l'algorithme de Dijkstra pour vous faire cette recommandation?

## 7 Lien avec enjeux sociétaux

### Introduction (5 min)
Retour sur openstreetmap et présentation de l'histoire de la startup Waze, rachetée par Google
https://fr.wikipedia.org/wiki/Waze 

### 2 Travail en groupe(20 min, à finir comme devoir) 
 Par groupe de 3 ou 4, les élèves doivent proposer une application imaginaire qui utiliserai l'algorithme de Dijkstra
pour proposer un service à ses utilisateurs. En particulier, ils doivent préciser les points suivants:
1. Quel service propose l'application
1. Qui ce service pourrait intéressé.
1. Quelles sont les données dont l'application aurait besoin (et comment elle pourrait les obtenir)
1. En quoi la notion de graphe serait utile pour programmer cette application et comment l'algorithme de Dijkstra serait utilisé (donner un exemple concret)
1. Quels impacts positifs ou négatifs peut-on imaginer pour cette application? 

L'enseignant guide les élèves et donnent des idées à ceux qui n'en n'ont pas. 

Les élèves rédigent ensuite un diaporama dans lequel chacun de ces points est abordé par une diapo

### Présentation et discussion(30 min)
Chaque groupe fait une présentation de son projet en 5 minutes suivi d'une petite discussion avec la classe. 
 
