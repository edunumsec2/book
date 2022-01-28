# Ecrire - `str`

Dans ce chapitre nous allons nous intéresser au texte. Le texte est une catégorie d'information qui est essentiel dans beaucoup de programmes, tel qu'une application de messagerie ou un programme de traitement de texte.

<!-- ![text-based](media/text_game.jpg)

```{admonition} Le saviez-vous ?
:class: hint
Les tout premiers jeux vidéos sur ordinateur utilisaient presque exclusivement du texte, et quelques dessins en ASCII art, pour plonger le joueur dans un univers d'aventure et de découvertes. Dans l'image ci-dessus, le texte dit "Vous êtes maintenant à la fin d'une route, en face d'un petit bâtiment en briques. Autour de vous il y a une forêt. Un ruisseau sort du bâtiment et s'écoule dans une rigole. - *Entrer dans le bâtiment*. Vous êtes à l'intérieur du bâtiment (...)"
Ce qui est intéressant ici, c'est que c'est le joueur qui a dû trouver la commande lui permettant de réaliser une action qui l'a fait avancer dans le jeu. "Colossal Cave Adventure", dont l'extrait est issu, est un jeu de 1975, qui a fasciné une génération entière d'informaticiens qui ont cherché à résoudre les énigmes posées par le jeu pour arriver au bout de l'aventure. Aujourd'hui, il existe de nombreux outils en ligne vous permettant d'écrire des histoires interactives où vos lecteurs peuvent prendre des décisions sur la suite de l'aventure. 
``` 
-->

Techniquement un texte est appelé une **chaîne de caractères**, ou string en anglais (`str`). Nous allons voir que :

- un texte est délimité par une apostrophe `'` ou un guillemet double `"`,
- l'opérateur `*` répète un texte,
- la fonction `ord(c)` retourne le code pour représenter un caractère.

```{question}
Un string informatique est

{f}`un sous-vêtement pour informaticien`  
{f}`une ficelle de données`  
{v}`un enchaînement de lettres`  
{f}`un instrument de musique`
```

## Délimiter un texte

Tout caractère imprimable peux être utilisé pour créer un texte :

- lettres (`a...z` et `A...Z`)
- chiffres (`0...9`)
- ponctuations (`.,;:?!`)
- parenthèses (`[]{}<>`)
- symboles (`$*#...`)

Pour différencier un morceau de texte du reste d'un programme, il doit être délimité par des symboles spéciaux qui sont :

- apostrophe (`'`)
- guillemets doubles (`"`)
- trois guillemets doubles (`"""`)

```{codeplay}
:file: str1.py
print('apostrophe')
print("guillemets doubles")
print("""
Délimité avec trois guillements, 
le texte peut s'étaler sur plusieurs lignes.
""")
```

**Exercice** : Ajoutez des lignes supplémentaires au texte qui est délimité par `"""`.

## Répéter un texte

L'opérateur `*` permet de répéter un texte composé d'un ou de plusieurs caractères.

```{codeplay}
:file: str2.py
print('ha' * 10)
print('=' * 20)
print('hello ' * 3)
```

**Exercice** : Répétez une chaîne plus longue.

## Concaténer un texte

Le mot **concaténer** veut dire enchaîner ou coller ensemble.

L'opérateur `+` permet de concaténer deux chaînes de texte.
Mais juxtaposer deux chaînes de texte et les séparer par zéro ou plusieurs espaces va aussi concaténer la chaîne.

```{codeplay}
:file: str3.py
print('bon'    'jour')
print('bon''jour')
print('bon' + 'jour')
```

## La longueur d'une chaîne

La fonction `len()` retourne la longueur d'une chaîne.
La chaîne vide (`""`) a une longueur de 0.

```{codeplay}
:file: str4.py
print(len('bonjour'))
print(len(""))
print(len("""
Délimité avec trois guillements, 
le texte peut s'étaler sur plusieurs lignes.
"""))
```

