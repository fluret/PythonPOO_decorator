class Article:
    # Attribut statique pour le taux de TVA
    taux_tva = 20

    def __init__(self, reference=0, designation="", prix_ht=0):
        self._reference = reference
        self._designation = designation
        self._prix_ht = prix_ht

    # Propriétés pour accéder aux attributs
    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, value):
        self._reference = value

    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, value):
        self._designation = value

    @property
    def prix_ht(self):
        return self._prix_ht

    @prix_ht.setter
    def prix_ht(self, value):
        self._prix_ht = value

    # Méthode pour calculer le prix TTC
    def calculer_prix_ttc(self):
        return self._prix_ht + (self._prix_ht * Article.taux_tva / 100)

    # Méthode pour afficher les informations de l'article
    def afficher_article(self):
        print(f"Référence : {self._reference}")
        print(f"Désignation : {self._designation}")
        print(f"Prix HT : {self._prix_ht}")
        print(f"Le prix TTC est {self.calculer_prix_ttc()}")