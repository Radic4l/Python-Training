class Employer():
    def __init__(self, id=10, prenom='Inconnu',nom='Inconnu'):
        self.id = id
        self.prenom = prenom
        self.nom = nom

    def changeId(self, nouveauId=0):
        self.id = nouveauId
        print('Le ID de {0} a ete modifie. nouvelle valeur: {1}'.format(self.prenom,self.id))

premier_employer = Employer(id=0, nom="Marchand", prenom="Julie")
deuxieme_employer = Employer(id=1, nom="Passant", prenom="Manue")
troisieme_employer = Employer(id=2, prenom="John") # Valeur de nom par defaut

print("\nId: " + str(premier_employer.id) + " Employer: \n" + "-- Nom: " + premier_employer.nom + "\n-- Prenom: " + premier_employer.prenom + "\n \n" +
    "Id: " + str(deuxieme_employer.id) + " Employer: \n" + "-- Nom: " + deuxieme_employer.nom + "\n-- Prenom: " + deuxieme_employer.prenom + "\n \n" +
    "Id: " + str(troisieme_employer.id) + " Employer: \n" + "-- Nom: " + troisieme_employer.nom + "\n-- Prenom: " + troisieme_employer.prenom + "\n \n")

premier_employer.changeId(nouveauId=1)
deuxieme_employer.changeId(nouveauId=0)

print("--------- Nouveaux Id: --------- \n")
print("Id: " + str(premier_employer.id) + " Employer: \n" + "-- Nom: " + premier_employer.nom + "\n-- Prenom: " + premier_employer.prenom + "\n \n" +
    "Id: " + str(deuxieme_employer.id) + " Employer: \n" + "-- Nom: " + deuxieme_employer.nom + "\n-- Prenom: " + deuxieme_employer.prenom + "\n \n" +
    "Id: " + str(troisieme_employer.id) + " Employer: \n" + "-- Nom: " + troisieme_employer.nom + "\n-- Prenom: " + troisieme_employer.prenom + "\n \n")