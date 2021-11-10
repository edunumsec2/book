(participationdeveloppement)=
# Participation au développement

Les ressources sont pensées sur un modèle collaboratif. Elles se veulent flexibles, adaptables, et bénéficieront de tous les apports des personnes concernées. Le groupe de travail considère qu'il est important que toute enseignante ou enseignant de la matière `informatique` se sente libre de contribuer à l'amélioration des ressources. 

(marcheasuivreinstallation)=
## Marche à suivre installation

### Environnement Github, jupyter{book}, Visual Studio Code

````{panels}
:column: col-lg-12 p-3
⚠️ Attention
^^^^
Ce chapitre s'adresse aux personnes qui souhaitent intervenir sur les fichiers sources, que ce soit pour les transformer à leur guise et en faire de nouveaux outils de travail, ou pour participer au projet en partageant leurs créations.
````

**Pour installer l'environnement nécessaire à la création du contenu**

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
      * Pour macOS, un excellent tuto si l'installation pose problème (mais il faut bien lire la deuxième partie): [Tuto](https://opensource.com/article/19/5/python-3-default-mac#what-to-do)

 4. Installer [Jupyter Book](https://jupyterbook.org). Ceci **met aussi à jour** Jupyter Book lorsqu'une nouvelle version est disponible. Si l'équipe de rédaction utilise de nouvelles fonctions de Jupyter Book, il faut faire retourner ceci pour l'obtenir.
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
      
      ![](media/presentation/extension_recommendations.png)

    * Si l'installation des extensions ne vous est pas proposée, le faire manuellement via l'interface graphique de VS Code ou via le terminal:
      ```bash
      code --install-extension <extension-id>
      ```


```{admonition} Important
:class: caution
N'oubliez pas de contrôler que les **mises à jour** des différents environnements et extensions soient toujours faites. 
```

### Build

**Pour produire l'output HTML statique depuis les fichiers source**

Avec VS Code si installé comme ci-dessous, cliquer sur un des boutons en bas de la fenêtre:

![](media/presentation/build_screenshot.png)

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