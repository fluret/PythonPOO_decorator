class supp_example:
    def __init__(self, nom):
        self.nom = nom
        
    def supp_instance(self):
        del self

b = supp_example("test")

print(b.nom)

b.supp_instance()

print(b.nom) # Should raise an error