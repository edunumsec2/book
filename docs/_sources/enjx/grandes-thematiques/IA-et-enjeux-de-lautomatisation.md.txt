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

<div align="right"> 
    <a href="http://files.edunumsec2.ch/enjeux-sociaux/xx.pdf" class="round-button">
         <font color=white id="demo">Voir <br>dossier</font>
    </a>
</div>

# IA et enjeux de l'automatisation

<br>

Ce dossier aborde le vaste sujet que forment l’intelligence artificielle (IA) et l’automatisation. Qu’est-ce que l’IA, d’où vient-elle et quelle place occupe-t-elle dans nos vies ? Comment les imaginaires culturels impactent-ils les discours sur l’IA ? Quelles sont les opportunités, les craintes et les défis propres aux applications de l’IA ? Comment réguler ces nouvelles technologies ?

## Objectifs

* Comprendre le contexte d’émergence de l’intelligence artificielle
* Connaître les forces et les faiblesses de l’IA
* Prendre conscience des défis de l'automatisation en matière de délégation et de régulation


##

La quête d’une forme d’intelligence artificielle n’est pas nouvelle et apparait dans la littérature dès 1818 avec le fameux roman *Frankenstein* de Mary Shelley. Plus tard, la science-fiction en fera également un thème central et récurrent, des premiers robots rebelles de la pièce R.U.R. (Čapek, 1920) à la voix artificielle de Her du film homonyme (Spike Jonze, 2013). Ces personnages sont des exemples d’**intelligence artificielle forte**, ils sont autonomes et dotés d’une conscience. L’impact des histoires et des images issues de la science-fiction sont perceptibles dans certaines représentations, fantasmes et inquiétudes suscitées par l’IA. Mais les récits fictifs qui mobilisent diverses formes d’IA n’ont pas la prétention de prédire l’avenir. De plus, les techniques actuelles se limitent à de l’**intelligence artificielle faible**, centrées sur une tâche précise. 

La lecture des récits de science-fiction permet surtout d’identifier des problématiques centrales concernant les aspects philosophiques, sociaux ou juridiques autours de l’IA. Le retour en force de l’IA observé depuis le début des années 2010 nous amène à réfléchir à certaines questions longtemps restreintes au monde de la fiction. Quelle place accorde-t-on à l’IA et à ses technologies ? Sont-elles pensées en opposition ou au contraire, avec l’intelligence humaine ? Qui est responsable en cas de problème généré par une machine ?

Pour apporter des pistes de réflexion, un rappel du contexte d’émergence de l’IA est proposé avant de présenter trois enjeux contemporains propres à ses utilisations.



<div align="left"; style="font-size:20px ;color:rgb(0, 0, 0); font-family:helvetica">
  <b>🕶 Une vision de l’intelligence</b>
</div>

<br>

L’émergence des premières techniques dites d’intelligence artificielle s’inscrit dans le courant de pensée de la cybernétique, fondé par le mathématicien Norbert Wiener à la fin des années 1940 aux États-Unis. Ce mouvement interdisciplinaire considère que tous les systèmes vivants (humains et animaux) et matériel (machines) sont régulés par une loi générale basée sur des boucles de rétroaction ou feedback. Cette conjecture permet de placer les humains et les machines sur un pied d’égalité quant à leur fonctionnement. Elle promeut une vision formaliste et donc simplificatrice du fonctionnement du vivant. Bien que réductrice, cette approche permettra notamment d’envisager les premières théories concernant l’intelligence artificielle basée sur le raisonnement humain.

L’engouement autour de la cybernétique s’essouffle à la moitié des années 1960, mais son influence reste aujourd’hui encore perceptible dans de nombreux domaines scientifiques tels que les sciences cognitives, l’informatique et bien sûr, les recherches en IA.

**« Les machines peuvent-elles penser ? »**

C’est la question que pose le mathématicien britannique Alan Turing dans un célèbre article publié en 1950. Pour y répondre, il propose le « jeu de l’imitation », également connu sous le nom de « Test de Turing ». L’expérience se résume comme suit : Un être humain (A) est mis en communication via un clavier et un écran, avec deux entités qu’il ne voit pas et dont il ignore la nature ; d’un côté, se trouve un ordinateur (B), de l’autre, un humain (C). Si, au bout de 5 minutes de conversation, l’être humain (A) n’est pas capable de savoir qui de (B) et (C) est l’ordinateur, ce dernier passe le test.

