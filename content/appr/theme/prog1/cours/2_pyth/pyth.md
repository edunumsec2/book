# 1. Débuter avec Python

Python est un langage de programmation populaire. 
Il a été créé par un scientifique néerlandais, Guido van Rossum, en 1991.
Le nom fait référence au fameux groupe d'humoristes anglais, les *Monty Python*.

![Monty phyton](https://media.giphy.com/media/RzKHvdYC3uds4/giphy.gif)  
John Cleese des Monty Python dans le sketch *Ministery of Silly Walks*

Un langage de programmation permet à un humain de décrire ce que doit faire un ordinateur.
Tous les ordinateurs, smartphones et sites web fonctionnent grâce à des programmes, encore appelés logiciels.

Le langage Python, comme la plupart des langages de programmation, est basé sur l'anglais. 

Pourquoi choisir ici Python?

- Python est multiplateforme (Windows, Mac, Linux),
- Python a une syntaxe simple et visuelle,
- Python est interprété et donne un résultat immédiat,
- Python est "souple" s'agissant du {glo}`typage|typage` - cet avantage s'agissant 
d'un langage tourné vers le monde éducatif peut toutefois s'avérer pénalisant dans un contexte de production.

## Qu'est un programme ?
Un **programme** est une séquence d'instructions pour faire faire quelque chose par un ordinateur. Par exemple :

- exécuter un calcul mathématique,
- trier une liste de mots,
- résoudre une équation.

En général, un langage de programmation intègre tout ou partie de ces aspects :

- des entrées (au clavier, via un fichier),
- une sortie (à l'écran, sur un fichier),
- des opérations au sens large : mathématiques ou manipulations,
- des structures conditionnelles (if-else),
- des structures itératives (boucles for, while).

## Le premier programme

Nous allons nous lancer tout de suite dans la programmation, avec un programme minimaliste d'une seule ligne. 

```{codeplay}
print('bonjour')
```

Ce premier programme afficher le mot *bonjour* sur console.

Le programme consiste en :

- une fonction `print` qui affiche son argument, <!-- REVIEW/JPP: on ne sait pas à ce stade ce qu'est un argument, il faudrait pouvoir le définir -->
- des parenthèses `()` qui entourent l'argument,
- des guillemets `'...'` qui délimitent une <span commented>chaîne de caractère,</span><!-- REVIEW/JPP: une chaîne de caractères, ou du texte -->
- du texte (chaine de caractères), `bonjour`, qui est délimité par des guillemets.

## L'éditeur (IDE)

Pour éditer et exécuter du code Python, il faut un éditeur. 
Ce peut être Visual Studio Code, Pycharm, VIM ou encore Wing IDE. 
On se propose ici de décrire sommairement l'éditeur **Thonny** qui est un outil pratique pour débuter. 
C'est un **EDI (IDE en anglais)**, un environnement de développement intégré. 
Cela signifie qu'il contient :

- un éditeur de script,
- un interpréteur Python.

Les IDE présentent souvent trois régions dans leur fenêtre:

- une barre d'outils (Nouveau, Ouvrir, Exécuter...),
- l'éditeur de script,
- la console.

![Thonny](img/thonny.png)

Dans l'éditeur de script, on peut écrire des programmes complexes contenant des centaines de lignes. 
Après avoir été sauvegardé, le script sera exécuté avec un clic sur le bouton vert **Exécuter**.

La console permet de rapidement exécuter et tester des expressions de façon interactive. 
On écrit la commande Python sur la ligne avec l'invite `>>>` et on exécute avec la touche **Retour**.

Le résultat apparaît sur la ligne suivante, et une nouvelle invite `>>>` est affichée.

+++

## Opérations arithmétiques
Nous avons découvert une commande simple qui affiche un bout de texte dans la zone de résultat.
Avec la plupart des langages de programmation, on manipule aussi facilement des nombres.
Voyons comment, en Python, on effectue les opérations arithmétiques de base comme l'addition, la soustraction, la division et la multiplication.

```{codeplay}
print(123 + 456)
```

Voici une multiplication:

```{codeplay}
print('123 * 456')
print(123 * 456)
```

La division utilise l'opérateur `/` et retourne un <span commented>nombre à virgule flottante</span><!-- REVIEW/JPP: ils ne savent pas ce que c'est --> comme résultat.

**NOTE** : en Python, comme dans la plupart des langages de programmation, quand on indique un nombre à virgule, on sépare par un point et non par une virgule la partie entière de la partie décimale. 

```{codeplay}
print('123 / 456 =', 123/456)
```

Dans une expression complexe, on peut indiquer l'ordre d'exécution avec des parenthèses. Sans cela, les opérations sont effectuées selon la priorité des opérateurs, qui correspond en général à l'idée qu'on s'en ferait en utilisant ce que l'on connaît de l'algèbre. Par exemple, ici, la multiplication est effectuée avant l'addition.

```{codeplay}
print(2 + 3 * 4)
print((2 + 3) * 4)
```

Ici, l'addition est effectuée en premier grâce aux parenthèses.

La mise à la puissance (aussi appelée _exponentiation_) utilise l'opérateur `**`. 
Cet exemple calcule donc $123^{456}$ !

```{codeplay}
print(123 ** 456)
```

Ceci montre que les résultats des calculs en nombres entiers en Python 
ne sont pas limités en termes de nombres de chiffres nécessaires à la représentation de ces entiers: 
le nombre ci-dessus, par exemple, s'écrit avec 953 chiffres.


## La fonction print()

La fonction `print()` affiche (imprime) vers la console ce qui se trouve entre les parenthèses. 

```{codeplay}
print(12 + 34)
print(12 / 34)
print(12 * 34)
```

La fonction `print()` peut aussi afficher du texte.

```{codeplay}
print('bonjour')
print("au revoir")
```

En programmation, un tel morceau de texte s'appelle _chaîne de caractères_. 
En Python, on peut indiquer une chaîne de caractères aussi bien avec les guillemets anglais simples (`'...'`, aussi appelés apostrophes) que les guillemets anglais doubles (`"..."`).

On utilise les guillemets simples quand la chaîne contient des guillemets doubles.
On utilise les guillemets doubles quand la chaîne contient des guillemets simples ou des apostrophes.

```{codeplay}
print('le langage "Python" est puissant')
print("c'est intéressant")
```

Que faire si une chaîne contient à la fois des apostrophes et des guillemets doubles?

Si la chaîne est délimitée par des guillemets simples, il faut utiliser le symbole d'échappement `\` (la barre oblique inversée, aussi appelée _backslash_) devant une apostrophe qui apparait à l'intérieur.

```{codeplay}
print('c\'est "très" cool')
print("c'est \"très\" cool")
```

Si une sous-partie du texte est délimitée par des guillemets doubles, il faut utiliser le symbole d'échappement `\` devant ces guillemets.

Lorsqu'il est utilisé avec du texte, l'opérateur `+` crée une nouvelle chaîne de caractères formée à partir des deux chaînes indiquées — une opération appelée _concaténation_.

```{codeplay}
print('bon' + 'jour')
print('ha' * 10)
print('*' * 30)
```

L'opérateur `*` permet de répéter une chaîne.

Les nombres peuvent être représentés comme chaîne de caractères:

```{codeplay}
print('12' + '12')
print(12 + 12)
print('12 + 12')
```
Une opération mathématique représentée comme chaîne n'est pas exécutée. Elle est retournée telle quelle : en effet, le caractère `+` est inclus à l'intérieur des guillemets et il est considéré comme faisant partie de ce texte plutôt que comme étant l'opérateur `+` représentant l'addition en Python.

Les deux nombres (représentés sous forme de chaînes) sont concaténés et non pas additionnés.

Ce nombre (représenté sous forme de chaîne) est répété et non pas multiplié.

```{codeplay}
print('12' * 12)
print(12 * 12)
print('12 * 12')
```

## Commentaire

Un commentaire commence par un dièse (`#`) et se termine naturellement à la fin d'une ligne. Il permet de documenter un programme et n'est pas interprété comme du code.

```{codeplay}
# ceci est un commentaire
print('bonjour')
# print('bonsoir')
```

Le symbole `#` peut être utilisé pour signaler à la machine une instruction à ne pas exécuter. 

Un commentaire peut aussi être placé après une instruction pour donner une explication supplémentaire.

```{codeplay}
print('bonjour') # utilisé le matin
print('bonsoir') # utilisé le soir
```

*Les exercices suivants sont à faire après avoir installé l'IDE de votre choix.*


````{admonition} Exercice 1 : première impression ... 🔌
:class: note
<!-- <span style="color:green">Niveau débutant</span> -->

Programmez une instruction qui vous demande, puis affiche votre âge.

````

````{admonition} Exercice 2 : ... deuxième impression ! 🔌
:class: note
<!-- <span style="color:green">Niveau débutant</span> -->

Écrivez un programme qui affiche les phrases suivantes:

    Le soleil brille à nouveau sur townsville.
    Toi t'es vraiment sympa!
    C'est un type "chelou", disait-il.

````

````{admonition} Exercice 3 : multiplication 🔌
:class: note
<!-- <span style="color:green">Niveau débutant</span> -->

Trouvez et programmez l'expression qui calcule le résultat de 4321 multiplié par 1234.

````

````{admonition} Exercice 4 : moyenne 🔌
:class: note
<!-- <span style="color:orange">Niveau intermédiaire</span> -->

Trouvez et programmez une expression qui calcule la moyenne des 5 notes suivantes : 4.5, 3.5, 6, 5 et 4.

````

````{admonition} Exercice 5 : surface 🔌
:class: note
<!-- <span style="color:orange">Niveau intermédiaire</span> -->

Trouvez et programmez une expression qui calcule la surface d'un carré de 9 cm de côté sans utiliser `9 * 9`.

````

````{admonition} Exercice 6 : chaîne 🔌
:class: note
<!-- <span style="color:red">Niveau avancé</span> -->

Trouvez et programmez une instruction qui renvoie la longueur de la chaîne `"anticonstitutionnellement"`.
````
