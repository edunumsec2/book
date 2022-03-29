# Puissance 4

Puissance 4 est un jeu de stratégie combinatoire abstrait, commercialisé pour la première fois en 1974 par la Milton Bradley Company.

Le but du jeu est d'aligner une suite de 4 pions de même couleur sur une grille comptant 6 rangées et 7 colonnes.

![puissance4](media/puissance4.png)

Tour à tour, les deux joueurs placent un pion dans la colonne de leur choix, le pion coulisse alors jusqu'à la position la plus basse possible dans ladite colonne à la suite de laquelle c'est à l'adversaire de jouer. Le vainqueur est le joueur qui réalise le premier un alignement (horizontal, vertical ou diagonal) consécutif d'au moins quatre pions de sa couleur.

## Version console

Nous commençons la programmation avec une représentation du jeu.
De nouveau nous choisissons un tableau 2D. Les entrés ont la signification suivante :

- 0 - la case est vide
- 1 - la case contient un pion du joueur 1
- 2 - la case contient un pion du joueur 2

```{codeplay}
state = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

def show():
    for line in state:
        print(line)

tour = 0
player = 1

show()

x = int(input('Entrez votre colonne: '))
```

## Alterner les tours

Le jeu peut continuer pour un maximum de 42 tours.

```{codeplay}
state = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

def show():
    for line in state:
        print(line)

tour = 1
joueur = 1

while tour <= 42:
    x = int(input(f'\nTour {tour} - joueur {joueur} : '))
    
    tour += 1
    joueur = 2 if joueur == 1 else 2
    show()
```

## Parcourir en ligne

Par rapport aux coordonnes `(x, y)` de la tortue, l'ordre des indices `(i, j)` d'un tableau est inversé. Les matrices 2D en mathématique utilisent cette convention :

- indice de ligne `i` désigne la direction `y`
- indice de colonne `j` désigne la direction `x`

```{codeplay}
table = [[0, 1, 2, 0, 2],
         [2, 1, 2, 1, 2],
         [0, 1, 2, 0, 2]]

table[0][2] = 9
table[1][3] = 9

for line in table:
    print(line)
```

La deuxième différence est la position de l'origine :

- l'origine du tableau `(0, 0)` est en haut à gauche
- l'origine de l'image  `(x0, y0)` est en bas à gauche

Donc, la direction de `y` et `i` est inversée.
Nous en tenons compte dans la fonction `pos(i, j)`.

`y = y0 + (n - 1 - i) * d`

```{codeplay}
from turtle import *
color('red')

d = 50
n, m = 5, 7
x0 = -d * (m-1) / 2
y0 = -d * (n-1) / 2

def pos(i, j):
    x = x0 + j * d
    y = y0 + (n - 1 - i) * d
    return x, y

for i in range(n):
    for j in range(m):
        goto(pos(i, j))
        dot(d/2)
```

## Parcourir en colonne

Nous allons parcourir colonne par colonne.

- indice de ligne `i` désigne la direction `y`
- indice de colonne `j` désigne la direction `x`

```{codeplay}
from turtle import *
color('lime')

d = 50
n, m = 5, 7
x0 = -d * (m-1) / 2
y0 = -d * (n-1) / 2

def pos(i, j):
    return x0 + j * d, y0 + (n - 1 - i) * d

for j in range(m):
    for i in range(n):
        goto(pos(i, j))
        dot(d/2)
```

## Parcourir en diagonale

Nous allons parcourir le tableau en diagonale.
Combien de diagonales avons-nous ?

Dans un tableau `n` fois `m` nous avons `n + m - 1` diagonales.
Nous allons utiliser la variable d'itération `k` pour désigner une diagonale.

```{codeplay}
n, m = 4, 6

for i in range(n):
    print([0] * m)
  
print()
for k in range(m + n - 1):
    i0 = max(0, k-n-1)
    i1 = min(k+1, n)
    print(f'diagonale {k} - i in range({i0}, {i1})')
```

- indice de ligne `i` désigne la direction `y`
- indice de colonne `j` désigne la direction `x`

```{codeplay}
from turtle import *
color('blue')

d = 50
n, m = 5, 7
x0 = -d * (m-1) / 2
y0 = -d * (n-1) / 2

def pos(i, j):
    return x0 + j * d, y0 + (n - 1 - i) * d

for k in range(m + n - 1):
    i0 = max(0, k-n-1)
    i1 = min(k+1, n)
    for i in range(i0, i1):
        goto(pos(i, k-i))
        dot(d/2)
```

## L'autre diagonale

```{codeplay}
from turtle import *
color('blue')

d = 50
n, m = 5, 7
x0 = -d * (m-1) / 2
y0 = -d * (n-1) / 2

def pos(i, j):
    return x0 + j * d, y0 + (n - 1 - i) * d

for k in range(m + n - 1):
    i0 = max(0, n-k-1)
    i1 = min(m+n-k-1, n)
    for i in range(i0, i1):
        goto(pos(i, i+k+1-n))
        dot(d/2)
```

## Puissance 4

Voici un début d'une version graphique.
Essayez de compléter le jeu.

```{codeplay}
from turtle import *
hideturtle()
speed(0)
up()

class Board:
    def __init__(self, pos=(-150, -150), size=(6, 7), d=50):
        self.x0, self.y0 = pos
        self.n, self.m = size
        self.d = d
        self.x1 = self.x0 + self.m * self.d
        self.y1 = self.y0 + self.n * self.d
        self.turn = 0
        self.bg()
        
    def bg(self):
        goto(self.x0, self.y0)
        color('blue')
        begin_fill()
        for d in (self.m * self.d, self.n * self.d) * 2:
            forward(d)
            left(90)
        end_fill()
        
        color('white')
        for i in range(self.n):
            for j in range(self.m):
                goto(self.pos(i, j))
                dot(self.d - 10)
        
    def grid(self):
        for i in range(self.n + 1):
            y =  self.y0 + i * self.d
            goto(self.x0, y)
            down()
            goto(self.x1, y)
            up()

        for j in range(self.m + 1):
            x = self.x0 + j * self.d
            goto(x, self.y0)
            down()
            goto(x, self.y1)
            up()
            
    def pos(self, i, j):
        x = self.x0 + j * self.d + self.d//2
        y = self.y0 + i * self.d + self.d//2
        return x, y
    
    def click(self, x, y):
        if self.x0 < x < self.x1:
            j = (x - self.x0) // self.d
        if self.y0 < y < self.y1:
            i = (y - self.y0) // self.d

        c = 'red' if self.turn % 2 else 'yellow'      
        self.turn += 1
        color(c)
        goto(self.pos(i, j))
        dot(self.d - 10)
    
board = Board()
    
getscreen().onclick(board.click)
getscreen().listen()
```
