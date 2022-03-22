# Questionner - `input`

Dans ce chapitre, nous découvrons comment un programme peut poser une question lors de son exécution. L'utilisateur du programme peut alors répondre et entrer une information. La réponse sera stockée dans la mémoire de l'ordinateur et sera associée à une variable. Grâce à cette variable, le programme peut traiter la réponse fournie, et le résultat peut être affiché. Nous allons voir que :

- la fonction `input('question')` demande une information,
- une variable, par exemple `x`, mémorise une information,
- la fonction `print()` affiche un texte (une réponse).

```{question}
En informatique, une variable est

{v}`une place en mémoire`  
{v}`une étiquette pour un objet`  
{v}`un endroit spécifique de stockage`  
{v}`un nom pour une valeur`
```

## Dire bonjour

Nous commençons par le grand classique des livres d'introduction à la programmation : afficher la fameuse phrase *hello world*.
La fonction `print()` permet d'écrire du texte vers la console.
Ici, la console est la zone rectangulaire qui s'affiche sous le code du programme.

```{codeplay}
:file: input0.py
print('hello world.')
```

**Exercice** : Affichez encore 2-3 lignes de texte en plus avec la fonction `print()`.

## Écrire et dessiner

Votre programme peut faire les deux choses dans un même programme : dessiner une image et écrire un texte.
Le texte apparait dans la console, qui apparait directement après le programme.
Le dessin apparait dans une fenêtre spéciale après la console.

```{codeplay}
:file: input1.py
from turtle import *

print('ce programme dessine un carré')

for i in range(4):
    forward(100)
    left(90)
```

**Exercice** : Ajoutez du code pour dessiner un triangle, et annoncez-le dans le texte.

## La fonction `input()`

La fonction `input('question')` permet de demander une entrée (input) à l'utilisateur.
L'utilisateur voit le texte `question` affiché à la console et doit répondre à cette question. Il termine son entrée avec la touche Enter.

La réponse de l'utilisateur est ensuite mémorisée dans une variable que nous appelons `x` dans cet exemple.
Ensuite, nous pouvons utiliser cette variable `x` dans la suite du programme, par exemple dans une expression `print()`.

```{codeplay}
:file: input2.py
x = input('Entrez votre nom: ')
print('Bonjour', x)
```

## La fonction `print()`

La fonction `print()` peut accepter un ou plusieurs arguments, séparés par une virgule. Un espace est inséré à la place de la virgule.
Appeler la fonction `print()` sans argument, insère une ligne vide.

```{codeplay}
:file: input3.py
x = input('Entrez votre nom: ')
print()                 # sans argument - ligne vide
print('Hello')          # un argument
print('Bonjour', x)     # deux arguments
print(x, 'comment vas-tu?')
print(x, 'restera toujours', x)     # trois arguments
print(x, 'voit', x, 'qui voit', x)  # cinq arguments
```

## La variable

Une variable est une place en mémoire pour stocker de l'information.
Vous êtes complètement libres dans le choix des noms pour les variables, mais il est recommandé de choisir des noms qui sont le plus explicites possible. C'est mieux d'utiliser des noms de variable parlants, comme `nom` et `âge`, même si on avait pu utiliser `x` et `y`.  

```{codeplay}
:file: input3.py
nom = input('Entrez votre nom: ')
print('Bonjour', nom)

age = input('Entrez votre âge: ')
print('Très bien', nom, 'vous avez', age, 'ans')
```

**Exercice** : Ajoutez une troisième question et utilisez la réponse dans un `print()`.

## Nommer une variable

Normalement, il est conseillé d'utiliser des variables très explicites, comme `âge`, `prenom`, `nom`, `longueur`, `hauteur`, etc. Cela aide à la compréhension du code.

Mais dans des boucles et dans un contexte local, nous adoptons la convention suivante, consistant à utiliser des variables courtes d'une seule lettre.

