# Dessiner - `forward`

Dans ce chapitre, nous explorons ce que c'est un programme et nous prenons
 la métaphore du dessin. Ici, un programme est une séquence d'instructions pour dessiner une image.

Allons de l'avant (forward) avec la programmation. Nous allons voir que :

- l'expression `from turtle import *` met a disposition les fonctions de dessin,
- les instructions `forward()`, `backward()` permettent de tracer une ligne,
- les instructions `left()`, `right()` permettent de changer de direction.

```{question}
Un programme informatique est

{f}`une instruction de séquence`  
{v}`une séquence d'instructions`  
{f}`un algorithme`  
{f}`une recette de cuisine`
```

## Le module `turtle`

Dans le langage de programmation Python, le module `turtle` (tortue en anglais) présente une façon sympathique pour faire des dessins. C'est pour cela que nous commençons notre aventure de programmation avec cet animal qui avance tout doucement à son propre rythme.

On s'imagine une tortue qui se déplace sur un canevas et laisse une trace.

Ci-dessus, vous trouvez notre premier programme de trois lignes :

- dans la première ligne nous importons toutes (`*`) les fonctions du module `turtle`,
- avec `shape('turtle')` nous affichons une tortue (au lieu de la flèche),
- avec `forward(150)` nous faisons avancer la tortue de 150 pixels.

```{codeplay}
:file: forward1.py
from turtle import *

shape('turtle')
forward(150)
```

**Exercice** : Ajoutez d'autres fonctions telles que `backward()`, `left()`, et `right()` pour faire un dessin.

```{question}
En Python `turtle` est

{v}`un module standard`  
{f}`un éditeur de dessin`  
{f}`une tortue`  
{f}`une commande`
```

## Se déplacer

La tortue peut se déplacer et dessiner une trace avec les 4 fonctions:

- `forward(d)` pour avancer d'une distance `d` (en pixels)
- `backward(d)` pour reculer
- `left(a)` pour tourner à gauche d'un angle `a` (en degrés)
- `right(a)` pour tourner à droite

## Le canevas

Au début, la tortue se trouve au centre d'une zone rectangulaire appelé le canevas.  Ce rectangle a les propriétés suivantes :

- l'origine (0, 0) se trouve au centre,
- l'axe x s'étend de -300 à +300,
- l'axe y s'étend de -200 à +200.

```{codeplay}
:file: forward2.py
from turtle import *

shape('turtle')
forward(300)
backward(600)
forward(300)

left(90)
forward(200)
right(180)
```

**Exercice** : Ajoutez une instruction pour aller tout en bas.

```{question}
La largeur de la zone de dessin de la tortue est

{f}`200 pixels`   
{f}`400 pixels`  
{v}`600 pixels`  
{f}`800 pixels`  
```

## Une séquence

Un programme est une séquence d'instructions. Le bloc des 8 instructions ci-dessous indique comment dessiner un carré. La tortue doit avancer, tourner, avancer, tourner etc.

```{codeplay}
:file: forward3.py
from turtle import *

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
```

**Exercice** : Modifiez ce code pour en faire un rectangle.

```{question}
Une séquence d'instructions d'un bloc est exécutée

{f}`selon la priorité`  
{f}`simultanément`  
{v}`dans l'ordre`  
{f}`aléatoirement`   
```

## Equivalence

La tortue possède 4 fonctions de déplacement, mais à strictement parler, on pourrait s'en sortir avec seulement deux fonctions, `forward()` et `left()`, car :

- `backward(d)` est équivalent à `forward(-d)`
- `right(a)` est équivalent à `left(-a)`

Dans le programme ci-dessous, les 4 lignes du deuxième bloc sont équivalentes aux 4 instructions du premier bloc et donnent un résultat identique.

```{codeplay}
:file: forward4.py
from turtle import *

forward(160)
left(90)
forward(100)
left(90)

backward(-160)  # équivalent à forward(160)
right(-90)  # équivalent à left(90)
backward(-100)
right(-90)
```

```{question}
L'expression `left(90)` est équivalent à

