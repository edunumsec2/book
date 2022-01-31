### La chambre

 Dessinez une chambre avec des meubles, que vous définissez chacun par une fonction. Vous êtes libre d'inventer d'autres meubles, de les arranger différemment et de les utiliser de multiples fois.

 ```{codeplay}
 :file: chambre.py
 from turtle import *
 # Prénom, nom, classe
 def chaise():
     left(90)
     forward(100)
     back(50)
     right(90)
     forward(50)
     right(90)
     forward(50)
     left(90)
 def table():
     ...
 def lit():
     ...
 chaise()
 table()
 lit()
 done()
 ```

 ### Jeu du moulin
 Le [jeu du moulin](https://fr.wikipedia.org/wiki/Jeu_du_moulin) est un jeu de société traditionnel en Europe. Le tablier de jeu existait déjà dans la Rome antique. Aussi appelé **jeu du charret** (en Suisse), certains lui donnent le nom médiéval de jeu de mérelles, voire de marelle.
 ```{image} media/moulin.png
 :width: 200
 ```

 Pour les points d'intersection, utilisez la fonction `dot()` que vous allez découvrir plus en détail dans le chapitre suivant. La distance entre les lignes est de 50 pixels.  
 Vous constatez aussi une symétrie par 4. Donc avec un choix intelligent de fonction, vous pouvez réduire le nombre de lignes de code par 4.

 ```{codeplay}
 :file: moulin.py
 from turtle import *
 # Votre prénom, nom, classe
 width(8)
 up()
 forward(50)
 down()
 dot()
 forward(50)
 dot()
 forward(50)
 dot()
 ...
 done()
 ```

 ### Tetris

 Le jeu vidéo [Tetris](https://fr.wikipedia.org/wiki/Tetris) est un puzzle conçu par l'informaticien russe Alekseï Pajitnov en 1984.
 Tetris met le joueur au défi de réaliser des lignes complètes en déplaçant des pièces de formes différentes, les [tétrominos](https://fr.wikipedia.org/wiki/Tétromino), qui défilent du haut jusqu'au bas de l'écran.

 ```{image} media/tetris.png
 ```

 Les éléments de base d'un tétromino mesurent 20 x 20 pixels. Il existe 7 formes de tétrominos, qui sont nommés d'après les lettres auxquels ils ressemblent :

 - S
 - L
 - O (carré)
 - Z
 - I (bâton)
 - J
 - T

 ```{codeplay}
 :file: tetris.py
 from turtle import *
 # Votre prénom, nom, classe
 def I():
     down()
     forward(20)
     left(90)
     forward(80)
     left(90)
     forward(20)
     left(90)
     forward(80)
     left(90)
     up()
 def O():
     ...
 def T():
     ...

 def L():
     ...

 def J():
     ...

 def Z():
     ...
 def S():
     ...
 up()
 back(250)
 I()
 forward(40)
 O()
 ...
 done()
 ```