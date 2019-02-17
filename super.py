class Employe(object):
    def __init__(self):
        self.salaireHoraire = 20

class Ingenieur(Employe):
    def __init__(self, prenom):
        # Employe.__init__(self) Utilise plutot la classe super !
        super(Ingenieur, self).__init__() # Ici plutôt que specifier le nom de la classe don on herite on met le nom de la classe elle meme
        # super va donner le meme resultat que la ligne commenter au dessus
        self.prenom = prenom

julie = Ingenieur('Julie')
print(julie.salaireHoraire)

# La fonction super est utiliser pour appeller le constructeur de la classe de laquelle on herite.
# Utile si jamais on veux changer le nom d'une classe sans avoir besoin de tout renommer