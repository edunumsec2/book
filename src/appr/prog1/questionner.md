(prog1.questionner)=

# Questionner - `input()`

Dans ce chapitre, nous découvrons comment un programme peut poser une question lors de son exécution. L'utilisateur du programme peut alors répondre et entrer une information. La réponse sera stockée dans la mémoire de l'ordinateur et sera associée à une variable. Grâce à cette variable, le programme peut traiter la réponse fournie, et le résultat peut être affiché. Nous allons voir que :

- la fonction `input('question')` demande une information,
- une variable, par exemple `x`, mémorise une information,
- la fonction `print()` affiche un texte (une réponse).

## La fonction `input()`

La fonction `input('question')` permet de demander une entrée (input) à l'utilisateur.
L'utilisateur voit le texte `question` affiché à la console et doit répondre à cette question. Il termine son entrée avec la touche Enter.

La réponse de l'utilisateur est ensuite mémorisée dans une variable que nous appelons `x` dans cet exemple.
Ensuite, nous pouvons utiliser cette variable `x` dans la suite du programme, par exemple comme argument dans une fonction `print()`.

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
Vous êtes complètement libres dans le choix des noms pour les variables, mais il est recommandé de choisir des noms qui sont le plus explicites possible. C'est mieux d'utiliser des noms de variable parlants, comme `nom` et `age`, même si on avait pu utiliser `x` et `y`.  

```{exercise}
Ajoutez une troisième question et utilisez la réponse dans un `print()`.
```

```{codeplay}
:file: input3.py
nom = input('Entrez votre nom: ')
print('Bonjour', nom)

age = input('Entrez votre âge: ')
print('Très bien', nom, 'vous avez', age, 'ans')
```

## Demander un nombre

La fonction `input()` permet d'obtenir une entrée de l'utilisateur. Mais attention !
La valeur retournée est une chaine de caractères (de type string `str`). Nous pouvons le prouver avec la fonction `type()`.

```{codeplay}
x = input('Entrez un nombre: ')
print(type(x))
```

Pour pouvoir utiliser cette valeur dans un calcul, nous devons la transformer en nombre. Pour convertir une chaine de caractères en un nombre à virgule flottante nous utilisons la fonction de conversion `float()`.

```{codeplay}
x = '1.5'
print(type(x))          # la variable x contient une chaîne
print(type(float(x)))   # la fonction float(x) renvoie un nombre
```

## Opérations de base

En Python, nous retrouvons les 4 opérations arithmétiques de base :

- addition (`+`)
- soustraction (`-`)
- multiplication (`*`)
- division (`/`)

```{codeplay}
print('Opérations de base')
a = float(input('Entrez un nombre: '))
b = float(input('Entrez un nombre: '))
print()
print('Addition      ', a + b)
print('Soustraction  ', a - b)
print('Multiplication', a * b)
print('Division      ', a / b)
```

## Puissance

En Python l'opérateur de puissance est `**`. Ne le confondez pas avec le symbole `^` utilisé dans d'autres langages tel qu’Excel.

```{codeplay}
print('Puissance')
a = float(input('Entrez un nombre: '))
n = float(input('Entrez un exposant: '))
print()
print(a, 'puissance', n, '=', a ** n)
```

Nous pouvons utiliser une puissance de 0.5 pour calculer une racine.

```{codeplay}
print('Racine')
a = float(input('Entrez un nombre: '))
print('La racine de', a, 'est', a ** 0.5)
```

Nous pouvons maintenant calculer une diagonale, en utilisant le théorème de Pythagore.

```{codeplay}
print('Pythagore')
a = float(input('Entrez un nombre a: '))
b = float(input('Entrez un nombre b: '))
print()
print('La diagonale est', (a ** 2 + b ** 2) ** 0.5)
```

## Division entière

En Python, nous avons un opérateur spécial pour la division entière (`//`) ainsi que pour le reste de la division entière. L'opérateur pour le reste de la division entière est `%` est s'appelle **modulo**.

Cette fois-ci nous transformons la chaine pas en nombre à virgule flottante (`float`), mais en nombre enter (`int`).

