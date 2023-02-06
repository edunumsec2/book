# Corrigé


```python
import matplotlib.pyplot as plt
import csv
```


```python
susceptibles = 100000
malades = 1
gueris = 0
morts = 0
```


```python
p_contamination = 0.000005 # probabilité de contamination par jour, prendre 0.2 pour la version avancée
p_guerison = 0.1 # probabilité de guérison par jour
p_deces = 0.0001 # probabilité de deces par jour
nb_rencontre = 10 # nombres de personnes rencontrées en moyenne par jour (avec lesquelles une transmission serait possible)
```


```python
courbe_infection = []
duree = 50 # nombre de jours consideres
```


```python
for i in range(duree):

    # modele de base 
    infections = p_contamination * malades * susceptibles
    guerisons = p_guerison * malades
    deces = p_deces * malades

    ## une version un peu plus élaborée qui tient compte du pourcentage de malades
    ## dans nos contacts plutôt que du nombre total de malades pour déterminer le risque d'être infecté. 
    # infections = p_contamination * malades/(malades+gueris+susceptibles) *nb_rencontre * susceptibles


    # pour éviter les nombres négatifs dus à la méthode d'Euler (à ajouter ensuite)
    infections = min(infections,susceptibles)
    deces = min(deces,malades)
    guerisons = min(guerisons,malades)


    susceptibles = susceptibles - infections
    malades = malades + infections - deces - guerisons
    morts = morts + deces
    gueris = gueris + guerisons
    courbe_infection.append(infections)

```


```python
# on imprime le nombre de personne appartenant a chaque categorie
print("Susceptibles:", susceptibles)
print("Malades:", malades)
print("Guéris:", gueris)
print("Morts:",morts)
```

    Susceptibles: 1266.2603561594362
    Malades: 19853.258506438633
    Guéris: 78802.678458943
    Morts: 78.80267845894298



```python
# on fait un graphic du nombre d'infections
plt.plot(courbe_infection,'-')
plt.xlabel('jours')
plt.ylabel("nombres d'infections")
plt.show()

```


```python
cascumul = []
ncas = []
date = []
```


```python
with open("covid_vd.csv") as covid_file:
    reader = csv.reader(covid_file)
    for row in reader:
        date.append(row[0])
        if row[4]== '':
            cascumul.append(0)
        else:
            cascumul.append(int(row[4]))
            ncas.append(cascumul[-1]-cascumul[-2])
```

```python
# on affiche la vraie courbe
plt.plot(cascumul)
plt.show()
```
