# Directives

Les directives sont des appels de fonctions Sphinx qui permettent d'afficher un contenu spécifique (images, tableaux, encarts, etc.).

## Directives Sphinx

Les directives Sphinx suivantes sont les plus communément utilisées dans les ressources Modulo :

- [Image](https://docutils.sourceforge.io/docs/ref/rst/directives.html#image)
- [Figure](https://docutils.sourceforge.io/docs/ref/rst/directives.html#figure)
- [Table](https://docutils.sourceforge.io/docs/ref/rst/directives.html#table)

_Liste complète des directives Sphinx : https://docutils.sourceforge.io/docs/ref/rst/directives.html_.

## Directives Modulo

Les directives suivantes ont été créées sur mesure pour le projet Modulo.

### Blank

Pour ajouter des *blancs* dans le texte, il suffit d'utiliser le rôle `bl`.
Dans le texte du rôle, les différentes options de réponses sont séparées par un caractère `|`.
Une réponse valable est précédée d'un caractère `>`.

```{code-block} text
Dans le texte suivant, certains {bl}`>mots|trucs|machins` sont laissés {bl}`pour compte|>blancs|verts|seuls`.
```

### Codeplay
Cette directive permet d'ajouter un interpréteur Python dans le contenu.

Il est possible d'insérer un interpréteur Python et éditeur directement dans le document, le tout implémenté en Javascript et qui tourne dans le client Web du visiteur.
Pour ceci, il suffit d'utiliser la directive `codeplay`.

`````{tabbed} Aperçu
```{codeplay}
def double(x):
    return x + x

print(double(int(input("x = "))))
```
`````

#### Options

##### Noms de fichier

L'option `:file:`permet de définir le nom du fichier .py qui pourra être téléchargé depuis le codeplay en ligne. 

`````{tabbed} Aperçu
```{codeplay}
:file: puissance.py
def puissance(x, y):
    return x ** y

print(puissance(2, 10))
```
`````

##### Execution immediate

Via l'option `:exec:`, le code est exécuté dès le chargement de la page.

`````{tabbed} Aperçu
```{codeplay}
:exec:
def puissance(x, y):
    return x ** y

print(puissance(2, 10))
```
`````

##### Code statique

Via l'option `:static:`, l'éditeur est mis en mode lecture seule.

`````{tabbed} Aperçu
```{codeplay}
:static:
def puissance(x, y):
    return x ** y

print(puissance(2, 10))
```
`````

##### Cacher les boutons de contrôle

Via l'options `:nocontrols:` les boutons de contrôle sont cachés.
Le code peut tout de même être lancé via les raccourcis claviers, ainsi qu'initialement via le bouton affiché dans le texte dans la zone de sortie.

`````{tabbed} Aperçu
```{codeplay}
:nocontrols:
def puissance(x, y):
    return x ** y

print(puissance(2, 10))
```
`````

#### Prélude

Par défaut toutes les lignes apparaissant avant la première ligne formée uniquement d'au moins 3 caractères `=` (ignorant les caractères d'espaces avant et après sur la ligne) est considéré comme un préambule qui n'est pas affiché aux utilisateurs du site mais qui est tout de même exécuté.

`````{tabbed} Aperçu
```{codeplay}
def puissance(x, y):
    return x ** y
===
print(puissance(2, 10))
```
`````

De même, lorsqu'au deux délimitations sont faites, seule la seconde est affichée.
L'ordre d'exécution est préservé.

`````{tabbed} Aperçu
```{codeplay}
def test(condition, erreur):
     if not condition:
        print(erreur)
===
def puissance(n, m):
    pass
===
test(puissance(2, 3) == 8, "Oups, ton implémentation est incorrecte.")
```
`````

Pour désactiver cette fonctionnalité, l'option `:noprelude:` peut être spécifiée.

#### Indices

`````{tabbed} Aperçu
```{codeplay}
---
hints: |
    Rappelle toi de l'opérateur `**`!
    ===
    Toujours pas?
---

def test(condition, erreur):
     if not condition:
        print(erreur)
===
def puissance(n, m):
    pass
===
test(puissance(2, 3) == 8, "Oups, ton implémentation est incorrecte.")
```
`````


#### Librairies

##### Turtle

```{codeplay}
from turtle import *
up()
forward(-100)
down()
speed(10)
color('red', 'yellow')
begin_fill()
for i in range(9):
    forward(200)
    left(160)
end_fill()
done()
```

### Gallery

-> Documenter et tester

### Glossary

Syntaxe pour une référence à un mot du glossaire:

````{code-block} text
{glo}`economieattention|L'économie d'attention` présente...
Cette {glo}`economieattention@1|économie d'attention`...
````

Pour insérer la définition dans son propre encart:

````{code-block} text
```{definition} economieattention@1
```
````

### Logic

Pour le fonctionnement du simulateur logique, regarder la documentation ci-contre : https://enseigner.modulo-info.ch/archi/activ/simulateur.html

### Questions

Il est possible d'intégrer des questions à choix multiples au fil des pages via la directive `question`.
Dans le corps de la directive, les bonnes et mauvaises réponses sont indiquées via les rôles `{v}` et `{f}` pour *vrai* et *faux*.

`````{tabbed} Aperçu

```{question}
Combien y a t'il de bits dans un octet ?
Je pense qu'il y en a {f}`2`, {f}`4`, {v}`8` ou {f}`64`.
```
`````

Il est possible de changer le titre affiché au dessus de la question.
Le contenu de la question peut lui-même être structuré en text.
Dans l'exemple ci-dessous, les réponses sont affichées dans une liste.

`````{tabbed} Aperçu

```{question} Question avec un titre personnalisé
Parmi les informaticiens et informaticiennes suivants, qui a reçu le prix Turing ?
* {v}`Barbara Liskov`
* {v}`Niklaus Wirth`
* {f}`Alan Turing`
* {v}`Tim Berners-Lee`
```
`````

### Options

Par défaut, si il y a uniquement une réponse correcte, les autres réponses se désélectionnent automatiquement.
Pour que plusieurs réponses puissent être sélectionnées même s'il n'y a qu'une seule réponse, l'option `:multi:` peut être ajoutée.

`````{tabbed} Aperçu

```{question}
:multi: 
Parmi les personnes suivantes, laquelle ou lesquelles sont à l'origine du Web ?
* {f}`Barbara Liskov`
* {f}`Niklaus Wirth`
* {f}`Alan Turing`
* {v}`Tim Berners-Lee`
```
`````

### Videos

#### Vidéos YouTube

Pour ajouter une vidéo YouTube directement dans le document, utiliser la directive `youtube`.
La directive attend en argument l'identifiant de la vidéo (généralement 11 caractères au format `base64url`).
L'identifiant d'une vidéo YouTube peut être trouvé dans l'URL de la video, juste après la chaîne `?v=`.
Par exemple, l'identifiant de la vidéo à l'URL `https://www.youtube.com/watch?v=dQw4w9WgXcQ` est `dQw4w9WgXcQ`.

`````{tabbed} Aperçu
```{youtube} uHKfrz65KSU
```
`````

##### Options

###### Départ de la lecture

Par défaut, la lecture commence au début de la vidéo.
Via l'option `:start:`, il est possible de faire commencer la lecture à un endroit différent de la vidéo.
L'option `:start:` attend en argument un nombre entier qui indique la seconde à laquelle la lecture doit commencer.

`````{tabbed} Aperçu
```{youtube} _OBlgSz8sSM
:start: 18
```
`````

###### Contrôles

Par défaut, les boutons de contrôle de la vidéo sont affichés dans une barre en bas de la vidéo.
Ils peuvent cependant être cachés via l'option `:nocontrols:`.

`````{tabbed} Aperçu
```{youtube} wGGqWwVb3sU
:nocontrols:
```
`````

#### Vidéos SwitchTube

Pour ajouter une vidéo hébergée sur SwitchTube directement dans le document, utiliser la directive `switchtube`.
La directive attend en argument l'identifiant de la vidéo (généralement une suite de caractères au format `base64url`).
L'identifiant d'une vidéo SwitchTube peut être trouvé à la fin de l'URL de la video.
Par exemple, l'identifiant de la vidéo à l'URL `https://tube.switch.ch/videos/f6365946` est `f6365946`.

`````{tabbed} Aperçu
```{switchtube} f6365946
```
`````

##### Options

###### Départ de la lecture

Par défaut, la lecture commence au début de la vidéo.
Via l'option `:start:`, il est possible de faire commencer la lecture à un endroit différent de la vidéo.
L'option `:start:` attend en argument un nombre entier qui indique la seconde à laquelle la lecture doit commencer.

`````{tabbed} Aperçu
```{switchtube} f6365946
:start: 122
```
`````

###### Cacher le titre

Il est possible d'ajouter l'option `:notitle` pour cacher le titre de la vidéo dans le lecteur.

`````{tabbed} Aperçu
```{switchtube} f6365946
:notitle:
```
`````

#### Vidéos du CNRS

Pour ajouter une vidéo du CNRS directement dans le document, utiliser la directive `cnrs`.
La directive attend en argument l'identifiant de la vidéo (généralement 8 caractères au format `base64url`). L'identifiant d'une vidéo peut être trouvé dans les sources de la page HTML sur le site du CNRS (par exemple: [https://images.cnrs.fr/video/2975](https://images.cnrs.fr/video/2975)), juste après la chaîne de caractère: `code=`. *À noter que ce code ne correspond pas au numéro figurant dans l'URL de la page.*

`````{tabbed} Aperçu
```{cnrs} pUV9f15n
```
`````
