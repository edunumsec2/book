(selecteurchien)=
# Sélecteur de chien

---- 

Dans cette activité les élèves construisent une machine permettant de définir la race d'un chien à partir d'un certain nombre de critères le concernant. 

----

```{admonition} Caractéristiques
:class: hint

* Nom : Sélecteur de chien
* Durée : 1 période
* Thème : Architecture des ordinateurs
* Objectifs d’apprentissage : L'objectif de cette activité est de faire se familiriser les élèves aves les portes de base **ET**, **OU** et **NON** en dehors d'un contexte trop «technique» avec un petit exemple suivi qui doit nous dire si oui ou non un chien donné correspond à une liste de critères.
* Notions fondamentales : Portes logiques 
* Approche pédagogique : Travaux pratiques avec le simulateur logique
* Matériel : Simulateur logique en ligne
* Niveau : `à compléter`
* Mots-clés : `à compléter`
* Dynamique (groupe / individuel) : Par groupe
* Taille du groupe : `à compléter`
```

```{dropdown} **Déroulement**

1. {ref}`Introduction<selecteur.introduction>` (`durée : à compléter`) à l'activité à partir de l'histoire du sélecteur de chiens. 

1. {ref}`Mise en place<selecteur.miseenplace>` (`durée : à compléter`) de l'activité et distribution du matériel. 

**Première partie : critères simples**

1. {ref}`Exercice 1<selecteur.exercice1>` (`durée : à compléter`) durant lequel les élèves doivent construire le sélecteur pour qu'il fonctionne comme porte **ET** avec deux critères. 

**Deuxième partie : critères plus compliqués**

1. {ref}`Exercice 2<selecteur.exercice2>` (`durée : à compléter`) durant lequel les élèves doivent construire le sélecteur pour qu'il fonctionne comme porte **ET** avec deux critères. 

**Troisième partie : encodage et décodage des races**

1. {ref}`Exercice 3<selecteur.exercice3>` (`durée : à compléter`) durant lequel les élèves doivent construire le sélecteur pour qu'il fonctionne comme porte **ET** avec deux critères. 



```

(selecteur.introduction)=
## Introduction

*Durée : `à compléter`*

Introduire l'activité aux élèves comme un «sélecteur de chien»: une famille a décidé d'accueillir un chien à la maison et une personne est chargée d'aller le récupérer au chenil, mais il s'agit de trouver le bon chien. On décide donc de construire un circuit logique qui va permettre de sélectionner le bon chien en fonction des critères déterminés par la famille.


(selecteur.miseenplace)=
## Mise en place

*Durée : `à compléter`*

Distribuer aux élèves le fichier JSON qui correspond au circuit logique de base suivant. Leur demander de se rendre sur <https://logic.modulo-info.ch> et de glisser le fichier JSON dans la fenêtre pour charger le circuit de départ. Alternativement, leur distribuer le [lien direct](https://logic.modulo-info.ch/?mode=full&showonly=and,or,xor&data=N4KABGBEBukFxgEwBpxQPYAcAuBneYwkuAFugO4DyAdgDYCeBA2pAIbUAmkyGATt1AAe6fj0jV02SAF0AvqgiQAltWZFM6fAiYBGHQAYeAVn3SxSrgh0AWMdVYBbAKYFIAcSfVsS2gJitfBH15QkgNLTBdAx49U3NLMB0ANjtHFwRIAAUnbykxaACCYLM0SHQAVyltdU1mAGYkwzAADjioCwIdZtTnV0oAaTANct4wAGMncZIlTwBCSFlpEFkgA).

------

## Première partie : critères simples


(selecteur.exercice1)=
### Exercice 1

*Durée : `à compléter`*

