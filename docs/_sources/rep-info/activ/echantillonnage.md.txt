# 3. Echantillonnage 

Classe : 1M, 2M

<span style="color:green">Difficulté de manipulation : basique </span> 
<sup> [1](#myfootnote1)</sup>

<span style="color:green">Difficulté conceptuelle : élevée </span>  

Prérequis structurel :
2 séances de 45mn, devant machines pour les élèves. 

Configuration pour la machine enseignant : le logiciel Audacity installé avec une sortie son de qualité, un éditeur python (Visual Studio, Thonny , ou autre) avec les librairies installées et codes fournis dans l'activité. 

Pour les élèves, des machines avec le logiciel Audacity installé, accès à des écouteurs personnels, connexion internet (accès au support Modulo - apprendre, puis aux questionnaires en fin d'activité).

<!--
Les fichiers suivants sont à télécharger pour l'activité complète : ...
--> 
    

## 3.1. Objectifs 

### 3.1.1. Objectif informatique

Le premier objet de cette activité est de permettre à l'élève d'appréhender la problématique de la représentation de l'information au sens large, comme le passage d'un univers symbolique à un autre.  
Il s'agit tout d'abord de passer d'un espace physique sensoriel (l'audition) à un autre espace sensoriel (la vue) 
en utilisant la modélisation mathématique du son avec des variations sinusoïdales, puis sa représentation numérique discrète avec une qualité variable qui sera présente par exemple dans les téléphones et autres objets numériques des élèves.
<!--
et à la modélisation mathématique permettant de représenter ce phénomène acoustique : la représentation pseudo-sinusoïdale continue d'une onde sonore théorique, puis sa représentation numérique discrète. 
-->

Ce premier travail intellectuel doit permettre aux élèves d'une part de se familiariser avec le matériau servant de support aux activités suivantes (quelques notions élémentaires relatives au son), et d'autre part de faciliter leur compréhension du codage binaire du son en faisant un lien entre la réalité physique et le binaire.


<!--
et d'autre part de faciliter leur compréhension du changement de paradigme ultérieur entre l'espace physique (plutôt que mathématique) et l'espace numérique et le codage binaire de l'information.  
-->


Le second objet de cette activité est de permettre aux élèves de se familiariser avec un outil tel qu'Audacity, qui permet de visualiser graphiquement le son et de le reproduire auditivement, offrant deux modes de représentation du son.  
En particulier la notion de discrétisation, de fréquence d'échantillonnage et le niveau de segmentation minimal en lien avec la qualité du son peuvent être perçus visuellement et auditivement (découpage de l'onde sonore en une multitude de points et perception des effets de la fréquence d'échantillonnage sur la qualité du rendu).
    
Enfin la notion de taille de fichier directement liée au nombre de points pris sur l'onde sonore permet de faire le lien entre codage binaire et qualité du son.    

### 3.1.2. Objectif mathématique et physique (transversal)

L'activité permet de réactiver, confirmer ou souligner des savoirs mathématiques relatifs aux relations fonctionnelles, aux représentations dans le plan et à la trigonométrie.
L'activité permet de réactiver, confirmer ou souligner des savoirs mécaniques et physiques relativement aux ondes, à la notion de milieu de propagation, de période et de fréquence.
</br> </br>

## 3.2. Spécifications

### 3.2.1. Mode

**«Branché/débranché»** utilisation de l'ordinateur et du logiciel Audacity - pas d'environnement de développement.  Cette activité pourrait permettre de faire utiliser le tableur et ses fonctionnalités aux élèves et coïncider avec un enseignement de type bureautique - science informatique transversal.

### 3.2.2. Pré-requis  

- Informatique :
        <span style="color:green">utilisation de l'ordinateur et familiarisation avec l'environnement informatique
        </span> 
        
    Pour l'enseignant : il est recommandé d'utiliser python à partir de la version 3.9. Il faut préalablement réaliser les installations des librairies via la commande pip dans la console :

        pip install numpy   
        pip install matplotlib   
        pip install pyo  
        pip install WxPython 

        python3.9 /Users/.../Puresignalsum.py
        
    
- Mathématique :
        <span style="color:orange">fonctions,</span>
        <span style="color:orange">fonctions trigonométriques simples,</span> 
        <span style="color:orange">notions d'amplitude, de période et de fréquence,</span> 
        <span style="color:green">représentation sur un repère plan,</span> 
        <span style="color:green">notion d'espace continu / discret</span> 
        
    
- Physique :
        <span style="color:orange">notion d'onde mécanique (pression, compression-dilatation) et sa représentation</span>    


### 3.2.3. Moments didactiques

 **1er moment didactique.** Mise en situation, apport théorique initial - Première séance (cours) - <span style="color:violet">45mn</span>

</br> **2ème moment didactique.** Exploration individuelle : chaque élève prend possession du matériel, des outils : ordinateur, environnement de travail, logiciel Audacity, matériel audio - Deuxième séance (activité proprement dite) - <span style="color:violet">15-25mn</span>

</br> **3ème moment didactique.** Moment technique et technologique : les élèves manipulent le programme Audacity, lancent les exécutions, manipulent les fenêtres graphiques (interfaces), observent les graphes et écoutent différentes portions de morceaux de musique (3 maximum) - <span style="color:violet">20-30mn</span>

</br> **4ème moment didactique.** Mise en commun et institutionnalisation : l'enseignant reprend la main au tableau et vidéoprojecteur. Examen des modes de représentation visuel et audio : sens, interprétation. Interprétation du visuel de la courbe sonore dilatée temporellement : la *discrétisation numérique* est mise en évidence. L'enseignant recueille de manière guidée les appréciations des élèves sur la qualité du morceau de musique écouté à différentes *fréquences d'échantillonnage*. Cette notion est simplement posée à ce stade, elle sera reprise et développée dans le temps suivant. Le recueil des appréciations concernant la qualité sonore peut être réalisé via un tableau où figurent en première ligne toutes les fréquences autour de la fréquence médiane 48000 Hz, et dans la ligne suivante la qualité perçue par les élèves : Mauvaise / Convenable / Bonne ; l'enseignant inscrit un segment (représentation au tableau) pour chaque choix de chaque qualité associée, ou travaille de préférence directement sur un [tableau excel](/tab/appqualson.ods) complété avec les retours élèves  - <span style="color:violet">20-30mn</span>

</br> **5ème moment didactique.** Travail sur la technique : les élèves sont laissés en autonomie une bonne partie du temps sur leurs postes de travail, expérimentent les outils et concepts institutionnalisés en manipulant les paramètres d'Audacity (zoom temporel, visualisation de parties du morceau, identification de l'aspect «sinusoïdal») en fin de troisième séance - <span style="color:violet">15-25mn</span>

