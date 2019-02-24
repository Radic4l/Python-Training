# Training 2 / mettre le cours en pose.

# 1 Soit la liste countries = ["France","Spain","Russian","Canada","Australia","Argentina"]
# 2 Soit la liste temperatures = [122.5,124.0,95.7,105.2,112.5,128.3]
# 3 Sélectionner les 3 premières valeurs de la variable countries et assigner le résultat à la variable countries_slice.
# 4 Sélectionner les 4 dernières valeurs de temperatures et assigner le résultat à la variable temperatures_slice
# 5 Afficher les résultats.

#1
countries = ["France","Spain","Russian","Canada","Australia","Argentina"]
#2
temperatures = [122.5,124.0,95.7,105.2,112.5,128.3]
#3
countries_slice = countries[0:3]
#4
temperature_slice = temperatures[len(temperatures)-4:]
#5
print(countries_slice)
print(temperature_slice)