Le jeu de l’imitation est avant tout un exemple théorique. La puissance des machines des années 1950 ne permet pas d’envisager l’assimilation des questions et encore moins la formulation de réponses adaptées. Aujourd’hui, les agents conversationnels ou chat bots sont ce qui se rapprochent le plus de l’ordinateur du jeu de l’imitation. Leurs performances actuelles demeurent relativement faibles et sont encore loin de créer la confusion pour les utilisateurs.

Au-delà de la pertinence du jeu de l’imitation, sa conceptualisation permet de comprendre comment Turing concevait la pensée. Pour lui, il s’agit de capacités cognitives, c’est-à-dire d’un ensemble de facultés qui permettent d’apprendre, d’organiser et d’utiliser les connaissances. En considérant que la pensée peut être réduite à un ensemble de facultés définies (entre autres la perception, la mémoire et le langage), il devient également possible d’envisager de les reproduire de manière artificielle. C’est sur ce principe, inspiré de la cybernétique, que se baseront les premières recherches dans le domaine, quelques années plus tard. Cette approche très rationnelle de la pensée permet de placer l’intelligence humaine et l’intelligence artificielle au même niveau afin de les mettre en opposition. Le rapport de force entre l’être humain et la machine instauré par Turing exercera une influence certaine dans l’histoire. Cette opposition servira de point de repère pour évaluer l’efficacité de différents systèmes d’IA face à l’intelligence humaine.

**Création d’un domaine scientifique**

Le terme intelligence artificielle ou plutôt artificial intelligence en anglais, apparait pour la première fois en 1955 aux États-Unis. Quatre scientifiques formés en mathématiques et en neurologie organisent une conférence d’été au Dartmouth College, afin de réfléchir aux questions de programmation et de langage des ordinateurs, de réseaux de neurones, de puissance de calcul et d’auto-apprentissage. Mises ensemble, ces disciplines forment un nouveau domaine appelé "intelligence artificielle".
Dans leur [proposition de projet](http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf) les auteurs expliquent leur approche de la manière suivante :

*« L’étude devra se dérouler sur la base de la conjecture que chaque aspect de l’apprentissage ou toute autre caractéristique de l’intelligence peut, en principe, être décrit avec une telle précision qu’une machine peut être conçue pour la simuler »*

L’un des buts motivant les premières recherches en IA est explicitement de reproduire l’intelligence humaine. Comme Turing avant eux, les pionniers de l’IA partent du principe que le fonctionnement du raisonnement humain est suffisamment compris pour être modélisé. 

Certes, cette approche permet d’ouvrir la voie dans certains domaines bien précis. Cependant, l’intelligence humaine ne se limite pas à un processus logique, mesurable et individuel contrairement aux idées des pionniers de l’IA. Cette conception est en fait porteuse d’un paradoxe : pour pouvoir modéliser et reproduire artificiellement l’intelligence, elle est réduite à des fonctions définies. Or, les notions d’intelligence sociale, émotionnelle ou créative sont exclues du problème. La notion du corps est également totalement absente de ces considérations.

**Courants symbolique et connexionniste**

Trouver une définition générale de l’IA est un exercice difficile car il s’agit en fait d’un ensemble de technologies particulières. Historiquement, on différencie principalement deux approches.D'un côté, l’**IA symbolique** qui vise à reproduire le raisonnement humain sous la forme de règles statiques pour l’intégrer à des machines. C’est sur ce principe que reposent l’ordinateur du jeu de l’imitation et plus généralement les **systèmes experts**. De l’autre, l’**IA connexionniste** est un ensemble de techniques d’apprentissage basées sur de grands volumes de données. Elle comprend l’**apprentissage automatique** ou machine learning et l’**apprentissage profond** ou deep learning. Cette dernière utilise des modèles de **réseaux de neurones**, superposés en plusieurs couches pour établir des règles complexes de manière autonome. 

**Prédire à partir des données**

