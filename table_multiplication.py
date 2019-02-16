nombre = 5

continuer = 'o'

while continuer == 'o':

    nombre = int(input('Entrez un nombre: '))

    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(nombre, i, nombre * i))

    continuer = input('Voulez vous continuer ? o/n ')

print('Fin du script')