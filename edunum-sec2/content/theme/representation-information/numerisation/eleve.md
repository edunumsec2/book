# Numérisation

La conversion d’une grandeur physique continue  – intensité sonore, température… – en données numériques manipulables par un ordinateur est appelée numérisation. Elle requiert un échantillonnage et une quantification/encodage.

```{figure} media/numerisation-00.png
---
height: 16em
name: fig-repr-num-sig
---
Soit un signal continu à numériser.
```

L’intervalle temporel auquel les mesures sont prises est la fréquence d’échantillonnage (sampling rate).

```{figure} media/numerisation-01.png
---
height: 16em
name: fig-repr-num-freq
---
Effet de la fréquence d'échantillonnage (sampling rate : 100, 200 et 400 Hz) 
sur la représentation obtenue par numérisation.
```

Les limites pratiques d’un échantillonnage sont fixées par la fréquence de Nyquist, qui, de façon très simplifiée, indique que l’information découlant d’un processus dont la fréquence est deux fois supérieure à celle de l’échantillonnage sera perdue lors de la numérisation.
Sachant que l’oreille humaine perçoit globalement les fréquences entre 20 et 20 kHz, une fréquence d’échantillonnage supérieure à 40 kHz permettra de restituer l’ensemble de l’information physiologiquement perceptible par l’oreille humaine, raison pour laquelle l’échantillonnage de la musique en qualité “CD” est réalisé à 44.1 kHz. Une fréquence d’échantillonnage supérieure ne générerait que plus d’information sans ajouter de valeur qualitative pour la plupart des auditeurs.  

La quantification de la valeur requiert de déterminer la précision (bit depth) de chaque échantillon, ce qui détermine le volume de données générées.

```{figure} media/numerisation-02.png
---
height: 16em
name: fig-repr-num-depth
---
Effet de la profondeur de l'échantillonnage (sampling depth : 3, 4 et 5 bit) 
sur la représentation obtenue par numérisation.
```

Ici encore, plus on augmente la profondeur de l’encodage, plus la quantité d’information générée augmente, de même que la discrimination du signal, exprimée en amplitude (la différence entre l’intensité la plus faible et la plus élevée).

```{figure} media/numerisation-03.png
---
height: 16em
name: fig-repr-num-depth
---
Effet de la fréquence d'échantillonnage (sampling rate : 400, 200 et 100 Hz) 
sur la représentation obtenue par numérisation 
à une profondeur donnée (sampling depth : 5 bit).
```

La distorsion découle d’un signal dont l’amplitude dépasse les capacités d’encodage du système. Dans ces conditions, un ajustement du gain d’entrée est nécessaire pour rester au plus proche des limites du système, sans les franchir. La numérisation d’un signal dont l’amplitude serait par trop réduite débouche sur un encodage qui contient moins d’information.

```{figure} media/numerisation-04.png
---
height: 16em
name: fig-repr-num-dist
---
Effet du gain (trop haut, correct, trop bas) 
sur la représentation obtenue par numérisation.
```
