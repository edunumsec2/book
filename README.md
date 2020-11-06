# Ressources d'enseignement de l'informatique au secondaire 2

## Outils nécessaires ou recommandés

 * Git/GitHub:
   * Terminal avec les commandes directes de `git`
   * ou application [GitHub Desktop](https://desktop.github.com)
 * Édition du Markdown (`*.md`) et du format Jupyter (`*.ipynb`):
   * [Visual Studio Code](https://code.visualstudio.com)
 * Contruction du rendu HTML:
   * [Jupyter Book](https://jupyterbook.org)
     * [Installation de Juypter Book](https://jupyterbook.org/intro.html#install-jupyter-book)
     * Syntaxe Mardown utilisée: [MyST](https://jupyterbook.org/reference/glossary.html#term-MyST)


## Build

Comment produire l'output HTML statique depuis les fichiers source:

```bash
cd <dossier-du-checkout>
jupyter-book build edunum-sec2
```

Ouvrir ensuite le fichier `edunum-sec2/_build/html/index.html`, par exemple (macOS):

```bash
open edunum-sec2/_build/html/index.html
```

Si nécessaire (erreurs, vieux fichiers qui traînent dans `_build`):

```bash
jupyter-book clean edunum-sec2
```

Test de commit sur le readme.md
