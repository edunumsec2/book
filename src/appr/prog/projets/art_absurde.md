# Art absurde

Ce chapitre montre la création d'un texte aléatoire. On s'imagine ici l'autobiographie absurde d'un artiste contemporain. Nous allons voir que

- la fonction `nom = choice(liste)` permet de choisir un élément aléatoire dans une liste,
- la **f-string** de forme `f"{nom} est {adj}."` permet d'insérer des variables dans une phrase,
- les variables à insérer doivent être entourées d'accolades `{nom}`.

## Inventer un personnage

Pour inventer un nom d'artiste, il suffit de choisir aléatoirement un prénom et un nom avec la fonction `choice()` et de les combiner avec un **f-string** pour former une phrase.

```{exercise}
Exécutez le programme multiple fois et observez le résultat.
```

```{codeplay}
from random import choice

prenom = choice(('Christopher', 'Ryan', 'Ethan', 'John'))
nom = choice(('Walker', 'Thompson', 'Anderson', 'Johnson', 'Tremblay'))
artiste = choice(('peintre', 'artiste', 'musicien', 'plasticien'))
adjectif = choice(('sublime', 'génial', 'phénoménal', 'controversé'))

phrase = f"{prenom} {nom} est un {artiste} {adjectif}."
print(phrase)
```

## Inventer une introduction

Voici un exemple un peu plus long, avec deux phrases. Les variables `nom` et `prenom` sont utilisées dans les deux phrases pour faire une continuité.

```{exercise}
Exécutez le programme multiples fois et observez le résultat.
```

```{codeplay}
from random import choice

prenom = choice(('Christopher', 'Ryan', 'Ethan', 'John'))
nom = choice(('Walker', 'Thompson', 'Anderson', 'Johnson', 'Tremblay', 
    'Peltier','Cunningham', 'Simpson', 'Mercado', 'Sellers'))

verbe1 = choice(("présenter", "reconstruire",  "questionner",  "interroger", 
    "juxtaposer", "rencontrer", "joindre"))

sujet = choice(("les hétérogénéités", "les consensus",  "les hétérodoxies",
    "les masques", "les conventions", "les subjectivités"))

ville1 = choice(("Bâle", "Amsterdam", "Rotterdam", "Hong-Kong", "Singapour",
    "New-York", "Lausanne",  "Genève",  "Budapest",  "Zürich", "Vevey", 
    "Montreux", "Aigle", "Sion", "Verbier", "Martigny"))

medium = choice(("la poterie", "l'alphabet", "les monstres", "les dinosaures", "l'anglais",
    "les fabriques de sandales", "la guerre", "l'art", "le mouvement néo-classique",
    "le pointillisme", "l'œuvre de Van Gogh", "la musique viennoise", "le cinéma expérimental"))

ville2 = choice(("Bâle", "Amsterdam", "Rotterdam", "Hong-Kong", "Singapour", "New-York"))

phrase1 = f"{prenom} {nom}, {verbe1} {sujet}."
phrase2 = f"Né à {ville1}, {prenom} {nom} découvre {medium} à {ville2}."

print(phrase1)
print(phrase2)
```

## Inventer un paragraphe

La phrase 3 et la phrase 4 forment un paragraphe. Ils sont affiché avec la même fonction `print()`.

