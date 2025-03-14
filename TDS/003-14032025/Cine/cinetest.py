from cine import SalleCinema
# Exemple d'utilisation
if __name__ == "__main__":
    salle = SalleCinema("L'Enfant", 60, 9.5)
    print(salle)
    salle.vendre_places(20, False)
    salle.vendre_places(14, True)
    print(salle)
    print(f"Chiffre d'affaires : {salle.chiffre_affaires():.2f} €")
    print(f"Taux de remplissage : {salle.taux_remplissage():.2f} %")
    salle.remise_a_zero()
    print(salle)