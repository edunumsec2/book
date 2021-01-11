# Présentation des ressources

Les ressources pour l'enseignement de la branche *Informatique* au niveau secondaire II ont été produites par le `groupe de travail DGEP, EPFL, HEP, UNIL`. Leur objectif est la mise à disposition de contenus théoriques, de séries d'exercices, et d'idées d'activités pour les enseignantes et enseignants de ladite matière. 

## Licence

Les ressources sont publiées sous licence Creatives Commons `Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions (CC BY-NC-SA)`. Cela signifie qu'elles peuvent être copiées, transformées, adaptées, et diffusées, hormis à des fins commerciales, tant qu'elles créditent le groupe de travail présenté ci-dessus, et qu'elles utilisent la même licence pour le partage futur. Les conditions sont disponibles [ici](https://creativecommons.org/licenses/?lang=fr). 

![licence](images/presentation/by-nc-sa.png)

## Modification des ressources

Les ressources sont diffusées selon le modèle open-source, qui veut que tout utilisateur ait accès aux documents d'origine, et puisse les transformer à sa guise. Pour ce faire, un accès au dépôt Github contenant les documents sources est disponible en haut à droite de la fenêtre de navigation. 

![iconeGit](images/presentation/iconegit.png)

La marche à suivre pour y accéder est la suivante : 

1. Créer un compte Github ou se connecter à un compte déjà existant. 
2. Ouvrir le dépôt [edunum-sec2](https://github.com/edunum-sec2/ressources).
3. Cloner le dépôt selon la [marche à suivre Github](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository). 
4. [Créer une branche](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-and-deleting-branches-within-your-repository#:~:text=Further%20reading-,Creating%20a%20branch,main%20page%20of%20the%20repository.&text=Click%20the%20branch%20selector%20menu,branch%2C%20then%20select%20Create%20branch.).  pour manipuler les fichiers, si besoin. 
5. Créditer, selon la licence CC décrite ci-dessus, les éventuelles publications issues de la transformation des fichiers sources. 

## Participation au développement

Les ressources sont pensées comme un "work in progress". Elles se veulent flexibles, adaptables, et bénéficieront de tous les apports des personnes concernées. Le groupe de travail considère qu'il est important que toute enseignante ou enseignant de la matière `informatique`se sente libre de faire des retours et de suggérer des améliorations au produit présenté ici. 

Pour ce faire, la marche à suivre est la suivante : 

1. Créer un compte Github ou se connecter à un compte déjà existant. 
2. Ouvrir le dépôt [edunum-sec2](https://github.com/edunum-sec2/ressources).
3. Ouvrir une "issue" dans le dépôt concerné, selon les [directives suivantes](https://docs.github.com/en/free-pro-team@latest/github/managing-your-work-on-github/creating-an-issue). 

## Exécution des cellules interactives

Certains chapitres de ces ressources comprennent des contenus exécutables directement dans une fenêtre du navigateur. C'est le cas, par exemple, du chapitre introduction à la programmation. 

Dans ce cas, une icône supplémentaire apparaît dans le menu en haut à droite, qui permet d'ouvrir un environnement en ligne permettant d'exécuter des cellules de code. 

![Binder](images/presentation/iconebinder.png)


## Chapitrage

Les ressources sont découpées selon un chapitrage qui correspond au plan d'études (ajouter réf). Elles sont divisées en quatre parties, dont nulle n'a de préseance sur les autres. Il appartient à l'enseignante ou enseignant de choisir l'ordre dans lequel les contenus seront abordés. Le fait que dans la version présente les chapitres soient successifs est le résultat des limitations de l'affichage. Pour atténuer quelque peu ce problème nous avons choisi de renoncer à des numéros de chapitre. 

Les chapitres, ainsi qu'un résumé de leur contenu, sont : 

1. **Représentation de l'information**. Où il est question du passage du système décimal au `système binaire`, ainsi que des problématiques de traitement des données telles que `l'encodage`, `la compression`, `l'échantillonnage`, `le cryptage`, et la `représentation des caractères, des images et des sons` sous forme de bits. 
2. **Introduction à l'algorithmique**. Ce chapitre propose une `définition générale de l'algorithmique`, ainsi qu'une présentation de certains `algorithmes classiques`. 
3. **Introduction à la programmation**. Après avoir présenté un échantillon de langages de programmation et leurs différences respectives, ce chapitre `pose les bases du language Python`. 
4. **Architecture des ordinateurs**. Il est question ici de notions telles que `les portes logiques`, `les transistors`, `l'architecture de Von Neumann`, et autres concepts essentiels à la compréhension de ce qui se passe au niveau physique et électronique dans un ordinateur.

## {ref}`Syntaxe MyST <syntaxemyst>`

Les documents originaux des ressources sont écrites dans un language appelé [**MyST**](https://myst-parser.readthedocs.io/en/latest/using/syntax.html), pour Markedly Structured Text. 

[**MyST**](https://myst-parser.readthedocs.io/en/latest/using/syntax.html) est une fusion entre la syntaxe Markdown et le language utilisé par le générateur de documentation [Sphinx](https://fr.wikipedia.org/wiki/Sphinx_(g%C3%A9n%C3%A9rateur_de_documentation)#:~:text=Sphinx%20est%20un%20g%C3%A9n%C3%A9rateur%20de,%2C%20Urwid%2C%20ou%20encore%20Bazaar.). 

Une version allégée de la syntaxe est disponible {ref}`ici <syntaxemyst>`.

````{admonition} Important
:class: note
La version de MyST utilisée dans ce projet est celle qui a été adaptée pour le projet [jupyter{book}](https://jupyterbook.org/intro.html). 
````

## jupyter{book}

Les ressources sont affichées sous la forme du site statique ici-présent par l'intermédiaire des scripts ayant été développés dans le cadre du projet [jupyter{book}](https://jupyterbook.org/intro.html). 

[jupyter{book}](https://jupyterbook.org/intro.html) est un projet open-source initialement prévu pour créer un site html statique à partir d'une collection de [notebooks jupyter](https://jupyter.org/). Les avantages de cette solution sont multiples, mais en particulier elle offre la possibilité de présenter sur un site html statique des cellules de code compilables. 


