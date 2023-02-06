# Associer - `dict`

Un **dictionnaire** est une structure de données qui, comme une liste, contient plusieurs éléments, mais qui est plus puissante. Dans une liste les indices sont des entiers. Dans un dictionnaire les indices peuvent être de n'importe quel type immuable (entier, nombre, texte). Nous allons voir que :

- un dictionnaire est composé de paires `clé:valeur`,
- l'expression `dico[clé]` renvoie la valeur associée à la clé,
- la méthode `dico.get(clé, défaut)` renvoie la valeur ou son défaut.

```{question}
L'expression `dict([(1, 2)])` est un dictionnaire

{f}`dont une clé est 2`  
{f}`dont une valeur est 1`  
{v}`avec une entrée`  
{f}`avec deux entrées`
```

## Un dictionnaire de mots

Un dictionnaire classique associe un mot d'une langue au mot correspondant d'une autre langue.
Nous pouvons utiliser la structure du dictionnaire en Python de cette façon et l'utiliser pour associer des mots en français à des mots d'une autre langue.

De façon générale, un dictionnaire associe une série de **clés** à une autre série de **valeurs**.
Toutes les clés d'un dictionnaire sont uniques.

```{codeplay}
:file: dict1.py
anglais = {'maison':'house', 'voiture':'car', 'ordinateur':'computer'}

print('dictionnaire =', anglais)
print(anglais['maison'])
```

Nous pouvons très bien définir un deuxième dictionnaire.

```{codeplay}
:file: dict2.py
anglais = {'maison':'house', 'voiture':'car', 'ordinateur':'computer'}
allemand = {'maison':'House', 'voiture':'Auto', 'ordinateur':'Rechner'}

print('anglais =', anglais)
print('allemand =', allemand)
print()

mot = 'voiture'
print(mot, 'en anglais est', anglais[mot])
print(mot, 'en allemand est', allemand[mot])
```

## Traduire une phrase

À l'aide d'un dictionnaire, nous pouvons traduire maintenant toute une phrase.
Pour pouvoir accéder à chaque mot d'une phrase, nous allons découper la phrase en mots en utilisant la méthode `split()`.
Nous obtenons alors une liste qui contient les mots de la phrase.

```{codeplay}
:file: dict3.py
phrase = 'la maison est grande'
print('phrase =', phrase)
print('liste =', phrase.split())
```

À l'aide d'une boucle `for` nous pouvons traduire la phrase entière.

```{exercise}
Avec les mots donnés dans le dictionnaire, faites une nouvelle phrase.
```

```{codeplay}
:file: dict4.py
anglais = {'la':'the', 'maison':'house', 'est':'is', 'rouge':'red', 
           'et':'and', 'grande':'big', 'voiture':'car', 'rapide':'fast', 
           'très':'very', 'sympa':'nice'}

phrase = 'la maison est rouge et grande'
print(phrase)

for mot in phrase.split():
    print(anglais[mot], end=' ')
```

## Traduire un texte

Un texte est constitué de plusieurs lignes. Pour découper un texte multiligne en lignes,
nous utilisons de nouveau la méthode `split('\')`, mais cette fois avec un séparateur (newline).

```{codeplay}
:file: dict5.py
texte = """la maison est grande
la voiture est rapide
la voiture et la maison est très sympa"""

print(texte.split('\n'))
```

Nous pouvons maintenant traduire un texte de plusieurs lignes.

```{codeplay}
:file: dict6.py
anglais = {'la':'the', 'maison':'house', 'est':'is', 'rouge':'red', 
           'et':'and', 'grande':'big', 'voiture':'car', 'rapide':'fast', 
           'très':'very', 'sympa':'nice'}

texte = """
la maison est grande
la voiture est rapide
la voiture et la maison est très sympa"""

print(texte)

for phrase in texte.split('\n'):
    for mot in phrase.split():
        print(anglais[mot], end=' ')
    print()
```

## Traduire en code Morse

Le code Morse est composé de points et de traits. Il associe à chaque lettre de l'alphabet un code.

```{image} media/Morse.jpg
:width: 400px
```

Un autre exemple pour un dictionnaire est la table du code Morse.

