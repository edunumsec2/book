# Informatique au Gymnase / Pilote

![chatbot](https://user-images.githubusercontent.com/73947555/117774857-301d3580-b23a-11eb-9657-2eeebb19fde3.png)


## Introduction

Les ressources pour l'enseignement de la discipline obligatoire *Informatique* au niveau secondaire II ont été produites par le groupe de travail DGEP, EPFL, HEP, UNIL, dans le cadre de l’introduction de la discipline obligatoire en informatique qui devrait se faire à la rentrée 2022, dans le canton de Vaud. Leur objectif est la mise à disposition de contenus théoriques, de séries d'exercices, et d'idées d'activités pour les enseignantes et enseignants de ladite matière au Gymnase. 

En accord avec la DGEP, nous mettons déjà une partie de ce matériel à disposition des enseignants vaudois en informatique pour un enseignement pilote.

Les ressources pédagogiques sont accessibles via un [site web](https://edunumsec2.ch), elles peuvent être utilisées telles quelles ou modifiées via un [dépôt GitHub](https://github.com/edunumsec2/book).

Merci de bien vouloir vous intégrer dans les processus d’enquêtes qui nous permettront de recueillir des données de manière scientifique afin qu’elles soient pertinentes pour mieux comprendre ce qui marche ou non, pour qui et pourquoi. En aucun cas vos capacités à enseigner ne feront l’objet d’analyses. Toutes les données sont confidentielles et sont destinées soit à vous, soit au responsable de la thématique, avec votre accord. En dernier lieu, les analyses se feront en termes de masse pour de grandes cohortes mais toujours avec votre accord.

## Table des matières

---

- [Introduction](#introduction)
- [Utilisation](#utilisation)
- [Installation](#installation)
  - [Installation recommandée](#installation-recommandée)
  - [Installation Ubuntu 20.04 LTS](#installation-ubuntu-20.04-lts)
  - [Références](#références)
  - [Build](#build)
- [Exemples d'utilisation des ressources](#exemples-dutilisation-des-ressources)
  - [Utilisation en ligne](#utilisation-en-ligne)
  - [Modifications indépendantes](#modifications-indépendantes)
  - [Participation au développement](#participation-au-développement)
  

## Utilisation

L'utilisation **standard** des ressources ne requiert pas d'installation particulière et peut-être effectuée immédiatement à l'adresse https://edunumsec2.ch. 

Dans le cadre du projet pilote, nous vous saurions gré de suivre le protocole minimal décrit ci-dessous :  

1. Participer aux sondages suivants (30mn) : 
    - [Choix entre TigerJython et Micro:Bit](https://fr.surveymonkey.com/r/programPR)
    - [Besoin en termes de Formations](https://fr.surveymonkey.com/r/27QW723)
    - [Sondage profil enseignant](https://fr.surveymonkey.com/r/J3B3J8D)
    - [Sondage en amont de l'enseignement](https://www.surveymonkey.com/r/gymprescinf)

2. Ecrire à nathalie.farenc@epfl.ch pour la tenir informée du début et de la fin d'un cours donné sur l'un ou l'autre des sujets du Plan d'études.
3. Signaler tout défaut éventuel des ressources à nathalie.farenc@epfl.ch ou directement à la personne en charge du chapitre en question dont vous trouverez l'adresse sous [comité de rédaction](#comité-de-rédaction).

L'utilisation **avancée** des ressources comprend, en outre, les étapes suivantes : 

4. Utiliser les fonctionnalités de GitHub telles que [issues](https://github.com/edunumsec2/book/issues) et [discussions](https://github.com/edunumsec2/book/discussions) pour signaler des améliorations potentielles. 
5. Proposer et rédiger des modifications via la création d'une [branche](https://github.com/edunumsec2/book/branches). 
6. Forker le dépôt pour en faire un clône indépendant via le mécanisme de [fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo). 
7. Utiliser l'environnement Jupyter-book pour tester ses améliorations en local sur sa propre machine. 

## Installation 

Les fonctionnalités décrites aux points 4 à 6 ne nécessitent pas d'installation particulière et sont inhérentes à GitHub. Pour un descriptif détaillé de leur utilisation, se référer au WIKI (en construction). Une explication allégée de leur utilisation est disponible directement dans les services en question : [issues](https://github.com/edunumsec2/book/issues) et [discussions](https://github.com/edunumsec2/book/discussions). 

Pour ceux qui souhaitent utiliser l'environnement Jupyter-book pour tester des contenus et participer au développement, la marche à suivre est la suivante : 

### Installation recommandée

 1. Seulement si pas encore présent: [installer git](https://git-scm.com/downloads) sur votre machine
   * Sous Windows, il faut activer les symlinks de git. Après l'installation de git, éditer le fichier `C:\ProgramData\Git\config` et y insérer:

     ```
     [core]
         symlinks = true
     ```

     ([Plus d'info](https://www.joshkel.com/2018/01/18/symlinks-in-windows/) si ça ne marche pas sous Windows.)

 2. Cloner ce repository git
    * Soit depuis un terminal avec les commandes directes de `git`
    * Soit avec application [GitHub Desktop](https://desktop.github.com)

 3. Installer une version récente (3.x, x ≥ 8) de **Python**
    * [Téléchargement](https://www.python.org/downloads/)
      * Pour macOS, un excellent tuto si l'installation pose problème (mais il faut bien lire la deuxième partie): [Tuto](https://opensource.com/article/19/5/python-3-default-mac#what-to-do)<sup>1</sup>

 4. Installer [Jupyter Book](https://jupyterbook.org).  Ceci **met aussi à jour** Jupyter Book lorsqu'une nouvelle version est disponible. Si l'équipe de rédaction utilise de nouvelles fonctions de Jupyter Book, il faut faire retourner ceci pour l'obtenir.
    * Avec Python 3.9:
      ```bash
      pip3.9 install -U jupyter-book
      ```
      * [Instructions complètes](https://jupyterbook.org/intro.html#install-jupyter-book) si la version ci-dessus ne marche pas

 5. Installer [Visual Studio Code](https://code.visualstudio.com) 
    * Sert à éditer le Markdown et le format Jupyter (et le format YAML pour la config si nécessaire)
    * Fournit des boutons pour produire l'output sans passer par le terminal

 6. Ouvrir le fichier `workspace.code-workspace` dans VS Code
    * L'installation des extensions suivantes de VS Code sera proposée:
      * `ms-python.python` pour avoir un éditeur/linter Python
      * `ms-toolsai.jupyter` pour ouvrir et éditer des fichier Jupyter `*.ipynb`
      * `redhat.vscode-yaml` pour éditer des fichiers de configuration YAML
      * `executablebookproject.myst-highlight` pour utiliser la syntaxe Markdown étendue prise en charge par `jupyter-book`
      * `seunlanlege.action-buttons` pour avoir des boutons directement dans VS Code pour faire un build
      * `ban.spellright` pour une correction orthographique de base dans VS Code
      
      Accepter l'installation de ces recommandations à l'ouverture du workspace:
      
      ![](docs/media/extension_recommendations.png)

    * Si l'installation des extensions ne vous est pas proposée, le faire manuellement via l'interface graphique de VS Code ou via le terminal:
      ```bash
      code --install-extension <extension-id>
      ```
<sup>1</sup> *Note de Philippe: J'ai pris la version 3.9.0 et tout ce qui suit fonctionne parfaitement.*

### Installation Ubuntu 20.04 LTS

* Cloner le dépôt  dans un dossier de votre choix

```bash
# install git if needed
sudo apt install -y git

# clone in the directory of your choice
cd {BASE_FOLDER}
git clone https://github.com/edunum-sec2/ressources.git
cd ressources
```

* Lancer le script d'installation

```bash
./install_ubuntu.sh
```

### Références

* Syntaxe Mardown utilisée: [MyST](https://jupyterbook.org/reference/glossary.html#term-MyST)


### Build

**Pour produire l'output HTML statique depuis les fichiers source**

Avec VS Code si installé comme ci-dessous, cliquer sur un des boutons en bas de la fenêtre:

![](docs/media/build_screenshot.png)

Sinon, via le terminal. Pour la partie élèves:

```bash
cd <dossier-du-checkout>/edunum-sec2/config/eleve
jupyter-book build .
```

Pour la partie enseignant·e·s:

```bash
cd <dossier-du-checkout>/edunum-sec2/config/maitre
jupyter-book build .
```

Ouvrir ensuite le fichier `_build/html/index.html`, par exemple (macOS):

Si nécessaire (erreurs, vieux fichiers qui traînent dans `_build`):

```bash
cd <dossier-du-checkout>/edunum-sec2/config/eleve
# ou:
cd <dossier-du-checkout>/edunum-sec2/config/maitre

#puis:
jupyter-book clean .
```

## Exemples d'utilisation des ressources

### Utilisation en ligne

1. Je me rends sur https://edunumsec2.ch
2. Je navigue à travers les différents chapitres du cours. 
3. Si une information m'intéresse, par exemple une anecdote historique, un angle d'attaque pour une notion, un exemple particulier, voire même une séquence entière de cours théorique, je prends des notes et la réutilise à souhait dans mes leçons. 
4. Je parcours les idées d'activité et je choisis celles qui m'intéressent. 
5. J'utilise les séries d'exercice à disposition comme "devoirs" pour mes élèves. 
6. Je demande à mes élèves de lire certains chapitres en préparation des cours. Je reprends les notions essentielles en classe.  

### Modifications indépendantes

1. Si certains contenus m'intéressent, mais que je considère qu'ils pourraient être transformés pour être plus efficaces, je peux à tout moment aller consulter les fichiers sources. 
2. Je reviens sur ce dépôt Github.
3. Je retrouve le chapitre qui m'intéresse. 
4. Je télécharge le fichier source. 
5. Je le retravaille pour en faire ma propre version. 

### Participation au développement

1. Je me réfère au chapitre [installation](#installation). 
2. Une fois que l'environnement est installé, plusieurs options s'offrent à moi. 
3. Je peux travailler à l'amélioration des ressources en tant que *correcteur*. Dans ce cas, j'utilise les fonctions [issues](https://github.com/edunumsec2/book/issues) et [discussions](https://github.com/edunumsec2/book/discussions) de Github et je propose de améliorations ou des modifications qui me paraissent importantes. 
4. Je peux travailler en tant que *rédacteur*. Dans ce cas je crée une branche, je propose des contenus originaux à l'intérieur d'un chapitre - séquences théoriques, activités, séries d'exercices, et je les soumets au reste des utilisateurs pour validation via un pull-request.

## Comité de rédaction

- Représentation de l'information : 
- Algorithmique : 
- Programmation : 
- Architecture des ordinateurs : 
- Enjeux sociaux : 


