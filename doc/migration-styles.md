# Migration des balises de `sphinx-panels` vers `sphinx-design`

Suite au passage vers Sphinx version 5, le système de `sphinx-panels` a été remplacé par `sphinx-design`.
Ça implique des changements dans la creation des éléments du style dans les pages, notamment en ce qui concerne
les tabs est les panels.

Exemple pour illustration:

```
````{panels}
:img-top: media/Usine_avant.jpeg

**Usine du début du siècle dernier.** Les machines dans cette usine de métallurgie à Vallorbe dans le canton de Vaud sont au service des ouvriers. Source : https://wikivaud.ch/metallurgie-vaudoise/

----
:img-top: media/Usine_après.jpeg

**Usine du début de ce siècle.** Les machines dans cette usine de montage Mistubishi en Chine ont remplacé les ouvriers. Source : https://www.lemonde.fr/blog/fredericjoignot/2015
````
```

devient

```
:::::{grid} 1 2 2 2
:gutter: 2

::::{grid-item}
:::{card}
:img-top: media/Usine_avant.jpeg

**Usine du début du siècle dernier.** Les machines dans cette usine de métallurgie à Vallorbe dans le canton de Vaud sont au service des ouvriers. Source : https://wikivaud.ch/metallurgie-vaudoise/

:::
::::

::::{grid-item}
:::{card}
:img-top: media/Usine_après.jpeg

**Usine du début de ce siècle.** Les machines dans cette usine de montage Mistubishi en Chine ont remplacé les ouvriers. Source : https://www.lemonde.fr/blog/fredericjoignot/2015

:::
::::
:::::
```

Pour plus d'exemples, conslutez le commit `e836c1c185f2609cfaac950acc8c3aa05992444c` et sur la page de référence de
[sphinx-design](https://sphinx-design.readthedocs.io/en/latest/).