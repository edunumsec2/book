(ens:repinfo:redondancehamming)=
# Redondance et code de Hamming

---- 

Une introduction à la redondance et au code de Hamming.

Nous allons voir ce qui peut se passer lorsque des messages numériques sont enregistrés ou envoyés depuis un expéditeur vers un destinataire.

----

```{admonition} Caractéristiques
:class: hint

* **Thème** : Représentation de l'information 
* **Niveau** : Facile 
* **Durée** : 2 périodes
* **Objectifs pédagogiques** : `à compléter`
* **Notions fondamentales** : `à compléter`
* **Modalité** : Débranchée
* Matériel : Des jetons avec 2 faces différentiables avec un support pour les positionner.
Les activités décrites ci-dessous sont basées sur des messages de 4 bits, le support doit pouvoir en contenir le double, soit 8.
* **Prérequis** : Représentation binaire
```

| Étapes                                   | Durée          | Phase de l'activité   | 
|---------------------------------------|------|---------------------|
| {ref}`Contexte<hamming.contexte>` | 10 min | Mise en situation |
| {ref}`Envoyer un message<hamming.envoyer>` | 15 min | Enseignement / Apprentissage |
| {ref}`Sécuriser la transmission<hamming.securiser>` | 30 min | Enseignement / Apprentissage |
| {ref}`Codage de Hamming<hamming.hamming>` | 20 min | Enseignement / Apprentissage |

(hamming.contexte)=
## Contexte

*Durée : `à compléter`*

*Objectif : Mettre en place le contexte et le principe de l'activité.*

On définit 16 mots pouvant former différentes phrases (sujet-verbe ; complément ; adjectif), le tout peut donc être encodé sur 4 bits.  
On sépare la classe en 2 groupes, les expéditeurs et les destinataires, chaque groupe pouvant lui aussi être subdivisé en sous-groupe qui se charge d'une partie de la phrase.  
Les expéditeurs définissent le message, l'encode en positionnant les jetons sur les supports et envoient le message en passant par le prof

(hamming.envoyer)=
## Envoyer un message

*Durée : `à compléter`*

*Objectif : `à compléter`*

Commencer par définir les mots qui vont être utilisés pour écrire les messages, on peut par exemple utiliser 4 phrases ayant la même structure.
Ainsi, il sera possible de générer des erreurs qui rendront la phrase transmise incompréhensible, ou pas.

Exemple :
1. Mathilde mange des tacos salés
2. Dan joue du violon anglais
3. Anastasia imagine un roman épique
4. Tim écrit un programme compliqué

Il faut ensuite associer un code binaire à chaque mot/morceau de phrase. Il peut être intéressant de la faire de manière réfléchie pour pouvoir maîtriser le résultat de l'erreur introduite.

| |00 | 10 | 01 | 11 |
|:---| :--: | :--: | :--: | :--: |
| 00 | Mathilde | Dan | Anastasia | Tim |
| 10 | mange | joue | écrit | imagine |
| 01 | des nems | du violon | un programme | un roman |
| 11 | végétarien | anglais | compliqué | épique |

De cette manière, tous les sujets commencent par 00, tous les verbes par 10, etc. On peut donc facilement décider d'introduire une erreur en restant dans la même catégorie (on change 1 des 2 derniers bits) ou pas.

Maintenant, le groupe expéditeur choisi une phrase et l'encode sur 4 supports distincts, 1 pour chaque morceau de phrase :

|Mathilde | joue un | roman | anglais |
| :--: | :--: | :--: | :--: |
| 0000 | 1010 | 0111 | 1110 |

Pour envoyer le message aux destinataires, les expéditeurs doivent le donner à l'enseignant (= rôle du canal de transmission) qui le transmet aux destinataires.  
Lors de la *transmission*, l'enseignant peut introduire des erreurs dans le message, simulant ainsi les incidents impondérables du canal de transmission. 
Au maximum, l'enseignant peut changer 1 bit par mot (c.-à-d. 1 bit sur 4).

Ainsi la phrase Mathilde joue un roman anglais peut facilement devenir

|Dan | joue | du violon | anglais |
| :--: | :--: | :--: | :--: |
| 0010 | 1010 | 0110 | 1110 |

ou encore 

|Des nems | anglais | Tim | végétarien |
| :--: | :--: | :--: | :--: |
| 0100 | 1110 | 0011 | 1100 |

Les destinataires décodent le message et **avant** de connaitre le message original, doivent estimer s'il y a eu ou pas un problème lors de la transmission.  

Un humain pourra se douter d'une erreur dans le second cas, mais pas dans le premier. 
Une machine, quant à elle, ne sait pas faire de différence entre les 2 cas et n'a pas de moyen pour détecter un problème lors de la transmission.

(hamming.securiser)=
## Sécuriser la transmission

*Durée : `à compléter`*

*Objectif : Trouver un moyen pour que le destinataire puisse détecter un problème lors de la transmission.*

