class employer():
    def __init__(self, id=10, prenom='Inconnu',nom='Inconnu'):
        self.id = id
        self.prenom = prenom
        self.nom = nom

premier_employer = employer(id=0, nom="Marchand",prenom="Julie")
deuxieme_employer = employer(id=1,nom="Passant",prenom="Manue")
troisieme_employer = employer(id=2,prenom="John")

print(premier_employer.nom)
print(deuxieme_employer.nom)
print(troisieme_employer.nom)