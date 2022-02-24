# 4. Redondance et code de Hamming

## 4.1. Introduction

Une introduction à la redondance et au code de Hamming.

## 4.2. Objectifs du cours


## 4.3. Durée

2 périodes de cours en classe (théorie et exercices *déconnectés*).

## 4.4. Matériel requis

Des jetons avec 2 faces différentiables avec un support pour les positionner.
Les activités décrites ci-dessous sont basées sur des messages de 4 bits, le support doit pouvoir en contenir le double, soit 8.

## 4.5. Accroche

Nous allons voir ce qui peut se passer lorsque des messages numériques sont enregistrés ou envoyés depuis un expéditeur vers un destinataire.

## 4.6. Marche à suivre

### 4.6.1. Étape 1 - Envoyer un message

#### Objectif : Mettre en place le contexte et le principe de l'activité

On définit 16 mots pouvant former différentes phrases (sujet-verbe ; complément ; adjectif), le tout peut donc être encodé sur 4 bits.  
On sépare la classe en 2 groupes, les expéditeurs et les destinataires, chaque groupe pouvant lui aussi être subdivisé en sous-groupe qui se charge d'une partie de la phrase.  
Les expéditeurs définissent le message, l'encode en positionnant les jetons sur les supports et envoient le message en passant par le prof


#### Déroulement

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