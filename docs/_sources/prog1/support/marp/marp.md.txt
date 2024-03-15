---
marp: true
theme: gaya
paginate: true
header: Représentation de l'information
footer: Modulo
---
# Marp presentation
<!-- _paginate: false -->
<!-- _header: ''-->
<!-- _footer: ''-->

## Markdown presentation ecosystem

- écrire en Markdown
- exporter en PDF, HTML et PowerPoint

---

# Comment créer des slides

- écire en Markdown
- découper les slides avec (`---`). 
- présenter ! :satisfied:

```markdown
# Slide 1

texte

---

# Slide 2

texte
```

---


# Claude Shannon

1916-2001

Pendant la Seconde Guerre mondiale, Claude Shannon travaille pour les services secrets de l’armée américaine, en cryptographie.

C’est ce qui le mènera par la suite à développer une mesure mathématique de la **quantité d’information** contenue dans un message.

![bg left](claudeshannon.jpg)

----

# Cuneiforme

- Sumériens
- écriture cunéiforme

![bg left fit](cuneiform.jpg)

---

# Morse

- inventé par Samuel Morse
- les symboles les plus court pour les lettres les plus fréquents
- transmission par 1 seul fil

![bg right fit](morse.png)

---

# Formules mathématiques

Formule de Pythagore

$$ a^2 + b^2 = c^2 $$

Somme

$$ \sum_i^{n} \frac{1}{1 + i} $$

---

# Images

![height:400 px](camera_obscura.jpg)

---

# Capture d'image

![](captimage.png)

---

# Code

    liste = [4, 12, 43, 12]

    a = 0
    for element in liste:
        a = a + element

Explication
1. mettre à zéro une variable **accumulateur** `a`
1. boucler **pour chaque élémment** de la liste
1. additionner cet élément à l'acumulateur