</br> **6ème moment didactique.** Evaluation formative ou sommative portant sur les aspects théoriques disciplinaires ou transdisciplinaires. {download}`Devoir - évaluation maison de type quiz moodle<quizzech.ods>`  - <span style="color:violet">20-30mn</span>
</br>


### 3.2.4 Supports didactiques
    
Ordinateur individuel, logiciel Audacity, casque audio individuel connecté sur la sortie audio de l'ordinateur de chaque élève, documentation en ligne (Modulo - apprendre : https://dev-apprendre.modulo-info.ch/rep-info/son.html), supports papier éventuels pour la prise de notes. Ordinateur enseignant avec sortie audio (2 enceintes - stéréo), vidéoprojecteur, tableau, codes python installés et testés.


### 3.2.5. Durée
La séquence d'enseignement se découpe en <span style="color:violet"> deux périodes de 45mn </span> en demi-classes.

</br> 

## 3.3. Déroulement

### 3.3.1. Première période : éléments de cours sur l'information et le son en particulier, puis manipulation logicielle (Audacity par les élèves, codes python par l'enseignant)

#### 3.3.1.1 Eléments théoriques

**<span style="color:red">DE T0 À T1 = T0 + 15mn</span>**

Ce premier moment de cette première séance doit être vu comme une introduction à la problématique traitée par l'activité proprement dite. Elle est aussi l'occasion de travailler la transdisciplinarité avec d'autres disciplines fondamentales (mathématiques, physique) mais également d'aborder la discipline artistique que les élèves affectionnent tout particulièrement qu'est la musique..  
Elle peut donc s'effectuer en parallèle d'un de ces enseignements, en coordination avec un enseignant de ces disciplines : mathématiques, physique, ou musique.  
Les éléments mathématiques et physiques théoriques suffisants sont présentés dans cet ouvrage à la section 1.1 : Signal analogique (physique) temporel. L'enseignant peut également s'appuyer sur certains éléments de la section 1.2 Contenu fréquentiel (analyse spectrale).  
Une introduction sous l'angle de la musique pourra s'appuyer sur une approche instrumentale mettant en évidence les notions de hauteur (fréquence), de timbre (richesse harmonique), d'onde de pression transmise dans un espace matériel : ceci devra être fait en collaboration avec un enseignant de musique, avec le concours d'instruments divers : piano, flute, cordes, cuivres ou vents...  
</br>
Les éléments principaux à évoquer sont : 
    
