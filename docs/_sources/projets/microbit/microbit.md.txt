# Micro:bit

Le **micro:bit**  est un ordinateur mono-carte (single-board computer) est un ordinateur pour un usage éducatif.

La platine 4 x 5 cm contient:

- un processeur ARM Cortex-M0
- un capteur de mouvement 3D
- une boussole numérique
- une connexion Bluetooth
- une matrice 5 x 5 de LEDs
- deux boutons

## EditeurThonny

L'éditeur Thonny permet de programmer le micro:bit

```{image} thonny_microbit.png
:width: 500px
```

Dans les options, il faut choisir MicroPython (BBC micro:bit). Eventuellement il faut cliquer sur **install or update firmware** pour installer MicroPython sur la carte micro:bit.

## Editeur en ligne

Avec un navigateur basé sur Chrome, vous pouvez programmer le micro:bit depuis le site:

<https://python.microbit.org/v/2>

## Détails de version

Quand un micro:bit est connecté à un ordinateur, il apparait comme un volume de stockage tel un disque du ou une clé USB. Le volume s'appelle **MICROBIT**.

Dedans vous trouvez deux documents:

- DETAILS.TXT
- MICROBIT.HTM

Le document DETAILS.TXT contient des informations sur la version:

```text
# DAPLink Firmware - see https://mbed.com/daplink
Unique ID: 9900000049734e45004580160000005b0000000097969901
HIC ID: 97969901
Auto Reset: 1
Automation allowed: 0
Daplink Mode: Interface
Interface Version: 0241
Git SHA: fa4132987102c51c110751d8bdb8a74aeb7b071b
Local Mods: 1
USB Interfaces: MSD, CDC, HID
Interface CRC: 0xe369fb16
```

## La console du micro:bit

Quand le micro:bit est connecté à Thonny, il est possible d'exécuter des commandes Python par l'interprète MicroPython qui est installé dans le micro:bit.

La console affiche la version qui est actuellement installé.

```bash
MicroPython v1.9.2-34-gd64154c73 on 2017-09-01; micro:bit v1.0.1 with nRF51822
Type "help()" for more information.
```

Comme indiquez, entrons la commande help() pour obtenir:

```text
Welcome to MicroPython on the micro:bit!

Try these commands:
display.scroll('Hello')
running_time()
sleep(1000)
button_a.is_pressed()
What do these commands do? Can you improve them? HINT: use the up and down
arrow keys to get your command history. Press the TAB key to auto-complete
unfinished words (so 'di' becomes 'display' after you press TAB). These
tricks save a lot of typing and look cool!

Explore:
Type 'help(something)' to find out about it. Type 'dir(something)' to see what
it can do. Type 'dir()' to see what stuff is available. For goodness sake,
don't type 'import this'.

Control commands:
CTRL-C        -- stop a running program
CTRL-D        -- on a blank line, do a soft reset of the micro:bit
CTRL-E        -- enter paste mode, turning off auto-indent

For a list of available modules, type help('modules')

For more information about Python, visit: http://python.org/
To find out about MicroPython, visit: http://micropython.org/
Python/micro:bit documentation is here: https://microbit-micropython.readthedocs.io/
```

Les expressions que vous tapez maintenant dans la console sont maintenant exécuté dans le processeur du micro:bit et affiché dans la console de Thonny.

```python
>>> 1 + 2
3
```

Ou même un calcul plus conséquent

```python
>>> 12 ** 34
4922235242952026704037113243122008064
```

Dans la console de Thonny écrivez le code suivant

```python
>>> import microbit
>>> microbit.display.scroll('hello')
```

## Le module

La fonction `dir()` permet d'afficher les attributs et méthodes d'une objet.
Regardez les attributs qui font partie de

```python
>>> import microbit
>>> dir(microbit)
['__name__', 'Image', 'display', 'button_a', 'button_b', 'accelerometer', 'compass', 'i2c', 'uart', 'spi', 'reset', 'sleep', 'running_time', 'panic', 'temperature', 'pin0', 'pin1', 'pin2', 'pin3', 'pin4', 'pin5', 'pin6', 'pin7', 'pin8', 'pin9', 'pin10', 'pin11', 'pin12', 'pin13', 'pin14', 'pin15', 'pin16', 'pin19', 'pin20']
```

Nous pouvons afficher les méthodes de `microbit.display`

```python
>>> dir(microbit.display)
['get_pixel', 'set_pixel', 'show', 'scroll', 'clear', 'on', 'off', 'is_on', 'read_light_level']
```

## Premier programme

Dans l'éditeur Thonny, vous pouvez écrire

```python
import microbit
microbit.display.scroll('hello')
```

Avec cette façon d'importer le module, vous devez précéder toutes les éléments importé depuis le module `microbit` avec la notation `microbit.`.

Une autre façon vous permet d'importer toutes les éléments et de pouvoir les appeler tel quel.

```python
from microbit import *
display.scroll('Hello, World!')
```

```{image} scroll-hello1.gif
:width: 300px
```

## Afficher une image

Le micro:bit peut afficher des images 5x4 pixels.
Pour faciliter l'affichage, toute une série d'images simple sont prédéfinis.

Vous les trouvez avec

```python
dir(Image)
````

Le programme suivant affiche un smiley

```python
from microbit import *
display.show(Image.HAPPY)
```

```{image} happy.png
:width: 300px
```

Vous pouvez également créer vos propres image avec le constructeur de classe `Image`, en indiquant la valeur des 25 pixels. L'intensité de la lumière est donnée par une valeur de 0 (noir) à 9 (maximum).

```python
from microbit import *

maison = Image('00500:'
            '05050:'
            '50005:'
            '50705:'
            '55755')

display.show(maison)
```

Essayez de créer autre image

```python
pomme = Image('05050:50505:50005:50005:05550')
```

## The Zen of MicroPython

Comme Pyhton, MicroPython aussi a un *Easter egg*. Tapez `ìmport this` à la console et exécutez la commande. 
La machine va répondre avec le Zen de MicroPython.

```python
>>> import this
The Zen of MicroPython, by Nicholas H. Tollervey

Code,
Hack it,
Less is more,
Keep it simple,
Small is beautiful,

Be brave! Break things! Learn and have fun!
Express yourself with MicroPython.

Happy hacking! :-)
```
