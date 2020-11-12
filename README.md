# Ressources d'enseignement de l'informatique au secondaire 2

## Outils nécessaires ou recommandés

 * Git/GitHub:
   * Terminal avec les commandes directes de `git`
   * ou application [GitHub Desktop](https://desktop.github.com)
 * Édition du Markdown (`*.md`) et du format Jupyter (`*.ipynb`):
   * [Visual Studio Code](https://code.visualstudio.com)
 * Contruction du rendu HTML:
   * Une version récente (3.x, x ≥ 6, ou mieux: x ≥ 9) de [Python](https://www.python.org/downloads/)
   * [Jupyter Book](https://jupyterbook.org)
     * [Installation de Juypter Book](https://jupyterbook.org/intro.html#install-jupyter-book)
       * En gros, avec Python 3.9: `pip3.9 install -U jupyter-book`
     * Syntaxe Mardown utilisée: [MyST](https://jupyterbook.org/reference/glossary.html#term-MyST)


## Build

Comment produire l'output HTML statique depuis les fichiers source:

```bash
cd <dossier-du-checkout>
jupyter-book build eleve
jupyter-book build maitre
```

Ouvrir ensuite le fichier `edunum-sec2/_build/html/index.html`, par exemple (macOS):

```bash
open edunum-sec2/_build/html/index.html
```

Si nécessaire (erreurs, vieux fichiers qui traînent dans `_build`):

```bash
jupyter-book clean eleve
jupyter-book clean maitre
```


