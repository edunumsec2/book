# Fonctions

<!-- REVIEW/JPP: les fonctions sont l'un des principaux outils que la programmation nous offre pour organiser le code, le modulariser, monter dans les niveaux d'abstractions, etc., le tout avec des principes et une syntaxe simple en Python. Je suis d'avis de les traiter avant toutes les structures de données (ne serait-ce que parce que la manipulation des structures de données demande d'utiliser des fonctions et des méthodes). -->
Souvent, en programmation, on a besoin de faire la même chose plusieurs fois, ou de résoudre des problèmes semblables par une même suite d'instructions.

## Concept de fonction

La quasi-totalité des langages de programmation disposent d'un concept de *sous-programme*, qui nous permet de prendre une suite d'instructions, de lui donner un nom, et d'ensuite les exécuter autant de fois que nécessaire simplement en utilisant le nom de ce sous-programme. En Python, un tel sous-programme s'appelle une **fonction**.

Les fonctions sont flexibles et peuvent être _paramétrées_, c'est-à-dire qu'elle vont demander des valeurs supplémentaires lors de leur exécution, valeurs qu'on appelle _arguments_. Finalement, elle peuvent aussi calculer et _retourner une valeur_ qui sera utilisable depuis le code qui a appelé la fonction.

On peut considérer que les fonctions fournissent ainsi la possibilité d'enrichir le _vocabulaire_ avec lequel on donne des instructions à la machine. Voici un exemple:

```{codeplay}
def saluer(nom):
    print("Bonjour", nom)
    print("Vous êtes en train de programmer!")

saluer('Marc')
```

**Exercice:** Ajoutez un deuxième appel de fonction pour `Ada`.

Cet exemple illustre à la fois

- la _définition_ d'une nouvelle fonction avec `def saluer(nom)` et
- son _appel_, donc son utilisation avec `saluer('Marc')`.

Une fonction doit être définie avant sa première utilisation. Ici, elle s'appelle `saluer` et exécute deux instructions `print`. Elle possède un argument qui est nommé **nom**.
Cet argument est utilisé au sein de la fonction, et prendra la valeur qu'on lui assignera lors de l'appel de la fonction.
L'argument de la fonction est une variable local, qui est visible et utilisable uniquement à l'intérieur du bloc de la fonction.

## Appeler une fonction

Une fois une fonction définie, il est possible de l'utiliser en l'appelant. Pour ce faire, il suffit d'écrire le nom de la fonction suivi des éventuels arguments de la fonction entre parenthèses.

Voici quelques exemples d'utilisation de fonctions prédéfinies en Python.
La fonction `print` affiche ses arguments dans la console.
Elle est très polyvalent au niveau du nombre des arguments:

- avec 1 argument : affiche une chaine de texte
- avec 0 arguments : affiche une ligne vide
- avec 2 arguments : affiche chaque résultat séparé par une espace

```{codeplay}
print('bonjour')
print()
print(123, 2**8)
```

**Exercice:** Ajoutez une instruction `print` avec 3 arguments de type différent.

La fonction `print` possède aussi un paramètre optionnel, qui indique quel caractère à utiliser comme séparateur entre plusieurs arguments à afficher.

- le séparateur par défaut et l'espace `' '`
- l'exemple 2 utilise la chaine vide comme séparateur, les arguments sont collées ensemble
- l'exemple 3 utilise la chaine `'---'` comme séparateur

```{codeplay}
nom = 'Guido'
print('Bonjour', nom, 'ça va?')
print('Bonjour', nom, 'ça va?', sep='')
print('Bonjour', nom, 'ça va?', sep='---')
```

**Exercice:** Ajoutez une fonction `print` avec 4 arguments et un séparateur non-standard.

## Fonctions natives

Voici quelques fonctions natives, c'est à dire des fonctions standards qui font partie de Python:

- la fonction `pow` retourne la puissance de ses deux arguments (ici, par exemple, $3^5$)
- la fonction `len` retourne la longueur d'une chaine de caractères ou d'une liste
- la fonction `round` retourne l'arrondi d'une valeur numérique

```{codeplay}
print(pow(3, 5))
print(len("Bonjour"))
print((round(333.76)))
```

**Exercice:** Aujoute une ligne avec la fonction `min` qui retourne la valeur minimale des arguments qu'on lui fournit.

