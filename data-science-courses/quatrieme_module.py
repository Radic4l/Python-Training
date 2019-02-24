# Training 4 / mettre le cours en pause

# Utiliser des operateurs pour determiner des equivalences sur la variable departements (contenant tous les departements français):
# 1 equivalence entre le premier élément de departements et "Ain" ? assigner le resultat à la variable first_ain
# 2 equivalence entre le second element de departements et "Ain" ? assigner le resultat a la variable second_ain
# 3 equivalence entre le premier element de departements et le dernier ? assigner le resultat a la variable first_last
# 4 afficher les 3 resultats


file = open("sources/departements-fr.csv","r")
print(file)

data = file.read()
rows = data.split('\n')

departements = []
int_habitants = []

for row in rows:
    values = row.split(',')
    int_habitants.append(int(values[1]))
    departements.append(values[0])

print(departements)
print(int_habitants)

first_ain = (departements[0] == 'Ain')
second_ain = (departements[1] == 'Ain')
first_last = (departements[0] == departements[-1])
print(first_ain)
print(second_ain)
print(first_last)

# la variable int_habitants est une liste d'entier contenant le nombres d'habitants de tous les departements français. Realiser quelques comparaisons.

# 5 Evaluer si le premier element est plus qrand que 500000 habitants. assigner le resultat a la variable first_500000
# 6 Evaluer si le premier element est plus grand que 650000 habitants. assigner le resultat a la variable first_650000
# 7 Evaluer si le premier element est superieur ou egale au dernier element. assigner le resultat a la variable first_last_int
# 8 afficher les 3 resultats.

first_500000 = (int_habitants[0] > 500000)
first_650000 = (int_habitants[0] > 650000)
first_last_int = (int_habitants[0] >= int_habitants[-1])

print(first_500000)
print(first_650000)
print(first_last_int)

# determiner si le 6e element de la liste departement est egale a "Ardèche".
# 9 soit une variable result egale a 0 par defaut et a 1 si la condition est vraie.
# 10 afficher la variable result


result = 0
if departements[5] == "Ardèche":
    result = 1

print(result)

# Ecrire un morceau de code qui teste 2 conditions
# 11 une premiere condition qui teste si le premier element de int_habitants est superieur a 600000 habitants.
# 12 une seconde qui teste que le second element de int_habitants est superieure a 300000 habitants.
# 13 si les 2 elements sont vrais assigner True a la variable both_conditions ( variable initialement egale a False)
both_conditions = False
if int_habitants[0] > 600000:
    if int_habitants[1] > 300000:
        both_conditions = True

print(both_conditions)