# Présentation des ressources

Les ressources pour l'enseignement de la branche *Informatique* au niveau secondaire II ont été produites par le `groupe de travail DGEP, EPFL, HEP, UNIL`. Leur objectif est la mise à disposition de contenus théoriques, de séries d'exercices, et d'idées d'activités pour les enseignantes et enseignants de ladite matière. 

Voici une liste non-exhaustive des usages potentiels de ces ressources : 

{fa}`check, text-success mr-1`**Rafraîchir vos connaissance dans les sujets du plan d'études**
: Ces ressources ont été rédigées en accord avec le plan d'études *informatique* pour le secondaire II. 

{fa}`check, text-success mr-1`**Vous inspirer du fil rouge des différents chapitres**
: Les *introductions* aux chapitres, par exemple, abordent la matière sous un angle peut-être différent de celui avec lequel vous avez l'habitude d'enseigner. 

{fa}`check, text-success mr-1`**Découvrir des idées d'activités à faire en classe**
: De nombreuses activités sont disponibles à l'intérieur de chacun des chapitres pour vous aider à mettre en place des séquences de cours interactives. 

{fa}`check, text-success mr-1`**Faire le plein d'exercices pour tester vos leçons**
: Une base de données d'exercice est à disposition dans la section concernée. 

{fa}`check, text-success mr-1`**Imprimer les ressources depuis une version PDF**
: Si vous êtes intéressés par un morceau de cours en particulier, vous pouvez l'imprimer directement depuis votre navigateur. 

{fa}`check, text-success mr-1`**Consulter les fichiers sources directement**
: Le projet est construit sur un modèle open-source, ce qui vous permet d'aller chercher les documents originaux, en format brut, directement ici. 

{fa}`check, text-success mr-1`**Exécuter des cellules de code dans le navigateur grâce à Binder**
: Si vous souhaitez faire travailler vos élèves sur des machines, l'option Binder vous permet d'exécuter des cellules de code sans devoir pré-configurer l'environnement. 

{fa}`check, text-success mr-1`**Contribuer au développement et à l'amélioration de du projet**
: Comme tout projet, celui-ci possède ses avantages et ses inconvénients. C'est pour bénéficier de votre expterise que nous avons construit ce projet sur un modèle open-source avec la possibilité à tout moment de le forker, de le transformer, ou d'y contribuer en utilisant l'infrastructure offerte par Github. 


:::{admonition,tip} Votre implication nous tient à ❤️

C'est l'objectif même du projet d'accueillir vos retours, idées d'améliorations, critiques, suggestions de toutes sortes. 