```{codeplay}
:file: dict7.py
Morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'.--', 'e':'.', 'f':'..-.', 
         'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 
         'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 
         's':'...', 't':'-', 'u':'..-', 'v':'....-', 'w':'.--', 'x':'-..-', 
         'y':'-.--', 'z':'--..'}
         
print(Morse)
print(len(Morse))
print()

for c in 'python':
    print(c, '=', Morse[c])
```

Maintenant nous pouvons traduire une phrase entière. Ici nous devons faire attention aux espaces :

- les caractères sont séparés par 2 espaces,
- les mots sont séparés par 4 espaces.

```{exercise}
Écrivez votre nom en Morse.
```

```{codeplay}
:file: dict8.py
Morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'.--', 'e':'.', 'f':'..-.', 
         'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 
         'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 
         's':'...', 't':'-', 'u':'..-', 'v':'....-', 'w':'.--', 'x':'-..-', 
         'y':'-.--', 'z':'--..'}
===      
phrase = 'le morse est beau'
print(phrase)

for c in phrase:
    if c == ' ':
        print(end='  ')
    else:
        print(Morse[c], end='  ')
```

## Système de login

L'exemple suivant simule le processus de login à un système informatique.
Dans le dictionnaire `passwords` nous gardons les informations de connexion sous forme de paires `user:password`.

L'opérateur spécial `in` permet de tester si une clé donnée fait partie du dictionnaire.

Dans un premier temps on vérifie que l'utilisateur existe avec `user in passwords`.
Dans un deuxième temps on vérifie si c'est le bon mot de passe avec `pw == passwords[user]`.

```{exercise}
Essayez avec utilisateur `mar`, `mark` et les mots de passe `123`, `1234`.
```

```{codeplay}
:file: dict9.py
passwords = {'mark':'1234', 'steve':'abQF$12', 'sarah':'01[+]a.'}

while True:
    user = input('login: ')
    if user in passwords:
        pw = input('mot de passe: ')
        if pw == passwords[user]:
            print('vous êtes connecté au système')
            break
        else:
            print('mot de passe incorrecte')
    else:
        print(user, "n'est pas un utilisateur reconnu")
```

## Un dictionnaire de couleurs

Un spécialiste de la publication, de la mode, ou du web, utilise une centaine des mots spécifiques pour désigner un ton de couleur particulier. Ces couleurs peuvent être spécifiées avec les 3 couleurs de base : rouge, vert, bleu (RVB).

Nous pouvons utiliser un dictionnaire `RVB` pour associer des noms de couleurs à des triplets de nombres qui indiquent les 3 composantes RVB.

```{exercise}
Ajoutez 2-3 couleurs du domaine de la mode.
```

```{codeplay}
:file: dict10.py
from turtle import *
up()

RVB = {'rouge':(1, 0, 0), 'vert':(0, 1, 0), 'bleu':(0, 0, 1),
      'jaune':(1, 1, 0), 'cyan':(0, 1, 1), 'magenta':(1, 0, 1),
      'orange':(1, 0.5, 0)}

couleurs = 'rouge', 'orange', 'jaune', 'vert', 'magenta', 'bleu'

d = 50
backward(200)
for x in couleurs:
    dot(d, RVB[x])
    forward(d)
```

## Compter des lettres

Avec un dictionnaire nous pouvons facilement compter les lettres dans un texte.
Compter le nombre d'occurrences de quelque chose est appelé faire un histogramme.

Notre dictionnaire s'appelle `histogram` et au début il est vide.
Les clés de l’histogramme sont des caractères que nous désignons par `c`.

Si le caractère `c` fait déjà partie de l’histogramme, alors on ajoute 1 au compte, sinon on met le compte à 1.

```{codeplay}
:file: dict11.py
phrase = 'hello world'
histogram = {}

for c in phrase:
    if c in histogram:
        histogram[c] += 1
    else:
        histogram[c] = 1
        
print(histogram)
```

Nous constatons que la lettre `l` apparait 3 fois.

## Faire un histogramme

Nous pouvons maintenant établir un histogramme sur un texte de plus grande taille.

