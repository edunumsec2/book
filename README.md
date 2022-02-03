 ````{image} modulo_banner3.svg
````

# Informatique au Gymnase / Pilote

## Introduction

Des moyens d'enseignement pour l'informatique en discipline obligatoire au niveau Secondaire II ont été produits par un groupe de travail issu d'une collaboration entre la DGEP, l'EPFL, la HEP et l'UNIL. Dans le cadre de l’introduction de cette discipline, prévue à la rentrée 2022 dans le canton de Vaud, l'objectif de ces ressources est de proposer aux enseignant·e·s d'informatique des contenus théoriques, des séries d'exercices et des idées d'activités.

En accord avec la DGEP, une partie de ce matériel est déjà mise à disposition des enseignant·e·s vaudois·e·s pour une première phase pilote.

Les ressources sont accessibles via le [site web](https://edunumsec2.ch) (Username : edunum, Password : Edunumsecondaire2). Elles peuvent être utilisées telles quelles ou modifiées via un [dépôt GitHub](https://github.com/edunumsec2/book).

## Table des matières

---

- [Introduction](#introduction)
- [Utilisation](#utilisation)
- [Documents importants](#documents-importants)
- [Chapitrage du livre](#chapitrage)
- [Structure du dépôt GitHub](#structure-dépôt-GitHub)
- [Licence du projet](#licence-du-projet)
- [Installation](#installation)
  - [Installation recommandée](#installation-recommandée)
  - [Installation Ubuntu 20.04 LTS](#installation-ubuntu-20.04-lts)
  - [Références](#références)
  - [Build](#build)
- [Exemples d'utilisation des ressources](#exemples-dutilisation-des-ressources)
  - [Utilisation en ligne](#utilisation-en-ligne)
  - [Modifications indépendantes](#modifications-indépendantes)
  - [Participation au développement](#participation-au-développement)
- [Comité de rédaction](#comité-de-rédaction)


### Votre avis et ceux de vos élèves sont importants

En tant que membre du projet pilote, nous vous remercions par avance pour votre participation au processus d’enquête. Les données recueillies permettront d'évaluer la pertinence des contenus afin de réaliser les ajustements nécessaires. La démarche porte uniquement sur les ressources et les élèves, il ne s'agit en aucun cas d'évaluer la qualité de l'enseignement dispensé. Toutes les données seront traitées de façon confidentielle. En dernier lieu, ces données agrégées et anonymisées feront l'objet d'analyses statistiques à la fin de chaque semestre. 
  

## Utilisation

L'utilisation **standard** des ressources ne requiert pas d'installation particulière et peut-être effectuée immédiatement à l'adresse https://edunumsec2.ch. 

Dans le cadre du projet pilote, nous vous saurions gré de suivre le protocole minimal décrit ci-dessous :  

1. Participer aux sondages suivants (10 min par sondage) : 
    - [Questionnaire de rentrée / élève](https://www.surveymonkey.com/r/VVZQYRR)
    - [Questionnaire de rentrée / enseignant·e](https://www.surveymonkey.com/r/s2enspre)
    - [Questionnaire post-thématique / élève](https://www.surveymonkey.com/r/s2elpostthem)
    - [Questionnaire post-thématique / enseignant·e](https://www.surveymonkey.com/r/s2enspostthem)
    - [Questionnaire post thématique enjeux sociaux / enseignant·e](https://www.surveymonkey.com/r/s2postensejs)

2. Ecrire à nathalie.farenc@epfl.ch pour la tenir informée du début et de la fin d'un cours donné sur l'un ou l'autre des sujets du Plan d'études.
3. Signaler tout défaut éventuel des ressources à nathalie.farenc@epfl.ch ou directement à la personne en charge de la thématique en question, dont vous trouverez l'adresse sous [comité de rédaction](#comité-de-rédaction).

L'utilisation **avancée** des ressources comprend, en outre, les étapes suivantes : 

4. Utiliser les fonctionnalités de GitHub telles que [issues](https://github.com/edunumsec2/book/issues) et [discussions](https://github.com/edunumsec2/book/discussions) pour signaler des améliorations potentielles. 

Après la phase **pilote**, les enseignant.es pourront en outre : 

6. Proposer et rédiger des modifications via la création d'une [branche](https://github.com/edunumsec2/book/branches). 
7. Forker le dépôt pour en faire un clone indépendant via le mécanisme de [fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo). 
8. Utiliser l'environnement [Jupyter-book](#installation) pour tester ses améliorations en local sur sa propre machine. 

## Documents importants

* [Livret de cours](https://files.edunumsec2.ch/livret.pdf) décrivant le découpage du plan d'études dans le détail. 
* [Questionnaire de rentrée / élève](https://www.surveymonkey.com/r/VVZQYRR)
* [Questionnaire de rentrée / enseignant·e](https://www.surveymonkey.com/r/s2enspre)
* [Questionnaire post-thématique / élève](https://www.surveymonkey.com/r/s2elpostthem)
* [Questionnaire post-thématique / enseignant·e](https://www.surveymonkey.com/r/s2enspostthem)
* [Questionnaire post thématique enjeux sociax / enseignant·e](https://www.surveymonkey.com/r/s2postensejs)

## Chapitrage

Les ressources sont découpées selon un chapitrage qui correspond au plan d'études romand (voir ci-dessus). Elles sont divisées en quatre parties, dont nulle n'a de préséance sur les autres. Il appartient à l'enseignante ou l'enseignant de choisir l'ordre dans lequel les contenus sont abordés. Le fait que les chapitres soient successifs est le résultat des limitations de l'affichage. Pour atténuer quelque peu ce problème, nous avons choisi de renoncer à une numérotation des chapitres. 

[Représentation de l'information](https://eleve.edunumsec2.ch/content/theme/representation-information/accueil/eleve.html)
: Où il est question du passage du système décimal au *système binaire*, ainsi que des problématiques de traitement des données telles que *l'encodage*, *la compression*, *l'échantillonnage*, *le cryptage*, et la *représentation des caractères, des images et des sons* sous forme de bits. 

[Algorithmique I](https://eleve.edunumsec2.ch/content/theme/introduction-algorithmique/accueil/eleve.html)
: Ce chapitre propose une *définition générale de l'algorithmique*, ainsi qu'une présentation de certains *algorithmes classiques*. 

[Programmation I](https://eleve.edunumsec2.ch/content/theme/programmation/accueil/eleve.html)
: Après avoir présenté un échantillon de langages de programmation et leurs différences respectives, ce chapitre *pose les bases du langage Python*. 

[Architecture des ordinateurs](https://eleve.edunumsec2.ch/content/theme/architecture-ordinateurs/accueil/eleve.html)
: Il est question ici de notions telles que *les portes logiques*, *les transistors*, *l'architecture de Von Neumann*, et autres concepts essentiels à la compréhension de ce qui se passe au niveau physique et électronique dans un ordinateur.

## Structure dépôt GitHub

* [config](https://github.com/edunumsec2/book/tree/master/config) contient essentiellement les documents .yml et .py qui servent à générer la version html statique de la documentation. Ce qui est présent dans ce dossier tire sa source dans la documentation [Sphinx](https://www.sphinx-doc.org/en/master/index.html), ainsi que la documentation [jupyter-book](https://jupyterbook.org/intro.html). 
* [content](https://github.com/edunumsec2/book/tree/master/content) contient le contenu du cours, découpé en *annexes*, *enjeux* (pour enjeux de société), *readme*, *theme*. C'est dans le dossier *theme* que vous trouverez les documents sources des différentes thématiques. Dans les documents sources, il existe deux extensions : les documents .md, et les .ipynb. Les documents .md sont rédigés dans une sytanxe Mardown étendue, le [MyST](https://myst-parser.readthedocs.io/en/latest/). Les documents .ipynb sont à l'origine des documents créés pour [jupyter notebook](https://jupyter.org/). Les deux syntaxes sont tolérées pour la génération du site html statique via l'outil [jupyter-book](https://jupyterbook.org/intro.html). 
* [docs](https://github.com/edunumsec2/book/tree/master/docs) contient les *archives* de la documentation, à savoir des fichiers qui ne sont plus utilisés dans la version actuelle du livre. Le dossier *landing*, contient le .html qui génère la [page d'accueil](https://edunumsec2.ch/). *media*, comme d'ailleurs tous les autres dossiers portant ce nom, contient les media utilisés dans le dossier parent en question. *palette* contient des indications relatives à la palette graphique du projet. *wiki* contient les tutoriels nécessaires à l'utilisation du dépôt GitHub. 


## Licence du projet

Les ressources sont publiées sous licence Creatives Commons *Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions (CC BY-NC-SA)*. Cela signifie qu'elles peuvent être copiées, transformées, adaptées, et diffusées, hormis à des fins commerciales, tant qu'elles créditent le groupe de travail présenté ci-dessus, et qu'elles utilisent la même licence pour le partage futur. Les conditions sont disponibles [ici](https://creativecommons.org/licenses/?lang=fr). 

![](docs/media/by-nc-sa.png)

Toute personne qui réutilise les ressources est priée de le faire de la façon suivante : 

* 💰 Pas d'utilisation commerciale. 
* ♻️ Possibilité de modifier les ressources à souhait. 
* 📗 Crédit : "Par le groupe de travail DGEP, EPFL, HEP, UNIL". 
* 🤝 Partage selon les mêmes conditions. Donc en ajoutant simplement le logo ci-dessus pour toute publication éventuelle. 

## Installation 

⚠️ *Attention : l'installation qui suit N'EST PAS nécessaire dans le cadre du projet pilote. Elle figure ici à titre informatif pour celles et ceux qui souhaitent comprendre l'architecture globale du projet et veulent avoir une idée de l'intégralité des possibilités qu'offre un modèle de projet open source. Après la première année de pilote, et compte tenu des retours qui auront été faits, le projet se déploiera entièrement, et les enseignant.es d'informatique auront tout le loisir d'installer l'environnement ci-dessous et de s'amuser à leur guise avec la documentation open source de ce dépôt GitHub.* 

Pour ceux et celles qui souhaitent utiliser l'environnement Jupyter Book pour tester des contenus et participer au développement, la marche à suivre est la suivante : 

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

 4. (Optionnel) Créer un environnement virtuel pour que les autres installs de Python n'interfèrent pas avec celle utilisée ici:
    * Avec Python 3, depuis de dossier `book`:
      ```bash
      python3 -m venv venv
      ```
      Bien utiliser le nom `venv` (pas `.env` ou `.venv`); c'est celui qui sera reconnu par les scripts de compilation.

 5. Installer [Jupyter Book](https://jupyterbook.org).  Ceci **met aussi à jour** Jupyter Book lorsqu'une nouvelle version est disponible. Si l'équipe de rédaction utilise de nouvelles fonctions de Jupyter Book, il faut faire retourner ceci pour l'obtenir.
    * Avec Python 3, depuis de dossier `book`:
      ```bash
      source venv/bin/activate # si vous utilisez un environnement virtuel (recommandé), sinon à sauter
      pip3 install -U jupyter-book
      ```
      * [Instructions complètes](https://jupyterbook.org/intro.html#install-jupyter-book) si la version ci-dessus ne marche pas

 6. Installer [Visual Studio Code](https://code.visualstudio.com) 
    * Permer d'éditer le Markdown et le format Jupyter (et le format YAML pour la config, si nécessaire)
    * Fournit des boutons pour produire l'output sans passer par le terminal

 7. Ouvrir le fichier `workspace.code-workspace` dans VS Code
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

⚠️ *Attention : les utilisations suivantes sont présentes à titre indicatif mais ne seront effectives qu'après la phase pilote.* 

### Utilisation en ligne

1. Je me rends sur https://edunumsec2.ch
2. Je navigue à travers les différents chapitres du cours. 
3. Si une information m'intéresse, par exemple une anecdote historique, un angle d'attaque pour une notion, un exemple particulier, voire même une séquence entière de cours théorique, je prends des notes et la réutilise à souhait dans mes leçons. 
4. Je parcours les idées d'activité et je choisis celles qui m'intéressent. 
5. J'utilise les séries d'exercices à disposition comme "devoirs" pour mes élèves. 
6. Je demande à mes élèves de lire certains chapitres en préparation des cours. Je reprends les notions essentielles en classe.  

### Modifications indépendantes

1. Si certains contenus m'intéressent mais que je considère qu'ils pourraient être transformés pour être plus efficaces, je peux à tout moment aller consulter les fichiers sources. 
2. Je reviens sur ce dépôt Github.
3. Je retrouve le chapitre qui m'intéresse. 
4. Je télécharge le fichier source. 
5. Je le retravaille pour en faire ma propre version. 

### Participation au développement

1. Je me réfère au chapitre [installation](#installation). 
2. Une fois que l'environnement est installé, plusieurs options s'offrent à moi. 
3. Je peux travailler à l'amélioration des ressources en tant que *correcteur*. Dans ce cas, j'utilise les fonctions [issues](https://github.com/edunumsec2/book/issues) et [discussions](https://github.com/edunumsec2/book/discussions) de Github et je propose des améliorations ou des modifications qui me paraissent importantes. 
4. Je peux travailler en tant que *rédacteur*. Dans ce cas je crée une branche, je propose des contenus originaux à l'intérieur d'un chapitre - séquences théoriques, activités, séries d'exercices, et je les soumets aux autres utilisateurs pour validation via un pull-request.

## Comité de rédaction

- Représentation de l'information : David Da Silva (david.dasilva@eduvaud.ch) - Gymnase de Chamblandes & Javier Iglesias (javier.iglesias@eduvaud.ch) - Gymnase de Renens
- Algorithmique : Biljana Petreska (biljana.petreska@fileinformatique.ch) - Gymnase d'Yverdon & Micha Hersch (demander contact à nathalie.farenc@epfl.ch) Gymnase de Renens / HEP
- Programmation : Raphaël Holzer (raphael.holzer@eduvaud.ch) - Gymnase du Bugnon & Gilles Racine (gilles.racine@eduvaud.ch) - Gymnase de Sevelin
- Architecture des ordinateurs : Philippe Rochat (philippe.rochat@fileinformatique.ch) - Gymnase de Morges & Jean-Philippe Pellet (jean-philippe.pellet@fileinformatique.ch) - HEP
- Enjeux sociaux : Lucile Berset (lucile.berset@epfl.ch) - EPFL ;  Virginia Haussauer (virginia.haussauer@epfl.ch) - EPFL;  Frank Dayen (frank.dayen@eduvaud.ch) - Gymnase de Morges & Boris Beaude (boris.beaude@unil.ch) - UNIL
- Plateforme : Romain Edelmann (romain.edelmann@epfl.ch) - EPFL & Grégoire Gavin (gregoire.gavin@epfl.ch) - EPFL
- Charte éditoriale, plateforme, rédaction : Elliot Vaucher (elliot.vaucher@epfl.ch) - EPFL
- Coordination : Nathalie Farenc (nathalie.farenc@epfl.ch) - EPFL


Test actions