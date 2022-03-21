# Calculer - `int`

Dans ce chapitre, nous allons voir comment un programme peut calculer avec des nombres.
Ceci est utilisé dans une calculatrice ou un tableur.

Les nombres entiers forment une catégorie très importante. En anglais, un entier est appelé **integer** (`int`). Nous allons voir que :

- les opérateurs de base sont `+`, `-`, `*` et `/`,
- les nombres sont du type `int` ou `float`,
- un texte est du type `str`.

```{question}
En informatique, `int` est l'abbréviation pour

{f}`international`  
{v}`entier`  
{f}`interne`  
{f}`intelligent`
```

## Un calcul simple

Dans ce chapitre, nous allons explorer comment nous pouvons calculer avec des nombres. Voici un exemple qui affiche dans une première ligne sous forme de texte une expression mathématique, et dans une deuxième ligne une expression mathématique qui sera évaluée vers son résultat numérique.

```{codeplay}
:file: int0.py
print('2 à la puissance 32 =')
print(2 ** 32)
```

## Opérateurs de base

En Python, nous retrouvons les 4 opérations arithmétiques de base :

- addition (`+`)
- soustraction (`-`)
- multiplication (`*`)
- division (`/`)

```{codeplay}
:file: int1.py
print('3 + 4 =', 3 + 4)
print('3 - 4 =', 3 - 4)
print('3 * 4 =', 3 * 4)
print('3 / 4 =', 3 / 4)
```

**Exercice** : Modifiez les 4 calculs et exécutez de nouveau.

```{question}
Quel est le résultat de l'expression `'12' + '12'` ?  
{f}`12`  
{f}`24`  
{v}`1212`  
{f}`1221`  
```

## Puissance

En Python l'opérateur de puissance est `**`. Ne le confondez pas avec le symbole `^` utilisé dans d'autres langages tel qu’Excel.

```{codeplay}
print('le carré de 7 est')
print(7 ** 2)
print()
print('le cube de 4 est')
print(4 ** 3)
```

Nous pouvons utiliser une puissance de 0.5 pour calculer une racine.

```{codeplay}
print('la racine de 2 est')
print(2 ** 0.5)
```

Nous pouvons maintenant calculer une diagonale, en utilisant le théorème de Pythagore.

```{codeplay}
print("la diagonale d'un rectangle de 3 sur 6 est")
print((3 ** 2 + 6 ** 2) ** 0.5)
```

## Division entière

En Python, nous avons un opérateur spécial pour la division entière (`//`) ainsi que pour le reste de la division entière. L'opérateur pour le reste de la division entière est `%` est s'appelle **modulo**.

```{codeplay}
print('division')
print('7 / 3 =', 7 / 3)
print('division entière')
print('7 // 3 =', 7 // 3)
print('modulo')
print('7 % 3 =', 7 % 3)
```

```{question}
Quel est le résultat de l'expression `10 % 3` ?

{v}`1`  
{f}`2`  
{f}`3`  
{f}`3.333333`
```

## Les variables

Une **variable** est une manière de désigner une valeur par un nom. Le terme technique pour associer une valeur à une variable est **affectation** et elle utilise le symbole `=` (égal).

Mais faites attention ! Il ne s'agit pas d'une équation dans le sens mathématique. La variable doit toujours figurer seule à gauche.
La forme générique d'une affectation est `var = expression`.

```{codeplay}
:file: int3.py
r = 3
pi = 3.14

print('rayon =', r)
print('diamètre =', 2 * r)
print('circonférence =')
print('surface =')
```

**Exercice** : Ajoutez le calcul de la circonférence et de la surface du cercle.

Pour nommer une variable, vous pouvez utiliser :

- lettres (`a...z` et `A...Z`),
- chiffres (`0...9`),
- le tiret bas (`_`).

Le nom de variable :

- est sensible aux majuscules/minuscules,
- ne peut pas commencer avec un chiffre,
- ne doit pas consister d'un mot-clé (`if`, `else`, `for`),
- ne doit pas contenir un caractère spécial (`* + % & $ - / ?`).

Ces noms de variables sont donc valides : `a2`, `_a`, `speed`, `pos_x`, `POS_X`

Ceux-ci sont invalides :

- `2var` (commence avec un chiffre),
- `if` (correspond à un mot-clé),
- `var$2` (contient un caractère spécial),
- `mon nom` (contient une espace et est interprété comme deux noms de variables).

```{question}
Lesquels des noms de variable sont valides ?

{f}`var 2`  
{v}`var2`  
{f}`2var`  
{f}`if`  
```

Voici un autre calcul où `a` et `b` désignent largeur et hauteur d'un rectangle.

```{codeplay}
:file: int4.py
a = 3
b = 5

print('largeur =', a)
print('hauteur =', b)
print('surface =', a * b)
print('périmètre =')
print('diagonale =')
```

**Exercice** : Complétez le calcul du périmètre et de la diagonale.

