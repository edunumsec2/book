# La géolocalisation, agrégation, connaissance et pouvoir

Cette activité fait partie d'une série de ressources ayant pour objectif général d'identifier et de discuter des enjeux socio-techniques, politiques et économiques liés à la protection de la vie privée et des données personnelles.

En particulier, le sujet de cette activité est la géolocalisation et ses effets dans l'agrégation des données qui génère de la connaissance et donc du pouvoir.

---- 

```{admonition} La géolocalisation
:class: hint
* Thème : Vie privée et données personnelles
* Niveau : `moyen`
* Durée : 2 périodes - Travaux pratiques
* Objectifs pédagogique : Comprendre la précision de la géolocalisation à partir de ses données. 
Analyser le pouvoir de la géolocalisation et de son impact sur la qualité de vie privée et professionnelle.
* Modalité : Branchée - Utilisation de l'ordinateur pour analyser des données récoltées
* Matériel : Utilisation de la plateforme [Digipower Academy](https://digipower.academy/experience/google)
* Prérequis : Activation de la géolocalsation et collecte des données selon le protocole défini ci-dessous
* Notions fondamentales : géolocalisation, agrégation, travail numérique, management algorithmique 
* Taille du groupe : demi-classe

```

## Déroulement

|     Etape                             | Durée  | Phase de l'activité   | 
|---------------------------------------|------- |-----------------------|
| {ref}`Préparation <geolocalisation.preparation>`  | N.A. | Préparation |
| {ref}`Récupération des données <geolocalisation.recuperation>`  | N.A. | Préparation |
| {ref}`Introduction <geolocalisation.introduction>`  | 5-10 min | Préparation |
| {ref}`Analyse et exploration des données de géolocalisation <geolocalisation.exploration>`  | 30-35 min | Analyse |
| {ref}`Étude d'un cas pratique<geolocalisation.cas_pratique>` | 20-25 min | Présentation / Analyse|
| {ref}`Conclusion<geolocalisation.conclusion>` | 10-15 min| Institutionnalisation |


(geolocalisation.preparation)=
### Préparation

*min 1 semaine avant la séquence*

Afin de rendre cette séquence la plus interactive et personnalisée possible, l'enseignant·e invitera les élèves à activer la géolocalisation Google en suivant ce [protocole](https://github.com/hestiaAI/data-catalog/blob/main/workshop/enable-google-location-tracking.md) au moins 1 semaine avant la séquence.  
Il est important de vérifier que l'activation a bien fonctionné. Pour cela, les élèves pourront ouvrir https://timeline.google.com/ quelques minutes après l’avoir effectuée afin de vérifier que des données s’affichent.

Un certain nombre d'élèves ne pourront pas ou ne voudront pas le faire (contrôle parental, pas de compte Google, idéologie, etc.), il n'est pas utile de chercher à avoir le 100% de participation, si uniquement quelques élèves le font, cela permettra déjà d'alimenter la discussion.

Les objectifs de cette séquence sont les suivants : 
1. Définir la géolocalisation à partir de ses données
2. Analyser le pouvoir de la géolocalisation permettant d’acquérir des connaissances de manière agrégée sur une population
3. Prendre connaissance de l’impact de la géolocalisation au-delà de la vie privée, dans la vie professionnelle et sa qualité de vie
4. Saisir la valeur de ses données personnelles lorsqu’elles sont sous le contrôle de l’individu et de la société, et non d’une app
5. Comprendre le contrôle de ses données à l’échelle sociale comme un enjeu de pouvoir
6. Acquisition des concepts clés : géolocalisation, agrégation, travail numérique, management algorithmique


(geolocalisation.recuperation)=
### Récupération des données 

*1-2 jours avant la séquence*

Le protocole de récupération des données suivant devrait être fait en amont de la séquence, car la réception et le téléchargement de ces données peut prendre un peu de temps.
````{figure} media/GoogleTakeout3.png
---
height: 200px
name: fig-googletakeout1
align: center
---
Délai de récupération.
````

