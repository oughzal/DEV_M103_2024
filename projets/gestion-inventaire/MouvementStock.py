from datetime import date
class MouvementStock:
    cmp = 0

    def __init__(self,produit,typeMouvement,Qt):
        MouvementStock.cmp += 1
        self.id = MouvementStock.cmp
        self.produit = produit
        self.type = typeProduit
        self.Qt = Qt
        self.date = date().today()
    
    def afficherInfo(self):
        print(f"produit : {self.produit}")
        print(f"type : {self.type}")
        print(f"Quatité : {self.Qt}")
        print(f"date : {self.date}")
    
    def __str__(self):
        return f"{self.produit}\t{self.type}\t{self.Qt}\t{self.date}"



