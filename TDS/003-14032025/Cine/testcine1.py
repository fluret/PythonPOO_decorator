from cines import SalleCinema

s1 = SalleCinema("Le seigneur des anneaux", 100, 10)

print(s1.nb_places_disponibles())
s1.vendre_places(10, False)
print(s1.nb_places_disponibles())
s1.vendre_places(10, True)
print(s1.nb_places_disponibles())
s1.vendre_places(90, False)
print(s1.nb_places_disponibles())
s1.vendre_places(80, False)
print(s1.nb_places_disponibles())