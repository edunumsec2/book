# L'app de rencontre

Note : remix du "Knight's tour". 

## Contexte

Vous êtes le créateur d'une application de rencontre. Vous avez douze utilisateurs. Vous savez que certains profils sont connectés les uns avec les autres. Chaque utilisateur peut passer d'un profil à un autre, mais seulement en passant par les profils connectés. Vous voulez que chaque utilisateur voit une fois, et seulement une fois, tous les profils différents. S'ils les voyaient plus d'une fois, ils se rendraient compte qu'il n'y a en réalité pas beaucoup de monde sur votre plateforme. 

## Les utilisateurs

1. Bob
2. Pablo
3. Marie
4. Marc
5. Jacques
6. Alice
7. Joseph
8. Alessia
9. Arthur
10. Jeanne
11. Silvia
12. Jean

## Les connexions entre utilisateurs

1. Bob -> Alice, Joseph, Arthur
2. Pablo -> Alessia, Marie, Jeanne
3. Marie -> Arthur, Pablo, Silvia
4. Marc -> Jeanne, Jean
5. Jacques -> Silvia, Joseph
6. Alice -> Bob, Alessia, Jean
7. Joseph -> Jacques, Bob, Jean
8. Alessia -> Pablo, Alice
9. Arthur -> Bob, Marie
10. Jeanne -> Pablo, Marc, Silvia
11. Silvia -> Jeanne, Jacques, Marie
12. Jean -> Alice, Marc, Joseph

## Comment faire ? 

- Partons de l'utilisateur Bob.
- On aimerait que Bob puisse voir le profil de tous les autres utilisateurs, mais seulement une fois. * S'il les voyait plusieurs fois, il se rendrait compte que l'application n'a pas beaucoup d'utilisateurs, et il s'ennuyerait trop vite. *
- Le problème est qu'il ne peut voir le profil d'un utilisateur avec qui il n'est pas connecté que s'il est passé au préalable par une connexion commune. Par exemple, Bob peut voir le profil de Jean que s'il est passé par Alice (car Bob est connecté à Alice, qui est connectée à Jean... Un peu comme sur Facebook). 
- Essayez de trouver un chemin qui commence par Bob et qui voit tous les utilisateurs une seule fois. 
- Si vous avez réussi, faites la même chose avec chacun des utilisateurs. 

## Impossible ? 

La solution est un graphe ! 

## Extensions

> cf : Judith Duportail, l'amour sous algorithmes. 
> Contacter Jessica Pidoux, thèse là-dessus. 


- On imagine une app sur le modèle Tinder. Profils voient profils, profils choisissent like ou swipe. 
- L'objectif est d'augmenter le temps passé sur l'app. 
- On lance la version Beta. Donc base d'utilisateurs, et fonctionnalités basiques de profil, match, etc. 
- On observe une correlation forte entre nombre de matchs et temps passé sur l'app. 
- On veut optimiser. 
- On remarque qu'il y a plus de matchs entre personnes ayant coché les mêmes centres d'intérêt (statistique). 
- On crée des groupes. 
- ! Evènement : 5 désinscriptions. Enquête.
- On observe les cinq derniers profils vus. Y a-t-il une corrélation entre eux ? Hmm... 30% ont coché "cuisine" dans intérêts... Ah, bingo ! 99% ont été swipés 3 fois plus souvent que la moyenne des utilisateurs. 
- Y a-t-il une similarité entre les profils désinscrits ? Oui ! 90% ont été swipés 3 fois moins souvent que la moyenne. 
- On crée donc une nouvelle règle. Le nombre de swipe, ou de like, accumulés, nous classe dans différentes catégories qui ne se voient pas entre elles (en soi ça revient au faciès dans les clubs...). 
- On crée donc le score de désirabilité. 
- On regarde les chiffres depuis la nouvelle règle ? Yep. Ca marche. 
- *On passe en dark mode*
- Bizarre, 5 désinscrits. Ah, 90% des cinq dernières intéractions filles trop diplômées. Donc (j'accélère), diplômes diminuent score de désirabilité chez les filles. Et chez les garçons ? L'inverse. On crée différents protocoles pour hommes et femmes. 
- Des femmes cessent de mettre leurs diplômes. Mince... Perte d'une info. 
- On crée un système de chat. 
- Dans le chat, on fait du NLP. On compte la variété du vocabulaire. On remarque (dans la société), une correlation entre nombre de mots de voc et degré d'études. Bingo ! On possède de nouveau cette info. 

