(programmation)=
Programmation
========================
 

## Le but

Notre vie moderne est imprégnée de nos interactions avec des ordinateurs. La communication, la recherche d'information, les divertissements, les processus, les réseaux sociaux ou encore les object connectés sont autant d'exemples de choses qui font désormais partie de notre quotidien. En sachant programmer un ordinateur, on se dote d'un outil considérable pour simplifier, multiplier et accélérer certaines actions comme la gestion de réservations pour un grand hôtel, effectuer une quantité importante de calculs dans un projet de recherche et même la bonne réalisation d’une recette de cuisine. 
 
Malheureusement, les ordinateurs ne comprennent pas le langage humain. Les circuits électroniques qui leur permettent de manipuler une grande quantité d'information en peu de temps ne peuvent traiter que des 0 et des 1. Pour pouvoir donner des ordres à l'ordinateur, nous devons utiliser des _langages de programmation_ qui, grâce à leur syntaxe stricte et non ambiguë, peuvent à la fois être compris des humains et traités par un ordinateur.
 

## Le fonctionnement

Un programme informatique est une représentation écrite d'une suite d'ordres que l'on veut donner à la machine. On appelle ces ordres des instructions et une suite d'instruction, un algorithme. On distingue plusieurs paradigmes, ou style de programmation différents en fonction du but qu’a le programme. Par exemple, la programmation séquentielle est décrite par une suite d’instructions qui s’exécutent les unes après les autres. La programmation événementielle est représentée par des couples événements-actions qui permettent, après une entrée nommée événement, d’exécuter des instructions. 
 

## Les langages

Il y a des centaines de langages de programmation différents qui ont souvent une caractéristique leur donnant l’avantage d’être utilisés dans un domaine plutôt qu’un autre. On utilisera par exemple JavaScript (pour une interface web), C# (pour les jeux vidéos), le PHP et SQL (pour la programmation web) ou encore Python (pour la diversité de ses usage et sa facilité d’accès). Ils sont tous définis par des règles précises de syntaxe et par un vocabulaire de base.
 

## Exemples de langages

Ces trois programmes font la même chose, mais nous pouvons voir certaines différences de syntaxe et certaines similitudes dans la structure.

### Javascript

<!-- REVIEW/JPP: utilité var, === et console.log pour du JavaScript plus moderne -->
```javascript
// Test de mot de passe 

let mot_de_passe = "1234";
if (mot_de_passe === "Bonjour") {
  console.log("Le mot de passe est correct");
} else {
  console.log("Le mot de passe est incorrect");
}
```

### PHP

```php
# Test de mot de passe 

$mot_de_passe = "1234";
if ($mot_de_passe == "Bonjour") {
  echo "Le mot de passe est correct";
} else {
  echo "Le mot de passe est incorrect";
}
```

### Python

```python
# Test de mot de passe 

mot_de_passe = "1234"
if mot_de_passe == "Bonjour":
    print("Le mot de passe est correct")
else:
    print("Le mot de passe est incorrect")
```
