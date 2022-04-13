![modulo-banner](https://github.com/edunumsec2/modulo2/blob/main/source/_static/assets/modulo-head-banner.svg)

# Informatique au Gymnase

## Introduction

Des moyens d'enseignement pour l'informatique en discipline obligatoire à l'école de maturité ont été produits par un groupe de travail issu d'une collaboration entre la DGEP, l'EPFL, la HEP Vaud et l'UNIL. Dans le cadre de l’introduction de cette discipline, prévue à la rentrée 2022 dans le canton de Vaud, l'objectif de ces ressources est de proposer aux enseignant·e·s d'informatique des contenus théoriques, des séries d'exercices et des idées d'activités.

Les ressources sont accessibles via le [site web](https://modulo-info.ch) (Pour la version "enseigner", Username : edunum, Password : Edunumsecondaire2). Elles peuvent être utilisées telles quelles ou modifiées via un [dépôt GitHub](https://github.com/edunumsec2/book).

## Table des matières

---

- [Introduction](#introduction)
- [Utilisation](#utilisation)
- [Contributions](#contributions)
- [Liens](#liens)
- [Documents importants](#documents-importants)
- [Licence du projet](#licence-du-projet)
- [Installation](#installation)
  - [Installation recommandée](#installation-recommandée)
  - [Installation Ubuntu 20.04 LTS](#installation-ubuntu-20.04-lts)
  - [Build](#build)
- [Exemples d'utilisation des ressources](#exemples-dutilisation-des-ressources)
  - [Utilisation en ligne](#utilisation-en-ligne)
  - [Modifications indépendantes](#modifications-indépendantes)
  - [Participation au développement](#participation-au-développement)
- [Comité de rédaction](#comité-de-rédaction)
  

## Utilisation

L'utilisation des ressources ne requiert pas d'installation particulière et peut-être effectuée immédiatement à l'adresse https://modulo-info.ch. 

## Contributions

Si vous souhaitez contribuer au projet, la marche à suivre est décrite dans ce [document](https://github.com/edunumsec2/book/blob/master/CONTRIBUTING.md)

## Code de conduite

Un code de conduite est disponible [ici](https://github.com/edunumsec2/book/blob/master/CODE_OF_CONDUCT.md). 

## Liens

*Attention : Pour la version "enseigner", Username : edunum, Password : Edunumsecondaire2*

**Version actuelle des ressources**

* apprendre : https://apprendre.modulo-info.ch/
* enseigner : https://enseigner.modulo-info.ch/

(Actualisation annuelle)

**Version en développement**

* apprendre : https://dev-apprendre.modulo-info.ch/
* enseigner : https://dev-enseigner.modulo-info.ch/

(Actualisation continue)

**Archive des versions antérieures**

* apprendre : https://old-apprendre.modulo-info.ch/
* enseigner : https://old-enseigner.modulo-info.ch/

(Archive de la version de l'année précédente)

*Avertissement : le projet étant encore dans une phase de construction, il est possible que la version actuelle soit mise à jour plus rapidement qu'à l'échéance d'une année. Tout changement de version majeur est signalé aux enseignant·e·s participant au projet.*

## Documents importants

* [Livret de cours](https://files.edunumsec2.ch/livret.pdf) décrivant le découpage du plan d'études dans le détail. 
* [Questionnaire de rentrée / élève](https://www.surveymonkey.com/r/VVZQYRR)
* [Questionnaire de rentrée / enseignant·e](https://www.surveymonkey.com/r/s2enspre)
* [Questionnaire post-thématique / élève](https://www.surveymonkey.com/r/s2elpostthem)
* [Questionnaire post-thématique / enseignant·e](https://www.surveymonkey.com/r/s2enspostthem)
* [Questionnaire post thématique enjeux sociax / enseignant·e](https://www.surveymonkey.com/r/s2postensejs)

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

 4. Installer [Jupyter Book](https://jupyterbook.org).  Ceci **met aussi à jour** Jupyter Book lorsqu'une nouvelle version est disponible. Si l'équipe de rédaction utilise de nouvelles fonctions de Jupyter Book, il faut faire retourner ceci pour l'obtenir.
    * Avec Python 3.9:
      ```bash
      pip3.9 install -U jupyter-book
      ```
      * [Instructions complètes](https://jupyterbook.org/intro.html#install-jupyter-book) si la version ci-dessus ne marche pas

 5. Installer [Visual Studio Code](https://code.visualstudio.com) 
    * Permer d'éditer le Markdown et le format Jupyter (et le format YAML pour la config, si nécessaire)
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

1. Je me rends sur https://modulo-info.ch
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
- Charte éditoriale, plateforme, rédaction : Elliot Vaucher (elliot.vaucher@epfl.ch) - EPFL, Christophe Dumas (christophe.dumas@epfl.ch) - EPFL
- Coordination : Nathalie Farenc (nathalie.farenc@epfl.ch) - EPFL
