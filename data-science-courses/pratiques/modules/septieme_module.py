# Training 5 / mettre le cours en pause

# Repprendre notre liste weather qui contient tout les climats de Madrid sur l'annee 2016
# Creer un dictionnaire vide weather_counts
# compter combien de fois chaque climat apparait dans la liste weather
# A la fin. le dictionnaire weather_count doit contenir les differents climats de Madrid en 2016 avec leur frequence sur 365 jours.
# Afficher le resultat

weather = []
weather_data = []
weather_count = {}

file = open("../../sources/madrid-weather-2016.csv","r")

data = file.read().split('\n')

for row in data[1:len(data)]:
    values = row.split(',')
    weather_data.append(values)

#print(weather_data)

for row in weather_data:
    weather.append(row[1])

#print(weather)
for item in weather:
    if item in weather_count:
        weather_count[item] += 1
    else:
        weather_count[item] = 1

print(weather_count)
