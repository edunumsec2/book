# 2. De Turing à Von Neumann

````{panels}

:img-top: media/JohnvonNeumann-LosAlamos.jpeg

John von Neumann
^^^^^
* ***1903-1957*** 🇭🇺 🇺🇸
```{dropdown} Bio
:animate: fade-in-slide-down

John von Neumann est un mathématicien et physicien américano-hongrois qui a apporté des contributions importantes dans les domaines des mathématiques, de la physique quantique, de l'informatique et de l'économie. Il participa à des projets militaires comme le projet Manhattan, sur la mise au point de la première bombe atomique américaine.
En informatique, on retient son nom pour l'élaboration d'une architecture, publiée en 1945 et qui est encore aujourd'hui la référence dans la conception des ordinateurs. L'idée centrale de son architecture est de stocker dans la mémoire à la fois le programme et les données du programme. Sur ce dernier point, sa proposition est très similaire à celle proposée par Turing.

```

----
:img-top: media/AlanTuring.jpeg

Alan Turing
^^^^^
* ***1912-1954*** 🇬🇧 
```{dropdown} Bio
:animate: fade-in-slide-down
Pendant la Seconde Guerre mondiale, [**Alan Mattison Turing**](https://fr.wikipedia.org/wiki/Alan_Turing Alan Turing) travaille pour les services secrets de l'armée anglaise, en cryptographie. Il est chargé de déchiffrer les messages allemands chiffrés avec la machine Enigma.
Dans un article de 1936, Alan Turing présente une «machine à programme enregistré dans laquelle le programme et les données ont une égale importance» (Gérard Berry).
```

````
## Contexte historique

````{panels}
:column: col-lg-12 p-2

**Contexte historique**
^^^^
L'ENIAC

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
Le 2 novembre 1988 est lancé le ver Morris ou ver de Morris ou ver Internet ou encore Le Ver. Il est considéré comme le premier ver à s'être propagé sur Internet et il a aussi mené à la première condamnation pour fraude informatique.
Robert Tappan Morris avait comme première intention de démontrer le principe de propagation et les vulnérabilités, mais des erreur de programmation ont conduit à une propagation hors de contrôle et à un blocage de nombreux système. On considère de manière très approximative que dix pour cent des soixante mille machines connectées à Internet avait été infectées à l'époque.

```


```{image} media/Von_Neumann_architecture_fr.svg
:width: 700
:height: 400
```
Architecture de von Neumann

<br> <br>

On trouve dans le schéma de cette figure les éléments suivants:

**L'ALU ou ULA, c'est-à-dire l'unité logique et arithmétique**: cet élément effectue les opérations logiques et arithmétiques.

**L'unité de contrôle (UC)**: cette unité est responsable du séquençage des opérations. C'est en quelque sorte le chef d'orchestre.

**La mémoire**: la mémoire contient le programme et les données.

**Les entrées et sorties (E/S ou I/O en anglais)**: les entrées-sorties permettent de communiquer avec les autres périphériques comme la souris, le clavier, l'écran, etc.


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

Ce simulateur permet de se familiariser avec le concept de programmation et de machine de Turing. Prenez quelques minutes (environ 10') pour résoudre les six enigmes proposées.

```



### Références

https://fr.wikipedia.org/wiki/John_von_Neumann
https://fr.wikipedia.org/wiki/John_von_Neumann#/media/Fichier:Von_Neumann_architecture_fr.svg