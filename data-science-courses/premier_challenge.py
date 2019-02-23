# Ouvrir de nouveau le fichiers departements-fr.csv puis creer une liste d'entiers contenant le nombre d'habitants de tout les departements français.

data = open("sources/departements-fr.csv")
print(data)

read_data = data.read()
#print(read_data)

rows = read_data.split('\n')

final_data = []
for row in rows:
    split_row = row.split(',')
    final_data.append(split_row)

print(final_data)
nombres_habitants = []

for row in final_data:
    habitants = row[1]
    nombres_habitants.append(int(habitants))

print(nombres_habitants)