💡 [Ouvrez une issue Github](https://github.com/edunum-sec2/ressources/issues)
: pour nous suggérer de nouvelles idées, nous donner des retours sur vos expériences, ou aider d'autres utilisateurs à profiter de ces ressources. to 

✉️ [Contactez-nous pour du feedback](https://www.epfl.ch/education/educational-initiatives/center-learn/)
: dans le but de continuer de faire évoluer ce projet dans le bon sens. 

👍 [Votez pour de nouvelles améliorations](https://github.com/edunum-sec2/ressources)
: ajoutez un +1 aux *issues* qui vous intéressent particulièrement. 

🙌 [Contribuez aux ressources](../demostests/edito/presentation-ressources.md)
: en lisant la documentation relative à la contribution aux ressources. 

:::

## Chapitrage

Les ressources sont découpées selon un chapitrage qui correspond au plan d'études (ajouter réf). Elles sont divisées en quatre parties, dont nulle n'a de préseance sur les autres. Il appartient à l'enseignante ou l'enseignant de choisir l'ordre dans lequel les contenus seront abordés. Le fait que les chapitres soient successifs est le résultat des limitations de l'affichage. Pour atténuer quelque peu ce problème nous avons choisi de renoncer à des numéros de chapitre. 

🟠 [Représentation de l'information](theme/representation-information/eleve.md)
: Où il est question du passage du système décimal au `système binaire`, ainsi que des problématiques de traitement des données telles que `l'encodage`, `la compression`, `l'échantillonnage`, `le cryptage`, et la `représentation des caractères, des images et des sons` sous forme de bits. 

🟡 [Introduction à l'algorithmique](content/theme/introduction-algorithmique)
: Ce chapitre propose une `définition générale de l'algorithmique`, ainsi qu'une présentation de certains `algorithmes classiques`. 

🟢 [Introduction à la programmation](content/theme/introduction-programmation)
: Après avoir présenté un échantillon de langages de programmation et leurs différences respectives, ce chapitre `pose les bases du language Python`. 

🔵 [Architecture des ordinateurs](content/theme/architecture-ordinateurs)
: Il est question ici de notions telles que `les portes logiques`, `les transistors`, `l'architecture de Von Neumann`, et autres concepts essentiels à la compréhension de ce qui se passe au niveau physique et électronique dans un ordinateur.

## Modification indépendante des ressources

````{panels}
:column: col-lg-12 p-3
⚠️ Attention
^^^^
Ceci est une procédure simplifiée. La procédure détaillée est disponible {ref}`ici <ajouter référence>` (réf à ajouter). 
````

Les ressources sont diffusées selon le modèle open-source, qui veut que tout utilisateur ait accès aux documents d'origine, et puisse les transformer à sa guise. Pour ce faire, un accès au dépôt Github contenant les documents sources est disponible en haut à droite de la fenêtre de navigation. 

L'idée d'une **modification indépendante des ressources** est de vous approprier n'importe quel morceau de ces ressources, le remixer, en faire ce que vous voulez, et utiliser le résultat là où vous le désirez. Cette utilisation n'implique aucune interaction avec la version *originale* des ressources présentée ici. Vous êtes libre d'utiliser cette matière comme vous le souhaitez, pour peu que vous respectiez les usages de {ref}`la licence choisie <licenceduprojet>`. 

![iconeGit](images/presentation/iconegit.png)

La marche à suivre pour y accéder est la suivante : 

1. Créer un compte Github ou se connecter à un compte déjà existant. 
2. Ouvrir le dépôt [edunum-sec2](https://github.com/edunum-sec2/ressources).
3. Cloner le dépôt selon la [marche à suivre Github](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository). 
4. [Créer une branche](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-and-deleting-branches-within-your-repository#:~:text=Further%20reading-,Creating%20a%20branch,main%20page%20of%20the%20repository.&text=Click%20the%20branch%20selector%20menu,branch%2C%20then%20select%20Create%20branch.)  pour manipuler les fichiers, si besoin. 
5. Créditer, selon la licence CC décrite ci-dessus, les éventuelles publications issues de la transformation des fichiers sources. 

## Participation au développement

Les ressources sont pensées comme un "work in progress". Elles se veulent flexibles, adaptables, et bénéficieront de tous les apports des personnes concernées. Le groupe de travail considère qu'il est important que toute enseignante ou enseignant de la matière `informatique` se sente libre de contribuer au à l'amélioration des ressources. 

Pour contribuer au projet, suivre la `marche à suivre installation`.

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

 4. Installer [Jupyter Book](https://jupyterbook.org)
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
      
      Accepter l'installation de ces recommandations à l'ouverture du workspace:
      
      ![](images/presentation/extension_recommendations.png)

    * Si l'installation des extensions ne vous est pas proposée, le faire manuellement via l'interface graphique de VS Code ou via le terminal:
      ```bash
      code --install-extension <extension-id>
      ```


::::{caution} Mises à jour
N'oubliez pas de contrôler que les mises à jour des différents environnements et extensions soient toujours faites. 
::::

### Build

**Pour produire l'output HTML statique depuis les fichiers source**

Avec VS Code si installé comme ci-dessous, cliquer sur un des boutons en bas de la fenêtre:

![](images/presentation/build_screenshot.png)

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
(licenceduprojet)=
## Licence du projet

Les ressources sont publiées sous licence Creatives Commons `Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions (CC BY-NC-SA)`. Cela signifie qu'elles peuvent être copiées, transformées, adaptées, et diffusées, hormis à des fins commerciales, tant qu'elles créditent le groupe de travail présenté ci-dessus, et qu'elles utilisent la même licence pour le partage futur. Les conditions sont disponibles [ici](https://creativecommons.org/licenses/?lang=fr). 

![licence](images/presentation/by-nc-sa.png)

Toute personne qui réutilise les ressources est priée de le faire de la façon suivante : 

* 💰 Pas d'utilisation commerciale. 
* ♻️ Possibilité de modifier les ressources à souhait. 
* 📗 Crédit : "Par le groupe de travail DGEP, EPFL, HEP, UNIL". 
* 🤝 Partage selon les mêmes conditions. Donc en ajoutant simplement le logo ci-dessus pour toute publication éventuelle. 

## Exécution des cellules interactives

Certains chapitres de ces ressources comprennent des contenus exécutables directement dans une fenêtre du navigateur. C'est le cas, par exemple, du chapitre introduction à la programmation. 

Dans ce cas, une icône supplémentaire apparaît dans le menu en haut à droite, qui permet d'ouvrir un environnement en ligne permettant d'exécuter des cellules de code. 

![Binder](images/presentation/iconebinder.png)

## {ref}`Syntaxe MyST <syntaxemyst>`

Les documents originaux des ressources sont écrits dans un language appelé [**MyST**](https://myst-parser.readthedocs.io/en/latest/using/syntax.html), pour Markedly Structured Text. 

[**MyST**](https://myst-parser.readthedocs.io/en/latest/using/syntax.html) est une fusion entre la syntaxe Markdown et le language utilisé par le générateur de documentation [Sphinx](https://fr.wikipedia.org/wiki/Sphinx_(g%C3%A9n%C3%A9rateur_de_documentation)#:~:text=Sphinx%20est%20un%20g%C3%A9n%C3%A9rateur%20de,%2C%20Urwid%2C%20ou%20encore%20Bazaar.). 

Une version allégée de la syntaxe est disponible {ref}`ici <syntaxemyst>`.

````{admonition} Important
:class: note
La version de MyST utilisée dans ce projet est celle qui a été adaptée pour le projet [jupyter{book}](https://jupyterbook.org/intro.html). 
````

## jupyter{book}

Les ressources sont affichées sous la forme du site statique ici-présent par l'intermédiaire des scripts ayant été développés dans le cadre du projet [jupyter{book}](https://jupyterbook.org/intro.html). 

[jupyter{book}](https://jupyterbook.org/intro.html) est un projet open-source initialement prévu pour créer un site html statique à partir d'une collection de [notebooks jupyter](https://jupyter.org/). Les avantages de cette solution sont multiples, mais en particulier elle offre la possibilité de présenter sur un site html statique des cellules de code exécutables. 


{fa}`heart, text-success mr-1` Fait avec amour par le `groupe de travail DGEP, EPFL, HEP, UNIL`. 