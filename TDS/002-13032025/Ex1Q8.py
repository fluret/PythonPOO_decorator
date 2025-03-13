from personnages import Personnage

monstre = Personnage(130, 100)

cpt = 0
while monstre.donne_etat() > 0:
    monstre.perd_vies(10)
    cpt += 1

#print(monstre.donne_etat())
print(f'Le monstre a perdu en {cpt} attaques')
monstre.donne_etat()
print(monstre)
del monstre
monstre.donne_etat()