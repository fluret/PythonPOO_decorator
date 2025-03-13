from personnages import Personnage
gollum = Personnage(nb_vies=15, age=100)
gollum.perd_vies(2)
print(gollum.donne_etat())