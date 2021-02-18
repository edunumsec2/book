# Du codage à la transmission

## L'alphabet ASCII

L'ASCII pour *American Standard Code for Information Interchange* est une norme de codage des caractères apparue dans les années 1960. 

En résumé, chacun des caractères de l'alphabet latin est représenté par un chiffre binaire sur 7 bits. 

L'exemple ci-dessous vous renvoie la valeur binaire du texte que vous écrivez. 

```{codeplay}
  
texte = input("Ton texte : ")

print("Le texte d'origine est : " + str(texte)) 
  
res = ' '.join(format(ord(i), 'b') for i in texte) 
  
print("Le texte en binaire est : " + str(res))

```

### L'ASCII Art

Dès l'introduction de l'encodage ASCII, et jusqu'à aujourd'hui, une pratique répandue dans les milieux informatiques est d'utiliser les caractères ASCII comme support de créativité artistique. Les caractères ont un poids minimal en code binaire, c'est donc une façon très efficace de transmettre une information visuelle. 

```{codeplay}
print ("""
  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$ /$$$$$$$ 
 /$$__  $$ /$$__  $$| $$  /$$/|_  $$_/| $$__  $$
| $$  \ $$| $$  \__/| $$ /$$/   | $$  | $$  \ $$
| $$$$$$$$|  $$$$$$ | $$$$$/    | $$  | $$$$$$$/
| $$__  $$ \____  $$| $$  $$    | $$  | $$____/ 
| $$  | $$ /$$  \ $$| $$\  $$   | $$  | $$      
| $$  | $$|  $$$$$$/| $$ \  $$ /$$$$$$| $$      
|__/  |__/ \______/ |__/  \__/|______/|__/      
                                           
""")
```

[Cet outil](https://www.patorjk.com/software/taag/#p=display&f=Small&t=Entrez%20votre%20texte) vous permet de transformer n'importe quel texte en ASCII. 

## Text-based games

À l'époque où les programmes s'exécutaient directement dans le terminal, sans être enrobés dans une interface graphique, beaucoup de jeux furent créés qui n'utilisaient que la fonction *print* des langages de programmation. 

```{codeplay}
import random 

print('Jouons ensemble directement dans la console. Choisis un gobelet et si la balle est sous le gobelet tu gagnes. Il y a dix gobelets et tu as un bandeau sur les yeux.')
print('Choisis un chiffre entre 1 et 10, ce sera ton choix de gobelet.')
userInput = input()
ballPlaceholder = random.randrange(1,10)

if int(userInput) == ballPlaceholder:
    print('Bravo, victoire!')
else: 
    print('Tu as perdu')
```

%%% Ajouter références text-based games plus solides

## La compression

À partir du moment où l'on possède un alphabet pour représenter les messages écrits en nombres binaires se pose la question de l'optimisation du nombre de bits dont on a besoin pour coder un message. Très tôt des chercheurs se sont penchés sur la question de l'équilibre entre lisibilité et poids du message. Il fallait garder le minimum vital d'information pour que le message soit lisible, tout en compressant au maximum pour optimiser le poids. 

L'une des meilleures solutions qui a été trouvée est celle d'un certain David Albert Huffman, qui a proposé de d'utiliser différentes longueurs de nombre binaires suivant que la lettre revenait plus ou moins souvent dans le message. 

L'important dans cette technique est de construire un code qui soit sensible au préfixe, c'est à dire que deux lettres différentes ne doivent pas pouvoir être confondues au fur et à mesure qu'on décode le message, sachant que tout l'intérêt d'une compression est de ne pas se donner un nombre fixe de bits pour représenter une lettre, qui nous permettrait de savoir qu'une lettre se termine toujours au bout de 7 bits (dans le cas du ASCII).

Voilà quoi ressemble l'arbre de Huffman pour la phrase "Salut ceci est un arbre de Huffman". Il a été généré [ici](http://huffman.ooz.ie/). On notera au passage qu'il n'est pas très utile d'utiliser un arbre de HUffman pour comprimer un message dont la redondance est très faible. Ca devient intéressant quand certains caractères apparaissent un grand nombre de fois dans des messages beaucoup plus longs. 

```{image} images/repinfo1/Huffman.png
```

Et voici un programme qui te donne une idée d'une implémentation d'un arbre de Huffman en Python. L'idée est simplement de t'amuser en écrivant des phrases qui seront ensuite découpées par rapport à la fréquences des lettres de ton message. Tu peux aussi écrire des messages comme "AAHJFHHDJJDJJJJJDHFHJDFJDHJFDJFHJDHFJDFH" et voir ce qui se passe. 


```{codeplay}

string = input('Ton texte : ')
===

class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))
```


## Le cryptage



<!-- import random 

print('Jouons ensemble directement dans la console. Choisis un gobelet et si la balle est sous le gobelet tu gagnes. Il y a dix gobelets et tu as un bandeau sur les yeux.')
print('Choisis un chiffre entre 1 et 10, ce sera ton choix de gobelet.')
userInput = input()
ballPlaceholder = random.randrange(1,10)

# Tu fixes le chiffre au premier jet de dé
# Ensuite tu donnes des indices plus petit ou plus grand
# Exercice suivant : tu choisis un nombre et le programme le recherche. 

if int(userInput) == ballPlaceholder:
    print('Bravo, victoire!')
else: 
    print('Tu as perdu') -->

<!-- 
    Pour Huffman : 
        
    # ajouter le texte en code non compressé
    # ajouter le code compressé
    # préciser qu'il faut transmettre le dictionnaire (pour un texte cout on ne gagne pas de place)


    Ajouter : 

    - Exercices qui confirment l'acquisition. 
 -->


```{codeplay}

import random

def trouve():
    print("Je pense à un nombre entre 1 et 10, lequel ?")
    number = random.randint(1, 10)
    found = False
    tries = 0
    while not found:
        tries += 1
        try: 
            candidate = int(input("Le nombre: "))
            if candidate < 1 or candidate > 10:
                print("Donne moi au moins un nombre entre 1 et 10...")
            elif candidate == number:
                print("Bravo!")
                if tries == 1:
                    print("Et du premier coup en plus !")
                elif tries >= 5:
                    print("Tout arrive !")
                break
            elif candidate < number:
                print("Ton nombre est trop petit, voyons !")
            else:
                print("Ton nombre est trop grand, non mais !")
        except:
            print("Ce n'est même pas un nombre!")
===
trouve()
```


```{codeplay}

def cherche():
    print("Penses à un nombre entre 1 et 10")
    print("S'il te plait, réponds à mes questions par <, > ou =.")
    print("Utilise < quand ton nombre est plus petit que celui "
          "que je propose, > quand il est plus grand, "
          "et = quand j'ai trouvé.")
    minimum = 1
    maximum = 10
    while True:
        if minimum > maximum:
            print("J'abandonne...")
            break
        candidate = (minimum + maximum) // 2
    	answer = input("Tu penses à " + str(candidate) + ", c'est bien ça ? ")
        if answer == "<":
            print("Oups, j'ai visé trop haut !")
            maximum = candidate - 1
        elif answer == ">":
            print("Mince, trop bas !")
            minimum = candidate + 1
        elif answer == "=":
            print("Ha ha, trop facile !")
            break
        else:
            print("J'ai pas bien compris...")
===
cherche()
```