# Données et Enjeux de Réputation

---- 

Cette activité fait partie d'une série de ressources ayant pour objectif général d'identifier et de discuter des enjeux socio-techniques, politiques et économiques liés à la protection de la vie privée et des données personnelles.

En particulier, le sujet de cette activité est le lien entre les données personnelles et les enjeux de réputation.

---- 

```{admonition} Les enjeux de réputation
:class: hint
* Thème : Vie privée et données personnelles
* Niveau : `facile`
* Durée : 1 période
* Objectifs pédagogique : Comprendre ce qu’est une donnée. Mettre en relation les données et leur écosystème.
* Modalité : Débranché
* Matériel : Article du journal [The Pillar](https://www.pillarcatholic.com/p/pillar-investigates-usccb-gen-sec)
* Prérequis : Lecture de l'article *Pillar Investigates Burrill* (facultatif) 
* Notions fondamentales : données, collecte de données, base de données, recoupement de données
* Taille du groupe : classe entière

```

L'article en version PDF est disponible à télécharger pour distribution aux élèves (VO ou VF) : 

- {download}`Article du journal The Pillar (VO) <media/Pillar_Investigates_Burrill.pdf>`
- {download}`Article du journal The Pillar (VF traduit avec DeepL) <media/Pillar_Investigates_Burrill_fr.pdf>`

## Déroulement

|     Etape                             | Durée  | Phase de l'activité   | 
|---------------------------------------|------- |-----------------------|
|{ref}`Introduction <reputation.situation>`  | 5-10 min | Préparation |
| {ref}`Qu'est-ce qu'une donnée, où et comment sont-elles collectées ? <reputation.exploration>` | 15-20 min | Théorie |
| {ref}`Étude d'un cas pratique<reputation.cas_pratique>` | 5 min | Présentation |
| {ref}`Organisation d'un jeu de rôle <reputation.debat>` | 10-20 min | Mise en situation / Discussion |
| {ref}`Conclusion<reputation.conclusion>` | 5 min| Institutionalisation |


(reputation.situation)=
### Introduction 

*Durée : 5-10 min*

L'enseignant·e introduit la thématique en questionnant les élèves sur leurs usages des réseaux sociaux (*Instagram, TikTok, Facebook,etc.*) et les données personnelles récoltées selon leur expérience.  
Cette introduction sert à jeter les bases de ce que peut être une donnée personnelle.

(reputation.exploration)=
### Les données et leur collecte

*Durée : 15-20 min*

Dans cette partie, l'enseignant·e va présenter les différentes notions nécessaires à comprendre les bases de l'économie des données et les enjeux sous-jacents.

1. Une donnée c'est quoi ?  
En questionnant les élèves on définit une donnée comme toute trace ou information issue d'une extraction avec référence au dispositif dont elle est issue.(Marres, N. 2017. Digital sociology: The reinvention of social research. John Wiley & Sons.)  
Cela peut être un nom, un âge, une date, une localisation, etc., un lien peut être fait avec les *cookies*.  

2. Comment sont-elles collectées ?  
Toujours en interaction avec les élèves, un inventaire des moyens de collecte est fait.  
Les élèves pensent assez vite aux téléphones, aux ordinateurs, aux objets connectés (Internet of Things).  
Il est moins évident les caméras de surveillances (ville, péages, etc.) ou d'autres organisations qui collectent des données depuis longtemps comme les banques (paiements CB) ou les commerces avec les cartes de fidélités (*la carte cumulus, c'est comme des likes en mode supermarché !*).  
Il peut être intéressant d'insister sur l'ampleur de cette collecte en parlant des **traceurs** (et kits de développement logiciel, Software Development Kit). Pour l'illustrer, l'utilisation d'*[Exodus Privacy](https://exodus-privacy.eu.org/fr/)* sur une application comme *[Instagram](https://reports.exodus-privacy.eu.org/en/reports/com.instagram.android/latest/)* fait apparaitre le nombre et type d'autorisations demandées par l'application *(le fonctionnement de l'application a-t-il vraiment besoin de tout ça ? est-ce justifié / justifiable ?)*. L'application des CFF (très largement diffusée), qui se veut un exemple en termes de transparence, a une section très détaillée sur la collecte et le traitement des données à caractère personnel. Les élèves peuvent aller voir les longues listes des *Fournisseurs* et *SDK* en allant dans *Profil > Paramètres relatifs à la protection des données*.  
L'enseignant·e se charge de synthétiser tous les éléments mentionnés afin de mener les élèves à la notion de *profilage* ou *profil d'individu*. Ces profils qui peuvent par exemple alimenter le marketing en se basant sur nos comportements, ont intrinsèquement de la valeur qui peut encore augmenter en fonction de ce qu'on en fait.

