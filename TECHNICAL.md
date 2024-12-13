# Logic

Nom du plugin: Logic  
Version: _latest_, en ligne sur <https://logic.modulo-info.ch>  
Auteur: Jean-Philippe Pellet  
Description: Permet l'édition en ligne de circuits logiques sans installation de logiciel

## Installation

Aucune installation particulière n'est requise, Logic est directement intégré au projet. L'ajout de blocs de type {logic} cause l'inclusion d'un seul et unique fichier JavaScript via le plugin sphinx, JavaScript qui sera chargé depuis <https://logic.modulo-info.ch>

## Utilisation

La directive `logic` permet l'inclusion d'un éditeur de circuits logiques. Le contenu doit être du code JSON5 représentant le circuit logique. Une telle représentation peut être obtenue en utilisant l'éditeur graphique en ligne à <https://logic.modulo-info.ch> et en cliquant sur le bouton de partage. Voici un exemple de comment inclure un circuit simple avec deux entrées, une sortie et une porte AND:

    ```{logic}
    :height: 235
    :mode: full
    
    { // JSON5
      v: 6,
      components: {
        in0: {type: 'in', pos: [110, 85], id: 0},
        out0: {type: 'out', pos: [380, 140], id: 1},
        in1: {type: 'in', pos: [110, 150], id: 2},
        and0: {type: 'and', pos: [225, 130], in: [3, 4], out: 5},
      },
      wires: [[0, 3], [2, 4], [5, 1]]
    }
    ```

La directive a plusieurs paramètres:

| Nom        | Type      | Description                                                                                            |
| ---------- | --------- | ------------------------------------------------------------------------------------------------------ |
| `height`   | int       | [Obligatoire] La hauteur en pixels à réserver dans la page pour cet éditeur                            |
| `ref`      | string    | [Optionnel] Une référence à utiliser pour ce diagramme au sein de la page dans laquelle il est intégré |
| `mode`     | enum      | [Optionnel] Le mode d'interaction selon lequel présenter le contenu de cet éditeur (cf. ci-dessous)    |
| `showonly` | list[str] | [Optionnel] Une liste séparée par des virgules d'identifants de composants à afficher                  |

Si `showonly` est spécifié, seuls les composants dont l'identifiant est dans la liste seront affichés. Les autres composants seront cachés. Les composants sont identifiés par leur identifiant unique, qui est visible dans le tooltip affiché lorsqu'on passe la souris sur un bouton de composant dans l'éditeur principal.

Le paramètre `mode` peut prendre les valeurs suivantes:

 * `static`: le circuit est affiché en mode statique, sans possibilité d'interaction.
 * `tryout`: le circuit est affiché en mode interactif, mais sans possibilité de modification de la structure. Les entrées peuvent être modifiées et la sortie est mise à jour en conséquence.
 * `connect`: le circuit est affiché en mode interactif, avec possibilité de modification de la structure. Les entrées peuvent être modifiées et la sortie est mise à jour en conséquence. Les composants peuvent être déplacés et les fils peuvent être ajoutés ou supprimés. Le menu des composants est caché.
 * `design`: le circuit est affiché en mode interactif, avec possibilité de modification de la structure. Les entrées peuvent être modifiées et la sortie est mise à jour en conséquence. Les composants peuvent être déplacés et les fils peuvent être ajoutés ou supprimés. Le menu des composants est affiché. Si `showonly` est spécifié, seuls les composants listés seront affichés.
 * `full`: le circuit est affiché comme pour `design`, mais permet en plus des interactions comme la création de composants ou de fils défectueux, la création de tests, etc.

## Liens “highlight” depuis le texte

Il est possible de faire en sorte qu'une partie d'un circuit logique soit mis en évidence lorsqu'on clique sur un lien dans le texte principal d'une page. Pour ce faire, on peut utilier le markup suivant:

    {logicref}`fulladder_2bits.{a1,b1}|les deux bits de la colonne suivante`

