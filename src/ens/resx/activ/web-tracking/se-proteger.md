# Comprendre et se protéger

```{admonition} Notice
:class: hint

* **Thème** : `Réseaux` (transversal avec `Vie privée et surveillance` et `Économie du numérique`)
* **Niveau** : `moyen` 
* **Durée** : 1 à 2 périodes
* **Objectifs pédagogiques** : les objectifs de cette séquence sont associés à ceux du chapitre Réseaux, notamment `sécurité et sensibilisation aux bonnes pratiques. De plus, les objectifs transversaux d’enjeux sociaux sont visés notamment `vie privée et surveillance; économie du numérique`. Plus d’explications sont données dans la partie [](webtracking.didactique)
* **Modalité** : `débranché`
* **Matériel** : -
* **Prérequis** : L’activité {ref}`encheres` ou équivalent sur le fonctionnement de la publicité ciblée est également requis pour comprendre la présence des acteurs et des enjeux (ceci pourrait s’intégrer dans une séance préliminaire débranchée)
* **Notions fondamentales** : Les technologies du web et leur fonctionnement, l’{glo}`adtech|Ad Tech` et l’économie du web, les concepts et l’évaluation de vie privée du numérique, la modélisation d’une interaction sur le web avec l’association à des entités et leurs intérêts
* **Taille du groupe** : `classe entière`

```

(webtracking.proprietevieprivee)=

## Vie privée - propriétés et menaces

*Durée : 10-15 min*

Lors de cette dernière partie de la séquence, l’idée est de créer des ponts entre les **relations abstraites de haut-niveaux entre des individus/entreprises** et les **réalités des communications réseau sur le web**. Ainsi, il est important d’amener brièvement ce que l’on appelle des propriétés de la vie privée : *des éléments qui, lorsqu’ils sont manquants, peuvent être utilisés dans des contextes intrusifs contre des individus* (rappel des histoires de l’[accroche](webtracking.accroche)).


| Propriété       | Définition                                                                                                                                                   | Cherche à protéger                                                                                                                   | Ne permet pas de protéger (entre autres)                                                                                                                                               | Comment l’atteindre                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Confidentialité | le fait de ne permettre qu’aux personnes souhaitées d’accéder à une information                                                                              | des données (mots de passe, codes de carte bleu)                                                                                     | le contexte autour de ces informations (savoir qu’une information existe par exemple)                                                                                                  | Chiffrement                                                                  |
| Pseudonymité    | le fait de remplacer un identifiant par un autre (un nom de famille par un pseudo par exemple)                                                               | un nom en particulier                                                                                                                | l’association entre un pseudo et différentes actions d’une même personne (sous couvert du même pseudo sur 2 forums, il est possible d’associer nos messages postés à la même personne) | Remplacer les noms par des alternatives                                      |
| Anonymité       | le fait de rendre indistingables différent·e·s utilisateur·trice·s : il pourrait s’agir à chaque fois de la même personne ou de personnes toutes différentes, aucune information disponible ne permet de distinguer | l’identité des utilisteur·trice·s (protéger leur réelle identité et pouvoir en adopter de nouvelles vis-à-vis de différents acteurs) | la déniabilité, la possibilité de rendre indistingable le fait d’avoir fait une action ou non                                                                                          | Très complexe et dans beaucoup de cas, impossible sans supprimer des données (les [](webtracking.ressources) peuvent donner des exemples intuitifs) |

Ces propriétés permettent d’encadrer en partie ce qu’est la vie privée d’un point de vue plus formel. Dans chacune des histoires de l’accroche, il existe un problème, car les individus concernés s’attendent à une forme d'anonymat sur internet vis-à-vis de certains acteurs (leur entreprise, le public, les groupes "anti-choix", leur réseau social ...). Il est alors pertinent d’utiliser cette explication en parallèle d’un rappel de l’accroche choisie pour le cours.

```{admonition} À retenir
:class: attention
- il existe différents aspects de la vie privée qu’il est intéressant de protéger
- la vie privée s’évalue toujours **par rapport à un "adversaire"**, une entité définie dans notre système d’interaction (le service de publicité ciblée, le fournisseur de service, le réseau, l’État, ...)
- la pseudonymité est la plupart du temps la seule propriété qu’il est facile d’obtenir sur le web
- l’**anonymité est une propriété très puissant**e, loin d’être applicable et encore moins dans le contenu du suivi sur le web
- les technologie du suivi sur le web ont toutes un dénominateur commun : **identifier le plus précisément possible les utilisateur·trice·s**. Cependant cela est précisément l’encontre de l’anonymité et peut avoir des répercussions néfastes si ce n’est pas contrôlé
```

```{question}
:multi:
Dans [l’activité "Aller plus loin" de la partie précédente](trackography), quelles propriétés de la vie privée peut-on espérer avoir vis à vis de l’entité Alphabet (Google) dans notre communication avec les journaux suisses ?
- {v}`Confidentialité`
- {v}`Pseudonymité`
- {f}`Anonymité`
```

```{dropdown} Réponse
Cette réponse est bien entendu à nuancer et n’est pas si noire ou blanche avec aussi peu de précisions. Intuitivement :
- il ne manque pas de confidentialité car il est désiré de la part des journaux que Google ait accès au contenu visité par l’utilisateur·trice. La question se pose du consentement de ce·tte dernier·ère : on consent ou pas aux cookies, pas aux communication avec les services d’analyse. Comme toujours, la réponse varie selon la considération de "qui se protège de quel adversaire"
- on peut espérer de la pseudonymité pourvu que nous n’ayons transmis notre nom réel ni à Google, ni à la Tribune de Genève ni a Suisse Info. Dans le cas contraire, cette propriété serait en péril
- nous n’avons clairement pas d’anonymité : un acteur commun rassemble nos informations de navigations sur ces deux sites différents et peut lier notre identité et nos actions dans ces deux contextes

