# Avancer - `onkey`

Dans cette deuxième partie nous allons avancer plus vite. Tout d'abord nous allons faire *avancer* la tortue à l'aide des touches du clavier. C'est une technique que nous allons utiliser plus tard pour les jeux vidéos. Nous allons découvrir également le concept *avancé* de la fonction lambda.

Dans ce chapitre nous découvrons comment utiliser le clavier de l'ordinateur pour interagir avec un programme. Nous allons voir que

- la fonction `onkey(f, 'a')` installe une fonction de rappel `f()`,
- la fonction `f()` est appelée à chaque fois que la touche `a` est appuyé,
- la fonction `lambda` permet de définir une fonction *sans nom*.

En passant nous allons aussi voir que

- la fonction `home()` ramène la tortue à l'origine,
- la fonction `clear()` efface les traces de la tortue,
- la fonction `xcor()` renvoie la coordonnée x de la tortue,
- la fonction `setx()` configure la coordonnée x de la tortue.

## Fonction de rappel

En informatique, une fonction de rappel (**callback** en anglais) ou fonction de post-traitement est une fonction qui est passée en argument à une autre fonction. Cette dernière peut alors faire usage de cette fonction de rappel comme de n'importe quelle autre fonction, alors qu'elle ne la connaît pas par avance.

## Avancer la tortue

Le programme suivant fait avancer la tortue à l'aide de la touche `a` du clavier.

La variable `s` fait référence à l'objet `Screen` qui possède les deux méthodes : 

- `onkey(f, 'a')` pour installer une fonction de rappel `f()` pour la touche `'a'`,
- `listen()` pour commencer à *écouter* les événements du clavier.

Deux lignes de texte sont affichées au début, pour que l'utilisateur sache qu'il doit d'abord cliquer dans la fenêtre pour l'activer.

```{codeplay}
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

**Exercice** : Modifiez la fonction de rappel `f()` pour que la tortue tourne en cercle.

## Retourner à l'origine

La fonction `home()` ramène la tortue à son origine. Nous avons changé le nom de la fonction de rappel `f()` en `avancer()`. C'est plus clair. La fonction `home()` existe déjà, donc nous n'avons pas besoin de la définir.

```{codeplay}
from turtle import *
shape('turtle')
color('red')

def avancer():
    forward(20)

s = getscreen()
s.onkey(avancer, 'a')
s.onkey(home, 'h')
s.listen()

print("Appuyez sur la touche 'a' pour avancer.")
print("Appuyez sur la touche 'h' pour home.")
```

**Exercice** Ajoutez une fonction de rappel pour faire reculer la tortue.

## Effacer la trace

Dans le prochain programme nous ajoutons des touches supplémentaires pour les fonctions suivantes :

- la fonction `home()` ramène la tortue à l'origine,
- la fonction `clear()` efface la trace,
- la fonction `reset()` efface la trace et ramène la tortue à l'origine.

```{codeplay}
from turtle import *
shape('turtle')
color('red')

def avancer():
    forward(20)

s = getscreen()
s.onkey(avancer, 'a')
s.onkey(home, 'h')
s.onkey(clear, 'c')
s.onkey(reset, 'r')
s.listen()

print("Appuyez sur la touche 'a' pour avancer.")
print("Appuyez sur la touche 'h' pour home.")
print("Appuyez sur la touche 'c' pour clear.")
print("Appuyez sur la touche 'r' pour reset.")
```

**Exercice** : Ajoutez une fonction de rappel pour faire tourner la tortue.

## Tourner la tortue

Le programme suivant fait bouger la tortue à l'aide de 3 touches du clavier :

- `a` pour avancer
- `d` pour tourner à droite
- `g` pour tourner à gauche

```{codeplay}
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

print("Appuyez sur la touche 'a' pour avancer.")
print("Appuyez sur la touche 'g' pour gauche.")
print("Appuyez sur la touche 'd' pour droite.")
```

**Exercice** : Ajoutez une fonction de rappel pour faire reculer la tortue.

## Les flèches

Les touches de flèche portent les nom `left`, `right`, `up` et `down`.
Nous pouvons utiliser les 4 flèches pour faire bouger la tortue.

Le référentiel utilisé se rapporte à la tortue. Quand la tortue est en face de nous, c'est difficile de la contrôler, car nous devons inverser les directions dans notre tête.

```{codeplay}
from turtle import *
shape('turtle')
color('red')

