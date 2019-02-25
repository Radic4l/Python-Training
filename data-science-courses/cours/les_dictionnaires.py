# Les dictionnaires par rapport au liste


# exemple : deux liste sont necessaire si je veux afficher le score de mes eleves

students = ["Serge","Paul","Bertrand","John"]
scores = [12, 8, 11, 15]

index = [0, 1, 2, 3]
name = "Bertrand"
score = 0

for i in index:
    if students[i] == name:
        score = scores[i]

print(score)

# voici maintenant comment fonctionne un dictionnaire.

dic_students = {"Serge":12,"Paul":8} # creation d'un dictionnaire avec deux cles / valeurs
# ajout de nouvelles cles /valeurs au dictionnaire
dic_students["Bertrand"] = 11
dic_students["John"] = 15
dic_students["Paul"] = dic_students["Paul"] + 8
dic_students["Serge"] = 10

john_found = 'John' in dic_students
matt_found = 'Matt' in dic_students

print(john_found)
print(matt_found)
print(dic_students)

# La condition if / else

# le if
temperature = 30

if temperature > 40:
    print('il fait chaud !')
if temperature <= 40:
    print('Il fait froid !')

# le if else: solution beaucoup plus souple que deux if
if temperature > 40:
    print('Il fait chaud !')
else:
    print('Il fait froid !')

temperatures = [50,18,39,78,12,40]

hight_temperatures =[]
low_temperatures = []

for temp in temperatures:
    if temp > 40:
        hight_temperatures.append(temp)
    else:
        low_temperatures.append(temp)

print(hight_temperatures)
print(low_temperatures)

# Compter les elements d'une liste et presenter le resultat dans cun dictionnaire

fruits = ["Citron", "Banane", "Pomme", "Pomme", "Pomme","Banane"]

fruits_counts = {}

for item in fruits:
    if item in fruits_counts:
        fruits_counts[item] = fruits_counts[item] + 1
    else:
        fruits_counts[item] = 1
print(fruits_counts)
