class ma_classe():
    def __init__(self, id=0):
        self.id= id

premier = ma_classe(id=5)
deuxieme = ma_classe(id=10)

print(premier.id)
print(deuxieme.id)


class Voiture():
    def __init__(self, couleur = "Noir"):
        self.couleur = couleur


premiere_voiture = Voiture(couleur="rouge")
deuxieme_voiture = Voiture()

print(premiere_voiture.couleur)
print(deuxieme_voiture.couleur)