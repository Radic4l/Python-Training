class Employe():
    def __init__(self):
        self.salaireHoraire = 20

    # def printSalaire(self):
    #   print('Le salaire de base et de {0}$/h'.format(self.salaireHoraire))

class Ingenieur(Employe):
    def __init__(self,prenom):
        Employe.__init__(self)
        self.prenom = prenom

    def redefinirSalaire(self, nouveauSalaire):
        self.salaireHoraire = nouveauSalaire

    # def printSalaire(self)
    #   print('Le salaire de {0} est de {1}$/h'.format(self.prenom,self.salaireHoraire))

julie = Ingenieur('Julie')
print(julie.salaireHoraire)
julie.redefinirSalaire(25)
print(julie.salaireHoraire)
tom = Ingenieur('Tom')
print(tom.salaireHoraire)