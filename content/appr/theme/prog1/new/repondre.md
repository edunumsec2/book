# Répondre - `input`

Dans ce chapitre nous introduisons une façon pour que le programme puisse poser des questions. L'utilisateur du programme peut alors répondre et entrer une information. La réponse sera mémorisé dans une variable. Nous allons apprendre que

- la fonction `print()` affiche un texte,
- la fonction `input('question')` demande une information,
- une variable `x` mémorise une information.

## Dire bonjour

Nous commençons par le grand classique des livres d'introduction à la programmation : afficher la fameuse phrase *hello world.*.
La fonction `print()` permet d'écrire du texte vers la console.
Ici, la console est la région de texte qui suit le programme interactive.

```{codeplay}
print('hello world.')
```

**Exercice** : Affichez encore 2-3 lignes de texte en plus avec la fonction `print()`.

## Ecrire et dessiner

Votre programme peut faire les deux choses dans un même programme: dessiner une image et écrire un texte.
Le texte apparait dans la console qui apparait directement après le programme.
Le dessin apparait dans une fenêtre spéciale après la console.

```{codeplay}
from turtle import *

print('ce programme dessine un carré')

for i in range(4):
    forward(100)
    left(90)
```

**Exercice** : Ajoutez en plus du code pour dessiner un triangle, et annoncez-le dans le texte.

## La fonction `input()`

La fonction `input('question')` permet de demander une entrée (input) à l'utilisateur.
L'utilisateur voit le texte `question` affiché à la console et doit répondre à cette question. Il termine son entrée avec la touche Enter.

La réponse de l'utilisateur est ensuite mémorisée dans une variable que nous appelons `x` dans cet exemple.
Ensuite nous pouvons utiliser cette variable `x` dans la suite du programme, par exemple dans une expression `print()`.

```{codeplay}
x = input('Entrez votre nom: ')
print('Bonjour', x)
```

## Les variables

Une variable est une place en mémoire pour stocker de l'information.
Vous êtes complètement libre dans le choix des noms pour les variables, mais c'est recommandé de choisir des noms qui sont le plus explicite possible. C'est mieux d'utiliser des noms de variable parlants, comme `'nom'` et `'age'`,  bien qu'on aurait pu utiliser `'x'` et `'y'`.  

```{codeplay}
nom = input('Entrez votre nom: ')
print('Bonjour', nom)

age = input('Entrez votre age: ')
print('Trés bien', nom, 'vous avez', age, 'ans')
```

**Exercice** : Ajoutez une 3e question.

## Convention

Normalement c'est conseillé d'utiliser des variables très explicite, comme `age`, `prenom`, `nom`, `longuer`, `hauteur`, etc.

Mais dans des boucles et dans un contexte local, nous adoptons la convention suivante d'utiliser des variables courte d'une seule lettre.

- `a` pour une longueur ou distance
- `c` pour un caractère dans une boucle
- `d` pour un diamètre
- `i` pour un entier dans une boucle
- `j` pour un deuxième entier
- `n` pour un nombre donné
- `r` pour un rayon
- `x` pour une coordonnée en direction x
- `y` pour une coordonnée en direction y

```{question}
La variable `i` désigne normalement

{f}`une longeur`  
{f}`un caractère`  
{v}`un entier`  
{f}`une coordonné`
```

## Demander une couleur

Nous pouvons utiliser une entrée interactive avec la fonction `input()`
et demander à l'utilisateur d'entrer une couleur valide pour l'arrière-fond.

```{codeplay}
from turtle import *

x = input('Entrez une couleur: ')
getscreen().bgcolor(x)
```

**Exercice** : Entrez différentes couleurs valides.

Nous pouvons continuer les questions avec une couleur de ligne et une couleur de remplissage, pour dessiner un rectangle.

```{codeplay}
from turtle import *

x = input('Entrez une couleur de arrière-fond: ')
getscreen().bgcolor(x)

y = input('Entrez une couleur de ligne: ')
pencolor(y)

z = input('Entrez une couleur de remplissage: ')
fillcolor(z)

width(10)
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()
```

**Exercice** : Ajoutez une 4e question pour demander la couleur des points (dot) et ajoutez un point colorié dans chaque sommet.

## Demander en boucle

La boucle `while` permet de répéter les instructions qui se trouvent dans son bloc en indentation.
Dans la dernière ligne du bloc en indentation nous reposons la question.

Cette boucle répète aussi longtemps que la variable `x` contient une valeur, c'est à dire qu'elle n'est pas vide.
Si vous appuyez sur **Enter** sans entrer quelque chose, la boucle s'arrête.

```{codeplay}
from turtle import *
up()

back(200)
x = input('Entrez une couleur: ')
while x:
    dot(80, x)
    forward(80)
    x = input('Entrez une couleur: ')
```

## Erreurs

Il est important de bien comprendre les messages d'erreurs.
Dans cette section vous allez découvrir les différentes catégories d'erreur et comment les corriger.

### SyntaxError

Cette erreur est produite quand vous utilisez des accents dans des noms de fonctions ou de variables.

```{codeplay}
from turtle import *

def carré():
    for à in range(4):
        forward(100)
        left(90)
        
carré()
```

**Exercice** : Corrigez les 3 erreurs de syntaxe'.

### SyntaxError: EOF

Cette erreur est produite quand vous oubliez de fermer une parenthèse.

```{codeplay}
from turtle import *

forward(100)  
left(90)
forward(100
```

**Exercice** : Corrigez l'erreur de syntaxe'.

### ValueErreor

Cette erreur est produite quand la valeur numérique est trop grande pour correspondre à un Unicode.

```{codeplay}
print(chr(10000000))
```

**Exercice** : Corrigez l'erreur de valeur'.
