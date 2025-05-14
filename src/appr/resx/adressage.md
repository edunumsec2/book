# Adressage

L'adresse est une notion importante en communication, qui permet à une personne ou une machine de s'adresser à une autre personne ou machine spécifique.
Le rôle d'un système d'adressage, tel que celui de la poste, est de permettre d'identifier et de joindre une destination sans ambiguïté, et c'est pour ceci que
chaque adresse doit être unique. 


## Les noms de domaine

Le nom *champignons.ch* est ce qu'on appelle un *nom de domaine*.
Les noms de domaines sont gérés par l'ICANN, une organisation non gouvernementale à but non lucratif
basée aux États-Unis dont la fonction principale est la gestion de l'adressage sur Internet.
Les noms de domaines sont gérés de manière hiérarchique, selon le
*nom de domaine de premier niveau*, c'est à dire la "terminaison" de l'adresse (*.ch*, *.org*, *.fr*, etc.) Ainsi la gestion des adresses en *.ch* est
confiée à Switch, une fondation suisse dont c'est le rôle principal. La personne qui a créé le site *champignons.ch* a donc
réservé ce nom de domaine auprès de Switch (en passant par un intermédiaire) et peut le conserver moyennant un paiement d'environ CHF 15.- par an.

```{didyouknow}
Au début, les noms de domaine de premier niveau étaient limités à quelques possibilités, telles que ".com" pour les organisations
commerciales, ".edu" pour les universités (américaines), ".gov" pour le gouvernement (américain), ".mil" pour l'armée (américaine), ".org"
pour les organisations (à but non lucratif) et, dès les années 80, différents pays ont décidé d'enregistrer des noms de domaine de premier
niveau pour leur pays, par exemple ".ch" pour la Suisse, ".fr" pour la France. Puis il a été décidé d'ouvrir d'autres noms de domaine et
de les mettre aux enchères. Une entreprise a
alors décidé de vendre des domaines ".sucks" qu'elle a vendus très cher à certaines grandes entreprises (par exemple apple.sucks) qui avaient
peur que ce site ne devienne une plateforme pour les critiquer. 

````

Si les noms de domaines sont pratiques pour désigner des adresses sur Internet, les machines, elles, utilisent des
nombres pour référencer les machines connectées à Internet, c'est ce qu'on appelle les *adresses IP*. Ainsi,
la personne qui a enregistré le site *champignons.ch* a également reçu une (ou plusieurs) adresse IP de la part de
Switch ou d'un intermédiaire.

{itodo}`Ajouter une illustration de la gestion des noms de domaines?`

```{micro}
Déterminer à l'aide du site web <https://www.nic.ch/whois/> qui a enregistré le nom de domaine champignons.ch.
```

## Les adresses IP

### Version 4 (IPv4)

Afin de pouvoir identifier chacune des machines connectées à Internet, il a été décidé de leur attribuer à chacune
un nombre, un peu à la manière dont les numéros de téléphone sont attribués à chaque téléphone du réseau téléphonique.
Dans sa version la plus courante, ce nombre est codé sur 32 bits, ce qui donne à peu près 4 milliards de possibilités ($2^{32}$).
On pensait alors (c'était en 1982) que 4 milliards d'adresses seraient amplement suffisantes pour pouvoir accommoder
toutes les machines pendant encore beaucoup d'années, et qu'Internet
ne dépasserait pas les 4 milliards de machines connectées. A cette éqpoque, il n'y avait que quelques centaines d'ordinateurs
connectés à Internet. 
Afin de rendre ces adresses plus lisibles pour les humains, on décompose d'habitude une adresse IP de 32 bits en
quatre groupes de 8 bits séparés par un point. Chaque groupe de 8 bits peut alors être représenté comme un nombre décimal
entre 0 et 255 ($2^8-1$).

% L'exemple suivant montre comment trouver la représentation binaire, d'un tuple de 4 nombres décimaux. L'adresse montrée est
% `128.233.53.23`
% 
% 
% ```{codeplay}
% addr = (128, 233, 53, 23)
% 
% print(*addr, sep='.')
% for i in addr:
%     print(f'{i:08b}.', end='')
% ```
% 
% Le code suivant montre la transformation d'un tuple de 4 nombres binaires en nombres décimaux, séparés par un point (`.`)
% 
% ```{codeplay}
% addr = (0b1111_1111, 0b0001_1111, 0b0000_0011, 0b0000_0000)
% 
% for i in addr:
%     print(i, end='.')
% ```
% 
````{exercise}
Lesquelles des adresses suivantes sont des adresses IP valides:
1. ```240.264.23.2```
1. ```123.8.12.2.34```
1. ```123.23.2```
1. ```205.233.12.23```

````
% 
% Pour répondre à une telle question automatiquement nous pourrions ajouter des tests comme celui-ci.
% 
% ```{codeplay}
% addresses = ((240, 264, 23, 2),
%              (123, 8, 12, 2, 34), 
%              (123, 23, 2),
%              (205, 233, 12, 23))
% 
% for a in addresses:
%     print(*a, sep='.', end='\t')
%     if len(a) != 4:
%         print('erreur: nombre de composants incorrect')
%         continue
%     if max(a) > 255:
%         print('erreur: composant supérieur à 255')
%         continue
%     print('addresse IP valide')
% ```
% 

### Version 6 (IPv6)

Avec le développement d'Internet, il est vite devenu clair que le nombre de machines connectées à Internet allait dépasser le nombre d'adresses IP différentes, et c'est pourquoi un nouveau type d'adressage a été développé dès les années 90, IPv6 (Internet Protocol, version 6). Il a été décidé de coder les adresses IP sur 128 bits. Plutôt que
de les représenter avec 16 nombres entre 0 et 255, il a été décidé de coder en 8 nombres hexadécimaux
entre 0000 et FFFF. Chaque chiffre de 0 à F représente ainsi 4 bits, et chaque nombre de 4 chiffres hexadécimaux représente donc $4\cdot 4 = 16$ bits. En en prenant 8, on arrive bien à $8\cdot 16 = 128$ bits. 

Par exemple ```4E3F.DEA7.409B.412C.2516.4A2B.2CFE.1282``` pourrait constituer une adresse IPv6 valide. Elle est en effet
constituée de 8 nombres à quatre chiffres hexadécimaux.

Actuellement, les deux types d'adresses IPv6 et IPv4 coexistent sur Internet, la version IPv4 étant encore largement
plus répandue. Une adresse IP peut donc soit être sur 32 bits soit sur 128 bits.

````{exercise}
Parmi les adresses suivantes, indiquer lesquelles sont au format IPv4, lesquelles sont IPv6 et lesquelles ne sont pas valides. Justifier sa réponse. 

1. ```128.23.54.45```
1. ```31.43.132.45.51.654.4355.4325```
1. ```1923.2123.1323.4324.4241.2434.7657.5757```
1. ```ADEFE.ACDEA.AABCD.DDEBC.FFEDA.AEABC.ACADE.EFDF```
1. ```1230.121D.12AEAB.1231D.4324B.2765.5435D.4378```
1. ```D2G3.4234.534FG.2141.12GE.12AD.85C2.GE32```
1. ```123A.3213.564E.6746.2DD2.A897```
1. ```124.234.432.21```

````

### Gouvernance

Comme les noms de domaine, les adresses IP sont gérées hiérarchiquement. Ainsi, les adresses IPv4 de la forme
`46.x.x.x` (c'est-à-dire celles qui commencent par `46 = 00101110`) sont assignées au Centre de Coordination
Européen qui les répartit entre différents *Registres Internet locaux* tels que Switch qui va pouvoir
louer une partie de ces adresses IP à des organisations, des entreprises (par exemple des fournisseurs d'accès Internet)
ou des particuliers qui en feraient la demande.

Certains blocs d'adresses IP sont réservés à des usages particuliers. Par exemple les adresses `10.x.x.x`  ou
`192.168.x.x` sont réservées aux réseaux privés, c'est-à-dire des machines qui ne communiquent pas directement
avec le reste d'Internet. Ainsi, ces adresses peuvent être utilisées au sein du réseau interne des entreprises,
ou pour faire communiquer différents appareils connectés (imprimante, télévision, ordinateurs, ou smartphones) au sein d'une
maison. Dans l'exemple ci-dessous, un fournisseur d'accès à Internet (tel que Swisscom par exemple) à reçu toutes les
adresses de type 213.221.x.x. Il en garde une partie pour son propre usage, par exemple pour son site web et les machines qui opèrent le réseau.
Une autre partie des adresses sera louée à
des entreprises ou des particuliers qui sont ses clients. Ceux-ci bénéficieront donc d'une adresse IP leur permettant d'être
joignables par le reste d'Internet. 

```{micro}
- Déterminer à l'aide de cette [page Wikipedia](https://en.wikipedia.org/wiki/List_of_assigned_/8_IPv4_address_blocks) à quel continent sont allouées les adresses IP suivantes:
  - 212.x.x.x
  - 154.x.x.x
  - 20.x.x.x
