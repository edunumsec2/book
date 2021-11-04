<font size="6"> De la logique à la mémoire </font>

**TODO:** _Du contenu supplémentaire sera rajouté ici pour parler de la mémoire._

<u> La construction de la mémoire </u>

Les {glo}`transistor|transistors`, les {glo}`portelogique|portes logiques` et leur représentation en {glo}`tableverite|tables de vérités`, permettent de manipuler des 0 et des 1 au niveau physique. Tant qu'un courant électrique se déplace dans les {glo}`circuit|circuits`, on est capable de le transformer, de le laisser passer ou de l'arrêter, dans le but d'exprimer des portes «ouvertes» ou des portes «fermées» et donc des nombres binaires.  

Mais comment faire pour {glo}`stockage|stocker` cette information ?

Pour comprendre comment la {glo}`stockage|mémoire` des ordinateurs fonctionne, il faut commencer par la classer en deux grandes catégories. La {glo}`memvolatile|mémoire volatile`, et la {glo}`memnonvolatile|mémoire non volatile`. La {glo}`memvolatile|mémoire volatile` s'efface quand la machine et éteinte. La {glo}`memnonvolatile|mémoire non volatile`, elle, persiste. Si un smartphone s'éteint alors que qu'on est en train de retoucher une photo, ces retouches disparaissent. Elles étaient stockées sur la {glo}`memvolatile|mémoire volatile`. Par contre, au moment où ces retouches sont sauvegardées, elles s'inscrivent dans la {glo}`memnonvolatile|mémoire non volatile`. 

### Les verrous informatiques

Pour stocker de l'information avec un circuit logique, il faut utiliser une autre technique que ce qui a été fait jusqu'à présent, où toutes les sorties dépendaient exclusivement et immédiatement des entrées. Regardons ce qui se passe avec ce circuit, par exemple : c'est une simple porte **OU**, dont l'une des entrées est en fait sa propre sortie.

```{logic}
:height: 100
:mode: tryout

{
  "in": [{"pos": [50, 30], "id": 4, "name": "X", "val": 0}],
  "gates": [{"type": "OR", "pos": [140, 40], "in": [5, 6], "out": 7}],
  "out": [{"pos": [240, 40], "id": 0, "name": "Z"}],
  "wires": [[4, 5], [7, 6, {"waypoints": [[170, 80, "w"], [110, 80, "w"]]}], [7, 0]]
}
```

Au début, les deux entrées de la porte valent 0, comme sa sortie. Si l'on essaie de faire passer l'entrée $X$ à 1, on voit que la sortie $Z$ passera à 1 elle aussi, comme il s'agit d'une porte **OU**. Mais comme $Z$ est aussi relié à l'autre entrée de la porte, on a maintenant un circuit dont on ne peux plus modifier la sortie : même si $X$ passe de nouveau à 0, l'autre entrée reste à 1 et suffit donc pour que $Z$ vale maintenant 1 indéfiniment. On est obligé de remettre le circuit complètement à zéro (l'équivalent de débrancher la prise de courant et de la rebrancher) pour obtenir à nouveau un 0 sur la sortie $Z$.

Assurément, ce circuit n'est pas très intéressant : il se bloque dans un état sans retour possible. Serait-ce possible de construire un circuit un peu plus élaboré qui permettrait de choisir la valeur de sa sortie et de la conserver ? Ces circuits existent en effet et sont à la base du stockage de l'information dans les microprocesseurs. On appelle ces circuits des {glo}`verrou|verrous`. Examinons le circuit ci-dessous : c'est le verrou dit «S-R», pour _set/reset_, en anglais. 

```{logic}
:height: 160

{
  "in": [
    {"pos": [50, 30], "id": 8, "name": "R", "val": 1},
    {"pos": [50, 130], "id": 9, "name": "S", "val": 0}
  ],
  "out": [
    {"pos": [290, 40], "id": 10, "name": "Q"},
    {"pos": [290, 120], "id": 11, "name": "Q'"}
  ],
  "gates": [
    {"type": "OR", "pos": [130, 40], "in": [0, 1], "out": 2},
    {"type": "OR", "pos": [130, 120], "in": [4, 5], "out": 6},
    {"type": "NOT", "pos": [200, 120], "in": 3, "out": 7},
    {"type": "NOT", "pos": [200, 40], "in": 12, "out": 13}
  ],
  "wires": [
    [8, 0],
    [9, 5],
    [6, 3],
    [7, 11],
    [2, 12],
    [13, 10],
    [7, 1, {"waypoints": [[80, 50]]}],
    [13, 4, {"waypoints": [[80, 110]]}]
  ]
}
```

Dans l'exemple ci-dessus, à partir du moment où on a «ouvert» la porte S (donc qu'on a «set», c'est à dire «établi» l'état initial), la sortie Q est 1. Si on avait une ampoule à cet endroit, elle serait allumée. Maintenant, même si on «ferme» la porte S, Q reste bloqué sur 1. On a donc créé une forme de mémoire. La seule façon «d'éteindre» la sortie Q est d'ouvrir R (donc de «reset», c'est à dire réinitialiser le système). 

Voici une vidéo qui illustre ce principe de verrou S-R.

```{youtube} KM0DdEaY5sY
:start: 4:58
```

Pour aller plus loin, une vidéo de résumé qui parle aussi des bascules et des registres :

```{youtube} I0-izyq6q5s
```

````{admonition} Pour aller plus loin
:class: attention

Dans le jeu en ligne «Nandgame» (<https://nandgame.com>), on construit petit à petit un ordinateur complet juste avec, à la base, des portes **NON-ET**. Elles sont la particularité, avec la porte **NON-OU**, de pouvoir simuler toutes les autres portes (y compris un inverseur).
````
