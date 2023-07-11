# Version imprimable

## Prérequis
latex
inkscape pour la conversion des fichiers svg en pdf. 
make et latexmk pour la génération automatique des fichiers imprimables

## Compilation

### Version courte avec make sur MacOS ou Linux 

Pour avoir un polycopié avec tous les chapitre imprimables:

`make modulo.pdf`

Pour avoir un polycopié avec uniquement une chaptre (par exemple alogrithmique I):

`make algo1.pdf`

Les chapitres disponibles sont: `rep-info.pdf algo1.pdf algo2.pdf archi.pdf resx.pdf hist.pdf`. 

Pour générer le tout,  version web et les imprimables de chaque chapitre, et le polycopié global:

`make all`

### Version longue sans dépendance

La compilation de la version imprimable de Modulo se fait en deux temps. Dans un premier temps,
la commande

`sphinx-build -b latex -t latex_mode src/appr build/latex/appr`

va compiler les sources en Markdown pour produire un document `build/latex/appr/modulo.tex` et recopier toutes les images
dans le dossier `build/latex/appr`. Les images aux formats .gif ou .svg qui ne sont pas traités en LaTeX sont converties au format pdf. D'autres conversions sont effectuées (par exemple pour les ciruits logiques). 

Si on ne veut compiler que certains chapitres, il faut ajouter, pour chaque chapitre à inclure,
des `-t <chap>` à la commande ci-dessus, où `<chap>` est le nom du chapitre à choisir parmi `rep-info algo1 algo2 archi resx hist`.



Le fichier `src/appr/conf.py` contient les options de compilation, notamment les chapitres à exclure de la compilation et certaines
options de compilation LaTeX, telle que le titre et les auteurs du polycopié. Dans ce fichier, la variable `latex_mode` permet de déterminer s'il s'agit d'une compilation en LaTeX ou en HTML. 

Les code de chacune des extensions disponible dans `src/exts/` (p. ex. codeplay, exercise, logic, videos...) indique également
comment ces extensions doivent être traitées lors de la compilation LaTeX. 

En deuxième temps, il faut se rendre dans le répertoire dans lequel les fichiers latex ont été générés:

`cd build/latex/appr`

Puis compiler les fichiers latex avec 
`make`

Si make n'est pas installé, on peut utiliser

`pdflatex modulo.tex`

Cette compilation va se faire en incluant le fichier `src/static/latex/customize.tex` qui contient
différentes commandes LaTeX permettant, par exemple le traitement de certains caractère non ASCII, le formatage du titre,
en-tête et pieds de page, ou la définition de certains environnements ou commandes permettant le rendu de certaines
directives. Pour ceci il faut que mklatex

