Architecture de von Neumann
===========================

````{panels}

:img-top: media/JohnvonNeumann-LosAlamos.jpeg

John von Neumann
^^^^^
* **Naissance** 28 décembre 1903 / Budapest 
* **Décès** 8 février 1957 / Washington 
```{dropdown} Bio
:animate: fade-in-slide-down

John von Neumann est un mathématicien et physicien américano-hongrois qui apporte des contributions importantes dans les domaines des mathématiques, de la physique quantique, de l'informatique et de l'économie. Il participe à des projets militaires comme le projet Manhatten (mise au point de la première bombe atomique américaine).
En informatique, on retient son nom pour l'élaboration d'une architecture, publiée en 1945 et qui est encore aujourd'hui la référence dans la conception des ordinateurs. L'idée centrale de son architecture est de stocker dans la mémoire à la fois le programme et les données du programme. Sur ce dernier point, sa proposition est très similaire à celle proposée par Turing.

```

----
:img-top: media/AlanTuring.jpeg

Alan Turing
^^^^^
* **Naissance** 23 juin 1912 Maida Vale (Londres) (Royaume-Uni) 
* **Décès** 	7 juin 1954 (à 41 ans) Wilmslow (Cheshire) (Royaume-Uni) 
```{dropdown} Bio
:animate: fade-in-slide-down
Pendant la Seconde Guerre mondiale, [**Alan Mattison Turing**](https://fr.wikipedia.org/wiki/Alan_Turing Alan Turing) travaille pour les services secrets de l'armée anglaise, en cryptographie. Il est chargé déchiffrer les messages allemands chiffrés avec la machine enigma.
Dans un article de 1936, Alan Turing présente une «machine à programme enregistré dans laquelle le programme et les données ont une égale importance» (Gérard Berry).
```

````
## Contexte historique

````{panels}
:column: col-lg-12 p-2

**Contexte historique**
^^^^
![ENIAC](media/ENIAC.jpeg)

Vous connaissez sans doute tous la formule : 

$
    ax^2 + bx + x
$

Qui correspond entre autre au calcul d'une trajectoire ballistique. La réalité est un peu plus complexe lorsque l'on prend en compte (et c'est nécessaire pour des questions de précision) le vent, les conditions atmosphérique et toute l'aérodynamique de l'objet en vol que ce soit un obus de canon ou un missile.

Ces calculs prennent une dimension stratégique au cours de la deuxième guerre mondiale. Ils sont long et fastidieux. Sur le terrain on utilise des tables pré-calculées, mais ces tables demandent un travail de fournis pour être établies. La mise au point de calculateurs capables d'effectuer automatiquement ces calculs et produire ces tables devient donc aussi un enjeux stratégique.

Dans ce contexte est élaboré l'ENIAC, un calculateur de 30 tonnes qui occupe 167m<sup>2</sup>. Il est opérationel fin 1945, mais ne sera dévoilé au public que le 14 février 1946.

````

````{panels}
:column: col-lg-12 p-2

**The Computers**

^^^^

Rapide historique des 6 femmes, premières programmeuses et informaticiennes qui programmèrent les premières l'ENIAC

https://laughingsquid.com/eniac-project-female-computer-programmers/
https://www.youtube.com/channel/UCBCtLBE97EPz_Fk2FLxTX3Q
http://eniacprogrammers.org/see-the-film/



short bio + photo

----
````

## L'architecture de Von Neumann
L'idée centrale de l'architecture de von Neumann, à l'instar de la machine de Turing, est d'enregistrer les données et le programme dans le même espace mémoire. Cela implique que le programme peut se modifier lui-même comme s'il modifiait des données. L'intention derrière cette possibilité résidait dans la capacité de modifier des adresses pour des branchements (sauts dans l'exécution). Mais ce point ne sera finalement pas ou peu exploité. Par contre cela permet à un programme de se crypter lui-même au cours de son exécution pour le rendre difficile à identifier une fois chargé en mémoire ou, pire encore, pour échapper à une décompilation pour en comprendre le fonctionnement. Cette dernière  particularité a été utilisée par des virus et des vers.

```{admonition} Anecdote
:class: Le ver Internet
Le 2 novembre 1988 est lancé le ver Morris ou ver de Morris ou  ver Internet ou encore Le Ver. Il est considéré comme le premier ver à s'être propagé sur Internet et il a aussi mené à la première condamnation pour fraude informatique.
Robert Tappan Morris avait comme première intention de démontrer le principe de propagation et les vulnérabilités, mais des erreur de programmation ont conduit à une propagation hors de contrôle et à un blocage de nombreux système. On considère de manière très approximative que dix pour cent des soixante mille machines connectées à Internet avait été infectées à l'époque.

```

```{figure} media/Von_Neumann_architecture_fr.svg 
---
height: 400px
width: 400px
name: architecture
---
Architecture de von Neumann.
```

On trouve dans le schémas de la figure {numref}`architecture` les éléments suivants:

**L'ALU ou ULA, c'est-à-dire l'unité logique et arithmétique**

Cette élément est responsable d'effectuer les opérations logiques et arithmétiques.

**L'unité de contrôle**

Cette unité est responsable du séquençage des opérations. C'est en quelque sorte le chef d'orchestre.

**La mémoire**

La mémoire contient le programme et les données.

**Les entrées et sorties**

Les entrées-sorties permettent de communiquer avec les autres périphériques comme la souris, le clavier, l'écran, etc.


:::{admonition} Le modèle Turing
:class: note
Cette vidéo de trente minutes présente le modèle Turing. On découvre ainsi la vie et l'œuvre d'Alan Turing ainsi que les réflexions qui ont abouti à un modèle qui est encore aujourd'hui une référence dans le domaine de l'informatique, mais qui a aussi inspiré de nombreux autres domaines scientifiques. On découvre également le contexte de la seconde guerre mondiale et le rôle crucial qu'a joué Turing dans la résolution de ce conflit.
```{cnrs} pUV9f15n
```
:::

:::{admonition} La machine de Turing réalisée
:class: note
Cette vidéo de sept minutes présente une réalisation en lego de la machine de Turing. Les explications permettent d'en comprendre le fonctionnement.
```{cnrs} 0st7M134
```
:::

```{admonition} Activité
:class: note

[Simulateur de la machine de Turing](https://www.google.com/doodles/alan-turings-100th-birthday)

*Ce simulateur permet de se familiariser avec le concept de programmation et de machine de Turing. Prenez quelques minutes (environ 10') pour résoudre les six enigmes proposées.

```



## Références

https://fr.wikipedia.org/wiki/John_von_Neumann
https://fr.wikipedia.org/wiki/John_von_Neumann#/media/Fichier:Von_Neumann_architecture_fr.svg