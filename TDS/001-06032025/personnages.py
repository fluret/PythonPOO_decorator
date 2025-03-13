class Personnage:
    def __init__(self, age, nb_vies=20):
        self.vie = nb_vies
        self.age = age
    
        
    def perd_une_vie(self):
        self.vie -= 1
    
    def donne_etat(self):
        return self.vie
    
    def boire_potion(self):
        self.vie += 1