De nouveau, l’intérêt de cette discussion est d’amener la complexité de ces propriétés et à quel point "elles n’ont de sens" que dans un contexte définit : **que protège-t-on précisément ? De qui le protège-t-on ? Sur quelle(s) interaction(s) ?**
```

(webtracking.commerceweb)=

## Trace réseau et suivi - commerce du web

*Durée : 5-10 min*

Cette partie fait office de rappel et de pont avec la première année du chapitre d’**économie du numérique**. Dans l’idéal, les élèves devraient pouvoir se rappeler l’activité {ref}`encheres` pour aborder cette partie. En effet, l’idée est de transmettre aux élèves la compréhension des **relations économiques des acteurs autour de l’industrie de la publicité**.

Bien qu’elle ne suffise pas comme support d’enseignement, la {numref}`adtech-schema` illustre le fonctionnement des technologies de la publicité pour l’un des sites web visité dans les exemples. Elle met notamment en avant les relations économiques entre **le fournisseur de service** (20 minutes), **le service d’analyse** (Google Analytics), **le vendeur de produit** (par exemple une marque de chaussures) et le **service fournissant la publicité** (Google Ads).

```{figure} media/images/adtech-schema.jpg
---
alt: schema fonctionnement économique technologie de la publicité
width: 700px
name: adtech-schema
---
Illustration schématique du fonctionnement des technologies de la publicité ciblée
```

```{question}
Dans l’activité {ref}`sur la première analyse de trackers sur un site web<ricardo-activity>`, quelle est la position économique de Google Tag Manager ?
- {f}`Ce site fournit le service principal`
- {v}`Ce site effectue un service d’analyse envers Ricardo`
- {f}`Ce site fournit des publicité ciblées sur la page de Ricardo`
- {f}`Ce site fournit des produits à vendre via des publicités sur Ricardo`
```

```{question}
:multi:
Sur la page d’accueil de Google comme dans l’activité {ref}`effectuée en début de TP<google-post>`, l’entité Google occupe la place de plusieurs acteurs de la boucle économique identifiée. Lesquels ?
- {v}`Le fournisseur de service principal` 
- {v}`Le service d’analyse`
- {v}`Le service de publicité ciblée`
- {f}`Le vendeur de produit`
```

(webtracking.protection)=

## Protection de la vie privée

*Durée : 15-20 min*

La question maintenant évidente est "que faire, si l’on ne veut pas mettre en péril notre vie privée" ? Comment faire pour ne pas tomber dans un monde où la surveillance rapporte tellement que des société privée connaissent et monétisent à qui veut l’acheter nos secrets et l’analyse de notre vie et de notre personnalité ? Évidement, une telle question n’a pas de réponse simple, et les deux approches suivantes ont pour but de montrer aux élèves **des pistes pour se protéger**, et même pour leur futur, **faire des choix plus éthiques** en ce qui concerne ce marché.

### Des outils pour se protéger

Comme vu dans la partie [](webtracking.proprietevieprivee), se protéger fait toujours écho aux questions **"de qui ?" et "de quoi ?"**. Ainsi, pour répondre aux situations et risques ayant été soulevés, l’idée sera de chercher des solutions pour **se protéger des entreprises de suivi** : les services d’analyse et les services de publicité ciblée. L’idée est de **protéger son anonymat autant que possible**, c'est-à-dire limiter le suivi possible de l’unicité de notre personne lors de la navigation. Plusieurs approches et solutions sont envisageables, notamment les suivantes sont intéressantes à mentionner auprès des élèves.

```{admonition} Le navigateur
:class: note
Comme vu lors de la séance de TP, le navigateur est **la porte d’entrée de la majorité de nos communications web**, c’est donc clairement l’élément le plus crucial à protéger. Choisir un navigateur respectueux de la vie privée est nécessaire pour espérer avoir une vie privée sur le web. Un navigateur respecte la vie privée lorsqu’il permet de **mettre en place simplement des mécanismes limitant le suivi** : le [Total Cookie Protection](https://blog.mozilla.org/security/2021/02/23/total-cookie-protection/) ou la [protection contre le fingerprinting](https://support.mozilla.org/en-US/kb/firefox-protection-against-fingerprinting) de Firefox en sont des exemples

Il existe de nombreux choix, les plus accessibles et de meilleure qualité sont sans doutes [Brave](https://brave.com/) et [LibreWolf](https://librewolf.net/), respectivement basés sur Chromium et Firefox. Le site web [PrivacyTests.org](https://privacytests.org/) fournit très régulièrement des tests très complets comparant les navigateurs sur différents critères d’implémentations de ces technologies limitant les mécanismes de suivi.

Un point qu’il peut être important d’appuyer est que **Google Chrome est le navigateur le moins respectueux de la vie privée** : et oui, étant donné que la publicité ciblée est [le principal revenu](https://www.cnbc.com/2021/05/18/how-does-google-make-money-advertising-business-breakdown-.html) de la société Alphabet, bloquer ces dernières est impensable.
```

```{admonition} Les extensions du navigateur
:class: note
La **configuration par défaut de la plupart des navigateurs ne permet pas une protection contre toutes les stratégie de tracking**. Ainsi, une extension peut permettre d’améliorer la sécurité générale mais aussi aider à préserver la vie privée lors de la navigation.

Il est possible de présenter aux élèves des extensions reconnues et efficace comme [uBlock Origin](https://github.com/gorhill/uBlock#ublock-origin), [Ghostery](https://www.ghostery.com/) ou [Privacy Badger](https://privacybadger.org/). Notamment, ces extensions ont l’avantage précieux d’être open-source ce qui limite les risques d’avoir un logiciel espion mal intentionné ayant accès à notre navigateur.

Il serait même par exemple pertinent de **montrer sur votre propre ordinateur un "avant-après"** pour attester de l’efficacité des extensions comme peut le montrer la capture d’écran suivante, en lien avec les communications faites et vues en TP.

![ubo works](media/images/ublock.jpeg)
```

```{admonition} Les VPN
:class: note
Au vu du martèlement marketing autour de ce produit, les élèves auront sans doutes entendu parlé de VPN personnels. Il peut être intéressant d’en expliquer **les avantages et inconvénients** :
- ✅ l’idée est de **remplacer votre adresse IP** par celle d’un de leur serveur, les beacons ne seront pas capables de vous identifier par ce biais
- ❌ vos **cookies et votre empreinte numérique peuvent eux être transmis sans soucis** : cela opère à une **couche applicative**, et pas une couche IP
  - de même, si vous utilisez un compte (compte google ou YouTube), vos données sont sauvegardées dans ce compte, cela peut sembler bête mais important de rappeler conceptuellement
- ❌ si les beacons ne sont plus informés du lien entre votre adresse IP et votre navigation, c’est car c’est à présent le service de VPN qui en est informé, **c’est une question de confiance** : avez-vous confiance en une entreprise d’analyse web ou en une entreprise de VPN. Il est important de **se former une opinion sur le service (et l’entreprise le soutenant) de VPN que l’on veut utiliser** pour faire un choix éclairé, il n’y a pas de protection magique avec ce genre de service.
```

```{question}
:multi:
Pour limiter l’usage des beacons sur ricardo.ch, il vaut mieux que j’utilise :
- {f}`une extension bloquant les capacités de JavaScript`
- {v}`une extension bloquant les communications vers le site googletagmanager.com`
- {v}`un VPN d’une entreprise en qui j’ai confiance du bon usage de mes données`
- {v}`un navigateur dans lequel sont intégrées des mesures de protections contre les beacons`
```

```{question}
:multi:
Pour limiter l’usage du fingerprinting sur google.com, il vaut mieux que j’utilise :
- {v}`une extension bloquant les capacités de JavaScript`
- {f}`une extension bloquant les communications vers le site google.com`
- {f}`un VPN d’une entreprise en qui j’ai confiance du bon usage de mes données`
- {v}`un navigateur dans lequel sont intégrées des mesures de protections contre le fingerprinting`
- (bonus) {v}`une extension bloquant les requêtes vers le site google.com/log`
```

### Des moyens plus respectueux d’utiliser la publicité

Suite à cette discussion, les élèves peuvent éventuellement poser la question de la **rupture de la boucle économique** décrite dans [](webtracking.commerceweb) dans le cas où les pubs seraient bloquées, et à juste titre. Chaque année, le marché de la publicité ciblée rapporte [plus d’une centaine de milliards de dollars à Google](https://www.cnbc.com/2021/05/18/how-does-google-make-money-advertising-business-breakdown-.html) par exemple. Il semble donc clair qu’**aucune entreprise ne veut se passer de ce marché et ces revenus**. C’est pourquoi il peut être judicieux de parler aux élèves en tant que futurs citoyen·ne·s et potentiellement futur·e·s analystes de trafic web : il existe des moyens d’**avoir des informations et de la publicité utiles sans s’introduire à ce point dans la vie privée** :

- [Plausible](https://plausible.io/) est une alternative open-source à Google Analytics qui permet d’analyser le trafic de ses sites web de façon plus légère, axée sur la vie privée et sur des infrastructures européennes
- [Matomo](https://matomo.org/) est une alternative également comparable, notamment prisée pour sa capacité à être déployée "on-premise", et donc éviter des communications tierces, mais toujours garder les données chez la même entité
- [Qwant](https://about.qwant.com/) propose un modèle publicitaire axé sur un suivi limité et un ciblage respectueux de la vie privée, c’est même ce qu’ils [promeuvent auprès des annonceurs](https://about.qwant.com/advertising/)

```{admonition} À retenir
:class: attention
- le **choix de navigateur est crucial**, c’est la porte d’entrée du suivi sur le web, si elle ne permet pas de limiter le suivi il sera impossible d’avoir une vie privée
- les extensions sont efficaces pour **limiter le trafic vers des sites non désirables**. Elles sont nombreuses et il est préférable d’en choisir des reconnues et recommandées
- pour se protéger, il faut faire **des choix à différents niveaux (réseau, application)** et utiliser des technologies qui limitent les capacités des technologies de tracking :   
  - **limite du fingerprinting en limitant les capacités de JavaScript** ou les capacités des communication avec les sites recevant l’empreinte numérique, éventuellement à l’aide d’une extension 
  - **limite des beacon en cachant son adresse IP** ou empêchant la communication avec les services connus de beacon comme Google Tag Manager, éventuellement à l’aide d’une extension. 
  - Les élèves doivent **comprendre le fonctionnement des technologies de tracking** pour **expliquer ce qui permet de les bloquer**
- les VPN ne permettent pas une protection mais un **changement d’entité capable d’analyser notre trafic**. C’est notre niveau de confiance qui déterminera la sécurité ou non
- il existe une **boucle économique respectueuse de la vie privée** tout en permettant d’analyser le trafic et promouvoir ses produits sur le web
```

(webtracking.reinvestissement)=

## Suivi et applications mobiles

*Durée : 5-10 min*

Cette dernière étape est un réinvestissement qui permet d’**élargir les compétences acquises** lors de la séquence pour les appliquer à un autre domaine. De nombreuses applications sont possibles, notamment vis-à-vis de rebonds avec l’accroche. La proposition est d’ici parler brièvement des applications mobiles et analyser que, même si ce n’est pas dans un navigateur, **la même boucle économique est en fonctionnement** (avec l’ajout intéressant de la commission sur les transactions in-app [comme le fait Apple](https://appleinsider.com/articles/23/01/08/the-cost-of-doing-business-apples-app-store-fees-explained) par exemple).

Le temps étant limité, il est possible d’aborder le sujet sous différents angles, mais il semble intéressant de travailler avec les élèves sur la compréhension des politiques en matières de vie privée des applications. Les **stores Apple et Android** indiquent aujourd’hui avec plus de précision le traitement des données et l’utilisation des périphériques faites par les apps. Par exemple dans la {numref}`instagram-privacy`, on peut voir un certain nombre de données permettant d’établir un lien avec l’identité de l’utilisateur·trice. Quelques questions peuvent guider une discussion :

1. Comment peut-on suivre quelqu’un avec *une seule application* ?
1. *Pourquoi* toutes ces données sont-elles collectées dans le cas d’Instagram ?
1. Quelle est *la position d’Instagram dans la boucle économique* de la publicité ciblée ?
1. Comment *protéger sa vie privée* en utilisant Instagram ?

(Ces questions sont tout à fait ouvertes et peuvent être guidées par les interactions avec les élèves ou des points spécifiques qu’il est utile d’appuyer en réponse à d’autres parties du cours ou même d’autres disciplines)

```{figure} media/images/instagram-privacy.jpeg
---
width: 250px
name: instagram-privacy
---
Description de l’utilisation des données par l’application Instagram dans l’Apple Store
```

Idéalement, l’enseignant·e s’assure que la discussion puisse mettre en valeur les compétences acquises lors de la séquence :

1. Il est possible de **suivre avec une seule application de nombreuses façons** : navigateur intégré, partage vers d’autres applications (messagerie), dans le cas de Meta, les données peuvent être regroupées avec celles de WhatsApp et Facebook. **Certaines technologies de suivi sont identiques** (fingerprinting, beacon, cookies), mais il y en a également des **propres aux applications mobiles** (suivie inter-application, numéro d’identifiant unique d’appareil, notifications push)
1. ces données sont collectées dans le but de créer **un profil publicitaire** pour la publicité ciblée, car
1. Meta est à la fois **fournisseur de service**, **fournisseur de publicité** et s’occupe via les applications d’être **un service d’analyse**. Autrement dit ils ont une position dans laquelle **ils ne font que gagner de l’argent dans la boucle**, d’où l’intérêt d’occuper toutes ces positions
1. **c’est plus difficile** ! Pas d’extension, pas de choix de navigateur et l’application a accès à beaucoup plus de données qu’un navigateur d’ordinateur (données de santé par exemple). La capacité à se protéger **dépend grandement des choix des développeur·euse·s de systèmes d’exploitation (iOS et Android)** pour implémenter des mécanismes de protection
