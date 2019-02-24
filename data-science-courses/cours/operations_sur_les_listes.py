
# je prepare ma liste de listes et je supprime l'entête

weather_data = []

file = open("../sources/madrid-weather-2016.csv")

data = file.read().split('\n')

for row in data[1:len(data)]:
    values = row.split(',')
    weather_data.append(values)

print(weather_data)

for row in weather_data:
    if 'Soleil' in row:
        #print('Soleil found !')
        pass

test = ['Bob','Jean','Richard']

found_bob = 'Bob' in test
not_found_steve = '6' in test

print(found_bob)
print(not_found_steve)

weather = []

for row in weather_data:
    weather.append(row[1])

print(weather)