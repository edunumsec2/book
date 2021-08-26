# De la logique à la mémoire

**TODO:** _Du contenu supplémentaire sera rajouté ici pour parler de la mémoire._

## La construction de la mémoire

Les {glo}`transistor|transistors`, les {glo}`portelogique|portes logiques` et leur représentation en {glo}`tableverite|tables de vérités`, permettent de manipuler des 0 et des 1 au niveau physique. Tant qu'un courant électrique se déplace dans nos {glo}`circuit|circuits`, nous sommes capables de le transformer, de le laisser passer ou de l'arrêter, dans le but d'exprimer des portes «ouvertes» ou des portes «fermées» et donc des nombres binaires.  

Mais comment faire pour {glo}`stockage|stocker` cette information?

Pour comprendre comment la {glo}`stockage|mémoire` des ordinateurs fonctionne, il faut commencer par la classer en deux grandes catégories. La {glo}`memvolatile|mémoire volatile`, et la {glo}`memnonvolatile|mémoire non volatile`. La {glo}`memvolatile|mémoire volatile` s'efface quand la machine et éteinte. La {glo}`memnonvolatile|mémoire non volatile`, elle, persiste. Si votre smartphone s'éteint alors que vous êtes en train de retoucher une photo, ces retouches disparaissent. Elles étaient stockées sur la {glo}`memvolatile|mémoire volatile`. Par contre, au moment où vous avez sauvegardé ces retouches, elles s'inscrivent dans la {glo}`memnonvolatile|mémoire non volatile`. 

## Les verrous informatiques

Certains circuits sont construits pour «bloquer» une information, ce qui nous permet de la garder en mémoire, tant que le circuit est alimenté par l'électricité. On appelle ces circuits des {glo}`verrou|verrous`. Le plus élémentaire est le verrou S-R, pour «set», «reset», en anglais. 

```{logic}
:height: 150
:mode: tryout

{
  "in": [
    {"pos": [50, 30], "id": 8, "name": "R", "val": 0},
    {"pos": [50, 120], "id": 9, "name": "S", "val": 1}
  ],
  "out": [
    {"pos": [240, 40], "id": 10, "name": "Q"},
    {"pos": [240, 110], "id": 11, "name": "Q'"}
  ],
  "gates": [
    {"type": "NOR", "pos": [120, 40], "in": [0, 1], "out": 2},
    {"type": "NOR", "pos": [120, 110], "in": [4, 5], "out": 6}
  ],
  "wires": [[8, 0], [9, 5], [2, 4], [2, 10], [6, 1], [6, 11]]
}
```

Dans l'exemple ci-dessus, à partir du moment où on a «ouvert» la porte S (donc qu'on a «set», c'est à dire «établi» l'état initial), la sortie Q est 1. Si on avait une ampoule à cet endroit, elle serait allumée. Maintenant, même si on «ferme» la porte S, Q reste bloqué sur 1. On a donc créé une forme de mémoire. La seule façon «d'éteindre» la sortie Q est d'ouvrir R (donc de «reset», c'est à dire réinitialiser le système). 

Voici une vidéo qui illustre ce principe de verrou S-R.

```{youtube} KM0DdEaY5sY
:start: 4:58
```