```{codeplay}
print('Division entière')
a = int(input('Entrez un entier a: '))
b = int(input('Entrez un entier b: '))
print()
print('Division normale    ', a / b)
print('Division entière    ', a // b)
print('Reste de la division', a % b)
```

```{question}
Quel est le résultat de l'expression `10 % 3` ?

{v}`1`  
{f}`2`  
{f}`3`  
{f}`3.333333`
```

```{question}
En informatique, `int` est l'abréviation pour

{f}`international`  
{v}`entier`  
{f}`interne`  
{f}`intelligent`
```

## Calcul géométrique

Dans l'exemple suivant, on demande le rayon et on affiche rayon, diamètre et circonférence. Ajoutez la surface du cercle en utilisant la formule :

$$ S = \pi r^2 $$

```{exercise}
Complétez le programme pour afficher la surface du cercle.
```

```{codeplay}
print('Circle')
r = float(input('Entrez le rayon: '))
pi = 3.14
print()
print('rayon =', r)
print('diamètre =', 2 * r)
print('circonférence =', pi * 2 * r)
print('surface =', ...)
```

Nous pouvons également créer des programmes où nous demandons plusieurs valeurs à l'utilisateur. Cette fois, nous permettons seulement l'utilisation de nombres entiers, et donc transformons la chaine obtenue avec `int()` en nombre entier.

```{exercise}
Complétez le programme pour afficher le périmètre et la diagonale.
```

```{codeplay}
:file: int8.py
print('Rectangle')
a = float(input('Entrez la largeur: '))
b = float(input('Entrez la longueur: '))

print('surface =', a * b)
print('périmètre =', ...)
print('diagonale =', ...)
```

## Créer un quiz

Pour faire des petits quiz, nous créons des paires de mots qui vont ensemble. Par exemple pays et capitale dans un cours de géographie, ou une liste de vocabulaire en deux langues, pour un cours de langue.

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

### Quiz avec score

Comment ajouter un score ?

Il faut ajouter 3 éléments de code pour:

- initialiser une variable au début
- augmenter la valeur avec chaque bonne réponse
- afficher le score à la fin

```{codeplay}
score = 0   # initialiser au début

print('avant', score)
score = score + 1
print('après', score)

print('Votre score est', score)
```

Nous reprenons l'exemple du [chapitre précédent](prog1.randomiser) et nous ajoutons le calcul du score

```{codeplay}
score = 0
quiz = (('France', 'Paris'),
        ('Allemagne', 'Berlin'),
        ('Suisse', 'Berne'))

for (question, solution) in quiz:
    print('Quelle est la capitale de', question)
    reponse = input('Votre réponse: ')
    if reponse == solution:
        print('correct')
        score = score + 1
    else:
        print('FAUX! La bonne réponse est', solution)
    print()

print('Votre score: ', score, 'sur', len(quiz))
```

### Quiz mathématique

Nous utilisons un tuple avec deux valeurs (a, b) que nous mettons dans un deuxième tuple.
Cette fois nous avons pas besoin de donner une solution, car nous pouvons la calculer.

```{exercise}
Ajoutez le score pour ce quiz.
```

```{codeplay}
print('Quiz addition')
quiz = ((12, 35), (23, 11), (55, 23))

for (a, b) in quiz:
    print(a, '+', b, '=')
    reponse = int(input())
    if reponse == a + b:
        print('correct')
    else:
        print('FAUX. La bonne réponse est', a + b)
    print()
```

## Erreurs

Dans des chapitres précédents, nous avons déjà vu quelques messages d'erreurs. Mais il y en a d'autres que nous allons voir ici.
Il est important de bien comprendre les messages d'erreur.
Dans cette section, vous allez découvrir les différentes catégories d'erreur et comment les corriger.

### SyntaxError - accents

Cette erreur survient lorsque vous utilisez des accents dans des noms de fonctions ou de variables.

```{exercise}
Corrigez les trois erreurs de syntaxe'.
```

```{codeplay}
from turtle import *

def carré():
    for à in range(4):
        forward(100)
        left(90)
        
carré()
```

### SyntaxError - parenthèses

Cette erreur survient lorsque vous oubliez de fermer une parenthèse.

```{exercise}
Corrigez l'erreur de syntaxe.
```

```{codeplay}
from turtle import *

forward(100)  
left(90)
forward(100
```

