(webtracking.interractionressourcesweb)=

# Interactions et ressources sur le web

```{admonition} Notice
:class: hint

* **Thème** : `Réseaux` (transversal avec `Vie privée et surveillance` et `Économie du numérique`)
* **Niveau** : `moyen` <!-- L’activité n’est pas facile, car elle demande une certaine supervision de l’enseignant·e et car les outils sont probablement inconnus des élèves. Elle n’est toutefois pas difficile car rien n’est à installer, l’activité peut se faire sans outil autre que l’ordinateur et le navigateur ce qui en simplifie l’accessibilité. Les objectifs sont d’une complexité notable mais peu exigeants sur les pré-requis et la technicité. Dépendant de l’aise des élèves et de l’avancée dans le chapitre Web, l’activité prévoit de revoir les points essentiels du web à comprendre pour effectuer l’activité à tout niveau. -->
* **Durée** : 1 à 2 périodes
* **Objectifs pédagogiques** : les objectifs de cette séquence sont associés à ceux du chapitre Réseaux, notamment `sécurité et sensibilisation aux bonnes pratiques; notions et modèles d’architectures et de protocoles`. Plus d’explications sont données dans la partie [](webtracking.didactique)
* **Modalité** : `débranché`
* **Matériel** : Ordinateur et navigateur web pour l'enseignant·e
* **Prérequis** : Il est préférable d’avoir étudié les éléments du chapitre [World Wide Wide](https://apprendre.modulo-info.ch/resx/web.html). Cette activité le complète (éventuellement conclut).
* **Notions fondamentales** : Les technologies du web et leur fonctionnement, la modélisation d’une interaction sur le web
* **Taille du groupe** : `classe entière`

```