- `a` pour un angle, ou une longueur
- `c` pour un caractère, ou une couleur
- `d` pour un diamètre, ou une distance
- `i` pour un entier dans une boucle
- `j` pour un deuxième entier
- `n` pour un nombre donné
- `r` pour un rayon
- `x` pour une coordonnée en direction x
- `y` pour une coordonnée en direction y

```{question}
La variable `i` désigne normalement

{f}`une longueur`  
{f}`un caractère`  
{v}`un entier`  
{f}`une coordonnée`
```

## Demander une couleur

Nous pouvons utiliser la fonction `input()` pour créer une entrée interactive qui demande à l'utilisateur d'entrer une couleur pour l'arrière-plan.

```{codeplay}
:file: input4.py
from turtle import *

x = input('Entrez une couleur: ')
getscreen().bgcolor(x)
```

**Exercice** : Entrez différentes couleurs valides.

Nous pouvons continuer les questions avec une couleur de ligne et une couleur de remplissage, pour dessiner un carré.

```{codeplay}
:file: input5.py
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

**Exercice** : Ajoutez une quatrième question pour demander la couleur des points (dot) et ajoutez un point colorié à chaque sommet du carré.

## Demander en boucle

La boucle `for` permet de répéter les instructions qui se trouvent dans son bloc en indentation.
À chaque tour nous demandons une couleur et nous dessinons un disque colorié avec cette couleur. Si la couleur ne correspond pas à un nom de couleur standard, alors le disque est noir la première fois, et répète la couleur précédente pour les cas suivants.

```{codeplay}
:file: input6.py
from turtle import *
up()

backward(200)
for i in range(6):
    x = input('Entrez une couleur: ')
    dot(80, x)
    forward(80)
print('fini')
```

**Exercice** Entrez les couleurs de l'arc-en-ciel.

## Dessiner un drapeau

Nous reprenons l'exemple des formes ouvertes, avec les deux équerres coloriées.

```{codeplay}
from turtle import *

def equerre():
    begin_fill()
    for i in range(2):
        forward(80)
        left(90)
    end_fill()

def drapeau():
    for i in range(2):
        x = input('Couleur: ')
        fillcolor(x)
        equerre()
    
drapeau()
```

## Créer un quiz

Pour faire des petits quiz nous créons des paires de mots qui vont ensemble. Par exemple pays et capitale dans un cours de géographie, ou une liste de vocabulaire en deux langues, pour un cours de langue.

### Séquence de questions

Nous mettons les deux valeurs `question` et `solution` dans un tuple et nous regroupons ces paires dans un deuxième tuple que nous appelons `quiz`

Quand nous parcourons `quiz` avec une boucle `for` nous pouvons utiliser une seule variable, par exemple `x` et lui affecter le tuple `(question, solution)`

Nous pouvons aussi parcourir le quiz avec un tuple de deux variables `(q, s)` et associer les deux valeurs séparément à chaque variable : donc
`q = question` et `s = solution`.

```{codeplay}

quiz = (('France', 'Paris'),
        ('Allemagne', 'Berlin'),
        ('Suisse', 'Berne'))

print('parcourir avec x')
for x in quiz:
    print('x =', x)
   
print()
print('parcourir avec (q, s)')
for (q, s) in quiz:
    print('q =', q, '   s =', s)
```

### Poser une question

Nous pouvons maintenant extraire la question et la poser plusieurs fois dans une boucle `for`. Avec `input()` nous demandons la réponse. Nous séparons les questions avec un `print()` sans argument pour insérer une ligne vide entre les questions.

```{codeplay}

quiz = (('France', 'Paris'),
        ('Allemagne', 'Berlin'),
        ('Suisse', 'Berne'))

for (q, s) in quiz:
    print('Quelle est la capitale de', q)
    reponse = input('Votre réponse: ')
    print()
