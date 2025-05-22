# Installation

Modulo est basé sur le générateur de documentation [Sphinx](https://www.sphinx-doc.org/en/master/) et utilise le template [Furo](https://github.com/pradyunsg/furo). Les ressources sont rédigées au format [Markdown](https://www.markdownguide.org/basic-syntax/) et sont générées par Sphinx sous la forme d'un site web statique (HTML/CSS/JS).

## Pré-requis

- Python 3.x et pip ([Installation MacOSX](https://docs.python-guide.org/starting/install3/osx/)) ([Installation Windows](https://docs.python-guide.org/starting/install3/win/)) ([Installation rapide](https://www.python.org/downloads/))
- [virtualenv](https://virtualenv.pypa.io/en/latest/) (`$ pip install virtualenv`)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Pour vérifier la bonne installation de l'environnement de base :

- `$ python --version`
- `$ virtualenv --version`
- `$ git --version`

Pour simplifier les actions fréquentes (build, clean), le projet contient un Workspace pour [Visual Studio Code](https://code.visualstudio.com/). Lors de l'ouverture du Workspace (à la racine du projet), il vous sera proposé d'installer les plugins suggérés. L'utilisation de VSCode est optionnelle, mais le Workspace propose des boutons qui vous éviteront de saisir certaines commandes à la main dans le Terminal.

## Installation

1. Récupération du projet : `git clone git@github.com:edunumsec2/book.git` (ou alors plus simplement avec [GitHub Desktop](https://github.com/edunumsec2/book/blob/documentation/doc/github-desktop.md))
1. Déplacement vers la racine du projet : `cd book`
1. Création d'un environnement virtuel : `virtualenv .env`
1. Activation de l'environnement virtuel  
    MacOS : `source .env/bin/activate`  
    Windows : `.env\Scripts\activate`
1. Installation des librairies dans l'environnement virtuel : `pip install -r requirements.txt -U`, puis `playwright install chromium` (nécessaire seulement pour la génération de la version imprimable)

_**Remarque** : à chaque fois que vous travaillez sur le projet, l'environnement virtuel doit être activé (point 4). Si vous utilisez VSCode et le Workspace, les boutons de build/auto-build l'activent automatiquement._

## Serveur local

Le projet utilise [sphinx-autobuild](https://github.com/executablebooks/sphinx-autobuild) qui démarre un serveur sur <http://localhost:8000> (ou <http://127.0.0.1:8000>) et rebuild la documentation automatiquement lorsqu'un changement est détecté.

1. Activation de l'environnement virtuel (si pas déjà fait)
2. Activation du serveur local :

- Documentation 'Apprendre' : `sphinx-autobuild src/appr build --watch src --open-browser -a --delay 1`
- Documentation 'Enseigner' : `sphinx-autobuild src/ens build --watch src --open-browser -a --delay 1`

Pour arrêter le serveur : <kbd>Ctrl</kbd>+<kbd>c</kbd> ou <kbd>⌘</kbd>+<kbd>c</kbd>

_**Remarque**: si vous utilisez le workspace VSCode, vous pouvez utiliser les boutons proposés en bas de l'interface._

## Génération de build

- Génération du build 'Apprendre' : `sphinx-build -b html src/appr build`
- Génération du build 'Enseigner' : `sphinx-build -b html src/ens build`

_**Remarque**: si vous utilisez le workspace VSCode, vous pouvez utiliser les boutons proposés en bas de l'interface._

## Génération de polycopié

*La génération automatique d'un polycopié est actuellement en développement et n'est pas encore stabilisée. De plus elle n'est testée pour l'instant que sur Mac OS.*

Sphinx permet de générer un build LaTeX des sources qui peut ensuite être utilisé pour générer une polycopié au format pdf.

- Génération du fichier latex: `sphinx-build -b latex -t latex_mode src/appr build/latex/appr`
- Compilation du fichier latex: `cd build/latex/appr && make`

Un makefile est également fourni, si bien qu'il est possible de compiler les polycopiés avec la commande suivante  depuis
le répertoire racine:
`make pdf`

Cela génère un fichier pdf par chapitre imprimable ainsi qu'un document contenant tous les chapitres imprimables. Ces fichiers se
trouvent alors dans le répertoire `build/pdf`.

## Configuration et personnalisation

Les options de build, notamment les chapitres à générer, le titre, le noms des auteurs, les couleurs etc., peuvent être modifées dans le fichier [src/appr/conf.py](src/appr/conf.py) et [src/ens/conf.py](src/ens/conf.py)
