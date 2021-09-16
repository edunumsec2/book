# Représentation du son
</br>

# Table des matières

* [Introduction](#Introduction)
* [Le son](#Chapter1)
    * [Signal analogique (physique) temporel](#Section1.1)
        * [Onde de pression](#Section1.1.1)
        * [L'oreille comme capteur](#Section1.1.2)
        * [Vibration et fréquence](#Section1.1.3)
    * [Contenu fréquentiel (analyse spectrale)](#Section1.2)
        * [Signal pur](#Section1.2.1)
        * [Signal complexe (à contenu fréquentiel)](#Section1.2.2)
    * [Signal sonore et musique](#Section1.3)       
        * [Le timbre : caractéristique d'un signal sonore](#Section1.3.1)
        * [La musique comme "organisation" de timbres sonores](#Section1.3.2)    
* [Génération et enregistrement sonores](#Chapter2)
    * [Générer et enregistrer un son analogique](#Section2.1)
        * [Les instruments acoustiques classiques](#Section2.1.1)
        * [Les synthétiseurs analogiques](#Section2.1.2)
        * ["Capter" le son analogique ](#Section2.1.3)
        * ["Garder en mémoire" le son analogique](#Section2.1.4)
        * [Transmettre le son analogique](#Section2.1.5)
    * [Générer et enregistrer un son numérique](#Section2.2)
        * [Synthèse pwm – Problématique générale](#Section2.2.1)
        * [Les synthétiseurs actuels et les banques de sons](#Section2.2.2)
        * [« Capter » le son numérique¶](#Section2.2.3)
        * [« Garder en mémoire » le son numérique¶](#Section2.2.4)
        * [Transmettre le son numérique¶](#Section2.2.5)
* [Transmission du son](#Chapter3)
    * [Problématique du canal de transmission](#Section3.1)
        * [De l'émetteur vers le récepteur](#Section3.1.1)
        * [Perturbation liée au canal de transmission : la fidélité](#Section3.1.2)
    * [Solution : du signal physique au signal numérique](#Section3.2)
        * [Théorie et codage de l’information](#Section3.2.1)
    * [Spécificités du codage numérique](#Section3.3)
        * [Un signal physique exprimé sous forme de ... 0 et de 1 ?!](#Section3.3.1)
        * [Echantillonnage](#Section3.3.2)
* [Conclusion](#Conclusion)

</br>
</br>

<a name="Introduction"></a>
# Introduction 
Le lien entre mathématiques et musique n’est pas récent puisque dès l'antiquité la musique est associée aux mathématiques. Elle est même considérée par Pythagore au VIe siècle avant J.C. comme étant une science mathématique, au même titre que l'arithmétique, l'astronomie et la géométrie.

On cite souvent Pythagore comme l'un des pères de la théorie musicale. C'est à lui qu'on doit la compréhension des fréquences, c'est-à-dire des différentes hauteurs qui sont symbolisées par les notes de musique.

Un travail que continuera, des siècles plus tard, Jean-Philippe Rameau avec son fameux Traité de l'harmonie réduite à ses principes naturels publié en 1722. A la même époque, Jean-Sébastien Bach s'amuse à utiliser des procédés mathématiques, pour écrire ses fugues en jouant avec la symétrie par exemple.

La musique serait donc mathématique, c'est du moins ce que disait Leibniz en 1712 :
"La musique est un exercice caché d'arithmétique, l'esprit n'ayant pas conscience qu'il est en train de compter ".
Car contrairement à la peinture ou la littérature, la musique peut très précisément se traduire en équations et en graphique.

Au XXe siècle, les compositeurs cherchent à tout prix à se détacher de la musique tonale. Il faut trouver de nouveaux systèmes de composition. On assiste alors à la création de l'atonalité, du dodécaphonisme, de la musique sérielle.
Exemple avec l'un des compositeurs les plus inclassables de la première moitié du siècle dernier: Béla Bartók. Il utilise le nombre d'or pour structurer ses compositions, c'est-à-dire un rapport proportionnel entre différents éléments d'une même pièce. Il est certainement l'un des premiers compositeurs à se servir de ce procédé de manière consciente. En résulte une structure cohérente et qui paraît équilibrée sans que l'esprit ne comprenne pourquoi. Jugez par vous même avec le 3e mouvement du Concerto pour piano n°3.
Le nombre d'or également utilisé par Iannis Xenakis, compositeur grec, et qui a une formation d'architecte et d'ingénieur. Il crée une musique nouvelle qui est constituée de masses sonores. Cela donnera Metastasis en 1955, une composition entièrement déduite de règles et de procédures mathématiques.
Il ira encore plus loin en créant des algorithmes pour tenter de représenter musicalement les notions de hasard et de probabilité.

Il n'y a pas que les compositeurs qui se soient intéressés aux mathématiques. L'inverse est aussi vérifiable. De nombreux mathématiciens, physiciens, sont également de grands mélomanes voire de bons musiciens. Einstein qui était un excellent violoniste, celle qui deviendra la directrice du Cern, Fabiola Gianotti, qui en plus de son doctorat de physique sub-nucléaire expérimentale, a également un diplôme professionnel du conservatoire de Milan en piano. Ou encore la chanteuse lyrique Karen Vourc'h titulaire d'un DEA en physique théorique à l'Ecole Normale Supérieure qui déclarait dans une interview "qu'imaginer des sons, des univers, grâce à des formules mathématiques ou sous la forme de mélodies participe au même processus de recherche intellectuelle."

Et c'est certainement là que réside le mystère qui a fasciné et qui fascine toujours autant les mathématiciens, les physiciens, les scientifiques au même titre que les compositeurs. L'émotion provoquée par la musique est-elle explicable, théorisable ? A partir de quand arrête-t-on de parler de sons pour parler de musique ? La musique contemporaine basée sur des équations est-elle trop abstraite pour provoquer des émotions ?

Le XXe siècle est aussi celui des machines, et en particulier celui des ordinateurs. Depuis Alan Turing en 1936 et sa célèbre « machine », ses concepts de programme prendront tout leur sens avec l’essort des ordinateurs. Ce siècle voit s’interpénétrer mathématiques et informatique, cette dernière discipline investissant aujourd’hui tous les champs de l’activité humaine.
L'algorithme, objet central de l'informatique, mais aussi objet des mathématiques depuis des siècles, prend maintenant une nouvelle place dans les mathématiques et nécessairement dans leur enseignement. Les mathématiques s'en trouvent interrogées et leur enseignement aussi. Cette discipline a acquis aujourd’hui dans le monde de la recherche un statut comparable à celui de l’algèbre, de la géométrie ou de l’analyse, ou encore des probabilités statistiques. Le National Council of Teachers of Mathematics a consacré en 1998, son «Yearbook» à l'enseignement et l'apprentissage des algorithmes dans la classe de mathématiques (NCTM 1998). 

Depuis 2009, en France, une part d'algorithmique a été introduite dans les programmes du lycée et le vocable apparaît même à l’école primaire. La discipline trouve peu à peu sa place dans les manuels du secondaire... et dans le cœur des enseignants de mathématiques.
La science informatique s’est également imposée, progressivement, comme une discipline tout aussi fondamentale que les disciplines scientifiques « dures » classiques que sont les mathématiques, la physique ou la mécanique. Le développement exponentiel des capacités des ordinateurs, dans un XXème siècle de l’information a accéléré de manière phénoménale ce positionnement. L’enseignement « officiel » de la discipline peut apparaître tardif, en France comme en Suisse, malgré des plans numériques élaborés depuis plusieurs années.

La Conférence intercantonale de l’instruction publique de la Suisse romande et du Tessin (CIIP) a adopté son plan d’action pour l’éducation numérique en 2018. Ce plan prévoyait que dans les cinq prochaines années, tous les élèves de l’école obligatoire et de toutes les filières du degré secondaire II disposent de connaissances et de compétences numériques. L’utilisation active des outils, l’éducation aux médias et la science informatique sont concernées. Ce plan ambitieux décline ses objectifs en cinq domaines prioritaires : les plans d’études, les équipements, la formation des directions d’établissements et du corps enseignant, ainsi que la collaboration avec les hautes écoles et le développement de la veille technologique et pédagogique. Il s’agit de doter l’école des moyens de former au numérique par le numérique. L’informatique, science et technique du traitement automatique de l’information, est clairement distinguée des usages des outils numériques de médiation des savoirs, tandis que l’éducation aux médias a pour objet la compréhension de l’environnement médiatique contemporain dans une perspective critique et responsable. Ces trois dimensions sont considérées comme inséparables.


L’élaboration d’activités spécifiques, en mode «débranché» ou non, s’appuyant sur l’utilisation ou la création de ressources logicielles est donc centrale. Activités que devront s’approprier les enseignants et qui devront recevoir l’adhésion des élèves.

Dans ce contexte, l’élaboration de séquences d’enseignement, dont la finalité est de toucher, sensibiliser les élèves afin de les motiver à poursuivre dans l’apprentissage de la science informatique, doit s’appuyer sur différents ressorts :


• la perception scientifique des phénomènes, à travers des concepts déjà perçus ou connus : mathématique et physique ont toute leur place dans cet apprentissage, renforçant la formation scientifique, mais vus plus comme un outil pédagogique n’obstruant pas l’accès à la connaissance de la science informatique elle-même,

• le ressort émotionnel, vecteur d’apprentissage et d’adhésion (métacognition) : l’aspect ludique, pratique et la connexion avec le monde sensoriel est particulièrement favorisé par la relation de plus en plus étroite qu’entretien l’informatique avec la musique : depuis le début de la musique électronique dans les années 1950, l’informatique a pénétré l’univers musical : au niveau des outils, mais surtout s’agissant de la création et de la diffusion, sans parler de l’émotion même suscitée par l’aspect algorithmique, synthétique d’oeuvres aujourd’hui créées exclusivement via la technologie. L’informatique s’est par ailleurs affirmé comme un incomparable outil de démocratisation et d’accès à la création musicale, notamment avec ce que l’on nomme les « home studios ».


On se propose ici de poser le cadre de séquences d’enseignement de l’informatique à destination d’un public d’élèves de l’enseignement secondaire deux (maturité), mêlant mathématiques, physique, et s’appuyant sur les leviers pédagogiques et didactiques offerts par l’expérience sensorielle (la musique) et la métacognition.

Cette vingtaine d’activités constitue une base de travail pouvant être utilisée à différents niveaux d’approfondissement concernant l’apprentissage informatique : familiarisation avec un environnement informatique général (machine et hardware, système d’exploitation, fichiers, dossiers, communication via serveur ou entre machines, ...), de programmation (éditeur graphique, langage – python), exploitation et création via l’environnement de programmation (accès aux bibliothèques spécifiques, à la documentation en ligne, créations de programmes et d’utilitaires, manipulation et/ou création d’interfaces graphiques, utilisation approfondie du langage de programmation et des interfaces ...).

Elle peut être ajustée également s’agissant des différents niveaux de profondeurs souhaités concernant les autres disciplines fondamentales dont il est fait référence, les mathématiques, la mécanique et la physique, et intéresser indifféremment toutes les années de la maturité.

Elle mérite bien entendue d’être enrichie, en particulier par les retours enseignants-élèves.

</br>
</br>
</br>

<a name="Chapter1"></a>

# Le son

<a name="Section1.1"></a>

## Signal analogique (physique) temporel

<a name="Section1.1.1"></a>

### Onde de pression
Le son est une onde mécanique nécessitant un milieu matériel pour se propager. Ce milieu peut être un gaz (comme l'air), un solide ou un liquide. Le son ne peut donc pas se propager dans le vide. Une onde sonore est une succession de champs de pression-dépression, ou compression-dilatation.
L’exemple « visible » de l’impulsion mécanique donnée sur une corde élastique illustre parfaitement ce phénomène.

<br/>
<center> 

```{image} png/Im1.png
:width: 400px
:height: 200px
```
</center>
<center> Propagation d’onde de pression</center> 
  
<br/>

***Illustration expérimentale*** 

Lorsqu’on frappe les branches d'un diapason, celles-ci se mettent à vibrer et le diapason émet un son. L'amplitude de vibration des branches est trop faible pour être vue directement, mais on peut mettre en évidence la vibration en baignant les extrémités des branches du diapason dans un verre rempli d'eau ; <a href="https://youtu.be/K6FHFTtc9Ew"> on peut alors observer des vagues à la surface de l'eau et quelques éclaboussures.</a>

<br/>

<a name="Section1.1.2"></a>

### L’oreille comme capteur
*Caractéristiques de l’oreille, sensibilité, oreille interne, transfert acoustique-électrique vers le système nerveux. - à compléter*

<br/>
<center> 

```{image} png/Im3.png 
:width: 400px
:height: 300px
```
```{image} png/Im4.png
:width: 400px
:height: 300px
```
</center>
<center> Schéma de l’oreille et rôle des cellules ciliées </center>
<br/>

<a name="Section1.1.3"></a>

### Vibration et fréquence
Un son pur est représenté par une fonction sinusoïdale du temps, de période T et de fréquence f = 1/T.

<br/>
<center> 

```{image} png/Im5.png
:width: 300px
:height: 200px
``` 
</center> 
<center> Représentation graphique d’un son pur (monofréquence) </center> 

<br/>

Un son est une vibration mécanique se propageant dans un milieu matériel jusqu’à atteindre un récepteur, notre oreille par exemple.

</br>

* * Activité 1 - **Signal sonore élémentaire**

    Classe : 1M, 2M

    <span style="color:green">Difficulté : basique </span> <sup> [1](#myfootnote1)</sup>
    

    Objectif informatique 1 : 
    - le premier objet de cette activité est de permettre à l'élève d'appréhender la problématique de la représentation de l'information au sens large, comme le passage d'un univers symbolique à un autre.
    Il s'agit ici de passer d'un espace physique sensoriel (l'audition) à un autre espace sensoriel (la vue) et à la modélisation mathématique permettant de représenter un phénomène, ici acoustique (la représentation sinusoïdale continue d'une onde harmonique). Ce premier travail intellectuel doit permettre aux élèves d'une part de se familiariser avec le matériau servant de support aux activités suivantes (les éléments relatifs au son), et d'autre part de faciliter leur compréhension du changement de paradigme entre l'espace physique (plutôt que mathématique) et l'espace numérique et le codage binaire de l'information.
    - le second objet de cette activité est de permettre aux élèves de se familiariser avec les outils informatiques de visualisation graphique et de production sonore, offrant deux modes de représentation du son. 
    En particulier l'information fréquentielle, essentielle en traitement du signal, est abordée visuellement dans le plan temporel (sinusoide, période), puis fréquentiel (spectre), et perçue auditivement (hauteur du son - grave/aigu).
    
    </br>

    Objectif informatique 2 : 
    - cette activité peut être envisagée comme support de sensibilisation de l'élève à l'environnement de programmation et à la programmation en python elle même : graphe sinusoïdal obtenu via un programme python, familiarisation avec l’environnement de programmation (éditeur Visual Studio ou autre, ...), avec la création de programme, le débug ; entrées / sorties, sotie graphique, appels aux bibliothèques (numpy, matplotlib, pyo). Certaines notions élémentaires relatives aux langages de programmations et au langage python peuvent être mises en pratique, après un cours préalable (notion de variable, boucle for, passage de valeur à travers une fonction, ...). Elle pourra donc être reprise dans l'onglet "programmation" du document général.
    
    
    </br>

    Objectif mathématique et physique (transversal) :
    - l'activité permet de réactiver, confirmer ou s'appuyer sur des savoirs mathématiques relatifs aux relations fonctionnelles,  aux représentations dans le plan et à la trigonométrie.
    - l'activité permet de réactiver, confirmer ou s'appuyer sur savoirs mécaniques et physiques relativement aux ondes, à la notion de milieu de propagation, de période et de fréquence.

    </br>

    Pré-requis : 

    - informatique :
        * <span style="color:green">programmation</span>
        * <span style="color:green">utilisation de l'ordinateur et environnement</span> 
        
        </br> 
    
    - mathématique :
        * <span style="color:orange">fonctions</span>
        * <span style="color:orange">fonctions trigonométriques simples</span> 
        * <span style="color:green">représentation sur un repère plan</span> 
        
        </br>
    
    - physique :
        
        * <span style="color:orange">notion d'onde mécanique (pression, compression-dilatation)</span>    
</br>
    
    Supports didactiques : 
    
    ordinateur et environnement de programmation, casque audio individuel connecté sur la sortie audio de l'ordinateur de chaque élève, documentation papier ou en ligne, supports papier pour la prise de notes. Ordinateur enseignant avec sortie audio (2 enceintes - stéréo), vidéoprojecteur.

<br/>

<a name="myfootnote1">1</a>: *code couleur pour le niveau de connaissance dans le degré :* 

<span style="color:green">vert : basique </span>  <span style="color:orange"> orange : médian </span> <span style="color:red"> rouge : avancé </span> 

<a name="Section1.2"></a>
<br/>
## Contenu fréquentiel (analyse spectrale) 

<a name="Section1.2.1"></a>

### Signal pur
Un signal audio pur est un signal sinusoïdal.

* *{Activité 2 : l’activité 1 est reprise. Le module pyo va être utilisé. Import de la bibliothèque, utilisation des fonctions pyo spécifique afin de « sortir » le son à partir des fichiers sinusoïdaux créés au cours de l’activité 1. La relation fréquence – hauteur du son est ainsi appréciée}*

     *[Supports didactiques : ordinateur et environnement de programmation, documentation papier ou en ligne, supports papier pour la prise de notes]* 

<center> 

```{image} png/Im6.png
:width: 300px
:height: 200px
```
```{image} png/Im7.png
:width: 300px
:height: 200px
```
</center>

<center>
Signal temporel et signal spectral
</center>
<br/>

<a name="Section1.2.2"></a>

### Signal complexe (à contenu fréquentiel)
Un signal complexe est un signal à contenu fréquentiel multiple. Il correspond acoustiquement à un signal audio réel. Ce type de signal s’obtient en fait en sommant plusieurs signaux « fondamentaux », sinusoïdaux.

<br/>
<center> 

```{image} png/Im8.png
:width: 300px
:height: 200px
``` 
<center> 

```{image} png/Im9.png
:width: 300px
:height: 200px
``` 
</center> 
</center> 
<center> Composition (addition) de signaux – signal résultat </center>
<br/>
<center> 

```{image} png/Im10.png
:width: 300px
:height: 200px
``` 
</center> 
<center> Composition spectrale d’un signal </center>
<br/>

* *{Activité 3 : les travaux des deux précédentes activités sont repris. Les élèves vont construire des nouveaux signaux à partir des fichiers sinusoïdaux déjà obtenus... en les ajoutant ! De nouvelles courbes sont ainsi tracées. Via le module pyo, le résultat peut être écouté. Cette activité permet d’aller progressivement vers la notion de composition/décomposition spectrale et de transformée de Fourier..}*

    *[Supports didactiques : ordinateur et environnement de programmation, documentation papier ou en ligne, supports papier pour la prise de notes]*

<br/>

<a name="Section1.3"></a>

## Signal sonore et musique

<a name="Section1.3.1"></a>

### Le timbre : caractéristique d’un signal sonore

* *{Activité 4.1 : plusieurs timbres d’instruments classiques ou de synthétiseurs sont écoutés. Les élèves déterminent d’eux-mêmes ce qui caractérise tel instrument par rapport à un autre}*

    *[Supports didactiques : instruments, audio, photos, vidéo]*

#### Amplitude
#### Fréquence ou contenu fréquentiel
#### Enveloppe
* *{Activité 4.2 : les fichiers de l’activité 3 sont repris. Les élèves éditent des courbes de différentes amplitudes et fréquence et apprécient auditivement le résultat, via le module pyo ou music21. Ensuite, via un interface graphique, ils peuvent modifier ces paramètres en temps réel en manipulant des « potentiomètres » graphiques : modulation d’amplitude et de fréquence. Une troisième étape est l’introduction de la notion d’enveloppe (Attack Delay Sustain Release} : elle est introduite via le module pyo ; les élèves peuvent modifier chacun de ces 4 paramètres, distinctement ou ensemble.}*

A travers la perception de ces trois paramètres (amplitude, fréquence-contenu fréquentiel et enveloppe), les élèves ont une appréciation auditive et visuelle (donc sensorielle), mais également physique et mathématique de la notion de timbre.
* *[Supports didactiques : ordinateur et environnement de programmation, documentation papier ou en ligne, supports papier pour la prise de notes]*

<a name="Section1.3.2"></a>

### La musique comme « organisation » de timbres sonores
#### Harmonie : gammes et modes
Gammes de pythagore, naturelle, tempérée : construction mathématique. Autres types de gammes.
Les 7 modes, Ionien, Dorien, Phrygien, Lydien, Mixolydien, Éolien et Locrien : écoute et construction des enchaînements de notes (renversement de gammes).

<br/>
<center> 

```{image} png/Im11.png
:width: 300px
:height: 200px
``` 
</center> 
<center> Intervalles pour la gamme tempérée 
</center> 
<br/>
<center> 

```{image} png/Im12.jpg
:width: 300px
:height: 200px
``` 
</center> 
<center> Représentation modale sur le clavier du piano
</center> 

<br/>

* *{Activité 5 : les élèves, après avoir apprécié auditivement chacune des gammes, en particulier sur le clavier du piano (numérique...), se placent dans l’environnement informatique et créent des enchaînements de notes. Le but est de reproduire les intervalles (donc créer les notes) pour chacune des gammes.}*

    *[Supports didactiques : instruments, audio, photos, vidéo, ordinateur et environnement de programmation, documentation papier ou en ligne – notions de cours projetées – cahiers élèves pour prise de notes]*

<br/>

#### Rythme et tempo
<br/>
<center> 

```{image} png/Im13.png
:width: 300px
:height: 200px
``` 
</center> 
<center> 

```{image} png/Im14.png
:width: 200px
:height: 200px
``` 
</center> 
<center> 

```{image} png/Im15.jpg
:width: 200px
:height: 100px
``` 
</center> 

<center> 
Mesures, décomposition rythmique et tempo
</center>
<br/>

* *{Activité 6 : le découpage en temps – mesures musicales, durée de signal – et la vitesse d’exécution (tempo ou BPM). Les élèves écoutent, puis manipulent leurs fichiers générés sous python et les exploitent : enchaînements de notes déroulés à différents tempi et types de mesures (2/4, 3/4, 4/4, 5/4!).}*

    *[Supports didactiques : audio, photos, vidéo, ordinateur et environnement de programmation, documentation papier ou en ligne – notions de cours projetées – cahiers élèves pour prise de notes]*  

<br/>

#### Composition et accords
* *{Activité 7 : les élèves manipulent leurs fichiers afin d’associer des notes fondamentales et créer des accords. Ils composent mélodie et suite d’accords en programmant.}*

    *[Supports didactiques : ordinateur et environnement de programmation, documentation papier ou en ligne, – notions de cours projetées – cahiers élèves pour prise de notes]*

<center> 

```{image} png/Im16.png
:width: 300px
:height: 200px
``` 
</center> 
<center>
Composition d’un accord sur le clavier d’un piano
</center>
<br/>

#### Séquences rythmiques et harmoniques
* *{Activité 8 : via le module graphique de Pyo, les élèves ont la possibilité d’enregistrer une séquence audio qu’ils ont composée à partir de python. Ils peuvent moduler la vitesse d’exécution de la séquence... mais aussi la tonalité!}*

    *[Supports didactiques : ordinateur et environnement de programmation, documentation papier ou en ligne – notions de cours projetées – cahiers élèves pour prise de notes]*

<center> 

```{image} png/Im17.png
:width: 300px
:height: 200px
``` 
</center> 

<center>
Environnement de programmation python et bibliothèque pyo
</center>
</br>
</br>
</br>

<a name="Chapter2"></a>

# Génération et enregistrement sonores 

<a name="Section2.1"></a>

## Générer et enregistrer un son analogique

<a name="Section2.1.1"></a>

### Les instruments acoustiques « classiques »
Quelques principes de génération sonore pour les instruments acoustiques : piano , saxophone, guitare, percussions.
</br>
<center> 

```{image} png/Im18.png
:width: 300px
:height: 200px
``` 
</center> 
<center>
Instruments acoustiques : piano, saxophone, guitare, percussion
</center>
</br>


* *{Activité 9.1 : par la pratique instrumentale (plus ou moins sommaire...) de l’enseignant, les élèves tentent de s’approprier les mécanismes de production sonore pour les instruments acoustiques. Ces aspects sont repris par l’enseignant via un support projeté : percussion (onde mécanique), résonance, conduit aérien et forme (saxophone...) ou table d’harmonie}*
    *[Supports didactiques : instruments, audio, photos, vidéo, cahiers élèves pour prise de notes]*

<a name="Section2.1.2"></a>

### Les synthétiseurs analogiques
Les musiques électroniques se sont popularisées dans les années 80 quand les avancées technologiques, appuyées sur les résultats de la recherche scientifique, ont permis le développement d'un nouvel instrument : le synthétiseur. Rien n'est enregistré à l'intérieur, il n'a pas de mémoire, il crée lui-même des sons sous forme de signaux électriques qui sont ensuite transformés en signaux sonores à l'aide d'une ou plusieurs enceintes.


</br>
<center> 

```{image} png/Im19.png
:width: 400px
:height: 200px
``` 
</center> 
<center>
Synthétiseurs analogiques et électronique
</center>

</br>

* *{Activité 9.2 : présentation d’un synthétiseur analogique - principe. Génération d’un son en manipulant les différents modules (VCF, VCO, ...) et analogie avec l’étude préalable (signal pur, complexe, analyse spectrale, enveloppe, timbre (ADSR), .... Ce type d’instrument n’étant pas forcément facilement accessible pour l’enseignant, une séquence vidéo peut être présentée aux élèves. }*

    *[Supports didactiques : instruments, audio, photos, vidéo, cahiers élèves pour prise de notes]*

<a name="Section2.1.3"></a>

### « Capter » le son analogique
Principe du microphone permettant de capter un son analogique, afin de le distribuer sur un système d’amplification ou d’enregistrement.

</br>

<center> 

```{image} png/Im20.png
:width: 400px
:height: 200px
``` 
</center> 
<center>Prise de son avec un microphone dans une chambre anéchoïque</center>
</br>


<a name="Section2.1.4"></a>

### « Garder en mémoire » le son analogique
Principe de l’enregistrement analogique

</br>

<center> 

```{image} png/Im21.png
:width: 400px
:height: 200px
``` 
</center> 
<center>Enregistreur à bande de studio</center>

<a name="Section2.1.5"></a>

### Transmettre le son analogique

Principe de la diffusion analogique
* *{Activité 9.3 : présentation de la chaîne émetteur – microphone – amplificateur – enceintes}*

    *[Supports didactiques : instruments, matériel audio (microphone, amplificateur, enceintes), photos, vidéo, cahiers élèves pour prise de notes]*

</br>

<a name="Section2.2"></a>

## Générer et enregistrer un son numérique 

<a name="Section2.2.1"></a>

### Synthèse pwm – Problématique générale
Un exemple : cas de la synthèse pwm : du numérique à l’analogique (Raspberry Pi) et inversement.

</br>

<center> 

```{image} png/Im22.png
:width: 700px
:height: 150px
``` 
</center> 
<center>Principe de l’enregistrement numérique d’un signal analogique</center>
</br>

</br>
<center> 

```{image} png/Im23.gif
:width: 400px
:height: 200px
``` 
</center> 
<center>De l’analogique vers l’analogique... en passant par le numérique</center>
</br>

<a name="Section2.2.2"></a>

### Les synthétiseurs actuels et les banques de sons
De la synthèse analogique à la synthèse numérique (actuelle).
* *{Activité 10.1 : après une démonstration de l’enseignant via un synthétiseur numérique ou une vidéo, les élèves sont amenés à reprendre leurs fichiers créés via python... et reproduire les effets générés avec le synthétiseur : via pyo, puis en associant l’interface graphique, ils créent leur propre synthétiseur... numérique ! }*

    *[Supports didactiques : synthétiseur numérique ou support vidéo, ordinateur et environnement de programmation, documentation papier ou en ligne – notions de cours projetées – cahiers élèves pour prise de notes]*
</br>
<center> 

```{image} png/Im24.png
:width: 400px
:height: 200px
``` 
</center> 
<center>Synthèse sonore numérique actuelle – Outils pythons-pyo </center>  
</br>

<a name="Section2.2.3"></a>

### « Capter » le son numérique
Intérêt de la dispense de l’interface micro et de la transmission filaire ou wifi du signal numérique
* *{Activité 10.2 : simulation de l’émission-réception d’un signal analogique et d’un signal numérique : les élèves sont amenés à générer différents sons (purs, complexes) à partir de leurs codes python. Via la carte son, ces signaux sont rendus audibles et captés par un microphone. Ce microphone est relié à la carte d’acquisition de la machine et on accède au signal récupé directement sur l’ordinateur. Les élèves peuvent ainsi comparer le signal de départ avec celui d’arrivée, ayant subi deux conversions et le transit aérien sous forme analogique. Les élèves sont amenés à observer et comparer via un outil visuel Pyo. Ils exploitent à nouveau les fichiers créés au cours d’activités précédentes et peuvent en créer de nouveaux.*

    *[Supports didactiques : ordinateur et environnement de programmation, documentation papier ou en ligne, – notions de cours projetées – cahiers élèves pour prise de notes]*

</br>
<center> 

```{image} png/Im25.png
:width: 400px
:height: 200px
``` 
</center> 
<center>Câbles de transmission par fibre optique et routeur wifi</center>

</br>

<a name="Section2.2.4"></a>

### « Garder en mémoire » le son numérique
Principe et intérêt de l’enregistrement numérique
</br>
<center> 

```{image} png/Im26.png
:width: 400px
:height: 200px
``` 
</center>   
<center>Supports d’enregistrement numérique : disque dur Ssd et clé Usb</center>
</br>

<a name="Section2.2.5"></a>

### Transmettre le son numérique
#### Diffusion dans un réseau numérique
   
</br>
<center> 

```{image} png/Im27.png
:width: 400px
:height: 200px
``` 
</center>    
<center>Transmission de l’information sonore numérique sur le réseau digital</center>
</br>

* *{Activité 10.3 : simulation de la transmission de l’information d’un signal analogique et d’un signal numérique en fonction de la longueur du canal de transmission (câble standard / fibre optique). Les élèves sont amenés à introduire des constantes de propagation liées aux matériaux, effectuer des calculs et simuler les effets de la propagation avec un outil visuel Pyo. Ils exploitent à nouveau les fichiers créés au cours d’activités précédentes et peuvent en créer de nouveaux. Comparaison des signaux reçus.}*

    *[Supports didactiques : ordinateur et environnement de programmation, documentation papier ou en ligne – notions de cours projetées – cahiers élèves pour prise de notes]*
#### Diffusion vers un monde analogique (l’oreille humaine)
 </br>
</br>
<center> 

```{image} png/Im28.png
:width: 400px
:height: 200px
``` 
</center>       
<center>Conversion numérique – analogique – Méthodes de compression</center>
</br>

* *{Activité 10.4 : les élèves sont amenés à enregistrer leurs créations via différents formats d’enregistrement, compressés ou non, avec ou sans pertes (avi, mp3, wav, aiff, ...) et constater les différences ; puis ils s’échangent leurs créations via le réseau et constatent la fidélité lors du transfert de l’information numérique audio }*

    *[Supports didactiques : ordinateur et environnement de programmation, documentation papier ou en ligne – notions de cours projetées – cahiers élèves pour prise de notes]*
</br>
</br>
</br>

<a name="Chapter3"></a>

# Transmission du son

<a name="Section3.1"></a>

## Problématique du canal de transmission

<a name="Section3.1.1"></a>

### De l’émetteur vers le récepteur

Reprise des éléments du chapitre trois, activités de 10.1 à 10.4, synthèse et interprétation.

<a name="Section3.1.2"></a>

### Perturbation liée au canal de transmission : la fidélité
Reprise des éléments du chapitre trois, activités de 10.1 à 10.4, synthèse et interprétation.
Privilège de la transmission numérique, nécessité de « coder » l’information.
* *[Supports didactiques : ordinateur et environnement de programmation, documentation papier ou en ligne – notions de cours projetées – cahiers élèves pour prise de notes]*
</br>


<a name="Section3.2"></a>

## Solution : du signal physique au signal numérique 

<a name="Section3.2.1"></a>

### Théorie et codage de l’information
#### Analogique (historique et principe)
Des ondes acoustiques au micro-sillon et à la bande magnétique... La physique derrière les techniques classiques de « gravage » de l’information. Avantages et inconvénients.
#### Numérique – avantage et limites
Des ondes acoustiques... aux nombres
* *{Activité 11.1 : les élèves sont invités à écouter un passage musical sur un disque vinyle lu sur une platine disque puis commenter. Le même morceau de musique est ensuite écouté via une clé usb. Les élèves sont invités à commenter et tirer leurs propres conclusions. Pour terminer, une partie du passage musical diffusé en analogique est enregistré via le microphone et visualisé sur l’ordinateur via l’environnement graphique proposé par Py. Les élèves doivent sélectionner la partie correspondante sur le signal numérique et identifier les correspondances, ainsi que le bruit. Le travail proposé ici est l’opposé de la construction harmonique de l’activité 3 : il s’agit à présent « d’extraire » du signal parasite, le « bruit », afin de retrouver un signal se rapprochant le plus possible du signal numérique de départ. }*

    *[Supports didactiques : ordinateur et environnement de programmation, clé usb avec enregistrement numérique, disque vinyl et table de lecture, micro et enceintes, CAN, documentation papier ou en ligne – notions de cours projetées – cahiers élèves pour prise de notes]*



<
<a name="Section3.2.2"></a>

### Théorie de l’information de Shannon
</br>
<center> 

```{image} png/Im29.png
:width: 400px
:height: 200px
``` 
</center>     
<center> Concepts et outils pour l’échantillonnage </center>
</br>

* *{Activité 11.2 : les élèves vont échantillonner un signal au départ numérique diffusé depuis l’ordinateur sur une enceinte audio, via le convertisseur analogique / numérique. L’outil Pyo avec interface visuelle est utiliser. Les élèves peuvent choisir différentes fréquences d’échantillonnage et constater les effets visuels et audios. Le choix d’une fréquence acceptable doit amener au critère de Shannon, qui sera simplement énoncé ensuite.}*

    *[Supports didactiques : ordinateur et environnement de programmation, interfaces A/N, documentation papier ou en ligne – notions de cours projetées – cahiers élèves pour prise de notes]*

</br>


<a name="Section3.3"></a>

## Spécificités du codage numérique

<a name="Section3.3.1"></a>

### Un signal physique exprimé sous forme de ... 0 et de 1 ?!
* *{Activité 11.3 : les élèves vont échantillonner un signal numérique diffusé depuis l’ordinateur sur une enceinte audio, via le convertisseur analogique / numérique. L’outil Pyo avec interface visuelle est utilisé. Les élèves peuvent choisir différentes fréquences d’échantillonnage et constater les effets visuels et audios. Le choix d’une fréquence acceptable doit amener au critère de Shannon, qui sera simplement énoncé ensuite.}*

    *[Supports didactiques : ordinateur et environnement de programmation, interfaces A/N, documentation papier ou en ligne – notions de cours projetées – cahiers élèves pour prise de notes]*

</br>    

<a name="Section3.3.2"></a>

### Échantillonnage

Théorème de Shannon

</br>
<center> 

```{image} png/Im31.png
:width: 400px
:height: 200px
``` 
</center> 
<center>Principe de l’échantillonnage – aspects temporels et fréquentiels</center>

</br>
</br>
</br>

<a name="Conclusion"></a>

# Conclusion
Cette conclusion n’en est en fait pas une ! Les activités proposées et décrites ici peuvent être étendues et surtout envisagées à différents niveaux techniques et scientifiques pour les classes de maturité, avec une connexion disciplinaire transversale au choix mathématique, mécanique ou physique.
Nous l’avons mis en évidence : l’appropriation de savoirs et connaissances informatiques fondamentales est facilitée par la thématique du son, de l’analyse et de la production musicale. Gravitent autour de ce type d’activités des notions fondamentales de mathématiques, physique, mais également de traitement du signal et de l’information, ou même d’électronique.
La richesse du sujet invite donc à approfondir la mise en œuvre d’un tel type d’activités par un retour expérimental et des ajustements.

Les moyens matériels se résument à :

• ordinateurs standards intégrant éditeur et programme python (3.5 ou supérieur), ainsi que les biliothèques numpy, matplotlib et pyo,

• clés usb,

• convertisseurs analogique / numérique et cartes son,

• microphones et enceintes

• instruments de musique et synthétiseurs analogiques et numériques.

Les établissements gymnasiaux sont tous équipés d’ordinateurs, où généralement python est installé. La bibliothèque pyo est gratuite, les clés usb pour une classe représentent un moindre coût.
Convertisseurs, cartes sons, microphones et enceintes basiques, l’ensemble représente un investissement pour une classe de 22 élèves. Ces éléments facilement trouvables dans le commerce peuvent être montés facilement sur un circuit adapté, au sein d’un boitier, pour un coût moindre :

• CAN et carte son : ~30 à 40 chf,

• microphone et enceintes : ~30 à 40 chf,

• une demande de mise à disposition des instruments (ou de la salle de musique de l’établissement) peut être formulée, l’investissement pour les synthétiseurs analogiques restant important (~500 chf l’ensemble),

soit un investissement de moins de 100 chf par élève. Évidemment, les expérimentations de préférence individualisées pour les élèves peuvent être prises en charge par l’enseignant qui peut alors transmettre les signaux éventuellement récupérés à chaque élève. Cette option didactique réduit bien évidemment l’investissement relatif au type d’activités proposées.