**Exercice** : Ajoutez quelques caractères et re-exécutez le code.

Pour savoir combien de fois il faut répéter un symbole dans le but d'obtenir la même longueur qu'un texte donné, nous pouvons utiliser la fonction `len()` et ainsi créer des lignes qui ont la même longueur qu'un texte.

```{codeplay}
:file: str5.py
x = input('Entrez une phrase: ')
print('=' * len(x))
print(x)
print('=' * len(x))
```

**Exercice** : Entourez votre texte d'un autre symbole.

## Le code ASCII

Le code ASCII  (American Standard Code for Information Interchange) était un des premiers standards utilisé pour représenter des symboles dans un ordinateur. Avec initialement 7 et plus tard 8 bits il désigne un ensemble de lettres, chiffres, symboles et ponctuations.

Aujourd'hui le standard Unicode permet d'encoder la totalité des symboles utilisés dans les différents langages du monde.

La fonction `ord(c)` retourne le code ASCII (Unicode) qui est associé au caractère `c`.

```{codeplay}
:file: str6.py
print('A =', ord('A'))
print('B =', ord('B'))
print('a =', ord('a'))
```

Nous constatons que :

- le code ASCII pour la lettre A est 65,
- les codes suivent l'ordre de l'alphabet,
- les codes des minuscules ont un écart de 32 par rapport au code des majuscules.

```{codeplay}
:file: str7.py
for c in 'Python':
    print(c, '=', ord(c))
```

La fonction `chr(i)` retourne le caractère qui correspond au code `i`.

```{codeplay}
:file: str8.py
for i in range(65, 75):
    print(i, '=', chr(i))
```

## L'art ASCII

L’**art ASCII** consiste à réaliser des images uniquement à l'aide des lettres et caractères spéciaux contenus dans le code ASCII.

Précéder la chaîne de caractères avec `r` permet de ne pas tenir compte des symboles d'échappement (barre oblique en arrière `\`).

Voici un exemple :

![rabbit](media/ascii-art.jpeg)