```{codeplay}
:file: dict12.py
texte = """Le monde numérique est extrêmement vaste. 
Au moyen d’applications dédiées, il est possible d’y travailler sur 
une certaine représentation du réel. Des textes, des images, 
des sons ou des données financières peuvent y être manipulés.
Pourtant, il faut avoir conscience qu’aussi «réelles» que ces 
représentations puissent paraître, elles n’en sont pas moins des 
représentations.
Dans cette section, nous allons comprendre comment les ordinateurs 
parviennent à représenter le monde et les compromis qui doivent être 
faits pour simplifier le réel jusqu’à ce que sa représentation puisse 
être manipulée automatiquement au moyen de calculs élémentaires."""

print(len(texte))
histogram = {}

for c in texte:
    c = c.lower()
    if c in histogram:
        histogram[c] += 1
    else:
        histogram[c] = 1
        
print(histogram)
```

## Visualiser un histogramme

Pour visualiser cet histogramme, nous allons dessiner un diagramme de barres.

```{codeplay}
:file: dict13.py
texte = """
Le monde numérique est extrêmement vaste. 
Au moyen d’applications dédiées, il est possible d’y travailler sur 
une certaine représentation du réel. Des textes, des images, 
des sons ou des données financières peuvent y être manipulés.
Pourtant, il faut avoir conscience qu’aussi «réelles» que ces 
représentations puissent paraître, elles n’en sont pas moins des 
représentations.
Dans cette section, nous allons comprendre comment les ordinateurs 
parviennent à représenter le monde et les compromis qui doivent être 
faits pour simplifier le réel jusqu’à ce que sa représentation puisse 
être manipulée automatiquement au moyen de calculs élémentaires."""

histogram = {}

for c in texte:
    if c.isalpha():
        c = c.lower()
        if c in histogram:
            histogram[c] += 1
        else:
            histogram[c] = 1
        
===
from turtle import *
up()
width(5)
color('blue')
left(90)

goto(-280, 0)

for c in histogram:
    write(c, font=(None, 12), align='center')
    d = histogram[c]
    forward(20)
    down()
    forward(d)
    up()
    forward(10)
    write(d, font=(None, 12), align='center')
    backward(d + 30)
    setx(xcor() + 25)
```

## La fonction `get()`

Adresser une clé qui n'existe pas dans un dictionnaire produit une erreur de type `KeyError`.

```{codeplay}
:file: dict14.py
anglais = {'maison':'house'}
print(anglais['voiture'])       # KeyError: 'voiture'
```

La méthode `get(clé, val_défaut)` permet d'obtenir une valeur par défaut et d'éviter une erreur si la clé n'existe pas encore dans le dictionnaire.

```{codeplay}
:file: dict15.py
anglais = {'maison':'house'}
print('maison =', anglais.get('maison', 'not defined'))
print('voiture =', anglais.get('voiture', 'not defined'))
```

Ceci nous permet de compacter encore davantage le programme de l'histogramme.

```{codeplay}
:file: dict16.py
phrase = 'hello world'

histogram = {}
for c in phrase:
    histogram[c] = histogram.get(c, 0) + 1

print(histogram)
```

## Color typewriter

Ce programme interactif permet d'écrire une image ligne par ligne en utilisant les 26 touches du clavier, comme une machine à écrire (typewriter).

Nous utilisons ici un dictionnaire pour associer une lettre à une couleur.

```{codeplay}
from turtle import *
from random import *
s = getscreen()
speed(0)
d = 60
goto(-300+d/2, 200-d/2)

couleurs = dict()
couleurs['a'] = 'aqua'
couleurs['b'] = 'blue'
couleurs['c'] = 'chocolate'
couleurs['d'] = 'dodgerblue'
couleurs['f'] = 'fuchsia'
couleurs['g'] = 'green'
couleurs['k'] = 'black'
couleurs['l'] = 'lime'
couleurs['i'] = 'indigo'
couleurs['m'] = 'mistyrose'
couleurs['n'] = 'navy'
couleurs['o'] = 'orange'
couleurs['p'] = 'pink'
couleurs['r'] = 'red'
couleurs['s'] = 'silver'
couleurs['t'] = 'tan'
couleurs['v'] = 'violet'
couleurs['w'] = 'white'
couleurs['y'] = 'yellow'

def f(x):
    col = couleurs.get(x, 'lightgray')
    dot(d, col)
    write(col, align='center')
    if xcor() < 300 - d/2:
        forward(d)
    else:
        goto(-300+d/2, ycor()-d)

for c in 'abcdefghijklmnopqrstuvwxyz':
    s.onkey(lambda x=c: f(x), c)
    
s.listen()
```
