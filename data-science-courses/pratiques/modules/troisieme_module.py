# Training 3 / mettre le cours en pose.

# 1 Lire le fichier "departements_fr.csv"
# 2 Assigner le resultat a la variable data
# 3 Afficher le resultat

# j'ouvre mon fichier en mode read et je l'assigne à ma variable data
data = open("../../sources/departements-fr.csv","r")
print(data)

# je lis mon fichier data
read_data = data.read()
#print(read_data)

# 4 Separer la chaine de caracteres contenue dans la variable data en prenant comme delimiteur'\n'.
# 5 stocker le resultat dans la variable rows
# 6 afficher les 5 premiers elements de rows

rows = read_data.split('\n')
#print(rows[:5])

# 7 Soit la variable ten_rows contenant les 10 premiers elements de la liste rows
# 8 Ecrire une boucle qui pour chaque elements de ten_rows applique la fonction print()

ten_rows = rows[:10]

#for row in ten_rows:
    #print(row)

# 9 Creer une liste vide final_data
# 10 Ecrire une boucle for qui
## 10.1 delimite les elements de la liste rows
## 10.2 ajoute chaque element a la liste final_data
# Afficher les 5 premiers elements de la liste final_data

final_data = []

for row in rows:
    splited_row = row.split(',')
    final_data.append(splited_row)

print(final_data[:5])

# 11 Creer une nouvelle liste departements_list qui contient tout les noms des departements de final_data

departements_list = []
for row in final_data:
    departement = row[0]
    departements_list.append(departement)

print(departements_list)