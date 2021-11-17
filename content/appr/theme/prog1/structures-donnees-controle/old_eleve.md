Structures de données et structures de contrôle
===============================================

## Les expressions conditionnelles
Les expression conditionelles permettent d'executer une suite d'instructions seulement si une condition est remplie. Nous rencontrons des dizaines de conditions par jour, ceci régit les actions que nous entrenons. Par exemple: face à deux files d'attente au supermarché nous allons nous diriger vers la file qui contiens le moins de client. Concrètement nous avons fait le test logique suivant : Est-ce que le nombre de client dans la file A est inférieur au nombre de client dans la file B ? Si la réponse à ce test logique est vraie, on se dirige vers la file A sinon on se dirige vesr la file B.

### Les tests logiques
 Un test logique permet d'obtenir une valeur booléenne "TRUE" ou "FALSE" suite à une une question qui serait posée à un certain moment du programme. Pour poser ces questions nous devons utiliser un opérateur de comparaison ou un opérateur logique.
 ### Les opérateurs de comparaison
 Comme leur nom l'indique ces opérateurs sont utilisés pour comparer des valeurs numériques ou textuelles. Ainsi, la question "Est-ce que la valeur contenue dans la variable a est inférieur à 4" se transcrira "a < 4".
 * **\>** *"plus grand que..."*
 * **<** *"plus petit que..."*
 * **<=** *"plus petit ou égal à..."*
 * **>=** *"plus grand ou égal à..."*
 * **==** *"égal à..."*
 * **!=** *"non égal à..."*

:::{note} Note
Ne pas confondre le signe = qui permet d'assigner une valeur à une variable et l'opérateur de comaraison == qui permet de comparer si deux valeurs ou deux chaines de caractères sont égales.
:::
### Les opérateurs logiques
Quand il est nécessaire de réaliser un test logique plus complexe, des opérateurs logiques peuvent être utilisés. Ces opérateurs renvoient un booléen suite à l'analyse logique d'autres booléens. On retrouve les opérateurs logiques suivants:
* not "non"
* and "et"
* or "ou"
* == "égal à..."

## L'instruction if
L'instruction "if" permet d'executer une suite d'instruction si une condition est remplie. Si la condition n'est la remplie le programme suit son cours sans executer ces instructions.

```python
if a > 4:
    print('a est plus grande que 4')
```

### L'instruction if...else
L'instruction if...else permet d'executer une suite d'instruction si une condition est remplie ou une autre suite d'instruction si la condition n'est pas remplie. 
```python
if a > 4:
    print('la variable a est plus grande que 4')
else:
    print('la variable a est plus petite ou égale à 4')
```

### L'instruction if...elif...else
L'instruction if...elif..else permet d'executer une suite d'instruction si une condition est remplie. Si la première condition n'est pas remplie,une autre est testée.

```python
if a == 4:
    print('la variable a est égale à 4')
elif a == 3:
    print('la variable a est égale à 3')
elif a == 2:
    print('la variable a est égale à 2')
else:
    print('la variable a est différente de 2, 3 ou 4')
```
