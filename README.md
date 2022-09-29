![modulo-banner](https://github.com/edunumsec2/modulo2/blob/main/source/_static/assets/modulo-head-banner.svg)

# Informatique au Gymnase

## Introduction

Des moyens d'enseignement pour l'informatique en discipline obligatoire au niveau Secondaire II ont été produits par un groupe de travail issu d'une collaboration entre la DGEP, l'EPFL, la HEP Vaud et l'UNIL. Dans le cadre de l’introduction de cette discipline, prévue à la rentrée 2022 dans le canton de Vaud, l'objectif de ces ressources est de proposer aux enseignant·e·s d'informatique des contenus théoriques, des séries d'exercices et des idées d'activités.

Les ressources sont accessibles via le [site web](https://modulo-info.ch/). Elles peuvent être utilisées telles quelles ou modifiées via un [dépôt GitHub](https://github.com/edunumsec2/book).

## Table des matières

---

- [Introduction](#introduction)
- [Utilisation](#utilisation)
- [Contributions](#contributions)
- [Code de conduite](#code-de-conduite)
- [Documents importants](#documents-importants)
- [Chapitrage](#chapitrage)
- [Installation](#installation)
  - [Installation recommandée](#installation-recommandée)
  - [Pré-requis](#pré-requis)
  - [Installation rapide](#installation-rapide)
  - [Serveur local](#serveur-local)
  - [Génération de build](#génération-de-build)
  - [Génération de polycopié](#génération-de-polycopié)
  - [Configuration et personnalisation](#configuration-et-personnalisation)
- [Comité de rédaction](#comité-de-rédaction)

## Utilisation

L'utilisation des ressources ne requiert pas d'installation particulière et peut-être effectuée immédiatement à l'adresse <https://modulo-info.ch>.

## Contributions

Si vous souhaitez contribuer au projet, la marche à suivre est décrite dans ce [document](https://github.com/edunumsec2/book/blob/master/CONTRIBUTING.md)

## Code de conduite

Un code de conduite est disponible [ici](https://github.com/edunumsec2/book/blob/master/CODE_OF_CONDUCT.md).

## Documents importants

- [Livret de cours](https://files.edunumsec2.ch/livret.pdf) décrivant le découpage du plan d'études dans le détail.
- [Questionnaire de rentrée / élève](https://www.surveymonkey.com/r/VVZQYRR)
- [Questionnaire de rentrée / enseignant·e](https://www.surveymonkey.com/r/s2enspre)
- [Questionnaire post-thématique / élève](https://www.surveymonkey.com/r/s2elpostthem)
- [Questionnaire post-thématique / enseignant·e](https://www.surveymonkey.com/r/s2enspostthem)
- [Questionnaire post thématique enjeux sociax / enseignant·e](https://www.surveymonkey.com/r/s2postensejs)

## Chapitrage

Les ressources sont découpées selon un chapitrage qui correspond au plan d'études romand (voir ci-dessus). Elles sont divisées en quatre parties, dont nulle n'a de préséance sur les autres. Il appartient à l'enseignante ou l'enseignant de choisir l'ordre dans lequel les contenus sont abordés. Le fait que les chapitres soient successifs est le résultat des limitations de l'affichage. Pour atténuer quelque peu ce problème, nous avons choisi de renoncer à une numérotation des chapitres.

[Représentation de l'information](https://apprendre.modulo-info.ch/content/appr/theme/rep-info/accueil/eleve.html)
: Où il est question du passage du système décimal au *système binaire*, ainsi que des problématiques de traitement des données telles que *l'encodage*, *la compression*, *l'échantillonnage*, *le cryptage*, et la *représentation des caractères, des images et des sons* sous forme de bits.

[Algorithmique I](https://apprendre.modulo-info.ch/content/appr/theme/algo1/accueil/eleve.html)
: Ce chapitre propose une *définition générale de l'algorithmique*, ainsi qu'une présentation de certains *algorithmes classiques*.

[Programmation I](https://apprendre.modulo-info.ch/content/appr/theme/prog1/accueil/elevenew.html)
: Après avoir présenté un échantillon de langages de programmation et leurs différences respectives, ce chapitre *pose les bases du langage Python*.

[Architecture des ordinateurs](https://apprendre.modulo-info.ch/content/appr/theme/archi/accueil/eleve.html)
: Il est question ici de notions telles que *les portes logiques*, *les transistors*, *l'architecture de Von Neumann*, et autres concepts essentiels à la compréhension de ce qui se passe au niveau physique et électronique dans un ordinateur.

## Installation

Pour ceux et celles qui souhaitent utiliser l'environnement Sphinx pour tester des contenus et participer au développement, la marche à suivre est la suivante :

### Installation recommandée

Modulo est basé sur le générateur de documentation [Sphinx](https://www.sphinx-doc.org/en/master/) et utilise le template [Furo](https://github.com/pradyunsg/furo).

### Pré-requis

- Python 3.x et pip ([Installation MacOSX](https://docs.python-guide.org/starting/install3/osx/)) ([Installation Windows](https://docs.python-guide.org/starting/install3/win/)) ([Installation rapide](https://www.python.org/downloads/))
- [virtualenv](https://virtualenv.pypa.io/en/latest/) (`$ pip install virtualenv`)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Pour vérifier la bonne installation de l'environnement de base :

- `$ python --version`
- `$ virtualenv --version`
- `$ git --version`

Pour simplifier les actions fréquentes (build, clean), le projet contient un workspace pour [Visual Studio Code](https://code.visualstudio.com/). L'utilisation de VSCode est optionnelle, vous pouvez bien sûr utiliser votre éditeur de code préféré.

### Installation rapide

1. Récupération du projet : `git clone git@github.com:edunumsec2/book.git`
1. Déplacement vers la racine du projet : `cd book`
1. Création d'un environnement virtuel : `virtualenv .env`
1. Activation de l'environnement virtuel  
    MacOS : `source .env/bin/activate`  
    Windows : `.env\Scripts\activate`
1. Installation des librairies dans l'environnement virtuel : `pip install -r requirements.txt -U`

**Remarque** : à chaque fois que vous travaillez sur le projet, l'environnement virtuel devrait être activé (point 4).

### Serveur local

Le projet utilise [sphinx-autobuild](https://github.com/executablebooks/sphinx-autobuild) qui démarre un serveur sur <http://localhost:8000> (ou <http://127.0.0.1:8000>) et rebuild la documentation automatiquement lorsqu'un changement est détecté.

1. Activation de l'environnement virtuel (si pas déjà fait)
2. Activation du serveur local :

- Documentation 'Apprendre' : `sphinx-autobuild src/appr docs --watch src --open-browser -a --delay 1`
- Documentation 'Enseigner' : `sphinx-autobuild src/ens docs --watch src --open-browser -a --delay 1`

Pour arrêter le serveur : `CTRL+c` ou `⌘+c`

### Génération de build

- Génération du build 'Apprendre' : `sphinx-build -b html src/appr docs`
- Génération du build 'Enseigner' : `sphinx-build -b html src/ens docs`

### Génération de polycopié

*La génération automatique d'un polycopié est actuellement en développement et n'est pas encore stabilisée. De plus elle n'est testée pour l'instant que sur Mac OS.*

Sphinx permet de générer un build LaTeX des sources qui peut ensuite être utilisé pour générer une polycopié au format pdf.

- Génération du fichier latex: `sphinx-build -b latex -t latex_mode src/appr build/latex/appr`
- Compilation du fichier latex: `cd build/latex/appr && pdflatex modulo.tex`

### Configuration et personnalisation

Les options de build, notamment les chapitres à générer, le titre, le noms des auteurs, les couleurs etc., peuvent être modifées dans le fichier [src/appr/conf.py](src/appr/conf.py) et [src/ens/conf.py](src/ens/conf.py)

## Comité de rédaction

- Représentation de l'information : David Da Silva (david.dasilva@eduvaud.ch) - Gymnase de Chamblandes & Javier Iglesias (javier.iglesias@eduvaud.ch) - Gymnase de Renens
- Algorithmique : Biljana Petreska (biljana.petreska@fileinformatique.ch) - Gymnase d'Yverdon & Micha Hersch (Gymnase de Renens / HEP Vaud)
- Programmation : Raphaël Holzer (raphael.holzer@eduvaud.ch) - Gymnase du Bugnon & Gilles Racine (gilles.racine@eduvaud.ch) - Gymnase de Sevelin
- Architecture des ordinateurs : Philippe Rochat (philippe.rochat@fileinformatique.ch) - Gymnase de Morges & Jean-Philippe Pellet (jean-philippe.pellet@fileinformatique.ch) - HEP Vaud
- Enjeux sociaux : Lucile Berset (lucile.berset@epfl.ch) - EPFL ;  Virginia Haussauer (virginia.haussauer@epfl.ch) - EPFL;  Frank Dayen (frank.dayen@eduvaud.ch) - Gymnase de Morges & Boris Beaude (boris.beaude@unil.ch) - UNIL
- Plateforme : Romain Edelmann (romain.edelmann@epfl.ch) - EPFL & Grégoire Gavin (gregoire.gavin@epfl.ch) - EPFL
- Charte éditoriale, plateforme, rédaction : Elliot Vaucher (elliot.vaucher@epfl.ch) - EPFL
- Coordination : Nathalie Farenc (nathalie.farenc@epfl.ch) - EPFL
