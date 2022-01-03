# Répéter

Nous avons vu qu'un programme exécute souvent des instructions similaires multiples fois. Dans ce cas une boucle permet de mieux structurer le code et le rendre beaucoup plus court.
Une boucle ne représente pas seulement une économie de code, mais donne aussi beaucoup de flexibilté. En Python nous avons deux types de boucle :

- la boucle `for` pour parcourir un ensemble de valeurs
- la boucle `while` pour répéter pendant qu'une condition est vrai

Le programme suivant demande comme entrée le nombre de sommets, et dessine alors un polygon avec n sommets.

```{codeplay}
from turtle import *

n = input('Nombre de sommets: ')
n = int(n)

for i in range(n):
    forward(50)
    left(360/n)
```

## Itérer

Le mot **itérer** veut dire parcourir un ensemble un par un. Dans la boucle `for` une variable d'itération va parcourir un ensemble qui peut être : 

- une plage numérique avec `range()``
- une chaîne numérique
- une liste

La **varible d'itération** prend succéssivement les valeurs 0, 1, ... n-1.
Cette fois nous affichons cette variable dans chaque sommet. 

La valeur de `i` est affichée dans chaque sommet du polygone.

```{codeplay}
from turtle import *

n = input('Nombre de sommets: ')
n = int(n)

for i in range(n):
    forward(50)
    left(360/n)
    write(i, font=(None, 24))
```

## Dessiner une spirale

Si nous dessinons un polygone mais augmentons la longeur de chaque segment succéssif, nous obtenons une spirale.

```{codeplay}
from turtle import *

for i in range(100):
    forward(i * 2)
    left(60)
```

**Exercice** : Modifie le code pour que l'image ressemble plus à une vraie spirale.

## Goto

La fonction `goto(x, y)` permet d'aller directement vers la position `(x, y)`,
sans changer l'orientation de la tortue.

```{codeplay}
from turtle import *

goto(40, 0)
goto(40, 40)
goto(60, 40)
goto(60, 0)
goto(100, 0)
goto(100, 60)
goto(50, 110)
goto(0, 60)
goto(0, 0)
```

## Polygone

Un polygone régulier est une forme ou toutes les côtes ont la même longueur est toute les angles sont identiques.

```{codeplay}
from turtle import *

def polygon(n, a):
    for i in range(n):
        forward(a)
        dot(8)
        left(360/n)
        
polygon(3, 100)
polygon(4, 100)
polygon(5, 100)
polygon(6, 100)
```

Pour dessiner des formes qui ne sont pas connecté par une ligne, nous utilisons les deux fonctions:

- `up()` pour lever le stylo
- `down()` pour baisser le stylo

```{codeplay}
from turtle import *

def polygon(n, a):
    for i in range(n):
        forward(a)
        dot(8)
        left(360/n)

up()
back(200)

for i in range(3, 7):
    down()
    polygon(i, 60)
    up()
    forward(120)
```

##  Cercle

Plus que le polygone régulier a de sommets, plus il ressemble à un cercle.
Avec 36 sommets, il ressemble déjà raisonablement à un cercle.

```{codeplay}
from turtle import *

def polygon(n, a):
    for i in range(n):
        forward(a)
        left(360/n)

polygon(36, 10)
```

**Exercice** : Modifie le code pour que l'image ressemble plus à une vraie spirale.

## La fonction `circle(r)`

La fonction `circle(r)` dessine un cercle de rayon `r`.
Le cercle est dessiné :

- vers la gauche si r est positif,
- vers la droite si r est négatif.

```{codeplay}
from turtle import *

forward(50)
circle(40)
forward(100)
circle(-30)
forward(100)
```

Cette fonction peut avoir un deuxième paramètre sous la forme `circle(r, angle)` 
ou `angle` représente l'angle du cercle dessiné.
Par défaut c'est 360°, donc un cercle entier.

Voici un exemple qui utilise deux demi-cercles de 180°.

```{codeplay}
from turtle import *

forward(100)
circle(40, 180)
forward(50)
circle(-30)
forward(50)
circle(40, 180)
```

## Dessiner un coeur

Nous pouvons combiner deux segments de cercle et deux segments droits pour dessiner un coeur.

```{codeplay}
from turtle import *
r = 40
fillcolor('red')

begin_fill()
forward(2 * r)
circle(r, 180)
right(90)
circle(r, 180)
forward(2 * r)
end_fill()
```

## Dessiner une fleur

Dessinons des cercle dans une boucle, et tournons à chaque fois.

```{codeplay}
from turtle import *

n = 6
for i in range(n):
    circle(50)
    left(360/n)
```

Il est également possible de faire varier le rayon dans une boucle `for` avec une expression `range()`.

```{codeplay}
from turtle import *

for r in range(20, 100, 20):
    circle(r)
```

## Deux boucles imbriquées

Dans Excel, les cellules sont nommés avec une lettre et un nombre. 
Pour recréer les noms de cellule nous itérons dans une chaine de chiffres et une deuxième fois dans une chaîne des lettres de l'alphabet.

Nous concatenons les deux éléments lettre et nombre (`x + y`) et nous ajoutons l'option `end=' '` pour remplacer le retour à la ligne par une espace.

```{codeplay}
for y in '1234567':
    for x in 'ABCDEFG':
        print(x + y, end=' ')
    print()
```

**Exercice** : Transformez le code pour afficher 20 colonnes de cellules.

## La boucle `while`

La boucle `while` exécute un bloc tant qu'une condition est vraie.

On peut l'utiliser pour créer un compteur à rebours.
Pour attendre une seconde la fonction `sleep()` du module `time` est importée.

```{codeplay}
from time import sleep

n = int(input('Entrez un entier: '))
while n > 0:
    print(n)
    sleep(1)
    n = n - 1

print('boum!!!')
```

## Lister des noms

Nous utilisons une boucle `while` pour demander des noms à l'utilsateur. 
On ne peut pas savoir à l'avance combien de noms il y aura. Nous prenons comme condition de terminaison de boucle le fait de répondre avec une chaine vide (`''`).

```{codeplay}
noms = []
nom = input('Entrez un nom: ')

while nom != '':
    noms.append(nom)
    nom = input('Entrez un nom: ')
    
print(noms)
```

## Calculer une somme

Nous utilisons une boucle `while` pour demander des nombres à l'utilsateur. 
On ne peut pas savoir à l'avance combien de nombres il y aura. Nous prenons comme condition de terminaison de boucle le fait de répondre avec une chaine vide (`''`).

Au lieu d'écrire `while x != '':` nous pouvons simplifier vers  `while x:`. 
La raison est que la chaine vide est associé à `False` et toute autre chaine non-vide est associé à `True`. 

```{codeplay}
somme = 0
x = input('Entrez un nombre: ')

while x:
    somme += float(x)
    x = input('Entrez un nombre: ')
    
print('somme =', somme)
```

## Calculer une moyenne

Nous utilisons une boucle `while` pour demander des nombres à l'utilsateur. 
On ne peut pas savoir à l'avance combien de nombres il y aura. Nous prenons comme condition de terminaison de boucle le fait de répondre avec une chaine vide (`''`).

```{codeplay}
somme = 0
n = 0
x = input('Entrez un nombre: ')

while x:
    somme += float(x)
    n += 1
    x = input('Entrez un nombre: ')
    
print('moyenne =', somme/n)
```