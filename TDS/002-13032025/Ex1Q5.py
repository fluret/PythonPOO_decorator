from personnages import Personnage

def simul(a, n):
    p1 = Personnage(a, n)  
    p1.boire_potion()
    print(p1.donne_etat())

simul(127, 10)