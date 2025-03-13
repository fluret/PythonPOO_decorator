from personnages import Personnage
from random import randint

gollum = Personnage(127, 100)
bilbon = Personnage(127, 100)
nb_attaques = 0
attaquant = randint(0,1)

while gollum.donne_etat() > 0 and bilbon.donne_etat() > 0:
    if attaquant == 0:
        gollum.perd_vies(10)
        nb_attaques += 1
    else:
        bilbon.perd_vies(10)
        nb_attaques += 1
    attaquant = (attaquant + 1) % 2

print(nb_attaques)
print(f'Gollum a {gollum.donne_etat()} points de vie')
print(f'Bilbon a {bilbon.donne_etat()} points de vie')