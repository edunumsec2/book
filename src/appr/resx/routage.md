# Routage 
(ou comment acheminer l'information)
Nous avons vu précédemment, comment il est possible d'identifier sur internet
une machine avec laquelle on souhaite communiquer, en ayant recours à son
adresse IP ou un nom de domaine. Contrairement à un système centralisé comme
le téléphone, où un opérateur va mettre directement en relation les deux
machines qui communiquent, sur internet l'acheminement de l'information d'une
machine à une autre se fait de manière décentralisée. C'est le problème du
*routage*, c'est-à-dire quel chemin (ou quelle route) l'information va emprunter pour
aller d'un point à l'autre du réseau. [ajouter une illustration]

## Les routeurs    
Les *routeurs* sont des ordinateurs spécialisés dont le rôle est de relayer
et d'orienter correctement les informations qui circulent sur internet. Si
internet est représenté par un graphe dont les arêtes représentent les canaux
de communication, alors les routeurs sont situé aux noeuds du graphes et
décident dans quelle direction faire suivre une information afin qu'elle atteigne
son destinataire. Les routeurs sont donc comme des facteurs
disposés aux intersections du réseau internet qui vont lire la destination des
messages qui leur arrivent et les rediriger vers la prochaine intersection
de manière à les rapprocher de leur distination. [ajouter une illustration]
Pour ceci, les routeurs s'aident de *tables de routage* qui leur indique la
direction à suivre pour chaque destination. 
        
## Les tables de routage
Une table de routage est un tableau qui indique dans quelle direction orienter
un message en fonction de son destinataire. Conceptuellement, on peut imaginer
une table de routage comme un tableau à deux colonnes, la première colonne contenant
l'adresse IP de destinatation (ou un sous réseau à laquelle elle appartient),
la seconde colonne indique *l'interface* à laquelle il faut envoyer
les messages destinés à cette adresse. L'interface représente la "direction" dans laquelle envoyer le message,
(par exemple un port ethernet, un cable en fibre optique, un émetteur wifi).
Ainsi lorsqu'un nouveau message atteindra le routeur, celui-ci regardera dans sa table
de routage la ligne contenant le sous-réseau le plus spécifique incluant l'adresse IP
de destination et le fera suivre dans l'interface correspondante (qui est elle-même connectées soit à un
autre routeur soit au destinataire). 

[Ajouter une illlustration]

### Format effectif 
[Mettre cette information comme facultative, utile si on veut travailler avec un vrai réseau]
Toutefois, afin de ne pas avoir à conserver en mémoire une ligne par destinataire possible,
la première colonne utilise les masques de sous-réseaux qui sont représentés par deux colonnes.


Dans des petits réseaux locaux, cette table de routage peut être construite
manuellement, mais généralement c'est le routeur qui construit sa
propre table de routage en interaction avec les routeurs voisins. 
    
## Le routage dynamique
Dans la pratique, le réseau de connections qui constitute Internet change et
évolue constamment: des nouvelles machines se connectent au réseau, changent
d'adresse IP, des
routeurs tombent en panne, certaines
connexion s'ajoutent ou disparaissent, par exemple en cas de dommages aux
cables. Cela ne serait pas gérable pour des humains de constamment mettre à
jour les tables de routage pour les adapter à la configuration du réseau.
C'est pourquoi un système automatisé de mise à jour des tables de routage
est utilisé. C'est ce qu'on appelle le *routage dyamique*.
Cela permet non
seulement de gérer les changement configuration du réseau, mais également les
phénomènes de congestion.    

### Le protocole RIP
Le protocale RIP (Routing Information Protocol) est une des manière les plus anciennes et
les plus simple de faire du routage dynamique. Toutes les 30 secondes, chaque routeur
envoie à tous ses voisins le contenu de sa table de routage. Lorsqu'un routeur reçoit une ligne
de la table de routage de son voisin dont la destination n'est pas inclue (au sens large [préciser]) dans sa propre table,
il l'ajoute à sa table en indiquant comme interface, celle le connectant avec ce voisin. 
De plus lorsqu'un routeur reçoit un ligne de la table de routage de son voisin dont la destination est inclue dans sa table mais
avec une distance plus grande, cela signifie qu'en passant par ce voisin le chemin sera plus court (ou égal) pour atteindre sa destination.
Le routeur modifie sa table de routage pour faire passer les messages à destination de ce destinateur par ce voisin. 
[ajouter deux exemples]