```{codeplay}
from random import choice

prenom = choice(('Christopher', 'Ryan', 'Ethan', 'John'))
nom = choice(('Walker', 'Thompson', 'Anderson', 'Johnson', 'Tremblay', 
    'Peltier','Cunningham', 'Simpson', 'Mercado', 'Sellers'))

verbe1 = choice(("présenter", "reconstruire",  "questionner",  "interroger", 
    "juxtaposer", "rencontrer", "joindre"))

sujet = choice(("les hétérogénéités", "les consensus",  "les hétérodoxies",
    "les masques", "les conventions", "les subjectivités"))

ville1 = choice(("Bâle", "Amsterdam", "Rotterdam", "Hong-Kong", "Singapour",
    "New-York", "Lausanne",  "Genève",  "Budapest",  "Zürich", "Vevey", 
    "Montreux", "Aigle", "Sion", "Verbier", "Martigny"))

medium = choice(("la poterie", "l'alphabet", "les monstres", "les dinosaures", "l'anglais",
    "les fabriques de sandales", "la guerre", "l'art", "le mouvement néo-classique",
    "le pointillisme", "l'œuvre de Van Gogh", "la musique viennoise", "le cinéma expérimental"))

ville2 = choice(("Bâle", "Amsterdam", "Rotterdam", "Hong-Kong", "Singapour", "New-York"))
===
ecole = choice(("Académie de peinture de Poitiers", "Ecole des beaux-arts de Nouvelle-Orléans",
    "Ecole de guitaire-couture de Londres", "Académie d'arts appliqués de Boncourt",
    "Atelier de design de Porrentruy"))

annee = choice((1939, 1928, 2002, 2012))
verbe2 = choice(("transcende", "peaufine", "développe", "affine", "précise"))

appetence = choice(("son goût", "sa passion", "son attrait", "son désir", "son attraction", "son penchant"))

sujetsocio = choice(("la lutte des classes", "l'écologie", "le climat", "la montée des eaux",
    "la pauvreté dans le tiers-monde", "les gammes pentatoniques", "la virtuosité des pinguins"))

verbe3 = choice(("marqué", "caractérisé"))

activite1 = choice(("les bacs à sable", "l'énergie éolienne", "les courses d'école",
    "les sandwichs", "l'astronomie", "la mécanique quantique",
    "la preuve de l'existence de Dieu", "la somme théologique de Saint Thomas d'Aquin",
    "les dynamiques sociales en milieux urbains", "l'apprentissage automatique des enfants singes"))

activite2 = choice(("l'électricité", "les conduites d'eau", "la navigation en eaux troubles",
    "les vagues scélérates", "l'école enfantine", "la gymnastique", "la marque Coca-Cola",
    "la danse classique", "l'œuvre de Chopin", "les montagnes russes", "l'extrême-Orient",
    "la dilpomatie des mollahs"))

activite3 = choice(("les panneaux de signalisation",  "l'exercice physique", "la gravitation",
    "le surpoids", "le diabète", "Jean-Jacques Rousseau", "l'âge d'or de l'école schubertienne",
    "les pianos à queue", "les dîners à la campagne", "l'œuvre de Marc Levy"))

phrase1 = f"{prenom} {nom}, {verbe1} {sujet}."
phrase2 = f"Né à {ville1}, {prenom} {nom} découvre {medium} à {ville2}.\n"
phrase3 = f"Son travail est {verbe3} par {activite1} ainsi que par {activite2} et {activite3}."
phrase4 = f"Diplômé de l’{ecole} en {annee}, il {verbe2} {appetence} pour {sujetsocio} à {ville2}."

print(phrase1)
print(phrase2)
print(phrase3, phrase4)
```

## Suite

Voici encore un paragraphe consistant de trois phrases.

```{exercise}
Exécutez le programme multiples fois et observez le résultat.
```

```{codeplay}
from random import choice

prenom = choice(('Christopher', 'Ryan', 'Ethan', 'John'))
nom = choice(('Walker', 'Thompson', 'Anderson', 'Johnson', 'Tremblay', 
    'Peltier', 'Cunningham', 'Simpson', 'Mercado', 'Sellers'))

recherche = choice(("sonde", "interroge", "questionne", "approfondit", 
    "met en lumière", "révèle", "généralise"))

activite4 = choice(("les autotamponeuses dans les milieux défavorisés", "les jeux sociaux des chimpanzés",
    "les stéréotypes de Walt Disney", "les biais algorithmiques"))

conjonction = choice(("À travers", "Grâce à", "Par l'entremise de"))

objet = choice(("cette performance", "cette installation", "ce bric-a-brac de génie",
    "ce coup d'éclat", "cette tentative réussie"))

travail = choice(("son travail", "sa production", "son parcours artistique"))

qualificatif = choice(("urgent", "impératif",  "important", "judicieux", "indispensable"))
actions = "réinvestir", "reconquérir", "renouveller", "transformer", "redécouvrir"
oeuvre = choice(("peintures", "toiles", "fresques", "pièces musicales", "compositions cinématographiques"))

influence = choice(("le Bauhaus", "la Grèce antique", "Picasso", "l'impressionisme",
              "l'école de Vienne", "les maîtres flamands", "le siècle d'or hollandais",
              "le pop-art", "l'Oktoberfest à Munich"))

generiques = "la géométrie",  "l'automne", "la vie", "l'existence", "l'enfance", "l'imaginaire", "l'altérité"

transcendence = choice(("la transcendence", "l'infini", "l'au-delà", "l'appel du vide", "le dasein"))

calme = choice(("calme", "revivifie", "apaise", "condamne", "transforme"))

pratiques = choice(("les pratiques sociales", "les émissions de télé-réalité", 
    "les réseaux sociaux", "les peuplades affamées", "les gens idiots", "les rétrogrades"))

phrase5 = f"L'artiste {prenom} {nom} {recherche} ce qui est induit par {activite4} dans des {oeuvre} inspirées par {influence}."
phrase6 = f"{conjonction} {objet}, {travail}  nous rappelle à quel point il est {qualificatif} de {choice(actions)} {choice(generiques)} à partir de {choice(generiques)}."
phrase7 = f"Son travail propose de {choice(actions)} {choice(generiques)} tandis que {transcendence} {calme} {pratiques}." 

print(phrase5, phrase6, phrase7)
```
