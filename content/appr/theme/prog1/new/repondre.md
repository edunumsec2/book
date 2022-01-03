# Répondre - `input`

Dans ce chapitre nous introduisons une façon pour que le programme puisse poser des questions. L'utilisateurs du programme peut alors répondre et entrer une information. La réponse sera mémorisé dans une variable.

- la fonction `print()` affiche un texte
- la fonction `input('question')` demande une information
- une variable `x` mémorise une information.

## Dire bonjour

Nous commençons par le grand classique des livres d'introduction à la programmation.
La fonction `print()` permet d'écrire du texte vers la console.
Ici, la console est la région de texte qui suit le programme interactive.

```{codeplay}
print('hello world.')
```

**Exercice** : Affichez encore 2-3 lignes de texte avec la fonction `print()`.

## Ecrire et dessiner

Votre programme peut faire les deux choses dans un même programme: dessiner une image et écrire un texte.
Le texte apparaitra dans la console qui apparait directement après le programme.
Le dessin apparait dans une fenêtre spéciale après la console.

```{codeplay}
from turtle import *

print('ce programme dessine un carré')

for i in range(4):
    forward(100)
    left(90)
```

**Exercice** : Ajoutez encore le code pour dessiner un triangle, et annoncez-le dans le texte.

## La fonction `input()`

La fonction `input('question')` permet de demander une entrée (input) à l'utilisateur.
L'utilisateur voit `question` affiché à la console et doit répondre à cette question. Il termine son entrée avec la touche Enter.

La réponse de l'utilisateur est ensuite mémorisée dans une variable que nous appelons `x` dans cet exemple. 
Ensuite nous pouvons utiliser cette variable `x` dans la suite du programme, par exemple dans une expression `print()`.

```{codeplay}
x = input('Entrez votre nom: ')
print('Bonjour', x)
```

## Les variables

Une variable est une place en mémoire pour stocker de l'information.
Vous êtes complètement libre dans le choix des noms pour les variables, mais c'est recommandé de choisir des noms qui sont le plus explicite possible. C'est mieux d'utiliser des variables parlant, comme `'nom'` et `'age'`,  bien qu'on aurait pu utiliser `'x'` et `'y'`.  

```{codeplay}
nom = input('Entrez votre nom: ')
print('Bonjour', nom)

age = input('Entrez votre age: ')
print('Trés bien', nom, 'vous avez', age, 'ans')
```

**Exercice** : Ajoutez une 3e question.


## Demander une couleur

Nous pouvons utiliser une entrée interactive avec la fonction `input()`
et demander à l'utilisateur d'entrer une couleur valide pour l'arrière-fond.

```{codeplay}
from turtle import *

x = input('Entrez une couleur: ')
getscreen().bgcolor(x)
```

**Exercice** : Entrez différents couleurs valides.

Nous pouvons continuer avec une autre couleur de ligne et de remplissage, pour dessiner un rectangle.

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

## Demander en boucle

La boucle `while` permet de répéter les instructions qui se trouvent dans son bloc indenté.
Sur la dernière ligne du bloc indenté nous reposons la question.

Cette boucle répète aussi longtemps que la variable `x` contient une valeur.
Si vous appuyez sur **Enter** sans entrer quelque chose, la boucle s'arrête.

```{codeplay}
from turtle import *
up()

back(200)
x = input('Entrez une couleur: ')
while x:
    color(x)
    dot(80)
    forward(80)
    x = input('Entrez une couleur: ')
```