(prog1.attendre)=

# Attendre - `while`

Dans ce chapitre, nous découvrons un deuxième type de boucle, la boucle `while`. Elle est souvent utilisée pour attendre quelque chose. Nous allons voir que :

- la boucle `while` répète aussi longtemps qu'une condition est vraie,
- la fonction `sleep()` permet d'attendre et ralentir le programme,
- le mot-clé `break` permet de sortir de la boucle.

```{question}
En Python, `while` est

{f}`une fonction`  
{f}`une condition`  
{f}`une boucle`  
{v}`un mot-clé`
```

## Compteur à rebours

On peut utiliser la boucle `while` pour créer un compteur à rebours.
Pour attendre une seconde, la fonction `sleep()` du module `time` est importée.

```{codeplay}
:file: while1.py
from time import sleep

n = int(input('Entrez un entier: '))
while n > 0:
    print(n)
    sleep(1)
    n = n - 1

print('boum!!!')
```

## Lister des noms

Nous utilisons une boucle `while` pour demander des noms à l'utilisateur.
On ne peut pas savoir à l'avance combien de noms il y aura, donc ici nous ne pouvons pas utiliser la boucle `for`.  Nous prenons comme condition de terminaison une réponse avec une chaîne vide (`''`).

La convention est d'utiliser des noms au pluriel (`noms`) pour désigner la liste et le même nom au singulier (`nom`) pour désigner un de ses éléments.

```{exercise}
Entrez les noms de 3-4 de vos amis.
```

```{codeplay}
:file: while2.py
noms = []
nom = input('Entrez un nom: ')

while nom != '':
    noms.append(nom)
    nom = input('Entrez un nom: ')
    
print(noms)
```

## Faire une somme

Nous utilisons une boucle `while` pour demander des nombres à l'utilisateur.
On ne peut pas savoir à l'avance combien de nombres il y aura, et donc nous ne pouvons pas utiliser la boucle `for`. Nous prenons comme condition de terminaison une réponse avec une chaîne vide (`''`).

Au lieu d'écrire `while x != '':` nous pouvons simplifier vers  `while x:`.
La raison est que la chaîne vide est associée à `False` et toute autre chaîne non vide est associée à `True`.

```{exercise}
Entrez les frais de vos 3 derniers achats.
```

```{codeplay}
:file: while3.py
somme = 0
x = input('Entrez un nombre: ')

while x:
    somme += float(x)
    x = input('Entrez un nombre: ')
    
print('somme =', somme)
```

## Faire une moyenne

Nous utilisons une boucle `while` pour demander des nombres à l'utilisateur.
On ne peut pas savoir à l'avance combien de nombres il y aura, et donc nous ne pouvons pas utiliser la boucle `for`.  Nous prenons comme condition de terminaison une réponse avec une chaîne vide (`''`).

```{exercise}
Entrez vos notes de français.
```

```{codeplay}
:file: while4.py
somme = 0
n = 0
x = input('Entrez un nombre: ')

while x:
    somme += float(x)
    n += 1
    x = input('Entrez un nombre: ')
    
print('moyenne =', somme/n)
```

## Deviner un nombre

On peut aussi utiliser une boucle `while` pour deviner un nombre.
Ici on importe la fonction `randint()` du module `random`.
Elle fournit un nombre entier aléatoire entre deux bornes (1, 99).

La fonction `input()` ne retourne que le type `str`.
La fonction `int()` transforme le type string (chaîne) en entier (integer).

```{exercise}
Quelle est la meilleure stratégie pour deviner un nombre ?
```

```{codeplay}
:file: while5.py
from random import randint

n = randint(1, 99)
x = int(input('Devinez un nombre entre 1 et 99: '))

while x !=  n:
    if x > n:
        print(x, 'est trop grand')
    else:
        print(x, 'est trop petit')
        
    x = int(input('Entrez un nombre: '))

print('\nBravo. Vous avez réussi!')
```

## Factoriser

Le programme va factoriser le nombre que vous entrez

```{codeplay}
:file: if6.py
n = int(input('Entrez un entier: '))
i = 2

while i < n:
    if n % i == 0:
        print(i)
        n = n // i 
    else:
        i = i + 1

print(n)
```

## En code binaire

Le programme transforme l'entier en code binaire.

```{codeplay}
:file: if7.py
n = int(input('Entrez un entier: '))

code = ''
while n > 0:
    if n % 2 == 1:
        code = '1' + code
    else:
        code = '0' + code
    n = n // 2

print(code)
```

## Indentation

On appelle **bloc** une ou plusieurs lignes d'instructions qui forment un ensemble.
Dans les langages C ou JavaScript un bloc est délimité avec des accolades `{...}`.
L'indentation est encouragée, mais reste optionnelle.

En Python, l'indentation est obligatoire. C'est la façon officielle de designer un bloc.
Ceci présente deux avantages :

- plus besoin d'accolades pour délimiter un bloc,
- la structure des blocs est claire et visuelle.

Une **indentation** est un retrait du code par rapport à la marge gauche de 4 caractères.
Elle peut être insérée avec la touche tabulateur **TAB** (symbolisée par une flèche à gauche du clavier).

Un bloc est défini comme un ensemble de lignes de même indentation.
Des blocs marqués par une indentation se trouvent après les mots-clés pour :

- la définition de fonction (`def`),
- l'instruction conditionnelle (`if-elif-else`),
- la boucle (`for/while`).

En Python, le symbole `:` en fin de ligne introduit un sous-bloc qui doit être indenté.
Voici 5 sous-blocs à la suite des mots-clés `def`, `if`, `elif`, `else`, `for` :

```{codeplay}
:file: while6.py
def f(x):
    if x > 0:
        return 'positif'
    elif x < 0:
        return 'négatif'
    else:
        return 'zéro'

for i in range(-2, 2):
    print(i, f(i)) 
```

Dans l'exemple suivant, nous avons une boucle qui fait trois itérations.
Les deux instructions `print()` font partie du bloc de la boucle.

```{exercise}
Enlevez l'indentation de l'instruction `print('-' * 11)`.
```

```{codeplay}
:file: while7.py
for i in range(3):
    print('itération', i)
    print('-' * 11)
```

## Sortir avec `break`

Le mot-clé `break`, seul sur une ligne, permet de sortir d'une boucle.
Souvent cette méthode est utilisée pour sortir d'une boucle infinie.

```{codeplay}
:file: while8.py
noms = []

while True:
    nom = input('Entrez un nom: ')
    if nom == '':
        break
    noms.append(nom)
    
print(noms)
```
