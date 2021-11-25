# Exercices de systèmes logiques

_**Note:** Ces exercices vont être ventilés sous les thématiques correspondantes sous peu. L'usage de logic.ly, système tiers payant non open source, sera notamment remplacé par des embeds du système que vous avons développé._

>**Contenus abordés**: Portes logiques, loi de De Morgan, systèmes logiques simples, demi-additionneur, additionneur

## Introduction

Dans cette série d'exercices, nous allons survoler quelques éléments des systèmes logiques. Les exercices sont organisés de manière progressive, les premiers ne devraient occuper l'élève que quelques minutes, alors que les derniers constituent de véritables mini-projets.

Nous introduisons également de nouveaux concepts théoriques dans la présentation des exercices. En effet, cet apprentissage par induction[^SPapert] dans la pratique nous paraît profitable pour la culture générale des élèves et les concepts abordés trouveront ainsi des échos dans des études ultérieures.

```{admonition} Rappel
:class: hint
Dans la suite, nous représentons fréquemment Vrai et Faux par **0** et **1** et vice versa sans autre formalisme.

L'avantage des systèmes logiques est que l'on peut souvent énumérer tous les états possibles avec des tables de vérité. La conception de circuits peut donc se faire soit en établissant de telles tables et en les implémentant avec des portes logiques, soit en analysant un cirtuit et retrouvant la table correspondante.

```


## Outils
Voici quelques outils *interactifs* pour simuler des systèmes logiques. Ils sont en principe équivalents. Si dans les exercices qui suivent nous vous recommandons l'usage de l'un ou l'autre, c'est surtout par commodité et pour rendre la réalisation de l'exercice plus facile.


```{admonition} Logic.ly
:class: note
Ce site vous propose un simulateur en ligne très facile à utiliser avec l'essentiel des portes logiques de base.
Il suffit de rendre sur le site [logic.ly](https://logic.ly/demo) pour accéder directement à l'application. 
```

```{admonition} Logidules et simulateur de logidues
:class: note
Les logidules ont été développés dès 1968 par J.-D. Nicoud. Ils ont beaucoup été utilisés pour des exercices et le prototypage de systèmes logiques. Un simulateur a même été créé qui nous permet d'expérimenter ces briques qui ont quasiment disparu.

![logidules](media/Logidules/logidules_registres.jpg)

**Installation**

Pour installer le logiciel, il suffit de le {download}`télécharger <media/Logidules/simul.jar>` et de double clicker sur le fichier .jar

Il faut alors un peu réarranger l'environnement (tirer le diagramme de temps que nous n'utiliserons pas à droite)

```



[^SPapert]: On appuiera cette approche avec les théories du constructionnisme de Seymour Pappert, lui-même dans la continuité du constructivisme de Piaget.
[^hexa]: La notation hexadécimale se fait en base 16 avec les chiffres suivants: {1,2,3,4,5,6,7,8,9,A,B,C,D,E,F}
[^2]:Par Teknad — Travail personnel, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=36768081
[^3]: CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=227770