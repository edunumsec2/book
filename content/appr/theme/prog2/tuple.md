# Grouper - `tuple`

Dans ce chapitre nous allons voir une structure très similaire à une liste - le tuple.
Contrairement à la liste, le tuple est immuable, c'est à dire on peux accéder à ces éléments via un indice, mais on ne peux pas le changer.

## Enumérer une liste

La fonction `enumerate()` permet d'énumérer une liste. Nous utilisons cette fonction dans une boucle `for` pour itérer à la fois sur l'indice et la valeur. Nous avons donc deux variables d'itération :

- `i` - index de l'élément
- `val` - valeur de l'élément

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]

for i, val in enumerate(liste):
    print(i, val)
```

**Exercice** : Modifier la liste et exécutez de nouveau.

Il est également possible d'énumérer une chaîne de caractères.

```{codeplay}
for i, val in enumerate('Python'):
    print(i, val)
```

## Minimum et son indice

Avec la fonction `enumerate()` nous pouvons itérer sur index et valeur à la fois.

```{codeplay}
liste = [3, 4, 1, 2, 6, 5]

i_min, min = 0, liste[0]

for i, val in enumerate(liste):
    if val < min:
        i_min, min = i, val
        
print(i_min, min)
```

