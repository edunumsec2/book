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

Pour simplifier les actions fréquentes (build, clean), le projet contient un Workspace pour [Visual Studio Code](https://code.visualstudio.com/). Lors de l'ouverture du Workspace (à la racine du projet), il vous sera proposé d'installer les plugins suggérés. L'utilisation de VSCode est optionnelle, vous pouvez bien sûr utiliser votre éditeur de code préféré.

## Installation rapide

1. Récupération du projet : `git clone git@github.com:edunumsec2/book.git`
1. Déplacement vers la racine du projet : `cd book`
1. Création d'un environnement virtuel : `virtualenv .env`
1. Activation de l'environnement virtuel  
    MacOS : `source .env/bin/activate`  
    Windows : `.env\Scripts\activate`
1. Installation des librairies dans l'environnement virtuel : `pip install -r requirements.txt -U`

**Remarque** : à chaque fois que vous travaillez sur le projet, l'environnement virtuel devrait être activé (point 4).

## Serveur local

Le projet utilise [sphinx-autobuild](https://github.com/executablebooks/sphinx-autobuild) qui démarre un serveur sur <http://localhost:8000> (ou <http://127.0.0.1:8000>) et rebuild la documentation automatiquement lorsqu'un changement est détecté.

1. Activation de l'environnement virtuel (si pas déjà fait)
2. Activation du serveur local :

- Documentation 'Apprendre' : `sphinx-autobuild src/appr docs --watch src --open-browser -a --delay 1`
- Documentation 'Enseigner' : `sphinx-autobuild src/ens docs --watch src --open-browser -a --delay 1`

Pour arrêter le serveur : `CTRL+c` ou `⌘+c`

## Génération de build

- Génération du build 'Apprendre' : `sphinx-build -b html src/appr docs`
- Génération du build 'Enseigner' : `sphinx-build -b html src/ens docs`

## Génération de polycopié

*La génération automatique d'un polycopié est actuellement en développement et n'est pas encore stabilisée. De plus elle n'est testée pour l'instant que sur Mac OS.*

Sphinx permet de générer un build LaTeX des sources qui peut ensuite être utilisé pour générer une polycopié au format pdf.

- Génération du fichier latex: `sphinx-build -b latex -t latex_mode src/appr build/latex/appr`
- Compilation du fichier latex: `cd build/latex/appr && pdflatex modulo.tex`

## Configuration et personnalisation

Les options de build, notamment les chapitres à générer, le titre, le noms des auteurs, les couleurs etc., peuvent être modifées dans le fichier [src/appr/conf.py](src/appr/conf.py) et [src/ens/conf.py](src/ens/conf.py)
