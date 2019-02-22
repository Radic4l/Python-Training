# Training 1 / mettre le cours en pose.

# 1 Créer une liste vide qu'on nommera countries.
# 2 Créer une liste vide qu'on nommera temperature.
# 3 Ajouter dans la liste countries les 3 pays suivants. France, Spain, Canada
# 4 Ajouter dans la liste temperature les températures correspondantes 122.5, 124.0 et 105.2 (dans l'ordre).
# 5 Assiger les valeurs des listes countries et temperature correspondant à la France, assigner les dans les variable france et france_temperature
# 6 Afficher france et france_temperature.

#1
countries = []
#2
temperature = []
#3
countries.append("France")
countries.append("Spain")
countries.append("Canada")
print(countries)
#4
temperature.append(122.5)
temperature.append(124.0)
temperature.append(105.2)
print(temperature)
#5
france = countries[0]
france_temperature = temperature[0]
#6
print(france)
print(france_temperature)