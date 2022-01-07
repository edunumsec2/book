# Cliquer - `onclick`

Dans ce chapitre nous explorons comment un programme peux détecter un clic de souris et y réagir.
Cliquer (ou toucher) est la méthode principale pour interagir avec un smartphone : on touche avec le droit une certaine position de l'écran et le programme y réagit. Nous allons voir que

- la méthode `onclick(f)` permet de définir une fonction qui réagit à un clic,
- la fonction `f(x, y)` est appelé lors d'un clic, avec les coordonnés x et y,
- la méthode `listen()` met en marche les événements interactifs.
 
## Fonction `onclick`

La méthode `onclick(f)` permet de définir une fonction `f` qui est alors appelé à chaque fois quand on clique avec la souris dans le canevas.

A ce moment la fonction `f` est appelé avec les coordonnés `(x, y)` du clic de la souris.

Le programme suivant dessine un point à la position du clic et affiche les coordonnées dans la console.

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

def f(x, y):
    print('clic à', x, y)
    goto(x, y)
    dot()
    
getscreen().onclick(f)
getscreen().listen()
```

**Exercice** : Cliquez dans les 4 coins et au centre.

## Dessiner une forme

Dans ce programme nous dessinons une ligne entre les clics successifs. 
C'est pour cette raison nous appelons la fonction `ligne(x, y)` au lieu de `f(x, y)`.

Nous réagissons également à deus touches du clavier :

- `u` (up) pour lever le stylo
- `c` (clear) pour effacer le canevas

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

def ligne(x, y):
    goto(x, y)
    down()
    dot()
    
getscreen().onkey(up, 'u')
getscreen().onkey(clear, 'c')
    
getscreen().onclick(ligne)
getscreen().listen()
```

**Exercice** : Dessinez une maison.

## Echéquier

Ici nous dessinons d'abord un tableau de jeu. Ensuite nous détectons la case dans laquelle le clic a eu lieu et y ajoutons un disque noir.

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

x0, dx, nx = -160, 40, 10
y0, dy, ny = -160, 40, 8
x1 = x0 + nx * dx
y1 = y0 + ny * dy

for i in range(ny + 1):
    y = y0 + i * dy
    goto(x0, y)
    down()
    goto(x0 + nx * dx, y)
    up()
    
for i in range(nx + 1):
    x = x0 + i * dx
    goto(x, y0)
    down()
    goto(x, y0 + ny * dy)
    up()

def f(x, y):
    if x0 < x < x1:
        i = (x - x0) // dx
    if y0 < y < y1:
        j = (y - y0) // dy

    x = x0 + i * dx + dx/2
    y = y0 + j * dy + dy/2
    
    goto(x, y)
    dot(dx)
    
getscreen().onclick(f)
getscreen().listen()
```

**Exercice** : Cliquez dans chaque deuxième case.


```{codeplay}
 
```

```{codeplay}
 
```

```{codeplay}
 
```