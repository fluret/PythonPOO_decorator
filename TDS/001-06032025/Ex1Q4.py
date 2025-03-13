from personnages import Personnage

gollum = Personnage(127, 20)
etat_1 = gollum.donne_etat()
etat_1 = gollum.vie
print(etat_1)
gollum.perd_une_vie()
etat_2 = gollum.donne_etat()
print(etat_2)