---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# <span commented>Fonctions</span><!-- REVIEW/JPP: les fonctions sont l'un des principaux outils que la programmation nous offre pour organiser le code, le modulariser, monter dans les niveaux d'abstractions, etc., le tout avec des principes et une syntaxe simple en Python. Je ssui d'avis de les traiter avant toutes les structures de données (ne serait-ce que parce que la manipulation des structures de données demande d'utiliser des fonctions et des méthodes). -->
<span commented>En programmation, les fonctions sont des suites d'instructions nommées qui permettent d'éviter d'écrire plusieurs fois la même suite d'instructions. En effet, les fonctions peuvent être utilisées autant de fois que nécessaire dans un programme. Il est d'usage de dire que les fonctions prennent des arguments et renvoient une valeur de retour.</span><!-- REVIEW/JPP: Proposition de refomulation. Souvent, en programmation, on a besoin de faire la même chose plusieurs fois, ou de résoudre des problèmes semblables par une même suite d'instructions. La quasi-totalité des langages de programmation disposent d'un concept de «sous-programme», qui nous permet de prendre une suite d'instructions, de lui donner un nom, et d'ensuite les exécuter autant de fois de nécessaire simplement en utilisant le nom de ce sous-programme. En Python, un tel sous-programme s'appelle une **fonction**. Les fonctions sont flexibles et peuvent être _paramétrées_, c'est-à-dire qu'elle vont demander des valeurs supplémentaires lors de leur exécution, valeurs qu'on appelle _arguments_. Finalement, elle peuvent aussi calculer et _retourner une valeur_ qui sera utilisable depuis le code qui a appelé la fonction. <newline, newline> On peut considérer que les fonctions fournissent ainsi la possibilibité d'enrichir le «vocabulaire» avec lequel on donne des instructions à la machine. <newline, newline> Voici un exemple: -->

```{code-cell} ipython3
def saluer(prenom, nom):
    print("Bonjour",prenom,nom)
    print("Vous êtes en train de programmer!")

a = "Marc"
b = "Zukerberg"
saluer(a,b)
```

Cet exemple illustre à la fois la _définition_ d'une nouvelle fonction et son _appel_, son utilisation.

La nouvelle fonction est déclarée au début de cet exemple. Elle s'appelle `saluer` et exécute deux instructions `print`. Elle nécessite deux arguments qui sont nommés **prenom** et **nom**. Le nom de ces arguments est utilisé uniquement au sein de la fonction, il sera impossible d'utiliser "nom" comme une variable hors de la fonction. À la dernière ligne, on appelle la fonction `saluer` en utilisant comme arguments les valeurs stockées dans les deux variables `a` et `b`, qui vont être assignées respectivement à `prenom` et `nom`.

+++

## Appeler une fonction
Une fois une fonction définie, il est possible de l'utiliser en l'appelant. Pour ce faire, il suffit d'écrire le nom de la fonction suivi des éventuels arguments de la fonction entre parenthèses.

Voici quelques exemples d'utilisation de fonctions prédéfinies en Python.
La fonction `type` retourne le type de son argument.

```{code-cell} ipython3
type("Bonjour")
```

La fonction `pow` retourne le résultat de son premier argument mis à la puissance du second (ici, par exemple, $3^5$).

```{code-cell} ipython3
pow(3, 5)
```

La fonction `len` retourne la longueur d'une chaine de caractères <!-- REVIEW/JPP: si on a déjà vu les listes ou d'autres structures: ajouter 'ou d'une liste', etc. -->.

```{code-cell} ipython3
len("Bonjour")
```

La fonction `round` retourne l'arrondi d'une valeur numérique.

```{code-cell} ipython3
round(333.76)
```

La fonction `min` retourne la valeur minimale des arguments qu'on lui fournit.

```{code-cell} ipython3
min(5,34,112)
```

## Définir une fonction
Pour définir une fonction, il faut écrire le mot-clé `def` puis le nom de la fonction suivi par une paire de parenthèses et d'un deux-points. La nomenclature d'une fonction est régie par les mêmes règles que pour les noms de variables: des lettres, des chiffres et des <span commented>traits de soulignement</span><!-- REVIEW/JPP: auparavant, on a je crois dit 'tiret bas' --> sont autorisés, mais le premier caractère ne peut pas être un chiffre. Il n'est pas possible d'utiliser un mot-clé comme nom d'une fonction, et il faut éviter d'avoir une variable et une fonction du même nom.

    def mafonction():

+++

Les instructions qui doivent être exécutées à l'appel de la fonction sont indentées.

```{code-cell} ipython3
def mafonction():
    a = 3 * 5
    return a

resultat = mafonction()
print (resultat)
```

