# Le protocole d'échange de clé de Diffie-Hellman

----

Le but de cette activité est de faire comprendre aux élèves comment deux personnes qui communiquent "en clair" sur un réseau peuvent se mettre d'accord sur un secret commun. C'est l'occasion d'expliquer aux élèves que c'est un point absolument fondamental de nos jours pour la communication sur internet, quand on veut par exemple s'inscrire sur un site web et transmettre un mot de passe de façon sécurisée: a priori, on n'a aucune relation privilégiée avec le site, ni aucun secret partagé en commun. Le protocole d'échange de clé de Diffie-Hellman permet de résoudre ce problème.

Dans ce qui suit, une version simplifiée du protocole est d'abord présentée, en lien avec l'activité proposée. Puis des indications sont données sur le fonctionnement du vrai protocole.

----

```{admonition} Titre de l'activité
:class: hint
* Thème : Réseaux, communication, sécurité
* Niveau : moyen
* Durée : 45 minutes
* Objectifs pédagogiques : comprendre le principe de la cryptographie à clé publique, et plus précisément le protocole d'échange de clé de Diffie-Hellman (ou du moins une version simplifiée de celui-ci)
* Modalité : débranché
* Matériel : papier/crayon, deux élèves doivent avoir une calculatrice
* Prérequis : rien
* Taille du groupe : classe entière
```

## Déroulement


| Étape                                   | Durée | 
|---------------------------------------|------ |
| {ref}`Introduction<diffie-hellman.intro>`| 5 min  |
| {ref}`Jeu<diffie-hellman.jeu>`| 20 min  |
| {ref}`Développements<diffie-hellman.developpements>`| 20 min   |



(diffie-hellman.intro)=
## Introduction

*Durée : 5 minutes*

En guise d'introduction, poser la question suivante aux élèves : "Pensez-vous qu'il soit possible pour deux personnes d'établir un secret commun en communiquant entre elles, alors que tout le monde écoute absolument tout ce qu'elles se disent ?"

La première réponse à cette question est "bien sûr que non !"

Mais de façon surprenante, la réponse peut devenir "oui, en pratique", si on dispose d'opérations dites "à sens unique", c'est-à-dire des opérations qui sont elles-mêmes faciles à effectuer, mais qui sont en même temps *très* difficiles à inverser ! C'est ce que vous allez voir maintenant.


(diffie-hellman.jeu)=
## Jeu

*Durée : 20 minutes*

Demander à trois volontaires dans la classe de jouer les rôles d'Alice, Bob et Eve. Le but pour Alice et Bob est de se mettre d'accord sur un secret commun, qu'Eve ne sera pas capable de retrouver, tout ceci sans qu'Alice et Bob ne s'échangent des informations en se transmettant des SMS, des petits bouts de papiers ou encore en se chuchotant à l'oreille, mais seulement en parlant à haute et intelligible voix, de façon à ce que tout le monde dans la classe puisse entendre ce qu'ils se disent.

Pour rester très concret, supposons que l'opération facile à réaliser et difficile à inverser soit la multiplication. Ce n'est bien sûr pas le cas en réalité, mais on peut en tout cas s'accorder sur le fait qu'effectuer une division est plus difficile que d'effectuer une multiplication (en se référant par exemple aux souvenirs que les élèves ont de l'école primaire).

Le protocole est le suivant:

1. Demander à Alice et Bob de choisir chacun.e de leur côté un nombre à trois chiffres (disons $A$ et $B$), qu'ils gardent secret, et aussi de se mettre d'accord publiquement sur un troisième nombre à trois chiffres, $C$, qui sera donc connu de tout le monde.

2. Demander à Alice de multiplier son nombre secret $A$ par le nombre public $C$ et de communiquer le résultat à tout le monde.

3. Demander à Bob de multiplier son nombre secret $B$ par le nombre public $C$ et de communiquer le résultat à tout le monde.

4. Demander à Alice de multiplier le résultat communiqué par Bob par son nombre secret $A$ (et de garder le résultat secret).

5. Demander à Bob de multiplier le résultat communiqué par Alice par son nombre secret $B$ (et de garder le résultat secret).

A ce stade, révéler qu'Alice et Bob ont en commun un nombre $A \cdot B \cdot C$ d'environ neuf chiffres qu'aucune autre personne dans la classe (et en particulier Eve) n'est capable de retrouver sans effectuer de division: voilà donc leur secret commun!

````{admonition} Remarque
:class: hint

Les nombres secrets $A$ et $B$ choisis au départ par Alice et Bob restent quant à eux complètement secrets: Bob ne peut pas retrouver $A$, ni Alice retrouver $B$ (si on suppose toujours que personne ne sait effectuer de division).

````

### Exemple de déroulement

1. Alice choisit le nombre $A=597$; Bob choisit le nombre $B=472$; et les deux se mettent d'accord sur le nombre $C=345$.

2. Alice calcule $A \cdot C=579 \cdot 345 = 205'965$ et communique publiquement le résultat.

