(appr:repinfo:redondance)=
# Redondance

Est-il possible de concevoir un objet qui ne tombe jamais en panne ?

Les ingénieurs cherchent le moyen d’y parvenir et des résultats probants sont observables dans l’aviation. Les [statistiques](https://www.icao.int/safety/iStars/Pages/Accident-Statistics.aspx) montrent que, depuis une décennie, seuls 2 à 4 accidents mortels par millions de vols sont enregistrés. Ce résultat est atteint au prix d’une maintenance extrêmement stricte, une formation exigeante et continue du personnel de bord, une analyse méticuleuse de chaque incident, un contrôle permanent du respect des recommandations tant par les constructeurs que par les opérateurs, et enfin un soin particulier apporté à la redondance des systèmes critiques.

La **redondance** est une technique qui consiste à dupliquer les composants qui gèrent les fonctions critiques d’un système pour augmenter sa fiabilité. Évidemment, la redondance des systèmes a un coût : en complexité, en masse et volume, en prix d’achat et en maintenance. En effet, paradoxalement, comme chaque composant présente une probabilité de tomber panne (fût-elle faible), plus il y a de composants, plus il y a de pannes. Toutefois, moins leurs conséquences sont graves, car la probabilité que les composants redondant tombent en panne simultanément devient négligeable. On parle alors d’un **système robuste ou résilient**, puisqu’il n’est pas mis en péril dès la première panne.

## Somme de contrôle (checksum)

La redondance se retrouve à tous les niveaux des systèmes informatiques, qu’ils soient embarqués dans un avion ou non. Pour s’assurer qu’une information est reçue **intégralement** (sans pertes) et **parfaitement** (sans erreurs), un expéditeur pourrait naïvement l’envoyer deux fois, par deux moyens indépendants, dans un SMS et sur une carte postale par exemple. Faudrait-il alors que le destinataire confirme la réception, également, par deux moyens indépendants ?! On convient aisément que cette solution serait atrocement coûteuse. Par ailleurs, une étude attentive montre que lorsque les copies reçues diffèrent, cette méthode ne permet pas de déterminer laquelle des deux copies est la bonne. Si elle permet d’identifier qu’il y a un problème, elle ne propose pas de solution pour le résoudre.

Pourtant, aucun signal n’étant parfait, l’augmentation de la vitesse de transmission débouche nécessairement sur une augmentation des erreurs, notamment des pertes d’information et des mutations. Les systèmes informatiques, dès lors qu’ils communiquent continuellement et abondamment, sont particulièrement sensibles à ce problème. Lorsqu’il s’agit d’assurer l’intégrité des informations transmises (cohérence et exactitude), des solutions plus élégantes que la proposition naïve présentée plus haut ont été élaborées pour effectuer un contrôle de qualité par redondance.

Parmi les solutions existantes, les **checksums** sont une brève représentation d’un bloc d’information plus grand, des sortes d’empreintes numériques. Bien qu’elles soient transmises avec le bloc d’information qu’elles représentent, leur petite taille relative ne surcharge pas démesurément la transmission. En choisissant une représentation qui se calcule et se contrôle facilement, ces checksums n’imposent pas non plus un temps de traitement beaucoup plus long pour les créer et les vérifier.

Idéalement, les checksums de deux blocs d’information sont très différentes même lorsque les différences entre les blocs sont infimes. Cela simplifie en effet la détection des erreurs.

Depuis la nuit des temps informatiques, la forme la plus simple d’une checksum est le **bit de parité**. Il permet de contrôler par redondance une erreur sur la transmission d’un paquet de 7 bits, en utilisant 1 bit supplémentaire.

Dans l’exemple qui suit, on donne la valeur 0 au bit de parité lorsque la somme des bits de la donnée à transmettre est paire, et la valeur 1 lorsque cette somme est impaire. On notera que, de cette façon, la somme des 8 bits est toujours paire. Le bit de parité est habituellement placé à la position de poids le plus faible (comme on peut le voir dans le tableau ci-dessous).

| Donnée à transmettre | Somme des bits | Bit de parité | Donnée transmise  |
|----------------------|----------------|---------------|-------------------|
|       0000000        |       0        |        0      |   0000000**0**    |
|       0000001        |       1        |        1      |   0000001**1**    |
|       0000010        |       1        |        1      |   0000010**1**    |
|       0000011        |       2        |        0      |   0000011**0**    |
|       0000100        |       1        |        1      |   0000100**1**    |
|       0000101        |       2        |        0      |   0000101**0**    |
|       0000110        |       2        |        0      |   0000110**0**    |
|       0000111        |       3        |        1      |   0000111**1**    |
|          …           |                |        …      |        …          |
|       1111101        |       6        |        0      |   1111101**0**    |
|       1111110        |       6        |        0      |   1111110**0**    |
|       1111111        |       7        |        1      |   1111111**1**    |

**Tab. 5** Exemple de la mise en oeuvre d’un bit de parité pour des données de 7 bits. Le bit de parité, placé à la position de poids le plus faible, indique si la somme des bits dans la donnée à transmettre est paire (0) ou impaire (1). Notez que la somme des 8 bits est toujours paire.

`````{htmlonly}
Le bloc suivant permet de créer un exemple illustrant le calcul de parité et de son contrôle.

````{codeplay}

def getControlBit(number):
    count = 0
    bit = 1
    while bit < 128:
        if number & bit:
            count += 1
        bit <<= 1

    return (count) % 2

value = int(input('Donnée à transmettre [0-127] : '))
print('-'*42)
print(format(value, ' 38b'))
value = value & 0x7f
control = getControlBit(value)
print('-'*42)
print('  donnée (limitée à 7 bits)  :', value)
print('  représentation binaire     :', format(value, '07b') + '.')
print('  bit de contrôle            :', '.'*7 + str(control))
print('-'*42)
print('Donnée transmise             :', format((value<<1) ^ control, '08b'))
print('-'*42)

===
# Cliquez sur Exécuter pour créer un exemple
````
`````

On notera que, pour un coût de taille modeste (un huitième des bits transmis) et un calcul rapide à réaliser (une somme et une comparaison), des erreurs de transmission ponctuelles — celles qui ne portent que sur un nombre de positions impair — sont immédiatement détectables. Cela inclut les erreurs qui porteraient sur le bit de parité lui-même.

La redondance contribue à la **sécurité des données** en renforçant, par exemple, leur *intégrité* ou leur *disponibilité*. En contrepartie, elle s’accompagne toujours d'un **coût**, qui peut se traduire par une augmentation de la *quantité de données stockées*, du *temps de traitement* nécessaire, ou des deux. 

````{didyouknow}

Les contrôles de bit de parité peuvent être intégrés aux composants électroniques. La mémoire vive RAM (*Random Access Memory*) de type ECC (*Error-Correcting Code*) s’appuie sur des bits de contrôle pour détecter, voire corriger, les erreurs de stockage qui pourraient affecter les données ou le code des logiciels en cours d’exécution. Cette fonction supplémentaire explique leur coût plus élevé.

````

## Fonction de hachage

L’exemple de bit de parité permet grossièrement de contrôler une communication caractère par caractère. Une forme plus élaborée du même concept est le **hachage** de l’information qui peut alors s’appliquer à des quantités d’information beaucoup plus importantes, de type et de longueurs variables.

Prenons par exemple un texte, représenté par les valeurs décimales de son encodage ASCII, et construisons une empreinte numérique à l’aide de calculs simples :

|   h |   a |   c |   h |   a |   g |   e |
|-----|-----|-----|-----|-----|-----|-----|
| 104 |  97 |  99 | 104 |  97 | 103 | 101 |

La somme de toutes ces valeurs totalise 705 (= 104 +  97 + 99 + 104 +  97 + 103 + 101), soit 0x2**C1** en hexadécimal.

La somme des produits de chaque valeur par l'index de sa position totalise quant à elle 2821 (= 1x104 + 2x97 + 3x99 + 4x104 + 5x97 + 6x103 + 7x101), soit 0xB**05** en hexadécimal.

On peut décider de garder uniquement les deux positions hexadécimales de poids le plus faible, (C1 et 05, respectivement), pour construire une empreinte numérique (**digest** ou **hash**) indépendante de la longueur du texte (C105 dans cet exemple).

Si le texte venait à être modifié, ne serait-ce que très légèrement, l'empreinte numérique ainsi définie serait affectée :

|   h |   a |   c |   h |   a |    h    |   e |
|-----|-----|-----|-----|-----|---------|-----|
| 104 |  97 |  99 | 104 |  97 | **104** | 101 |

En effet, la somme des valeurs totalise alors 706 (= 104 +  97 + 99 + 104 +  97 + 104 + 101), soit 0x2**C2** en hexadécimal, alors que la somme des produits totalise 2827 (= 1x104 + 2x97 + 3x99 + 4x104 + 5x97 + 6x104 + 7x101) soit 0xB**0B**, ce qui donne un nouveau hash de C20B. Bien que les deux messages ne diffèrent que d’un seul bit, leurs checksums sont très différentes (C105 et C20B, respectivement).

`````{htmlonly}
Le bloc suivant permet de créer un exemple illustrant la fonction de hachage décrite précédemment.

````{codeplay}

def getSum(information):
    answer = 0
    for car in information:
        answer += ord(car)
    return answer


def getProductsSum(information):
    answer = 0
    index = 1
    for car in information:
        answer += index * ord(car)
        index += 1
    return answer


def getTwoLastPositions(value):
    return '{:02X}'.format(value)[-2:]


def toHash(text):
    return getTwoLastPositions(getSum(text)) \
         + getTwoLastPositions(getProductsSum(text))


text = input('Texte à hacher : ')
sum = getSum(text)
prodSum = getProductsSum(text)

print('-'*42)
print('somme              :', sum)
print('                    ', hex(sum))
print('-'*42)
print('somme des produits :', prodSum)
print('                    ', hex(prodSum))
print('-'*42)
print('hash               :', toHash(text))
print('-'*42)
===
# Cliquez sur Exécuter pour créer un exemple
````
`````

On notera que la suppression d’une lettre au texte (“hachage” => C105) ne change pas la longueur de cette simple empreinte mais sa valeur (“hachag” => 5C42) et que cette fonction de hachage est aussi sensible à la casse (“Hachage” => A1E5).

On notera également que les mots ‘hat’ et ‘fer’ possèdent la même empreinte (3D86), l’empreinte n’est donc pas unique.

En effet, l’ empreinte numérique est une simplification de l’information hachée. Il est dès lors envisageable de trouver deux informations, de longueurs possiblement différentes, dont les empreintes sont identiques. En contrepartie, il n’est en principe pas envisageable de reconstruire le texte d’origine sur la base de la seule empreinte.

Toutefois, grâce à leurs propriétés (déterministes et rapides), des **fonctions de hachage** plus complexes (**SHA**, **MD5**, etc.) trouvent des applications dans de nombreux contextes : authenticité (signatures numériques) ; intégrité (erreurs de transfert, stockage, blockchains, etc.) ; identification (fichiers, connexions réseau, etc.) ; authentification (stockage et vérification des mots de passe) ; etc.


````{didyouknow}

Même si le hachage d’une information est à dessein relativement rapide en soi, des contraintes artificielles provoquant délibérémment la multiplication de ces hachages peuvent être imposées lors de l’ajout des blocs dans une blockchain. Cela constitue la preuve de travail (*proof-of-Work* ou PoW) des cryptomonnaies que l’on nomme communément **minage des cryptomonnaies**. 

<!--[quantité de calcul pour gagner une fraction de bitcoins, pour t’enrichir sur le fait que l’argent n’existe pas]-->

La quantité faramineuse de calculs ainsi engendrée pour complexifier artificiellement ce hachage est responsable d'une part mesurable de la consommation électrique mondiale.

Le partage de l'intégralité de la blockchain par l'ensemble des membres du réseau constitue en soi une redondance qui favorise la disponibilité de l'information, mais au prix du stockage d'une quantité mirobolante de copies et de la complexité de leur maintenance.

````


## Stockage de l’information

Les pannes de disques durs sont très communes et entrainent des pertes de données aux conséquences parfois irrécupérables.

La mise en place de sauvegardes automatiques régulières sur des supports distincts et, de préférence, délocalisés
(en soi une forme de redondance sur le stockage de l'information) représente un début de réponse. Toutefois, si le support utilisé pour le stockage n'est lui-même pas résilient, la sécurité de ces sauvegardes n'est pas assurée.

Une solution technique a été proposée dès les années 1980 basée sur la disponibilité de grappes de disques durs relativement bon marché (*Redundant Array of Independent Disks*, RAID). Il est alors possible de créer (entre autres) des disques logiques de taille T (RAID 1), formés d'une grappe de $n$ disques physiques de taille T, sur chacun desquels est stockée une copie complète des données. À chaque écriture, le système maintient automatiquement l'ensemble des $n$ copies, ce qui permet de récupérer l'intégralité de l'information, même si $n-1$ disques sont endommagés.

Ici encore, en exploitant le principe des bits de parité décrits précédemment, il est par exemple possible de construire une grappe de 3 disques (RAID 5) de taille T capable de stocker 2xT données. La part de stockage perdue (un disque sur trois) y est utilisée de telle sorte que, lorsqu'un des trois disques est perdu -- n'importe lequel des trois ! --, aucune information n'est réellement perdue. Mieux, si le disque défectueux est remplacé, son contenu peut être reconstruit automatiquement et la résilience de la grappe rétablie. n outre, les vitesses d’écriture et de lecture sur ces trois disques en grappe sont également accélérées.

Ce type d’infrastructure, malgré son coût plus élevé, est à la base des systèmes critiques qui doivent garantir la disponibilité des informations, ce qui pourrait également inclure les copies de sécurité de son ordinateur personnel.

Les systèmes informatiques récents sont distribués à l’échelle d’Internet, tant pour leurs parties matérielles que logicielles. On parle de **systèmes cloud** ou informatique en nuage.

On trouve ainsi des systèmes de stockage de fichiers distribués sur plusieurs ordinateurs, voire dans plusieurs fermes de stockage. Cette configuration augmente considérablement la sécurité des données en contribuant à leur **intégrité** et à leur **disponibilité**.

