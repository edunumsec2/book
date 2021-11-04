# Marche à suivre


1. Dans un nouveau programme python, définir les variables `susceptibles`, `malades`, `gueris`, et `morts` qui représentent respectivement le nombres de personnes susceptibles d'attraper la maladie, le nombre de malades, le nombre de guéris et le nombre de morts de la maladie. On commence avec une population d'un million de personnes dont une seule est malade, aucune n'est guéries et aucune n'est morte de la maladie. Déterminer les valeurs initiales de ces quatre variables.

1. Définir ensuite des variables pour les probabilités suivantes:

    1. la probabilité qu'un malade donné croise et contamine une personne susceptible donnée en l'espace d'un jour
        ```
        p_contamination = 0.00001 # probabilité de contamination
        ``` 
    1. la probabilité qu'un malade donné guérisse en l'espace d'un jour
        ```
        p_guerison = 0.1 # probabilité de guérison
        ``` 
    1. la probabilité qu'un malade donné meure en l'espace d'un jour
        ```
        p_deces = 0.0001 # probabilité de deces
        ```
1. Définir les variables suivantes et trouver comment calculer leur valeur en fonction des variables définies précédemment
    
    1. Le nombre de nouvelles infections en un jour `infections`
    1. Le nombre de guérisons en un jour `guerisons`
    1. Le nombre de décès en un jour  `deces`

    et compléter le code suivant avec 
    ```    
    infections = 
    guerisons = 
    deces = 
    ``` 
    Réfléchir à la cohérence de votre modèle, en particulier pour des valeurs particulières (par exemples 0) de malades et de susceptibles. 

1. En fonction des trois variables définies ci-dessus, calculer les nouvelles valeurs des variables `susceptibles`, `malades`, `gueris` et `morts` après le premier jour et compléter le code suivant en avec le résultat:
    ```
    susceptibles = 
    malades = 
    gueris = 
    morts = 
    ```
    Combien y a-t-il de malades après le premier jour selon ce modèle? Est-ce que cela vous semble cohérent? Sinon, quelle modification pouvez-vous apporter à votre modèle?

    Que peut-on dire du nombre total de personnes (susceptibles, malades, guéries ou décédées) dans votre modèle? Cela vous semble-t-il logique?

1. Placer une boucle `for jour in range(10):` au bon endroit de votre code pour que chaque répétition de la boucle corresponde au passage d'un jour. Attention à bien adapter l'indentation du code. 
    
    Combien y a-t-il de malades après 10 jours? Et après 20 jours?

1. On souhaite tracer la courbe des nouvelles infections. Pour ceci définir (avant la boucle `for`) une liste vide appelée `courbe_infection`. Le premier élément de cette liste contiendra le nombre de nouvelles infections le premier jour, le deuxième le nombre de nouvelles infections les deuxième jours etc. 
Pour remplir cette liste, placer l'instruction 
    ```
    courbe_infection.append(infections) 
    ```
    dans la boucle `for`. 
    
    Afficher le nombre d'infection les dix premiers jours. Est-ce que cela vous semble cohérent? Sinon quelle modification pouvez-vous apporter à votre modèle?

1. Afin de pouvoir utiliser `matplotlib`, un module python pour faire des graphique, ajouter l'instruction suivante en *début* de programme 
    ```
    import matplotlib.pyplot as plt
    ````
1. En utilisant les instructions suivantes en fin de programme, vous devriez pouvoir tracer un graphe des nouvelles infections sur les dix premiers jours.
    ```
    plt.plot(courbe_infection,'-')
    plt.xlabel('jours')
    plt.ylable("nombre d'infections")
    plt.show()
    ```
    Vous pouvez fermer la fenêtre du graphique pour terminer le programme. 

    Modifier le programme pour tracer un graphique du nombre d'infections les 50 premiers jours. 
1. Ajouter l'instruction `plt.savefig('courbe_infection.png')` en fin de programme pour sauvegarder votre graphique dans le fichier nommé dans la parenthèse ci-dessus. 

1. Modifier le programme pour tracer également la courbe des décès sur les 50 premiers jours.

1. Modifier les paramètres du modèle et relancer la simulation. Est-ce que vous observez des choses bizarres? Si oui, essayer d'en déterminer la cause.

1. On souhaite comparer le modèle à l'épidémie de Covid-19 dans le canton de Vaud. Le code suivant vous permet de lire le fichier 'covid_vd.csv' et d'obtenir une liste contenant le nombre de nouveaux cas chaque jour. 
```
import csv
cascumul = []
ncas = []
date = []
with open("covid_vd.csv") as covid_file:
    reader = csv.reader(covid_file)
    for row in reader:
        date.append(row[0])
        if row[4]== '':
            cascumul.append(0)
        else:
            cascumul.append(int(row[4]))
            ncas.append(cascumul[-1]-cascumul[-2])`

``` 
Essayer de trouver les paramètre de votre modèle qui correspondent le mieux à la première vague, puis à la seconde vague. Quelle vague reflète selon vous le mieux la réelle propagation du virus? 