3. Bob calcule $B \cdot C=472 \cdot 345 = 162'840$ et communique publiquement le résultat.

4. Alice calcule de son côté $579 \cdot 162'840 = 97'215'480$.

5. Bob calcule de son côté $472 \cdot 205'965 = 97'215'480$.

Alice et Bob ont donc bien trouvé le même résultat $97'215'480$, qui sera leur secret commun. Mais est-on vraiment bien sûr qu'Eve ne peut pas calculer ce nombre? Elle connaît le nombre $C=345$, ainsi que les deux nombres $205'965$ et $162'840$. Sans faire de division, il est effectivement impossible de retrouver à partir de ces trois nombres le nombre commun $97'215'480$ calculé par Alice et Bob. De même, les nombres $A$ et $B$ restent aussi secrets.

````{admonition} En couleurs
:class: hint

Il est également possible d'expliquer ce protocole avec des pots de peinture! Ici, l'opération facile à réaliser et difficile à inverser est simplement le mélange des couleurs. 

```{figure} media/diffie-hellman.png
---
alt: Protocole de Diffie-Hellman
width: 100%
---
```
````

(diffie-hellman.developpements)=
## Développements

*Durée : 20 minutes*

Cette deuxième partie revient plus à la forme classique d'un cours ex-cathedra. L'enseignant·e est libre de choisir quels points aborder plus précisément avec les élèves.

### Le vrai protocole de Diffie-Hellman

Pour trouver une vraie opération difficile à inverser, on a besoin de l'arithmétique modulaire: plus précisément, de l'opération d'*exponentiation modulaire*, qui consiste, étant donnés un nombre premier $P$ et deux nombres $A$ et $B$, chacun compris entre $1$ et $P-1$, à calculer:

$A^B (\text{mod }P)$, c'est-à-dire le reste de la division de $A^B$ par $P$

On peut montrer d'une part qu'il existe une manière efficace d'effectuer cette opération, mais que l'inverser est très difficile. Qu'est-ce que ça veut dire concrètement? Si on connaît les nombres $A$, $C$ et $P$ tels que

$A^B (\text{mod }P) = C$

alors il est très difficile de retrouver la valeur de l'exposant $B$, et ceci d'autant plus que le nombre premier $P$ est grand. Ce problème s'appelle le problème du *logarithme discret* et fascine les informaticien.ne.s depuis de nombreuses années... Il est bien sûr toujours possible de le résoudre en testant toutes les valeurs possibles de $B$ entre $1$ et $P-1$, mais si $P$ est vraiment un grand nombre, le temps nécessaire pour résoudre ce problème de cette manière peut vite dépasser l'âge de l'univers! Ainsi, tant qu'on n'aura pas trouvé d'autre méthode plus efficace pour résoudre ce problème (et donc inverser facilement l'opération d'exponentiation modulaire), le protocole de Diffie-Hellman restera une valeur sûre pour partager un secret (pour plus de détails sur ce sujet, voir [cette vidéo](https://tube.switch.ch/videos/bYYLrqs9fd)).

### Un secret partagé, c'est bien, mais qu'en faire?

Une fois établi un secret commun entre Alice et Bob dans le réseau, il existe de nombreuses façons d'utiliser celui-ci pour chiffrer leur conversation de bout en bout. De manière générique, on peut dire qu'Alice combine ce secret avec le message qu'elle désire envoyer, obtenant ainsi un message chiffré, qu'elle envoie à Bob. Puis Bob réutilise à son tour le secret partagé pour retrouver le message envoyé. Là aussi, il importe de faire en sorte que si Eve lit le message chiffré, elle ne soit pas capable de retrouver le message d'origine (ou seulement au prix d'efforts gigantesques, comme évoqué ci-dessus pour le problème du logarithme discret). Les possibilités de chiffrement sont très nombreuses; citons en particulier la clé à usage unique, le système DES (pour "Data Encryption Standard") et le système AES (pour "Advanced Encryption Standard"), qui a succédé au précédent et est toujours en vigueur de nos jours (pour plus de détails sur ce sujet, voir [cette vidéo](https://tube.switch.ch/videos/N6rj7ZDhXa)).

A noter qu'il existe également d'autres protocoles de cryptographie à clé publique qui permettent de directement envoyer un message chiffré en utilisant le même principe de chiffrement à clé publique: ce sont par exemple le protocole d'El Gamal et le protocole RSA.

## Conclusion

Contre toute attente, il est donc possible de nos jours de partager des secrets sur internet, sans devoir échanger par un canal secret au préalable de grands fichiers de données, comme c'était encore le cas pendant la seconde guerre mondiale, où les soldats allemands transportaient de grands cahiers contenant les codes de la machine Enigma pour communiquer entre eux.

Paradoxalement, cette possibilité nous est offerte car il existe d'autre part des problèmes difficiles que *nous ne savons pas* encore résoudre de manière efficace. On murmure que des ordinateurs quantiques pourraient un jour y parvenir, mais bien malin qui peut prédire quand ceci se produira...