L'instruction `return` permet de _retourner_ une valeur calculée par la fonction et d'ainsi déterminer quelle est son résultat — ce qu'on appelle sa _valeur de retour_. <span commented>Comme inscrit dans le premier exemple, cette instruction est facultative si le résultat de la fonction n'est pas un objet que l'on veut utiliser.</span><!-- REVIEW/JPP: confusing, parce que c'est le code appelant qui décide s'il veut utiliser la valeur de retour alors que c'est quand on écrit la fonction qu'on décide si oui ou non elle va retourner quelque chose. Proposition de reformulation: Toutes les fonctions ne doivent pas forcément retourner une valeur. Comme le premier exemple le montre, une fonction pourrait se contenter de faire quelques `print` sans calculer un résultat donné. Dans ce cas, lorsqu'il n'y a pas de valeur à retourner, on n'a pas besoin du mot clé `return`: (ensuite, même avec cette reformulation, je pense qu'il faudrait un exemple pour montrer que 'return' cause l'arrêt de l'exécution du reste du code de la fonction, qui est aussi un point sur lequel les élèves se plantent facilement) -->

```{code-cell} ipython3
def spammer(n):
    for i in range(n):
        print("Spam!")
        
spammer(8)
```

Dans l'exemple ci-dessus, la fonction `spammer` a un argument `n` qui indique le nombre de répétitions de la boucle. Elle n'a aucune valeur de retour.

```{code-cell} ipython3
#Distance en kilomètre et temps en heure

def vitesse(distance, temps):
    v = distance / temps
    return v

a = vitesse(12,3)
print(a,"km/h")

b = vitesse(3,12)
print(b,"km/h")
```

Il est possible d'utiliser plusieurs arguments dans une fonction en les séparant par une virgule. L'ordre des arguments doit être respecté; ainsi, `vitesse(12, 3)` ne retournera pas la même valeur que `vitesse(3, 12)`: l'un calcule la vitesse nécessaire pour parcourir 12 kilomètres en 3 heures, alors que l'autre calcule la vitesse nécessaire pour parcourir 3 kilomètres en 12 heures.

+++

Un élément à prendre en compte dans l'utilisation de fonction est la visibilité des variables. Lorsqu'une variable est utilisée dans une fonction, elle n'est «visible» (ou _définie_) qu'à l'intérieur de cette fonction. Dans l'exemple ci-dessus, la variable `v` n'est pas définie en dehors de la fonction `vitesse` et ne peut donc pas être utilisée en dehors. Par contre, si l'on souhaite <span commented>utiliser</span><!-- REVIEW/JPP: je ne sais pas si ça vaut la peine de parler de ceci, parce que c'est assez complexe: on n'a par exemple pas besoin de global pour lire une structure, mais seulement pour réaffecter une variable, mais avec les structures non immuable comme les listes, on peut quand même changer leur contenu sans global parce que ce n'est pas une réaffectation... est-ce donc nécessaire d'en parler? --> une variable globale (c'est-à-dire définie dans le script principal, en dehors d'une fonction), alors il faut l'indiquer avec le mot-clé `global`, comme dans l'exemple ci-dessous.

```{code-cell} ipython3
def saluer(nom):
    global nbpers
    nbpers = nbpers + 1
    print("Bonjour", nom)
    print("Bienvenue")

nbpers = 0
saluer("Pierre")
saluer("Jeanne")
print("J'ai pu saluer", nbpers, "personnes")
```

Dans l'exemple ci-dessus, le programme garde le compte du nombre de personnes saluées dans la variable globale `nbpers` qui est mise à jour à chaque appel de fonction. Grâce au mot-clé `global` de la ligne 2, Python va chercher la valeur de cette variable à l'extérieur de la fonction. Elle a été initialisée à la ligne 7, qui est la première ligne exécutée par le programme après la définition de la fonction `saluer`.

```{code-cell} ipython3
def fonction(x): 
    a = 3
    a = a+1
    return a*x 

a = 5
b = fonction(10)
print(b)
b = fonction(10)
print(b)
```

Dans l'exemple ci-dessus, la variable `a` qui est utilisée dans la fonction n'est pas la même que la variable `a` définie à la ligne 6.

```{code-cell} ipython3
def fonction(x):
    global a
    a = a+1
    return a*x

a = 5
b = fonction(10) 
print(b)
b = fonction(10) 
print(b)
```

Dans l'exemple ci-dessus, la valeur de la variable `a` utilisée dans la fonction est récupérée grâce au mot clé `global`. Ainsi, la variable `a` modifiée lors de l'exécution de la fonction peut être utilisée dans la suite du programme.

+++

## Exercices

+++

### Ex
Faites un programme qui demande à l'utilisateur les coefficients **a, b** et **c** d'une fonction du deuxième degré et qui retourne les solutions de l'équation $ax^2 + bx + d = 0$. Afin de pouvoir réutiliser ce calcul dans plusieurs programmes, nous allons créer une fonction `solution2degre acceptant 3 arguments (a, b et c).

**Rappel:**.  
Si le discriminant $\Delta = b^2 - 4ac$ est
- négatif: il n'y a pas de solution, 
- nul: il y a qu'une seule solution, 
- positif: il y a deux solutions.

La racine carrée peut s'obtenir avec la puissance 0.5, <span commented>ou avec la fonction `sqrt` importée du module `math`</span><!-- REVIEW/JPP: mais on n'a pas encore parlé de modules, donc information à taire ici, à mon avis -->.

```{code-cell} ipython3

```
