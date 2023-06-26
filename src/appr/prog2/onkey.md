# Déclencher - `onkey()`

Avec la fonction `input()` nous avons pu questionner l'utilisateur à un moment spécifique du programme. C'est utilisé pour demander une information spécifique à un moment précis.

Dans ce chapitre nous allons voir une autre façon d'utiliser les touches du clavier. Ici, appuyer sur une touche spécifique, à n'importe quel moment, va déclencher une action.

Dans ce chapitre nous découvrons comment utiliser le clavier de l'ordinateur pour interagir avec un programme. Nous allons voir que :

- la fonction `onkey(f, 'a')` installe une fonction de rappel `f()`,
- la fonction `f()` est appelée à chaque fois que la touche `a` est appuyée,
- la fonction `listen()` démarre l'*écoute* des événements du clavier.

```{question}
Une fonction de rappel

{f}`retourne à l'origine`  
{f}`renvoie une valeur`  
{f}`renforce la mémoire`  
{v}`réagit à un événement`
```

## Fonction de rappel

En informatique, une fonction de rappel (**callback** en anglais) ou fonction de post-traitement est une fonction qui est passée en argument à une autre fonction. Cette dernière peut alors faire usage de cette fonction de rappel comme de n'importe quelle autre fonction, alors qu'elle ne la connaît pas par avance.

## Avancer la tortue

Le programme suivant fait avancer la tortue à l'aide de la touche `a` du clavier qui appelle une fonction de rappel.
La variable `s` fait référence à l'objet `Screen` qui possède les deux méthodes :

- `onkey(f, 'a')` pour installer une fonction de rappel `f()` pour la touche `'a'`,
- `listen()` pour commencer à *écouter* les événements du clavier.

Deux lignes de texte sont affichées au début, pour que l'utilisateur sache qu'il doit d'abord cliquer dans la fenêtre de la tortue pour l'activer.

```{exercise}
Modifiez la fonction de rappel `f()` pour que la tortue tourne en cercle.
```

```{codeplay}
:file: onkey1.py
from turtle import *
shape('turtle')
color('red')

def f():
    forward(20)

s = getscreen()
s.onkey(f, 'a')
s.listen()

print("Cliquz dans la fenêtre pour l'activer.")
print("Appuyez sur la touche 'a' pour avancer.")
```

## Retourner à l'origine

La fonction `home()` ramène la tortue à son origine. Nous avons changé le nom de la fonction de rappel `f()` en `avancer()`. C'est plus clair. La fonction `home()` existe déjà, donc nous n'avons pas besoin de la définir.

Au lieu d'écrire les explications dans la console, nous allons les écrire directement dans la fenêtre de la tortue.

```{exercise}
Ajoutez une fonction de rappel pour faire reculer la tortue.
```

```{codeplay}
:file: onkey2.py
from turtle import *
up()
goto(-290, 180)
write('a–avancer  h–home', font=('Arial', 14))

home()
down()
shape('turtle')
color('red')

def avancer():
    forward(20)

s = getscreen()
s.onkey(avancer, 'a')
s.onkey(home, 'h')
s.listen()
```

## Effacer la trace

Dans le prochain programme, nous ajoutons des touches supplémentaires pour les fonctions suivantes :

- `h` pour ramener la tortue à l'origine avec `home()`,
- `c` pour effacer la trace avec `clear()`,
- `r` pour effacer la trace et ramener la tortue à l'origine avec `reset()`.

Le désavantage de ce programme, c'est que `clear()` va aussi effacer le texte explicatif. Ça serait bien si ce texte était indépendant de la tortue qui bouge.

```{codeplay}
:file: onkey3.py
from turtle import *
up()
goto(-290, 180)
write('a–avancer  h–home  c–clear', font=('Arial', 14))
home()
down()
shape('turtle')
color('red')

def avancer():
    forward(20)

s = getscreen()
s.onkey(avancer, 'a')
s.onkey(home, 'h')
s.onkey(clear, 'c')
s.listen()
```

## Tourner la tortue

Le programme suivant fait bouger la tortue à l'aide de 3 touches du clavier :

- `a` pour avancer
- `d` pour tourner à droite
- `g` pour tourner à gauche

```{exercise}
Ajoutez une fonction de rappel pour faire reculer la tortue.
```

```{codeplay}
:file: onkey4.py
from turtle import *
shape('turtle')
color('red')

