# Stockage et manipulation des données

## Stockage

Au niveau du disque dur, c'est à dire de la mémoire de votre ordinateur, on pourrait représenter les choses sous la forme d'un tableau. Chacune des entrées de ce tableau est un bit. Si vous voulez stocker une image, en reprenant notre exemple simplifié, chaque pixel correspondrait à un bit, noir ou blanc, et serait "écrit" dans une entrée de ce tableau. 

Les smartphones que vous possédez ont en moyenne une mémoire de 64Go, ce qui correspond à 512000000000 bits. À chaque fois que vous enregistrez une image, vous utilisez un certain nombre d'entrées de ce tableau, et une fois que la mémoire est pleine, il n'est plus possible d'enregistrer quoi que ce soit. 

> **La taille des fichiers**. Par exemple, une chanson occupe en moyenne 3 Mo, donc 24000000 bit. En gros, il vous faudrait à peu près 2000 chansons pour occuper tout l'espace de votre smartphone de 64Go. C'est à peu près le même espace utilisé par une photo prise par votre caméra en résolution "normale". 

> **Pour aller plus loin** : À votre avis où est stockée une chanson que vous écoutez sur Spotify ? 

## Compression

La **compression** d'un fichier, que ce soit une chanson, une photo, un texte, est le procédé par lequel ce fichier va passer pour occuper moins de place dans la mémoire de l'ordinateur. 

Si on reprend notre exemple d'image ultra minimaliste en noir et blanc, on peut trouver une façon de stocker l'image sur la mémoire de l'ordinateur en utilisant moins de place que si l'on décrivait chaque pixel l'un après l'autre. 

Plutôt que de décrire chaque pixel l'un après l'autre, on va simplifier en décrivant à l'ordinateur le nombre de pixels blancs qui se suivent, puis le nombre de pixels noirs qui se suivent. Si plusieurs pixels sont de la même couleur, cela nous permet de les décrire en une fois. 

[Length encoding](https://www.csfieldguide.org.nz/en/interactives/run-length-encoding/)

Il existe de nombreux **standards** de compression, qui utilisent tous une technique particulière. Les plus célèbres sont JPEG pour les photographies, ou MP3 pour la musique. 

[Comparaison de compression](https://www.csfieldguide.org.nz/en/interactives/compression-comparer/)

Tout l'enjeu de la compression consiste à prendre des décisions sur les informations que l'on doit garder, et les informations que l'on peut "supprimer" pour garder une représentation correcte de notre fichier de base. Bien sûr, c'est toujours une décision, et plus on compresse, plus on perd de l'information, ce qui peut conduire à l'extrême à une dégradation de la qualité du fichier qui le rend inutilisable.  