Ici, `{logicref}` est le nom du _rôle_ à utiliser; il est attribué à la portion de texte entre backticks qui suit sans espaces. Cette portion de texte est séparée en deux parties par `|`. La seconde partie est le texte à afficher; la première partie est une liste de composants à mettre en évidence lors d'un clic. Ils sont tous de la forme `circuit_id.component_id`, où `circuit_id` est l'identifiant du circuit logique (donné au circuit avec le paramètre `ref`; voir ci-dessus), et `component_id` est l'identifiant du composant à mettre en évidence tel qu'attribué par l'éditeur. (Une des options de rendu de l'éditeur en mode `full` est d'afficher les identifiants des composants, ce qui facilite leur repérage.)

Comme on le voit dans cet exemple, il est possible de mettre en évidence plusieurs composants en les séparant par des virgules, et on peut mettre en évidence la référence du circuit logique en faisant des choses du type `fulladder_2bits.{a1,b1}`. On peut également faire l'inverse: mettre en évidence le même composant dans plusieurs circuits différents, avec une syntaxe qui va ressembler à `{xor_circuit_01,xor_circuit_10}.or`, par exemple.

## Documentation de l'API

Chaque instance d'un `LogicEditor` a une méthode `save(): Circuit` qui retourne un objet représentant le circuit logique. De même, chaque instance a une méthode `loadCircuitOrLibrary(data: string | Circuit)` qui charge un circuit logique à partir d'un objet.

S'il s'agit d'obtenir une représentation textuelle et non objet du circuit, `Serialization.stringifyObject(circuit: Circuit, compact: boolean): string` est à appeler sur le résultat de `save()`. Le résultat peut aussi être passé directement à la méthode `loadCircuitOrLibrary`.

Pour plus de détails sur l'API, voir le code source du plugin et les méthodes publiques de la classe `LogicEditor` [ici](https://github.com/jppellet/Logic-Circuit-Simulator/blob/master/simulator/src/LogicEditor.ts). 

## Exemples

Pour des exemples, on peut s'inspirer du code source des pages du chapitre **Architecture des ordinateurs**.

## Licence & autres informations

Voir le repository principal du plugin: <https://github.com/jppellet/Logic-Circuit-Simulator/>

---

# Codeplay

Nom du Plugin : Codeplay  
Auteur : Romain Edelmann  
Description : Codeplay est un environnement de programmation Python minimaliste basé sur [Skulpt](https://skulpt.org/) et [CodeMirror](https://codemirror.net/). Une directive Sphinx accompagne cet environnement de programmation afin de pouvoir facilement l'inclure dans des documents.

## Installation

Aucune installation particulière n'est requise, CodePlay est directement intégré au projet.

## Utilisation

La directive `codeplay` permet l'inclusion de l'environnement de programmation CodePlay.
La directive a plusieurs paramètres :

| Nom                | Type            | Description                                                            |
| ------------------ | --------------- | ---------------------------------------------------------------------- |
| `exec`             | Flag            | Exécute automatiquement le code au chargement de la page.              |
| `static`           | Flag            | Empêche l'édition du code.                                             |
| `nocontrols`       | Flag            | Cache les boutons de contrôle.                                         |
| `output_lines`     | Nonnegative int | Spécifie la taille de la zone de sortie, en nombre de lignes.          |
| `min_output_lines` | Nonnegative int | Spécifie la taille minimale de la zone de sortie, en nombre de lignes. |
| `max_output_lines` | Nonnegative int | Spécifie la taille maximale de la zone de sortie, en nombre de lignes. |
| `file`             | Text            | Spécifie le nom du fichier lors du téléchargement.                     |

## Configuration

Aucune configuration globale.

## Documentation de l'API

Aucune API n'est fournie.

## Exemples

CodePlay est très largement utilisé dans le chapitre Programmation sur la partie Apprendre de Modulo.

## Licence

CodePlay faisant partie intégrante du projet, il est disponible sous la même license que le reste du projet.

---

# Print

Consulter le document [suivant](doc/imprimable.md). 