def avancer():
    forward(50)

def gauche():
    left(30)
    
def droite():
    right(30)

s = getscreen()
s.onkey(avancer, 'a')
s.onkey(gauche, 'g')
s.onkey(droite, 'd')
s.onkey(home, 'h')
s.onkey(clear, 'c')
s.onkey(reset, 'r')
s.listen()
print("a:avancer  g:gauche  d:droite")
print("h:home     c:clear   r:reset")
```

## Les touches flèches

Les touches de flèche portent les noms `Left`, `Right`, `Up` et `Down`.
Nous pouvons utiliser les 4 flèches pour faire bouger la tortue.

- `↑` pour avancer
- `↓` pour reculer
- `←` pour tourner vers la gauche
- `→` pour tourner vers la droite

Le référentiel utilisé se rapporte à la tortue. Quand la tortue est en face de nous, c'est difficile de la contrôler, car nous devons inverser les directions dans notre tête.

```{exercise}
Ajoutez les fonctions de rappel `up()` et `down()` pour monter et descendre le stylo.
```

```{codeplay}
:file: onkey5.py
from turtle import *
shape('turtle')
color('red')

def avancer():
    forward(50)

def reculer():
    backward(50)

def gauche():
    left(30)
    
def droite():
    right(30)

s = getscreen()
s.onkey(avancer, 'Up')
s.onkey(reculer, 'Down')
s.onkey(gauche, 'Left')
s.onkey(droite, 'Right')
s.onkey(home, 'h')
s.onkey(clear, 'c')
s.onkey(reset, 'r')
s.listen()

print("Utilisez les flèches pour bouger la tortue.")
```

## Les touches WASD

Les jeux vidéos utilisent souvent les touches WASD pour déplacer le personnage du jeu (player) :

- `w` pour aller vers le haut
- `a` pour aller vers la gauche
- `s` pour aller vers le bas
- `d` pour aller vers la droite

Cette fois nous utilisons un référentiel absolu, fixé au canevas. La tortue peut se déplacer dans les 4 directions haut, bas, gauche et droite.

```{exercise}
Ajoutez les fonctions de rappel `home()`, `clean()` et `reset()` pour effacer la trace et ramener la tortue à l'origine.
```

```{codeplay}
:file: onkey6.py
from turtle import *
shape('turtle')
color('blue')
speed(0)

def droite():
    setheading(0)
    forward(50)
    
def haut():
    setheading(90)
    forward(50)

def gauche():
    setheading(180)
    forward(50)

def bas():
    setheading(270)
    forward(50)

s = getscreen()
s.onkey(haut, 'w')
s.onkey(gauche, 'a')
s.onkey(bas, 's')
s.onkey(droite, 'd')
s.listen()

print("Utilisez les touches WASD pour bouger la tortue.")
```

## Courbes en cercle

Appuyer sur la touche `g` va dessiner un quart de cercle à gauche. Appuyer sur la touche `d` va dessiner un quart de cercle vers la droite.

```{codeplay}
:file: onkey7.py
from turtle import *
shape('turtle')

def avancer():
    forward(50)
    
def gauche():
    circle(50, 90)
    
def droite():
    circle(-50, 90)
    
s = getscreen()
s.onkey(avancer, 'a')
s.onkey(gauche, 'g')
s.onkey(droite, 'd')
s.listen()
print("a:avancer  g:gauche  d:droite")
```

## Dessiner une maison

Appuyer sur la touche `m` va dessiner une maison.

```{codeplay}
:file: onkey8.py
from turtle import *
shape('turtle')

def avancer():
    forward(50)
    
def maison():
    forward(70)
    for a in (90, 45, 90, 45):
        left(a)
        forward(50)
    left(90)

