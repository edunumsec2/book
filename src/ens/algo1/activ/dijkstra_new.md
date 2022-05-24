# L'algorithme du plus court chemin de Dijkstra

------

Activité collaborative et débranchée pour introduire l'algorithme du plus court de chemin de Dijkstra.

------

```{admonition} Caractéristiques
:class: hint

* Nom : L'algorithme du plus court chemin de Dijkstra
* Durée : 2 périodes
* Thème : Algorithmique
* Objectifs d’apprentissage : Découvrir l'algorithme de Dijkstra, son utilité, son fonctionnement
* Notions fondamentales : `à compléter`
* Approche pédagogique : Débranché
* Matériel : `à compléter`
* Niveau : `à compléter`
* Mots-clés : `à compléter`
* Dynamique (groupe / individuel) : `à compléter`
* Taille du groupe : `à compléter`
```

```{dropdown} **Déroulement**
1. **Mise en situation générale** (5 mn) pour comprendre un contexte de la vie quotidienne dans lequel cet algorithme est utilisé et qui constituera un fil rouge concret tout au long de l'activité.  

1. **Mise en situation spécifique** (15 mn) pour passer à un niveau d'abstraction et de généralisation plus élévé. 

1. **Identification du problème** (5 mn), identification de l'objectif, explication de la non-trivialité du problème.

1. **Découverte** (15 mn) par essais-erreurs de l'algorithme et de sa justification par simulation humaine.

1. **Formalisation** (10 mn) de l'algorithme.

1. **Exemples d'utilisation** (15 mn) de l'algorithme et exercices.

1. **Réflexions** plus approfondie sur l'algorithme *pour aller plus loin*.
```

## Mise en situation générale

*Durée : 5 mn*

L'enseignant va sur une page de navigation (p.ex [OpenStreetMap](https://www.openstreetmap.org/#map=8/46.825/8.224)) et montre un exemple de requête de chemin pour relier deux points.


````{tabbed} Questions
* Comment le site web a-t-il déterminé le chemin qu'il nous indique ?
* Quelles données a-t-il à sa disposition pour déterminer ce chemin ? 
````
````{tabbed} Réponses
* Tout le réseau routier est représenté sous forme d'un graphe.
* Les croisements et embranchements sont représentés par les *sommets* du graphe et les routes qui les relient sont représentées par les *arêtes* du graphe.
````

## Mise en situation spécifique

*Durée : 15 mn*

```{tabbed} Exemple 1
L'enseignant distribue à chaque élève un graphe suffisamment compliqué dans lequels la longueur des
arêtes est indiquée. Ils doivent trouver, individuellement, le plus court chemin reliant deux points.
Le graphe est tel qu'il y a plusieurs plus courts chemins. 

![graphe 1](media/graph1.png)

**Mise en commun**

* Qui a trouvé le plus court chemin ?
* Etes-vous sûr qu'il s'agit du plus court chemin? Le cas échéant, comment le savez-vous ?
* Chacun donne son plus court chemin. 
* Y a-t-il des chemins plus courts que ça ?
```
```{tabbed} Exemple 2

Dans un voyage en voiture, on ne veut pas forcément le plus court chemin, mais souvent le plus rapide.

Par exemple, on va prendre l'autoroute de contournement de Lausanne qui est plus longue, mais plus rapide que
de traverser la ville.

On retrouve le même graphe qu'avant, mais cette fois on a le temps de parcours entre chaque point qui est indiqué et on ne peut plus se baser sur les aspects géométriques pour trouver le plus courts chemin.

![graphe 2](media/graph2.png)

**Mise en commun**

* Qui a trouvé le plus court chemin ?
* Etes-vous sûr qu'il s'agit du plus court chemin? Le cas échéant, comment le savez-vous ?
* Chacun-e donne son plus court chemin. 
* Y a-t-il des chemins plus courts que ça ?
* Que faut-il faire pour être sûr-e que ce soit vraiment le plus court ?
```

## Identification du problème

*Durée : 5 mn*

Le problème est donc donné sous forme d'un graphe constitué de *sommets* reliés par des *arêtes* qui ont une certaine *longueur*. Dans le cas ci-desssus, les sommets représentent des villes, les arêtes les routes, et les longueurs la durée du trajet. La *longueur totale* est donnée par la somme des longueurs des arêtes empruntée.

## Découverte 

*Durée : 15 mn*

