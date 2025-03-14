class Livre():
    def __init__(self, titre, auteur, etat):
        self.titre = titre
        self.auteur = auteur
        self.etat = etat
    def __str__(self):
        texte = f'"Titre: ", {self.titre}\n'
        texte += f'"Auteur: ", {self.auteur}\n'
        if self.etat > 0:
            texte += f'"Etat: ", {self.etat}'
        else:
            texte += "Livre à supprimer"
        return texte
    def degrade(self):
        if self.etat >0:
            self.etat -= 1