{v}`right(-90)`  
{f}`right(180)`  
{f}`left(180)`  
{f}`left(-90)`  
```

## Epaisseur de ligne

La fonction `width(d)` (épaisseur en anglais) permet de définir l'épaisseur de la ligne.
Voici un triangle où chaque côté a une épaisseur différente.

```{codeplay}
:file: forward5.py
from turtle import *

forward(200)
left(120)

width(5)
forward(200)
left(120)

width(10)
forward(200)
left(120)
```

**Exercice** : Explorez différentes épaisseurs de ligne.

## Maison avec toit

Nous dessinons une maison et marquons le toit par une ligne plus épaisse.

```{codeplay}
:file: forward6.py
from turtle import *

forward(100)
left(90)
forward(60)
left(45)
width(5)
forward(71)
left(90)
forward(71)
width(1)
left(45)
forward(60)
left(90)
```

**Exercice** : Modifiez l'épaisseur du toit.

## Raquette de ping-pong

L'épaisseur de ligne est très utile dans le dessin.

```{codeplay}
:file: forward7.py
from turtle import *

width(20)
forward(100)
width(80)
forward(20)
```

**Exercice** : Transformez la raquette de ping-pong en haltères de musculation.

## Lunettes de soleil

Voici encore un exemple où avec un simple changement d'épaisseur, vous obtenez un effet très intéressant.

```{codeplay}
:file: forward8.py
from turtle import *

width(50)
forward(20)
width(10)
forward(60)
width(50)
forward(20)
width(10)
forward(40)
left(45)
forward(60)
```

**Exercice** : Ajoutez la première branche qui manque.

## Editeur de Python

Jusqu'à maintenant, nous avons exécuté nos petits programmes ici dans cette page web. Malheureusement, ces programmes disparaissent quand nous rechargeons la page. Pour pouvoir les sauvegarder et programmer indépendamment de ce site web, nous avons besoin d'un éditeur de Python externe.

Nous vous proposons d'utiliser [Thonny](https://thonny.org), qui est un logiciel libre, facile à installer, et un excellent éditeur pour débuter avec Python. Essayez de faire ceci :

1. Ouvrez l'éditeur Thonny
1. Définissez la fonction `maison()`
1. Appelez la fonction
1. Sauvegardez le programme sous `maison.py`
1. Exécutez le programme

```{image} media/thonny.png
```

Quand vous utilisez le module `turtle` avec Thonny, ajoutez toujours la fonction `done()` comme dernière ligne de code, pour que vous puissiez quitter le programme.

## Exercices

- Téléchargez un exercice.
- Ouvrez-le dans un éditeur externe (tel que Thonny).
- Mettez votre prénom, nom et classe.
- Remplacez `...` par votre code.
- Déposez votre exercice sur Moodle (ou plateforme équivalente).

### Rectangle

Dessinez un rectangle.

```{codeplay}
:file: rectangle.py
from turtle import *
# Prénom, nom, classe

forward(200)
...
done()
```

### Triangle

Dessinez un triangle.

```{codeplay}
:file: triangle.py
from turtle import *
# Prénom, nom, classe

forward(200)
...
done()
```

### Hexagone

Dessinez un hexagone.

```{codeplay}
:file: hexagone.py
from turtle import *
# Prénom, nom, classe

forward(100)
...
done()
```

### Maison

Dessinez une maison.

```{codeplay}
:file: maison.py
from turtle import *
# Prénom, nom, classe

forward(100)
...
done()
```

### Chaise

Dessinez une chaise.

```{codeplay}
:file: chaise.py
from turtle import *
# Prénom, nom, classe

left(90)
forward(100)
...
done()
```

### Table

Dessinez une table.

```{codeplay}
:file: table.py
from turtle import *
# Prénom, nom, classe

left(90)
forward(100)
...
done()
```

### Lit

Dessinez un lit.

```{codeplay}
:file: lit.py
from turtle import *
# Prénom, nom, classe

left(90)
forward(100)
...
done()
```
