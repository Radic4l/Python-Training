class Employer():
    def __init__(self):
        self.salaireHoraire = 20

class Ingenieur(Employer):
    def __init__(self, prenom):
        Employer.__init__(self)
        self.prenom = prenom

julie = Ingenieur('Julie')
print(julie.prenom + " Possede un salaire de " + str(julie.salaireHoraire) + " Euros de l'heure")
