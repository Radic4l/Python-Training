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
except NameError as erreur:
    if 'numerateur' in str(erreur): # utilisation de str(message) pour python3 au lieu de erreur.message de python2
        print('Une variable numerateur n\'a pas ete declaree')
    elif 'denominateur' in str(erreur):
        print('La variable denominateur n\'a pas ete declarer')