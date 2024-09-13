# Introduction

Internet est une infrastructure essentielle qui a complètement changé notre vie, que ce soit dans les
relations sociales, l'éducation, la recherche, le commerce, la santé, etc. Dans ce chapitre, nous allons voir, dans les grands principes, comment
Internet fonctionne et en quoi son fonctionnement est différent d'autres réseaux de communication qui l'ont précédé, tels que les réseaux postaux ou
téléphoniques. En effet, une innovation majeure d'internet est qu'il s'agit d'un réseau *décentralisé*, et ceci explique dans une large mesure son succès
et ce qu'il est devenu, même si certains craignent une recentralisation d'Internet autour des géants du numérique tels que Google et Amazon.

## Origine d'Internet

Les réseaux de communication existaient bien avant Internet, par exemple : 

- le réseau de télégraphie optique de Chappe (1794)
- le réseau de télégraphie électrique de Morse (1843)
- le réseau téléphonique de Bell (1877)
- le réseau de télégraphie par ondes radio de Marconi (1896)

Ces anciens réseaux avaient besoin d'opérateurs ou opératrices pour la transimssion des messages,
ou, pour les plus récents, ils étaient centralisés.
Cela signifie qu'il y a un point central du réseau par lequel passent toutes
les communications.
Après la 2e guerre mondiale, qui avait vu le nivellement de villes entières par des bombardements aériens (comme à Dresde)
et la bombe atomique, l'armée américaine a décidé de financer le développement d'un réseau de communication décentralisé (ou distribué),
qui serait moins vulnérable à une attaque. L'idée était qu'un réseau de communication centralisé pouvait facilement être mis hors service
par un adversaire en détruisant le point central, alors qu'un réseau de communication sans point central serait beaucoup plus difficile à
attaquer.

````{document}

```{figure} media/baranNetworks.png
---
width: 500
align: center
---
Image tirée de l'article proposant de réaliser un réseau décentralisé. Baran,
*On Distributed Communications: I. Introduction to distributed communications networks*, RAND CORP CALIF, 1964,
disponible [ici](https://www.rand.org/pubs/research_memoranda/RM3420.html). Cette image illustre la différence
entre un réseau centralisé (à gauche), dans lequel toutes les communications passent par un point central,
et un réseau distribué (droite), dans lequel tous les nœuds ont plus ou moins la même importance.
Le réseau du milieu représente un intermédiaire décentralisé, entre le réseau complètement centralisé de gauche
et le réseau distribué de droite

```
````

Les universitaires américains ont été associés à la conception de ce réseau et l'ont utilisé pour partager des informations et des ressources entre universités.
Ainsi est né Internet, par une association entre universitaires attachés surtout à la libre circulation de l'information et des militaires aux visées plutôt
sécuritaires. Dès les années 70, le mouvement hippie, séduit par les possibilités d'auto-organisation et la philosophie non hiérarchique d'Internet
a investi cette infrastructure et a développé une "cyberculture" qui marquera durablement l'histoire d'Internet, de l'émergence des réseaux sociaux
aux cryptomonnaies. En 1983, les militaires ont déconnecté leur partie du réseau du reste d'Internet pour des raisons de sécurité. 

## Structure d'internet

Internet est souvent décrit comme un *réseau de réseaux*. En effet, Internet est construit sur une structure de {glo}`lan|réseaux locaux` interconnectés les
uns aux autres. Par exemple, les ordinateurs d'une école, d'une entreprise ou d'un appartement peuvent être reliés entre eux par le wifi,
ou des câbles Ethernet et constituer un réseau local. Le réseau local est ensuite connecté, par le biais d'un {glo}`routeur|routeur`, au reste d'Internet.
Ainsi Internet est constitué d'une myriade de sous-réseaux connectés (et potentiellement enchâssés) les uns aux autres. Ces réseaux sont connectés par
les *dorsales d'Internet*, des
câbles de fibre optique capables de transférer des données à haut débit, qui traversent les continents et les océans.

```{figure} media/struct.svg
---
width: 500
align: center
---
Un réseau de sous-réseaux. Les points représentent les machines, alors que les traits indiquent les connexions entre les machines. La couleur
de fond indique les sous-réseaux. 
```

```{micro} Les câbles sous-marins d'Internet
Aller sur le site <https://www.fiberatlantic.com/submarinecablemap/> et regarder la carte des câbles sous-marins d'Internet. Trouver le câble qui relie
l'Afrique du Sud à l'Inde. Comment s'appelle-t-il, depuis quand existe-t-il et quelle est sa longueur? À qui appartient-il et quand est-il prévu de le mettre
hors service?
```

## Fonctionnement d'Internet

Cette section présente une vue d'ensemble des éléments centraux du fonctionnement d'Internet
et qui seront repris dans la suite du chapitre.

### Adressage

