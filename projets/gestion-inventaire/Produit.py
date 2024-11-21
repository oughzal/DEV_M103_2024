class Produit:
    cmp = 0
    def __init__(self,nom,Qt,prix):
        Produit.cmp += 1
        self.id = Produit.cmp
        self.nom = nom
        self.quantity = Qt
        self.prix = prix

    def afficherInfo(self):
        print(f"id : {self.id}")
        print(f"nom : {self.nom}")
        print(f"Quantité : {self.quantity}")
        print(f"prix : {self.prix}")

    def __str__(self): # toString
        return f'{self.nom} ({self.prix}dh)'
    
    def ajouterQuantite(self,Qt):
        if Qt >0 :
            self.quantity += Qt
    
    def retirerQuantite(self,Qt):
        if self.quantity >= Qt:
            self.quantity -= Qt
        
    

if __name__ == "__main__":
    p = Produit("Lait",1000,3)
    print(p)