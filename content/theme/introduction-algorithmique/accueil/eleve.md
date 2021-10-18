(algorithmique)=
Algorithmique I
==============================

<!-- Quand on cherche ses clés, on commence par fouiller ses poches. Si elles n'y sont pas, on va regarder en surface dans plusieurs pièces de la maison, pour voir si elles ne traîneraient pas quelque part. Si on ne les trouve toujours pas, on finit par refaire le même chemin en boucle, mais en cherchant toujours plus profond dans nos poches, dans nos vestes, dans nos tiroirs, et ainsi de suite jusqu'à les trouver. Pourquoi ne pas avoir commencé par fouiller à fond le premier tiroir rencontré ? Pourquoi ne pas s'être restreint dès le début à ne chercher que dans une pièce mais en soulevant le moindre objet pour voir si elles n'étaient pas dessus ? 

Parce que, grâce à l'habitude, on sait que la meilleure stratégie, c'est à dire celle qui a fait que l'on trouve ses clés la plupart du temps, est celle que l'on a utilisé. 

Cette stratégie, en informatique, ressemble à peu de choses près à un algorithme nommé [algorithme de parcours en profondeur itératif](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search). Derrière ce nom se cache un principe simple. Dans l'exemple des clés ce serait : commencer par fouiller une pièce, en se limitant dans la profondeur de la recherche, puis changer de pièce, et réitérer ce schéma en allant de plus en plus profond dans les tiroirs et les poches.  -->

Nous avons tous entendu parler DES ALGORITHMES. Ils sont partout et font toutes sortes de choses... Mais, c'est quoi en fait un algorithme ? Comment ça marche ? Et comment faire la différence entre un bon et un mauvais algorithme ? Nous tenterons ici de répondre à toutes ces questions.

Bienvenue dans le monde fascinant des algorithmes. 

## Contenu du chapitre

```{tableofcontents}
```

## Objectifs

A la fin de ce chapitre, vous saurez ce qu'est un algorithme et vous serez capable de transcrire des algorithmes en programmes. Vous saurez résoudre des problèmes, en décomposant leur solution en étapes à suivre. Vous verrez également que pour un même problème, on peut avoir plusieurs solutions avec différents propriétés, avantages et désavantages. 

{fa}`check, text-success mr-1`Se familiariser avec la notion d’algorithme.

{fa}`check, text-success mr-1`Savoir résoudre des problèmes, en décomposant leur solution en étapes à suivre.

{fa}`check, text-success mr-1`Savoir que pour un même problème, on peut avoir plusieurs solutions avec différents propriétés, avantages et désavantages.

{fa}`check, text-success mr-1`Être capable de transcrire un algorithme dans un programme.





````{panels}

:img-top: media/Al-Khwarizmi.png

Al-Khwarizmi 🇺🇿
^^^^^
* **Naissance** 780
* **Décès** 850

Considéré comme le père de l’algèbre [**Al-Khwarizmi**](https://fr.wikipedia.org/wiki/Al-Khw%C3%A2rizm%C3%AE) a vécu au VIII<sup>e</sup> siècle dans le Moyen Orient. Il est l'auteur de plusieurs ouvrages de mathématiques, d’astronomie et de géographie. Son nom est à l’origine du mot **algorithme**.

----
:img-top: media/Dijkstra.jpg

Edsger Dijkstra 🇳🇱
^^^^^
* **Naissance** 11 mai 1930
* **Décès** 06 août 2002

[Edsger Wybe Dijkstra](https://fr.wikipedia.org/wiki/Edsger_Dijkstra) est un mathématicien et informaticien néerlandais du XX<sup>e</sup> siècle. Il reçoit en 1972 le prix Turing pour ses contributions sur la science et l’art des langages de programmation et au langage Algol. Il est le concepteur de l'algorithme éponyme de recherche du plus court chemin. 
````






