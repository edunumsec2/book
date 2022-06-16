# Instructions

## 1. Affichage de texte
1. Ecrire le programme python suivant
    ```python
    from microbit import *
    display.scroll('Mon premier programme')
    ```
1. Brancher le micro:bit à l'ordinateur avec le cable USB, "flasher" le programme et vérifier qu'il s'exécute correctement en affichant un texte avec les LEDs

1. Modifier le programme pour qu'il affiche un autre texte, le flasher à nouveau, et vérifier si le comportement du micro:bit est conforme à vos attentes. 

1. Modifier le programme pour qu'il affiche quelques vers d'une poésie ou un extrait des paroles d'une chanson

1. Modifier le programme pour qu'il affiche trois fois cet extrait.


## 2. Affichage d'images
1. Dans un nouveau fichier, écrire et tester le programme suivant:
    ```python
    from microbit import *
    display.show(Image.HAPPY)
    ```

1. Visiter le [guide de référence python pour micro:bit](https://microbit-micropython.readthedocs.io/fr/latest/) et le mettre en signet dans votre navigateur

1. Lire la section Image du guide et modifier le programme ci-dessus pour qu'il affiche une autre image parmi celles définies dans le guide.

1. Tester différentes images proposées

1. Ecrire et tester le programme suivant:

    ```python
    from microbit import *
    display.show(Image.SAD)
    sleep(3000)
    display.show(Image.HAPPY)
    sleep(3000)
    `````
1. Modifer le programme pour qu'il affiche la première image plus longtemps. 
1. Modifier le programme pour qu'il affiche une autre séquence d'image
1. Modifier le programme pour qu'il affiche cette séquence six fois
1. Ecrire dans un nouveau fichier appelé "cœur.py" un programme qui montre un cœur qui bat en affichant successivement un grand et un petit cœur. Le cœur doit faire 1000 battements
1. Modifier le programme pour que le cœur batte plus vite. 

## 3 Animations
1. Créer une petite animation contenant du texte et des images
1. Regarder dans la documentation comment définr soi-même ses propres images et animation et essayer d'en créer. 