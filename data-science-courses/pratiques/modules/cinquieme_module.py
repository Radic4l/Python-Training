# Training 5 / mettre le cours en pause

# Soit la liste weather_types = ["Pluis","Soleil","Nuage","Nuage-Pluie","Orage","Climat"]
# Créer la liste vide weather_type_found.
# Ecrire une boucle qui verifie la presence ou non des elements de weather_types dans la liste weather.
# Ajouter le resultat a la liste weather_type_found.
# Afficher le resultat.

weather = []
weather_data = []
weather_types = ["Pluie","Soleil","Nuage","Nuage-Pluie","Orage","Climat"]
weather_type_found = []


file = open("../../sources/madrid-weather-2016.csv")

data = file.read().split('\n')

for row in data[1:len(data)]:
    values = row.split(',')
    weather_data.append(values)

#print(weather_data)

for row in weather_data:
    weather.append(row[1])

print(weather)
print(weather_types)

for item in weather_types:
    found = item in weather
    weather_type_found.append(found)


print(weather_type_found)