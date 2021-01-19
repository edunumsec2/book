# Extensions

Dans ce document, vous trouverez de la documentation utilisateur pour toutes les extensions de syntaxe développées spécifiquement pour le projet.

Ces extensions de syntaxes sont des extensions Sphinx locales implémentées en Python.
Les sources sont situées dans le dossier `config/extensions/`.

## Questions à choix multiples

Il est possible d'intégrer des questions à choix multiples au fil des pages via la directive `question`.
Dans le corps de la directive, les bonnes et mauvaises réponses sont indiquées via les roles `{v}` et `{f}` pour *vrai* et *faux*.

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