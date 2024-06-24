# Suivi sur le web

Cela n’a pas pu vous échapper, le web moderne est rempli de "**{glo}`tracker@2|traqueurs`**", de "**publicité ciblée**" et de "**collecte de données**". Selon [The Economist, en 2017](https://www.economist.com/leaders/2017/05/06/the-worlds-most-valuable-resource-is-no-longer-oil-but-data), "**La ressource la plus précieuse du monde n’est plus le pétrole, mais les données**", mais comment les données sont-elles collectées ? Comment fonctionne ce marché ? Quels sont les risques pour la vie privée ? Quelles sont les bonnes pratiques à adopter en matière de sécurité et vie privée sur le web ? Cette activité va vous guider pour comprendre le fonctionnement technique et économique de cette industrie, et quelles pratiques adoptées pour limiter les risques de sécurité et d’atteinte à la vie privée.

```{admonition} Un ensemble de 4 activités
:class: note
Cette activités se découpe en 4 sous activités construites pour fonctionner en cohérence mais également réalisables indépendemment. Libre à vous d'en effectuer une, plusieurs ou toutes pour couvrir la séquence.

Cette page regroupes les informations générales sur les 4 activités, notamment avec les [](webtracking.didactique) associées.
```

```{admonition} Notice
:class: hint

* **Thème** : `Réseaux` (transversal avec `Vie privée et surveillance` et `Économie du numérique`)
* **Niveau** : `moyen` <!-- L’activité n’est pas facile, car elle demande une certaine supervision de l’enseignant·e et car les outils sont probablement inconnus des élèves. Elle n’est toutefois pas difficile car rien n’est à installer, l’activité peut se faire sans outil autre que l’ordinateur et le navigateur ce qui en simplifie l’accessibilité. Les objectifs sont d’une complexité notable mais peu exigeants sur les pré-requis et la technicité. Dépendant de l’aise des élèves et de l’avancée dans le chapitre Web, l’activité prévoit de revoir les points essentiels du web à comprendre pour effectuer l’activité à tout niveau. -->
* **Durée** : 4 périodes (1 séance de 45 minutes débranchées, 1 séance de 90 minutes branchée et une dernière séance de 45 minutes débranchées)
* **Objectifs pédagogiques** : les objectifs de cette séquence sont associés à ceux du chapitre Réseaux, notamment `sécurité et sensibilisation aux bonnes pratiques; notions et modèles d’architectures et de protocoles`. De plus, les objectifs transversaux d’enjeux sociaux sont visés notamment `vie privée et surveillance; économie du numérique`. Plus d’explications sont données dans la partie [](webtracking.didactique)
* **Modalité** : `branché` et `débranché`
* **Matériel** : Ordinateur et navigateur web
* **Prérequis** : Il est préférable d’avoir étudié les éléments du chapitre [World Wide Wide](https://apprendre.modulo-info.ch/resx/web.html). Cette activité le complète (éventuellement conclut) et lui apporte une activité pratique. L’activité {ref}`encheres` ou équivalent sur le fonctionnement de la publicité ciblée est également requis pour comprendre la présence des acteurs et des enjeux (ceci pourrait s’intégrer dans une séance préliminaire débranchée)
* **Notions fondamentales** : Les technologies du web et leur fonctionnement, l’{glo}`adtech|Ad Tech` et l’économie du web, les concepts et l’évaluation de vie privée du numérique, la compréhension d’une trace réseau, la modélisation d’une interaction sur le web avec l’association à des entités et leurs intérêts
* **Taille du groupe** : `classe entière` pour les séquences débranchées et `demi-classe` pour les séquences branchées

```

## Déroulement

|                                             | Phase de l’activité                               |
| ------------------------------------------- | ------------------------------------------------- |
| [](webtracking.accroche)                    | Mise en situation (débranché)                     |
| [](<webtracking.interractionressourcesweb>) | Apprentissage - Institutionnalisation (débranché) |
| [](<webtracking.theorietracereseau>)        | Apprentissage (branché)                           |
| [](<webtracking.observationdetracereseau>)  | Application (branché)                             |
| [](<webtracking.tracereseauetsuivi>)        | Exploration (branché)                             |
| [](<webtracking.analysecomplete>)           | Objectivation et Évaluation (branché)             |
| [](<webtracking.proprietevieprivee>)        | Institutionnalisation (débranché)                 |
| [](<webtracking.commerceweb>)               | Institutionnalisation (débranché)                 |
| [](<webtracking.protection>)                | Apprentissage (débranché)                         |
| [](<webtracking.reinvestissement>)          | Réinvestissement (débranché)                      |

<!-- *Note : le moment didactique dans lequel se situe l’étape est optionnel*
Liste des phases à choix possibles pour la dernière colonne du tableau ci-dessus:

- Mise en situation
- Enseignement frontal
- Exploration
- Apprentissage
- Application
- Objectivation
- Institutionnalisation
- Évaluation
- Réinvestissement
- Discussion -->

(webtracking.didactique)=

## Considérations didactiques

Cette activité a été conçue dès le départ avec l’idée en tête d’en faire une activité axée sur **l’alignement curriculaire** autour du plan d’étude vaudois. Notamment, le but de cette tâche est de la créer en résonance d’une **tâche d’évaluation sommative authentique**, qui évalue des **compétences cognitives élevées** chez les élèves et s’inscrive dans une **boucle de rétro-action** avec l’enseignant·e pour aider et attester de l’acquisition de compétences.

Cette partie présente donc **les objectifs identifiés du plan d’étude** que la tâche cherche à faire atteindre, et les met en perspective avec des **critères d’évaluation** qui seraient applicables pour une évaluation sommative suivant cette séquence.

### Référenciation restreinte du plan d’étude

#### Objectifs généraux

**Objectifs généraux** du cursus gymnasial en informatique

- Compétence
  - Prendre des décisions fondées sur des connaissances techniques
  - Identifier et analyser quelques enjeux sociaux et politiques du numérique
- Savoirs
  - Principes de communication de l’information
  - Modéliser et simuler
- Savoir-Faire
  - Développer une réflexion autour des enjeux socio-politiques du numérique
- Attitude
  - Esprit critique

**Objectifs généraux de deuxième année** en informatique

- Réseaux : sécurité et sensibilisation aux bonnes pratiques; notions et modèles d’architectures et de protocoles
- Enjeux de société : vie privée et surveillance; économie du numérique

#### Objectifs spécifiques

- Applique
  - L’élève sait lancer, manipuler et utiliser un logiciel d’analyse de trafic réseau pour présenter des éléments d’une trace en les identifiant avec le vocabulaire adapté du réseau
- Analyse
  - L’élève peut décrire et/ou schématiser sa représentation des processus en cours lors d’une communication réseau
  - L’élève peut développer une analyse d’une communication réseau en mettant en avant des risques pour la vie privée et la sécurité des communications en pointant sur des informations sensibles et peut classer ces éléments selon : la confidentialité, le pseudonymat, l’anonymat et la dissociabilité
  - L’élève peut déterminer les acteurs impliqués dans l’établissement d’une connexion réseau et identifier la position de chacun en ce qui concerne les risques de la vie privée et les enjeux économique
- Évalue
  - L’élève peut évaluer si les besoins d’accès aux données/de communication d’une application sont justifiés ou non pour l’usage qu’il/elle en ferait et peut juger des mécanismes à mettre en place pour se protéger ou proposer des alternatives à rechercher
  
### Tâche d’évaluation sommative

#### Critères obligatoires (nécessaires pour avoir 4)

- *Technique et application*
  - L’élève est capable d’**ouvrir un outil de capture de réseau** (p. ex. outil de capture d’un navigateur, Wireshark, tcpdump, ...). Iel connaît la **manipulation** nécessaire et peut, au besoin, s’aider de recherches autonomes sur le web (en validant un acquis du vocabulaire lié au réseau) mais sans l’aide externe de l’enseignant·e
  - L’élève peut **naviguer sur différents site web en capturant et identifiant** les différentes **communications réseaux** faites par son navigateur via : leur destination, le contenu de leurs cookies, ou d’autres **attributs utiles pour évaluer la pertinence économique et de tracking de cette communication**
- *Analyse de communication : vie privée et économie*
  - En observant une trace réseau, l’élève peut **identifier des processus** en cours et **modéliser** (par description ou schématiquement) **le système sous-jacent** avec ses acteurs et leurs interactions
  - L’élève peut se rendre sur un site donné au préalable et **identifier une potentielle menace de la vie privée** qu’iel déterminera en **sélectionnant avec pertinence des informations provenant d’une trace réseau**
  - L’élève peut justifier en quoi une menace de la vie privée concerne plus ou moins les domaines de la **confidentialité, le pseudonymat, l’anonymat et/ou la dissociabilité**
  - L’élève peut consulter une trace réseau donnée et **identifier des acteurs économiques en jeux** dans la communication parmi le **fournisseur de service, le service d’analyse, l’intermédiaire publicitaire, le revendeur de produit et le client** et fournir une explication du fonctionnement du financement en lien avec la trace observée
- *Sécurité et bonnes pratiques*
  - Étant donnée des risques pour la vie privée identifiés à partir d’une trace réseau, l’élève peut **déterminer un type d’outil permettant d’éliminer un risque** et **justifier de la capacité de l’outil à faire cela**

#### Critères de perfectionnement

- Pour chacun des critères obligatoires, l’élève est capable de fournir le travail pour plusieurs traces réseaux ayant chacune des caractéristiques différentes (sites différents, menaces différentes, acteurs variés ou centralisés, ...)

## Liens avec les autres thématiques

### Économie du numérique

- **L’activité "Enchère du numérique"** est clairement en lien puisque expliquant le fonctionnement et les acteurs de la publicité en ligne. Elle met notamment en avant la raison économique **motivant la collecte de données** pour permettre de faire des publicités plus ciblées et donc plus efficaces économiquement

### Surveillance et vie privée

- Toute l’activité, dès son accroche, fait écho aux discussions de ce chapitre, notamment le débat sur **"Rien à cacher ?"**, et approfondit l’explication concrète des **"Traces numériques"**

### Numérique et environnement

- Comme mentionné dans le dossier, l’**impact environnemental de la publicité ciblée** est non négligeable ! Comme vu avec la base de données de la partie [](webtracking.tracereseauetsuivi), il est possible de voir la quantité du trafic (en MB et en pourcentage de contenu chargé par la page) dédiée au suivi et à la publicité ciblée.
- De même, dans la partie [](webtracking.protection), les extensions discutées fournissent pour la plupart des **rapports sur le nombre de publicités ciblées bloquées**, et éventuellement le temps de chargement économisé ou la taille des fichiers non-téléchargés. Cela peut aider à se rendre compte de **l’impact en taille et temps informatique de la publicité ciblée**

### Réseau : interopérabilité

- Dans la partie [](webtracking.protection), il est mentionné que la protection de la vie privée doit passer par des technologies agissant à **différents niveaux de la couche OSI** et que notamment, les cookies et le VPN agissent à différents niveaux. En effet, il est pertinent de mentionner que **la sécurité en général doit être considérée aux différents niveaux de couches**, créant des liens intéressants avec la partie réseaux

(webtracking.ressources)=

## Ressources complémentaires

### L’anonymat : une propriété utopique

- Le youtubeur Micode montre comment il fait pour joindre des informations pour retrouver des informations sur quelqu’un à partir d’une photo : un bon exemple de **la complexité d’être anonyme sur internet** - <https://www.youtube.com/watch?v=udYtHVEwbYA>
- Le youtubeur Great Review raconte l’histoire de l’œuvre "He will not divide us" et son lien avec le forum 4Chan qui a utilisé des données publiques pour retrouver l’œuvre d’art à travers le monde : de nouveau, **il est dur d’être anonyme sur internet** - <https://www.youtube.com/watch?v=jDU1uywsoaM>

### Le suivi sur internet

- Un blog post de l’entreprise SurfShark pour expliquer **leur protocole de mesure de la présence de traqueurs** sur un ensemble de site web populaires - <https://surfshark.com/whos-tracking-you>
- Un article de la BBC décrivant comment **cliquer sur un lien depuis Google informe des tiers** - <https://www.bbc.com/news/technology-49593830>
- Une petite BD résumant **le fonctionnement du suivi sur le web** - <https://www.freecodecamp.org/news/what-you-should-know-about-web-tracking-and-how-it-affects-your-online-privacy-42935355525/>

### Le fingerprinting

- Tester **son empreinte numérique** - <https://www.amiunique.org/> ou <https://coveryourtracks.eff.org/>
- Tester le fonctionnement de l’empreinte numérique, **moyen d’identification unique sans cookies** - <https://nothingprivate.gkr.pw/> et leur code source <https://github.com/gautamkrishnar/nothing-private>

```{toctree}
:maxdepth: 1
:hidden:
Le suivi - l'affaire de tou·te·s <suivi-affaire-tous>
Les technologies du web <techno-web>
Analyse de requêtes <analyse-requetes>
Comprendre et se protéger <se-proteger>
```