3. Où vont ces données ?  
Ces données peuvent rester dans l'organisation qui les a collectées (banque, gouvernement, commerces), mais pas toujours.  
Parfois elles sont vendues (légalement ou pas), exemple de [Migros et Coop](https://www.blick.ch/fr/news/suisse/une-veritable-mine-dor-migros-et-coop-revendent-les-donnees-de-leurs-clients-en-toute-legalite-id18997319.html?utm_medium=social&utm_campaign=share-button&utm_source=copy-to-clipboard), à des *annonceurs* ou à des *boursiers des données, *data brokers* qui les revendront à leur tour, et parfois elles sont aussi volées, [Facebook et autres](https://www.lemonde.fr/pixels/article/2021/04/05/cinq-questions-sur-la-fuite-de-donnees-concernant-plus-de-533-millions-de-comptes-facebook_6075616_4408996.html).  
Dans tous les cas, ces données collectées à un endroit, stockées ailleurs, vendues, revendues, volées, achetées, circulent et génèrent de l'argent, c'est l'économie des données. Il n'est utile de rentrer le détail de son fonctionnement, mais sa complexité et la diversité des acteurs peut être illustrée avec cette {download}`infographie <media/EconomieDonnees.pdf>`.  

Agrégées ou rassemblées, mises en commun et organisées en base de données, toutes ces données permettent d'extraire une grande quantité d'informations qui génère de la connaissance, donc du pouvoir et par conséquent des risques aussi bien au niveau collectif (manipulation de masse, cf. [Cambridge Analytica](https://fr.wikipedia.org/wiki/Scandale_Facebook-Cambridge_Analytica)), qu'individuel ({ref}`cas pratique<reputation.cas_pratique>`).


(reputation.cas_pratique)=
### Cas Pratique : *The Pillar investigates Burrill*

*Durée : 5 min*

Si les élèves n'ont pas lu l'article, le résumer brièvement, dans tous les cas, rappeler les points clés suivants :

1. Achat de bases de données dans le cadre de journalisme d'investigation.
2. Les données contenaient des informations de géolocalisation horodatées ainsi que des *Mobile Advertising ID* ([MAID](https://kb.narrative.io/mobile-advertising-ids)).
3. Le croisement d'informations a permis d'identifier J. Burrill
4. Ses appareils émettent des signaux géolocalisés avec MAID

Grâce au croisement des données, les journalistes ont montré que J. Burrill, haut fonctionnaire de l'Église catholique, utilisait des applications de rencontres homosexuelles et qu'il s'était également rendu dans des bars homosexuels.

(reputation.debat)=
### Jeu de rôles

*Durée : 10-20 min*

Afin de sensibiliser les élèves à la complexité du sujet de la collecte et de l'utilisation des données personnelles, l'enseignant·e organise un jeu de rôle / débat ou les élèves sont réparti.e.s en 4 groupes ayant chaque groupe un rôle distinct :

- Groupe A : Une commission de journalistes défendant le droit à informer, protégeant les journalistes, ainsi que les méthodes utilisées par le journal
- Groupe B : L’entreprise / application transmettant des données personnelles
- Groupe C : L’autorité de protection des données où une plainte a été déposée
- Groupe D :La fédération romande des consommateurs (FRC) défendant la personne utilisant l’application

Les élèves devront construire leurs arguments selon leur rôle autour du cas The Pillar. En particulier, il est nécessaire de répondre aux deux questions suivantes :

1. Êtes-vous pour ou contre la collecte de la géolocalisation ?
2. Quelles mesures demandez-vous à mettre en place pour ou contre la collecte de la géolocalisation ?

L’enseignant·e passe dans les groupes pour rappeler les rôles, les aider à prendre position, guider les réflexions et rappeler le temps accordé pour répondre aux deux questions (~ 5 min).  
A la fin du temps imparti, l'enseignant·e se positionne au milieu des groupes et :
- demande à chaque groupe de rappeler son rôle et de donner ses réponses aux questions
- confronte les groupes en fonction des sujets amenés
- fera de la modération ou stimulera les réactions en fonction des besoins

L'objectif étant que les élèves réalisent que le sujet est délicat et qu'en fonction des rôles et des positions, il est difficile de trouver une solution satisfaisante mais qu'il est crucial de coopérer.

(reputation.conclusion)=
### Conclusion

*Durée : 5 min*

L'enseignant·e pourra conclure la séquence en notant que :
- les enjeux de réputation sont au cœur de l'économie des données
- les conséquences sont au niveau individuel et collectif : diffamation, vol d'identité, discrimination, harcèlement, surveillance, etc...
- les conséquences sont également au niveau des marques et des plateformes, [principalement financières](https://noyb.eu/fr/eu-58-million-fine-grindr-confirmed)

L'enseignant·e pourra également faire un rappel au droit avec le Règlement Général sur la Protection des Données ([RGPD](https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32016R0679)) en Europe et la nouvelle Loi sur la Protection des Données ([nLPD](https://www.kmu.admin.ch/kmu/fr/home/faits-et-tendances/digitalisation/protection-des-donnees/nouvelle-loi-sur-la-protection-des-donnees-nlpd.html)) entrée en vigueur le 1er septembre 2023.

Il pourra par exemple mentionner :
- droit d'accès
- droit à la portabilité des données
- droit de retrait du consentement
- droit d’opposition
- droit de rectification
- droit à l’effacement
- droit à la limitation du traitement
- droit de déposer une plainte
- prise de décision individuelle automatisée

---

Activité réalisée en collaboration avec [Dr. J. Pidoux](https://doi.org/10.5075/epfl-thesis-8830), [PersonalData.IO](https://personaldata.io/) et leur partenaire technologique [Hestia.ai](https://hestia.ai/)