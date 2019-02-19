from random import randint

amplitude = int(input('Entrez la range maximum du nombre a deviner: '))

nombre_a_deviner = randint(1, amplitude)
#print(nombre_a_deviner)

nombre_essais_input = int(input("Entrez le nombre d'essai(s) maximum: "))

nombre_essais = range(nombre_essais_input)

for i in nombre_essais:

    essai = int(input('Entrez un nombre ({0} essai): '.format(i + 1)))

    if essai < nombre_a_deviner:
        print('Le nombre a deviner est plus grand que {0}'.format(essai))
    elif essai > nombre_a_deviner:
        print('Le nombre a deviner est plus petit que {0}'.format(essai))
    elif essai == nombre_a_deviner:
        print('Bravo vous avez gagne en {0} essai(s)'.format(nombre_essais))
        break

if essai != nombre_a_deviner:
    print('Vous avez perdu')
    print('Le nombre a deviner etait: {0}'.format(nombre_a_deviner))

print('Fin du jeu')