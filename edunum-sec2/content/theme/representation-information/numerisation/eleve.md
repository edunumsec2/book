# Numérisation

La conversion d’une grandeur physique analogique continue  – température, vitesse du vent, position d'une girouette… – en données numériques digitales est appelée *numérisation*. Elle est réalisée en trois étapes: un *échantillonnage*, une *quantification* puis un *encodage*.

Le processus de numérisation engendre une quantité d'information (des bits) qui vise à représenter, aussi précisément que nécessaire, la grandeur physique sous une forme manipulable par les ordinateurs. 

Il s'agit donc d'un compromis entre la qualité de la représentation et les coûts engendrés par un fichier plus grand, qui prend plus de place de stockage ; prend plus de temps à copier, à transmettre sur un réseau ; et/ou nécessite une puissance de calcul plus importante pour la numérisation (conversion analogique/digitale) et pour la restitution (conversion digitale/analogique).

Ci-après, un signal continu sera numérisé, mettant en évidence le rôle et les effets des différents paramètres de la numérisation. Il s'agira pour l'exemple de l'intensité sonore telle qu'elle peut être capturée par un microphone.


```{figure} media/numerisation-00.png
---
height: 16em
name: fig-repr-num-sig
---
Soit un signal continu à numériser, par exemple un son.
```



## Échantillonnage

L’intervalle temporel auquel les mesures sont prises est la *fréquence d’échantillonnage* (sampling rate)exprimée en Hz. 

Les limites pratiques d’un échantillonnage sont fixées par la fréquence de Nyquist, qui, de façon très simplifiée, indique que l’information découlant d’un processus dont la fréquence est deux fois supérieure à celle de l’échantillonnage sera perdue lors de la numérisation. Il ne sera donc jamais possible d'avoir une représentation complète d'un processus complexe, tout au mieux une représentation suffisante. 

Sachant que l’oreille humaine ne perçoit globalement que les fréquences entre 20 et 20 kHz, une fréquence d’échantillonnage supérieure à 40 kHz permettra de restituer l’ensemble de l’information physiologiquement perceptible par l’oreille humaine. C'est la raison pour laquelle l’échantillonnage de la musique en qualité “CD” est réalisé à 44.1 kHz. 

Une fréquence d'échantillonnage inférieure génère un son dans la qualité est dégradée, à commencer par la précision des sons les plus aigus, aboutissant à une numérisation qui rappelle le son des anciens téléphones analogiques. 

Une fréquence d’échantillonnage supérieure génère une plus grande quantité d’information, sans ajouter de valeur qualitative pour la très grande majorité des auditeurs.  

Ce choix résulte donc d'une délicate balance entre coûts (taille des données) et bénéfices (qualité de la numérisation).



```{figure} media/numerisation-01.png
---
height: 16em
name: fig-repr-num-freq
---
Effet de la fréquence d'échantillonnage (sampling rate : 100, 200 et 400 Hz) 
sur la représentation obtenue par numérisation. 
Puis la fréquence est élevée, puis la quantité d'information est importante. 

```



## Quantification

La quantification de la valeur requiert de déterminer la *précision* de chaque échantillon, ce qui détermine le volume de données générées. Cela découle de la représentation des nombres par les ordinateurs. 

La précision de l'encodage est donnée par la *profondeur de l'échantillonnage* (bit depth) exprimée en bits (binary digits). Comme pour l'échantillonnage, plus la profondeur de l'échantillonnage est importante, plus la quantité d'information générée est importante. 



```{figure} media/numerisation-02.png
---
height: 16em
name: fig-repr-num-depth
---
Effet de la profondeur de l'échantillonnage (bit depth : 3, 4 et 5 bit) 
sur la représentation obtenue par numérisation. 
Plus la profondeur est importante, plus la discrimination du signal et 
la différence entre les bases et les hautes intensités est importante.
La quantité d'information générées (le nombre de 0 et de 1) devient 
également plus importante.
```


