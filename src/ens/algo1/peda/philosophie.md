# Algorithmique I 

## Philosophie 

### Partie « Apprendre » 

La partie « Apprendre » a été conçue pour être utilisable de manière autonome par les élèves.

Au niveau de la durée, chaque chapitre est conçu comme un **cours de 2 périodes** ou de 90 minutes. Ces chapitres **ne sont pas à faire dans leur entièreté**. L'hétérogénéité des élèves étant importante en informatique, nous avons prévus des **contenus optionnels**, souvent sous la forme d'exercices supplémentaires ou d'encarts "pour aller plus loin".  

Le troisième chapitre, « Des algorithmes aux programmes », ne peut être traité qu'après avoir vu le thème programmation, car il fait le lien entre les algorithmes et les programmes.

<div id="philosophie"></div>

### Cadre des « Cinq Co »

Pour écrire le chapitre Algorithmique, nous avons suivi le cadre des « Cinq Co ». Ce cadre consiste en cinq composantes (voir figure ci-dessus) qui commencent par des aspects généraux pour se rapprocher de plus en plus vers l’élève :

<img src="Schéma_co_2.png">

1. **Cohérence**, ou raconter une histoire cohérente. Le choix d’aborder l’algorithmique par les algorithmes de tri a été motivé par l’envie de raconter une histoire unique et cohérente, une sorte de fil rouge multi-usages, qui couvrirait tous les objectifs pédagogiques. En effet, même si les algorithmes de tri peuvent paraître fastidieux au premier abord, il permettent d’aborder non seulement la pluralité des algorithmes (e.g. « tri par sélection », « tri par fusion »), mais aussi les stratégies algorithmiques plus complexes (e.g. « diviser pour régner ») qui figurent au plan d’études. 

2. **Concepts et principes**, ou éviter les formules mathématiques. Nous avons présenté ci-dessus les raisons derrière notre souhait de dé-mathématiser l’informatique. Démathématiser un chapitre comme l’algorithmique représentait un défi de par la nature des objets didactiques. Pour y arriver, nous nous sommes focalisés sur les concepts et sur les principes, en les formalisant le moins possible. Par exemple, nous avons préféré nous appuyer sur la représentation intuitive de ce qu’est un tri dans la vie courante, plutôt que de commencer par une définition mathématique du tri.

3. **Contextualisation**, ou faire des références à la vie courante, aux autres disciplines et à des casse-têtes. Quand cela était possible, nous avons utilisé des exemples qui s’inspirent de la vie courante, comme l’organisation d’un voyage ou la fête d’anniversaire, afin d’éveiller l’intérêt des élèves. Etant outil de communication, d’investigation scientifique ou d’expression artistique, l’informatique touche à toutes les disciplines et se prête bien à des activités interdisciplinaires, permettant de « faire découvrir la complexité de la réalité en développant l’esprit critique par la confrontation de points de vue différents ou par la multiplicité des approches » et à « favoriser la réactivation de notions et de méthodes déjà vues dans les cours, ainsi que leur enracinement dans des sujets particuliers » [CDIP, 2020]. C’est pourquoi nous proposons des activités en lien avec d’autres disciplines, par exemple en lien avec les arts visuels (e.g. algorithme dans la tête de Mondrian), la biologie (e.g. modélisation d’une épidémie) ou encore l’économie (e.g. les enchères du Web). Finalement, nous entrons régulièrement dans la matière par des problèmes à résoudre sous la forme d'encarts intitulés « matière à réfléchir » (généralement en début de chapitre) et par des petits casse-têtes, dans l’idée de stimuler la réflexion des élèves et influer positivement sur leur motivation [Viau, 2004].

4. **Collaboration**, ou travailler en équipe. En plus de faire partie intégrante du développement des objets informatiques (voir ci-dessus), le travail en équipe sur des grands projets est la norme en informatique. Nous avons souhaité que les ressources proposées reflètent cette réalité du terrain et intègrent l’esprit d’équipe, en suggérant à l’élève de confronter sa solution avec celle de ses camarades ou de résoudre des problèmes en groupe. 

5. **Corps**, ou manipuler des objets et bouger. En contextualisant, nous avons souhaité faire réfléchir les élèves avec leur tête, mais pas seulement. En effet, conformément aux théories énactives de la cognition [Varela, Pfeifer], les aspects cognitifs et sensori-moteurs sont étroitement couplés. L’engagement du système locomoteur dans les phases d’apprentissage, par exemple par la manipulation manuelle d’objets (e.g. dispositif physique d’algorithmes de tri) ou le mouvement du corps dans l’espace (e.g. activité Dijkstra et le plus court chemin) permet d’associer plus de modalités sensorielles et motrices aux objets d’apprentissage et favorise leur intégration, un phénomène bien étudié (et débattu)[Pouw, 2014], mais peu mis en pratique au niveau du lycée. 