## Définir une fonction

Pour définir une fonction, il faut écrire sur la première ligne:

- le mot-clé `def`
- le nom de la fonction
- suivi par une paire de parenthèses `()`
- contenant une liste de 0 ou plusieurs arguments, séparé par une virgule `,`
- terminé par un deux-points `:`

On appelle cette première ligne **signature** de la fonction:

```python
def ma_fonction(arg1, arg2):
```

Le nom d'une fonction suit les mêmes règles que pour les noms de variables:

- des lettres,
- des chiffres (sauf pour le premier caractère)
- le tiret bas `_`
- les mots-cés (`if`, `else`) sont exclus

La première ligne de définition de la fonction (signature) est suivi d'un bloc d'instructions qui doit être indenté.
Ce sont les instructions qui seront exécutés à chaque appel de la fonction.
Lors de la définition, ces instructions ne sont pas encore exécuté.

Donc, si une fonction est définie mais jamais appelé, ces lignes de code ne seront jamais exécutés.

```{codeplay}
def ma_fonction(arg1, arg2):
    resultat = 1
    for i in range(arg2):
        resultat = resultat * arg1
    return resultat

print(ma_fonction(3, 5))
```

## Valeur de retour

L'instruction `return` permet de _retourner_ une valeur calculée par la fonction et d'ainsi déterminer quelle est son résultat — ce qu'on appelle sa _valeur de retour_.

Toutes les fonctions ne doivent pas forcément retourner une valeur. Comme le premier exemple le montre, une fonction pourrait se contenter de faire quelques `print` sans calculer un résultat donné. Dans ce cas, lorsqu'il n'y a pas de valeur à retourner, on n'a pas besoin du mot clé `return`.

<!--- (ensuite, même avec cette reformulation, je pense qu'il faudrait un exemple pour montrer que 'return' cause l'arrêt de l'exécution du reste du code de la fonction, qui est aussi un point sur lequel les élèves se plantent facilement) -->

L'exemple suivant définit une fonction pour calculer la vitesse à partir de la distance parcourue et le temps utilisé.

```{codeplay}
def vitesse(distance, temps):
    v = distance / temps
    return v

print(vitesse(12, 3), "km/h")
print(vitesse(3, 12), "km/h")
```

Il est possible d'utiliser plusieurs arguments dans une fonction en les séparant par une virgule. L'ordre des arguments doit être respecté; ainsi, `vitesse(12, 3)` ne retournera pas la même valeur que `vitesse(3, 12)`: l'un calcule la vitesse nécessaire pour parcourir 12 kilomètres en 3 heures, alors que l'autre calcule la vitesse nécessaire pour parcourir 3 kilomètres en 12 heures.

**Exercice:** Calculez la vitesse d'une voiture qui fait la distance Lausanne-Genève (65 km) en 45 minutes.

## Exercices

### Exercice 1 - Pythagore

Définissez une fonction `pythagore` qui calcule l'hypotenuse d'un triangle rectanlge à partir de ses deux cotés.

La racine carrée peut s'obtenir avec la puissance 0.5.

```{codeplay}
def pythagore(a, b):

print(pythagore(3, 4))
````

### Exercice 2 - eq. quadratique

Faites un programme qui demande à l'utilisateur les coefficients **a, b** et **c** d'une fonction du deuxième degré et qui retourne les solutions de l'équation $ax^2 + bx + d = 0$.

```{codeplay}
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

print('Voici votre équation:')
print(a, 'x^2 +', b, 'x +', c, '= 0')
print()
print('La solution est ...')
```

Afin de pouvoir réutiliser ce calcul dans plusieurs programmes, nous allons créer une fonction `solutions_eq2` acceptant 3 arguments (a, b et c).

**Rappel:**.  
Si le discriminant $\Delta = b^2 - 4ac$ est

- négatif: il n'y a pas de solution,
- nul: il y a qu'une seule solution,
- positif: il y a deux solutions.

```{codeplay}
def solutions_eq2(a, b, c):

print(solutions_equ2(1, 2, 3))
print(solutions_equ2(2, -1, 2))
```

Calculez par exemple les solutions de

- $x^2 + 2x + 3 = 0$
- $2x^2 - x + 2 = 0$
- ou d'une autre équation quadratique
