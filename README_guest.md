# Présentation des ressources

Les ressources pour l'enseignement de la branche *Informatique* au niveau secondaire II ont été produites par le `groupe de travail DGEP, EPFL, HEP, UNIL`, dans le cadre du projet **EduNum** du canton de Vaud. Leur objectif est la mise à disposition de contenus théoriques, de séries d'exercices, et d'idées d'activités pour les enseignantes et enseignants de ladite matière au Gymnase. 

---

- [Présentation des ressources](#présentation-des-ressources)
  - [:dart: Usages](#dart-usages)
  - [:file_folder: Chapitrage](#file_folder-chapitrage)
  - [:pencil: Licence](#pencil-licence)
  - [:rocket: Exécution des cellules interactives](#rocket-exécution-des-cellules-interactives)
  - [:bulb: Syntaxe MyST](#bulb-syntaxe-myst)
- [Exemples d'utilisation des ressources](#exemples-dutilisation-des-ressources)
  - [:computer:	Utilisation en ligne](#computer-utilisation-en-ligne)
  - [:printer: Utilisation print](#printer-utilisation-print)
  - [:key: Modifications indépendantes](#key-modifications-indépendantes)
  - [:dna: Participation au développement](#dna-participation-au-développement)
  

## :dart: Usages 

Voici une liste non-exhaustive des usages potentiels de ces ressources : 

:white_check_mark: **Rafraîchir vos connaissance dans les domaines du plan d'études**
: Ces ressources ont été rédigées en accord avec le plan d'études *informatique* pour le secondaire II. 

:white_check_mark: **Vous inspirer du fil rouge des différents chapitres**
: Les *introductions* aux chapitres, par exemple, abordent la matière sous un angle peut-être différent de celui avec lequel vous avez l'habitude d'enseigner. 

:white_check_mark: **Découvrir des idées d'activités à faire en classe**
: De nombreuses activités sont disponibles à l'intérieur de chacun des chapitres pour vous aider à mettre en place des séquences de cours interactives. 

:white_check_mark: **Faire le plein d'exercices pour tester vos leçons**
: Une base de données d'exercice est à disposition dans la section concernée. 

:white_check_mark: **Imprimer les ressources depuis une version PDF**
: Si vous êtes intéressés par un morceau de cours en particulier, vous pouvez l'imprimer directement depuis votre navigateur. 

:white_check_mark: **Consulter les fichiers sources directement**
: Le projet est construit sur un modèle open-source, ce qui vous permet d'aller chercher les documents originaux, en format brut, directement ici. 

:white_check_mark: **Exécuter des cellules de code dans le navigateur grâce à Binder**
: Si vous souhaitez faire travailler vos élèves sur des machines, l'option Binder vous permet d'exécuter des cellules de code sans devoir pré-configurer l'environnement. 

:white_check_mark: **Contribuer au développement et à l'amélioration de du projet**
: Comme tout projet, celui-ci possède ses avantages et ses inconvénients. C'est pour bénéficier de votre expterise que nous avons construit ce projet sur un modèle open-source avec la possibilité à tout moment de le forker, de le transformer, ou d'y contribuer en utilisant l'infrastructure offerte par Github. 

## :file_folder: Chapitrage

Les ressources sont découpées selon un chapitrage qui correspond au plan d'études romand (ajouter réf). Elles sont divisées en quatre parties, dont nulle n'a de préseance sur les autres. Il appartient à l'enseignante ou l'enseignant de choisir l'ordre dans lequel les contenus sont abordés. Le fait que les chapitres soient successifs est le résultat des limitations de l'affichage. Pour atténuer quelque peu ce problème nous avons choisi de renoncer à une numérotation des chapitres. 

🟠 [Représentation de l'information](theme/representation-information/eleve.md)
: Où il est question du passage du système décimal au `système binaire`, ainsi que des problématiques de traitement des données telles que `l'encodage`, `la compression`, `l'échantillonnage`, `le cryptage`, et la `représentation des caractères, des images et des sons` sous forme de bits. 

🟡 [Introduction à l'algorithmique](content/theme/introduction-algorithmique)
: Ce chapitre propose une `définition générale de l'algorithmique`, ainsi qu'une présentation de certains `algorithmes classiques`. 

🟢 [Introduction à la programmation](content/theme/introduction-programmation)
: Après avoir présenté un échantillon de langages de programmation et leurs différences respectives, ce chapitre `pose les bases du language Python`. 

🔵 [Architecture des ordinateurs](content/theme/architecture-ordinateurs)
: Il est question ici de notions telles que `les portes logiques`, `les transistors`, `l'architecture de Von Neumann`, et autres concepts essentiels à la compréhension de ce qui se passe au niveau physique et électronique dans un ordinateur.

## :pencil: Licence

Les ressources sont publiées sous licence Creatives Commons `Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions (CC BY-NC-SA)`. Cela signifie qu'elles peuvent être copiées, transformées, adaptées, et diffusées, hormis à des fins commerciales, tant qu'elles créditent le groupe de travail présenté ci-dessus, et qu'elles utilisent la même licence pour le partage futur. Les conditions sont disponibles [ici](https://creativecommons.org/licenses/?lang=fr). 

![licence](.../content/demostests/edito/images/presentation/by-nc-sa.png)

Toute personne qui réutilise les ressources est priée de le faire de la façon suivante : 

* 💰 Pas d'utilisation commerciale. 
* ♻️ Possibilité de modifier les ressources à souhait. 
* 📗 Crédit : "Par le groupe de travail DGEP, EPFL, HEP, UNIL". 
* 🤝 Partage selon les mêmes conditions. Donc en ajoutant simplement le logo ci-dessus pour toute publication éventuelle. 

## :rocket: Exécution des cellules interactives

Certains chapitres de ces ressources comprennent des contenus exécutables directement dans une fenêtre du navigateur. C'est le cas, par exemple, du chapitre introduction à la programmation. 

Dans ce cas, une icône supplémentaire apparaît dans le menu en haut à droite, qui permet d'ouvrir un environnement en ligne permettant d'exécuter des cellules de code. 

![Binder](images/presentation/iconebinder.png)

## :bulb: Syntaxe MyST

Les documents originaux des ressources sont écrits dans un language appelé [**MyST**](https://myst-parser.readthedocs.io/en/latest/using/syntax.html), pour Markedly Structured Text. 

[**MyST**](https://myst-parser.readthedocs.io/en/latest/using/syntax.html) est une fusion entre la syntaxe Markdown et le language utilisé par le générateur de documentation [Sphinx](https://fr.wikipedia.org/wiki/Sphinx_(g%C3%A9n%C3%A9rateur_de_documentation)#:~:text=Sphinx%20est%20un%20g%C3%A9n%C3%A9rateur%20de,%2C%20Urwid%2C%20ou%20encore%20Bazaar.). 

# Exemples d'utilisation des ressources

## :computer:	Utilisation en ligne

1. Je reçois le lien des ressources en ligne. 
2. Je parcours la documentation pour comprendre le projet dans son ensemble, en commençant par le chapitre {ref}`présentation des ressources <presentationressources>`.
3. Je navigue à travers les différents chapitres du cours. 
4. Si une information m'intéresse, par exemple une anecdote historique, un angle d'attaque pour une notion, un exemple particulier, voire même une séquence entière de cours théorique, je prends des notes et la réutilise à souhait dans mes leçons. 
5. Je parcours les idées d'activité et je choisis celles qui m'intéressent. 
6. J'utilise les séries d'exercice à disposition comme "devoirs" pour mes élèves. 
7. Je demande à mes élèves de lire certains chapitres en préparation des cours. Je reprends les notions essentielles en classe.  

## :printer: Utilisation print

1. À tout moment, je peux utiliser la fonction print des ressources, pour en extraire certains contenus. 

````{image} images/utilisation/print.png
````

## :key: Modifications indépendantes

1. Si certains contenus m'intéressent, mais que je considère qu'ils pourraient être transformés pour être plus efficaces, je peux à tout moment aller consulter les fichiers sources. 

![iconeGit](images/presentation/iconegit.png)

2. {ref}`Je m'inscris sur Github <modificationindependante>`.
3. Je retrouve le chapitre qui m'intéresse. 
4. Je télécharge le fichier source. 
5. Je le retravaille pour en faire ma propre version. 

## :dna: Participation au développement

1. Je me réfère au chapitre suivant pour l'installation de l'environnement : README.md (sur la page d'accueil du dépôt).
2. Une fois que l'environnement est installé, plusieurs options s'offrent à moi. 
3. Je peux travailler à l'amélioration des ressources en tant que `correcteur`. Dans ce cas, j'utilise la fonction de commentaires de Github (à détailler selon procédure choisie), j'ouvre des `issues`, je commente les `issues` des autres, et j'apporte des modifications aux texte sources qui me paraissent importantes. 
4. Je peux travailler en tant que `rédacteur`. Dans ce cas je propose des contenus originaux - séquences théoriques, activités, séries d'exercices, et je les soumets au reste des utilisateurs pour validation. 
5. Je peux aussi créer une `branche` du projet total, et la partager par la suite avec l'ensemble des utilisateurs des ressources dans la rubrique `spin-off des ressources`. 
