# Structure du projet

Cette structure partielle reflète les dossier utiles pour une contribution à Modulo. 

_Les autres dossiers et fichiers (non représentés ci-dessous) sont liés sont liés à la configuration globale, aux plugins et ne doivent pas être modifiés._

```
book
|   build
└───src
│   └───appr
|   |   └───algo1
|   |   |   └───media
|   |   |   algo-progs.md
|   |   |   algorithmes.md
|   |   |   conclusion.md
|   |   |   index.md
|   |   |   intro.md
|   |   |   tri.md
|   |   └───algo2
|   |   |   ...
|   |   └───...
|   |   conf.py
|   |   index.rst
│   └───ens
|       └───algo1
|       |  ...
|       └───algo2
|       |   ...
|       └───...
|       conf.py
|       index.rst
|   workspace.code-workspace
```
## Description
Le répertoire `build` contient les fichiers générés automatiquement par Sphinx lors du build.

Le répertoire `src` contient les fichiers sources des deux sites générés : apprendre et enseigner.

Chacun de ces répertoires, `appr` et `ens`, contient l'arborescence des différentes thématiques, ainsi que : 
- conf.py : contenant la configuration du thème, des plugins, etc.
- index.rst : la table des matières, qui permet d'afficher l'arborescence et les fichiers sur la gauche des sites respectifs

Chacune des thématiques contient une structure similaire. Ici, `algo1` contient :
- Différents fichiers markdown faisant office de chapitres (`algo-prog.md`, `algorithmes.md`, etc.)
- Un fichier `index.md`, nécessaire au bon fonctionnement de Sphinx - c'est la porte d'entrée du chapitre
- Un dossier `media`, qui contient les images, sons et autres médias utilisés au sein du chapitre

Enfin, le fichier `workspace.code-workspace` permet d'installer automatiquement les plugins utiles pour une utilisation agréable avec VSCode.

