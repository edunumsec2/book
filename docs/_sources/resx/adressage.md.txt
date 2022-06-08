# Adressage 

(ou comment identifier son interlocuteur)
## Les noms de domaine
Le nom *champignons.ch* est ce qu'on appelle un *nom de domaine*.
Les noms de domaines sont gérés par l'ICANN, une organisation non gouvernementale à but non lucratif
basée aux Etats-Unis dont la fonction principale est la gestions de l'adressage sur Internet.
Les noms de domaines sont gérés de manière hierarchique, selon le
*nom de domaine de premier niveau*, c'est à dire la "terminaison" de l'adresse (*.ch*, *.org*, *.fr*, etc.)Ainsi la gestion des adresses en *.ch* est confiée à Switch, une fondation suisse dont c'est le rôle principal.La personne qui a créé le site *champignons.ch* a donc
réservé ce nom de domaine auprès de Switch (en passant par un intermédiaire) et peut le conserver moyennant un paiement d'environ CHF 15.- par an.     
[Faire un encadré sur l'internationalisation des noms de domaines, et les controverses (.sucks)? ]

Si les noms de domaines sont pratiques pour désigner des adresses sur internet, les machines, elles, utilisent des
nombres pour référencer les machines connectées à Internet, c'est ce qu'on appelles les *adresses IP*. Ainsi,
la personne qui a enregistré le site *champignons.ch* a également reçu une (ou plusieurs) adresses IP de la part de
Switch ou d'un intermédiaire. 

[Ajouter une illustration de la gestion des nom de domaines? ]
    
Exercice: déterminer à l'aide du site web https://www.nic.ch/whois/ qui a enregistré le nom de domaine champignons.ch. 

## Les adresses IP
### Version 4 (IPv4)
Afin de pouvoir identifier chacune des machines connectées à Internet, il a été décidé de leur attribuer à chacune
un nombre, un peu à la manière dont les numéros de téléphones sont attribués à chaque téléphone du réseau téléphonique.
Dans sa version la plus courante, ce nombre est codé sur 32 bits, c'est-à-dire entre 0 et 2^32-1=4'294'967'295
(4 millards 294 millons 967 mille 295). On pensait
alors (c'était en 1982) que ce serait amplement suffisant pour pouvoir accomoder toutes les machines et qu'Internet
ne dépasserait pas les 4 millards de machines connectées. [dire combien il y en avait à l'époque].
Afin de rendre ces adresses plus lisibles pour les humains, on décompose d'habitude une adresse IP de 32 bits en
quatre groupes de 8 bits séparés par un point. Chaque groupe de 8 bits peut alors être représenté comme un nombre
entre 0 et 2^8-1 = 255. 

Exemple:

L'adresse 010100101010... sera décrite comme 128.233.53.23. 

Question:
Lesquelles des adresses suivantes sont des adresses IP valides:

### Blocs et masques ?

### Gouvernance
Comme les noms de domaine, les adresses IP sont gérée hiérarchiquement. Ainsi, les adresses de la forme 
46.x.x.x (c'est-à-dire celles qui commencent par 46 = 00101110) sont assignées au Centre de Coordination
Européeen qui les répartis entre différents *Registres Internet locaux* tels que Switch qui va pouvoir
louer une partie de ces adresses IP à des organisations, des entreprises (par exemple des fournisseurs d'accès Internet) ou des particuliers qui en feraient la demande. 

Certains blocs d'adresses IP sont réservés à des usages particuliers. Par exemple les adresses 10.x.x.x  ou
192.168.x.x sont réservées aux réseaux privés, c'est-à-dire des machines qui ne communiquent pas directement
avec le reste d'internet. Ainsi, ces adresses peuvent être utilisées au sein du réseau interne des entreprises,
ou pour faire communiquer différents appareils connectés (lampes, télévision, four, télécommande) au sein d'une
maison. 
** Exercices **
- Combien y aurait-il eu d'adresses IP possible s'il avait été décidé de la encoder sur 24 bits?
- Déterminer à l'aide du site xxx à quel continent sont allouées les adresses IP suivantes:
- Déterminer l'entité suisse qui possède le plus d'adresses IP
- Donner la représentation binaire de l'adresse IP y.y.y.y
- Combien y a-t-il d'adresses IP de type 192.168.x.x ?

### Adressage statique et dynamique

Une adresse IP peut être alouée de manière *statique* ou *dynamique*. Dans le cas de l'adressage statique, on configure la machine en lui indiquant son adresse IP, est c'est elle qui annonce au réseau quelle est son
adresse IP, afin que les messages puisse lui parvenir. La machine conserve ainsi toujours la même adresse IP, de la même façon qu'un téléphone conserve toujours le même numéro (sauf si on le reconfigure en modifiant par exemple la carte SIM). Dans le cas de l'adressage dynamique, la machine demande une adresse IP au moment où elle se connecte à Internet. Cette demande se fait auprès d'un serveur qui va lui allouer une adresse IP disponible parmi celles qu'il a à disposition. C'est un peu comme si chaque fois qu'on allumait son téléphone, on recevait un autre numéro pour être joignable. Si c'est nous qui initions les appels, cela ne pose pas vraimment de problème, mais si on veut être
joignable, cela devient problématique car les autres ne sauront pas comment nous trouver. Mais cela a d'une part l'avantage d'éviter qu'une machine non connectée monopolise une adresse IP sans l'utiliser et d'autre part, cela donne un (petit) degré d'anonymat et de sécurité en plus, car il sera plus difficile de cible précisément notre machine et intercepter nos messages sur sur internet.

Ainsi les serveurs (les sites web, par exemple), qui doivent être joignable en tout temps ont généralement une adresse IP statique, alors que les machines des utilisateurs et utilisatrices ont souvent une adresse IP dynamique. Lorsqu'on fait un
abonnement internet, le fournisseur d'accès propose d'habitude une adresse IP dynamique (cela lui permet d'économiser les adresse IP en sa possession), mais il est également possible, en payant un peu plus, d'obtenir une adresse IP statique. 

Exercice:
- Déterminer si votre machine a une adresse IP statique ou dynamique
- Vous souhaitez entrer en communication avec votre ami-e, mais vous avez les deux des adresses IP dynamique. Quel
moyen pourriez-vous imaginer pour que vous puissiez vous joindre. 
- En tant que propriétaire d'un site web, vous avez accès aux adresses IP des machines qui visitent votre site. Que pouvez-vous en déduire 

### Système de noms de domaine
Pour récapituler ce qui a été vu précédemment, les humains utilisent les noms de domaines pour les machines, alors que les machines, elles, utilisent les adresses IP. Afin que ces deux modes de recensement des machines soient cohérents entre eux, il est nécessaire de disposer d'un annuaire qui fera correspondre les noms de domaines aux adresses IP. Ceci est analogue aux annuaires téléphoniques qui permettre de faire correspondre le nom des personnes que l'on veut atteindre (qui serait équivalent au nom de domaine) au numéro de téléphone (qui est analogue à l'adresse IP). Cet annuaire est ce qu'on appelle le *système de noms de domaine* (Domain Name System ou DNS selon l'appellation anglaise). Au début d'internet, il s'agissait simplement d'un fichier texte librement accessible qui listait le noms de domaines et les adresses IP correspondantes. Ce fichier était maintenu à la main. Maintenant, il s'agit de machines, les serveurs DNS dans le réseau auprès desquelles il est possible d'obtenir l'adresse IP correspondante à un nom de domaine. Ces machines sont aussi organisée hierarchiquement de telle sorte que chaque serveur DNS ne stocke que les noms de domaines correspondant à une sous partie du réseau. 

[Mettre une illlustration]
[Donner quelques détails du système ? ]
    
### Version 6 (IPv6)
Avec le développement d'Internet, il est vite devenu clair que le nombres de machines connectées à Internet allait dépasser le nombre d'adresses IP différentes, et c'est pourquoi des nouveaux type d'adressage à été développé dès les années 90, IPv6 (Internet Protocol, version 6). Il a été décidé de coder les adresses IP sur 128 bits. Plutôt que
de les représenter avec 16 nombre entre 0 et 255, il a été décider des coder en 8 nombres hexadécimaux
entre 0000 et FFFF. Chaque digit de 0 à F représente ainsi 4 bits.
[montrer un exemple] 

Actuellement, les deux types d'adresses IPv6 et IPv4 coexistent sur Internet, la version IPv4 étant encore largement
plus répandue. Une adresse IP peut donc soit être sur 32 bits soit sur 128 bits. 
    
Exercices:
- Parmi les adresses suivantes, indiquer lesquelles sont au format IPv4, lesquelles sont IPv6 et lesquelles ne sont pas valides. 