Tout réseau de communication a besoin d'un système d'adresses afin de pouvoir distinguer et joindre les différents destinataires.
Dans un réseau décentralisé qu'est Internet, le système d'adressage doit permettre à chaque machine connectée au réseau d'être identifiable
et joignable, sans causer de quiproquo. Cela passe par une gestion hiérarchique des adresses.

### Routage

Dans un réseau centralisé comme le téléphone traditionnel, un opérateur central (le standard dans le cas du
téléphone) relie tous les appareils branchés au réseau. Lorsque deux personnes veulent entrer en
communication, l'opérateur central les met en relation, c'est-à-dire relie leurs appareils. C'était d'abord
fait à la main, puis automatiquement (avec le téléphone à cadran rotatif). Dans un réseau décentralisé,
la mise en lien doit se faire de manière décentralisée. C'est ce qu'on appelle le *routage*.

{itodo}`exemple opératrice Marvelous Mrs Masel (ou les demoiselles du téléphone)`
{itodo}`Ajouter une illustration graphique`

### Commutation par paquets

Dans un réseau centralisé comme le téléphone, lorsque deux personnes sont en communication, elles "occupent la ligne": ces deux personnes ne sont pas joignables par d'autres personnes (c'est ce qu'indique le signal "occupé"), mais cela n'implique pas d'autres personnes qui veulent communiquer entre elles (sauf si le standard est surchargé). C'est ce qu'on appelle la *commutation de circuits*, car un circuit électrique est créé entre les deux appareils qui communiquent.

Imaginons maintenant qu'une relation soit établie entre deux appareils d'un réseau décentralisé. Si l'on avait une commutation de circuits, toutes les connexions utilisées pour acheminer
l'information entre deux appareils seraient inutilisables pour les autres personnes utilisatrices du réseau, comme illustré dans la figure ci-dessous.

```{figure} media/packetvscircuit.svg
---
width: 400
align: center
---
Si on réservait un circuit entre les ordinateurs de Liam et Julie (en orange) lorsque ceux-ci sont en
communication par internet, Tom ne pourrait pas entrer en même temps en communication avec Anna, car tous
les segments oranges seraient occupés. 
```

Cela pourrait conduire rapidement à une saturation du réseau. Pour éviter ce problème, il a été décidé de
"découper" la communication en petits morceaux (appelés les paquets) et d'envoyer chaque morceau
individuellement. C'est ce qu'on appelle la *commutation par paquets*. C'est un peu comme si au téléphone on
raccrochait et on se rappelait entre chaque mot. Cela ne monopolise pas la ligne et permet de mener plusieurs
conversations en même temps sur la même ligne. En plus, cela ne sollicite la ligne que lorsqu'une information
est transmise et pas, par exemple, pendant les moments de silence, ou lorsqu'on est en train de rédiger sa
réponse sur une messagerie.

### Les protocoles

Lorsque deux personnes entrent en communication, elles se mettent d'accord (souvent implicitement) sur la
manière dont elles communiquent, par exemple la langue qu'elles vont utiliser, la manière dont on signifie
le début et la fin d'une conversation (les salutations), etc. Pour les machines, ces règles doivent être
précisées beaucoup plus en détails, car les machines n'ont pas la faculté d'interprétation et d'adaptation
des humains. Dans un réseau décentralisé, il faut spécifier quels sont exactement les signaux que doit
envoyer une machine qui veut se connecter au réseau et établir une communication avec une autre machine.
C'est ce qu'on appelle le {glo}`protocolecomm|protocole de communication`, par exemple comment
la machine indique qu'elle veut
établir ou fermer une communication, comment elle indique avec qui elle veut établir une communication, etc.
Il y a pleins de protocoles différents, par exemple le protocole qui régit comment une machine veut se
connecter par wifi à un routeur, le protocole qui régit comment demander le contenu d'une page web à un
serveur (HTTP), le protocole qui régit comment envoyer un email sur le réseau (SMTP), ou se connecter à distance sur une
autre machine (SSH). Ces protocoles peuvent être ouverts (ou publics) et cela permet à chacun ou chacune de les utiliser,
ou ils peuvent être fermés (ou privés) ce qui limite leur utilisation à l'entreprise ou l'entité qui les a inventés.

## Organisation du chapitre

Dans le reste de ce chapitre, nous allons aborder plus concrètement les notions décrites ci-dessus et en approfondir certains aspects. Pour illustrer notre propos,
considérons la situation suivante.

```{eval} l'application aux champignons

Imaginons qu'Alice est partie à la cueillette aux champignons dans la forêt.
Elle pense avoir trouvé un beau bolet, mais pour plus de sécurité, consulte
avec son téléphone portable un site web (fictif) spécialisé dans les champignons de notre région,
*www.champignons.ch*.
 Que se passe-t-il réellement entre derrière l'écran de son téléphone?
 C'est ce que nous allons découvrir dans ce chapitre.
```
