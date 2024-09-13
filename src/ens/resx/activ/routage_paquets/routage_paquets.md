# Routage et paquets sur Internet

```{toctree}
:maxdepth: 2
:hidden:
Exercices <exercices>
```

Le but de cette activité de simulation humaine est de découvrir
les deux éléments centraux de la transmission d'information sur internet
suivants:

1. le principe du routage sur internet, ou comment peut se mettre en place une
procédure décentralisée qui permet de savoir par où acheminer l'information
afin de pouvoir atteindre n'importe quel destinataire du réseau. 
1. le principe de la commutation par paquet, c'est à dire comment l'information
est découpée en petits morceau pour l'envoi et reconstituée à l'arrivée. 

```{admonition} Notice
:class: hint

* **Thème** : eg. `Réseau`, `routage`
* **Niveau** : `facile`
* **Durée** : 2 périodes
* **Objectifs pédagogiques** : Découvrir par la simulation les principes du routage et de la commutation par paquets. 
* **Modalité** : `débranché`
* **Matériel** : scotch de carrossier, billets ou post-its de
trois couleurs différentes, feuille d'exercices
* **Prérequis** : les adresses IP
* **Notions fondamentales** : table de routage, routage, TCP-IP, RIP
* **Taille du groupe** : `demi-classe`  peut-être possible en classe entière mais plus difficile à gérer. 
```

## Déroulement


|                                       | Durée  | Phase de l'activité   | 
|---------------------------------------|------ |---------------------|
| {ref}`Introduction <routage.intro>`| 5 min  | Introduction   |
| {ref}`Les tables de routage <routage.tdr>`| 15 min  | Exercices   |
| {ref}`Simulation de routage <routage.simul>`| 10 min  | Exploration    |
| {ref}`Routage dynamique <routage.dyn>`| 15 min         | Exploration                     |
| {ref}`TCP-IP <routage.tcpip>`| 10 min    | Exploration                 |
| {ref}`Simulation complète (facultatif) <routage.simc>`| 10 min    | Exploration                 |
| {ref}`Récapitulatif <routage.rec>`| 10 min   | Institutionnalisation |


(routage.intro)=
## Introduction
En quelques minutes, l'enseignant-e introduit le sujet du "fonctionnement d'Internet", en interrogeant les élèves
sur leurs préconceptions et en partant d'un exemple concret de consultation d'un site web, d'échange sur un
réseau social, ou d'échange d'email. La discussion doit amener la notion d'étapes intermédiaires (par exemple
l'antenne 4G, la borne wifi) et donc des routeurs. On peut illustrer le propos avec une carte des dorsales d'Internet. 
On indique qu'Internet peut être représenté par un graphe avec nœuds et arêtes. 

(routage.tdr)=
## Les tables de routage

Le but de cette étape est d'amener la notion de table de routage par trois types d' [exercices](exercices). Le premier consiste à
remplir les tables de routage d'un graphe donné, le second à déduire le graphe à partir des tables de routage, et
le troisième à déduire le chemin d'un message en n'ayant uniquement les tables de routage. Pour chaque exercice, le
premier exemple est résolu en commun, et les suivants sont faits individuellement. 

