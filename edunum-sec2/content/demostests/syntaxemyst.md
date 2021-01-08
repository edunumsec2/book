# Syntaxe MySt

````{admonition} Important
:class: caution
Pour voir la syntaxe MySt brut, ouvrir le document dans un éditeur markdown. 
````

### Encart

> Note : dans tout ce qui suit, on peut remplacer les "`" par des ":". 

```{admonition} Mon titre
:class: tip
Mon contenu
```
(optencarts)=
#### Optimisations des encarts

* les styles `:class:` disponibles sont : `note, warning, tip, caution, attention, danger, error, hint, important`.

* il est possible de *nester* des encarts dans des encarts. Pour cela, en lieu et place du contenu, ajouter la même syntaxe que pour déclarer l'encart de base, mais en diminuant le nombre de "`". Exemple ci-dessous. 

````{admonition} Mon titre
:class: tip
```{admonition} Mon sous-titre
:class: note
Mon contenu de sous-titre
```
Mon contenu
````

* on peut ajouter une fonction dropdown à un encart, en déclarant `dropdown` après la déclaration `admonition` dans les curly brackets. Attention : pour une raison que j'ignore, dans le cas des dropdowns, il faut déclarer la `class`juste après la déclaration `dropdown`. Exemple ci-dessous : 

::::{admonition,dropdown} Cliquez-ici
Voilà le contenu du dropdown. Attention ! Je ne sais pas pourquoi mais le dropdown ne fonctionne que quand on utilise les ":", à la place des "`" pour déclarer notre encart...
::::

* tous les contenus présents dans les encarts peuvent être stylisés avec la syntaxe élémentaire du Markdown pour la stylisation des polices de caractères (*italiques*, **gras**, etc.).

* on peut ajouter des images dans les encarts de la façon suivante. *Note : pour l'utilisation des images se référer au {ref}`chapitre sur les images et figures <imagesetfigures>`. 

````{admonition} Mon titre
:class: tip
```{image} images/img1.png
```
Mon contenu
````

### Contenus en marge

````{sidebar} Titre du contenu en marge
Contenu en marge
````
#### Optimisations des contenus en marge

* on peut ajouter des encarts à l'intérieur des contenus en marge, selon la syntaxe décrite ci-dessus. Exemple : 

````{sidebar} Titre du contenu en marge
```{admonition} titre de l'encart en marge
:class: caution
n'oubliez pas de respectez les contraintes de mise en forme des encarts
```
Contenu en marge
````
* on peut utiliser les fonctions dropdown décrites ci-dessus également en marge.

* on peut insérer des images dans les contenus en marge de la même façon que dans les encarts.

### Références et labels

* pour créer une référence à un autre chapitre, sous-chapitre, image, figure, etc., je dois d'abord labeliser la cible de la référence de la façon suivante : 

1. Si c'est un titre, je peux procéder ainsi au moment où je déclare le titre dans mon document : 

(lelabelquejesouhaitedonner)/=
/### Le titre que je souhaite référencer 

Note : les "/" qui précèdent le signe "=" et la déclaration du niveau de titre n'ont d'usage que de désactiver les fonctions concernées... Il faut les enlever dans votre version. 

2. Si c'est tout autre élément de contenu (équation, image, figure, encart, etc.), je vais simplement utiliser la déclaration `:name:` exactement de la même manière que j'ai utilisé la déclaration `:class:`dans les encarts. {ref}`Voir ici <optencarts>`. 

* quand j'ai labelisé ma cible, je peux l'appeler en utiliser la syntaxe : {ref}`le texte qui renvoie à la réf <lelabeldelaref>`. 

* il existe des subtilités de syntaxe plus détaillées [à voir ici](https://jupyterbook.org/content/citations.html)


(imagesetfigures)= 
### Images et figures

* on insère une image de la façon suivante : 

```{image} images/img1.png
:alt: titreimage1
:width: 200px
:align: center
```
#### Optimisations de l'image

* les déclarations communes sont : `alt, width, height, align`. Auxquelles on peut ajouter `name`si on veut labeliser l'image. `align` prend trois positions : left, center, right. 

* le chemin relatif de l'image commence dans le dossier où est stocké le fichier actif. 


### Blocs de code

* les blocs de code se déclarent comme des encarts, mais en spécifiant le language mis en avant, juste après les curly-brackets de la déclaration de l'encart. 

```{code-block} python
a = 2
print('voilà un print')
```

* on peut numéroter les lignes de codes avec la déclaration `lineno-start`. 

* on peut mettre l'emphase sur certaines lignes avec `emphasize-lines`. 

* voilà un exmple qui résume le tout. 

```{code-block} python
---
lineno-start: 10
emphasize-lines: 1, 3
---
a = 2
print('voilà un print')
print('voilà un deuxième print')
```