s = getscreen()
s.onkey(avancer, 'a')
s.onkey(maison, 'm')
s.listen()
print("a:avancer  m:maison")
```

## Lever le stylo

Nous allons utiliser les touches `u` et `d` pour les fonctions

- `u` pour lever le stylo avec `up()`,
- `d` pour baisser le stylo avec `down()`.

```{codeplay}
:file: onkey9.py
from turtle import *
shape('turtle')

def avancer():
    forward(50)
    
def maison():
    down()
    forward(70)
    for a in (90, 45, 90, 45):
        left(a)
        forward(50)
    left(90)

getscreen().onkey(avancer, 'a')
getscreen().onkey(maison, 'm')
getscreen().onkey(up, 'u')
getscreen().onkey(down, 'd')
getscreen().listen()
print("a:avancer  u:up  d:down  m:maison")
```

## Choisir l'épaisseur

Nous allons introduire des touches pour choisir l'épaisseur du trait.

- `1` pour un trait fin,
- `2` pour un trait normal,
- `3` pour un trait épais.

```{exercise}
Modifiez les épaisseurs.
```

```{codeplay}
:file: onkey10.py
from turtle import *
shape('turtle')

def fin():
    width(1)

def normal():
    width(3)

def epais():
    width(10)

def avancer():
    forward(50)
    
def tourner():
    left(90)

getscreen().onkey(avancer, 'a')
getscreen().onkey(tourner, 't')
getscreen().onkey(fin, '1')
getscreen().onkey(normal, '2')
getscreen().onkey(epais, '3')
getscreen().listen()
print("a:avancer  t:tourner  1:fin  2:normal  3:épais")
```

## Choisir la couleur

Nous allons introduire des touches pour choisir l'épaisseur du trait.

- `r` pour un trait rouge,
- `v` pour un trait vert,
- `b` pour un trait bleu.

```{exercise}
Modifiez les couleurs.
```

```{codeplay}
:file: onkey11.py
from turtle import *
shape('turtle')
width(3)

def rouge():
    color('red')

def vert():
    color('lime')

def bleu():
    color('blue')

def avancer():
    forward(50)
    
def tourner():
    left(90)

getscreen().onkey(avancer, 'a')
getscreen().onkey(tourner, 't')
getscreen().onkey(rouge, 'r')
getscreen().onkey(vert, 'v')
getscreen().onkey(bleu, 'b')
getscreen().listen()
print("a:avancer  t:tourner  r:rouge  v:vert  b:bleu")
```

## Écrire dans le canevas

Nous pouvons aussi utiliser les touches pour écrire dans le canevas de la tortue. Pour avancer la tortue avec la lettre, nous choisissons l'option `move=True`

```{codeplay}
:file: onkey12.py
from turtle import *

def x():
    write('x', font=(None, 50), move=True)

getscreen().onkey(x, 'x')
getscreen().listen()
```

## Exercice

### Snake

Utilisez une liste pour limiter le nombre de segments du serpent à 10.

```{codeplay}
:file: snake.py
from turtle import *
shape('square')
color('red')

d = 20
speed(0)
dot(d)

def haut():
    seth(90)
    forward(d)
    dot(d)

def bas():
    seth(-90)
    forward(d)
    dot(d)

def gauche():
    seth(180)
    forward(d)
    dot(d)
    
def droite():
    seth(0)
    forward(d)
    dot(d)

s = getscreen()
s.onkey(haut, 'Up')
s.onkey(bas, 'Down')
s.onkey(gauche, 'Left')
s.onkey(droite, 'Right')
s.onkey(clear, 'c')
s.listen()
```

### Tetris

Les flèches gauche/droite permettent de déplacer le tétronimo. Programmez les touches haut/bas pour le tourner.

```{codeplay}
:file: tetris.py
from turtle import *
hideturtle()
tracer(0)
up()
d = 20

def L():
    fillcolor('orange')
    begin_fill()
    for a in 0, 90, 90, -90, 0, 90, 90, 0, 0, 90:
        forward(d)
        left(a)
    end_fill()
    
L()
update()

def gauche():
    clear()
    backward(d)
    L()
    update()
    
def droite():
    clear()
    forward(d)
    L()
    update()

s = getscreen()
s.onkey(gauche, 'Left')
s.onkey(droite, 'Right')
s.onkey(clear, 'c')
s.listen()
```