- Déterminer à l'aide de [ce site](https://www.nirsoft.net/countryip/ch.html) l'entité suisse qui possède le plus d'adresses IP
```


```{exercise}
- Combien y a-t-il d'adresses IP de type `192.168.x.x` ?
- Combien y aurait-il eu d'adresses IP possibles s'il avait été décidé de l’encoder sur 24 bits?
- Donnez la représentation binaire de l'adresse IP `10.0.45.12`
```



### Réseau privé

Les particuliers et entreprises ont généralement un réseau privé, un *intranet*, qui utilise
les adresses 10.x.x.x. L'appareil qui permet de connecter ce réseau privé au reste d'Internet est un *routeur*, par exemple
la boîte wifi qui est fournie par le fournisseur d'accès. Ce routeur a à la fois une adresse locale
(dans notre exemple 10.0.1.1) pour être joignable depuis le réseau privé et une adresse globale (213.221.190.41 dans
l'exemple ci-dessous) pour être atteignable depuis le reste d'Internet. Le routeur joue un peu le rôle du secrétariat de
l'école en s'occupant de transmettre le courrier entre l'intérieur et l'extérieur de l'école. De manière similaire,
le secrétariat a d'habitude deux boites aux lettres, une pour les documents déposés par des personnes qui sont à l'intérieur
de l'école (élèves, personnel enseignant) et une destinée au facteur qui amène le courrier en provenance de l'extérieur du
gymnase. 

```{figure} media/IPnetwork.svg
---
width: 600
align: center
---
Exemple de distribution des adresses IP, avec un fournisseur d'accès ayant obtenu les adresses 213.221.x.x, rt qui fournit un
accès Internet à Alice et Bob. Les routeurs, en vert clair, ont deux adresses IP. 
```

```{micro}
- A l'aide d'un navigateur web, aller sur le site <https://www.whatismyip.com> et déterminer sa
propre adresse IP. 
- Dans un terminal taper la commande suivante qui détermine votre adresse IP:
  - sur Mac Os ou Linux: `ipconfig getifaddr en0`
  - sur Windows: `ipconfig`
