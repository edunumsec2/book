# Annexe

## Fichier de configuration

Vous pouvez télécharger ce fichier.
Il

```{codeplay}
:file: turtle.cfg
:static:
width = 640
height = 440
leftright = -1
topbottom = 0
canvwidth = 600
canvheight = 400
mode = standard
colormode = 1.0
delay = 10
undobuffersize = 1000
shape = turtle
pencolor = indigo
fillcolor = white
resizemode = noresize
visible = True
language = english
exampleturtle = turtle
examplescreen = screen
title = Modulo - Programmation
using_IDLE = False
```

## Exporter en en EPS

```python
from tkinter import * 
Screen().getcanvas().postscript(file='file.eps')
```
