class SalleCinema():
    def __init__(self, film, nb_places, prix_tn):
        self.film = film
        self.nb_places = nb_places
        self.prix_tn = prix_tn
        self.npv_t_normal = 0
        self.npv_t_reduit = 0
    def nb_places_disponibles(self):
        return self.nb_places - self.npv_t_normal - self.npv_t_reduit
    def vendre_places(self, nb, tarif_reduit):
        if nb > self.nb_places_disponibles():
            print("Plus de places disponibles")
        else:
            if tarif_reduit:
                self.npv_t_reduit += nb
                prix_a_payer = nb * self.prix_tn * 0.8
            else:
                self.npv_t_normal += nb
                prix_a_payer = nb * self.prix_tn
            print(f"Prix à payer: , {prix_a_payer:.2f}€")
    