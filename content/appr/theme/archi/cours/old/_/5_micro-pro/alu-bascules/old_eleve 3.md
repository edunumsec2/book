

### Conclusion

Dans ce sous-chapitre nous avons donc vu les briques de base des ordinateurs. À savoir les éléments suivants:
* Les portes logiques qui s'assemblent en systèmes logiques qui effectuent des opérations logiques qui aboutissent à des fonctions arithmétiques et logiques dans une ALU
* Les bascules qui permettent de mémoriser une information et s'assemblent dans des registres

Nous pouvons les assembler dans des microprocesseurs que nous allons détailler au sous-chapitre suivant.

::::{panels}
:column: col-lg-12 p-2
:card: bg-info

**Vite ... très vite**
^^^^
Nous avons démontré que finalement nos ordinateurs ont un cerveau très simple dans le fonctionnement de ses éléments de base : des portes logiques qui traitent des **0** ou des **1**. Il est cependant très difficile de se représenter à quel point ces traitements vont vite.
Imaginons pour cela que le processeur écrive toutes les opérations qu'il effectue sur un ruban de papier et calculons la vitesse de défilement de ce papier. 

Pour cela nous faisons les hypothèses suivantes:
* Les processeurs actuels ont une cadence d'horloge de 3GHz, c'est à dire $3·10^9 [s^{-1}]$. Pour simplifier nous allons supposer qu'ils effectuent une opération par cycle[^1].
* Nous transcrivons un mot de 64 bit (taille standard pour les processeurs) sur une longueur de 15cm, ce qui correspond à $15·10^{-2}[m]$.

Le calcul devient alors:

$$
    3·10^9 [s^{-1}] · 15·10^{-2}[m] \\
    45·10^7 [m/s]
$$

Que nous convertissons en km :

$$
    45·10^5 [km/s] ou encore: 450'000 [km/s]
$$

Rappelons que la vitesse de la lumière est:

$$
    c \cong 300'000 [km/s]
$$

Ce qui veut dire que si un microprocesseur, tel que ceux que l'on trouve dans notre ordinateur ou notre smartphone, écrivait sur un ruban de papier tout ce qu'il fait, ce ruban de papier devrait se déplacer à une fois et demi la vitesse de la lumière. Ou encore, ce ruban ferait chaque seconde plus de 11 fois le tour de la terre.

Si les éléments de base sont simples, la complexité et la richesse des expériences numériques comme l'immersion dans un jeu vidéo proviennent de la quantité extraordinaire d'opérations effectuées.

[^1]: En fait le opérations d'un processeur prennent plus d'un cycle pour être réalisées, mais comme les processeurs ont plusieurs cœurs et un pipeline dont nous n'abordons pas ici le fonctionnement, la simplification proposée n'est pas aberrante.



::::
