
# Exécution conditionnelle
## 1. Dis-moi comment tu vas?
1. Ecrire et tester le programme suivant qui utilise la fonction `button_a.was_pressed()` qui retourne vrai (`True`) si on a appuyé sur le bouton A du micro:bit depuis le début du programme ou le dernier appel à cette fonction, et faux (`False`) sinon.
    ````python
    from microbit import *
    display.scroll("Si tu te sens bien maintenant, appuie sur A.")
    sleep(2000) # on laisse 2 secondes pour appuyer
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
    ````
1. Modifier ce programme pour qu'il ajoute un commentaire encourageant si la personne n'appuie par sur A.
1.  Modifier ce programme pour qu'il ajoute un commentaire positif si la personne appuie sur A.
1. Modifier ce programme pour qu'il dise "Bye!" avant de s'arrêter. 
1. Modifier ce programme pour qu'il pose une autre question et ait d'autres réactions selon si la personne appuie ou pas
sur le bouton A.
1. Remplacer la ligne du \var{if} par la ligne suivante:
    ````python
    if button_a.was_pressed() or button_b.was_pressed():
    ````
    Tester en appuyant sur le bouton B.
1. Que se passe-t-il si on remplace le mot \var{or} par le mot \var{and}? Vérifier votre réponse.   
 
## 2. Quizz
1. Ecrire et tester le programme suivant:
    ````python
    from microbit import *
    display.scroll("Quelle est la capitale du Canada? A=Montreal, B=Ottawa")
    sleep(2000) # on laisse 2 secondes pour appuyer
    if button_a.was_pressed():
        display.scroll("Faux, la capitale est Ottawa")
    elif button_b.was_pressed():
        display.scroll("Juste, la capitale est Ottawa")
    else:
        display.scroll("Trop tard, la capitale est Ottawa")
    ````
1. Modifier ce programme pour qu'il pose une autre question.

## 3. Arrêt cardiaque
1. Ecrire et tester le programme suivant (il faut appuyer sur le bouton A du micro:bit):
    ````python
    from microbit import *
    display.scroll("Bonjour!")    
    while not button_a.was_pressed():
        display.scroll("...")
    display.scroll("Bye!")
    ````
1. Que va-t-il se passer si le mot \var{not} est enlevé de la troisième ligne? Vérifier sa réponse. 
1. Reprendre le programme de la série précédente qui affiche un cœur qui bat (sauvé dans le fichier "cœur.py") et modifier la ligne du `for`
pour qu'il s'arrête de battre lorsqu'on appuie sur le bouton A.
1. Modifier le programme du cœur pour qu'il affiche un fantôme (`Image.GHOST`) après qu'on a appuyé sur le bouton A. 


## 4. L'histoire sans fin
1. Ecrire et tester le programme suivant:
    ````python
    from microbit import *    
    while True:
        display.scroll("Ca continue...")
        sleep(100)
    ````
    Quand ce programme s'arrête-t-il?
1. Modifier ce programme pour qu'il affiche un sourire si on appuie sur A et un visage triste si on appuie sur B.
1. Modifier ce programme pour qu'il affiche aussi "Merci" si on appuie sur A et sur B en même temps. 
1. Dans un fichier 'histoire.py', écrire un programme qui raconte une histoire interactive, c'est-à-dire dont le déroulement dépend des actions de l'utilisateur-rice. 
