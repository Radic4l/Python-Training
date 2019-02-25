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