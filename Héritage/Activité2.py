class Employe:
    def __init__(self,id,nom):
        self.id = id
        self.nom = nom
    def travailler(self):
        print("Je travaille")

class Vendeur(Employe):
    def __init__(self,id,nom,rayon):
        super().__init__(id,nom)
        self.rayon = rayon

    def vendre(self):
        print("Je vends")

class Docteur(Employe):
    def __init__(self,id,nom,specialite):
        super().__init__(id,nom)
        self.specialite = specialite

    def soigner(self):
        print("Je soigne")
