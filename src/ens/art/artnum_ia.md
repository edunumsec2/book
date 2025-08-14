# Art numérique et intelligence artificielle

---- 

Cette activité s'inscrit dans une série de ressources visant à explorer les relations entre l'art et l'informatique. Elle vise particulièrement à mettre en lumière les enjeux sociaux de l'intelligence artificielle générative.

---- 

```{admonition} Enjeux sociaux de l'IA générative
:class: hint

* Thèmes : Intelligence artificielle & Art numérique
* Niveau : `moyen`
* Durée : 2 périodes 
* Objectifs pédagogiques : Connaître les 4 périodes de l'art numérique. Être capable de prédire le comportement d'une IA générative avec un *prompt*. Créer une œuvre d'art numérique à partir d'un sujet défini. Illustrer quelques enjeux sociaux des GANs
* Modalité : `branchée`
* Matériel : {download}`Diffusionbee <https://diffusionbee.com/download>`
* Prérequis : Notions fondamentales sur l'IA
* Taille du groupe : `demi-classe`

```

## Déroulement

|     Étape                             | Durée  | Phase de l'activité   | 
|---------------------------------------|------- |-----------------------|
| {ref}`Installation de DiffusionBee <diffusionbee>` |  | Préparer |
| {ref}`Histoire de l'art numérique <historique>`  | 15 min | Découvrir |
| {ref}`Prompt battle <prompt.battle>`  | 20 min | Analyser |
| {ref}`Création d'une œuvre d'art numérique <creation>` | 25 min | Appliquer
| {ref}`Discuter des enjeux sociaux des GANs <enjeux.sociaux>` | 25 min | Discuter
| {ref}`Conclusion <ia.conclusion>` | 5 min | Réfléchir


(diffusionbee)=

## Installation de Diffusionbee

*Durée : variable*

Pour cette activité, vous aurez besoin du logiciel open-source et gratuit {download}`Diffusionbee <https://diffusionbee.com/download>`, basé sur le moteur d'IA générative StableDiffusion. Il est recommandé de l'installer sur toutes les machines des élèves avant le début du cours pour optimiser le temps à disposition.


Une IA générative nécessite un réseau de neurones artificiels pré-entraînés, également appelé modèle dans l'univers de **Diffusionbee**. La version de base de **Diffusionbee** ne comprend qu'un seul modèle par défaut. Cependant, il est possible d'ajouter des modèles pré-entraînés en les téléchargeant depuis l'un des deux principaux sites suivants :

