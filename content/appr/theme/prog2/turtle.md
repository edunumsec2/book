# Multiplier - `Turtle`

Dans cette deuxième partie, nous allons changer de concept. D'un style de programmation procédurale nous allons vers la programmation orienté objet.

Le premier changement est que nous pouvons multiplier à volonté les tortues. Les tortues sont des objets dérivé de la classe `Turtle`

```{codeplay}
from turtle import *

ana = Turtle()
ana.shape('turtle')
ana.color('red')
ana.forward(100)

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.left(60)
bob.forward(100)
```

**Exercice** : Créer encore une autre tortue, choisissez sa couleur et faites la bouger quelque part.