Aujourd’hui, l’IA fait principalement référence aux techniques d’apprentissage automatique. Le but des systèmes intégrant ces technologies est d’exploiter de grands volumes de données afin d’établir des modèles statistiques qui serviront ensuite à orienter des décisions de manières automatiques. 

Mais le travail des ingénieurs demeure central tant dans le choix et la préparation des données exploitées que dans le développement et l’application des algorithmes. Les tâches de collecte, de tri et de mise en forme des données se doivent d’être effectuées de manière réflexive, en prenant en compte les buts du traitement automatiques de l’information. Le développement ou le choix des algorithmes qui traiteront les données sont également à considérer. Finalement, le travail d’interprétation des résultats est nécessaire, puisque le système se limite à élaborer des modèles statistiques, basés sur des propriétés mathématiques.

<div align="left"; style="font-size:20px ;color:rgb(0, 0, 0); font-family:helvetica">
  <b>♖ Avec ou contre l'être humain?</b>
</div>

La force de prédiction des intelligences artificielles n’a cessé d’augmenter depuis son émergence. En 1997, la victoire du superordinateur Deep Blue (IBM) face au grand maître d’échecs Garry Kasporov marque un tournant dans l’histoire opposant l’humain à la machine. 

Lors de sa victoire, Deep Blue calcule environ 200 millions de possibilités par seconde ce qui correspond à l’anticipation de 12 coups. Kasparov est capable d’anticiper au mieux les 10 prochains coups. Mais cet exploit a également nécessité d’importants moyens humains. Les ingénieurs d’IBM ont travaillé plus de 10 ans pour développer «Deep Blue». Ce sont également des données produites par de grands joueurs qui ont servi à entrainer la machine.  

En 2015, l’histoire de l’IA est à nouveau marquée par une victoire de la machine sur l’être humain. Le programme informatique AlphaGo (développée par la société britannique Deep Mind, rachetée par Google en 2014) bat un joueur professionnel lors d’une partie du traditionnel jeu de Go. L’exploit réside surtout dans le cheminement emprunté pour parvenir à cette victoire. Le jeu de Go est bien plus complexe que les échecs et les possibilités sont trop nombreuses pour être listées et apprises à une machine. Une combinaison d’apprentissage supervisé considérant des parties jouées par des humains et d’apprentissage profond uniquement basé sur l’expérience de la machine va permettre à AlphaGo de déduire les coups optimaux et de battre pour la première fois de l’histoire un joueur professionnel. La dernière version du programme baptisée AlphaGo Zero est parvenue à battre n’importe quel joueur humain ainsi qu’AlphaGo lui-même, en apprenant uniquement de sa propre expérience. Le programme est ainsi devenu imbattable. 

Ces exemples montrent que les technologies de l’IA peuvent s’avérer plus performantes que l’être humain dans des situations précises. Ces domaines de performance correspondent à des environnements fermés, où le but est fixé à l’avance. C’est le cas du jeu d’échec et du jeu de Go. La capacité d’adaptation contextuelle des systèmes d’IA constitue l’un des défis non résolu pour les chercheurs.  

C’est également grâce au contexte du jeu que subsiste la logique d’opposition entre le joueur et la machine, dans la continuité du Test de Turing. Mais cette logique élude tout le travail humain consacré au développement des programmes et des algorithmes, sans lesquels l’exploit ne peut pas avoir lieu. Des années de développement et de tests réalisés par des ingénieurs, associés à des données issues de parties jouées par des êtres humains sont nécessaires pour parvenir à de telles performances. En prenant un pas de recul sur les performances de Deep Blue et AlphaGo, l’opposition apparente entre l’humain et la machine se transforme en un exploit collaboratif entre les ingénieurs d’une part, mais également avec la technologie et la puissance de calcul des ordinateurs d’autre part.  