Demander aux élèves de développer le circuit de manière à faire en sorte que la sortie «OK pour ce chien» soit allumée (c'est-à-dire, vaille 1) lorsque les 2 entrées sont réglées selon les caractéristiques d'un chien précis et que ce chien est à la fois petit et gentil.
     
     Pour tester un chien donné, ce qu'on fera avec ce circuit est donc de régler les deux entrées selon comment est le chien et vérifier ensuite ce que le circuit fournit sur la sortie: si c'est un 0, le chien ne correspond pas à ces critères; si c'est un 1, il correspond.

```{logic}
:height: 200
:mode: design
:showonly: and,or,xor

{
  "v": 2,
  "opts": {"showOnly": ["and", "or", "xor", "not"]},
  "in": [
    {"pos": [110, 50], "id": 14, "name": "Gentil", "val": 0},
    {"pos": [110, 110], "id": 16, "name": "Petit", "val": 0}
],
  "out": [{"pos": [360, 80], "id": 18, "name": "OK pour ce chien!"}]
}
```

#### Solution

Il faut insérer une porte **ET**.

```{logic}
:height: 160
:mode: tryout

{
  "v": 2,
  "in": [{"pos": [110, 50], "id": 14, "name": "Gentil", "val": 0}, {"pos": [110, 110], "id": 16, "name": "Petit", "val": 0}],
  "out": [{"pos": [360, 80], "id": 18, "name": "OK pour ce chien!"}],
  "gates": [{"type": "AND", "pos": [240, 80], "in": [0, 1], "out": 2}],
  "wires": [[2, 18], [14, 0], [16, 1]]
}
```

------

## Deuxième partie : critères plus compliqués

(selecteur.exercice2)=
### Exercice 2

*Durée : `à compléter`*

1. Les critères sont maintenant devenus plus complexes. Le chien doit remplir les conditions suivantes:
  * Le chien est un chien qui doit être gentil;
  * Le chien ne doit pas baver tout le temps;
  * Il faut soit que ce soit un petit chien, soit que ce soit un labrador.
  
Pour tester, par exemple, si un gentil petit berger allemand qui ne bave pas tout le temps estunchien qui est un candidat à être récupéré, on règlera les entrées suivantes:
  * Gentil: 1 (le chien est gentil)
  * Bave tout le temps: 0 (le chien ne bave pas tout le temps)
  * Petit: 1 (le chien est un petit chien)
  * Labrador: 0 (le chien n'est pas un labrador)

On s'attend dans ce cas à ce que la sortie «OK pour ce chien» vaille 1.

```{logic}
:height: 320
:mode: design
:showonly: and,or,xor,not

{
  "v": 2,
  "in": [
    {"pos": [190, 70], "id": 14, "name": "Gentil", "val": 0},
    {"pos": [190, 130], "id": 15, "name": "Bave tout le temps", "val": 0},
    {"pos": [190, 190], "id": 16, "name": "Petit", "val": 0},
    {"pos": [190, 250], "id": 17, "name": "Labrador", "val": 0}
  ],
  "out": [{"pos": [440, 160], "id": 18, "name": "OK pour ce chien!"}]
}
```

#### Solution

```{logic}
:height: 330
:mode: tryout

{
  "v": 2,
  "in": [
    {"pos": [190, 70], "id": 14, "name": "Gentil", "val": 0},
    {"pos": [190, 130], "id": 15, "name": "Bave tout le temps", "val": 0},
    {"pos": [190, 190], "id": 16, "name": "Petit", "val": 0},
    {"pos": [190, 250], "id": 17, "name": "Labrador", "val": 0}
  ],
  "out": [{"pos": [490, 210], "id": 18, "name": "OK pour ce chien!"}],
  "gates": [
    {"type": "AND", "pos": [420, 210], "in": [0, 1], "out": 2},
    {"type": "OR", "pos": [310, 220], "in": [3, 4], "out": 5},
    {"type": "AND", "pos": [340, 120], "in": [6, 7], "out": 8},
    {"type": "NOT", "pos": [260, 130], "in": 9, "out": 10}
  ],
  "wires": [[2, 18], [8, 0], [14, 6], [15, 9], [10, 7], [16, 3], [17, 4], [5, 1]]
}
```

D'autres solutions sont possibles.

-------

## Troisième partie: encodage et décodage des races

(selecteur.exercice3)=
### Exercice 3

*Durée : `à compléter`*

1. Expliquer aux élèves que l'entrée «labrador» de la partie précédente n'est pas très intéressante, car elle ne permet de modéliser qu'une seule race de chiens. Dans cette deuxième partie, on va se permettre d'utiliser deux bits pour représenter plusieurs races. Faire réfléchir les élèves à ceci: combien de races pourra-t-on au maximum représenter si on se permet d'utiliser deux entrées? La réponse est 4 et non pas 2.

2. Dire aux élèves qu'on va donc s'intéresser, pour simplifier, à uniquement 4 races de chiens: border collie, berger allemand, husky et labrador. On décide de l'encodage suivant:

  | Représentation binaire | Race            |
  | :--------------------: | :---------------|
  | 00                     | border collie   |
  | 01                     | berger allemand |
  | 10                     | husky           |
  | 11                     | labrador         

On a donc maintenant besoin d'un décodeur: en utilisant les 2 bits d'entrées, il s'agit d'avo un circuit qui va activer une seule des quatre sortie, celle correspondant à la race du chi  représentée selon la table ci-dessus.

```{logic}
:height: 390
:mode: design
:showonly: and,or,xor,not

{
  "v": 2,
  "in": [
    {"pos": [120, 80], "orient": "s", "id": 0, "val": 0},
    {"pos": [160, 80], "orient": "s", "id": 1, "name": "Code de la race du chien sur 2 bits", "val": 0}
  ],
  "out": [
    {"pos": [460, 190], "id": 2, "name": "c’est un border collie"},
    {"pos": [460, 310], "id": 3, "name": "c’est un labrador"},
    {"pos": [460, 270], "id": 4, "name": "c’est un husky"},
    {"pos": [460, 230], "id": 5, "name": "c’est un berger allemand"}
  ]
}
```

#### Solution

```{logic}
:height: 390
:mode: tryout

{
  "v": 2,
  "in": [
    {"pos": [120, 80], "orient": "s", "id": 0, "val": 0},
    {"pos": [160, 80], "orient": "s", "id": 1, "name": "Code de la race du chien sur 2 bits", "val": 0}
  ],
  "out": [
    {"pos": [460, 190], "id": 2, "name": "c’est un border collie"},
    {"pos": [460, 310], "id": 3, "name": "c’est un labrador"},
    {"pos": [460, 270], "id": 4, "name": "c’est un husky"},
    {"pos": [460, 230], "id": 5, "name": "c’est un berger allemand"}
  ],
  "gates": [
    {"type": "AND", "pos": [210, 310], "in": [6, 7], "out": 8},
    {"type": "AND", "pos": [360, 270], "in": [9, 10], "out": 11},
    {"type": "NOT", "pos": [230, 110], "in": 12, "out": 13},
    {"type": "NOT", "pos": [230, 160], "in": 14, "out": 15},
    {"type": "AND", "pos": [390, 120], "in": [16, 17], "out": 18},
    {"type": "AND", "pos": [360, 210], "in": [19, 20], "out": 21}
  ],
  "wires": [
    [8, 3],
    [1, 6],
    [0, 7],
    [11, 4],
    [1, 12],
    [0, 14],
    [18, 2],
    [13, 16],
    [15, 17],
    [21, 5],
    [13, 9],
    [0, 10, {"via": [[240, 280]]}],
    [15, 19],
    [1, 20, {"via": [[200, 220]]}]
  ]
}
```

### Quatrième partie: conditions avec décodage

((TODO))