```{question}
Quels noms de variable sont valides ?

{f}`if`  
{v}`VAR_2`  
{v}`_if`  
{v}`elseif`  
{f}`var$2`
```

## Les types

Un ordinateur peut manipuler différentes catégories d'objets telles que image, texte, nombre. On parle alors du type de ces données.

La fonction `type()` retourne le type d'un objet.

```{codeplay}
:file: int5.py
print(type('hello'))
print(type(123))
print(type(3.14))
```

**Exercice** : Trouvez encore d'autres types.

L'exemple ci-dessus nous montre que

- `str` (string) désigne des chaînes de caractères,
- `int` (integer) désigne des nombres entiers,
- `float` (floating point) désigne des nombres à virgule flottante.

Les trois fonctions `str()`, `int()` et `float()` permettent de transformer un objet d'un type à un autre.

Par exemple, la chaîne `'123'` peut être transformée soit en entier, soit en nombre à virgule flottante.

```{codeplay}
a = '123'
b = int(a)
c = float(a)

print(b, c)
print(type(a))
print(type(b))
print(type(c))
```

Nous reconnaissons la différence entre un entier (`int`) et un nombre à virgule flottante (`float`) par la présence du point décimal (`123.0`).

## Demander un nombre

La fonction `input()` permet d'obtenir une entrée de l'utilisateur. Mais attention !
La valeur retournée est une chaine de caractères (de type string `str`).

```{codeplay}
x = input('Entrez un nombre entier: ')
print(type(x))
print(x * 5)
print(int(x) * 5)
```

Pour pouvoir l'utiliser dans un calcul, nous devons la transformer en virgule flottante avec la fonction de conversion `float()`.

```{codeplay}
r = float(input('Entrez le rayon: '))
pi = 3.14

print('Circle')
print('rayon =', r)
print('diamètre =', 2 * r)
print('circonférence =', pi * 2 * r)
print('surface =')
```

**Exercice** : Complétez le programme pour afficher la surface du cercle.

Nous pouvons également créer des programmes où nous demandons plusieurs valeurs à l'utilisateur. Cette fois, nous permettons seulement l'utilisation de nombres entiers, et donc transformons la chaine obtenue avec `int()` en nombre entier.

```{codeplay}
:file: int8.py
print('Rectangle')
a = int(input('Entrez la largeur: '))
b = int(input('Entrez la longueur: '))

print('surface =', a * b)
print('périmètre =')
print('diagonale =')
```

**Exercice** : Complétez le programme pour afficher le périmètre et la diagonale.

## Quiz avec score

Nous reprenons l'exemple du chapitre précédent et nous ajoutons le calcul du score

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

## Quiz mathématique

Nous utilisons un tuple avec deux valeurs (a, b) que nous mettons dans un deuxième tuple.
Cette fois nous avons pas besoin de donner une solution, car nous pouvons la calculer.

```{codeplay}
print('Quiz addition')
for (a, b) in ((12, 35), (23, 11), (55, 23)):
    print(a, '+', b, '=')
    reponse = int(input())
    if reponse == a + b:
        print('correct')
    else:
        print('FAUX. La bonne réponse est', a + b)
    print()
```

**Exercice** : Ajoutez le score pour ce quiz.

## Erreurs

En utilisant les calculs, nous allons rencontrer encore d'autres types d'erreurs. Pour bien programmer, vous devez savoir interpréter les messages d'erreur. Ces messages vous indiquent sur quelle ligne du programme il y a quel type d'erreur.

### SyntaxError

Cette erreur survient lorsque vous oubliez un signe de ponctuation (parenthèse, virgule, apostrophe).

```{codeplay}
print('hello'
print(12 34)
print('bonjour)
```

**Exercice** : Corrigez les trois erreurs de syntaxe.

### TypeError

Cette erreur survient lorsque vous mettez des opérandes dont le type n'est pas approprié pour l'opérateur.

```{codeplay}
print('10' > 0)
print('10' * '10')
print('10' + 10)
```

**Exercice** : Corrigez les trois erreurs de type.

### ZeroDivisionError

Cette erreur survient lorsque vous essayez de diviser par zéro.

```{codeplay}
print(10 / 0)
print(10 // 0)
print(10 % 0)
```

**Exercice** : Corrigez les trois erreurs de division par zéro.

### RangeError

Cette erreur survient lorsqu'une fonction récursive s'appelle elle-même un trop grand nombre de fois.

```{codeplay}
def f(x):
    if x == 1:
        return 1
    else: 
        return 1 + f(x-1)

print(f(100))
print(f(1000))
print(f(10000))
print(f(20000))
```

## Exercices

- Téléchargez l'exercice
- Lancez un éditeur externe (tel que Thonny)
- Depuis l'éditeur, ouvrez le fichier téléchargé
- Remplacez ... par votre code
- Déposez vos exercices sur Moodle

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

r = float(input('Entrez le rayon r: '))
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

r = float(input('Entrez le rayon r: '))
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
