class Ma_Classe():
    def __init__(self, id=0):
        self.id = id

premier = Ma_Classe(id=107)

print(isinstance(premier,Ma_Classe))

ma_liste = 'toto'
print(isinstance(ma_liste, str))

# isinstance() Pratique pour comprendre à quelle classe appartient la methode