def avancer():
    forward(50)

def reculer():
    back(50)

def gauche():
    left(30)
    
def droite():
    right(30)

s = getscreen()
s.onkey(avancer, 'up')
s.onkey(reculer, 'down')
s.onkey(gauche, 'left')
s.onkey(droite, 'right')
s.onkey(home, 'h')
s.onkey(clear, 'c')
s.onkey(reset, 'r')
s.listen()

print("Utilisez les flèches pour bouger la tortue.")
```

**Exercice** : Ajoutez les fonctions de rappel `up()` et `down()` pour monter et descendre le stylo.

## Les touches WASD

Les jeux vidéos utilisent souvent les touches WASD pour déplacer le personnage du jeu (player).

Cette fois nous utilisons un référentiel absolu, fixé au canevas. La tortue peut se déplacer dans les 4 directions haut, bas, gauche et droite.

```{codeplay}
from turtle import *
shape('turtle')
color('blue')
speed(0)
d = 50

def droite():
    setheading(0)
    forward(d)
    
def haut():
    setheading(90)
    forward(d)

def gauche():
    setheading(180)
    forward(d)

def bas():
    setheading(270)
    forward(d)

getscreen().onkey(haut, 'w')
getscreen().onkey(gauche, 'a')
getscreen().onkey(bas, 's')
getscreen().onkey(droite, 'd')
getscreen().listen()

print("Utilisez les touches WASD pour bouger la tortue.")
```

**Exercice** : Ajoutez les fonctions de rappel `home()`, `clean()` et `reset()` pour effacer la trace et ramener la tortue à l'origine.

## Fonction lambda

Parfois nous avons besoin d'une petite fonction, sans que ça vaut la peine de la définir de façon officielle avec le mot clé `def` et un nom de fonction.

```{codeplay}
def f(x):
    return x ** 3

print(f(2))
print(f(5))
```

Parfois nous avons juste besoin d'une fonction éphémère *sans nom*. Une telle fonction s'appelle fonction **lambda**.

```{codeplay}
print((lambda x : x ** 3)(2))
print((lambda x : x ** 3)(5))
```

La fonction **lambda** est pratique, parce qu'on peut la passer comme argument dans une fonction. On peut aussi l'affecter à une variable.

```{codeplay}
a = lambda x : x ** 3

print(a(2))
print(a(5))
```

## Argument `lambda`

Revenons vers notre tout premier programme. Nous voulons faire avancer la tortue quand nous appuyons sur la touche `a`. On est tenté de simplifier le programme et d'écrire ceci. Essayé-le, mais malheureusement ça ne fonctionne pas.

```{codeplay}
from turtle import *
shape('turtle')

s = getscreen()
s.onkey(forward(50), 'a')
s.listen()
```

C'est ici que la fonction `lambda` est très pratique. Nous pouvons créer une fonction *éphémère* sans nom.

```{codeplay}
from turtle import *
shape('turtle')

s = getscreen()
s.onkey(lambda : forward(50), 'a')
s.listen()
```

**Exercice** : Faites avancer la tortue avec la touche `a`.

## Bouger avec `lambda`

Avec la fonction lambda notre programme devient très compacte. Nous utilisons les fonctions 

- `xcor()` pour lire la position actuelle de la coordonnée `x`.
- `setx()` pour assigner une nouvelle valeur à la coordonnée `x`.

Comme cette dernière fonction n'agit pas sur l'orientation de la souris, nous choisissons le disque (`circle`) comme forme pour la tortue.

```{codeplay}
from turtle import *
shape('circle')
speed(0)
d = 50

s = getscreen()
s.onkey(lambda : setx(xcor() + d), 'right')
s.onkey(lambda : setx(xcor() - d), 'left')
s.onkey(lambda : sety(ycor() + d), 'up')
s.onkey(lambda : sety(ycor() - d), 'down')
s.listen()
```
