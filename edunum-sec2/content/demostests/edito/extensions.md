# Extensions

Dans ce document, vous trouverez de la documentation utilisateur pour toutes les extensions de syntaxe développées spécifiquement pour le projet.

Ces extensions de syntaxes sont des extensions Sphinx locales implémentées en Python.
Les sources sont situées dans le dossier `config/extensions/`.

## Questions à choix multiples

Il est possible d'intégrer des questions à choix multiples au fil des pages via la directive `question`.
Dans le corps de la directive, les bonnes et mauvaises réponses sont indiquées via les rôles `{v}` et `{f}` pour *vrai* et *faux*.

`````{tabbed} Aperçu

```{question}
Combien y a t'il de bits dans un octet ?
Je pense qu'il y en a {f}`2`, {f}`4`, {v}`8` ou {f}`64`.
```
`````

`````{tabbed} Code

````{code-block} markdown
```{question}
Combien y a t'il de bits dans un octet ?
Je pense qu'il y en a {f}`2`, {f}`4`, {v}`8` ou {f}`64`.
```
````
`````

Il est possible de changer le titre affiché au dessus de la question.
Le contenu de la question peut lui-même être structuré en Markdown.
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

`````{tabbed} Code

````{code-block} markdown
```{question} Question avec un titre personnalisé
Parmi les informaticiens et informaticiennes suivants, qui a reçu le prix Turing ?
* {v}`Barbara Liskov`
* {v}`Niklaus Wirth`
* {f}`Alan Turing`
* {v}`Tim Berners-Lee`
```
````
`````

### Options

Par défaut, si il y a uniquement une réponse correcte, les autres réponses se déselectionnent automatiquement.
Pour que plusieurs réponses puissent être sélectionnées même s'il n'y a qu'une seule réponse, l'option `:multi:` peut être ajoutée.

`````{tabbed} Aperçu

```{question}
:multi: 
Parmis les personnes suivantes, laquelle ou lesquelles sont à l'origine du Web ?
* {f}`Barbara Liskov`
* {f}`Niklaus Wirth`
* {f}`Alan Turing`
* {v}`Tim Berners-Lee`
```
`````

`````{tabbed} Code

````{code-block} markdown
```{question}
:multi: 
Parmis les personnes suivantes, laquelle ou lesquelles sont à l'origine du Web ?
* {f}`Barbara Liskov`
* {f}`Niklaus Wirth`
* {f}`Alan Turing`
* {v}`Tim Berners-Lee`
```
````
`````

## Blancs

Pour ajouter des *blancs* dans le texte, il suffit d'utiliser le rôle `bl`.
Dans le texte du rôle, les différentes options de réponses sont séparées par un caractère `|`.
Une réponse valable est précédée d'un caractère `>`.

`````{tabbed} Aperçu
Dans le texte suivant, certains {bl}`>mots|trucs|machins` sont laissés {bl}`pour compte|>blancs|verts|seuls`.
`````

`````{tabbed} Code
```{code-block} markdown
Dans le texte suivant, certains {bl}`>mots|trucs|machins` sont laissés {bl}`pour compte|>blancs|verts|seuls`.
```
`````

## Vidéos YouTube

Pour ajouter une vidéo YouTube directement dans le document, utiliser la directive `youtube`.
La directive attend en argument l'identifiant de la vidéo (généralement 11 caractères au format `base64url`).
L'identifiant d'une vidéo YouTube peut être trouvé dans l'URL de la video, juste après la chaîne `?v=`.
Par exemple, l'identifiant de la vidéo à l'URL `https://www.youtube.com/watch?v=dQw4w9WgXcQ` est `dQw4w9WgXcQ`.

`````{tabbed} Aperçu
```{youtube} uHKfrz65KSU
```
`````

`````{tabbed} Code
````{code-block} markdown
```{youtube} uHKfrz65KSU
```
````
`````

### Options

#### Départ de la lecture

Par défaut, la lecture commence au début de la vidéo.
Via l'option `:start:`, il est possible de faire commencer la lecture à un endroit différent de la vidéo.
L'option `:start:` attend en argument un nombre entier qui indique la seconde à laquelle la lecture doit commencer.

`````{tabbed} Aperçu
```{youtube} _OBlgSz8sSM
:start: 18
```
`````

`````{tabbed} Code
````{code-block} markdown
```{youtube} _OBlgSz8sSM
:start: 18
```
````
`````

#### Contrôles

Par défaut, les boutons de contrôle de la vidéo sont affichés dans une barre en bas de la vidéo.
Ils peuvent cependant être cachés via l'option `:nocontrols:`.

`````{tabbed} Aperçu
```{youtube} wGGqWwVb3sU
:nocontrols:
```
`````

`````{tabbed} Code
````{code-block} markdown
```{youtube} wGGqWwVb3sU
:nocontrols:
```
````
`````

## Vidéos SwitchTube

Pour ajouter une vidéo hébergée sur SwitchTube directement dans le document, utiliser la directive `switchtube`.
La directive attend en argument l'identifiant de la vidéo (généralement une suite de caractères au format `base64url`).
L'identifiant d'une vidéo SwitchTube peut être trouvé à la fin de l'URL de la video.
Par exemple, l'identifiant de la vidéo à l'URL `https://tube.switch.ch/videos/f6365946` est `f6365946`.

`````{tabbed} Aperçu
```{switchtube} f6365946
```
`````

`````{tabbed} Code
````{code-block} markdown
```{switchtube} f6365946
```
````
`````

### Options

#### Départ de la lecture

Par défaut, la lecture commence au début de la vidéo.
Via l'option `:start:`, il est possible de faire commencer la lecture à un endroit différent de la vidéo.
L'option `:start:` attend en argument un nombre entier qui indique la seconde à laquelle la lecture doit commencer.

`````{tabbed} Aperçu
```{switchtube} f6365946
:start: 122
```
`````

`````{tabbed} Code
````{code-block} markdown
```{switchtube} f6365946
:start: 122
```
````
`````

#### Cacher le titre

Il est possible d'ajouter l'option `:notitle` pour cacher le titre de la vidéo dans le lecteur.

`````{tabbed} Aperçu
```{switchtube} f6365946
:notitle:
```
`````

`````{tabbed} Code
````{code-block} markdown
```{switchtube} f6365946
:notitle:
```
````
`````

## Interpréteur Python

Il est possible d'insérer un interpréteur Python et éditeur directement dans le document, le tout implémenté en Javascript et qui tourne dans le client Web du visiteur.
Pour ceci, il suffit d'utiliser la directive `codeplay`.

`````{tabbed} Aperçu
```{codeplay}
def double(x):
    return x + x

print(double(1))
```
`````

`````{tabbed} Code
````{code-block} markdown
```{codeplay}
def double(x):
    return x + x

print(double(1))
```
````
`````

### Options

Via l'option `:exec:`, le code est executé dès le chargement de la page.

`````{tabbed} Aperçu
```{codeplay}
:exec:
def puissance(x, y):
    return x ** y

print(puissance(2, 10))
```
`````

`````{tabbed} Code
````{code-block} markdown
```{codeplay}
:exec:
def puissance(x, y):
    return x ** y

print(puissance(2, 10))
```
````
`````