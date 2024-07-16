# Routage

Le **routage** est le mécanisme par lequel des chemins sont sélectionnés dans un réseau pour acheminer les données d'un expéditeur jusqu'à une destination.

Pour comprendre le routage, il faut distinguer deux types de machines qui font fonctionner Internet :

- le **routeur**, qui sert d'intermédiaire dans la transmission d'un message,
- l' **hôte** qui émettent ou reçoivent un message.

{itodo}` [ajouter une illustration] `

## Les routeurs

Les *routeurs* sont des ordinateurs spécialisés dont le rôle est de relayer
et d'orienter correctement les informations qui circulent sur Internet. Si
Internet est représenté par un graphe dont les arêtes représentent les canaux
de communication, alors les routeurs sont situés aux nœuds du graphe et
décident dans quelle direction faire suivre une information afin qu'elle atteigne
son destinataire. Les routeurs sont donc comme des facteurs
disposés aux intersections du réseau Internet qui vont lire la destination des
messages qui leur arrivent et les rediriger vers la prochaine intersection
de manière à les rapprocher de leur destination. Les hôtes sont généralement aux l'extrémités
du graphe. 


```{figure} media/routing.svg
---
width: 600
align: center
---
Un routeur regarde le destinataire de chaque paquet qu'il reçoit et le redirige dans la bonne direction vers le prochain routeur ou
le destinataire. Dans notre exemple, le paquet de données (représenté par le carré orange) qu'Alice veut envoyer au serveur
champignons.ch transite par différents routeurs (représenté en violet), qui décident par où faire transiter le message en fonction
de l'adresse de destination du paquet. 
```

Pour ceci, les routeurs s'aident de *tables de routage* qui leur indique la direction à suivre pour chaque destination.

## Les tables de routage

Une table de routage est un tableau qui indique dans quelle direction orienter
un message en fonction de son destinataire. Conceptuellement, on peut imaginer
une table de routage comme un tableau à deux colonnes, la première colonne contenant
l'adresse IP de destination (ou un sous réseau à laquelle elle appartient),
la seconde colonne indiquent *l'interface* à laquelle il faut envoyer
les messages destinés à cette adresse. L'interface représente la "direction" dans laquelle envoyer le message
(par exemple un port Ethernet, un câble en fibre optique, un émetteur wifi).
Ainsi lorsqu'un nouveau message atteindra le routeur, celui-ci regardera dans sa table
de routage la ligne contenant le sous-réseau le plus spécifique incluant l'adresse IP
de destination et le fera suivre dans l'interface correspondante (qui est elle-même connectée soit à un
autre routeur soit au destinataire).

| Destinataire | Interface |
|--------------|-----------|
| 127.1.1.1    | A         |
| 34.234.15.x  | B         |
| 87.45.x.x    | C         |
| 87.33.x.x    | C         |
| x.x.x.x      | D         |

La dernière ligne représente la *passerelle par défaut* qui indique où envoyer les messages dont l'adresse
ne correspond à aucune autre ligne de la table. 

````{Exercise}
Remplir les tables de routage simplifiées des routeurs R1 et R2 du réseau suivant dans lequel les interfaces sont représentées
par les lettres A,B, et C. 
```{image} media/exo_res.svg
---
width: 600
align: center
---
```
````

Les tables de routage contiennent souvent des informations, c'est-à-dire des colonnes, supplémentaires. Elle peuvent
par exemple contenir une colonne "Distance" qui indique le nombre de d'étapes avant d'arriver à destination. Les voisins
directs sont ainsi une distance de 1, alors que les voisins des voisins ont une distance de 2, etc. D'autres informations
peuvent figurer comme le coût de transmission d'un paquet, ou le traffic maximal que cette route peut supporter.

```{Exercise}
Ajouter une colonne "Distance" à la table de routage de l'exercice précédent.

```


```{togofurther} Masques de réseau
Pour qu'une machine sache si une autre machine est dans le même sous-réseau qu'elle, son sous-réseau est spécifié par un
*masque* de réseau composé d'une suite de 32 bits (en IPv4) dont les $n$ premiers sont à 1 et les $32-n$ suivants sont à 0.
Par exemple, une machine peut avoir une adresse IP 128.178.23.132 avec un masque de 11111111.11111111.1111111.000000000.
Cela signifie que toutes les machines qui ont la même adresse IP là où le masque vaut 1 sont dans le même sous-réseau. Dans
notre exemple, cela correspond à toutes les adresses IP 128.178.23.x. Pour gagner de la place, les masques sont aussi exprimés
en 4 nombres décimaux, dans notre exemple 255.255.255.0, ou alors, pour faire encore plus court, on peut simplement spécifier
le nombre de 1 du masque, ce qui donne, toujours pour le même exemple, 128.178.23.132/24. 

Ainsi toutes les adresses IP qui n'a pas les mêmes $n$ premiers bits, fait partie d'un différent sous-réseau. Pour lui envoyer
des paquets, il faudra passer par la *passerelle par défaut* (*default gateway* en anglais) qui est le routeur qui s'occupe de
communiquer avec l'extérieur du sous-réseau.

```

Dans des petits réseaux locaux, cette table de routage peut être construite
manuellement, mais généralement c'est le routeur qui construit sa
propre table de routage en interaction avec les routeurs voisins.

