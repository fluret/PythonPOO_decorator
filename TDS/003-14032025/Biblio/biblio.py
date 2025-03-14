class Bibliotheque():
    def __init__(self):
        self.livres = []
    def ajoute(self, livre):
        self.livres.append(livre)
    def inventaire(self):
        print("--------------------")
        print('Inventaire de la bibliothèque')
        print("--------------------")
        for livre in self.livres:
            print(livre)
    def supprime_livres_abimes(self):
        for livre in self.livres:
            if livre.etat == 0:
                self.livres.remove(livre)