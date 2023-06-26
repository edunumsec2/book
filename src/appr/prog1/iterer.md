(prog1.iterer)=
# Itérer - `range()`

Dans ce chapitre, nous allons voir de près comment une variable peut parcourir ou itérer sur une plage numérique.

Une boucle permet de raccourcir le code et de mieux le structurer.
Une boucle ne représente pas seulement une économie de lignes de code, mais donne aussi la possibilité de contrôler le nombre de répétitions. Nous allons voir que :

- la boucle `for` répète du code pour un ensemble de valeurs données,
- la variable d'itération `i` prend une autre valeur à chaque tour,
- le parcours est possible sur des plages numériques, du texte, et des listes.

```{question}
En informatique, itérer c'est

{v}`parcourir`  
{f}`bifurquer`  
{f}`appeler`  
{v}`répéter`
```

## Parcourir une séquence

Dans la boucle `for` une variable d'itération va parcourir une valeur après l'autre d'une séquence d'objets. Cette séquence peut être :

- une plage numérique avec `range()`,
- une chaîne de caractères,
- une liste.

La **variable d'itération** prend successivement les valeurs 0 à n-1.
Comme la variable d'itération est de type entier (`int`) on l'appelle souvent `i`.

Nous reprenons l'exemple précédent du polygone, mais cette fois nous ne dessinons pas les segments, mais seulement les sommets. La valeur de la variable d'itération `i` est affichée à chaque sommet du polygone.

```{exercise}
Testez avec des nombres différents entre 5 et 13.
```

```{codeplay}
:file: range2.py
from turtle import *

n = 9       # nombre de sommets
a = 50      # longueur du côté
up()

for i in range(n):
    forward(a)
    left(360/n)
    write(i)
```

## Itérer avec `range()`

La fonction `range(start, stop, step)` permet de produire une séquence linéaire d'entiers. Les entiers se trouvent dans l'intervalle semi-fermé `[start, stop[` avec un incrément de `step`.

Le sens des paramètres :

- `start` est la valeur de départ,
- `stop` est la valeur finale, mais sans l'inclure,
- `step` est l'incrément.

La fonction `print()` utilise le paramètre optionnel `end` pour ne pas terminer avec un retour à la ligne, mais par un simple espace.

```{exercise}
Affichez les entiers entre -50 et 200 avec un incrément de 25.
```

```{codeplay}
:file: range3.py
from turtle import *
up()

start = -250
stop = 250
step = 50

for x in range(start, stop, step):
    goto(x, 0)
    write(x)
```

## Dessiner une spirale

Si nous dessinons un polygone, mais augmentons la longueur de chaque segment successif en utilisant la variable d'itération `i`, nous obtenons une spirale.

```{codeplay}
:file: range8.py
from turtle import *

for i in range(100):
    write(i)
    forward(i)
    left(30)
```

## Deux boucles imbriquées

Dans Excel, les cellules sont désignées avec une lettre et un nombre.
Pour recréer les noms de cellule nous parcourons une chaîne de chiffres et une deuxième fois dans une chaîne de lettres.

On appelle la première boucle avec `y` la **boucle extérieure** et la deuxième boucle avec `x` **la boucle intérieure**.

Nous concaténons les deux éléments lettre et nombre (`x + y`) et nous ajoutons l'option `end=' '` pour remplacer le retour à la ligne par un espace.

Pour bien montrer l'ordre consécutif, nous importons la fonction `sleep()` du module `time` pour ralentir le parcours de la boucle.

```{exercise}
Transformez le code pour afficher 20 colonnes de cellules.
```

```{codeplay}
:file: range9.py
from time import sleep

for y in '1234567':
    for x in 'ABCDEFG':
        print(x + y, end=' ')
        sleep(0.1)
    print()
```

## Itérer sur x et y

Deux boucles imbriquées peuvent itérer dans les directions x et y. Ceci permet d'afficher les coordonnées de la tortue.

```{codeplay}
:file: range10.py
from turtle import *
up()

for y in range(100, -150, -50):
    for x in range(-200, 300, 100):
        goto(x, y)
        dot(45, 'silver')
        write((x, y), align='center')
```

## Grille de points

Le programme suivant dessine des points sur une grille régulière avec une distance `d` entre les points. Nous utilisons deux boucles imbriquées avec les variables d'itération `x` et `y`.

```{codeplay}
from turtle import *
up()

def grille(p, size, dim):
    for i in range(dim[0]):         # itérer les lignes i
        for j in range(dim[1]):     # itérer les colonnes j
            x = p[0] + j*size[0]    # calculer x
            y = p[1] + i*size[1]    # calculer y
            goto(x, y)
            dot()

grille((-200, -100), (20, 20), (8, 8))
grille((100, 0), (10, 10), (5, 7))
```

## Grille de lignes

Le programme suivant dessine une grille de lignes qui sont à une distance `d` les unes des autres. Nous utilisons deux boucles séparées avec les variables d'itération `x` et `y`.

```{codeplay}
from turtle import *
up()

x0 = 180
d = 40

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

for y in range(-x0, x0+1, d):
    ligne((-x0, y), (x0, y))

for x in range(-x0, x0+1, d):
    ligne((x, -x0), (x, x0))
```