```

### Evaluer une réponse

Nous introduisons ici déjà la structure `if-else` que nous allons voir en détail plus tard.

Le mot-clé `if` est suivi d'une condition. Ici nous comparons la réponse donnée par l'utilisateur avec la solution connue par le programme.

L'expression `reponse == solution` renvoie comme valeur `True` ou `False`. Selon cette valeur, un des deux blocs est exécuté.

```{codeplay}

quiz = (('France', 'Paris'),
        ('Allemagne', 'Berlin'),
        ('Suisse', 'Berne'))

for (question, solution) in quiz:
    print('Quelle est la capitale de', question)
    reponse = input('Votre réponse: ')
    if reponse == solution:
        print('correct')
    else:
        print('FAUX! La bonne réponse est', solution)
    print()
```

## Erreurs

Dans des chapitres précédents, nous avons déjà vu quelques messages d'erreurs. Mais il y en a d'autres que nous allons voir ici.
Il est important de bien comprendre les messages d'erreur.
Dans cette section, vous allez découvrir les différentes catégories d'erreur et comment les corriger.

### SyntaxError

Cette erreur survient lorsque vous utilisez des accents dans des noms de fonctions ou de variables.

```{codeplay}
from turtle import *

def carré():
    for à in range(4):
        forward(100)
        left(90)
        
carré()
```

**Exercice** : Corrigez les trois erreurs de syntaxe'.

### SyntaxError: EOF

Cette erreur survient lorsque vous oubliez de fermer une parenthèse.

```{codeplay}
from turtle import *

forward(100)  
left(90)
forward(100
```

**Exercice** : Corrigez l'erreur de syntaxe.

### ValueError

Cette erreur survient lorsque la valeur numérique est trop grande pour correspondre à un Unicode.

```{codeplay}
print(chr(10000000))
```

**Exercice** : Corrigez l'erreur de valeur.

## Exercices

- Téléchargez l'exercice
- Lancez un éditeur externe (tel que Thonny)
- Depuis l'éditeur ouvrez le fichier téléchargé
- Remplacez ... par votre code
- Déposez vos exercices sur Moodle

### Chatbot

Créez un programme qui vous pose des questions

- votre nom
- votre âge
- votre couleur préférée
- votre groupe de musique préféré
- votre classe
- votre meilleur ami

À chaque fois le chatbot mémorise votre réponse dans une variable qu'il utilise dans la phrase suivante.

```{codeplay}
:file: chatbot.py
print('Je suis un chatbot')
print('Quel est ton nom ?')
nom = input()
print('Salut', nom)
...
...
```

### Maison

Créez un programme qui dessine une maison et demande :

- la couleur de la maison
- la couleur de la porte
- la couleur de la fenêtre

Comme nous devons indiquer les noms des couleurs en anglais, nous allons écrire ce programme en anglais.

```{codeplay}
:file: maison.py
from turtle import *

col_house = input('Color of the house: ')
...
```

### Tricolore

Créez un programme qui demande trois couleurs et dessine ensuite un drapeau tricolore.

```{codeplay}
:file: tricolore.py
from turtle import *

def rectangle():
    forward(100)
    ...

for i in range(3): 
    c = input('Couleur du rectangle: ')
    ...
```

### Smileys

Créez un programme qui demande les couleurs d'un smiley.

- visage
- yeux
- bouche

```{codeplay}
:file: smiley.py
from turtle import *

def smiley():
    ...

for i in range(3): 
    c = input('Couleur : ')
    ...
```

### Quiz

Faites un quiz avec 10 questions. Pour chaque question, vérifiez si la réponse est correcte.

```{codeplay}
:file: quiz.py
quiz = (('question1', 'solution1'),
        ('question2', 'solution2'))

for (question, solution) in quiz:
    print(question)
    reponse = input('Votre réponse: ')
    if reponse == solution:
        print('correct')
    else:
        print('FAUX! La bonne réponse est', solution)
    print()
```
