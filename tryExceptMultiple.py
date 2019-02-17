numerateur = 10
# denominateur = 0
# denominateur = 'toto'
try:
    resultat = numerateur / denominateur
    print(resultat)
except ZeroDivisionError:
    print('Division par zero impossible')
except TypeError:
    print('Une des deux variable n\'est pas un nombre')
except NameError:
    print('Une variable n\'a pas ete declaree')