options = ['pierre', 'feuille', 'ciseaux']

print('Choisissez entre:', *options)
choix = input('Faites votre choix: ')
while choix not in options:
    choix = input('Faites votre choix: ')
    
print('enfin !!')
    