L’idée de cette séquence est d’ancrer les contenus étudiés à propos du web (par exemple via la partie [World Wide Web de Modulo](https://apprendre.modulo-info.ch/resx/web.html)) avec des exemples concrets. Elle permet ainsi d’institutionnaliser des éléments discutés dans l’accroche, mais remplace difficilement une étude complète des technologies du web.

## HTTP : transférer des documents hypertextes

Comme vu en cours, HTTP est le protocole qui permet de définir **comment deux ordinateurs se demandent des fichiers hypertextes sur internet**. Ouvrir une page web ne veut rien dire d’autre que générer une requête `GET` depuis votre navigateur (appelé **client**) vers un autre ordinateur (appelé **serveur**). Ce dernier vous répond généralement qu’il est d’accord (`OK`) et **vous joint le fichier HTML correspondant**. Tout ceci se passe **automatiquement** : une fois que vous cliquez sur un lien, l’ordinateur gère la mise en place du protocole pour vous. Les interactions autorisées par le protocole sont limitées, et seules les suivantes sont importantes pour cette séquence :

| Méthode HTTP | Usage                                                                                                            |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| `GET`        | Le client demande une information au serveur. Il peut éventuellement lui en transmettre au passage (les URL avec un `?`). |
| `POST`       | Le client donne des informations au serveur.                                                                     |

## HTML : le format de fichier hypertexte

HTML est le format de base des fichiers échangés sur le web. Ce simple fichier texte est "*Hyper*" notamment, car il a pour essence de **créer des liens avec d’autres documents**, on les appelle les **hyperliens** et c’est ainsi que fonctionne le web ! Sur un moteur de recherche, vous faites une requête et recevez une page qui contient une liste de liens vers d’autres pages. C’est ce qui permet de "**naviguer**" sur le web d’une page à l’autre.

```{figure} media/images/web-search.jpeg
---
alt: ddg screenshot
width: 650px
name: web-search
---
Résultat d’une recherche sur le web : une liste d’hyperliens
```

```{figure} media/images/web-search-source.jpeg
---
alt: ddg source screenshot
width: 650px
name: web-search-source
---
Code source de la page HTML des résultats de DuckDuckGo (Lite) : une balise `<a>` symbolise un lien vers une nouvelle page 
```

Il existe différents types de ressources vers lesquelles peuvent pointer les hyperliens. Les plus connues et répandues sont généralement les **liens vers d’autres pages** (comme dans la page d’une recherche web), mais les **images**, les **feuilles de styles** ou les **scripts** sont aussi des ressources qui sont en permanence référencées par nos pages web !

```{admonition} Important
:class: caution
Traditionnellement, **les pages web référencées ne sont chargées que lorsque l’on clique dessus**, c’est l’utlisateur·trice qui décide quand télécharger la nouvelle ressource. Les images, scripts et feuilles de style sont quant à eux chargés **automatiquement** ! L’utilisateur·trice n’a la plupart du temps pas conscience du moment où sont chargées ces ressources et d’où elles proviennent. C’est un concept clé pour la suite !
```

Les liens référençant des ressources peuvent pointer sur des **ressources internes** (des images par exemple) stockées dans le même dossier que la page web (comme dans l’exemple donné dans le [cours HTML](https://apprendre.modulo-info.ch/resx/web.html#html)), ou vers des **ressources tierces** localisées n’importe où ailleurs.

```{admonition} Micro-activité
:class: note
Vous pouvez télécharger les deux fichiers d’exemple {download}`code/example.html` et {download}`code/example_bootstrap.html`. Ces fichiers très simples rappellent les bases de HTML avec le concept de balise. 

Il est ensuite possible d’identifier avec les élèves les **différences entre le code source des deux fichiers**. Les lignes `9-11` du fichier `example_bootstrap.html` sont effectivement des balises spéciales qui servent de **références à des scripts tiers**. Ces derniers sont **chargés automatiquement** et permettent d’améliorer l’apparence de ma page web grâce à des ressources tierces (sans avoir à coder soi même).
```

```html
<html>
<body>
 <h1 style="color:red"> L’amanite tue-mouche </h1>
 <p> L’amanite tue-mouche est très belle mais très dangereuse ! </p>
 <img src="photo.jpg" height="250" />
</body>
</html>
```

```html
<html>
<body>
 <h1 style="color:red"> L’amanite tue-mouche </h1>
 <p> L’amanite tue-mouche est très belle mais très dangereuse ! </p>
 <img src="https://upload.wikimedia.org/wikipedia/commons/0/03/Fly_Agaric_mushroom_04.jpg" height="250" />
</body>
</html>
```

```{admonition} Micro-activité
:class: note
La première page HTML contient {bl}`une ressource tierce|>une ressource interne` tandis que la seconde contient une {bl}`>une ressource tierce|une ressource interne`. En effet, l’une de ces page charge {bl}`>une image|une feuille de style|un script` hébergé {bl}`sur Moodle|sur Office365|>sur Wikimedia`.
```

```{admonition} Micro-activité
:class: note
Notre navigateur chargera la ressource tierce {bl}`>automatiquement|manuellement avec un clic` et pour ce faire, il {bl}`ira chercher dans sa mémoire vive|>utilisera le protocole HTTPs`
```

## JavaScript : exécuter du code dans le navigateur

Comme vu dans le cours, **JavaScript est un langage de programmation**, comme Python, qui a comme spécificité d’avoir été développé pour **s’exécuter dans un navigateur**. Ainsi, beaucoup des choses complexes (affichages dynamiques et animations par exemple) qui se passent dans nos pages web sont codées avec le langage JavaScript. Par exemple, l’API WebGL permet d’afficher des applications graphiques complexes (le cube tournant sur <https://get.webgl.org> est un exemple imagé).

Il est important que les élèves comprennent qu’utiliser JavaScript dans son navigateur permet d’**en permanence recevoir du code pour exécuter diverses actions de programmation**. Le langage de programmation est une interface entre l’humain·e et la machine, cela permet d’obtenir des informations intéressantes sur la machine utilisée.

Par exemple, voici un bout de code Python qui permet d’afficher des informations sur la machine qui exécute ce code. Un code similaire permet de facilement obtenir ce genre d’informations également avec JavaScript.

```{codeplay}
:file: platform-info.py
import platform

print("Type d’ordinateur :", platform.machine())
print("Le processeur a une architecture pour :", platform.architecture()[0])
print("Ce programme s’exécute sur un système :",platform.system())
print("Ce système est dans sa version :", platform.release())
print("Vous utilisez Python dans sa version :", platform.python_version())
```

```{admonition} Le saviez-vous ?
:class: hint
Vous pouvez essayer de changer de navigateur et voir les différences des valeurs de retour de ce bout de code ! Vous pouvez même le télécharger et l’exécuter sur votre machine locale.
```

```{admonition} Pourquoi est-ce important ?
:class: note
Les élèves doivent comprendre que la possibilité d’exécuter du code est une capacité très puissante donnée aux pages web. **La plupart des autres applications** que nous avons l’habitude d’utiliser (nos mails, notre calendrier), utilisent **un code prédéfini** qui n’est modifié que lors de mises à jour du logiciel.
```

```{admonition} À retenir
:class: attention
- HTTP est le protocole qui est compris par les clients et les serveurs et leur permet d’**échanger du contenu sur internet**. Les méthode indiquent l’**intention de l’interaction** (`GET` ou `POST`)
- HTML est un language qui permet de transmettre **du texte mais aussi des liens vers des ressources**. Ces dernières peuvent être **internes ou tierces**, auquel cas, le protocole HTTP permet de les charger auprès du réel hébergeur
- JavaScript est un **language de programmation** à part entière qui permet d’**exécuter du code dans le navigateur**. C’est une capacité puissante pour **extraire des information sur le navigateur**.
```

## (optionnel) Les cookies : les fichiers pour se rappeler des anciennes sessions

```{admonition} Important
:class: caution
Le reste de l’activité ne couvre pas particulièrement les cookies. Cette partie est à plutôt réserver aux élèves pour qui les notions de HTTP, HTML et JavaScript sont claires, ou simplement pour les élèves les plus curieux·ses.
```

Par nature, le protocole HTTP est ce que l’on appelle "Stateless", ce qui signifie que **rien dans le protocole ne s’assure d’avoir une mémoire entre deux requêtes** : si vous faites 2 requêtes d’affilée pour <https://wikipedia.org>, ces deux requêtes seront a priori traitées indépendamment, sans prendre en compte que la même personne a fait cette requête, ni que l’une doit arriver avant l’autre.

Or, il peut être bien **pratique de garder ces informations entre deux requêtes**, c’est ce qu’on appelle une **session**, et c’est ce qui se passe dans quasiment chacune de nos interactions web. Le meilleur exemple est par exemple celui d’une session sur <https://office.com>. Lorsque vous vous connectez avec votre compte, vous entrez votre mot de passe, puis tant que vous ne fermez pas votre navigateur, vous n’avez **plus besoin de l’entrer de nouveau**. *Comment Office sait que la même personne est connectées si toutes les requêtes sont indépendantes ?* Grâce aux cookies !

Les cookies sont simplement des **fichiers texte enregistrés dans le navigateur qui sont envoyés automatiquement avec la requête HTTP**. Ainsi, si le cookie contient votre mot de passe (ce n’est généralement pas le cas pour des raisons de sécurité, mais l’image est conceptuellement plus simple), à chaque requête, il est possible de vous authentifier automatiquement sans même que vous vous en rendiez compte ! Fermer le navigateur annule en général ceci, car il est souvent configuré que la fermeture du navigateur efface les cookies : plus de petit fichier texte avec votre "mot de passe" envoyé en même temps que chaque requête à <https://office.com>, il faut vous reconnecter.
