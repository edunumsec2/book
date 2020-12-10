Introduction à la programmation
===============================
 
## Le but  
Notre vie moderne est touchée par les ordinateurs. La communication, la recherche d'information, les divertissements, les processus, les réseaux sociaux ou les object connectés, sont autant d'exemples de choses qui font désormais partie de notre quotidien. En programmant un ordinateur, on se dote d'un outil considérable pour simplifier, multiplier et accélérer certaines actions comme la gestion de réservations pour un grand hôtel, effectuer une quantité importante de calculs dans un projet de recherche et même la bonne réalisation d’une recette de cuisine. 
 
Malheureusement, les ordinateurs ne comprennent pas le langage humain. Les circuits éléctriques qui leur permettent de manipuler une grande quantité d'information en peu de temps ne peuvent traiter que des 0 et des 1. Pour pouvoir donner des ordres à l'ordinateur nous devons utiliser des langages de programmation qui, grâce à leur sintaxe particulière, peuvent être compris des humains et traités par un ordinareur.
 
## Le fonctionnement 
Un programme informatique est une représentation écrite d'une suite d'ordres que l'on veut donner à la machine. On appelle ces ordres des instructions et une suite d'instruction, un algorithme. On distingue plusieurs paradigmes, ou style de programmation différents en fonction du but qu’a le programme. Par exemple, la programmation séquentielle est décrite par une suite d’instructions qui s’exécutent les unes après les autres. La programmation événementielle est représentée par des couples événements-actions qui permettent, après une entrée nommée événement, d’exécuter des instructions. 
 
## Les langages 
Il y a des centaines de langages de programmation différents qui ont souvent une caractéristique leur donnant l’avantage d’être utilisés dans un domaine plutôt qu’un autre. On utilisera par exemple le JavaScript (pour une interface Web), le C# (pour les jeux vidéos), le PHP et SQL (pour la programmation Web) ou encore le Python (pour la diversité de ses usage et sa facilité d’accès). Ils sont tous définit par des règles précises de syntaxe et un vocabulaire. 
 
## Exemples de langages 
Ces trois programmes font la même chose, mais nous pouvons voir certaines différences de syntaxe et certaines similitude dans la structure.

### Javascript

```JavaScript
// Test de mot de passe 

var mot_de_passe = "1234";
if (mot_de_passe == "Bonjour") {
  document.write("Le mot de passe est correcte");
} else {
  document.write("Le mot de passe est incorrecte");
}
```
### PHP

```{code-block} PHP
# Test de mot de passe 

$mot_de_passe = "1234";
if ($mot_de_passe == "Bonjour") {
  echo "Le mot de passe est correcte";
} else {
  echo "Le mot de passe est incorrecte";
}
```

### Python

```{code-block} PHP
# Test de mot de passe 

mot_de_passe = "1234"
if mot_de_passe == "Bonjour":
    print("Le mot de passe est correcte")
else:
    print(Le mot de passe est incorrecte")
```
