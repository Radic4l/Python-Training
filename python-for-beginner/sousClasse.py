class Employer():
    def __init__(self):
        self.salaireHoraire = 20

class Ingenieur(Employer):
    def __init__(self, prenom):
        Employer.__init__(self)
        self.prenom = prenom

julie = Ingenieur('Julie')
print(julie.prenom + " Possede comme salaire de " + str(julie.salaireHoraire) + " Euros de l'heure")

print(isinstance(julie,Ingenieur)) # l'objet julie est elle une instance de la classe Ingenieur ? return true;
print(isinstance(julie,Employer))  # l'objet julie et elle une instance par ricochet de l'instance Employer ? return true;

print(issubclass(Employer,Ingenieur)) # est-ce que Employer est une sous-classe de la classe Ingenieur ? return false;
print(issubclass(Ingenieur,Employer)) # est-ce que Ingenieur est une sous-classe de la classe Employer ? return true;