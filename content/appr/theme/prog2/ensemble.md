# Ensemble - `set`

## Chercher un élément

La fonction cherche un élément dans une liste

```{codeplay}
from random import *
 
a = []
for i in range(100):
    x = randint(1, 999)
    a.append(x)

print(a)
a.sort()
print(a)
```

L'expression `x in liste` retourne une valeur booléene qui indique si x fait partie de la liste.

```{codeplay}
a = [121, 939, 19, 143, 471, 273, 480, 852, 672, 321, 885, 628, 648, 374, 376, 555, 156, 239, 741, 348, 139, 665, 600, 801, 500, 320, 216, 396, 81, 965, 568, 45, 494, 723, 392, 704, 413, 879, 529, 468, 683, 479, 720, 959, 57, 207, 302, 931, 878, 681, 145, 462, 180, 318, 417, 337, 159, 800, 237, 898, 964, 907, 295, 669, 570, 474, 30, 111, 159, 777, 615, 516, 429, 973, 696, 209, 872, 147, 180, 142, 905, 415, 573, 512, 816, 814, 329, 598, 216, 131, 830, 134, 478, 313, 832, 470, 244, 480, 662, 855]

print(855 in a)
print(856 in a)
```

```{codeplay}
a = [121, 939, 19, 143, 471, 273, 480, 852, 672, 321, 885, 628, 648, 374, 376, 555, 156, 239, 741, 348, 139, 665, 600, 801, 500, 320, 216, 396, 81, 965, 568, 45, 494, 723, 392, 704, 413, 879, 529, 468, 683, 479, 720, 959, 57, 207, 302, 931, 878, 681, 145, 462, 180, 318, 417, 337, 159, 800, 237, 898, 964, 907, 295, 669, 570, 474, 30, 111, 159, 777, 615, 516, 429, 973, 696, 209, 872, 147, 180, 142, 905, 415, 573, 512, 816, 814, 329, 598, 216, 131, 830, 134, 478, 313, 832, 470, 244, 480, 662, 855]
===
x = 855
print(x)
for val in a:
    if x == val:
        print(True)
        break

x = 856
print(x)
for val in a:
    if x == val:
        print('True')
        break
print(False)
from turtle import *
n = len(a)
speed(0)

x = -300
for y in a:
    goto(x, y/5)
    dot()
    x += 6
    
color('red')
a.sort()
x = -300
for y in a:
    goto(x, y/5)
    dot()
    x += 6         
```

## Une liste est-elle triée ?

```{codeplay}
a = [570, 562, 87, 609, 411, 833, 825, 852, 390, 892, 417, 55, 632, 496, 902, 893, 222, 796, 179, 766, 793, 354, 793, 186, 254, 72, 995, 45, 362, 762, 118, 650, 19, 429, 504, 763, 111, 474, 167, 754, 344, 299, 13, 404, 703, 684, 760, 621, 674, 327, 836, 930, 390, 821, 51, 990, 416, 297, 553, 183, 307, 221, 350, 841, 762, 728, 341, 548, 798, 432, 103, 759, 525, 972, 174, 844, 566, 199, 76, 164, 383, 929, 480, 49, 798, 23, 976, 991, 570, 833, 336, 117, 953, 345, 635, 798, 510, 69, 725, 171]
b = [13, 19, 23, 45, 49, 51, 55, 69, 72, 76, 87, 103, 111, 117, 118, 164, 167, 171, 174, 179, 183, 186, 199, 221, 222, 254, 297, 299, 307, 327, 336, 341, 344, 345, 350, 354, 362, 383, 390, 390, 404, 411, 416, 417, 429, 432, 474, 480, 496, 504, 510, 525, 548, 553, 562, 566, 570, 570, 609, 621, 632, 635, 650, 674, 684, 703, 725, 728, 754, 759, 760, 762, 762, 763, 766, 793, 793, 796, 798, 798, 798, 821, 825, 833, 833, 836, 841, 844, 852, 892, 893, 902, 929, 930, 953, 972, 976, 990, 991, 995]

def is_sorted(a):
    n = len(a)
    for i in range(1, n):
        if a[i-1] > a[i]:
            return False
    return True

print(is_sorted(a))
print(is_sorted(b))
```

## Recherche binaire

```{codeplay}
liste = [13, 19, 23, 45, 49, 51, 55, 69, 72, 76, 87, 103, 111, 117, 118, 164, 167, 171, 174, 179, 183, 186, 199, 221, 222, 254, 297, 299, 307, 327, 336, 341, 344, 345, 350, 354, 362, 383, 390, 390, 404, 411, 416, 417, 429, 432, 474, 480, 496, 504, 510, 525, 548, 553, 562, 566, 570, 570, 609, 621, 632, 635, 650, 674, 684, 703, 725, 728, 754, 759, 760, 762, 762, 763, 766, 793, 793, 796, 798, 798, 798, 821, 825, 833, 833, 836, 841, 844, 852, 892, 893, 902, 929, 930, 953, 972, 976, 990, 991, 995]

a = 0
b = len(liste)
x = 995

while b - a > 0:
    m = (a + b) // 2
    print(a, m, b, liste[m])
    
    if x == liste[m]:
        break
    elif x < liste[m]:
        b = m
    else:
        a = m + 1
    
print(liste[m] == x)
```


## Noeuds aléatoires d'un graphe

```{codeplay}
from turtle import *
from random import *
up()

pos = []
for i in range(10):
    x = randint(-280, 280)
    y = randint(-180, 180)
    pos.append((x, y))
    goto(x, y)
    dot(10)
    write(i, font=(None, 18))
````

## Attributs

beau - laid
riche - pauvre
intélligent - stupid
grand - petit
gros - maigre
généreux - avare
courageux - timide
extroverti - introverti
sportif - sédentaire

```{codeplay}
Toni = {'beau':True, 'riche':True, 'grand':True}
print(Toni['beau'])
print(Toni['grand'])
````

## Ordre du tri par séléction

Quel est la somme de 1 + 2 + 3 + ... n ?  
Graphiquement ceci nous donne la surface d'un triangle.
Si nous affichons
- `x` sur la première ligne
- `xx` sur la deuxième ligne
- n fois `x` sur la dernière ligne

la réponse à la formule est la somme des x.
Nous pouvons ajouter un triangle identique (cette fois dessiné avec des traits (`-`)), ce qui nous donne un rectangle de taille `(n) * (n+1)`.
La taille du triangle est donc  `(n) * (n+1) / 2`.

```{codeplay}
n = 10
for i in range(n+1):
    print('x' * i + '-' * (n-i))

print(n * (n+1) // 2)
```

```{codeplay}

```

```{codeplay}

```

```{codeplay}

```
