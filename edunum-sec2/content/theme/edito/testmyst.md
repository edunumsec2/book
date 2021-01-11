# test myst

````{seealso} Important
Ceci est une information à checker
````


````{note}
The next info should be nested
```{warning}
Here's my warning
```
````


```{code-block} python
---
lineno-start: 10
emphasize-lines: 1, 3
caption: |
    This is my
    multi-line caption. It is *pretty nifty* ;-)
---
a = 2
print('my 1st line')
print(f'my {a}nd line')
```

````{versionadded} v.2
Ceci est une information à checker
````

.. versionadded:: 2.5
   The *spam* parameter.


```{warning}
```

```{admonition} My title
:class: tip
My content
```

```{admonition} My title
:class: warning
My content
```

```{admonition} My title
:class: seealso
My content
```

:::{admonition,dropdown,warning} Click here!
Here's what's inside!
:::

````{sidebar} **My sidebar title**
```{note}
here is a note in the margin
```
Here is my sidebar content, it is pretty cool!
````



![fishy](images/img1.png)


```{image} images/img1.png
:alt: titreimage1
:width: 200px
:height: 200px
:align: center
```

```{image} images/img2.jpeg
:alt: titreimage1
:width: 200px
:height: 200px
:align: center
```

```{image} images/img3.png
:alt: titreimage1
:width: 200px
:height: 200px
:align: left
```

```{image} images/img4.png
:alt: titreimage1
:width: 200px
:height: 200px
:align: right
```

```{figure} images/img4.png
---
height: 150px
name: figure-test
---
Ceci est un carré de Polybe
```