### Quid du pseudocode et des logigrammes ?

Vous avez certainement remarqué que nous ne faisons pas appel aux notions de logigrammes ou de pseudocode. Nous avons jugé ces notions **peu efficientes**. 

Apprendre un **pseudocode** est un peu équivalent à apprendre un nouveau langage de programmation, ce qui est extrêmement chronophage. Nous avons préféré distinguer **2 niveaux de formalisation des algorithmes** : description de l'idée avec du *langage naturel* et description des opérations de la machine avec un *langage inspiré de Python*. Ce deuxième niveau correspond en effet à du pseudocode, mais nous n'avons pas souhaité le nommer, ni insister sur les règles le définissant pour éviter de des contraintes qui rendrait l'apprentissage plus difficile.

Nous avons préféré éviter d'exprimer les algorithmes par des *logigrammes*. Nous avons estimé que le ratio du temps nécessaire pour maîtriser le code visuel des logigrammes et la plus-value de formaliser la résolution d'un problème simple par un logigramme n'était pas suffisant. En effet, les logigrammes sont extrêmement utiles dans les cas de flux d'informations complexe, a priori très éloignés des problèmes simples que les élèves vont résoudre.


<div id="activites"></div>

### Partie « Enseigner » : activités

La conception des activités a suivi les principes suivants :

- Apprivoiser les notions clés de manière (un peu) ludique

- Développer une compréhension intuitive des concepts

- Faire réfléchir les élèves (avec leur tête, mais aussi avec leur corps)

- Induire des questionnements de type algorithmique


L'apprentissage passe par tous les sens, et lorsque possible, nous avons fait appel aux modalités suivantes :

- La manipulation

- Le mouvement

- La collaboration



<!-- ## Approche pédagogique de la thématique Algorithmique I

1. **Approche orientée principes plutôt que formules mathématiques.** Il est important que les élèves qui ont des difficultés en mathématiques puissent entrer dans la matière informatique. Nous sommes convaincus qu'au niveau gymnasial, l'algorithmique peut s'enseigner sans équations, en ce concentrant sur les concepts et les principes.


2. ***Storytelling* – raconte une histoire cohérente.** Le choix d'enseigner les *algorithmes de tri* a été opéré afin de pouvoir raconter une histoire unique et cohérente qui couvre tous les objectifs pédagogiques. En effet, il existe plusieurs algorithmes de tri, de complexité différente (au programme de 2e année), dont plusieurs sont basés sur la stratégie algorithmique plus complexe « diviser pour régner ». De plus, les algorithmes de tri sont tous accessibles aux élèves, car « tout le monde sait ce que c'est que *trier* ».

3. **Références à la vie pratique, aux autres disciplines et à des casse-têtes encourageant la réflexion.** Pour la motivation des élèves, nous avons tenté d'utiliser autant que possible des exemples concrets qui parlent aux élèves, ainsi que des problématiques qui nous espérons réveilleront leur curiosité et stimuleront leur réflexion. 

4. **Activités collaboratives basées sur des problématiques concrètes.** En informatique, on travaille régulièrement en équipe et nous souhaitons que le cours reflète cette réalité du terrain.
 -->


### Références

CDIP, Evolution de la maturité Fédérale. Projet Actualisation du Plan d’études cadre. Chapitre II - Thématiques transversales, [en ébauche], 20 décembre 2020, p. 4-7.
https://matu2023.ch/fr/groupes-de-projet-et-de-travail/plan-d-etudes-cadre

Pfeifer, R., & Bongard, J. (2006). How the body shapes the way we think: a new view of
intelligence. MIT press.

Pouw, W. T. J. L., van Gog, T., & Paas, F. (2014). An Embedded and Embodied
Cognition Review of Instructional Manipulatives. Educational Psychology Review,
26(1), 51-72. https://doi.org/10.1007/s10648-014-9255-5

Varela, F., Thomson, E., & Rosch, E. (1991). The embodied mind: Cognitive science
and human experience. MIT Press.

Viau, R. (2004).  La motivation : condition au plaisir d’apprendre et d’enseigner en contexte scolaire. 3e congrès des chercheurs en Éducation, Bruxelles.