- [L’oreille comme capteur](https://enseigner.modulo-info.ch/content/ens/theme/rep-info/support/son/visu-et-ecoute-son.html#Section1.1.2)

- Le son : [une onde sinusoïdale de compression-dilatation](https://enseigner.modulo-info.ch/content/ens/theme/rep-info/support/son/visu-et-ecoute-son.html#Section1.1.1)

- Notion de fréquence : nombre de battements par seconde. Nombre de fois où le signal redevient identique par seconde.

- Avec les fonctions python [**tracesinus**](#tracesinus) et [**listensinus**](#listensinus), l'enseignant affiche et fait écouter quelques exemples de sons «purs» (grave médium et aigu).

- L'enseignant ajoute ensuite plusieurs signaux sinusoïdaux avec la fonction python [**puresignalssum**](#puresignalssum)  : somme d’harmoniques écoutée et visualisée.

- À la fin de la première période : l'enseignant sensibilise les élèves à l'utilisation d'Audacity : ouverture du logiciel, écoute d'un ou plusieurs morceaux. Les élèves commencent à manipuler en toute fin de séance et s'exerceront concrètement au cours de la suivante.


Une idée intéressante est de proposer d'aborder les notions fondamentales physiques de manière accessible via de courtes séquences vidéo explicités et reprises ensuite par l'enseignant.

Une première vidéo de 2 mn résume de manière assez complète l'ensemble des paramètres physiques mis en jeu lors du processus de production - transmission - réception sonore.


```{youtube} QEpk6feHMxQ
`````

<br>

Les éléments mentionnés peuvent être repris en temps réel ou différé par l'enseignant au tableau ou en déroulant un document powerpoint, pour permettre leur développement ensuite :
- cerveau de l'émetteur du son -> impulsions électriques -> cordes vocales -> ondulations -> molécules qui s'entrechoquent -> oreille -> tympan vibrant -> message électrique -> cerveau du récepteur du son

- musique = onde générée par une vibration

- signal analogique (physique) -> micro -> signal électrique

- signal électrique -> enceinte -> signal analogique (physique)

- son = onde = molécules vibrant à une certaine vitesse (fréquence), avec une certaine force (amplitude)

- vitesse de vibration des molécules = nombre de vibration par seconde = fréquence, unité le hertz (Hz)

- fréquence haute <=> vitesse des molécules élevée <=> son aigu

- amplitude élevée <=> ampleur importante du mouvement des molécules <=> son fort

- molécules => milieu matériel nécessaire : sans molécules (dans le vide par exemple), pas de son


Une deuxième vidéo très courte (27 s) permet de revenir sur le rôle du milieu de propagation et l'oscillation des molécules permettant la transmission du son.


```{youtube} kW9nwkrfGFw
`````

<br>

Enfin, une troisième vidéo diffusée à vitesse lente (0,25) permet de comprendre la relation entre le déplacement de ces molécules et la forme sinusoïdale caractéristique de la description d'une onde sonore.


```{youtube} XFyT1bsSnHI
`````

La molécule (illustrée par le bouchon ici) vibre verticalement ; dans le phénomène de propagation du son, les molécules vibrent horizontalement.
<br>

L'image animée ci-dessous illustre la propagation d'une onde telle qu'elle pourrait se visualiser après l'impact d'une pierre à la surface de l'eau par exemple.

<br>

<center>

```{image} media/son_couv1.gif
:width: 750
:height: 400
```
</center>

<br>

Dernier point : un son est donc une vibration qui se transmet dans l'air généralement. Mais peut-on «entendre» toutes ces vibrations ?

La vidéo ci-dessous permet d'apprécier justement ce que l'oreille humaine perçoit selon la fréquence du signal sonore :


```{youtube} o-lYdioQMfY
`````

La gamme de fréquences audibles apparait d'environ **20 Hz à 20000 Hz (ou 20 KHz)**. En-dessous, ou au-dessus, l'oreille humaine ne perçoit rien ou quasiment rien. En revanche, la physiologie humaine reste sensible à ces fréquences extrêmes.


<br> <br>


*Problématique de la représentation :* fonction sinus (non détaillée, simplement citée), amplitude, fréquence, période. Rappels mathématiques et physiques sur les notions abordées : notion d'onde de pression, compression-dilatation, compréhension de la représentation graphique (sinus). L'enseignant peut traiter rapidement la notion d'onde sonore comme la somme de «sons élémentaires», en fonction du niveau et de la sensibilité de la classe.

</br>

#### 3.3.1.2. Manipulation logicielle : Audacity - Aspects visuel et auditif d'un signal sonore

**<span style="color:red">DE T1 À TF = T1 + 30mn</span>**

Ce second moment de la séance vise à faire manipuler le logiciel Audacity par les élèves, puis en particulier à tenter de leur faire faire le parallèle entre la forme des signaux qu'ils visualisent et la forme sinusoïdale explicitée dans le premier moment de séance. L'enseignant manipule ses propres codes python afin d'expliciter les notions de fréquence, de hauteur de son (grave / aigu), puis de composition fréquentielle.

1ère phase.

**<span style="color:red">DE T1 À T2 = T1 + 10mn</span>**

L'enseignant communique les recommandations aux élèves afin d'utiliser le logiciel Audacity : ouvrir le logiciel, aller chercher le fichier son dans leur espace, manipuler les touches principales (lire, arrêter, revenir, se déplacer avec la souris sur le fichier son.

Les élèves travaillent de manière autonome, au casque individuel, les échanges entre eux sont limités. L'enseignant circule dans la classe et s'assure de l'appropriation des outils. Il revient au tableau régulièrement afin de dérouler les consignes : lancement d'Audacity, manipulation, écoute du morceau, zoom. 





</br>
<left> 
<html>
    <head>
        <title> audio1.mp3 </title>
    </head>
    <body>
        <div id="player">
        <audio controls>
        <source src="https://maitre.edunumsec2.ch/_videos/Audio1.mp3" type="audio/mpeg">
        </audio> 
        </div>
    </body> 
</html>     


```{figure} media/
---
align: left
alt:
width: 100%
---
**Ecoute d'un morceau de musique sur Audacity**
```

<br> <br>




```{figure} media/Im39.png
---
align: left
alt:
width: 100%
---
**Visualisation d'un morceau de musique sur Audacity**
```

<br> <br>

<left> 
<html>
    <head>
        <title> Util_Audacity.mov </title>
    </head>
    <body>
        <div id="player">
        <video width="500" height="300" controls>
        <source src="https://maitre.edunumsec2.ch/_videos/Util_Audacity.mov" type="video/quicktime">
        </audio> 
        </div>
    </body> 
</html>    


```{figure} media/
---
align: left
alt:
width: 100%
---
**Manipulation d'un morceau de musique sur Audacity**
```


<br> <br>




```{figure} media/Im38.png
---
align: left
alt:
width: 100%
---
```

```{figure} media/Im37.png 
---
align: left
alt:
width: 100%
---
```

```{figure} media/Im36.png
---
align: left
alt:
width: 100%
---
```

```{figure} media/Im35.png
---
align: left
alt:
width: 100%
---
**Zoom sur une partie du morceau visualisé sous Audacity : dilatation temporelle, composition fréquentielle.**
```


L'enseignant s'assure de la bonne compréhension des phénomènes suivants : notions d'amplitude et de fréquence, dilatation temporelle. Il pose la question de l'interprétation des oscillations perçues sur le signal (fréquences «visibles» des composantes du signal). 

<!--
En particulier, sur la dernière visualisation, on observe qu'on peut mettre en évidence une «quasi-période» entre les instants 06,8320 et 06,8345. Le calcul de la période donne donc 06,8345-06,8320 = 0,0025s, soit une fréquence de 1/0,0025 = 400Hz. L'enseignant questionne les élèves sur cette fréquence : est-elle basse ? haute ? 
-->

2ème phase.

**<span style="color:red">DE T2 À TF = T2 + 20mn</span>**

L'enseignant s'appuie ensuite sur la génération d'un son «pur» à 400Hz, 800 puis 1200 Hz, via les codes python **tracesinus**, **listensinus**. Les élèves peuvent ainsi relier fréquence et hauteur, auditivement et graphiquement.

<!--
Par la visualisation et l'écoute, les élèves peuvent se représenter l'information visible sur le fichier audio (composante de fréquence ~ 400Hz), 
-->

L'enseignant utilise ensuite le code **puresignalssum** en rentrant la fréquence fondamentale 400Hz, puis ses 4 harmoniques suivantes : 800, 1200, 1600, 2000Hz).

Les élèves observent alors ce qui se passe, toujours auditivement et visuellement, quand on ajoute plusieurs sons élémentaires (synthèse additive).

L'enseignant fait le parallèle entre la représentation graphique ainsi obtenue, et ce que les élèves peuvent observer sur Audacity.


<a name="tracesinus"></a>

```
from __future__ import print_function
import math
import numpy as np
import matplotlib.pyplot as plt
from pyo import *
from tkinter import Tk, StringVar, Label, Entry, Button, Frame, DoubleVar, Spinbox
from functools import partial

def tracesinus(freq):
#  sinus function at freq(Hz) frequency
    t = np.arange(0., 0.01, 0.00005)
    plt.plot(t,np.sin(2*pi*freq*t))
    label1 = "fonction sinus, fréquence " 
    label2 = str(freq) 
    label3 = "Hz"
    label = label1 + label2 + label3 
    plt.ylabel(label)
    plt.show()

tracesinus(400)
   ```

<a name="listensinus"></a>   
```
from __future__ import print_function
import math
import numpy as np
import matplotlib.pyplot as plt
from pyo import *
from tkinter import Tk, StringVar, Label, Entry, Button, Frame, DoubleVar, Spinbox
from functools import partial

def listensinus(freq):
#  sinus function at freq(Hz) frequency
   s = Server().boot()
   s.start()
   a = Sine(freq, mul=1, add=0).out()
   time.sleep(5)
   s.stop()

listensinus(400)   
   ```

<a name="puresignalssum"></a>   
```
from __future__ import print_function
import math
import numpy as np
import matplotlib.pyplot as plt
from pyo import *
from tkinter import Tk, StringVar, Label, Entry, Button, Frame, DoubleVar, Spinbox
from functools import partial

def puresignalssum(freq, harmo):
#  harmonic signals
   s = Server().boot()
   somme = 0
   for i in range (1,harmo+1):
      s.start()
      a = Sine(i*freq, mul=1, add=0).out()
      time.sleep(1)
#  graphic vizualisation       
      namesc = 'Signal '+str(i*freq)+' Hz'
      somme=somme+a
   s.stop
   sc = Scope(somme, 0.003, 0.2, wintitle='somme des signaux')
   somme.out
   s.gui(locals())

puresignalssum(400, 5)   

```

<br> 





### 3.3.2 Deuxième séance : discrétisation et fréquence d'échantillonnage 


Cette deuxième période traite des aspects disciplinaires informatiques à proprement parler sur lesquels on souhaite sensibiliser les élèves.

#### 3.3.2.1 Discrétisation

Cette étape aborde la problématique de la discrétisation d'un signal sonore.

**<span style="color:red">DE T0 À T1 = T0 + 15mn</span>**

L'enseignant reprend le logiciel Audacity et poursuit le zoom sur le signal ; il questionne les élèves sur l'interprétation de ce qu'ils voient - une succession de points, et non plus une courbe continue). Il les amène progressivement à la compréhension de la notion de *discrétisation*, résultat du passage d'une représentation continue *apparente* correspondant à la **réalité physique** à une représentation discrète *réelle* correspondant à la **réalité numérique**.



```{figure} media/Im40.png
---
align: left
alt:
width: 100%
---
```

```{figure} media/Im41.png
---
align: left
alt:
width: 100%
---
**Zoom sur une partie du morceau visualisé sous Audacity : mise en évidence de la discrétisation.**
```


#### 3.3.2.2 Echantillonnage

Cette étape traite de l'échantillonnage d'un signal sonore.

**<span style="color:red">DE T1 À T2 = T1 + 25mn</span>**


L'enseignant propose aux élèves d'écouter une partie du morceau de musique choisi à différentes fréquences proposées par Audacity : 8000 Hz, 22050 Hz, 44100 Hz, 88200 Hz, 176400 Hz.

```{figure} media/Im55.png
---
align: left
alt:
width: 100%
---
**Ecoute à différentes fréquences d'échantillonnage sous Audacity.**
```

Après une dizaine de minutes d'écoute autonome, l'enseignant questionne les élèves sur ce qu'ils ont écouté, la qualité des sons enregistrés à différentes fréquences et sur leur interprétation des fréquences indiquées. Il leur demande d'enregistrer chaque fichier son à chaque fréquence, en suivant le format : {download}`Audio1_8000.mp3<media/Audio1_8000.mp3>` par exemple pour l'enregistrement du fichier Audio1 à la fréquence d'échantillonnage de 8000 Hz. - <span style="color:violet">10-15mn</span>. Les fichiers suivants sont en particulier obtenus (ceux aux fréquences supérieures, lourds, ne sont volontairement pas chargés):
{download}`Audio1_8000.mp3<media/Audio1_8000.mp3>`, 
{download}`Audio1_22050.mp3<media/Audio1_22050.mp3>`,
{download}`Audio1_44100.mp3<media/Audio1_44100.mp3>`.


**<span style="color:red">DE T1 À T2 = T1 + 25mn = T0 + 45mn</span>**

L'enseignant met ensuite en commun et institutionnalise : il reprend la main au tableau et vidéoprojecteur. Examen des modes de représentation visuel et audio : sens, interprétation. Interprétation du visuel de la courbe sonore dilatée temporellement : la *discrétisation numérique* est mise en évidence. L'enseignant recueille de manière guidée les appréciations des élèves sur la qualité du morceau de musique écouté à différentes *fréquences d'échantillonnage*. Le recueil des appréciations concernant la qualité sonore est réalisé via un tableau  {download}`fichier de type excel<media/appqualson.ods>` où figurent en première ligne toutes les fréquences proposées, et dans la ligne suivante la qualité perçue par les élèves : Mauvaise / Convenable / Bonne ; l'enseignant interroge la classe par un vote à main levée sur la qualité du son perçue pour chaque choix de fréquence, et complète en temps réel avec les retours élèves. 

```{figure} media/tabexcel1.png
---
align: left
alt: Exemple de tableau excel enseignant récoltant les appréciations par les élèves de la qualité sonore de l'échantillon.
width: 100%
---
**Exemple de tableau excel enseignant récoltant les appréciations par les élèves de la qualité sonore de l'échantillon.**
```

Une fois le tableau est projeté et complété au fur et à mesure : l'enseignant questionne les élèves sur l'interprétation qu'ils peuvent donner des graphes issus du tableau de données. Il doit faire ainsi ressortir la qualité perçue à partie de la fréquence d'échantillonnage de 44100Hz. La nécessité d'une *fréquence d'échantillonnage minimale* doit ici apparaître.
Dans un deuxième temps, l'enseignant interroge sur les résultats pour les fréquences supérieures. L'inutilité d'aller au-delà d'une certaine fréquence (en l'occurence 44100 Hz) doit ressortir.
L'étape suivante consiste à identifier cette valeur de 44100 Hz : à quoi correspond-elle ? L'enseignant revient sur le champ audible par l'oreille humaine : 20Hz - 20000Hz, en faisant référence à la dernière vidéo projetée lors de la première séance.

Il situe alors 44100Hz par rapport à la fréquence la plus élevée que peut percevoir l'oreille humaine, 20000Hz... La fréquence d'échantillonnage apparaît comme devant être au moins égale au double de cette fréquence de 20000Hz.
Ensuite, l'enseignant revient sur la notion même de fréquence d'échantillonnage. Que signifie-t-elle ? C'est le nombre d'échantillons pris par unité de temps. L'enseignant peut illustrer son propos par le dernier visuel de la figure 4 : entre les temps 6,8310s et 6,8315s, on dénombre à peu près 23 échantillons, soit 23/0,0005 = 46000Hz. On retrouve quasiment la fréquence 44100 Hz apparaissant en bas à gauche de la fenêtre Audacity.

```{figure} media/Im41.png
---
align: left
alt:
width: 100%
---
**Identification de la fréquence d'échantillonnage (ici 44100Hz).**
```
En dernier lieu, il convient de s'interroger sur les conséquences de l'augmentation de la fréquence d'échantillonnage. 
L'enseignant demande à la classe, par l'intermédiaire de quelques élèves, les tailles constatées des fichiers enregistrés aux différentes fréquences, et complète ces valeurs dans le tableau excel situé en partie basse de la feuille du fichier excel intégrant la taille des fichiers numérisés aux différentes fréquences. 

```{figure} media/tabexcel2.png
---
align: left
alt:
width: 100%
---
**Echantillonnage et occupation mémoire.**
```



Le graphique affiche clairement la croissance forte de l'occupation mémoire en fonction de la fréquence d'échantillonnage, au delà de 44100Hz... - ainsi que le changement du mode de compression (on passe d'un format MP3 à un format WAV)-. L'analyse avec les élèves de la courbe permet de comprendre explicitement la nécessité de borner la fréquence d'échantillonnage : pas trop faible pour garantir une bonne qualité audio, pas trop élevée pour ne pas occuper inutilement de la place mémoire - <span style="color:violet">20-25 mn</span>.


### 3.3.4. Retours enseignant et élèves : questionnaires

Cette étape de «retours» doit permettre à l'enseignant d'apprécier la manière dont son activité est «passée» auprès des élèves, d'améliorer, de modifier ou d'affiner l'organisation de sa séquence d'enseignement.

**<span style="color:red">DE T2 À TF= T2 + 10mn</span>**


La séquence propose deux types de questionnaires, un premier à destination de l'[enseignant](https://www.surveymonkey.com/r/actens1), le second à destination des [élèves](https://www.surveymonkey.com/r/acteleve1).
Ces outils à destination de l'enseignant permettent une analyse a posteriori pour l'enseignant.


### 3.3.5. Evaluation : quizz moodle maison

L'évaluation pourra être réalisée via un quizz moodle open-book, en temps limité (<span style="color:violet">20-30mn</span>) créé par l'enseignant selon les compétences qu'il souhaite évaluer, et comportant 10-15 questions tirées du fichier excel {download}`Devoir - évaluation maison de type quizz moodle <media/QuizzEch.ods>`.
L'enseignant pourra également programmer un cycle d'entrainement préliminaire avec une partie des questions proposées dans ce fichier excel.
   



<br/>
<br/>
<br/>