````{panels}
:column: col-lg
🎲 Activité
^^^
Pour déterminer le plus court chemin dans ce graphe, la classe va le faire tous ensemble. Chaque élève représente un sommet et reçoit le sous-graphe constitué de son sommet et ses voisins directs (autrement dit une liste de ses voisins et les distances correspondantes). Chaque élève prend en outre une feuille avec un
crayon et une gomme.
```{dropdown} Déroulement

L'enseignant délimite la classe en trois zones:
1. La <span style="color:red">**zone A**</span>, contenant les sommets qui ont trouvé la longueur du chemin le plus court depuis le sommet de départ.
1. La <span style="color:green">**zone B**</span>, contenant les sommets qui ont trouvé une longueur de chemin depuis le sommet de départ, mais pas forcément la plus petite.
1. La <span style="color:black">**zone C**</span>, contenant les sommets qui n'ont pas trouvé de longueur depuis le sommet de départ.

Les instructions pour les élèves sont les suivantes:
1. Les élèves commencent tous dans la <span style="color:black ">**zone C**</span>.
1. Lorsqu'un·e élève se rend compte qu'elle peut calculer la longueur d'un chemin depuis le sommet de départ, elle écrit sur sa feuille par quel voisin ce chemin passe ainsi que la distance correspondante, et se place dans la <span style="color:green">**zone B**</span>.
1. Les élèves de la <span style="color:green">**zone B**</span> peuvent se voir mutuellement leur feuille
1. Lorsqu'un·e élève de la <span style="color:green">**zone B**</span> se rend compte qu'il existe un chemin plus court que la longueur indiquée sur sa feuille, elle met sa feuille à jour. 
1. Lorsqu'un·e élève se rend compte que le chemin indiqué sur sa feuille est le plus court, elle passe dans la <span style="color:red">**zone A**</span>.
1. Dans la <span style="color:red">**zone A**</span>, toutes les feuilles sont clairement visibles. 

Si tout se passe bien, les élèves vont se déplacer dans les **<span style="color:green">zones B</span> et <span style="color:red ">C</span>** en commençant par le sommet de départ. Idéalement, elles doivent se rendre compte des principes de base de l'alogrithme de Dijkstra:

1. Si un de leur voisin direct a trouvé une longueur de chemin, il ont également une longueur de chemin en ajoutant la distance qui les sépare.
1. Si un·e élève a le chemin de plus court de la <span style="color:green">**zone B**</span> et que personne ne s'y ajoute (i.e. tous les voisin des personnes dans la <span style="color:red">**zone A**</span> sont soit dans la <span style="color:red">**zone A**</span> soit dans la <span style="color:green">**zone B**</span>), elle peut passer en <span style="color:red">**zone A**</span>.
1. A la fin, en suivant les relations de voisinage, on peut reconstituer le chemin le plus court. 
```
````

```{admonition} Attention
:class: caution
Cette activité implémente dans les faits une version distribuée de l'algorithme où les sommets peuvent changer de zone en parallèle. Il est conseillé de bien marquer la transition à l'algorithme séquentiel.
```

## Formalisation

*Durée : 10 mn*

L'enseignant formalise l'algorithme au tableau avec l'aide des élèves. Pour aider à la compréhension et à la représentation, il peut utiliser des couleurs pour dénommer les zones et ainsi pouvoir changer les sommets de zone en modifiant la couleur (ou en utilisant un autre moyen graphique). Ici la **zone A** est "rouge", la **zone B** est "verte" et la **zone C** est "blanche" (non marquée). 


```{dropdown} Formalisation
1. Mettre le <span style="color:black ">sommet de départ (S)</span> en rouge, sa distance au sommet de départ est 0. 
1. Mettre en vert tous les <span style="color:green">sommets voisins de ce sommet (S)</span> qui sont en blanc et indiquer en vert leur <span style="color:green">distance au sommet de départ</span> en passant par ce sommet S et indiquer le chemin à ce sommet S par une <span style="color:green">flèche verte</span>.
1. Vérifier tous les <span style="color:green">voisins de ce sommet (S)</span> qui sont en vert si leur <span style="color:black">distance au sommet de départ est plus petite en passant par ce sommet</span>. Si c'est le cas ajuster leur distance au sommet de départ et leur flèche pour qu'elle pointe vers le sommet S.
1. Prendre le <span style="color:green">sommet vert</span> avec la plus petite distance au sommet de départ et le <span style="color:red ">mettre en rouge</span> avec sa distance et sa flèche. Ce sommet est le nouveau sommet S.
1. Si ce sommet S est le sommet d'arrivée, le plus court chemin est obtenu en suivant les flèches, sinon retourner au point 2.

![step123](media/steps.gif)
```

## Exemples d'utilisation 

*Durée : 15 mn*

L'enseignant fait un exemple au tableau avec les élèves et leur propose ensuite d'essayer seuls ou par deux sur des graphes donnés. 

```{tabbed} Jeu : de VERSE à LITRE
Ce jeu consiste à trouver une manière de relier deux mots ayant le même nombre de lettres (par exemple VERSE et LITRE) avec une série de mots existants dont chaque mot ne diffère du précédent que d'une seule lettre. Dans notre exemple, une solution est donnée par :

VERSE - VERRE - SERRE - SEVRE - LEVRE - LIVRE - LITRE

On suppose disposer d'une liste de tous les mots de la langue française. 

Comment l'algorithme du plus cours chemin peut-il être utilisé pour trouver une solution à ce jeu ? En particulier,
quel graphe serait-il nécessaire de construire, à quoi correspondrait ses nœuds et ses arêtes et ses distances ?

Selon le niveau atteint en programmation, une petite application proposant ce jeu et les solutions correspondantes pourrait être
programmée par exemple en utilisant une libraire de graphe telle que igraph ou networkX en python.
```
```{tabbed} Réseautage

L'autre jour, vous avez flashé sur quelqu'un que vous ne connaissez pas mais dont vous avez réussi à obtenir
le nom. Après avoir passé beaucoup de temps sur son profil dans votre réseau social préféré, vous recevez
une notification vous indiquant quel ami-e pourra sans doute vous aider à vous rapprocher de cette personne.
Comme ce réseau social a-t-il pu utiliser l'algorithme de Dijkstra pour vous faire cette recommandation?
```