## Grille de Sudoku

Le programme suivant dessine une grille de Sudoku 3x3 avec une distance `d` entre les lignes. La particularité de la grille Sudoku est que chaque 3e ligne est accentuée. Nous utilisons la condition modulo `i%3` pour ceci.

```{codeplay}
from turtle import *
up()

x0 = 180
d = 40

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

for y in range(-x0, x0+1, d):
    width(3 if y%3 == 0 else 1)
    ligne((-x0, y), (x0, y))

for x in range(-x0, x0+1, d):
    width(3 if x%3 == 0 else 1)
    ligne((x, -x0), (x, x0))
```

## Grille de tic-tac-toe

La grille du jeu tic-tac-toe est une grille 3x3. Nous ajoutons des étiquettes a-c pour les colonnes et 1-3 pour les lignes.

```{codeplay}
from turtle import *
up()

speed(10)
x0 = 150
d = 100

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

for y in range(-x0, x0+1, d):
    ligne((-x0, y), (x0, y))

for x in range(-x0, x0+1, d):
    ligne((x, -x0), (x, x0))

goto(-x0 + d/2, x0+10)
for c in 'abc':
    write(c, font=('Arial', 24))
    forward(d)
    
goto(-x0-10, x0 - d/2 - 12)
seth(-90)
for c in '123':
    write(c, font=('Arial', 24), align='right')
    forward(d)
```

## Jouer au tic-tac-toe

Pour jouer au tic-tac-toe, nous devons déchiffrer les noms des cellules qui sont constituées d'une lettre (a-c) et d'un chiffre (1-3). En alternance nous plaçons une croix et un cercle.

```{codeplay}
:output_lines: 5
from turtle import *
up()

speed(10)
x0 = 150
d = 100

def ligne(p, q):
    goto(p)
    down()
    goto(q)
    up()

for y in range(-x0, x0+1, d):
    ligne((-x0, y), (x0, y))

for x in range(-x0, x0+1, d):
    ligne((x, -x0), (x, x0))

goto(-x0 + d/2, x0+10)
for c in 'abc':
    write(c, font=('Arial', 24))
    forward(d)
    
goto(-x0-10, x0 - d/2 - 12)
seth(-90)
for c in '123':
    write(c, font=('Arial', 24), align='right')
    forward(d)

hideturtle()
for i in range(9):
    p = input('Entrez coordonné: ')
    x = -x0 + (ord(p[0]) - ord('a') + 0.5) * d
    y =  x0 - (int(p[1]) - 0.1) * d
    goto(x, y)
    write('×○'[i%2], font=('Arial', d), align='center')
```

## Plateau d'échec

Le plateau d'échec est constitué de 64 carrés qui sont alternativement noirs ou blancs.

```{codeplay}
from turtle import *

speed(0)
x0 = 160
d = 40
up()

def case():
    begin_fill()
    down()
    for i in range(4):
        forward(d)
        left(90)
    up()
    end_fill()

for i in range(8):
    for j in range(8):
        goto(-x0 + j*d, -x0 + i*d)
        fillcolor('white' if (i+j)%2 else 'black')
        case()
```

## Exercices

- Téléchargez un exercice.
- Éditez-le dans un éditeur.
- Déposez-le sur Moodle.

### Cadran

Dessinez le cadran d'une montre avec 60 petits points pour les minutes et secondes et 12 grands points pour les heures. Utilisez la fonction modulo `i%5` pour faire la différence entre les petits et les grands points.

```{codeplay}
:file: cadran.py
from turtle import *
# Prénom, nom, classe

for i in range(60):
    ...
```

### Plateau d'échec

Dessinez un échiquier, numérotez les lignes 1-8 et les colonnes a-h, et placez les pions noirs et blancs aux positions de départ.

```{codeplay}
from turtle import *

speed(0)
x0 = 160
d = 40
up()

blancs = '♖♘♗♔♕♗♘♖'

goto(-x0, -x0)
for c in blancs:
    write(c, font=(None, d))
    forward(d)
```

### Logo de l'EPFL

En mars 2019, l’[EPFL](https://www.epfl.ch/fr/) profite de son anniversaire de 50 ans pour renouveler son logo. Tout en maintenant la couleur du drapeau helvétique, l’agence [Moser Design](https://moserdesign.ch) utilise une police de caractères suisse, l’Helvetica Neue. Les lettres ont été remaniées à la manière de pixels pour laisser transparaître la dimension numérique de l’école. On peut percevoir dans le négatif des lettres E et F deux croix helvétiques.

```{codeplay}
from turtle import *
shape('arrow')

def pixel():
    color('white')
    begin_fill()
    down()
    for x in (21, 16) * 2:
        forward(x)
        left(90)
    up()
    end_fill()

up()
color('red')
speed(2)
goto(-200, -50)

for c in 'EPFL':
    write(c, font=('Helvetica Neue', 100, 'bold'), move=True)
    
goto(-191, -9)
pixel()
goto(-17, -9)
pixel()
hideturtle()
```

Selon le même schéma, créez un logo pour une autre institution. Justifiez le choix de la couleur.