> **La Singularité technologique** 
<br>
La Singularité technologique correspond au moment hypothétique du dépassement de l’intelligence humaine par l’intelligence artificielle. Plusieurs scientifiques dont Ray Kurzweil, Stephen Hawking et Elon Musk ont fait part de leurs inquiétudes quant aux dangers potentiels d’une technologie qui deviendra tôt ou tard, supérieure aux humains.
<br>
La théorie de la singularité est basée sur la loi de Moore qui illustre l’évolution exponentielle de la puissance de calcul des ordinateurs. En effet, depuis les premiers microprocesseurs des années 1970, on observe que le nombre de transistors double environ tous les deux ans. Les défenseurs de la singularité partent du principe que cette croissance exponentielle continuera jusqu’à ce que les machines soient elles-mêmes capables de programmer d’autres machines. 
<br>
Or, ces prédictions omettent plusieurs facteurs et il parait aujourd’hui difficile de penser que la croissance technologique poursuive sa route vers l’infini.  Les limites matérielles et énergétiques ne sont par exemple pas prises en compte. Les détracteurs de la singularité considèrent que ces prédictions relèvent plus de la science-fiction que de faits scientifiques fiables. 
<br>
Pour aller plus loin: 
Jean-Gabriel Ganascia (2017), Le mythe de la Singularité. Faut-il craindre l’intelligence artificielle. Édition du Seuil.
<div align="left"; style="font-size:20px ;color:rgb(0, 0, 0); font-family:helvetica">
  <b>🧬 Terrains de prédilection</b>
</div>

<br>

Les possibilités offertes par l’IA et les grands volumes de données disponibles font miroiter des perspectives inédites en termes de vitesse, de puissance et de quantité d’information pouvant être traitée. Depuis la fin des années 2010, les techniques d’apprentissage automatique basées sur des réseaux de neurones ont révolutionné des domaines tels que la traduction automatique, le traitement d’images et de la recherche en bio-informatique. 

Actif depuis 2017, le traducteur automatique DeepL a dépassé ses concurrents Google Translate, Microsoft Traduction et Facebook. En apprenant de textes existants indexées sur la base de données du site Linguee, DeepL offre un service de traduction efficace pour plus de 26 langues. 

Les technologies de traitement automatique de l’image et du son sont également performantes, si elles sont entraînées avec une quantité suffisante de données. Dans le domaine de l’audio-visuel, la technique du deepfake s’est rependue depuis 2017. Elle permet de reconstituer le visage d’une personne de manière ultra réaliste, de la mettre en scène et de lui faire tenir des propos inventés. Cette technique est particulièrement efficace avec des personnalités publiques (acteur-trice-s, politicien-nes, etc.) dont les images sont nombreuses et facilement accessibles sur Internet. Utilisée correctement, la technique du deepfake est difficile à desceller. Les risques relatifs à cette technologie sont les possibilités de nuire à un individu en utilisant son image dans un contexte inapproprié. Les possibilités de manipulation des opinions politiques ont aussi été pointée du doigt, en France et aux États-Unis.

Finalement, la société DeepMind s’est inspirée des méthodes d’apprentissage profond utilisées par AlphaGo pour développer AlphaFold.
En 2020, le système a permis de modéliser des protéines encore méconnues en un temps record. Ces nouvelles approches contribuent par exemple à l’accélération du développement de certains vaccins. 

**(...)**


<div align="left"; style="font-size:20px ;color:rgb(0, 0, 0); font-family:helvetica">
  <b>🛠 Le travail au défi de l'automatisation</b>
</div>

<br>
La logique de l’opposition entre l’être humain et la machine, souvent thématisé en science-fiction et reprise dans la présentation des victoires de Deep Blue et AlphaGo, entretient la crainte du remplacement des travailleurs et travailleuses humains par des systèmes automatisés. En 2013, une étude menée par des chercheurs de l’Université d’Oxford conclut que 47% des emplois ont une forte probabilité de disparaître compte tenu des avancées dans le domaine de l’apprentissage automatique. Des erreurs méthodologiques sont rapidement identifiées et discrédites les résultats de cette recherche. Le sociologue Antonio Casilli (EHESS) souligne que les auteurs de l’étude d’Oxford ne prennent pas en compte les résistances sociales souvent engendrées par la suppression de postes de travail.

