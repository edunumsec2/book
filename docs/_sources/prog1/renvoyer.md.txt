(prog1.renvoyer)=
# Renvoyer - `return`

Dans ce chapitre, nous allons voir comment une fonction peut renvoyer une valeur. Ceci est très important pour pouvoir utiliser une fonction dans une expression mathématique. Nous allons voir que :

- le mot-clé `return` permet de renvoyer une valeur,
- la fonction qui ne renvoie rien renvoie `None`,
- l'expression `return x, y` renvoie un tuple.

```{question}
En informatique, le mot-clé `return` est utilisé pour

{f}`changer de direction`  
{v}`renvoyer une valeur`  
{f}`répéter encore une fois`  
{f}`rentrer au début`
```

## Valeur de retour

L'instruction `return` permet de retourner une valeur.
Le grand intérêt d'une valeur de retour est qu'on peut l'utiliser de nouveau dans des expressions.

Par exemple, nous pouvons créer une expression comme celle-ci : `square(x) + cube(x)`

```{codeplay}
:file: return1.py
def carre(x):
    return x ** 2

def cube(x):
    return x ** 3

x = input('Entrez un nombre: ')
x = int(x)
print('carré =', carre(x))
print('cube =', cube(x))
print('carré + cube =', carre(x) + cube(x))
```

## Points de sortie

Une fonction peut avoir plusieurs points de sortie. En fait quand une ligne avec `return` est exécutée, toutes les lignes qui suivent ne sont plus exécutées.

La fonction `signe()` possède 3 points de sortie.

```{codeplay}
:file: return2.py
def signe(x):
    if x > 0:
        return 'positif'
    elif x < 0:
        return 'négatif'
    else:
        return 'zéro'

x = int(input('Entrez un nombre: '))
print(x, 'est', signe(x))
```

**Exercice** : Testez avec -2, 0 et 3.

## État de la tortue

Plusieurs fonctions nous renseignent sur l'état de la tortue :

- couleur
- tortue
- position
- fenêtre

```{codeplay}
:file: return3.py
from turtle import *

color('red', 'lime')
forward(100)
left(90)
forward(50)

print('Couleur:')
print('color =', color())
print('pen =', pencolor())
print('fill =', fillcolor())
print('mode =', colormode())

print('\nPosition:')
print('h =', heading())
print('x =', xcor())
print('y =', ycor())
print('pos =', pos())

print('\nFenêtre:')
print('h =', window_height())
print('w =', window_width())
```

## Renvoyer une couleur

Avec un argument, ces fonctions permettent de définir une couleur de la tortue et renvoient la valeur `None`.

- `color(c)`
- `fillcolor(c)`
- `pencolor(c)`

Sans un argument ces fonctions renvoient la couleur actuelle.

```{codeplay}
:file: return4.py
from turtle import *

width(10)
print('color =', color('red', 'blue'), color())
forward(100)
print('pencolor =', pencolor('lime'), pencolor())
print('fillcolor =', fillcolor('pink'), fillcolor())
forward(100)
```

## Renvoyer la position

Ces fonctions permettent de contrôler la position de la tortue et renvoient `None`.

- `setx(x)`
- `setx(y)`
- `setpos(x, y)`

Ces fonctions permettent de lire la position actuelle de la tortue et renvoient une valeur numérique.

- `xcor()`
- `ycor()`
- `pos()`

Les fonctions `seth(a)` et `geth()` permettent de définir ou renvoyer l'orientation actuelle (heading) de la tortue.

```{codeplay}
:file: return5.py
from turtle import *

width(5)
print('x =', setx(100), xcor())
print('y =', sety(50), ycor())
print('pos =', setpos(0, 100), pos())
print('h =', seth(90), heading())
```

## Fonctions natives

Voici quelques fonctions natives, c'est-à-dire des fonctions standards qui font partie de Python.

Les fonctions suivantes renvoient un nombre sous forme binaire, octale ou hexadécimale.

```{codeplay}
:file: ret6.py
n = 123
print(n)
print('bin =', bin(n))
print('oct =', oct(n))
print('hex =', hex(n))
```

Ces fonctions renvoient la valeur absolue, la puissance et la valeur arrondie.

```{codeplay}
:file: return7.py
n = -3.1415
print(n)
print('abs =', abs(n))
print('pow =', pow(n, 3))
print('round =', round(n, 2))
```

Ces fonctions renvoient le minimum, le maximum et la somme d'une séquence de nombres.

```{codeplay}
:file: return8.py
seq = (1, 3, 99, 9)
print(seq)
print('max =', max(seq))
print('min =', min(seq))
print('sum =', sum(seq))
```

Ces fonctions renvoient la longueur d'une chaine, l'entier du code Unicode, et le symbole Unicode associé à un entier.

```{codeplay}
:file: return9.py
print(len('hello'))
print(ord('😀'))
print(chr(128522))
```
