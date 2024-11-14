class Livre:
    cmp = 0
    def __init__(self,titre,auteur):
        Livre.cmp += 1
        self.id = Livre.cmp
        self.titre = titre
        self.auteur = auteur
        self.disponible = True
    
    def emprunter(self):
        self.disponible = False
    
    def retourner(self):
        self.disponible = True

    def afficherInfos(self):
        print(f"id : {self.id}")
        print(f"titre : {self.titre}")
        print(f"auteur : {self.auteur}")
        print(f"disponible : {self.disponible}")