# Variables

## 1 Compteur
1. Ecrire et tester le programme suivant (en appyuant sur le bouton A du micro:bit):
    ````python
    from microbit import *
    compteur = 0
    while True:
        if button_a.was_pressed():
            compteur = compteur + 1
            display.scroll(compteur)
    ````
1. Modifier ce programme pour qu'il compte de deux en deux.
1. Que se passe-t-il si on rempace la deuxième ligne par \var{compteur = 5}?
1. Modifier le programme pour que le compteur commence à 10 et diminue chaque fois qu'on appuie sur A.
1. En utilisant la fonction `sleep(1000)`, écrire dans un fichier "compteur.py" un programme qui fait un compte à rebours de 10 secondes (sans qu'on ait besoin d'appuyer sur un bouton).
1. Modifier votre programme pour qu'il ajoute une image lorsque le compteur arrive à zéro.

## 2 Arythmie cardiaque
1. Reprendre le programme du cœur qui bat du fichier "cœur.py" et y ajouter la ligne `duree=500` avant la boucle `while`.
1. Modifier les appels à la fonction `sleep` afin de faire intervenir la variable `duree` dans les appels: `sleep(duree)`. 
1. Tester votre programme avec diverses valeurs de la variables `duree``
1. Modifier votre programme pour que le cœur batte de plus en plus vite. Il faut pour cela modifier la valeur de `duree` à l'intérieur de la boucle `while`. 
1. Avec un instruction `if`, modifier le programme pour que si la durée d'un battement de cœur passe en dessous de 50 ms, on la remet à 1000 ms. 


## 3 Tamagotchi
Le but de ce programme est de programmer un petit Tamagotchi, un petit animal de compagnie virtuel populaire dans les années 1990.

1. Ecrire et tester le programme suivant qui représente un Tamagotchi placide (et peu intéressant): 
    ````python
    from microbit import *
    while True:
        display.show(Image.HAPPY)
        sleep(500)
    `````
1. Modifier ce programme pour que le Tamagotchi dise "Miam" lorsqu'on appuie sur le bouton A du Tamagotchi (c'est ainsi qu'on le nourrit). 
1. Définir une variable `faim=0` qui indique à quel point le Tamagotchi a faim et augmenter la faim du Tamagotchi chaque demi-seconde. 
1. Modifier le programme pour que la faim du Tamagotchi revienne à zéro lorsqu'on appuie sur le bouton A. 
1. Modifier le programme pour que le Tamagotchi dise "j'ai faim!" lorsque sa faim dépasse 20. 
1. Modifer le programme pour que le Tamagotchi affiche un visage triste lorsque sa faim dépasse 30. 
1. Modifier le programme pour que le Tamagotchi s'éteigne (avec l'instruction `display.clear()`) lorsque sa faim dépasse 50. 
1. Etoffer le comportement du Tamagotchi en utilisant le bouton B ou la posture du Tamagotchi, par exemple en le rendant fatigué s'il n'est pas suffisamment couché.  

%%   \end{parts}