(ens:repinfo:redondancehamming)=
# Redondance et code de Hamming

---- 

Une introduction à la redondance et au code de Hamming.

Nous allons voir ce qui peut se passer lorsque des messages numériques sont enregistrés ou envoyés depuis un expéditeur vers un destinataire.

----

```{admonition} Caractéristiques
:class: hint

* Nom : Redondance et code de Hamming
* Durée : 2 périodes
* Thème : Représentation de l'information
* Objectifs d’apprentissage : `à compléter`
* Notions fondamentales : `à compléter`
* Approche pédagogique : Débranchée
* Matériel : Des jetons avec 2 faces différentiables avec un support pour les positionner.
Les activités décrites ci-dessous sont basées sur des messages de 4 bits, le support doit pouvoir en contenir le double, soit 8.
* Niveau : `à compléter`
* Mots-clés : `à compléter`
* Dynamique (groupe / individuel) : `à compléter`
* Taille du groupe : `à compléter`
```

```{dropdown} **Déroulement**

1. {ref}`Contexte<hamming.contexte>` (`durée : à compléter`) de l'activité, avec présentation des enjeux. 

1. {ref}`Envoyer un message<hamming.envoyer>` (`durée : à compléter`), où l'enseignant·e explique le coeur de l'activité.
```

(algo-tri.conclusion)=
## Conclusion

*Durée : 5-10 mn*


(hamming.contexte)=
## Contexte

*Durée : `à compléter`*

On définit 16 mots pouvant former différentes phrases (sujet-verbe ; complément ; adjectif), le tout peut donc être encodé sur 4 bits.  
On sépare la classe en 2 groupes, les expéditeurs et les destinataires, chaque groupe pouvant lui aussi être subdivisé en sous-groupe qui se charge d'une partie de la phrase.  
Les expéditeurs définissent le message, l'encode en positionnant les jetons sur les supports et envoient le message en passant par le prof

(hamming.envoyer)=
## Envoyer un message

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

De cette manière, tous les sujet commence par 00, tous les verbes par 10, etc. On peut donc facilement décider d'introduire une erreur en restant dans la même catégorie (on change 1 des 2 derniers bits) ou pas.

Maintenant, le groupe expéditeur choisi une phrase et l'encode sur 4 support distincts, 1 pour chaque morceau de phrase :

|Mathilde | joue un | roman | anglais |
| :--: | :--: | :--: | :--: |
| 0000 | 1010 | 0111 | 1110 |