Dans un [article scientifique](https://www.aeaweb.org/articles?id=10.1257/jep.29.3.3) publié en 2015, l’économiste David H. Autor (MIT) démontre que les peurs liées au remplacement du travail de l’être humain par la machine ne sont ni nouvelles, ni fondées. Au début du XIX<sup>e</sup> siècle, en Grande Bretagne, des travailleurs de l’industrie du textile détruisent des machines qu’ils accusent de provoquer le chômage. Si l’automatisation de certaines tâches a bien eu lieu au cours du XX<sup>e</sup> siècle et continue aujourd’hui encore, [l’évolution des taux de chômage de différents pays](https://data.oecd.org/unemp/unemployment-rate.htm) ne reflètent pas une baisse drastique de l’emploi.

**Polarisation, pas remplacement**

Dans son livre En attendant les robots (Seuil, 2019) Antionio Casilli déconstruit la croyance du remplacement du travail de l’être humain par les machines et les IA. Selon l’auteur, les emplois ne disparaissent pas, mais se transforment. Avec l’arrivée des grands noms du numérique, le phénomène de polarisation du travail semble s’amplifier. D’un côté, on constate une forte demande pour les métiers hautement spécialisés, de l’autre, un besoin croissant de main d’œuvre peu qualifiée pour effectuer des tâches répétitives et standardisées, essentielles au bon fonctionnement des systèmes automatisés. 

Ce travail humain, peu qualifié mais indispensable à l’entraînement des IA, entre dans la catégorie du *digital labour*. Les entreprises ayant recours à ce type de  main d’œuvre font généralement appel à des services externalisés et le travail est divisé en micro-tâches (cliquer sur des images, retranscrire un texte, etc.). Les rémunérations ne dépassent que rarement les quelques centimes par micro-tâches effectuées. Cette nouvelle catégorie d’emplois peu qualifiés, rémunérés à la tâche et externalisé, dévalorise le travail humain au profit des grandes entreprises. 


<div align="left"; style="font-size:20px ;color:rgb(0, 0, 0); font-family:helvetica">
  <b>📱 L'IA et nos pratiques numériques</b>
</div>

<br>
Les pratiques en ligne sont orientées par des algorithmes qui collectent, agencent et analyses les traces numériques des utilisateurs de manière automatisée. Ainsi, les contenus, les suggestions et les publicités qui apparaissent sur leur écran sont déterminés à partir de leurs données respectives. Voici quelques exemples de domaines où une forme d’IA influence les contenus consommés : 

* E-commerce (Amazon, Galaxus, Zalando)
* Moteurs de recherche (Google Suggest)
* Plateformes de streaming vidéo (YouTube, Netflix)
* Plateformes de streaming audio (Spotify, Apple Music, Deezer)
* Médias sociaux (Facebook, Instagram, Twitter, TikTok,  Twitch)

Proposer du contenu «sur mesure» vise à améliorer l’expérience des utilisateurs  et des utilisatrices afin de prolonger le temps passé sur un site ou une application. Néanmoins, l’automatisation de certaines tâches est problématique pour différentes raisons. 

**L'effet bulle de filtre**

L’un des phénomène engendré par la suggestion automatique de contenu individualisé est l’effet bulle de filtre. 

Étant donné que les prédictions se font à partir des traces existantes, les contenus et publicités suggérés par algorithmes vont toujours dans le sens de l’utilisateur ou de l’utilisatrice. L’effet bulle de filtre est particulièrement fort sur les fils d’actualité des réseaux sociaux tels que Instagram, Tik Tok ou YouTube où les informations sur les profils sont nombreuses (genre, âge, localisation, etc.). La possibilité d’interagir avec les contenus, via les fonctions « j’aime » ou « ce contenu ne m'interesse pas »  renforce le profilage des comptes et augmente les probabilités de voir les mêmes types de contenus apparaître plus tard. 

Les résultats des requêtes sur le moteur de recherche de Google varient également en fonction des données connues sur l’utilisateur ou l’utilisatrice. Même s’il / elle n’est pas connecté-e à un compte, Google prend en considération la géolocalisation, le type d’appareil ou encore le navigateur utilisé lors de l’affichage des résultats. Deux individus faisant la même recherche auront ainsi des propositions de contenus différentes. 

La critique principale de l’effet bulle de filtre est qu’il maintient les individus dans leur zone de confort idéologique et ne permet de les confronter à d’autres visions du monde. [Pour le sociologue Dominique Cardon](https://www.lemonde.fr/pixels/article/2016/11/14/facebook-faiseur-de-rois-de-l-election-americaine_5030959_4408996.html), ce ne sont pas les algorithmes qui sont à l'origine du phénomène mais plutôt les choix d'affiliation (ami-e-s, pages suivies, etc.) de chaque utilisateur et utilisatrice. La suggestion automatique de contenu amplifie ainsi un effet préexistant au numérique. Car même avant l'apparition d'internet, les individus ont toujours eu pour habitude de chercher à confirmer leurs opinions plutôt que de les confronter et les remettre en question. L'effet bulle de filtre est donc bien réel mais il ne s'agit pas d'une nouveau phénomène propre à l'IA.

**Les biais**

Dans le domaine des statistiques, le biais correspond à une erreur méthodologique qui engendre de faux résultats. Il peut être causé par de la sélection d’un échantillon non-représentatif ou par la manière de collecter les données. Les algorithmes des IA, dont les choix sont déterminés par des calculs exploitant différents types de données, sont également à l’origine de nombreux biais.

Au début du mois de septembre 2021, une ancienne employée de Facebook [dénonce un biais raciste](https://www.24heures.ch/facebook-a-confondu-des-personnes-noires-avec-des-singes-677330452425) dans l’algorithme de suggestion de la plateforme. Au bas d’une vidéo dans laquelle figure des personnes noires, une bannière demande à l’utilisateur s’il ou elle souhaite continuer à « voir des vidéos sur des primates ». À la suite de cet épisode, Facebook admet que cette erreur est inacceptable s’excuse. Mais comment un tel scénario est-il possible? Pour le savoir, il faut comprendre le fonctionnement des techniques de reconnaissance automatique d’images.

Lorsqu’un programme est développé pour reconnaître des images, un volume important de données (dans ce cas, d’images) est nécessaire pour apprendre à reconnaitre les différentes formes qui la composent. Des techniques d’apprentissage automatique supervisé permettent par exemple de faire la différence entre ce qui est un visage et ce qui ne l’est pas. Dans le cas de l’algorithme de Facebook, la base de données utilisées ne contenait vraisemblablement pas assez d’exemples représentant des personnes de couleurs.

L’enjeu des biais se situe au niveaux de la qualité des bases de données disponibles pour entrainer les algorithmes. Si les données ne sont pas représentatives de la diversité des individus, des biais seront inévitablement reproduits. L’utilisation de systèmes d’apprentissage automatique dans les processus de prise de décision n’étant pas limitée aux pratiques en ligne, les risques de voir ces biais se reproduire sont réels. Dans son ouvrage *Weapons of Math Destruction* (2016, Crown Books), la mathématicienne Cathy O’Neil met en garde contre l’utilisation des big data et des algorithmes dans le domaine des assurances, du recrutement et des forces de l’ordre. Elle explique que la délégation d’importantes prises de décision à des programmes automatiques est dangereuse car elle renforce les inégalités existantes dans la société. 

Pour contrer cette tendance de reproduction numérique des biais, l’ingénieure Joy Buolamwini  (MIT) a créé la plateforme *Algorithmic Justice League*. Elle propose de rendre le domaine de l’IA plus inclusif, en s’assurant notamment que les spécialistes représentent la diversité de la société. Augmenter la part de femmes et de personnes non-blanches dans le processus de développement et d'entraînement des IA permettrait d'éviter de grossières erreurs de discrimination.




<div align="left"; style="font-size:20px ;color:rgb(0, 0, 0); font-family:helvetica">
  <b>👩🏻‍⚖️ Réguler</b>
</div>
<br>
À la suite des diverses controverses engendrées par les biais racistes des IA, certaines grandes entreprises comme Google, Microsoft ou IBM ont mis en place des comités d’éthique. Plusieurs projets en cours ont ainsi été suspendus ou abandonnés en raison du risque de perpétuer des pratiques discriminatoires. Il s’agit dans ce cas d’une forme de gouvernance interne aux entreprises qui n'est pas contraignante. 

Une autre manière de réguler l’IA est de légiférer sur ses usages. Aux [États-Unis](https://www.ncsl.org/research/telecommunications-and-information-technology/2020-legislation-related-to-artificial-intelligence.aspx), leader mondial dans le domaine, seuls quatre états avaient adopté une forme de regulation relative à l'IA en 2021. En Europe, la Commission Européenne a proposé en avril 2021 « [un ensemble d’actions visant à stimuler l’excellence dans le domaine de l’IA, ainsi que des règles destinées à garantir la fiabilité de cette technologie](https://ec.europa.eu/france/news/20210421/nouvelles_regles_europeennes_intelligence_artificielle_fr) ». Afin d’estimer les risques que pourraient représenter l’IA pour les citoyens et citoyennes, la CE propose un classement qui détermine le niveau de régulation nécessaire pour chaque domaine. La catégorie « haut risque » comprend par exemple les logiciels de recrutement ou les prises de décision automatisées dans l’attribution d’un crédit, situations où les biais sont souvent présents. 

La situation est encore différente en Chine, où le gouvernement a publié un plan dans le but de devenir le leader mondial dans le domaine de l'IA d'ici 2030. Pour atteindre cet objectif, l'Etat n'entend  pas réguler l'IA mais encourage et soutient les start-ups et entrerpises impliquées dans le domaine. 

L’Europe apparait donc comme le seul endroit où des perspectives concrètes de réglementation du numérique et plus précisément de l’IA et des ses usages sont envisagées. Il faudra néanmoins attendre encore quelques années avant l’entrée en vigueur de l’ensemble des lois proposé par la CE. 

Ces différentes approches quant à la régulation de l’IA traduisent l’ambiguïté des technologies qu’elle englobe. L’Europe considère leur utilisation comme potentiellement dangereuse pour la société et y voit donc un besoin de régulation par l’état. La maîtrise de l’IA constitue un outil de mesure de la puissance nationale pour la Chine, ce qui ne favorise aucunement sa régulation. 

### Ressources

* [Le sous-chapitre](https://www.boullier.bzh/livres/boullier-dominique-sociologie-du-numerique/) "Science-fiction et mythologie du numérique" du livre *Sociologie du numérique* (2016) de Dominique Boullier pour une discussion concernant les liens entre la science-fiction et le numérique. (303-306)

* [Le sous-chapitre](https://www.pressesdesciencespo.fr/fr/book/?gcoi=27246100540390) "L'intelligence artificielle" dans le livre Culture numérique de Dominique Cardon pour une brève présentation de l'IA. (385-398)

* [Le livre](https://www.seuil.com/ouvrage/le-mythe-de-la-singularite-jean-gabriel-ganascia/9782021309997) *Le mythe de la singularité* (2017) de Jean-Gabriel Ganascia 

* [Le documentaire](https://www.youtube.com/watch?v=WXuK6gekU1Y&t=3466s) AlphaGo - The Movie (2017) de Greg Kohs pour comprendre la victoire d'AlphaGo sur Lee Sedol

* [Un reportage](https://www.rts.ch/info/sciences-tech/technologies/11684864-lalgorithme-de-facebook-est-sexiste-pour-les-offres-demploi.html) de l'émission Mise au point de la RTS pour un exemple de biais engendré par un algorithme de Facebook. 

### Glossaire

* IA symbolique
* IA connexionniste
* Système expert
* Apprentissage automatique ou *machine learning*
* Apprentissage profond ou *deep learning*
* Réseaux de neurones
* *Chatbot*


<br>

## Pistes pédagogiques 

<br>

<div align="left"; style="font-size:20px ;color:rgb(0, 0, 0); font-family:helvetica">
  <b>Usages quotidiens</b>
</div>


1. IA ou pas? | Débranché

Objectif : être capable d'identifier les situations dans lesquelle l'IA influence les contenus consultés. 

Matériel:
* Captures d'écran à projeter à la classe 

2. Jeu de l'imitation | Branché

Objectif : Prendre conscience des forces et des limites d'un assistant vocal

Matériel: 
* Un assistant vocal de type Siri
* Une liste de [questions](https://www.aiunplugged.org/activity5-german.pdf) (En allemand pour l'instant)


Par groupe de 3 trois, les élèves posent tour à tour les questions de la liste à un assistant vocal et notent les réponses.

<div align="left"; style="font-size:20px ;color:rgb(0, 0, 0); font-family:helvetica">
  <b>Gouvernance</b>
  </div>

  1. Débat
  
  Un jeu de rôle par groupe. 
  Chaque groupe représente un acteur social de type citoyen / gouvernement / plateforme / scientifique... et 