- Obtient-on la même réponse? Pourquoi?
```


### Adressage statique et dynamique

Une adresse IP peut être allouée de manière *statique* ou *dynamique*. Dans le cas de l'adressage statique, on configure la machine en lui indiquant son adresse IP, est c'est elle qui annonce au réseau quelle est son
adresse IP, afin que les messages puissent lui parvenir. La machine conserve ainsi toujours la même adresse IP, de la même façon qu'un téléphone conserve toujours le même numéro (sauf si on le reconfigure en modifiant par exemple la carte SIM). Dans le cas de l'adressage dynamique, la machine demande une adresse IP au moment où elle se connecte à Internet. Cette demande se fait auprès d'un serveur qui va lui allouer une adresse IP disponible parmi celles qu'il a à disposition. C'est un peu comme si chaque fois qu'on allumait son téléphone, on recevait un autre numéro pour être joignable. Si c'est nous qui initions les appels, cela ne pose pas vraiment de problème, mais si on veut être
joignable, cela devient problématique, car les autres ne sauront pas comment nous trouver. Mais cela a d'une part l'avantage d'éviter qu'une machine non connectée monopolise une adresse IP sans l'utiliser et d'autre part, cela donne un (petit) degré d'anonymat et de sécurité en plus, car il sera plus difficile de cibler précisément notre machine et intercepter nos messages sur Internet.

Ainsi les serveurs (les sites web, par exemple), qui doivent être joignables en tout temps ont généralement une adresse IP statique, alors que les machines des utilisateurs et utilisatrices ont souvent une adresse IP dynamique. Lorsqu'on fait un
abonnement Internet, le fournisseur d'accès propose d'habitude une adresse IP dynamique (cela lui permet d'économiser les adresses IP en sa possession), mais il est également possible, en payant un peu plus, d'obtenir une adresse IP statique.

```{micro}
En regardant les paramètre réseaux, déterminer si sa machine a une adresse IP statique (manuel) ou dynamique (DHCP). 
```

```{exercise}
1. Vous souhaitez entrer en communication avec votre ami-e, mais vous avez les deux des adresses IP dynamiques. Quel
moyen pourriez-vous imaginer pour que vous puissiez vous joindre.

2. En tant que propriétaire d'un site web, vous avez accès aux adresses IP des machines qui visitent votre site. Pouvez-vous dès lors identifier une même personne
qui revient plusieurs fois sur votre site ?

3. Depuis votre adresse IP dynamique, vous être entré en communication avec un site web illégal. La police peut-elle vous retrouver à partir de votre adresse IP? Si oui comment, si non pourquoi?



