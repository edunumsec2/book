# Tic-tac-toe

Le tic-tac-toe, aussi appelé *morpion*, est un jeu de réflexion se pratiquant à deux joueurs au tour par tour dont le but est de créer le premier un alignement sur une grille de 3 x 3 cases.

Voici une partie gagnante pour le joueur X.

![tic-tac-toe](media/tic_tac_toe.png)

## Représenter le tableau

La structure de donnée appropriée pour représenter un tel jeu est un tableau 2D (en 2 dimensions). L'état initial est le tableau avec tous les éléments à 0.

Nous allons utiliser les entiers 1 et 2 pour représenter les pions du joueur 1 et 2.

```{codeplay}
state = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

for line in state:
    print(line)
```

Pour améliorer la présentation, nous allons utiliser le *packing* et *unpacking* d'une séquence.
Utiliser l'opérateur `*` est l'équivalent de déballer (unpacking) de la séquence et d'afficher `print(1, 2, 3)`.

```{codeplay}
a = (1, 2, 3)
print(a)
print(*a)   # unpacking de la séquence
````

Donc nous allons utiliser l'opérateur `*` avec la liste à imprimer pour créer une apparence plus compact.

```{codeplay}
state = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

for line in state:
    print(*line)
```

## Expliquer le jeu

Au début du jeu, il est utile d'afficher comment jouer le jeu.

```{codeplay}
state = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

explication = """\
Tic-tac-toe
-----------
Choisissez une case avec son nombre
1 2 3
4 5 6
7 8 9
"""

def help():
    print(explication)

def show():
    for line in state:
        print(*line)

help()
show()

x = input('Choisissez votre case: ')
```

## Jouer un tour

Ensuite faisons deux tours de jeu avec le joueur 1 et joueur 2.

```{codeplay}
state = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

explication = """\
Tic-tac-toe
-----------
Choisissez une case avec son nombre
1 2 3
4 5 6
7 8 9
"""

def help():
    print(explication)

def show():
    for line in state:
        print(*line)

help()
show()

x = int(input('Choisissez votre case: '))
state[(x-1) // 3][(x-1) % 3] = 1
show()

x = int(input('Choisissez votre case: '))
state[(x-1) // 3][(x-1) % 3] = 2
show()
```

## Alterner les tours

Nous désignons les joueurs avec 1 et 2 et utilisons une boucle `while` pour alterner entre les deux joueurs.

```{codeplay}
state = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

explication = """Choisissez une case
1 2 3
4 5 6
7 8 9"""

def help():
    print(explication)

def show():
    for line in state:
        print(*line)

help()
tour = 1
joueur = 1

while tour <= 9:
    x = int(input(f'\n{tour} - joueur {joueur} : '))
    state[(x-1) // 3][(x-1) % 3] = joueur
    joueur = 2 if joueur==1 else 1
    tour += 1
    show()
    
print('fin')
```

## Afficher lignes et colonnes

Pour vérifier une situation gagnante nous devons accéder aux :

- 3 lignes
- 3 colonnes
- 2 diagonales

```{codeplay}
state = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print('lignes:')
print(state[0])
print(state[1])
print(state[2])

c0 = [state[0][0], state[1][0], state[2][0]]
c1 = [state[0][1], state[1][1], state[2][1]]
c2 = [state[0][2], state[1][2], state[2][2]]

print('\ncolonnes:')
print(c0)
print(c1)
print(c2)
```

## Afficher les diagonales

Pour afficher les deux diagonales, nous composons une liste avec les éléments de la diagonale.

```{codeplay}
state = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

d0 = [state[0][0], state[1][1], state[2][2]]
d1 = [state[0][2], state[1][1], state[2][0]]

print('diagonales:')
print(d0)
print(d1)
```

## Qui a gagné ?

Ensuite il s'agit de déterminer à chaque tour si un joueur a gagné la partie.

```{codeplay}
def gagnant():
    l0 = state[0]
    l1 = state[1]
    l2 = state[2]

    c0 = [state[0][0], state[1][0], state[2][0]]
    c1 = [state[0][1], state[1][1], state[2][1]]
    c2 = [state[0][2], state[1][2], state[2][2]]
    
    d0 = [state[0][0], state[1][1], state[2][2]]
    d1 = [state[0][2], state[1][1], state[2][0]]

    for x in (l0, l1, l2, c0, c1, c2, d0, d1):
        if x == [1, 1, 1]:
            return 1
        elif x == [2, 2, 2]:
            return 2
        
    return 0

state = [[0, 0, 0],
         [0, 1, 0],
         [2, 1, 0]]
print(gagnant())

state = [[1, 0, 0],
         [0, 1, 2],
         [0, 2, 1]]
print(gagnant())

state = [[1, 0, 0],
         [2, 2, 2],
         [0, 1, 1]]
print(gagnant())
```

## Jouer un jeu complet

Maintenant nous pouvons combiner tous les éléments et jouer un jeu entier.

```{codeplay}
state = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

explication = """Choisissez une case
1 2 3
4 5 6
7 8 9"""

def help():
    print(explication)

def show():
    for line in state:
        print(*line)
        
def gagnant():
    l0 = state[0]
    l1 = state[1]
    l2 = state[2]

    c0 = [state[0][0], state[1][0], state[2][0]]
    c1 = [state[0][1], state[1][1], state[2][1]]
    c2 = [state[0][2], state[1][2], state[2][2]]
    
    d0 = [state[0][0], state[1][1], state[2][2]]
    d1 = [state[0][2], state[1][1], state[2][0]]

    for x in (l0, l1, l2, c0, c1, c2, d0, d1):
        if x == [1, 1, 1]:
            return 1
        elif x == [2, 2, 2]:
            return 2 
    return 0

help()
tour = 1
joueur = 1
winner = 0

while tour <= 9 and winner == 0:
    x = int(input(f'\n{tour} - joueur {joueur} : '))
    state[(x-1) // 3][(x-1) % 3] = joueur
    joueur = 2 if joueur==1 else 1
    tour += 1
    show()
    winner = gagnant()
    
if winner == 1:
    print('Bravo, le joueur 1 a gagné')
elif winner == 2:
    print('Bravo, le joueur 2 a gagné')
else:
    print('Match nul')
```

## Version graphique

Voici le début pour en créer une version graphique.
A vous de vous lancer à la programmation.

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

class Board:
    def __init__(self):
        self.pos = -150, -150
        self.box = 100, 100
        self.size = 3, 3
        self.draw()
        
    def draw(self):
        x0, y0 = self.pos
        dx, dy = self.box
        n, m = self.size
        
        for i in range(n + 1):
            y =  y0 + i * dy
            goto(x0, y)
            down()
            goto(x0 + n * dx, y)
            up()

        for i in range(m + 1):
            x = x0 + i * dx
            goto(x, y0)
            down()
            goto(x, y0 + m * dy)
            up()
            
    def click(self, x, y):
        x0, y0 = self.pos
        dx, dy = self.box
        n, m = self.size
        x1 = x0 + n * dx
        y1 = y0 + m * dy
        
        if x0 < x < x1:
            i = (x - x0) // dx
        if y0 < y < y1:
            j = (y - y0) // dy

        x = x0 + i * dx + dx/2
        y = y0 + j * dy + dy/2
    
        goto(x, y)
        dot(dx)
    
board = Board()
    
getscreen().onclick(board.click)
getscreen().listen()
```