* [https://huggingface.co](https://huggingface.co/)
* [https://civitai.com](https://civitai.com/)

Une fois téléchargés, les modèles doivent être importés dans **Diffusionbee** (Menu -> Paramètres -> Ajouter de nouveaux modèles). Ils peuvent ensuite être utilisés en spécifiant dans les options de création d'image le modèle que vous souhaitez utiliser.


**Diffusionbee** offre deux modes d'utilisation :

A. Mode *Image to Image*

Ce mode permet de créer une œuvre d'art à partir d'une image fournie à l'IA. En utilisant un *prompt*, il est possible de demander à l'IA de générer une nouvelle image.

Exemple : Transformer une image de Taylor Swift en version cubiste. En utilisant le *prompt* "*Pablo Picasso cubist remove background*" et les options fournies sur l'image 0, on passe de l'image 1 à l'image 2.


````{figure} media/ia.options.png
---
height: 300px
name: fig-tiktok.png
align: center
---
Image 0
````


````{figure} media/ia.taylor.png
---
height: 300px
name: fig-tiktok.png
align: center
---
Image 1 
<br> 
© AGENCE / BESTIMAGE
````

````{figure} media/ia.taylorpicasso.png
---
height: 300px
name: fig-tiktok.png
align: center
---
Image 2 
````

B. Mode *Text to Image*

Ce mode de création permet de générer une image à partir d'un *prompt* textuel. C'est ce mode que nous utiliserons pour les activités à venir. La génération d'une image prend environ 1 minute.

Les options sont cruciales et peuvent considérablement influencer le résultat final. Il est notamment important de choisir :

* Le **style** de l'image (dessin, photo, type de caméra, type d'éclairage, etc.).
* La **taille** de l'image : Par défaut, elle est de 512x512 pixels. Pour les premiers essais, vous pouvez réduire cette taille à 256x256 pixels, ce qui accélérera la production de l'image jusqu'à 4 fois.
* Le **modèle** (réseau de neurones artificiels pré-entraîné) que vous souhaitez utiliser.

Ce que vous spécifiez dans le *prompt* est essentiel pour la qualité de l'image générée.

Exemple : En utilisant le *prompt* "*Astronaut riding a unicorn, best quality, masterpiece, ulta-high res, photorealistic*" et le modèle *PicxReal_1*, on obtient l'image 3 : 

````{figure} media/ia.licorne.png
---
height: 300px
name: fig-tiktok.png
align: center
---
Image 3 
````

(historique)=

## Histoire de l'art numérique

*Durée : 15 minutes*

Pour commencer le cours, l'enseignant·e propose un bref survol de l'histoire de l'art numérique (*digital art*). Les historiens de l'art numérique distinguent quatre périodes clés qui ont contribué à l'émergence de l'art génératif que nous observons aujourd'hui :

1. Jusqu'en 1960 (les machinistes) : les machines mécaniques (Tinguely)
2. 1960-1990 (les ingénieur·e·s) : le *computer art*
3. 1990-2015 (les internautes) : l'essor du *net art* avec la démocratisation d'internet 
4. à partir de 2015 (les artistes) : l'intelligence artificielle, l'apprentissage automatique et l'art génératif

### Jusqu'en 1960 : les machines mécaniques

Les années 1950 ont été marquées par l'émergence des machines de Tinguely. L'image 4 présente la machine Meta-Matic N°10 de Jean Tinguely, un artiste suisse né en 1925 et décédé en 1991. Il s'agit d'une sculpture mécanique animée, aujourd'hui conservée au Musée Tinguely de Bâle.

````{figure} media/ia.machinistes.png
---
height: 300px
name: fig-tiktok.png
align: center
---
Image 4 
<br>
[Source](https://comgraph.hear.fr/surkrut/author/marisol/)
````

### 1960-1990 : Le *computer art*

Le *computer art* englobe toutes les formes d'art visuel créées à l'aide d'un ordinateur. Il nous ramène à l'histoire de l'informatique et aux types de machines disponibles dans les années considérées (1960-1990). Les artistes ont conçu des dispositifs qui leur permettaient de dessiner, car les imprimantes de l'époque ne pouvaient pas produire des œuvres d'art directement. À noter que bon nombre de ces artistes étaient aussi des ingénieurs et des informaticien·ne·s capables de programmer les ordinateurs pour créer de l'art.

````{figure} media/ia.computerart1.png
---
height: 300px
name: fig-tiktok.png
align: center
---
Image 5 
````

````{figure} media/ia.computerart2.jpg
---
height: 300px
name: fig-tiktok.png
align: center
---
Image 6 
````

### 1990-2015 : Le *net art*

Les années 1990 marquent la naissance du World Wide Web au CERN à Genève. Initialement réservé aux scientifiques et chercheur·se·s, il a rapidement été adopté par le grand public, y compris les artistes.

La Russe Olia Lialina est parmi les premières à saisir l’occasion d’utiliser ce nouvel outil.

````{figure} media/ia.netart.png
---
height: 300px
name: fig-tiktok.png
align: center
---
Image 7 
<br>
 © Olia Lialina
````
Pendant ces 25 années, les technologies de vision artificielle ont connu une croissance exponentielle. Au début des années 2000, les premiers grands réseaux de neurones artificiels, notamment le *deep learning*, ont émergé et ont bénéficié des progrès technologiques pour se développer. Parmi ces nouveaux modèles informatiques, on trouve les réseaux antagonistes génératifs (GAN), où deux réseaux sont mis en compétition selon la théorie des jeux. Dans ce jeu à somme nulle, le premier réseau génère une image tandis que le second tente de discriminer le résultat entre une image réelle et une image générée, le gain étant partagé intégralement entre les adversaires.

### À partir de 2015 : L'IA, l'apprentissage automatique et l'art génératif 

Pour créer des œuvres d’art avec de l’IA générative, on utilise un logiciel dit *text-to-image* qui produit une image à partir d’un texte qu'on appelle *prompt*. 

Exemple : l'image 8 représente un portrait généré par une IA générative. D'autres exemples sont disponibles sur [thispersondoesnotexist.](https://thispersondoesnotexist.com)


````{figure} media/ia.thispersondoesnotexist.png
---
height: 300px
name: fig-tiktok.png
align: center
---
Image 8 
<br>
 [Source](https://thispersondoesnotexist.com)
````
(prompt.battle)=

## *Prompt battle*

*Durée : 20 minutes*

**Frontal**

Avant de lancer une *prompt battle*, l'enseignant·e introduit aux élèves la notion de *prompt* comme l'ensemble des éléments textuels donnés à l'IA pour créer une œuvre. Il met en garde les élèves sur les points suivants :

* Le *prompt* est toujours en anglais (utilisation d'un traducteur en ligne si nécessaire)
* La précision est essentielle
* Chaque élément de l'image doit être séparé par une virgule
* Il est recommandé de respecter un ordre précis : **Quoi** (ex. : *A private house by the sea*), **Détails** (ex. : *Black man wearing a hat*), **Comment** (ex. : *Children's draw, photorealistic, using a Canon EOS 90D*), **Flags models** (ex. : *dvArchGothic*), etc.
* Deux types de *prompt* sont distingués :
  - **Le *prompt* positif** : Il décrit ce que vous souhaitez inclure dans votre création, comme les objets, les personnes, les couleurs, etc. (ex. : *A sunny beach with palm trees, a couple walking hand in hand, a clear blue sky*).
  - **Le *prompt* négatif** : Il permet d'ajouter des termes que vous ne voulez pas voir dans votre création. (ex. : *No rain, no clouds, no city buildings*). **Attention** : sur **Diffusionbee**, il doit être activé pour pouvoir l'utiliser (Options > Negative prompt > Enable).

**Exercice**

Une fois la notion de *prompt* introduite, l'enseignant·e lance la *prompt battle* !

Pour commencer, l'enseignant·e affiche l'image 9 aux élèves.

````{figure} media/ai.promptbattle.png
---
height: 300px
name: fig-tiktok.png
align: center
---
Image 9
````

L'enseignant·e demande ensuite aux élèves de trouver le *prompt* (positif et négatif) qui permettrait de générer une image similaire à l'image 9. Les élèves doivent essayer de reproduire au mieux cette image en utilisant le modèle par défaut de l'IA générative.

Une fois que les élèves ont soumis leurs *prompts* et généré leurs images, l'enseignant·e affiche le travail de certains d'entre eux. Ensemble, les élèves comparent les images générées et analysent les *prompts* utilisés. Iels discutent ensemble pour déterminer quelle image se rapproche le plus de l'image de référence (image 9).

(creation)=

## Création d'une œuvre d'art numérique 

*Durée : 25 minutes*

**Exercice**

L'enseignant·e demande aux élèves de créer une œuvre en suivant les étapes suivantes : 

1. Choisir un thème : 
    * Option 1 : mon auto-portrait
    * Option 2 : un paysage que j'apprécie en l'an 2300
2. Préparer mon *prompt*
3. Créer une image à l'aide de **Diffusionbee**
4. Modifier l'image à l'aide de **GIMP**
5. Écrire un texte qui décrit mon œuvre (pourquoi?)
5. Rendre mon travail au format png avec le texte qui l'accompagne (par ex. sur moodle ou par mail)


(enjeux.sociaux)=

## Discuter des enjeux sociaux des GANs

*Durée : 25 minutes*

Nous vous proposons ci-dessous quelques pistes pour alimenter une discussion autour des enjeux sociaux liés aux IA génératives avec les élèves.

**La propriété intellectuelle**

* D'où proviennent les images qui ont nourri l'IA ? 
* Qui est responsable de garantir que les images utilisées respectent les droits d'auteur ?
* À qui appartiennent les images générées par l'IA ? 
* Y a-t-il un propriétaire légitime ?
* Comment pouvons-nous concilier la créativité de l'IA avec le respect des droits de propriété intellectuelle existants ?

**Biais de l'IA**

L'enseignant·e fait défiler des portraits de [thispersondoesnotexist](https://thispersondoesnotexist.com) et demande aux élèves ce qu'iels observent ? 

* Qu'est-ce qui rend ces portraits particuliers ? 
* Quels sont les risques de biais lors de la création d'images par des IA génératives ?
* Quels types de biais voyez-vous ?
* Comment les biais sociétaux se reflètent-ils dans les productions de l'IA ?
* Comment pouvons-nous atténuer les biais dans les IA génératives ?

**Est-ce de l'Art ?**

* Quelle est la définition de l'art selon vous ? 
* Les créations de l'IA peuvent-elles être considérées comme de l'art ?
* En quoi la nature générative de l'IA remet-elle en question nos conceptions traditionnelles de l'art ?
* Quels critères pourrions-nous utiliser pour évaluer si une création générée par une IA est considérée comme de l'art ?
* Comment l'aspect non humain de la création affecte-t-il notre perception de sa valeur artistique ?

**Éthique de l'IA générative**

Éthique informatique :

   * Les IA génératives sont-elles généralement accessibles en open source ? Sont-elles considérées comme des boîtes noires ?
   * Quelles mesures sont prises pour assurer la transparence du fonctionnement des IA génératives ?

Éthique numérique :

   1. D'où proviennent généralement les images utilisées pour entraîner les réseaux des IA génératives ?
   2. Qui est responsable de la labellisation des images d'entraînement, et quelles sont les implications éthiques de ce processus ?

Éthique des usages :

   1. À quelles fins les créations générées par l'IA sont-elles principalement utilisées ?
   2. Quels sont les impacts environnementaux d'une génération d'images excessive ?


(ia.conclusion)=

## Conclusion

*Durée : 5 minutes*

Pour conclure cette exploration des enjeux sociaux liés à l'IA générative, l'enseignant·e peut mettre l'accent sur les points suivants :

* Approche critique des résultats
* Conscience des biais des IA : culture et histoire
* Utilisation raisonnée de l'IA et de ses créations
* Il est essentiel de souligner le *side effect* : Tout ce qui est publié (sur les réseaux sociaux, etc.) doit être considéré comme public et est potentiellement utilisé pour entraîner une IA. Cette prise de conscience est cruciale pour encourager une réflexion critique sur la gestion de la présence numérique des élèves !


---

Activité réalisée par [Vincent Keller](https://vkeller.github.io/modulo-gybe) en collaboration avec la Prof. [Nathalie Dietschy.](mailto:Nathalie.Dietschy@unil.ch)