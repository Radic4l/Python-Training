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

print(names_list[:10])
