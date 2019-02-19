import time

def printHeure():
    heureActuelle = time.localtime().tm_hour
    print('Il est {0}h'.format(heureActuelle))