Il s'agit ici de guider les élèves pour qu'ils suggèrent et testent différentes solutions permettant aux expéditeurs d'envoyer un message pour lequel les destinataires seront capable de détecter si le message reçu à été altéré durant la transmission.  
Bien entendu, la solution de sécurisation ne devrait pas prendre plus de bits que le message en lui-même.

Pour chaque solution proposée par les élèves, l'idée est de procéder toujours de la même façon :

1. Explicitation de la solution proposée
2. Mise en œuvre par les expéditeurs
3. Transmission du message
4. Décodage du message par les destinataires
5. Analyse
    - le message reçu est-il identique à celui expédié ?
    - dans le cas d'une erreur de transmission, a-t-elle été détectée ?
    - Avantages et inconvénients de la solution
    - comment peut-on l'améliorer ?

Compte tenu de l'objectif, il n'y a, dans ce cas, que 4 possibilités : ajouter x bits au message ou x $\in$ \[1,4\]

### Redondance (+4 bits)

On duplique le message et on transmet le tout, soit :
* en séquence : $0110 \rightarrow 01100110$
* entrelacé : $0110 \rightarrow 00111100$

Les 2 approches sont identiques et cette solution permet effectivement de détecter si le message a été altéré.  
Par contre, on ne peut pas savoir lequel des 2 messages est le bon et le *coût* est élevé, deux fois plus de bits que le message original.

### Bit de parité (+1 bit)

On fait la somme du nombre de bits à 1 dans le message original puis on donne la valeur 0 au bit de parité lorsque cette somme est paire et la valeur 1 lorsque cette somme est impaire. On notera que, de cette façon, la somme des 5 bits est toujours paire.

Le bit de parité est habituellement placé à la position de poids le plus faible :
* $0110 \rightarrow 01100$
* $1110 \rightarrow 11101$

Comme pour la redondance, on peut uniquement détecter s'il y a eu erreur de transmission, mais pour un coût bien plus raisonnable.
De plus, si l'erreur (on reste toujours dans le cas ou 1 bit maximum peut être modifié) se situe sur le bit de parité, celle-ci est aussi détectée. Dans ce cas, on sait que le message est en fait correct.
Sinon, pour obtenir le message correct, il faut passer par une nouvelle transmission...

Serait-il possible de pouvoir détecter s'il y a une erreur et la corriger, c.-à-d. savoir quel bit a été modifié ?

### Bits de position (+2 bits)

Les 4 positions des bits du message peuvent être encodés sur 2 bits. À l'instar de l'encodage utilisé pour résoudre {ref}`le problème des bouteilles empoisonnées<magiebinaire.mobiliser>`, on pourrait calculer la parité des bits dont la représentation binaire de leur position ont 1 bit en commun.  
Soient A et B les 2 bits de parités à ajouter au message de 4 bits avec les positions suivantes :

|Position des bits | 0 | 1 | 2 | 3 |
| :--: | :--: | :--: | :--: | :--: |
|Représentation binaire des positions| 00 | 01 | 10 | 11 |

Ainsi A sera le bit de parité pour les positions 1 et 3 tandis que B sera le bit de parité pour les positions 2 et 3.

Permet de détecter et corriger des erreurs sur les bits aux positions 1 à 3, mais pas sur la position 0, ni sur les bits de parité.

Par exemple, considérons le message initial $0010$ qui devient $001001$ et les 6 différents messages altérés qui peuvent être reçus :
1. $101001$ : le bit à la position 0 a été modifié, l'erreur n'est pas détectée
2. $011001$ : le bit à la position 1 a été modifié, le premier bit de parité (A) est incorrect tandis que le second (B) est juste. Par conséquent, l'erreur se trouve sur le bit de position 1 et peut être corrigée.
3. $000001$ : le bit à la position 2 a été modifié, le bit de parité A est correct tandis que B ne l'est pas. Par conséquent, l'erreur se trouve sur le bit de position 2 et peut être corrigée.
4. $001101$ : le bit à la position 3 a été modifié, le bit de parité A est incorrect ainsi que B. Par conséquent, l'erreur se trouve sur le bit de position 3 et peut être corrigée.
5. $001011$ : le bit de parité A a été modifié, le bit de parité A est incorrect tandis que B est juste. On se retrouve dans la même situation qu'au pt. 2, par conséquent, on conclue que l'erreur se trouve sur le bit de position 1 ce qui est faux.
6. $001000$ : le bit de parité B a été modifié, le bit de parité A est correct tandis que B ne l'est pas. On se retrouve dans la même situation qu'au pt. 3, par conséquent, on conclue que l'erreur se trouve sur le bit de position 2 ce qui est faux.

Dans ce cas les erreurs sur les bits aux positions 1 à 3 sont détectées et peuvent être corrigées.  
Lorsque l'erreur advient sur le bit de position 0, elle n'est pas détectée.  
Enfin, si l'erreur se trouve sur l'un des 2 bits de parité, cette erreur engendrera une correction sur un des bits des positions 1 à 3 qui n'avaient pas été altérés.

(hamming.hamming)=
### Codage de Hamming (+3 bits)

To Do