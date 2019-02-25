# Training 5 / mettre le cours en pause

# soit une liste planet_names = ["Mercure","Vénus","Terre","Mars","Jupiter","Saturne","Neptune","Uranus"]
# Creer deux listes vides long_names et short_names.
# Ecrire une boucle qui ajoute les planetes composes de plus de 5 lettres a long_names ou sinon qui ajoute les autres planetes a la liste short_names
# Afficher les deux liste

planet_names = ["Mercure","Vénus","Terre","Mars","Jupiter","Saturne","Neptune","Uranus"]
long_names = []
short_names = []

for planet in planet_names:
    if len(planet) > 5:
        long_names.append(planet)
    else:
        short_names.append(planet)

print(short_names)
print(long_names)