(routage.simul)=
## Simulation de routage
On procède ensuite la simulation d'un réseau. les élèves se disposent autour d'une grande table, ou assis-es de
manière à n'être pas trop éloigné-e-s les uns des autres. Chaque élève est un routeur qui est connecté à environs
trois autre routeurs. Les connections entre routeurs sont indiquées par des bandes de scotch carrossier sur la table
ou par terre. Chaque élève reçoit sur paper une table de routage vide à trois colonnes
(destination, interface, distance) sur laquelle il complète son numéro de routeur (donné par l'enseignant-e). 

Chaque élève nomme ensuite ses interfaces avec les lettres de l'alphabet, en inscrivant la lettre sur l'extrémité
correspondante du scotch. 

Enfin, l'enseignant dessine au tableau le graphe du réseau simulé, en demandant aux élève à quelles sont leurs connexions.
Les élèves sont ensuite invités à compléter leur table de routage à l'aide du graphe représenté au tableau. Pour vérifier
que les tables de routage sont justes, l'enseignant fait circuler quelque messages dont il indique la destination. Si
tous les messages arrivent à destination, les tables sont sans doute correctes, mais si certains message ne rejoignent
pas leur destination, cela signifie qu'il y a des erreurs qu'il faut corriger. 

(routage.dyn)=
## Routage dynamique

On explique aux élèves que le routage a bien fonctioné, mais que pour remplir leur table, ils et elles ont pu s'aider du
graphe dessiné au tableau. Dans la réalité, les routeurs n'ont pas une vision globale du réseau, ils peuvent uniquement
communiquer avec leurs voisins. La question se pose donc de comment remplir sa table de routage sans représentation
du graphe, mais en pouvant communiquer avec ses voisins directs. 

On débarasse le scotch et les tables de routage, et on redéfinit un nouveau réseau avec du scotch de carrossier
et des tables de routage vides. Maintenant les élèves doivent remplir au crayon leur table de routage en ne pouvant échanger qu'avec leur
voisin direct, il est interdit de se lever et de regarder les parties plus distantes du réseau. Ils savent combien de routeurs
il y a et donc combien de lignes doivent être remplies dans leur table de routage. 

Les élèves arrivent généralement assez vitre à compléter les lignes concernant leurs voisins directs, puis doit émerger l'idée qu'on peut
demander à ses voisins de partager les éléments de la table déjà remplis pour compléter sa propre table. 

Une fois que les élèves ont rempli leur table, on envoie quelque message sur le réseau pour voir s'ils sont correctement acheminé. Si c'est
le cas, cela signifie que les élèves ont réussi, de manière collective et décentralisée, à organiser le routage des messages
dans leur réseau, ce que font également les routeurs. 

(routage.tcpip)=
## TCP-IP

On demande ensuite aux élèves d'écrire une phrase à destination d'un ou d'une camarade. 
On explique aux élèves que dans la pratique, les messages, par exemples des images ou des vidéos,
sont souvent trop volumineux pour circuler d'un coup sur Internet. Il faut donc les envoyer par petits
morceaux. Pour la phrase qu'il ont écrite, ils doivent l'envoyer mettant un mot par billet. Tout le monde
envoie ses phrase en même temps, et on fait ensuite un bilan. Si tout se passe trop bien, on demande à chaque
élève d'envoyer de la même manière une phrase (différente) à deux personnes différentes. 
Là, les élèves devraient se rendre compte que c'est compliqué de reconstituer les phrases. Ensemble, les élèves
doivent se mettre d'accord pour trouver une solution à ce problème, qui sera sans doute d'indiquer l'expéditeur
et de numéroter les billets pour pouvoir les reconstituer dans le bon ordre. On teste la solution pour se rendre
compte que cela fonctionne. A ce moment l'enseignant annonce de la friture sur la ligne et supprime quelque billets
en cours de transfert. Les élèves doivent trouver un moyen de garantir la transmission de tous les billets. L'idée
d'un système de quittancement devrait émerger, et on fournit pour ceci des billets d'une autre couleurs. Les élèves
testent leur système pendant que l'enseignant perturbe la transmission des messages dans un premier temps, puis des
quittances dans un second temps. 

(routage.simc)=
## Simulation complète (facultatif)
S'il reste suffisamment de temps et que les élèves sont suffisamment à l'aise,
on peut simuler à la fois le routage des billets et les modifications du réseau, avec des billets d'une troisième couleur
la communication des tables de vérités entre routeurs. L'enseignant joue à la fois le rôle d'émetteur et celui de perturbateur
du réseau en coupant et ajoutant certaines lignes de communication entre les routeurs. 

(routage.rec)=
## Récapitulatif
En commun avec les élèves, l'enseignant reprend toute les principes vus pendant cette activité en les résumant et en y associant
leur nom "technique". Une possibilité est de le faire sous forme d'exercice sur papier dans lequel les élèves doivent relier une description
du principe avec son nom. 


