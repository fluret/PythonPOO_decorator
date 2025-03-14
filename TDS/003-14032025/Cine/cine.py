class SalleCinema:
    def __init__(self, film, nb_places, prix_tn):
        self.film = film
        self.nb_places = nb_places
        self.prix_tn = prix_tn
        self.npv_t_normal = 0
        self.npv_t_reduit = 0

    def nb_places_disponibles(self):
        return self.nb_places - (self.npv_t_normal + self.npv_t_reduit)

    def vendre_places(self, nbre, tarif_reduit):
        if nbre > self.nb_places_disponibles():
            print("Erreur : Nombre de places demandées supérieur au nombre de places disponibles.")
        else:
            if tarif_reduit:
                self.npv_t_reduit += nbre
                prix_a_payer = nbre * (self.prix_tn * 0.8)
            else:
                self.npv_t_normal += nbre
                prix_a_payer = nbre * self.prix_tn
            print(f"Prix à payer : {prix_a_payer:.2f} €")

    def remise_a_zero(self):
        self.npv_t_normal = 0
        self.npv_t_reduit = 0

    def chiffre_affaires(self):
        return (self.npv_t_normal * self.prix_tn) + (self.npv_t_reduit * self.prix_tn * 0.8)

    def taux_remplissage(self):
        total_vendu = self.npv_t_normal + self.npv_t_reduit
        return (total_vendu / self.nb_places) * 100

    def __str__(self):
        return (f"Film joué : {self.film}\n"
                f"Nombre de places : {self.nb_places}\n"
                f"Prix d'une place : {self.prix_tn} € (tarif normal), {self.prix_tn * 0.8} € (tarif réduit)\n"
                f"Places vendues au tarif normal : {self.npv_t_normal}\n"
                f"Places vendues au tarif réduit : {self.npv_t_reduit}")
