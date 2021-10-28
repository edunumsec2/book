
 <!DOCTYPE html>
<html>
<head>
<style>
.button {
  background-color: white;
  border: 1px solid;
  border-color: black;
  font-family:"Lato",sans-serif;
  font-weight:350;
  color: black!important;
  padding: 10px 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
.button:hover {
  text-decoration:none;
  background-color: black; 
  color: white!important;
}
.round-button {
    display:block;
    width:100px;
    height:100px;
    line-height:17px;
    border:0px ;
    border-radius: 50%;
    color:#6069db;
    text-align:center;
    text-decoration:none;
    display: table-cell;
    vertical-align: middle;
    background: #6069db;
    box-shadow: 0 0 0px gray;
    font-size:14px;
    font-weight:bold;
    }

</style>
</head>
</html>

<div align="right"> 
    <a href="http://files.edunumsec2.ch/enjeux-sociaux/economie-numerique.pdf" class="round-button">
         <font color=white id="demo">Voir <br>dossier</font>
    </a>
</div>

# IA et enjeux de l'automatisation

<br>

Ce dossier aborde le vaste sujet que forment l’intelligence artificielle (IA) et l’automatisation. Qu’est-ce que l’IA, d’où vient-elle et comment impose-t-elle une certaine vision du monde ? Quelles sont les opportunités, les craintes et les problèmes propres aux applications de l’IA ? Comment réguler les usages de ces nouvelles technologies ?

## Objectifs

* Comprendre le contexte d’émergence de l’intelligence artificielle
* Différencier l’IA symbolique et connexionniste
* Connaître les forces et les faiblesses de l’IA
* Comprendre les enjeux relatifs à la délégation des prises de décisions 
* Prendre conscience des différentes manières de réguler les pratiques liées à l’IA


## Introduction

<br>
Depuis les années 2010, on observe un retour en force de l’intelligence artificielle. La puissance des ordinateurs combinée à l’important volume de données disponible (big data) permet d’envisager de nouvelles approches notamment dans le domaine de l’apprentissage profond (deep learning). Pour illustrer cet engouement, les investissements globaux dans le domaine de l’IA ont augmenté de 40% entre 2019 et 2020 pour atteindre près de 68 milliards de dollars. <a href="#footnote-1">[1]</a>  Aujourd’hui, l’IA offre de nouvelles perspectives pour la recherche scientifique, oriente nos pratiques numériques et a été adoptée dans divers secteurs publics et privés. Difficile d’échapper à une forme automatisée du traitement de l’information, alors que 92% des adultes vivant en Suisse utilisent quotidiennement un smartphone. <a href="#footnote-2">[2]</a>  

L’intelligence artificielle et ses technologies sont à la fois porteuses d’espoir et de craintes. D’un côté, l’IA fait miroiter la possibilité de résoudre des problèmes extrêmement complexes. De l’autre, les bouleversements potentiels amenés par l’automatisation de certaines tâches et prises de décision inquiètent. Retourner aux débuts de l’IA en tant que domaine scientifique permet de comprendre une certaine vision de l’être humain et du monde, toujours plus influente aussi bien dans le domaine scientifique que dans l’orientation de certaines politiques publiques. 

Afin de faire la lumière sur les impacts, les forces et les faiblesses de l’intelligence artificielle, ce dossier propose un retour sur son histoire. Les principaux enjeux contemporains sont identifiés et présentés dans la deuxième partie du cours. 

<p id="footnote-1">[1] "Artificial Intelligence Index Report 2021", HAI Stanford University
https://aiindex.stanford.edu/wp-content/uploads/2021/03/2021-AI-Index-Report-_Chapter-3.pdf p. 14.
</p>
<p id="footnote-2">[2] "Le smartphone est au coeur de nos vies – Seuls 8% de la population suisse n'en possèdent pas encore", Deloitte
https://www2.deloitte.com/ch/fr/pages/press-releases/articles/deloitte-in-switzerland-smartphones-become-control-centre.html
</p>

<div align="left"; style="font-size:20px ;color:rgb(0, 0, 0); font-family:helvetica">
  <b>L'IA - un ensemble de technologies</b>
</div>

<br>

Trouver une définition générale de l’IA est un exercice difficile car il s’agit en fait d’un ensemble de technologies particulières. Historiquement, on différencie principalement deux approches : d’un côté l’IA symbolique vise à reproduire le raisonnement humain sous la forme de règles statiques pour l’intégrer à des machines. C’est sur ce principe que reposent les **systèmes experts**. De l’autre, l’IA connexionniste est un ensemble de techniques qui apprend à partir des grands volumes de données, également appelés ***big data***. Elle comprend l’**apprentissage automatique** ou ***machine learning*** et l’**apprentissage profond** ou ***deep learning***. Cette dernière se base sur des modèles de **réseaux de neurones**, superposés en plusieurs couches pour permettre l’établissement de règles complexes. 

Aujourd'hui, l'IA est principalement utilisée à des fins prédictives. À partir d'importantes quantités d'information connues, les données, elle établit des modèles statistiques qui serviront ensuite à prédire des faits ou des comportements. 


**L'IA - Entre science et fiction**
<br>

Les premières références à une forme d’intelligence artificielle apparaissent dans la littérature. L’un des premiers exemples est le roman « Frankenstein » de Mary Shelley (1818). Plus tard, la science-fiction en fera un thème central et récurrent, des premiers robots rebelles de la pièce R.U.R. (Čapek, 1920) à la voix de *Her* du film homonyme (Spike Jonze, 2013). L’impact des histoires et des images issus de la science-fiction sont perceptibles dans certaines représentations, fantasmes et inquiétudes suscitées par l’IA. Mais les récits fictifs qui mobilisent diverses formes d’IA n’ont pas la prétention de prédire l’avenir. Leur lecture permet surtout d’identifier des problématiques centrales concernant les aspects juridiques et philosophiques autours de l’IA. Aujourd’hui, les avancées techniques et technologiques amènent à réfléchir à certaines questions longtemps restreintes au monde de la fiction. Dans quelles situations fait-on et peut-on faire appel à l’IA ? Quelles tâches et prises de décision peuvent être déléguées aux machines et en quelles proportions ? Qui est responsable en cas de problème généré par une machine ?
<br>

**Héritage de la cybernétique**

Les premiers scientifiques intéressés par le concept d'IA sont influencés par le courant de pensée de la cybernétique, fondé par le mathématicien Norbert Wiener. Ce mouvement interdisciplinaire popularisé à la fin des années 1940 aux États-Unis considère que tous les systèmes vivants, (humains et animaux) et matériels (machines) sont régulés par une loi générale basée sur des boucles de rétroaction ou feedbacks. Cette hypothèse théorique place les humains et les machines sur un pied d’égalité, d'un point de vue fonctionnel. Elle promeut une vision formaliste et donc simplificatrice du fonctionnement du vivant. Bien que réductrice, cette approche permettra notamment d’envisager les premières théories concernant l’intelligence artificielle basée sur le raisonnement humain. 

L’engouement autour de la cybernétique s’essouffle à la moitié des années 1960, mais son influence reste aujourd’hui encore perceptible dans de nombreux domaines scientifiques tels que les sciences cognitives, l’informatique et bien sur les recherches en IA. 

**« Les machines peuvent-elles penser ? »**

Dans une approche symbolique de l’intelligence artificielle le mathématicien britannique Alan Turing pose cette question dans un célèbre article publié en 1950.  Pour y répondre, il propose le « jeu de l’imitation », également connu sous le nom de « Test de Turing ». L’expérience se résume comme suit : Un être humain (A) est mis en communication via un clavier et un écran, avec deux entités qu’il ne voit pas et dont il ignore la nature ; d’un côté, se trouve un ordinateur (B), de l’autre, un humain (C). Si, au bout de 5 minutes de conversation, l’être humain (A) n’est pas capable de savoir qui de (B) et (C) est l’ordinateur, ce dernier passe le test. 

Le jeu de l’imitation est avant tout un exemple théorique. La puissance des machines des années 1950 ne permet pas d’envisager l’assimilation des questions et encore moins la formulation de réponses adaptées. Aujourd’hui, les agents conversationnels ou ***chat bots*** sont ce qui se rapprochent le plus de l’ordinateur du jeu de l’imitation. Leurs performances actuelles demeurent relativement faibles et sont encore loin de créer la confusion pour les utilisateurs. 

Au-delà de la pertinence du jeu de l’imitation, sa conceptualisation permet de comprendre comment Turing concevait la pensée. Pour lui, elle est faite de capacités cognitives, c’est-à-dire d'un ensemble de facultés qui permettent d’apprendre, d’organiser et d’utiliser les connaissances. En considérant que la pensée peut être réduite à un ensemble de facultés définies (entre autres la perception, la mémoire et le langage), il devient également possible d’envisager de les reproduire de manière artificielle. C’est sur ce principe, inspiré de la cybernétique, que se baseront les premières recherches dans le domaine, quelques années plus tard. Cette approche très rationnelle de la pensée permet de placer l’intelligence humaine et l’intelligence artificielle au même niveau afin de les mettre en opposition. Le rapport de force entre l'être humain et la machine instauré par Turing exercera une influence certaine dans l'histoire. Cette opposition servira de point de repère pour évaluer l'efficacité des systèmes d'IA face à l'intelligence humaine. 

**Création d’un domaine scientifique**

Les termes intelligence artificielle ou plutôt *artificial intelligence* en anglais, apparaissent pour la première fois en 1955, aux États-Unis. Quatre scientifiques formés en mathématique et en neurologie organisent une conférence d’été au Dartmouth College, afin de discuter et de réfléchir aux questions de programmation et de langage des ordinateurs, de réseaux de neurones, de puissance de calcul et d’auto-apprentissage. Mises ensemble, ces thématiques forment un nouveau domaine appelé intelligence artificielle. 

Dans leur [proposition de projet](http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf) les auteurs expliquent leur approche de la manière suivante :

« L’étude devra se dérouler sur la base de la conjecture que chaque aspect de l’apprentissage ou toute autre caractéristique de l’intelligence peut, en principe, être décrit avec une telle précision qu’une machine peut être conçue pour la simuler » 

L’un des but motivant les premières recherches en IA est explicitement de reproduire l’intelligence humaine. 
Comme Turing avant eux, les pionniers de l’IA partent du principe que le fonctionnement du raisonnement humain est suffisamment compris pour être modélisé. Certes, cette approche permet d’ouvrir la voie dans certains domaines bien précis. Cependant, l’intelligence humaine ne se limitent pas à un processus logique et individuel contrairement aux idées des pionniers de l’IA. Cette conception est en fait porteuse d’un paradoxe : pour pouvoir modéliser et reproduire artificiellement l’intelligence, elle est réduite à des fonctions définies. Or, les notions d’intelligence sociale, émotionnelle ou créative sont exclues du problème. La notion du corps est également totalement absente de ces considérations.  

**Tournants**

Si les théories concernant l’intelligence artificielle existent dès les années 1950, il faut attendre plusieurs décennies pour observer les premiers résultats concrets. En 1997, après plus de dix ans de recherche et d’entraînement, le superordinateur d’IBM « Deep Blue » bat le grand maître d’échec Garry Kasparov. Cette première victoire de la machine sur l’homme marque un tournant dans l’histoire de l’IA. Dans un souci de transparence et pour comprendre sa défaite, le joueur russe demande à IBM de produire la liste des coups joués par l’ordinateur. L’entreprise fournit uniquement l’historique de l’une des six parties du match avant de démanteler la machine. 

La victoire de « Deep Blue » est avant tout rendue possible par de nombreuses années de développement et d’entraînement à partir de données produites par des humains. La machine dispose principalement d'une forte puissance de calcul qui permet d’évaluer les meilleurs coups de manière extrêmement rapide. Lors de sa victoire, « Deep Blue » calcule environ 200 millions de possibilités par seconde ce qui correspond à l’anticipation de 12 coups. Kasparov est capable d’anticiper au mieux les 10 prochains coups. 

En 2015, l’histoire de l’IA prend un nouveau virage important. Le programme informatique AlphaGo (développée par la société britannique Deep Mind, rachetée par Google en 2014) bat un joueur professionnel lors d’une partie du traditionnel jeu de Go. L’exploit réside surtout dans le cheminement emprunté pour parvenir à cette victoire. Le jeu de Go est bien plus complexe que les échecs et les possibilités sont trop nombreuses pour être listées et apprises à une machine. Une combinaison d’apprentissage supervisé considérant des parties jouées par des humains et d’apprentissage profond uniquement basé sur l'expérience de la machine va permettre à AlphaGo de déduire les coups optimaux et de battre pour la première fois de l’histoire un joueur professionnel. La dernière version du programme baptisée AlphaGo Zero est parvenue à battre n’importe quel joueur humain ainsi qu’AlphaGo lui-même, en apprenant uniquement de sa propre expérience. Le programme est ainsi devenu imbattable. 

Les technologies qui régissent « Deep Blue » et « AlphaGo » sont très différentes. Pour le premier, il s’agit uniquement d’application de règles logiques prédéfinies et de puissants calculs de probabilités. Pour le second, une association complexe de techniques d’apprentissage machine et d’apprentissage profond basé sur des réseaux de neurones artificiels permet au programme de trouver des possibilités auxquelles l’être humain n’avait encore pas pensé.  

Ces prouesses techniques montrent que l’IA est, dans certaines situations bien précises, supérieure à l’intelligence humaine. Il faut cependant garder en tête que ces domaines de performance correspondent à des environnements fermés, où le but est fixé à l’avance. 

<br>



<div align="left"; style="font-size:20px ;color:rgb(0, 0, 0); font-family:helvetica">
  <b>🌀 Enjeux contemporains autours de l'IA</b>
</div>

<br>

**Domaines d'application**

Quelles tâches et prises de décision sont déléguées aux IA?


Sciences

Pratiques numériques

Public/privé

...

**Nouvelles technologies, anciens problèmes**

Les biais discriminatoires, le remplacement de la force de travail des humains 

Question des voitures autonomes

Les biais de représentation causés par les données



**Gouvernance**

À la suite des diverses controverses engendrées par les biais racistes des IA, certaines grandes entreprises comme Google, Microsoft ou IBM ont mis en place des comités d’éthique. Plusieurs projets en cours ont ainsi été suspendus ou abandonnés en raison du risque de perpétuer des pratiques discriminatoires. Il s’agit dans ce cas d’une forme de gouvernance interne aux entreprises qui n'est pas contraignante. 

Une autre manière d’appréhender les risques liés à l’IA est de légiférer sur ses usages. Aux [États-Unis](https://www.ncsl.org/research/telecommunications-and-information-technology/2020-legislation-related-to-artificial-intelligence.aspx), leader mondial dans le domaine, seuls quatre états avaient adopté une forme de regulation relative à l'IA en 2021. En Europe, la Commission Européenne a proposé en avril 2021 « [un ensemble d’actions visant à stimuler l’excellence dans le domaine de l’IA, ainsi que des règles destinées à garantir la fiabilité de cette technologie](https://ec.europa.eu/france/news/20210421/nouvelles_regles_europeennes_intelligence_artificielle_fr) ». Afin d’estimer les risques que pourraient représenter l’IA pour les citoyens et citoyennes, la CE propose un classement qui détermine le niveau de régulation nécessaire pour chaque domaine. La catégorie « haut risque » comprend par exemple les logiciels de recrutement ou les prises de décision automatisées dans l’attribution d’un crédit, situations où les biais sont souvent présents. La situation est encore différente en Chine, où le gouvernement a publié un plan dans le but de devenir le leader mondial dans le domaine de l'IA d'ici 2030. Pour atteindre cet objectif, l'Etat n'entend  pas réguler l'IA mais encourage et soutient les srtat-ups et entrerpises impliquées dans le domaine. 

Les perspectives de règlementation du numérique sont bien présentes en Europe, même s’il faudra vraisemblablement attendre encore quelques années avant l’entrée en vigueur de cet ensemble de lois. La course à l'IA entre les États-Unis et la Chine n'encourage pas une régulation contraignante des pratiques par le politique.


**La Singularité technologique** (encadré)

La Singularité technologique correspond au moment hypothétique du dépassement de l’intelligence humaine par l’intelligence artificielle. Plusieurs scientifiques dont Ray Kurzweil, Stephen Hawking et Elon Musk ont fait part de leurs inquiétudes quant aux dangers potentiels d’une technologie qui deviendra tôt ou tard, supérieure aux humains.

La théorie de la singularité est basée sur la loi de Moore qui illustre l’évolution exponentielle de la puissance de calcul des ordinateurs. En effet, depuis les premiers microprocesseurs des années 1970, on observe que le nombre de transistors double environ tous les deux ans. Les défenseurs de la singularité partent du principe que cette croissance exponentielle continuera jusqu’à ce que les machines soient elles-mêmes capables de programmer d’autres machines. 

Or, ces prédictions omettent plusieurs facteurs et il parait aujourd’hui difficile de penser que la croissance technologique poursuive sa route vers l’infini.  Les limites matérielles et énergétiques ne sont par exemple pas prises en compte. Les détracteurs de la singularité considèrent que ces prédictions relèvent plus de la science-fiction que de faits scientifiques fiables. 

Pour aller plus loin: 
Jean-Gabriel Ganascia (2017), Le mythe de la Singularité. Faut-il craindre l’intelligence artificielle. Édition du Seuil.

<p id="footnote-1">[1] "Artificial Intelligence Index Report 2021", https://aiindex.stanford.edu/wp-content/uploads/2021/03/2021-AI-Index-Report-_Chapter-3.pdf, HAI Stanford University
 p. 14.
</p>

<p id="footnote-2">[2] "Le smartphone est au coeur de nos vies – Seuls 8% de la population suisse n'en possèdent pas encore", Deloitte
https://www2.deloitte.com/ch/fr/pages/press-releases/articles/deloitte-in-switzerland-smartphones-become-control-centre.html
</p>

### Ressources 

* [Le sous-chapitre](https://www.boullier.bzh/livres/boullier-dominique-sociologie-du-numerique/) "Science-fiction et mythologie du numérique" du livre *Sociologie du numérique* (2016) de Dominique Boullier pour une discussion concernant les liens entre la science-fiction et le numérique. (303-306)

* [Le sous-chapitre](https://www.pressesdesciencespo.fr/fr/book/?gcoi=27246100540390) "L'intelligence artificielle" dans le livre Culture numérique de Dominique Cardon pour une brève présentation de l'IA. (385-398)

* [Le livre](https://www.seuil.com/ouvrage/le-mythe-de-la-singularite-jean-gabriel-ganascia/9782021309997) *Le mythe de la singularité* (2017) de Jean-Gabriel Ganascia 

* [Le documentaire](https://www.youtube.com/watch?v=WXuK6gekU1Y&t=3466s) AlphaGo - The Movie (2017) de Greg Kohs pour comprendre la victoire d'AlphaGo sur Lee Sedol

* [Un reportage](https://www.rts.ch/info/sciences-tech/technologies/11684864-lalgorithme-de-facebook-est-sexiste-pour-les-offres-demploi.html) de l'émission Mise au point de la RTS pour un exemple de biais engendré par un algorithme de Facebook. 

### Glossaire

* Système expert
* Apprentissage automatique ou *machine learning*
* Apprentissage profond ou *deep learning*
* Réseaux de neurones
* *Chatbot*


<br>

## Pistes pédagogiques 

<br>

<div align="left"; style="font-size:20px ;color:rgb(0, 0, 0); font-family:helvetica">
  <b>1. Le jeu de l'imitation 2021</b>
</div>

Objectif : Prendre conscience d
es forces et des faiblesses d'un assistant vocal de type Siri ou Alexa

Matériel: 
* Un assistant vocal 
* Une liste de [questions](https://www.aiunplugged.org/activity5-german.pdf) (En allemand pour l'instant)


Par groupe de 3 trois, les élèves posent tour à tour les questions de la liste à un assistant vocal. 

