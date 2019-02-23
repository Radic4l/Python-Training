# Training 3 / mettre le cours en pose.

# 1 Lire le fichier "departements_fr.csv"
# 2 Assigner le resultat a la variable data
# 3 Afficher le resultat

# j'ouvre mon fichier en mode read et je l'assigne à ma variable data
data = open("sources/departements-fr.csv","r")
print(data)

# je lis mon fichier data
read_data = data.read()
#print(read_data)

# 4 Separer la chaine de caracteres contenue dans la variable data en prenant comme delimiteur'\n'.
# 5 stocker le resultat dans la variable rows
# 6 afficher les 5 premiers elements de rows

rows = read_data.split('\n')
print(rows[:5])