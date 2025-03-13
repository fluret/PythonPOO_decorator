from personnages import Personnage

monstre = Personnage(130, 100)
for i in range(3):
    monstre.perd_vies(10)

print(monstre.donne_etat())