# Charte rédactionnelle 

Ce document regroupe un ensemble de recommandations concernant la rédaction des parties  «enseigner» et «apprendre» du support pour l'enseignement de l'informatique au gymnase *modulo* https://modulo-info.ch. 

## Table des matières

- [Syntaxe MySt](#syntaxe-myst)
- [Apprendre](#apprendre)
    - [Niveaux de titres](#niveaux-de-titres)
    - [Accueil des chapitres](#accueil-des-chapitres)
    - [Utilisation des encarts](#utilisation-des-encarts)
    - [Insertion des figures](#insertion-des-figures)
    - [Insertion des tableaux](#insertion-des-tableaux)
    - [Insertion des cellules codeplay](#insertion-des-cellules-codeplay)
    - [Listes numérotées](#listes-numérotées)
    - [Exercices inline](#exercices-inline)
    - [Exercices fin de cours](#exercices-fin-de-cours)
    - [Hiérarchisation](#hiérarchisation)
    - [Titres et niveaux de titre](#titres-et-niveaux-de-titres)
    - [Formulation](#formulation)
- [Enseigner](#eneigner)
- [Autres](#autres)   
    - [Nomenclature fichiers](#nomenclature-fichiers)
    - [Glossaire](#glossaire)

# Syntaxe MySt et ReST

La syntaxe utilisée pour écrire les fichiers sources est détaillée [ici](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html).

Certains fichiers sources contiennent aussi du [rST](https://docutils.sourceforge.io/docs/user/rst/quickref.html).

# Apprendre 

## Niveaux de titres

- Chapitre (e.g "Programmation I")
- Sous-chapitre (e.g "Dessiner - `forward`")
- Section (e.g "Exercices")
- Sous-section (e.g "Rectangle")

*Note : les chapitres sont déclarés dans un fichier appelé "index.rst" à la source de la partie "apprendre" et "enseigner" (e.g src/appr/index.rst) respectivement.* 

*Les sous-chapitres sont déclarés dans le fichier "index.md" de chaque thématique (e.g src/appr/algo1/index.md) et correspondent au nom du fichier source.* 

## Accueil des chapitres

L'accueil des chapitres, accessible en cliquant sur le nom du chapitre dans le menu de navigation à gauche de la page web (e.g "Représentation de l'information") amène à une page d'accueil consitutée de : 

- Intro du chapitre
- Objectifs
- Personnages-clé

## Utilisation des encarts

Les encarts suivants sont disponibles.

### Encarts "internes à la matière du cours"

- Aller plus loin : contenus qui suggèrent des prolongements. 

- Mini-activité : contenus qui servent "d'exercices-exemples", c'est à dire pas une série d'exercices mais plutôt l'illustration d'un concept technique par un micro-exercice. On pourrait appeler ça des "micro-activités".

- Pourquoi est-ce important : contenus qui soulignent l'importance de telle ou telle notion. 

- Anecdote : contenus qui illustrent un concept par une anecdote (historique, politique, faits-divers, liens avec l'actualité, etc.).

- Le saviez-vous : contenus qui apportent une information inattendue en lien avec le sujet. 

- À retenir : contenus fondamentaux à retenir impérativement.

- Matière à réfléchir : contenus importants, qui pourraient ouvrir d'éventuels débats.

- Ai-je compris : contenus qui servent à résumer les points importants de la leçon en guise d'auto-évaluation pour l'élève. 

### Encarts "externes à la matière du cours"

- Important : contenus qui décrivent un aspect technique, qui n'a pas de rapport avec la matière directement mais avec l'environnement, la plateforme, ou du matériel nécessaire pour suivre un cours une activité.  

- Avertissement : contenus liés à des avertissements de maintenance du site, des problèmes rencontrés, ou tout autre mise en garde importante. 

Les règles à respecter pour leur utilisation sont les suivantes : 

- Ne pas commencer une page de cours par un encart (sauf en cas d'avertissement lié à la maintenance, mise à jour, etc. donc encarts "externes à la matière du cours")
- Ne pas nester des encarts à l'intérieur d'encarts.

## Insertion des figures 

Les figures (Fig.), fichiers sons ou vidéos seront désignés par leur numérotation simple suivie d’un  titre en dessous, aligné à gauche. 

On évite une succession de figures ou vidéos illustrant des idées différentes, en intercalant  systématiquement du texte. 

On numérote les figures dans le texte selon le format Fig.1 sans évoquer le chapitre, finalement  inutile et lourd, nécessitant de rentrer «à la main» ce paramètre et supprimant de fait l’utilité de  l’automaticité de la numérotation de figure présente dans Sphinx. 

Il est possible d’accompagner l’objet (image, son, vidéo) d'une légende descriptive. La légende a des retraits gauche et droit pour éviter qu’on la confonde avec le corps du texte.

## Insertion des tableaux

Les formats de tableaux sont libres. Tout comme les figures, ils seront numérotés et désignés (Tab.)  simplement par un titre en dessous, éventuellement une légende descriptive, aligné à gauche. 

## Insertion de codeplay

L’utilisation de l’outil codeplay est fortement recommandée afin d'illustrer de façon interactive une notion technique. 

## Listes numérotées

Elles seront déroulées selon le modèle-exemple suivant : 
1. Déterminer le coefficient maximum dont la valeur est plus petite que l’entier à convertir. 
2. Le bit associé à ce coefficient est 1. 
3. Soustraire la valeur de ce coefficient à l’entier à convertir pour obtenir le nouveau nombre à convertir. 3. Recommencer à l’étape 1 tant que le nombre est différent de 0. 
4. En commençant par le plus grand coefficient utilisé, le nombre binaire correspondant est composé de  la suite des bits où des 0 représentent les coefficients non utilisés. 

## Exercices inline

Des exercices, généralement corrigés, peuvent apparaître directement dans les chapitres, à l'intérieur du corps de texte. Il est  souhaitable de parler d’exercices applicatifs, de les désigner comme tels et d’adopter une  numérotation propre. Pour la nomenclature de ces exercices intérieurs au cours le choix s’est porté sur «Mini-activité». 

## Exercices fin de cours

Des exercices en fin de cours sont proposés à titre d'auto-contrôle pour les élèves concernant les notions apprises. Les exercices sont organisées implicitement selon une difficulté croissante. Le mode branché/débranché est indiqué. Chaque exercice est illustré par un titre, une indication, et  bien entendu son numéro. Le numéro reprend le titre du chapitre, puis le numéro de l’exercice lui même. 

Par exemple le 2ème exercice du chapitre 1, dans la partie exercice, sera nommé : Exercice  1.2. 

# Enseigner


