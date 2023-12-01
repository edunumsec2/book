# Analyser les données de twitter


Fouiller et analyser de grandes quantités de tweets



```{admonition} Analyser les données de twitter
:class: hint
* Thème : 
* Niveau : `facile`
* Durée : 60-90 minutes
* Objectifs pédagogiques : prendre conscience de la masse de données stockées par les réseaux sociaux et leur usage potentiel et de la puissance de python pour les traiter.
* Modalité : `branché`
* Matériel : Jeu de données [version lourde (1.3Go zippé)](http://mhers.ch/_downloads/twitter_full.zip) ou [version légère (130Mo zippé)](http://mhers.ch/_downloads/twitter_light.zip), un {download}`jupyter notebook <twitter/twitter.ipynb>`, un {download}`tweet au format json <twitter/tweet1.json>`, un {download}`set de tweet au format json <twitter/minute.json>`. Un serveur jupyter doit être disponible pour les élèves, par exemple en installant en local `pip install --user notebook` 
* Prérequis : aucun, mais des connaissances de python utiles. 
* Notions fondamentales : données, métadonnées, analyse de données, données massives, formats de fichier, 
* Taille du groupe : `demi-classe` ou `classe`

```


## Déroulement

|                             | Durée  | Phase de l'activité | 
|-----------------------------|------- |---------------------|
| Introduction                | 5 min  | Mise en situation |
| Qu'y a-t-il dans ton tweet? | 5 min  | Exploration       |
| Anyalyse de tweets          | 30 min | Exploration       |
| Questionnaires              | 5 min  | Objectivation     |
| Discussion                  | 15 min | Discussion        |
| Conclusion                  | 5 min  | Institutionnalisation |

(twitter.intro)=
### Introduction 

En mobilisant des évènements d'actualité et en interrogeant les élèves, l'enseignant
introduit twitter, devenu X, son concept et son histoire. 

### Qu'y a-t.il dans ton tweet?
L'enseignant demande aux élèves d'ouvrir le fichier `tweet1.json` avec firefox. Les élèves peuvent ainsi voir les
différents champs du tweet et leur valeurs, ainsi que le fichier texte brut original. L'enseignant pose certaines
questions sur le tweet en question (sa date de création, son autrice, etc.). L'accent est mis sur le contrast entre
la brièveté du tweet et la quantité d'information qu'il contient.

L'enseignant fait remarqué que la date du tweet correspond aux élections américaines de 2020. 

### Analyse de tweets

Les élèves ouvrent le jupyter notebook. La classe lit et exécute les cellules du notebook, soit de manière
synchronisée avec l'enseignant, soit chaque élève à son rythme. Selon ses objectifs en programmation, on peut
passer plus ou moins de temps à expliquer le code utilisé et faire des demandes plus ou moins précises de
modification du code. 

### Questionnaire

Une fois parvenus au bout du notebook et de l'exploration, les élèves remplissent individuellement un questionnaire. Il peut par exemple contenir les questions suivantes: 
 1. Qu'avez-vous pensé de cette activité?
 1. Y a-t-il quelque chose qui a suscité votre surprise ou votre étonnement?
 1. Pensez-vous que c'est bien de pouvoir accéder à toute ces données? Pensez-vous que c'est légal?
 1. Pensez-vous qu'il est possible d'accéder à des données similaires pour d'autres réseaux sociaux?
 1. Qui a accès à ce type de données pour d'autres réseaux sociaux?
 1. Que pourrait-on faire avec ce type de données pour d'autres réseaux sociaux?

### Discussion

On lance ensuite une discussion basée sur la mise en commun des réponses des élèves. L'enseignant donne ensuite des
exemples positifs et négatifs de l'utilisation des données issues des réseaux sociaux. Par exemple [l'article
scienitifique mesurant la vitesse de propagation des informations vraies ou fausses sur twitter](https://www.science.org/doi/full/10.1126/science.aap9559) ou [l'étude d'Amnesty International](https://www.amnesty.org/fr/latest/news/2023/11/tiktok-risks-pushing-children-towards-harmful-content/) montrant les effets délétères de TikTok. 

En fin de discussion, il peut être utile de mentionner que Twitter permettait un accès relativement aisé (et gratuit)
aux données pour des projets de recherche universitaire, mais qu'avec la reprise du réseau par Elon Musk, il faut
maintenant payer pour avoir accès à ces données. 

### Conclusion

L'enseignant conclut en résumant les messages principaux:
 1. Les données sont une source de savoir et donc de pouvoir.
 1. la programmation est un outil permettant la transformation de données en savoir.
 1. il faut garder un regard critique sur l'utilisation de cet outil. 


## Référence.

Les données sont issues du [Twitter Stream Grab](https://archive.org/details/twitterstream). Ces données ont été sous-échantillonées (ratio 1/4,pour grand jeu de données, ratio 1/40 pour le petit). 
