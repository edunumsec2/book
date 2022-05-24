# Titre

---- 

Description de l'activité

----

```{admonition} Caractéristiques
:class: hint

* Nom : 
* Durée : 
* Thème : 
* Objectifs d’apprentissage : 
* Notions fondamentales : 
* Approche pédagogique : 
* Matériel : 
* Niveau : 
* Mots-clés : 
* Dynamique (groupe / individuel) : 
* Taille du groupe : 
```

```{dropdown} **Déroulement**

*note : les catégories ci-dessous sont des exemples*

1. **Mise en situation générale** (5-10 mn) autour du concept de l'archivage traditionnel, son histoire, son utilité, son organisation, ce qu'il a permis comme pratique, et la fonction fondamentale du tri dans cette technique

1. **Exploration** (20-30 mn) en groupe au cours de laquelle les élèves explorent des procédures de tri induites par un dispositif physique

1. **Mise en commun** (15 mn) au cours de laquelle les élèves discute et présentent les résultats de
leurs recherche

1. **Formalisation (et institutionnalisation)** (20 mn) des divers algorithmes de tri. 

1. **Exercices (ou exemples)** (10-15 mn) d'application des algorithmes.

1. **Conclusion** (5-10 mn) en bouclant la boucle sur l'archivage informatisé et les pratiques (positives et négatives) qu'il permet.

```

## Mise en situation générale

*Durée : 5-10 mn*


## Exploration

*Durée : 20-30 mn*


## Mise en commun

*Durée : 15 mn*


## Formalisation

*Durée : 20 mn*


### Tri à bulles
```
répeter jusqu'à courant.vide():
    courant.mettre(haut)
    répéter jusqu'à courant.vide():
        courant.mettre(haut)
        droite.disposer(petit,au-dessous)
    gauche.disposer(seul,au-dessus)
    droite.courant()
gauche.courant()
```    
### Tri par insertion
```
répéter jusqu'à courant.vide():
    courant.mettre(haut)
    gauche.classer()
gauche.courant()
```

### Tri par pivot (quicksort)
````
répéter tant qu'il y des tas avec au moins deux cartes:
    courant.mettre(haut, gauche):
    initier(gauche)
    initier(droite)
    répéter jusqu'à courant.vide():
        courant mettre(haut,droite)
        si plus grand que (G>D):
            disposer(petite, gauche)
        sinon
            disposer(grande, droite)
    disposer(seule,courant)
    déplacer le marqueur vers le tas avec au moins 2 cartes le plus à droite
superposer tous les tas de gauche à droite.
````

```{admonition} Remarque
Le tri par sélection n'est pas vraiment adaptés à ce dispositif physique basé sur les
piles. Une variante de l'activité consisterait à donner au autre dispositif basé sur les tableaux à une partie de la classe afin de faire émerger ces algorithmes. 
```
 

## Exercices

*Durée : 10-15 mn*


## Conclusion

*Durée : 5-10 mn*

