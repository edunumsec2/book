# Ecrire

Un programme informatique peut manipulier ces différents catégories d'objets :

- image
- texte
- nombre

Les activités, ou verbes, qui y sont associés sont : 

- dessiner
- écrire
- calculer

Dans ce chapitre nous explorons ce que c'est le texte, et comment un programme peut écrire.

## Dire bonjour

Nous commençons par le grand classique des livres d'introduction à la programmation.

```{codeplay}
print('hello world.')
```

**Exercice** : Affichez des lignes de texte supplémentaires.

## Délimiter un texte

Toute caractère imprimable peux être utilisé pour créer un texte :

- lettres (`a...z` et `A...Z`)
- chiffres (`0...9`)
- ponctuations (`.,;:?!`)
- parenthèses (`[]{}<>`)
- symboles (`$*#...`)

Pour différencier un morceau de texte du reste d'un programme, il doit être délimité par des symboles spéciaux qui sont : 

- apostrophe (`'`)
- guillemets doubles (`"`)
- trois guillemets (`"""`)

```{codeplay}
print('apostrophe')
print("guillemets doubles")
print("""
Délimité avec trois guillements, 
le texte peut s'étaler sur plusieurs lignes.
""")
```
**Exercice** : Ajoutez du texte sur les deux lignes qui contienntent  `"""`.

## Répéter un texte

L'opérateur `*` permet de répéter un texte composé d'un ou de plusiers caractères.

```{codeplay}
print('ha' * 10)
print('=' * 20)
print('hello ' * 3)
```
**Exercice** : Répétez une chaines plus longue.


## Concaténer un texte

Le mot **concaténer** veut dire enchaîner ou coller ensemble.

L'opérateur `+` permet de concatener deux chaînes de texte. 
Mais juxaposer deux chaines de texte et les séparer par zéro ou plusieurs espaces va aussi concatener la chaîne.

```{codeplay}
print('bon'    'jour')
print('bon''jour')
print('bon' + 'jour')
```

## La longuer d'une chaine

La fonction `len()` retourne la longuer d'une chaine.
La chaine vide (`""`) a une longeur de 0.

```{codeplay}
print(len('bonjour'))
print(len(""))
print(len("""
Délimité avec trois guillements, 
le texte peut s'étaler sur plusieurs lignes.
"""))
```

**Exercice** : Ajoutez quelques caractères et re-exécutez le code.

Pour savoir combien de fois il faut répéter un symbole, pour obtenir la même longuer qu'un texte donné,  nous pouvons utiliser la fonction `len()` et ainsi créer des lignes qui ont la même longueur qu'un texte.

```{codeplay}
x = 'Python peux manipuler du texte'
print('=' * len(x))
print(x)
print('=' * len(x))
```

## L'art ASCII

L’**art ASCII** consiste à réaliser des images uniquement à l'aide des lettres et caractères spéciaux contenus dans le code ASCII.

Voici un exemple :

![](ascii-art.jpeg)

```{codeplay}
print("""
         ((`\ 
      ___ \\ '--._
   .'`   `'    o  )
  /    \   '. __.'
 _|    /_  \ \_\_
{_\______\-'\__\_\
""")

```
**Exercice** : Le site https://www.asciiart.eu contient beaucoup d'exemples d'art ASCII. Trouvez-en un et copiez-le dans un programme Python.

## Echapper un caractère

Les sybmoles `'` et `"` sont utilisés pour délimiter du texte. 
Si nous voulons utiliser ces caractères à l'intérieur, nous devons les échapper avec une barre oblique en arrière `\`.

```{codeplay}
print('c\'est bien')
print("\"citation\"")
```

Si nous voulons imprimer le symbole d'échappement, nous devons l'échapper également.

```{codeplay}
print('c\'est la \\barre oblique\\ en arière.')
```

## Retour à la ligne

Chaque commande `print()` termine avec un retour à la ligne.
Pour insérer un retour à la ligne à l'intéreur d'une chaîne de caractères nous utilisons la séquences d'échappement `\n` (newline).

```{codeplay}
print('chaque\nmot\nsur\nune\nligne')
```

**Exercice** : Ajoutez une deuxième ligne de code qui contient des `\n`.

## Aligner en colonnes

La séquence `\t` (tabulateur) permet d'aligner des éléments de texte en colonne. Les colonnes sont espacées de 8 caractères.

```{codeplay}
print('qte\tart.\tprix')
print('1\tsouris\t15.95')
print('12\tclavier\t25.95')
```

## Le code ASCII

La fonction `ord(c)` retourne le code ASCII qui est associé au caractère `c`. 

```{codeplay}
print('A', ord('A'))
print('B', ord('B'))
print('a', ord('a'))
```

Nous constatons que : 

- le code ASCII pour la lettre A est 65
- les codes suivent l'ordre de l'alphabet
- les codes des minuscules ont un écart de 32 par rapport au code des majuscules

```{codeplay}
for c in 'Python':
    print(c, ord(c))
```

## Les commentaires

Un commentaire en Python est un bout de code qui est ignoré par Python.
Un commentaire commence par le symole hashtag (`#`).

Les commentaires sont utilisés pour ajouter à un programme des informations supplémentaires :

- explications
- nom de l'auteur
- revisons

Parfois un commentaire est utilisé pour desactiver une ligne de code.
La pluspart des éditeurs marquent les commentaires en couleur grisée.

```{codeplay}
# commentaire sur une ligne

print('bonjour')  # commentaire en fin de ligne
print("# ceci n'est pas un commentaire")
# print('au revoir')

"""
Ceci est 
un long commentaire
sur plusieur lignes.
"""
```

**Exercice** : Enlever le # devant `print('au revoir')` pour l'exécuter.

## La fonction `write()`

Dans le module `turtle` nous avons fonction `write()` qui permet d'afficher du texte à l'intérieur d'un dessin. Cette fonction permet de spécifier la police sous forme de tuple (police, taille).

```{codeplay}
from turtle import *

left(90)
write('texte par défaut')

fillcolor('red')
forward(30)
write('Courier 24', font=('Courier', 24))

fillcolor('blue')
forward(40)
write('Arial 36', font=('Arial', 36))
```

```{codeplay}

```