Pour récupérer les données, il faut se rendre sur [Google Takeout](https://takeout.google.com/takeout/custom/location_history)

````{figure} media/GoogleTakeout1.png
---
height: 400px
name: fig-googletakeout1
align: center
---
Étape 1.
````

A l'étape 1, si plusieurs choix sont possibles, assurez-vous que seul l'*Historique des positions* soit sélectionné.
Passer à l'étape suivante.

````{figure} media/GoogleTakeout2.png
---
height: 400px
name: fig-googletakeout2
align: center
---
Étape 2.
````
A l'étape 2, choisir *Exporter une fois* et le format de fichier *ZIP*.
La taille de fichier peut être limitée à *1 Go*, mais laisser la valeur par défaut ne devrait pas avoir d'impact puisqu'elle n'intervient que si la quantité de données est très importante.
Cliquer sur *Créer une exportation* et attendre l'email.

````{figure} media/GoogleTakeout4.png
---
height: 400px
name: fig-googletakeout4
align: center
---
E-mail de récupération.
````
L'e-mail annonçant que les données sont disponibles contient un bouton *Télécharger vos fichiers* qui lance le téléchargement et redirige vers la page de gestion de vos exportations et lance le téléchargement du fichier.

````{figure} media/GoogleTakeout5.png
---
height: 400px
name: fig-googletakeout4
align: center
---
Gestion des exportations.
````
Le fichier ainsi téléchargé devrait être de la forme *takeout-yyyymmddTXXXXX-001.zip*, il ne faut **pas le décompresser**.

(geolocalisation.introduction)=
### Introduction 

*Durée : 5-10 min*

L'enseignant·e introduit la notion de géolocalisation en questionnant les élèves sur ce que ça représente et comment elle est mise en œuvre selon eux/elles.

Questions pour animer la discussion :
- Comment voyez-vous la géolocalisation sur votre téléphone ? 
- Dans quel format elle est collectée ?

````{admonition} Proposition de définition 
Les données de géolocalisation sont des données provenant de l'appareil d'une personne qui indiquent l'emplacement géographique de cet appareil, y compris les données GPS, les données relatives à la connexion avec l'équipement wifi local ou même bluetooth.
````



(geolocalisation.exploration)=
### Analyse et exploration des données de géolocalisation

*Durée : 30-35 min*

Afin d'analyser les données récupérées au préalable (cf {ref}`Récupération des données <geolocalisation.recuperation>`) l'enseignant·e utilisera la plateforme [Digipower Academy](https://digipower.academy/experience/google).

````{figure} media/DigipowerAcademy1.png
---
height: 400px
name: fig-digipower1
align: center
---
Interface Digipower Academy pour l'analyse des données Google Takeout.
````
La démonstration des possibilités d'analyse pourra se faire en utilisant les données de l'enseignant·e ou bien utiliser l'exemple disponible par défaut *google-takeout.zip*. Une fois les données choisies, cliquer sur *EXPLORE YOUR DATA*.

````{admonition} A noter
Aucune des donnée utilisée n'est transmise, toute l'analyse se fait au sein du navigateur.
````

Voici quelques éléments que l'enseignant·e peut discuter avec les élèves en se basant sur l'analyse de données de Google maps via digipower :

**Des prédictions algorithmiques**  

En s'appuyant sur la carte, sur une adresse voir *placeVisitImportance MAIN*, indique qu'une personne se rend fréquemment à cet endroit, ainsi les probabilités augmentent que ce lieu soit son domicile principal.

````{figure} media/DigipowerAcademy2.png
---
height: 400px
name: fig-digipower2
align: center
---
Onglet *PLACES VISITED*
````

On peut voir aussi que Google identifie le moyen de transports, à pied, voiture, bus, vélo, et également bateau...
On voit par ex. sur la carte un trajet traversant le lac, cela peut indiquer que l'utilisateur a *indiqué* le moyen de transport avec une recherche sur les horaires ou un site de billetterie en ligne. Il se peut aussi que Google soit capable de prédire le moyen avec l'analyse de la vitesse via le téléphone qui contient un accéléromètre.

Il y a finalement un niveau de confiance de la prédiction par Google, avec un score ou un niveau (par ex. 89 pour une adresse MAIN ou HIGH pour le transport en bateau). 

````{figure} media/DigipowerAcademy3.png
---
height: 400px
name: fig-digipower3
align: center
---
Onglet *TRAVELS*
````

Quand on est sur digipower on peut regarder ce qui se passe dans les différents onglets, chaque onglet a différentes vues sur les données et statistiques, on peut utiliser:

- **Trips** : pour parler de multimodalités et transfert modal, et de l'utilité de ces données pour les politiques publiques
- **Wifi** : près du petit chêne par ex. pour parler sur l'écoute de réseaux wifi pour contribuer a la géolocalisation
- **Other candidates** : pour vraiment détailler la précision de la surveillance, et comment elle fonctionne - y compris dans ses aspects sociaux.

Pour avoir plus d'informations, utiliser les [personas](https://digipower.academy/story/zoe-moves-around-the-city).

Cela montre le pouvoir d'acquisition des connaissances sur une personne à partir de la géolocalisation.



**Des considérations et des questionnements ouverts**  

 - Quelle est la vue qu'ont les élèves, et les habitant.e.s en général, sur leur ville ?  
 On peut d'abord mentionner les moyens que Google utilise pour cartographier la ville : satellites, voitures avec caméras, les commerces peuvent payer et indexer leur site sur Google Maps.  
 On peut ensuite ouvrir la discussion en demandant si les élèves ont déjà identifié des erreurs dans les itinéraires proposés par Google ?  
 Est-ce que Google connaît toutes les petites rues de leur ville ?  

- Il ne s'agit pas uniquement de la position d'une personne, c'est également l'apprentissage sur tout son entourage.  
Google connaît les déplacements des individus et ses interactions avec son environnement. Par exemple, les données de géolocalisation peuvent être utilisées pour des tâches algorithmiques comme l'analyse de la circulation en temps réel, l’estimation des vitesses durant des embouteillages et la proposition de déviations de route, mais aussi une proposition de restaurant proche...  

- Avec la proposition de routes multimodales Google demande aussi maintenant des compléments informations.  
Par exemple, après avoir pris un bus, Google demande quelle est la température dans le bus, s'il y a un contrôle de sécurité, une estimation du taux d'occupation dans le bus, etc.  
Plus l'humain enrichit la géolocalisation, plus Google peut apprendre sur la société en général.  

- Google croise aussi des informations avec d'autres applications qui utilisent Google Maps (par ex. Uber, Tinder, CFF).  
Beaucoup d'autres apps installent Google Maps via des SDK ce qui permet à Google de connaitre les habitudes sur l'espace physique avec des intérêts en ligne.  
Par exemple, si on a cherché une recette de lasagne sur Google, qu'on s'est rendu à la Migros plus proche pour acheter des ingrédients, puisqu'on a publié une photo chez nous sur Instagram et on a donné 5 étoiles à la Migros avec un commentaire qui se trouve indexé sur Google Maps avec notre pseudonyme affiché.  

- Finalement quelques questions pour ouvrir la discussion : 
    - Qu'est-ce qui se passe si Google te suit en permanence, et aussi tes parents et toute ton école ? 
    - Qui a le plus d'information sur toi, tes parents ou Google ? 
    - Qui a plus de pouvoir ? 
    - Qu'est-ce qui se passe si d'autres personnes accèdent à ces infos agrégées ?

(geolocalisation.cas_pratique)=
### Cas Pratique : *Les chauffeurs UBER*

*Durée : 20-25 min*

Dans cette partie, l'enseignant·e retracera l'affaire *des chauffeurs Uber* en Suisse et principalement à Genève et pourra s'appuyer pour cela sur les dias disponibles {download}`ici<media/ChauffeurUber.pdf>`.
Pendant l'exposé de cette affaire, l'enseignant·e pourra amener et ouvrir le débat sur les sujets suivants :
- Des chauffeurs *indépendants* et *autonomes*
- Uber, *technologie intermédiaire et neutre*
- La lutte des chauffeurs Uber au niveau mondial : sont-ils des employés ?
- Comment définiriez-vous le temps de travail des chauffeurs Uber ?

Finalement, la résolution de cette affaire a pu se faire en partie grâce à l'analyse des données de géolocalisation récupérées chez Uber qui a pu servir comme preuve du temps de travail et des revenus précis des chauffeurs. De plus, ces données servent à démontrer l'existence d'une gestion algorithmique de l'attribution des courses et donc de l'existence d'une relation employeur-employé. 

(geolocalisation.conclusion)=
### Conclusion

*Durée : 10-15 min*
La conclusion et les objectifs de cette séquence tourne autour de 2 points principaux :

1. Le contrôle de ses données personnelles a une valeur économique et un pouvoir pour négocier de manière collective sur les décisions politiques qui nous affectent.
2. Récupérer ses données permet de gagner en transparence et de renverser l’asymétrie d’information dominante qu’une plateforme a avec ses utilisateurs.
 
---

Activité réalisée en collaboration avec [Dr. J. Pidoux](https://doi.org/10.5075/epfl-thesis-8830), [PersonalData.IO](https://personaldata.io/) et leur partenaire technologique [Hestia.ai](https://hestia.ai/)