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