```

```{solution}
1. Vous pouvez vous connecter tous deux à un serveur central qui a une adresse IP fixe et qui s'occupera de relayer vos messages à vos adresses
dynamiques. C'est ce que fait un serveur mail ou de messagerie telle que Signal ou Whatsapp. 

2. Si elle a une adresse IP dynamique, alors elle aura probablement des adresses IP différentes lors de ses visites
en des jours différents. On ne pourra donc pas l'identifier en regardant uniquement son adresse IP. Par contre, ce sera possible
de le faire ne déposant un {glo}`cookie|cookie` sur l'ordinateur des personnes qui viennent sur votre site. De plus  en enregistrant
d'autres paramètres que son navigateur voudra bien nous transmettre, tels que son système d'exploitation, la langue,
l'appareil, etc., on peut reconstituer son empreinte numérique
et l'identifier ainsi. C'est ce qu'on appelle en anglais le fingerprinting, que l'on
peut [bloquer avec certains navigateurs](https://www.mozilla.org/fr/firefox/features/block-fingerprinting/).

3. Oui, votre fournisseur d'accès à Internet doit garder une trace de quelle adresse IP a été allouée à qui et à quel moment.
La police peut dès lors exiger ces informations en cas de soupçons.
```

## Système de noms de domaine

Pour récapituler ce qui a été vu précédemment, les humains utilisent les noms de domaines pour les machines, alors que les machines, elles, utilisent les adresses IP. Afin que ces deux modes de recensement des machines soient cohérents entre eux, il est nécessaire de disposer d'un annuaire qui fera correspondre les noms de domaines aux adresses IP. Ceci est analogue aux annuaires téléphoniques ou aux contacts du smartphone qui permettent de faire correspondre le nom des personnes que l'on veut atteindre (qui serait équivalentes au nom de domaine) au numéro de téléphone (qui est analogue à l'adresse IP). Cet annuaire est ce qu'on appelle le *système de noms de domaine* (Domain Name System ou DNS selon l'appellation anglaise). Au début d'Internet, il s'agissait simplement d'un fichier texte librement accessible qui listait le nom de domaines et les adresses IP correspondantes. Ce fichier était maintenu à la main. Maintenant, il s'agit de machines, les serveurs DNS dans le réseau auprès desquelles il est possible d'obtenir l'adresse IP correspondante à un nom de domaine. 

Ces machines sont aussi organisées hiérarchiquement de telle sorte que chaque serveur DNS ne stocke que les noms de domaines correspondant à une sous-partie du réseau.

```{didyouknow} Le hacking de DNS
Une méthode de hacking consiste à mettre en ligne un serveur DNS malveillant
qui va diriger le traffic vers des faux sites web se faisant passer pour des
vrais. Par exemple, un hacker pourrait mettre en ligne un DNS malveillant
indiquant une fausse adresse IP pour le site google.com, et à cette adresse,
mettre un serveur web ayant la même page d'accueil que Google. Lorsque une
quelqu'un essaiera de se connecter à son compte google sur le faux site,
ce site enregistrera simplement le login et mot de passe et renverra sur le
vrai site web. Le hacker aura ainsi le login et mot de passe du compte google
de la personne, pouvant ainsi avoir accès à ses emails et documents. La
difficulté pour le hacker est de "convaincre" que son serveur DNS est fiable.
```

```{didyouknow} La censure par le DNS
Une des méthodes à disposition d'un état qui souhaite empêcher ses habitants
d'accéder à certains sites consiste à interdire aux serveurs de DNS du pays
de répondre correctement aux requêtes concernant certains noms de domaine, voire
de renovoyer des fausses adresses IP lorsque les requêtes DNS sont interceptées.
En Chine, par exemple, Facebook.com est interdit, et les DNS chinois vont 
refuser de retourner l'adresse IP du site de Facebook. Cette censure peut
parfois être contournées en recourant à des serveurs DNS situés à
l'extéreur du pays.
```


```{eval} L'exemple d'Alice
L'organisation qui a développé l'application aux
champignons, a obtenu le nom de domaine *champignons.ch* et une adresse IP statique. 
Pour qu'Alice puisse aller sur ce site, son téléphone va envoyer une requête à un
serveur DNS avec le nom de domaine "champignons.ch". Cette requête transitera par
différents serveurs DNS organisés hiérarchiquement jusqu'à ce qu'un serveur DNS
puisse y répondre, et la réponse sera retransmise jusqu'au téléphone d'Alice.
Le téléphone d'Alice a lui aussi reçu une adresse IP dynamique de la part de son opérateur
téléphonique afin que le serveur web puisse lui envoyer la page web du site. 
```
