# Clavier - `onkey`

Dans ce chapitre nous découvrons comment nous pouvons utiliser le clavier de l'ordinateur pour interagir avec un programme.

- la fonction `onkey(f, 'c')` installe une fonction `f` quand la touche `c` est appuyé
- 

## Gauche-droite

Les touches de flèche portent le nom `left`, `right`, `up` et `down`.

```{codeplay}
from turtle import *
shape('turtle')
speed(0)

def go_left():
    back(10)

def go_right():
    forward(10)

getscreen().onkey(go_left, 'left')
getscreen().onkey(go_right, 'right')
getscreen().listen()
print("Clickez dans la fenêtre pour l'activer et pressez left/right.")
```

## Les touches WASD

Les jeux vidéo utilisent souvent les touches WASD pour déplacer le personnage du jeu (player).

```{codeplay}
from turtle import *

speed(0)
shape('turtle')
d = 50

def go_left():
    setheading(0)
    forward(d)
    
def go_up():
    setheading(90)
    forward(d)

def go_right():
    setheading(180)
    forward(d)

def go_down():
    setheading(270)
    forward(d)

getscreen().onkey(go_up, 'w')
getscreen().onkey(go_right, 'a')
getscreen().onkey(go_down, 's')
getscreen().onkey(go_left, 'd')
getscreen().listen()

print("Cliquez dans la fenêtre pour l'activer.")
print("Utilisez les touches WASD pour bouger la tortue.")
```

## Key events `lambda`

```{codeplay}
from turtle import *
speed(0)

getscreen().onkey(home, 'h')
getscreen().onkey(clear, 'c')
getscreen().onkey(reset, 'r')

getscreen().onkey(up, 'u')
getscreen().onkey(down, 'd')

getscreen().onkey(lambda : forward(50), 'space')
getscreen().onkey(lambda : seth(0), 'right')
getscreen().onkey(lambda : seth(90), 'up')
getscreen().onkey(lambda : seth(180), 'left')
getscreen().onkey(lambda : seth(-90), 'down')
getscreen().listen()

print("Cliquez dans la fenêtre pour l'activer.")
print("Utilisez les touches de direction pour orienter la tortue.")
print("Utilisez espace pour avancer.")
print("Utilisez U/D pour up/down.")
print("Utilisez H/C/R pour home/clear/reset.")
```
