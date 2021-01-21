# Représentation des caractères

Toute l'information est représentée dans un ordinateur par des nombres 
encodés sous forme binaire par des 0 et des 1. Se pose alors la question 
de la représentation des caractères, ne serait-ce que parce que la communication 
avec les ordinateurs s'opère essentiellement (encore pour l'heure…) 
sous forme textuelle (menus, boutons…). 



## Principe

La solution retenue a consisté à définir une table de conversion qui indique 
de façon univoque une concordance entre une valeur numérique et un caractère: 

| Caractère  |   Valeur   |  |  |  | Caractère  |   Valeur   |
|------------|------------|--|--|--|------------|------------|
|     A      |     65     |  |  |  |     a      |     97     |
|     B      |     66     |  |  |  |     b      |     98     |
|     C      |     67     |  |  |  |     c      |     99     |
|     …      |     …      |  |  |  |     …      |     …      |
|     Z      |     90     |  |  |  |     z      |    122     |


Chaque caractère frappé sur le clavier engendre le nombre correspondant.

Chacun des caractères de la phrase que vous lisez a ainsi eté stocké, 
transmis et manipulé par les ordinateurs sous la forme d'une suite 
de nombres qu'on nomme *chaîne de caractères*.

Lorsqu'il s'agit de représenter ce texte à l'écran ou à l'impression 
à destination des êtres humains, les logiciels utilisent la table 
dans l'autre sens pour rendre cela intelligible. 

En plus des lettres, les caractères qui représentent les nombres (les chiffres arabes) 
sont eux-mêmes listés dans la table de conversion. Contre-intuitivement, 
la valeur binaire du caractère ne correspond généralement pas au nombre:

| Caractère  |   Valeur   |
|------------|------------|
|     0      |     48     |
|     1      |     49     |
|     …      |     …      |
|     9      |     57     |


Ces tables donnent également une repréentation des caractères de ponctuation et 
des symboles mathématiques, ainsi que des caractères non imprimables comme 
le retour à la ligne.



En réalité, il n'existe pas une table de conversion unique, mais des dizaines 
de tables de conversion. Certaines tables ont été proposées à l'origine 
par des constructeurs d'ordinateurs ou des éditeurs de systèmes d'exploitation.


## Table ASCII

La première table à s'imposer historiquement était la table ASCII 
(American Standard Code for Information Interchange). Malgré sa large acceptation, 
avec ces *7 bits par caractère*, cette table avait pour principal défaut de 
ne pas prendre en compte les caractères qui n'existent pas dans la langue anglaise, 
ne serait-ce que les lettres accentuées. 

Des tables multiples, mutuellements incompatibles, ont alors émergé: une table 
pour les européens, une autre pour les japonais et ainsi de suite.

Progressivement, notamment avec l'émergence du Web au cours des années 1990,
l'augmentation de l'interconnexion des ordinateurs personnels a amené 
au début des années 2000 à la mise en place d'une énorme table 
intégrant le contenu de toutes les tables existantes (et plus encore…).



## Table UTF

Le [standard Unicode](https://home.unicode.org/) UTF (Universal Character Set Transformation Format) 
s'est imposé pour l'échange, car il permet d'agréger sur *64 bit par caractère* 
l'entier des caractères utilisés dans toutes les langues humaines… et même extraterrestres, 
puisque le Klingon est également intégré. 

Les caractères liés à l'édition des partitions de musique ou les émojis 
y sont également intégrés. 



### Variantes UTF

Pour éviter de consommer 64 bit par caractère, des variantes plus compactes 
ont été mises à disposition. 

La plus connue – des européens, puisqu'elle regroupe les caractères 
qui nous concernent… – est la table UTF-8. Elle se concentrer 
sur les premiers 8 bit de la table UTF complète (ceux qui portent les caractères 
qui nous sont les plus utiles). 




