# Introduction
<!--- Architecture des Ordinateurs --->
## Contexte historique

Dans ce chapitre, nous nous intéressons à comment sont construits les ordinateurs pour faire le travail qu'ils font.

Le chapitre TODO(LIEN) Représentation de l'information nous a appris que toutes les données que traitent les ordinateurs sont, d'une manière ou d'une autre, représentée par une suite de _bits_, de 0 et 1 — que l'on parle de nombres, d'image, de sons, etc. Dans ce chapitre, nous examinons d'un peu plus près comment ces bits traversent la machine. Nous parlons d'abord des circuits électroniques et d'un de leurs consituants fondamentaux, les portes logiques. Avec les portes logiques, nous montrons comment nous pouvons traiter de manière élémentaire 1 ou 2 bits à la fois. Petit à petit, nous découvrons comment un assemblage de ces portes logiques peut nous aider à réaliser une opération plus concrète avec l'exemple de l'addition de deux petits nombres représentés en binaire. Cela nous montre comment un circuit électronique peut réaliser une opération arithmétique.

Les ordinateurs savent faire plusieurs opérations. Nous parlerons de ce qu'est une unité arithmétique et logique en tant que composante servant à choisir l'opération à effectuer par l'ordinateur. Pour aller plus loin, nous aurons besoin de savoir comment l'ordinateur stocke les bits en expliquant comment sa mémoire fonctionne. Finalement, nous savons qu'un ordinateur exécute des programmes: nous verrons comment un microprocesseur simple fonctionne, en lisant une à une les instructions d'un programme dans la mémoire de l'ordinateur, et utilise ses circuits arithmétiques et logiques pour les exécuter.


````{panels}
:column: col-lg-12 p-2

**Contexte historique**
^^^^
La deuxième guerre mondiale joue un rôle décisif dans le développement des technologies de l'information. Deux besoins stratégiques révèlent les enjeux de l'informatique: la cryptologie[^1] et les calculs de simulation pour la balistique par exemple.

Dans ce contexte apparaissent les premières machines de traitement automatique de l'information. Les *bombes* d'**Alan Turing** permettent le decryptage des messages nazi chiffrés avec la machine *enigma* et fonctionnent avec des composants électroméchaniques. La défense aérienne anglaise développe le radar avec les *utbes électroniques* qui deviennent naturellement les  composants des premiers ordinateurs comme l'ENIAC (1945) spécifiquement dédié à des calculs balistiques. Dès le milieu des années 1950, ils seront remplacés par des transistors et ensuite des circuits intégrés. Tous ces éléments constituent les briques de base des systèmes logiques que nous allons examiner plus en détail dans une première partie.

John von Neumann est mathématicien et physicien qui contribuera à de nombreux domaines scientifiques et en particulier à l'essort de l'informatique. Il sera également un acteur important du projet Manhattan et la fabrication de la première bombe atomique. En juin 1945, il publie un article dans lequel il décrit une architecture d'ordinateur qui est encore celle utilisée aujourd'hui.

Les premiers microprocesseurs sont inventés chez Intel en 1969 (société fondée en 1968). Le premier modèle ne travaille que sur un demi-octet, mais il est rapidement remplacé par des microprocesseurs 8 bits comme le 8008 chez Intel, qui sera à son tour remplacé par le 8080 et tout la série des x86 qui dominent encore la marché de la microinformatique aujourd'hui.


````

````{panels}

**Alan Turing**

^^^^

short bio + photo


----

**John Von Neumann**

^^^^

short bio + photo
<!--img src=media/JohnvonNeumann-LosAlamos.jpg-->

++++

```{link-button} https://fr.wikipedia.org/wiki/John_von_Neumann
:text: Wikipedia
:type: url
:classes: stretched-link

```

````

[^0]: La cryptologie est la science qui regroupe la Cryptanalyse qui est le décodage des message encodés et la Cryptographie qui recouvre toutes les activités de chiffrement des messages pour les protéger.