```{codeplay}
:file: str9.py
print(r"""
         ((`\ 
      ___ \\ '--._
   .'`   `'    o  )
  /    \   '. __.'
 _|    /_  \ \_\_
{_\______\-'\__\_\
""")

```

**Exercice** : Le site [asciiart.eu](https://www.asciiart.eu) contient beaucoup d'exemples d'art ASCII. Trouvez-en un et copiez-le dans un programme Python.

## Echapper un caractère

Les symboles `'` et `"` sont utilisés pour délimiter du texte.
Si nous voulons utiliser ces caractères à l'intérieur de la chaîne, nous devons les échapper avec une barre oblique en arrière `\`.

```{codeplay}
:file: str10.py
print('c\'est bien')
print("\"citation\"")
```

Si nous voulons imprimer le symbole d'échappement, nous devons l'échapper également.

```{codeplay}
:file: str11.py
print('c\'est la \\barre oblique\\ en arière.')
```

## Une chaîne brute

Les chaînes de texte peuvent être préfixées par la lettre `r`; de telles chaînes sont appelées chaines brutes (raw strings en anglais) et traitent la barre oblique inversée comme un caractère normal.

```{codeplay}
:file: str12.py
print(r'c\'est bien')
print(r"\"citation\"")
print(r'c\'est la \\barre oblique\\ en arière.')
```

## Retour à la ligne

Chaque commande `print()` se termine avec un retour à la ligne.
Pour insérer un retour à la ligne à l'intérieur d'une chaîne de caractères nous utilisons la séquences d'échappement `\n` (newline).

```{codeplay}
:file: str13.py
print('chaque\nmot\nsur\nune\nligne')
print('\nhello world' * 5)
```

**Exercice** : Ajoutez une nouvelle ligne de code qui contient des `\n`.

## Aligner en colonnes

La séquence `\t` (tabulateur) permet d'aligner des éléments de texte en colonne. Les colonnes sont espacées de 8 caractères.

```{codeplay}
:file: str14.py
print('qte\tart.\tprix')
print('4\tsouris\t15.95')
print('12\tclavier\t25.95')
```

## Les émojis

Un  émoji (絵文字), est un terme issu du japonais pour désigner les pictogrammes utilisés dans les messages électroniques et les pages web japonaises, qui se sont répandus dans le monde entier.

Le mot emoji signifie littéralement « image » (e) + « lettre » (moji) ; la ressemblance avec « émotion » est un jeu de mot interculturel.

Un émoji peut être utilisée comme un caractère à l'intérieur d'un texte.
Nous pouvons le répéter avec l'opérateur `*` et obtenir son code **Unicode** avec la fonction `ord(c)`.

```{codeplay}
:file: str15.py
print('😀' * 10)

print(ord('🍎'))
print(ord('😀'))
```

Avec la fonction `chr(i)` nous pouvons afficher les 10 caractères qui suivent l'émoji de pomme.

```{codeplay}
:file: str16.py
for i in range(10):
    print(chr(i + 127822))
```

**Exercice** : Affichez les 10 emojis qui suivent 😀.

```{warning}
Utiliser des émojis dans Thonny ne fonctionne pas. Ceci fait planter Thonny !  
Le module graphique utilisé actuellement (Tk 8.6.8) ne supporte pas des émojis.
Ce bug sera corrigé avec Thonny 4.0 qui utilisera la version Tk 8.6.12.
```

Vous pouvez utilisez dans Thonny sans problème les anciens pictogrammes en noir et blanc. Voici les codes Unicode de 
[symboles divers](https://fr.wikipedia.org/wiki/Table_des_caractères_Unicode_(2000-2FFF)#Symboles_divers).

```{codeplay}
:file: str17.py
c = '☀'
print(c)

for i in range(20):
    print(chr(0x2660 + i), end=' ')
```

## Les kanji

Le japonais est écrit avec des pictogrammes qui s'appellent des kanjis.
Avec la fonction `ord(c)` nous pouvons obtenir leur **Unicode**.

```{codeplay}
:file: str18.py
print('日本語')
print('nihongo')
print('japonais\n')

for c in  '日本語': 
    print(c, ord(c))
```

Avec la fonction `chr(i)` nous pouvons afficher les 10 kanjis qui suivent le kanji 日 qui signifie soleil. Si vous regardez bien, vous remarquez qu'ils contiennent tous le radical pour soleil.

```{codeplay}
:file: str19.py
n = ord('日')
for i in  range(n, n + 10): 
    print(i, chr(i))
```

**Exercice** : Affichez les 10 kanjis qui suivent 語 (langage).

## Les commentaires

En Python, un commentaire est un bout de code qui est ignoré par Python.
Un commentaire commence par le symbole hashtag (`#`).

Les commentaires sont utilisés pour ajouter à un programme des informations supplémentaires :

- explications,
- nom de l'auteur,
- révision.

Parfois un commentaire est utilisé pour désactiver une ligne de code.
La plupart des éditeurs marquent les commentaires en couleur grisée.

```{codeplay}
:file: str20.py
# commentaire sur une ligne

print('bonjour')  # commentaire en fin de ligne
print("# ceci n'est pas un commentaire")
# print('au revoir')

"""
Ceci est 
un long commentaire
sur plusieurs lignes.
"""
```

**Exercice** : Enlever le # devant `print('au revoir')` pour l'exécuter.

## La fonction `write()`

Dans le module `turtle` nous avons la fonction `write()` qui permet d'afficher du texte à l'intérieur d'un dessin. Cette fonction permet de spécifier la police sous forme de paire (police, taille).

```{codeplay}
:file: str21.py
from turtle import *

up()
left(90)
write('texte par défaut')

color('red')
forward(30)
write('Courier 24', font=('Courier', 24))

color('blue')
forward(40)
write('Arial 36', font=('Arial', 36))
hideturtle()
```

**Exercice** : Essayez d'autres tailles et polices.
