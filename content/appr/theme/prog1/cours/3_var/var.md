# 2. Variables et expressions

Les données qu'un ordinateur manipule se trouvent dans sa mémoire.
On peux s'imaginer la mémoire comme un grand espace divisé en octets.
Chaque octet a une adresse numérique, souvent exprimée avec un nombre hexadécimal.

Par exemple la valeur `26` (ou `0x1A` en format hexadécimal) pourrait se trouver à l'adresse `0x1200A`.

Pour ne pas avoir besoin de gérer l'adresse exacte en mémoire, Python utilise le concept de variable. Une **variable** est une étiquette qui permet de réserver un espace mémoire pour stocker une donnée.

Une variable permet de :

- sauvegarder une valeur dans la mémoire,
- lire cette valeur depuis la mémoire,
- utiliser cette valeur dans une expression.

On peut notamment stocker dans des variables :

- des nombres,
- des chaînes de caractères,
- des valeurs booléennes (`True` ou `False`).

## Affectation

On appelle **affectation** l'action d'associer une valeur à une variable.  
La forme générale d'une affectation est `var = valeur` :

- le nom de la variable se trouve à gauche (`var`),
- le symbole d'affectation (`=`) se trouve ou milieu,
- la valeur à affecter à la variable se trouve à droite (`valeur`).

Dans l'exemple suivant nous avons deux variables `r` et `pi`.
Ensuite nous pouvons utiliser dans une expression mathématiques et afficher le résultat avec la fonction `print()`. L'exemple suivant calcule la circonférence d'un cercle.

```{codeplay}
r = 10
pi = 3.14

print(2 * pi * r)
```

**Exercice** : Calculez et affichez en plus la surface du cercle.

Faisons un autre exemple ou les variables `a` et `b` désignent hauteur et largeur d'un rectangle.

```{codeplay}
a = 5
b = 8

print('surface =', a * b)
print('périmètre =')
print('diagonale =')
```

**Exercice** : Complétez le calcul du périmètre et de la diagonale.


À n'importe quel moment, la variable peut être réaffectée, et donc changer de valeur.

```{codeplay}
r = 1
print('r =', r, 'surface =', 3.14 * r ** 2)

r = 3
print('r =', r, 'surface =', 3.14 * r ** 2)
```

## Affectation multiple

Python permet d'affecter plusieurs variables sur une même ligne.
Ceci est parfois utilisé pour assigner des coordonnées.

```{codeplay}
x, y = 3, 4
print(x, y)
```

L'affectation multiple est une manière élégante d'échanger les valeurs de deux variables.

```{codeplay}
x, y = 3, 4
print(x, y)

x, y = y, x
print(x, y)
```

## Fonction input()

La fonction `input()` permet de demander une valeur d'entrée (input) lorsque le programme est en cours d'exécution. Cela permet d'écrire des programmes qui utiliseront des valeurs qui sont encore potentiellement inconnues lors de l'écriture du programme.

L'instruction `input('explication')` affiche le texte `explication` dans la console. À ce moment l'exécution du programme est interrompue et le programme attend à ce que soit entrée une valeur, confirmée avec la touche `Enter`.

Dès que la touche `Enter` est enfoncée, la valeur entrée est alors retournée par la fonction `input()`.
Normalement cette valeur est affectée à une variable.

Voici un exemple de code pour vous saluer personnellement...

```{codeplay}
nom = input('Entrez votre nom: ')
print('Bonjour', nom)
```

Bien sur, nous pouvons utiliser n'importe quel nom de variable, par exemple `x` :

```{codeplay}
x = input('Entrez votre nom: ')
print('Bonjour', x)
```

**Exercice** : Ecrivez un programme qui demande votre age et qui affiche ensuite la phrase 'Vous avez x ans'

## Valeur et expression

Une **valeur** est une quantité élémentaire qui ne peut pas être évaluée par une forme plus simple.

Voici des exemples de valeurs :

- un nombre entier : `123`,
- un nombre à virgule flottante : `1.23`,
- une chaine de caractères : `'hello'`.

Une **expression** est une valeur, une variable ou la combinaison de valeurs et variables avec des opérateurs mathématiques. Par exemple :

- une variable : `a`,
- une variable et une valeur liées par un opérateur : `a + 4`,
- plusieurs valeurs liées par des opérateurs : `(1 + 2) * (3 + 4)`.

La dernière expression contient deux sous-expressions entre parenthèses.
Elles sont évaluées d'abord et donnent l'expression simplifiée `3 * 7` qui est de nouveau évaluée et qui donne `21` comme résultat final.

```{codeplay}
a = 7

print(a)
print(a + 4)
print((1 + 2) * (3 + 4))
```