## Le routage dynamique

Dans la pratique, le réseau de connections qui constituent Internet change et
évolue constamment: de nouvelles machines se connectent au réseau, changent
d'adresse IP, des
routeurs tombent en panne, certaines
connexions s'ajoutent ou disparaissent, par exemple en cas de dommages aux
câbles. Cela ne serait pas gérable pour des humains de constamment mettre à
jour les tables de routage pour les adapter à la configuration du réseau.
C'est pourquoi un système automatisé de mise à jour des tables de routage
est utilisé. C'est ce qu'on appelle le *routage dynamique*.
Cela permet non
seulement de gérer les changements configuration du réseau, mais également les
phénomènes de congestion du trafic.

### Le protocole RIP

Le protocole RIP (Routing Information Protocol) est une des manières les plus anciennes et
les plus simples de faire du routage dynamique. Toutes les 30 secondes, chaque routeur
envoie à tous ses voisins le contenu de sa table de routage. Lorsqu'un routeur reçoit une ligne
de la table de routage de son voisin dont la destination n'est pas incluse dans sa propre table,
il l'ajoute à sa table en indiquant comme interface, celle le connectant avec ce voisin.
De plus lorsqu'un routeur que son voisin dispose d'un chemin plus court pour atteindre une destination,
reçoit une ligne de la table de routage de son voisin dont la destination est incluse dans sa table, il
modifie sa table de routage pour faire passer par ce voisin les messages pour cette destination.

```{Exercise}
La table de routage d'un routeur 1 contient les lignes suivantes:
| Destinataire | Interface | Distance |
|--------------|-----------|----------|
| 114.2.1.1    | A         | 1        |
| 12.251.x.x   | B         | 2        |
| 12.25.x.x    | C         | 1        |
| 87.33.x.x    | C         | 8        |
| ...          | ...       | ...      |

Ce routeur reçoit de son voisin, le routeur 2 sur l'interface B une table contenant les lignes suivantes (les interfaces
ne sont pas indiquées):

| Destinataire | Interface | Distance |
|--------------|-----------|----------|
| 12.251.x.x   | -         | 1        |
| 12.252.x.x   | -         | 3        |
| 87.33.x.x    | -         | 5        |
| ...          | ...       | ...      |

Comment le routeur 1 peut-il compléter sa table de routage avec les informations reçue par son voisin? 

```

```{solution}
Il peut ajouter la lignes suivante:

| Destinataire | Interface | Distance |
|--------------|-----------|----------|
| 12.252.x.x   | B         | 4        |

En effet, c'est une nouvelle destination que le routeur 1 peut maintenant joindre en 
transmettant les paquets au routeur 2 (sur l'interface B) qui saura les transmettre
dans la bonne direction. 

Le routeur 1 peut aussi modifier la ligne pour la destination 87.33.x.x en mettant

| Destinataire | Interface | Distance |
|--------------|-----------|----------|
| 87.33.x.x    | B         | 6        |

Cette destination déjà existance pour le routeur 1,
mais elle peut être transmise plus rapidement en passant par le routeur 2 sur l'interface B (en 5+1=6 étapes)
que par l'interface C (en 8 étapes)
```

Toutefois, si l'on applique cette méthode telle quelle, cela peut créer des situations où des erreurs dans les tables de
routage se propagent à travers le réseau. Consédérons par exemple le bout de réseau suivant:

```{image} media/ripsplit.svg
---
width: 600
align: center
---
```
Lorsque la connexion en traitillés fonctionne, le routeur 1 remplit sa table de routage et la transmet au routeur 2.
Les tables de routage de ces routeurs contiennent donc les lignes indiquées en noir dans la figure. 
Si la connexion en traitillé se rompt, le routeur 2, va effacer de sa table de routage la ligne 
concernant la destination `2.3.1.x`, mais il serait tenté d'ajouter la ligne en rouge lorsqu'il
recevra la table du routeur 2, ce qui serait erroné. 


C'est pour éviter ces problèmes que la protocole RIP applique un certains nombre de principes, appliqués
également par d'autres protocoles de routage. 

1. Ne pas transmettre à une interface une information déjà reçue par cette interface. Ainsi, dans le l'exemple ci-dessus,
selon ce principe, le routeur 2 ne pourra pas transmettre sa ligne au routeur 1, car cette information lui vient du routeur 1.
C'est le principe de l'*horizon séparé* (*split horizon*). 


2. Si une route est bouchée, transmettre  cette information aux voisins. Dans le protocole RIP on indique
ceci par une distance égale à 16. Toute destination à distance supérieure à 15 est considérée comme inaccessible. Dans
l'exemple si dessus, le routeur 1 remplacera simplement la distance par 16 (au lieu de 1) et transmettra cette information
au routeur 2 qui mettra à jour sa table de routage. C'est le principe de l'*empoisonnement de route* (*route poisoning*).

```{eval} L'exemple d'Alice
Les paquets IP échangés entre le téléphone d'Alice et le serveur sont acheminé de routeur en routeur. Chaque routeur
consulte sa table de routage pour savoir dans quelle direction transférer le paquet reçu. Ces tables de routage
se constituent automatiquement en échangeant des informations avec les routeurs voisins. 
```