### SyntaxError - ponctuation

Cette erreur survient lorsque vous oubliez un signe de ponctuation (parenthèse, virgule, apostrophe).

```{exercise}
Corrigez les trois erreurs de syntaxe.
```

```{codeplay}
print('hello'
print(12 34)
print('bonjour)
```

### TypeError

Cette erreur survient lorsque vous mettez des opérandes dont le type n'est pas approprié pour l'opérateur, par exemple une comparaison entre une chaîne et un entier.

```{exercise}
Corrigez les trois erreurs de type.
```

```{codeplay}
print('10' > 0)
print('10' * '10')
print('10' + 10)
```

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
```

### Rectangle

Faites un programme qui demande à l'utilisateur les côtés a et b d'un rectangle et calcule ensuite

le périmètre

$$ p = 2 (a+b) $$

la surface

$$ S = ab $$

et la diagonale

$$ d = \sqrt{a^2 + b^2} $$

```{codeplay}
:file: rectangle.py
print('Le rectangle')

a = float(input('Entrez la longueur a: '))
...

```

### Cercle

Faites un programme qui demande à l'utilisateur le rayon d'un cercle et calcule ensuite

le diamètre

$$ d = 2r $$

la circonférence

$$ c = 2 \pi r $$

et la surface

$$ S = \pi r^2 $$

```{codeplay}
:file: cercle.py
print('Le cercle')

r = input('Entrez le rayon r: ')
...

```

### Sphère

Faites un programme qui demande à l'utilisateur le rayon d'une sphère et calcule ensuite

le diamètre

$$ d = 2r $$

la surface

$$ A = 4 \pi r^2 $$

et le volume

$$ V = \frac{4 \pi r^3}{3} $$

```{codeplay}
:file: sphere.py
print('La sphère')

r = input('Entrez le rayon r: ')
...

```

### Quiz de multiplication

Créez un quiz de multiplication.

- Complétez pour avoir 10 questions
- Corrigez les erreurs
- Ajoutez le calcul du score

```{codeplay}
:file: quiz_mul.py
print('Quiz de multiplication')
score = 0

for (a, b) in ((4, 6), (5, 6)):
    print(a, '*', b, '=')
    reponse = int(input())
    if reponse == a * b:
        print('correct')
    else:
        print('FAUX. La bonne réponse est', a + b)
    print()

print('Votre score est')
```

### Quiz de vocabulaire

Créez un quiz de vocabulaire français-anglais.

- Complétez pour avoir 10 questions
- Corrigez les erreurs
- Ajoutez le calcul du score

```{codeplay}
:file: quiz_mul.py
print('Quiz de vocabulaire anglais')
score = 0
quiz = (('ordinateur', 'computer'),
        ('clavier', 'keyboard'),
        ('souris', 'display'))

for (question, solution) in quiz:
    reponse = input(question + ': ')
    if reponse == solution:
        print('correct')
    else:
        print('FAUX. La bonne réponse est', question)
    print()

print('Votre score est')
```

### Quiz Kahoot

La plate-forme d'apprentissage ludique [Kahoot!](https://fr.wikipedia.org/wiki/Kahoot!) est utilisée comme technologie éducative dans les écoles et autres établissements d'enseignement.

Ses jeux d’apprentissage, *Kahoots*, sont des questionnaires à choix multiples qui permettent à plusieurs utilisateurs de jouer simultanément. Le site est accessible via un navigateur Web, mais aussi téléchargeable sur smartphone.

Créez un quiz avec des questions sur un sujet de culture générale, dans le style des quiz sur le site Kahoot.

- Complétez pour avoir 10 questions
- Ajoutez le calcul du score

```{codeplay}
:file: kahoot.py
print('Quiz Kahoot Disney')
print()
score = 0

quiz = (("Quel est le nom du cowboy dans Toy Story", 'Woody'),
        ("Comment s'appelle le garçon dont le nez grandit quand il ment", 'Pinocchio'),
        ("Quel est le nom de la fée dans Peter Pan", 'Tinkerbell'))


for (question, solution) in quiz:
    print(question + '?')
    reponse = input()
    if reponse == solution:
        ...
    else:
        ...
    print()

print('Votre score est', ...)
```