Lorsque l'entier de la plage des valeurs possibles est utilisée pour l'encodage, la profondeur de l'échantillonnage définit la *plage dynamique* disponible. Elle est donnée entre la valeur encodée la plus petite (0, par exemple) à la valeur encodée la plus élevée (2^n - 1 pour une valeur encodée sur n bits, par exemple).

Ici encore, l'oreille humaine ne peut percevoir ni les intensités les plus faibles (inférieures au bruit émis par l'individu lui-même) ni les intensités au-delà du seuil de douleur. 

Une précision minimale (environ 8 bit) est ainsi nécessaire à restituer agréablement un enregistrement respectant les subtilités de l'expression orale (entre voix posée et criée, par exemple). 

Au-delà de 16 bit, une profondeur d'échantillonnage supérieure engendre une plage dynamique qui n'a pas d'application pertinente pour la restitution des sons aux humains, au coût d'une quantité d'information collectée.




À l'inverse, il est nécessaire de gérer correctement la plage d'amplitude dans laquelle la numérisation du signal se déroule. Cela s'opère en agissant sur le paramètre de *gain* du signal. 

La *distorsion* découle d’un signal dont l’amplitude dépasse les capacités d’encodage du système. Dans ces conditions, un ajustement du gain d’entrée est nécessaire pour rester au plus proche des limites du système, sans les franchir. 

La numérisation d’un signal dont l’amplitude serait par trop réduite débouche au contraire sur un encodage qui contient moins d’information, ce qui limite les opérations réalisables numériquement par la suite sans déteriorer la qualité.



```{figure} media/numerisation-04.png
---
height: 16em
name: fig-repr-num-dist
---
Effet du gain (trop haut, correct, trop bas) 
sur la représentation obtenue par numérisation.
La distorsion résulte de valeurs très différentes de celles du signal original. 
Cette aberration du processus de numérisation ne peut plus être corrigée, car de l'information a été perdue au passage.
```






On notera finalement que la numérisation et la quantification travaillent ensemble pour définir la qualité du signal numérisé. Ces deux paramètres ne sont pas complétement indépendants. Leur choix est réalisé en fonction du résultat escompté et de ce que l'on cherche à réaliser avec le signal numérisé. 

Pour l'intesité sonore par exemple, une fréquence d'échantillonnage insuffisante ne peut pas être compensée par une profondeur d'échantillonnage supérieure. La qualité du résultat n'est pas améliorée.


```{figure} media/numerisation-03.png
---
height: 16em
name: fig-repr-num-bal
---
Effet de la fréquence d'échantillonnage (sampling rate : 400, 200 et 100 Hz) 
sur la représentation obtenue par numérisation 
à une profondeur donnée (sampling depth : 5 bit).
Une importante profondeur d'échantillonnage ne compense pas une fréquence d'échantillonnage insuffisante.
```








## Encodage

L'encodage de l'information numérisée se fait dans des formats de fichiers spécifiques aux applications. 

Dans l'absolu, on pourrait imaginer un format universel de stockage de 0 et de 1. En connaissant la profondeur de l'échantillonnage, il serait aisément possible de reconstruite un signal. Toutefois, cela pose plusieurs problèmes. 

Cela ne donnerait aucune indication sur l'interprétation qu'il faut faire de ce signal (est-ce un son ? une image ? la variation de la vitesse du vent ?) ou même les bornes de ce signal (entre 0 et 2^n - 1 ? entre -2^(n-1) et 2^(n-1) - 1 ?).

De plus, cela serait terriblement dispendieux. Il est en effet possible de construire des formats de fichiers qui exploitent les propriétés specifiques au signal numérisé pour simplifier dans un deuxième temps le résultat de la numérisation avant de l'enregistrer. Cela débouche sur des fichiers qui sacrifient une partie de la qualité du signal numérisé en échange d'un gain sur la taille des fichiers générés. 

C'est ainsi que des fichiers optimisés différents sont disponibles pour stocker des fichiers d'images (JPG) ; de vidéo (MP4) ; de son (MP3) ou tout autre application. La plupart recourent pour cela à des compressions destructives au-cours desquelles une partie de l'information est abandonnées car, dans le contexte particulier, elles ne sont pas jugées indispensables.  
