# Version imprimable

La compilation de la version imprimable de Modulo se fait en deux temps. Dans un premier temps,
la commande

`sphinx-build -b latex -t latex_mode src/appr build/latex/appr`

va compiler les sources en Markdown pour produire un document `build/latex/appr/modulo.tex` et recopier toutes les images
dans le dossier `build/latex/appr`. Les images aux formats .gif ou .svg que ne sont pas traités en LaTeX sont converties au format pdf. D'autres conversions sont effectuées (par exemple pour les ciruits logiques). Attention à bien installer les dépendances nécessaires comme décrit dans le fichier README.

Le fichier `src/appr/conf.py` contient les options de compilation, notamment les chapitres à exclure de la compilation et certaines
options de compilation LaTeX, tellle que le titre et les auteurs du polycopié. Dans ce fichier, la variable `latex_mode` permet de déterminer s'il s'agit d'une compilation en LaTeX ou en HTML. 

Les code de chacune des extensions disponible dans `src/exts/` (p. ex. codeplay, exercise, logic, videos...) indique également
comment ces extensions doivent être traitées lors de la compilation LaTeX. 

En deuxième temps, la commande 

`cd build/latex/appr && make`

va se rendre dans le fichier `build/latex/appr` et compiler le fichier `modulo.tex` généré par la première commande pour génére le pdf
modulo.pdf. Cette compilation va se faire en incluant le fichier `src/static/latex/customize.tex` qui contient différentes commandes LaTeX permettant, par exemple le traitement de certains caractère non ASCII, le formatage du titre, en-tête et pieds de page, ou la définition de certains environnements ou commandes permettant le rendu de certaines directives. 

