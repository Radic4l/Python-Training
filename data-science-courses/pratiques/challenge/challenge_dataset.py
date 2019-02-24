# Challenge dataset: prenom unisex aux Etats-Unis

## Mode d'emplois

### Pratiquer la datascience
### probleme structure et encadre
### cas reel dataset des prenoms unisex aux Etats-Unis

# Enonce

## Lire le fichier 'unisex-names.csv'
## Assigner cette chaine de caractere a la variable names.
## Convertire names en liste (methode split())
## Assigner le resultat a la variable names_list.
## Afficher les 10 premiers elements de names_list.

# Lire le fichier dans une liste

# preparation
file = open("../../sources/unisex-names.csv", "r")
# print(file)
# simplification au lieu de split names dans names_liste je le fais directement à la lecture
names_list = file.read().split('\n')

#print(names_list[:10])

# Enonce
## Creer une liste vide names_data
## Ecrire une boucle qui convertit notre liste en liste de listes

names_data = []
for row in names_list:
    value = row.split(',')
    names_data.append(value)

#print(names_data)

# Enonce
## Creer une nouvelle liste numerical_list
## Ecrire une boucle qui convertit les 'nombres' en nombres decimaux

numerical_list = []
for row in names_data:
    name = row[0]
    count = float(row[1])
    temp_list = [name,count]
    numerical_list.append(temp_list)

print(numerical_list)
print(len(numerical_list))
# Enonce
## Creer une liste vide final_list
## Ecrire une boucle qui conserve seulement les prenoms partagés par au moins 1000 personnes
## Afficher les 10 premiers elements de final_list

final_list = []
for line in numerical_list:
    if line[1] >= 1000:
        final_list.append(line[0])

print(final_list[:10])
print(len(final_list))