## Types

Les données que Python peut manipuler sont de types différents.
Selon leur type, les données occupent un nombre d'octets différent dans la mémoire de l'ordinateur :

- un nombre entier (integer) occupe 4 octets,
- un nombre à virgule flottante (double) occupe 8 octets,
- une chaine de caractères (string) occupe un espace mémoire variable (1 octet/caractère).

Les opérations possibles sont également différentes.
Par exemple nous pouvons multiplier deux nombres mais nous ne pouvons pas multiplier deux chaines de caractères.

La fonction `type()` nous retourne le type de la valeur donnée comme argument.

```{codeplay}
print(type(123))
print(type('123'))
```

**Exercice** : De quel type est `1.23` ?

L'expression `123` est de type `int` (integer = entier) tandis que la même expression entre guillemets `'123'` devient une chaîne de caractères de type `str` (string = chaine).

Les objets `123` et `'123'` sont traités de façon différente dans une expression :

```{codeplay}
print(123 * 3)
print('123' * 3)
```

## Transformer `str` en `int`

La valeur retourne avec `input()` est toujours une chaîne de caractères (`str`).
Avec la fonction `int()` nous pouvons transformer un nombre sous forme texte vers un entier.

```{codeplay}
x = input('entrez un nombre: ')
print(type(x))
print(x * 12)

x = int(x)
print(type(x))
print(int(x) * 12)
```

Avec la fonction `str` nous pouvons transformer un nombre en texte.
Ceci peut être utile pour connaître le nombre de chiffres dans un nombre.

```{codeplay}
x = str(123 ** 123)
print(x)
print(len(x))
````

**Exercice** : Combien de chiffres comporte le résultat de $123 ^ 456$

## Nom d'une variable

Le nom d'une variable est sensible à la casse (minuscule ou majuscule). Ainsi, `a` et `A` sont deux variables différentes.

```{codeplay}
a = 1
A = 99
print(a, A)
print(a + A)
```

Le nom d'une variable peut être composé de :

- lettres (minuscules et majuscules),
- tiret bas `_`,
- chiffres (sauf pour le premier caractère).

Sont interdits :

- les espaces,
- les mots-clés (`if`, `else`, ...),
- tout autre caractère spécial (`* + % & $ - / ?`).

Ces noms de variables sont donc valides : `a2`, `_a`, `speed`, `pos_x`, `POS_X`

Ceux-ci ne sont pas valides :

- `2var` (commence avec un chiffre),
- `if` (correspond à un mot-clé),
- `var$2` (contient un caractère spécial),
- `mon nom` (contient une espace et est interprété comme deux noms de variables).



<br>
<br>

## Exercices
*Les exercices suivants sont à faire dans l'IDE de votre choix.*

````{admonition} Exercice 1 : affectation ✏️📒
:class: note
<!-- <span style="color:green">Niveau débutant</span> -->

Sans utiliser l'ordinateur, déterminez ce qui va être affiché par les cinq instructions `print` dans ce programme.

```python
    a = 23
    b = "hello"
    c = 2
    print(a + 5)
    print(a - 1)
    a = a + c
    print(a)
    c = c + a
    print(c)
    print(b + a)
```
````


````{admonition} Exercice 2 : input 🔌
:class: note
<!-- <span style="color:green">Niveau débutant</span> -->

Faites un programme qui demande le **prénom** de l'utilisateur et qui affiche la phrase suivante :

```text
    Bonjour, _prénom_, avez-vous passé une bonne journée ?
```
````

````{admonition} Exercice 3 : cylindre 🔌
:class: note
<!-- <span style="color:orange">Niveau intermédiaire</span> -->

Faites un programme qui demande à l'utilisateur la hauteur et le diamètre d'un cylindre et retourne le volume du cylindre avec une phrase complète.
````

````{admonition} Exercice 4 : jeu 🔌
:class: note
<!-- <span style="color:red">Niveau avancé</span> -->

Le **cadavre exquis** est un jeu graphique ou d'écriture collectif inventé par les surréalistes, en particulier Jacques Prévert et Yves Tanguy, vers 1925.

Définition : _jeu qui consiste à faire composer une phrase, ou un dessin, par plusieurs personnes sans qu'aucune d'elles ne puisse tenir compte de la collaboration ou des collaborations précédentes._

Faites un programme qui permet de faire un jeu d'écriture collectif (cadavre exquis) :

- le premier utilisateur doit proposer un sujet,
- le deuxième, un verbe,
- le troisième, un complément d'objet direct (COD),
- le quatrième, un complément d'objet indirect (COI),
- le dernier, un groupe permutable.
````
